---
id: meta-adaptive-ranking-model-inference-scaling
title: "Meta Adaptive Ranking Model: Bending the Inference Scaling Curve for LLM-Scale Ads"
source: "Engineering at Meta"
url: "https://engineering.fb.com/2026/03/31/ml-applications/meta-adaptive-ranking-model-bending-the-inference-scaling-curve-to-serve-llm-scale-models-for-ads/"
published: "2026-03"
added: "2026-09-05"
category: ml-infra-serving
tags: [ads-ranking, fp8-quantization, model-system-codesign, inference-routing, mixture-of-experts, embedding-sharding]
novelty: 4
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Meta Adaptive Ranking Model: Bending the Inference Scaling Curve for LLM-Scale Ads

**Source:** [Engineering at Meta](https://engineering.fb.com/2026/03/31/ml-applications/meta-adaptive-ranking-model-bending-the-inference-scaling-curve-to-serve-llm-scale-models-for-ads/) · Published 2026-03 · Added 2026-09-05
**Category:** ML Infrastructure & Serving · **Tags:** `ads-ranking`, `fp8-quantization`, `model-system-codesign`, `inference-routing`, `mixture-of-experts`, `embedding-sharding`

## TL;DR

Meta replaced one-size-fits-all ranking inference with the Adaptive Ranking Model (ARM): intelligent per-request routing to appropriately-scaled models, combined with model-system codesign (selective FP8 quantization, custom kernels) and infrastructure that shards trillion-parameter embedding tables across GPU clusters — all to serve LLM-scale ads ranking within a bounded ~100ms latency budget.

## 1. Business context

Meta describes this as an "inference trilemma": ads ranking models were growing toward LLM-scale complexity (more parameters, longer user-behavior sequences, richer features) at the same time the service still needed sub-second latency and cost efficiency across billions of daily active users. Naively scaling up a single dense ranking model to LLM-scale parameter counts would blow both the latency budget and the infrastructure cost — the old assumption that "bigger model, same serving path" would work stops holding once model complexity crosses into LLM territory.

## 2. Technical details

ARM attacks the trilemma with three coordinated pieces:

- **Inference-efficient model scaling.** Rather than recomputing user-side signals independently for every ad candidate, the system shifts to request-centric computation: user signals and long behavior sequences are computed once per request centrally, then shared across candidates via "Request-Oriented Computation Sharing and In-Kernel Broadcast optimization." This also lets Top-K candidate selection drop from O(N log N) to O(N) complexity.
- **Model-system codesign ("Wukong Turbo").** Rather than blanket low-precision inference, FP8 quantization is applied selectively only to layers with high tolerance for precision loss, preserving accuracy where it matters while cutting compute elsewhere. Specialized kernels and operator fusion minimize memory movement, together reaching 35% Model FLOPs Utilization (MFU) across a heterogeneous hardware fleet.
- **Reimagined serving infrastructure.** A multi-card sharding mechanism splits massive embedding tables into segments distributed across an optimized hardware cluster, enabling roughly trillion-parameter ("O(1T)") scale models to load in under 10 minutes — a prerequisite for iterating on and deploying models of this size at all.

Together these let Meta route each request through an appropriately-scaled model rather than forcing every request through the same maximal-capacity path — "bending the curve" so that inference cost grows sub-linearly with model sophistication.

## 3. Impact — potential & realized

**Realized:** since launching on Instagram ads in Q4 2025, Meta reports a +3% increase in ad conversions and a +5% increase in ad click-through rate for targeted users, while holding inference latency to a bounded ~100ms even at LLM scale.

**Potential:** the request-centric computation-sharing pattern and selective-precision codesign generalize to any ranking system where the same expensive user-side computation is currently being wastefully repeated per-candidate — a common inefficiency in large-scale recommendation and ads systems well beyond Meta.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A strong, multi-layered systems answer to a real scaling wall

None of the individual techniques (selective quantization, computation sharing, embedding sharding) is brand new in isolation, but combining all three into a coherent "route requests through the right-sized model" system, with a concrete production A/B payoff at Meta's scale, is a genuinely strong piece of applied infrastructure engineering. It sits alongside Meta's other 2026 ads-ranking scaling work as evidence of a broader industry shift toward LLM-scale ranking models requiring LLM-grade serving infrastructure, not just bigger GPUs.

### Similar / related work

- [**From User Sequences to Scaling Laws: A Multi-Stage Architecture for Meta's Ads Ranking**](../articles/2026-08-31-meta-llatte-ads-ranking-scaling-laws.md) (in this bank) — Meta's companion piece on the modeling side of the same ads-ranking scaling problem this article addresses on the serving side.
- [**GEM Training: How Meta Doubled the Efficiency of Its LLM-Scale Ads Foundation Model**](../articles/2026-08-31-meta-gem-training-llm-scale-ads-efficiency.md) (in this bank) — the training-time efficiency counterpart (MFU, mixed precision, parallelism) to this article's inference-time efficiency story.
- [**SilverTorch: Index as Model**](../articles/2026-09-04-meta-silvertorch-index-as-model-retrieval.md) (in this bank) — another Meta infrastructure rethink (retrieval rather than ranking) built on the same theme of GPU-native, model-system-codesigned serving.

### Jargon buster

- **Model FLOPs Utilization (MFU)** — the fraction of a GPU's theoretical peak compute that a training or inference job actually achieves; higher MFU means less compute is wasted on overhead.
- **FP8 quantization** — running model computation in 8-bit floating point instead of the usual 16- or 32-bit, trading some numerical precision for large gains in speed and memory footprint, applied here only where the model can tolerate the precision loss.
