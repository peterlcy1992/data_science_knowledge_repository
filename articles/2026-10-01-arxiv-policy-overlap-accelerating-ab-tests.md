---
id: arxiv-policy-overlap-accelerating-ab-tests
title: "Accelerating A/B-Tests with Counterfactual Estimation: Reducing Variance through Policy Overlap"
source: "arXiv (Olivier Jeunen)"
url: "https://arxiv.org/abs/2607.14604"
published: "2026-07"
added: "2026-10-01"
category: experimentation-causal
tags: [variance-reduction, off-policy-estimation, recsys-evaluation, ab-testing, delta-estimator]
novelty: 4
sourced_via: "web search"
---

# Accelerating A/B-Tests with Counterfactual Estimation: Reducing Variance through Policy Overlap

**Source:** [arXiv (Olivier Jeunen)](https://arxiv.org/abs/2607.14604) · Published 2026-07 · Added 2026-10-01
**Category:** experimentation-causal · **Tags:** `variance-reduction`, `off-policy-estimation`, `recsys-evaluation`, `ab-testing`, `delta-estimator`

## TL;DR

Jeunen observes that when treatment and control policies pick the same action, the outcome adds noise but no signal about the treatment effect. Treating randomisation as a meta-policy and applying Δ-off-policy estimators gives an unbiased estimator whose variance scales with policy divergence instead of raw outcome variance.

## 1. Business context

Recommender, retrieval and LLM-interface experiments often compare two policies that agree on most decisions, yet standard difference-in-means pays the full outcome variance, making tests slower than necessary.

## 2. Technical details

Randomised assignment is framed as a meta-policy over actions. Δ-Off-Policy Estimation methods (the full text mentions inverse propensity weighting and doubly robust variants) are applied to estimate the treatment effect from logged data. The paper shows the estimator recovers the standard A/B estimator in the general case but is strictly better whenever the policies share common support with non-zero residual variance. Stated limitations: overlap may be weak in practice, propensity estimation adds bias–variance trade-offs, and performance degrades when policies diverge substantially.

## 3. Impact — potential & realized

Reported: variance reductions on synthetic and semi-synthetic benchmarks that the retrieved full-text summary puts at roughly 40–70% depending on overlap (treat as approximate; I could not verify the exact table). Potential: shorter tests and smaller samples for recsys, IR and LLM-interface evaluation. No production deployment is reported in what I reviewed.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A clean, general variance-reduction idea aimed exactly at the recsys setting where CUPED helps least.

Complements covariate-based methods (CUPED) by exploiting structure in the treatment itself rather than pre-period data, so the two could in principle stack. It needs the platform to know both policies' action probabilities, which is realistic for ranking but harder for black-box LLM systems.

### Similar / related work

- [**CUPED on Steroids: Multivariate Covariate Adjustment for Switchback Experiments**](2026-09-29-arxiv-cuped-on-steroids-switchback.md) — covariate-based variance reduction (in this bank)
- [**Variance Reduction Combining Pre-Experiment and In-Experiment Data**](2026-09-30-arxiv-variance-reduction-pre-and-in-experiment-etsy.md) — another route to power gains (in this bank)

### Jargon buster

- **Policy overlap** — The share of decisions on which two policies choose the same action.
- **Off-policy estimation** — Estimating how a policy would perform using data logged under another policy, usually via importance weighting.
- **Doubly robust** — An estimator that stays consistent if either the propensity model or the outcome model is right.
