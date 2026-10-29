---
id: arxiv-spillover-effects-multiple-pre-treatment-periods
title: "Identifying and disentangling direct and spillover effects using multiple pre-treatment periods"
source: "arXiv econ.EM (Martin Huber, University of Fribourg)"
url: "https://arxiv.org/abs/2610.37049"
published: "2026-10"
added: "2026-10-29"
category: experimentation-causal
tags: [interference, spillover, interrupted-time-series, double-machine-learning, exposure-mapping, no-anticipation]
novelty: 4
sourced_via: "full-text fetch"
---

# Identifying and disentangling direct and spillover effects using multiple pre-treatment periods

**Source:** [arXiv econ.EM (Martin Huber, University of Fribourg)](https://arxiv.org/abs/2610.37049) · Published 2026-10 · Added 2026-10-29
**Category:** Experimentation & Causal Inference · **Tags:** `interference`, `spillover`, `interrupted-time-series`, `double-machine-learning`, `exposure-mapping`, `no-anticipation`

## TL;DR

Under interference a clean comparison group is usually contaminated, so DiD-style designs identify only the total effect on the treated minus the spillover on the comparison units. Huber shows that with several pre-treatment periods you can extrapolate each group's own pre-trend (interrupted-time-series style) to get the no-treatment counterfactual, which identifies the total effect on the treated and the spillover on the non-treated separately, without an uncontaminated control group.

## 1. Business context

Whenever treating some units affects others (marketplaces, networks, geographic rollouts, policy), the usual comparison of treated and untreated units is muddied: the untreated group is itself exposed to spillovers. The paper notes that in this case a comparison-group estimand is the difference between the total effect on the treated and the spillover effect on the comparison units, that neither component is separately identified, and that the sign of the estimand says nothing about the sign of either. Existing remedies restrict the interference structure and still need some clean controls.

## 2. Technical details

Setup: under no anticipation, pre-treatment outcomes of every unit (treated or not) are free of both direct and spillover components, so they are realisations of the no-treatment potential outcome. Extrapolating a group's own pre-treatment trend (as in interrupted time series) therefore identifies the counterfactual in the absence of any treatment; applied to the treated it gives the total effect on the treated, and applied to non-treated units at a given exposure level it gives the spillover effect on them. Exposure is summarised by an exposure mapping (in the sense of Aronow and Samii), e.g. the number of treated units in a neighbourhood. With two pre-periods and a linear trend the counterfactual conditional mean is a second difference of the cell's own pre-treatment conditional means. Contributions beyond the covariate-free result the paper attributes to Celli et al. (2026): (1) a conditional version, letting trends differ by covariates and covariate composition change across periods, so it works in repeated cross sections as well as panels; (2) a precise statement of what separating direct from spillover effects needs, namely effect homogeneity (treated and non-treated units with the same exposure and covariates have the same average spillover) plus observed exposure with common support across groups; (3) a testable restriction: units the exposure mapping classifies as non-exposed must have zero estimated spillover, which tests the design jointly with the exposure mapping, and, if conditional parallel trends are also imposed, the counterfactual is overidentified and the two routes agree iff pre-treatment trends coincide across groups; (4) doubly robust, Neyman-orthogonal estimators that allow machine-learned nuisance functions, with root-n consistency and asymptotic normality.

## 3. Impact — potential & realized

Realized: a simulation study confirms root-n behaviour of the estimators and reliable standard errors. In an application to the compulsory licensing of enemy-owned patents in the United States in 1919, licensing raised patenting both in the licensed subclasses and in technologically close ones, so a comparison-group design understates the total effect. The polynomial order of the trend was chosen by cross-validation inside the pre-treatment era (a linear trend was used throughout). Potential: designs with staggered or partial rollouts where no unit is clean can still recover effects, provided the pre-trend extrapolation is credible. The author regards the total effect on the treated and the spillover on the non-treated as the main parameters, since the direct/spillover split needs the stronger homogeneity and common-support conditions.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A clean identification result that trades the clean-control assumption for a trend-extrapolation assumption. Which of the two is more believable is a design question; the testable non-exposed-units restriction is the practical gem. The extrapolation can be fragile with few pre-periods (the paper's own cross-validation shows quadratic and cubic trends being much more dispersed than linear).

Its main novelty over the covariate-free result is the conditional, doubly robust version plus the testable restriction. Likely most useful to economists and to teams evaluating rollouts where every unit may be exposed. Treat it as complementary to DiD, not a replacement: it swaps parallel trends for a valid within-group extrapolation.

### Similar / related work

- [**Honest inference for synthetic controls with imperfect fit**](2026-10-26-arxiv-honest-inference-synthetic-controls-imperfect-fit.md) — another way of getting counterfactuals from pre-period data, with explicit inference
- [**Bias-Aware Guardrail Selection Under Network Interference**](https://arxiv.org/abs/2610.36702) — design-side treatment of network interference
- [**Aronow & Samii, Estimating average causal effects under general interference**](https://arxiv.org/abs/1305.6156) — origin of the exposure-mapping idea used here

### Jargon buster

- **Interference / spillover** — One unit's treatment changes another unit's outcome, breaking the no-interference (SUTVA) assumption.
- **No anticipation** — Units do not change behaviour before treatment starts, so pre-period outcomes are untouched by it.
- **Exposure mapping** — A function summarising how strongly a unit is reached by others' treatment, e.g. number of treated neighbours.
- **Neyman-orthogonal** — An estimating equation insensitive to small errors in nuisance estimates, which lets ML models be used for controls.
