---
id: meta-cost-aware-agentic-feature-optimization-fleet-ranking
title: "Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models"
source: "Meta (arXiv cs.IR)"
url: "https://arxiv.org/abs/2611.26531"
published: "2026-11"
added: "2026-11-20"
category: ml-infra-serving
tags: [feature-selection, llm-agents, ads-ranking, pareto-optimality, shapley, cost-aware-ml, multi-task, a-b-testing]
novelty: 3
sourced_via: "full-text fetch"
---

# Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models

**Source:** [Meta (arXiv cs.IR)](https://arxiv.org/abs/2611.26531) · Published 2026-11 · Added 2026-11-20
**Category:** ML Infrastructure & Serving · **Tags:** `feature-selection`, `llm-agents`, `ads-ranking`, `pareto-optimality`, `shapley`, `cost-aware-ml`, `multi-task`, `a-b-testing`

## TL;DR

Meta describes an agentic system that re-selects features for a fleet of ads ranking models under per-model serving caps and shared pipeline-cost budgets. A fleet-wide fine-tuned LLM proposes cross features, and several importance estimators rank them. Pareto-front blending combines the rankings across tasks, and an LLM 'Researcher' runs 10–25 asynchronous trials. Deterministic tools train, measure and verify, and the winner rule is fixed in advance. Reported gains are −0.31% NE on average across seven models, −2.3% pipeline cost from trimming, and +0.20% on a primary online metric in A/B tests.

## 1. Business context

Large platforms run many ranking models that draw features from a shared pool of tens of thousands. Each feature costs serving throughput, latency and memory, plus upstream processing, storage and logging. Feature sets are usually inherited from the incumbent model with manual additions. Costs are multi-dimensional and set-dependent (a feature another model already uses adds no pipeline cost), so top-k-by-importance is suboptimal.

## 2. Technical details

- **Feature creation.** Transforms t = (operator, feature subset), e.g. n-gram crosses, give a combinatorial space of tens of millions. A single retrieval LLM scores candidates from a fleet-wide Signal database for recall. Deterministic feature importance re-ranks for precision. The FI outcomes continually fine-tune the shared LLM, so creation improves as more models are optimized.
- **Feature ranking.** Permutation importance, Shapley value sampling, Kernel SHAP, and segment-aware variants trained and scored on high-value slices (e.g. top revenue buckets).
- **Blending.** Multi-task models are ranked by successive Pareto fronts across tasks, so no task weights are needed. A mixture π splits the N-feature budget across ranking sources, including the incumbent's ranking.
- **Search.** θ = (per-category volumes for dense/sparse/transform/embedding features, mixture π). Minimize normalized entropy subject to resource caps relative to the incumbent (e.g. 1.2× FLOPs). The LLM Researcher runs an observe–reason–act loop with greedy, exploration, evolutionary and recipe moves. A validator rejects bad proposals, and the winner is the lowest-NE trial within caps by a pre-set rule the LLM cannot override. Each trial takes hours to days, with K ≈ 10–25 trials and W ≈ 4–8 concurrent.
- **Trimming.** Enforces shared pipeline budgets before training. It removes costly additions and refills each slot with an already-used feature of the same category.

## 3. Impact — potential & realized

**Measured:**
- 25-trial frontier on a 300/100/30/30 baseline: from +1.47% NE at 1.10× QPS to −1.08% NE at 0.77× QPS. Only volumes were tuned; mixture tuning is not yet evaluated.
- A production conversion model: a recipe that doubled embeddings and cut sparse features by 14% gave −0.17% NE, where pure scale-ups were flat or worse.
- Seven high-impact models: −0.31% NE on average. Trimming: −2.3% attributed pipeline cost on average (up to 6.3%), with loss within +0.03%. Online A/B: +0.20% on a primary metric, over six months of launches.

**Potential:** A pattern for putting LLM agents into ML workflows safely: the agent proposes, deterministic tools verify, and pre-registered selection rules decide. It also applies directly to cost-aware feature governance.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Good production hygiene for agentic AutoML; the guardrail design is the transferable part

The DS lesson here is the separation of concerns. The LLM generates hypotheses, but measurement, constraint checks and the winner rule are deterministic and fixed in advance, which keeps the agent from 'p-hacking' its own search. The finding that rebalancing feature categories beats scaling them up echoes the Amazon window paper: the inherited configuration is often the binding constraint.

It is a short industry paper. NE gains are small and not given with uncertainty beyond a 0.03% significance threshold, the online metric is unnamed, and mixture tuning is unevaluated.

### Similar / related work

- [**Agentic ML Exploration (A-MLE) for Ads Ranking**](https://arxiv.org/abs/2609.08248) — Meta's earlier agent for end-to-end ads-ranking experimentation, cited as related work.
- [**Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems**](2026-11-11-meta-feature-invariant-scaling-laws-ab-experimentation-recsys.md) (in this bank) — another Meta piece on making feature/model iteration cheaper to evaluate.

### Jargon buster

- **Normalized entropy (NE)** — log loss divided by the entropy of the background click rate; lower is better, and small relative gains matter at ads scale.
- **Pareto front** — the set of features not beaten on every task by any other feature; taking fronts in order avoids hand-tuned task weights.
- **Cross feature** — a feature built by combining two or more ID features (e.g. country × ad category).
- **Kernel SHAP** — an approximation of Shapley-value feature attributions via a weighted linear regression over sampled feature subsets.
