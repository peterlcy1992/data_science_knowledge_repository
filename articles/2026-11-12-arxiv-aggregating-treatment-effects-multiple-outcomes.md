---
id: arxiv-aggregating-treatment-effects-multiple-outcomes
title: "Aggregating treatment effects across multiple outcomes"
source: "arXiv econ.EM (Chun Pong Lau, University of South Carolina)"
url: "https://arxiv.org/abs/2611.05456"
published: "2026-11"
added: "2026-11-12"
category: experimentation-causal
tags: [composite-metrics, index-outcomes, PCA, inverse-variance-weighting, negative-weights, minimax, decision-theory]
novelty: 4
sourced_via: "full-text fetch"
---

# Aggregating treatment effects across multiple outcomes

**Source:** [arXiv econ.EM (Chun Pong Lau, University of South Carolina)](https://arxiv.org/abs/2611.05456) · Published 2026-11 · Added 2026-11-12
**Category:** experimentation-causal · **Tags:** `composite-metrics`, `index-outcomes`, `PCA`, `inverse-variance-weighting`, `negative-weights`, `minimax`, `decision-theory`

## TL;DR

The three standard ways to combine several outcomes into one treatment-effect index — PCA, inverse-variance-matrix (IVM) weighting and standardized averaging (SA) — have unexpected flaws: PCA and IVM can put negative weights on outcomes, and none necessarily maximizes precision. The paper proposes choosing nonnegative weights by minimizing mean-squared error under minimax or adaptation-regret criteria, and shows a published PCA-index result weakens under it.

## 1. Business context

Researchers routinely aggregate related outcomes to estimate an effect on an abstract concept — 'wealth', 'crime', 'productivity' — or just to summarize several outcomes. The author counts 30 PCA, 33 SA and 23 IVM uses in top-five economics journals in 2020–2024. The same problem appears whenever an experiment's decision rests on a composite of several metrics. The worry: if an index can give an outcome a negative weight, the aggregated effect can change sign relative to the individual effects, and the choice of method can manufacture or erase significance.

## 2. Technical details

**Setup.** Outcomes Y₁…Y_q are oriented the same way and standardized; the aggregated estimate is w′β̂. Interpretability requires weights nonnegative and summing to one; precision is the (asymptotic) variance or MSE of the aggregated effect.

**Shortcomings documented.** PCA can assign negative weights, need not maximize precision, depends on an arbitrary sign normalization, and can have nonstandard asymptotics — contrary to how it is often motivated. IVM (Anderson 2008) can also assign negative weights and need not maximize precision. SA (Kling et al. 2007) has equal positive weights but ignores the outcomes' correlation, leaving precision on the table. An appendix gives necessary and sufficient conditions for SA to be most powerful.

**Proposal.** Since the latent outcome is unobserved, choose nonnegative weights to minimize MSE under (a) a minimax criterion, which requires committing to a level of misspecification (how biased each outcome is as a measure of the latent concept), or (b) the adaptation-regret criterion of Armstrong et al. (2025), which adapts over a range of misspecification. Both reduce to convex optimization. Inference uses fixed-length confidence intervals that account for potential bias under the nonnegativity restriction; shape restrictions (e.g., some outcomes more important or less reliable) can be imposed. A communication model in which readers hold subjective weights also motivates the framework.

## 3. Impact — potential & realized

**Realized (reanalysis).** Revisiting a randomized cash-transfer study of COVID-era social distancing (Karlan et al., 2026) whose six-outcome PCA index showed a positive effect significant at 1% although no individual outcome was significant at that level: the author finds the PCA result is partly driven by the outcome with the largest negative treatment effect receiving the most negative PCA weight. With the decision-theoretic weights and no restriction on outcome quality, the effect is positive but smaller and not significant at 10%, even with variance-minimizing weights. Imposing the authors' own domain knowledge that two outcomes (e.g., days with visitors) are less informative recovers a positive effect significant at 5% under minimax — but only when those two are sufficiently downweighted and assumed more biased — which the paper frames as making precise how strong the assumptions must be.

**Potential.** A principled, auditable alternative to ad-hoc indices whenever several outcomes stand in for one concept.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Directly relevant to composite metrics and OEC design: shows how common index methods can flip signs and offers a convex, interpretable fix.

Industry experimentation platforms build composites all the time — an OEC, a 'health score', a satisfaction index from several survey items — often via PCA or variance-weighting. This paper is a crisp warning that those weights can be negative and that the method choice alone can create significance. The practical takeaways: constrain weights to be nonnegative, write down how much you trust each component as a proxy, and report how the conclusion depends on that trust. It's a job-market-style econometrics paper, so expect to translate the minimax/adaptation machinery into code yourself; a concurrent paper (Fedchenko 2026) reaches overlapping conclusions on SA and IVM.

### Similar / related work

- [**Do Modern Difference-in-Differences Estimators Change Published Findings in Business Research?**](2026-11-11-arxiv-modern-did-estimators-business-research-replication.md) — in this bank: a parallel 'negative weights change published conclusions' story, for DiD rather than indices
- [**Many Hands Make Light Work: Long-Term Effect Inference for the Experiment Reservoir**](2026-10-28-arxiv-experiment-reservoir-surrogate-long-term-effects.md) — in this bank: another way of combining several short-term metrics into one decision quantity
- [**Multiple Inference and Gender Differences in the Effects of Early Intervention (Anderson, 2008)**](https://doi.org/10.1198/016214508000000841) — the inverse-covariance-weighted index (IVM) analysed here

### Jargon buster

- **Index outcome** — A single weighted combination of several outcomes used to summarize a treatment's effect.
- **Standardized averaging (SA)** — Average of z-scored outcomes with equal weights (Kling, Liebman & Katz 2007).
- **Adaptation regret** — How much worse a rule does than the best rule you could have picked had you known the true amount of misspecification.
- **Fixed-length CI** — A confidence interval whose width accounts for the worst-case bias of the estimator, not just its variance.
