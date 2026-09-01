---
id: linkedin-feed-sr-sequential-recommender
title: "An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking (Feed SR)"
source: "LinkedIn / arXiv"
url: "https://arxiv.org/abs/2602.12354"
published: "2026-02"
added: "2026-09-01"
category: search-ranking
tags: [sequential-recommender, transformer, rope, feed-ranking, scaling-laws, flash-attention, production-ab-test]
novelty: 5
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking (Feed SR)

**Source:** [arXiv](https://arxiv.org/abs/2602.12354) · Published 2026-02 · Added 2026-09-01
**Category:** Search & Ranking · **Tags:** `sequential-recommender`, `transformer`, `rope`, `feed-ranking`

## TL;DR

LinkedIn replaced its DCNv2-based Feed ranker with **Feed SR**, a
decoder-only transformer processing up to 1,000 historical impressions per
member, backed by custom GPU serving kernels. It beat both the legacy ranker
and a tested LLM-based alternative, delivering **+2.10% time spent** and
**+3.52% social actions** in a production A/B test — while using *less*
energy than the CPU-served incumbent, despite being a larger model.

## 1. Business context

LinkedIn Feed serves over 1.2 billion members, and the legacy production
ranker — DCNv2, a feature-cross architecture — has no native way to model a
member's long interaction history as an ordered sequence; it works from
aggregated feature crosses instead. LinkedIn built Feed SR to test whether a
transformer-based sequential ranker could do better, evaluating it not just
against the DCNv2 incumbent but against LLM-based ranking alternatives too,
all under real production latency and cost constraints — a much harder bar
than an offline-only comparison.

## 2. Technical details

- **Architecture.** A decoder-only transformer with pre-LayerNorm, **RoPE**
  positional embeddings, and "RescaleAndAdd" scaled residual connections
  (chosen over vanilla residual and ReZero variants — without pre-LN, AUC
  collapses to 0.5). It processes up to **1,000 historical impressions** per
  member, interleaving post and action embeddings before transformer
  encoding.
- **Scoring head.** A "parallel DCNv2" head applied after the transformer
  beat linear, MLP, stacked-DCNv2, and MMoE alternatives in ablations.
- **Feature engineering.** Roughly **80% feature reduction** versus the
  legacy ranker. Item-popularity and viewer-author-affinity signals mattered
  most (+2.5% Long Dwell AUC on their own); late-fusing numeric features
  instead of feeding them through the transformer cut training step time
  12% for a negligible 0.04% AUC cost.
- **Training.** Incremental daily retraining — loss computed only on new
  interactions, though full history is still fed as model input.
  Cold-start training runs on 16 H200 GPUs, warm-start on 8; fused AdamW
  with OneCycleLR. Within-session label randomization fixed a train/serve
  skew caused by correlated in-session labels.
- **Serving.** A disaggregated CPU (feature fetch) / GPU (inference) stack,
  with member histories stored as Arrow columnar buffers for zero-copy
  tensor conversion. "Shared context batching" scores roughly 512 candidates
  in a single forward pass (an 80x speedup on the transformer forward pass
  alone); a custom flash-attention CUDA kernel ("SRMIS") gives roughly 2x
  speedup over PyTorch's built-in SDPA. CPU-side history parsing sped up
  225x (450ms → 2ms); sparse-to-dense conversion sped up 50x.
- **Scaling behavior.** Long Dwell AUC improves roughly 0.0093 per
  order-of-magnitude increase in training FLOPs; sequence length scales
  quality better than model depth or embedding dimension.
- **Rejected alternatives.** An "LLM-Ranker" (a fine-tuned LLM ranking via
  text prompts) struggled with encoding numeric features and produced huge
  token sequences, and never beat the production baseline online. A
  TransAct-style history encoder improved offline metrics but was too
  latency-heavy and incompatible with the existing pointwise-scoring
  serving infrastructure.

## 3. Impact — potential & realized

- **Realized:** in a production A/B test against the prior DCNv2 ranker —
  **+2.10% time spent** (DAU +2.38%, WAU +1.84%) and **+3.52%**
  likes/comments/reshares (DAU +4.07%), with gains concentrated among active
  members and roughly neutral for new members. Feed SR has served the
  majority of LinkedIn Feed traffic for 3+ months at time of writing.
  Despite being a larger model, it uses roughly **0.2x the training energy**
  and **0.7x the inference energy** of the legacy CPU-served pipeline.
  Ablations: removing RoPE costs -0.19% Long Dwell AUC, no positional
  encoding at all costs -0.91%, a linear head instead of parallel-DCNv2
  costs -1.20%, and swapping in an HSTU-style architecture at matched
  compute costs -0.23%.
- **Potential:** a template combining sequential-transformer ranking with
  serious GPU-serving engineering (custom kernels, batching) for teams whose
  ranking systems are still CPU-served feature-cross models.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 5/5 — rare rigor and rare honesty for a production systems paper

This is an unusually numbers-dense industrial paper: real production A/B
results, energy-efficiency numbers, kernel-level engineering detail (a
custom flash-attention kernel, shared-context batching), and — notably —
honest negative results about the LLM-ranker and TransAct approaches that
were tried and didn't ship. That combination of production rigor and
candor about what didn't work is rare in a single write-up.

### Similar / related work

- [**How Generative Recommenders Are Redefining RecSys at Scale**](2026-09-01-nvidia-generative-recommenders-recsys-scale.md) (in
  this bank) — the same generative/sequential-recommender industry shift
  described at the tooling level, including HSTU, the architecture Feed SR
  explicitly tested and rejected at matched compute.
- [**Towards Generalizable and Efficient Large-Scale Generative
  Recommenders**](2026-09-01-netflix-generalizable-generative-recommenders.md) (in this bank) — a parallel scaling-law study for a
  similar sequential-recommender backbone at Netflix.
- [**From Models to Products: LLMs for Recommendation at Spotify
  Scale**](2026-08-31-spotify-neo-glide-llm-recommendation-grounding.md) (in this bank) — another production system that rejected the
  most literal "just use a big LLM" design in favor of a compact,
  purpose-built model, echoing Feed SR's LLM-Ranker rejection.

### Jargon buster

- **DCNv2 (Deep & Cross Network v2)** — a feature-crossing ranking
  architecture common in production recommenders before sequence models.
- **RoPE (Rotary Positional Embedding)** — a way of encoding token position
  by rotating embedding vectors, used in many modern transformers.
- **Flash attention** — a GPU-memory-efficient algorithm for computing
  attention without materializing the full attention matrix.
- **Long Dwell AUC** — a ranking-quality metric (area under the curve)
  evaluated against long-dwell-time engagement as the positive label.
