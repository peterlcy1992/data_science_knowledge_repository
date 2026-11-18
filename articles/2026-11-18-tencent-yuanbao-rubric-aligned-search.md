---
id: tencent-yuanbao-rubric-aligned-search
title: "From Relevance to Utility: Rubric Alignment in Yuanbao Search"
source: "Tencent (arXiv cs.IR, KDD 2027)"
url: "https://arxiv.org/abs/2611.22503"
published: "2026-11"
added: "2026-11-18"
category: search-ranking
tags: [agentic-search, rag, rubrics, set-level-utility, llm-labeling, distillation, grpo, dense-retrieval, online-ab-test]
novelty: 3
sourced_via: "full-text fetch"
---

# From Relevance to Utility: Rubric Alignment in Yuanbao Search

**Source:** [Tencent (arXiv cs.IR, KDD 2027)](https://arxiv.org/abs/2611.22503) · Published 2026-11 · Added 2026-11-18
**Category:** Search & Ranking · **Tags:** `agentic-search`, `rag`, `rubrics`, `set-level-utility`, `llm-labeling`, `distillation`, `grpo`, `dense-retrieval`, `online-ab-test`

## TL;DR

Tencent's AI search engine Yuanbao trains retrieval, ranking and document-set selection against one query-specific rubric (weighted "must contain" criteria and "must avoid" deductions) instead of per-document relevance. A distilled labeler turns the rubric into per-document utility labels for retrieval and ranking; a rubric-conditioned judge gives a set-level reward for an RL selector. In a 14-day online A/B test on 5% of traffic, the full pipeline lifted agent answer quality (GSB) by 8.52% over production.

## 1. Business context

In agentic search the user gets one LLM-synthesised answer, so answer quality is gated by the utility of the small document set fed to the model — coverage, no conflicts, trustworthiness — not by ranked-list relevance for a human scanning results. Prior work either defines evidence quality without training on it, or optimises the selection stage (e.g. generator-aware selectors) while leaving retrieval and ranking trained on relevance. Three obstacles: rubrics judge *sets* while retrieval/ranking must score documents independently; rubric labelling with strong LLMs is too costly at corpus scale; and a single set-level scalar gives sparse credit for RL.

## 2. Technical details

- **Rubric generation (coarse-to-fine).** Three LLMs (ChatGPT, Claude, GLM) answer the query with live web retrieval; criteria are extracted from the answers and merged into a coarse skeleton, then anchored to the production system's top-15 documents to produce specific sub-criteria, which pass a fact-verification gate against search evidence.
- **Utility labeler.** A Qwen3-235B teacher grades (query, document) pairs 0–3 against the rubric; a Qwen3-4B student is distilled by SFT and refined by GRPO with accuracy, pairwise-rank and format rewards.
- **Retrieval.** Qwen3-Embedding-0.6B dual encoder: in-domain contrastive pre-training on 610M production pairs (bidirectional InfoNCE, Matryoshka dims up to 768), then utility-aligned fine-tuning with labeler grades ≥2 as positives (other positives masked from negatives). Retrieves ~1,000 from a billion-scale corpus; served with product quantization.
- **Ranking.** Qwen3-4B ranker with four heads (utility, authority, freshness, quality), pairwise losses with auxiliary weight 0.5, focal reweighting (γ=2); only the utility head is used at inference, reordering to ~20 documents.
- **Selection.** Qwen3-7B-Instruct selector picks 3–8 documents; reward from a pointwise-ensemble judge (DeepSeek-V4-Flash) scoring subsets against the rubric. Dual-branch RL: above-mean rollouts go through GRPO; below-mean rollouts are instead distilled toward the best in-group rollout ("best-rollout distillation"), weighted by the reward gap.

## 3. Impact — potential & realized

**Online (5% traffic, ≈2.8M queries, 14 days; blind side-by-side human GSB on 1,000 sampled queries; paired t-test p<0.05):** rubric-aligned retrieval +0.40%, ranking +3.94%, selection +4.82% when each is added alone; full pipeline +8.52% (sum of individual lifts 9.16%). **Offline:** with rubrics, reward-model agreement with human set-level verdicts on 2,000 pairs rises from 68.7% to 79.3%; ablating negative criteria drops it to 72.8%, fine sub-criteria to 74.3%, multi-model generation to 77.7%, criterion weights to 79.0%. Labeler PNR 4.50 (SFT) → 4.67 (data optimisation) → 4.82 (RL). Retrieval Recall@1K gains of +11.2 to +14.2 points over the zero-shot encoder across four benchmarks (in-domain pre-training +5.1–8.6, utility fine-tuning a further +5.6–6.1); INT4 quantisation costs at most 0.87 points (not significant). Ranker PNR 3.807 → 3.959 (+4.0%). Selector rubric utility score 9.45 → 9.73 (+3.0%), with SFT supplying most of it (9.70) and GRPO alone (9.68) below SFT. The offline pipeline takes 1–2 weeks to train.

**Potential:** a template for aligning a whole retrieval stack to the downstream LLM's needs with one supervision signal.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Rubrics as the single source of truth, at production scale

Rubric-as-reward is established for LLM post-training; the contribution is pushing one rubric through every stage of a production search funnel and showing additive online gains. The measurement design deserves credit (component-wise A/Bs, blind GSB, rubric-vs-human agreement ablations), though GSB on 1,000 sampled queries is a human-preference metric with its own variance, and the rubric pipeline depends on several external frontier LLMs. The DS lesson: when the consumer of a ranked list changes (human → LLM), the label definition has to change with it.

### Similar / related work

- [**Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads**](2026-10-06-arxiv-agentic-rag-evaluation-budget-allocation.md) (in this bank) — how to spend evaluation budget for agentic RAG systems.
- [**Better Rankers, Worse Retrievers: The Hidden Cost of RL Post-Training in Generative Recommendation**](2026-11-18-arxiv-better-rankers-worse-retrievers-rl-generative-recommendation.md) (in this bank) — RL on a funnel stage evaluated at the wrong depth; a cautionary counterpart.
- [**Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains**](https://arxiv.org/abs/2507.17746) (RaR) — checklist-style rubrics as GRPO rewards, cited as prior work not yet applied to search pipelines.

### Jargon buster

- **Set-level utility** — how useful a *group* of documents is for answering, which depends on coverage and redundancy, not on each document alone.
- **GSB (Good-Same-Bad)** — blind side-by-side human comparison of treatment vs baseline answers, aggregated into a lift.
- **PNR (positive-negative ratio)** — the ratio of correctly to incorrectly ordered document pairs relative to labels.
- **Best-rollout distillation** — training below-average RL samples to imitate the best sample in their group rather than just pushing them down.
