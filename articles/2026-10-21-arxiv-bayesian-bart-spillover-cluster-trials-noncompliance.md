---
id: arxiv-bayesian-bart-spillover-cluster-trials-noncompliance
title: "A Bayesian machine learning approach to direct and spillover effects in cluster-randomized trials with noncompliance"
source: "arXiv stat.ME (Bhandari, Li & Daniels)"
url: "https://arxiv.org/abs/2610.27425"
published: "2026-10"
added: "2026-10-21"
category: experimentation-causal
tags: [spillover, cluster-randomized, noncompliance, BART, g-computation]
novelty: 3
sourced_via: "web search"
---

# A Bayesian machine learning approach to direct and spillover effects in cluster-randomized trials with noncompliance

**Source:** [arXiv stat.ME (Bhandari, Li & Daniels)](https://arxiv.org/abs/2610.27425) · Published 2026-10 · Added 2026-10-21
**Category:** experimentation-causal · **Tags:** `spillover`, `cluster-randomized`, `noncompliance`, `BART`, `g-computation`

## TL;DR

Combines BART with cluster random effects and a 'peer-treatment clever covariate' to separate direct from spillover effects in cluster-randomized trials with noncompliance, estimated by Bayesian g-computation and applied to the Kenya school deworming project.

## 1. Business context

In cluster-randomized trials with imperfect compliance, treating some individuals also affects untreated peers; decisions about scaling an intervention need to know the direct effect and the spillover separately, which regularized flexible models tend to distort.

## 2. Technical details

Outcome and treatment-receipt models use Bayesian additive regression trees with cluster-level random effects. A clever covariate, the predicted proportion of treated peers from a preliminary receipt model, is added to reduce regularization-induced distortion in the decomposition. Estimation is by Bayesian g-computation, targeting cluster-average intent-to-treat effects and cluster-average local average treatment effects, and the authors assess sensitivity to the cross-world restrictions the decomposition needs.

## 3. Impact — potential & realized

Reported in simulations: reduced bias under model misspecification; correctly specified parametric models show expected frequentist behaviour; the clever covariate improves the direct/spillover split when spillover is moderate or strong, similarly in smaller clusters; 95% credible intervals are conservative. In the Primary School Deworming Project in Kenya the method suggests reduced infection risk, with a larger contribution from individual receipt than from peer receipt. Numerical estimates are not in the abstract.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Bayesian flexible-model route to separating direct and spillover effects under noncompliance.

Spillover matters beyond medicine: marketplaces, referrals and social products all have cluster structure and peer exposure. The clever-covariate trick is a transferable fix for BART's shrinkage bias. Caveats: conservative intervals and reliance on cross-world assumptions mean the decomposition is an identifiable-under-assumptions quantity; abstract-level read. Novelty 3/5.

### Similar / related work

- [**Rerandomization under Interference**](2026-09-29-arxiv-rerandomization-under-interference.md) — design-stage handling of interference between units (in this bank)
- [**Covariate-adaptive randomization using historical data**](2026-10-20-arxiv-covariate-adaptive-randomization-historical-data.md) — design-based precision gains in experiments (in this bank)

### Jargon buster

- **Spillover effect** — The effect of one unit's treatment on other units' outcomes.
- **LATE** — Local average treatment effect: the effect among compliers, units whose treatment receipt is changed by assignment.
- **BART** — Bayesian additive regression trees, a flexible sum-of-trees Bayesian regression model.
- **G-computation** — Estimating effects by modelling outcomes then averaging predictions under counterfactual treatment settings.
