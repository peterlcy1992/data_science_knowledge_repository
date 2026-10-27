---
id: arxiv-regression-adjustment-ratios-treatment-effects
title: "Regression Adjustment for Ratios of Treatment Effects in Randomized Experiments"
source: "arXiv econ.EM (Kakehi)"
url: "https://arxiv.org/abs/2610.35666"
published: "2026-10"
added: "2026-10-27"
category: experimentation-causal
tags: [regression-adjustment, variance-reduction, late, cross-fitting, lasso, design-based-inference]
novelty: 4
sourced_via: "full-text fetch"
---

# Regression Adjustment for Ratios of Treatment Effects in Randomized Experiments

**Source:** [arXiv econ.EM (Kakehi)](https://arxiv.org/abs/2610.35666) · Published 2026-10 · Added 2026-10-27
**Category:** experimentation-causal · **Tags:** `regression-adjustment`, `variance-reduction`, `late`, `cross-fitting`, `lasso`, `design-based-inference`

## TL;DR

For ratio estimands in randomized experiments (e.g. the LATE under noncompliance), existing regression adjustment fixes the numerator and denominator separately. The paper adjusts the transformed outcome Y−τD directly with a cross-fitted two-step estimator, keeps the final adjustment fixed-dimensional, and adds an augmented version that is asymptotically no less efficient than the benchmark estimators.

## 1. Business context

Randomized experiments often target a ratio of two treatment effects: the local average treatment effect (LATE) when some assigned units do not take up the treatment (the Wald ratio), or an incremental cost-effectiveness ratio. Regression adjustment with baseline covariates is the standard precision lever, and the paper notes it keeps a no-harm property (asymptotically no less precise than the unadjusted estimator even if the conditional-mean model is wrong). The existing ratio literature (Ren 2024; Jiang et al. 2026; Liu and Chen 2026) adjusts numerator and denominator separately. The paper argues this misses the efficiency target: the first-order variance of the Wald ratio is governed by the transformed potential outcome Y(z)−τD(z), and predicting Y(z) and D(z) separately does not necessarily predict that particular combination well. With ordinary least squares on one projection space the two routes coincide, but with flexible or regularized learners they need not.

## 2. Technical details

Two-step estimator: first predict the transformed outcome directly, then use the prediction as a single adjustment covariate, so the final adjustment is fixed-dimensional even when the first-stage learner sees many covariates (avoiding the many-regressor bias and variance-estimation problems of Lei and Ding 2020 and Chiang et al. 2025). Conditional cross-fitting (Lu et al. 2025a) lets flexible learners and cross-validation be used under prediction-level conditions. For LASSO the paper develops persistence-based theory (Greenshtein and Ritov 2004) that does not require sparsity, allows more covariates than observations, and covers cross-validated penalty selection. An augmented two-step estimator adds baseline covariates and the separate predictions to the adjustment set, so it nests the benchmark adjustment spaces and is asymptotically no less efficient than them; the feasible conservative variance estimator satisfies the same ordering. The setting is design-based (complete randomization; a stratified extension is in an appendix).

## 3. Impact — potential & realized

Realized (simulation, as reported): N=500, p=8 covariates with t3-distributed features and roughly 55% compliance, 5,000 complete randomizations of one fixed finite population, balanced assignment. With degree-two polynomial prediction the two-step estimator reduces the mean standard error by 39.4% and 17.5% relative to Wald and COB (Ren's calibrated Oaxaca-Blinder); a polynomial ILS estimator that puts many covariates into the final adjustment undercovers (coverage 0.928 against a 0.95 nominal level). With LASSO first-stage prediction the two-step estimator cuts the mean SE by 52.0%, 31.2% and 34.1% versus Wald, COB and R, and the augmented 'two-step extra' by 53.1%, 32.8% and 35.6%, with coverage 0.974. Application: the Dupas et al. (2018) savings-voucher experiment in Uganda (2,160 households randomized within 41 strata; 41.87% of assigned households opened an account and deposited within two years). For the 'formal financial institution' outcome the LATE estimate and SE are 22.024 (2.878) for two-step extra, against 22.737 (2.951) for the benchmark F estimator and 20.558 (3.067) unadjusted. Potential: a drop-in way to use ML-based prediction for noncompliance and ratio-metric experiments without enlarging the final regression. The simulation is a single synthetic design, and the paper reports precision gains rather than a general guarantee that two-step beats every benchmark in every design.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A clean 'adjust the right target' argument for ratio estimands, with the practical trick of compressing many covariates into one fixed-dimensional adjustment.

Product teams meet ratio estimands constantly (effect on conversions per exposed user, per-treatment-taker effects when assignment and exposure differ). The takeaway that transfers is that the variance of a ratio depends on the combined residual Y−τD, so the prediction target should be that combination, not two separate models. Treat the numbers as evidence from one synthetic design plus one reanalysis, and note the compliance setting is more common in field experiments than in on-platform A/B tests.

### Similar / related work

- [**Higher-Order Asymptotics of Regression-Adjusted Estimators in Randomized Trials**](2026-10-26-arxiv-higher-order-regression-adjustment-rct.md) (in this bank) — same family of regression-adjusted estimators; there the question is simple vs interacted regression at second order
- [**Ensuring Trustworthy Online A/B Testing: Addressing Five Key Questions on CUPED**](2026-10-02-arxiv-cuped-five-questions-bytedance.md) (in this bank) — practical side of covariate adjustment for online experiments

### Jargon buster

- **LATE / Wald ratio** — Average effect for units whose treatment take-up is changed by assignment, estimated as the effect of assignment on the outcome divided by its effect on take-up.
- **Cross-fitting** — Fit the prediction model on one part of the data and use it to predict on another part, so overfitting does not leak into the adjustment.
- **Transformed outcome Y−τD** — The combination of outcome and take-up whose variance drives the precision of the ratio estimate.
- **Persistence (LASSO theory)** — A prediction-stability framework that does not require the true coefficients to be sparse.
