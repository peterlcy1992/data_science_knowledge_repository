---
id: arxiv-optimal-variance-reduction-randomized-experiments-najmi-keselman
title: "Optimal Variance Reduction in Randomized Experiments"
source: "arXiv stat.ME (Amir Najmi, Michael D. Keselman)"
url: "https://arxiv.org/abs/2608.23615"
published: "2026-08"
added: "2026-11-09"
category: experimentation-causal
tags: [variance-reduction, regression-adjustment, delta-method, ratio-metrics, covariates]
novelty: 3
sourced_via: "full-text fetch"
---

# Optimal Variance Reduction in Randomized Experiments

**Source:** [arXiv stat.ME (Amir Najmi, Michael D. Keselman)](https://arxiv.org/abs/2608.23615) · Published 2026-08 · Added 2026-11-09
**Category:** experimentation-causal · **Tags:** `variance-reduction`, `regression-adjustment`, `delta-method`, `ratio-metrics`, `covariates`

## TL;DR

Covariate adjustment using a fixed function g(x) of treatment-unaffected covariates, chosen without access to the experiment data, keeps the effect estimate unbiased whatever model produces g. For additive metrics the variance-minimizing g is a convex combination of the two conditional-mean functions with 'backwards' weights; for ratio and multiplicative metrics the delta-method variance is minimized.

## 1. Business context

Variance reduction shortens experiments and sharpens decisions. Existing methods (CUPED and Double ML-style approaches) either use a single arm's model, require separately trained treatment and control models (a problem when one arm is much smaller), or handle only additive metrics. The paper offers a simpler route to an optimal adjustment, including for ratio metrics such as the share of offered recommendations that are accepted.

## 2. Technical details

Setup: iid (X, Y(0), Y(1)), units randomly assigned with treatment fraction gamma. The adjusted estimator subtracts the difference in arm means of g(X) from the difference in means of Y. Because g is fixed without access to experiment data, the correction is zero in expectation, so unbiasedness holds regardless of how complex g is; the authors compare this to Double ML, where models of arbitrary complexity can be used without concern for overfitting or regularization bias. Using a lemma based on the law of total variance, the variance is minimized at g*(x) = (1-gamma) E[Y(1)|X=x] + gamma E[Y(0)|X=x]: a single g that compromises between arms, with weights that look backwards (gamma on control, 1-gamma on treatment). For multiplicative and ratio metrics the delta-method variance is minimized; the paper works through additive, log-scale, ratio, ratio-of-ratio, stable-denominator, ratio-of-variances and regression/trend settings and discusses modelling choices and prediction accuracy versus variance reduction.

## 3. Impact — potential & realized

Realized (as reported): the contribution is theoretical, illustrated through examples; this entry does not quote empirical gains. Potential: a recipe for choosing and training the covariate function in practice, namely train outcome models on pooled data and blend them with arm-fraction weights, applicable to additive and ratio metrics alike. Optimality is with respect to the variance (delta-method variance for non-additive metrics), not a finite-sample guarantee.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid, incremental

A tidy theoretical note whose practical value is the explicit weighting rule and the ratio-metric extension. Much of the territory (optimal control variates, regression adjustment, Double ML) is known, so novelty is moderate; the authors themselves emphasize simplicity of the proofs. Best read as a reference for teams building experiment-analysis libraries.

### Similar / related work

- [**Regression Adjustment for Ratios of Treatment Effects in Randomized Experiments**](2026-10-27-arxiv-regression-adjustment-ratios-treatment-effects.md) (in this bank) — adjustment for ratio metrics
- [**Higher-Order Asymptotics of Regression-Adjusted Estimators in Randomized Trials**](2026-10-26-arxiv-higher-order-regression-adjustment-rct.md) (in this bank) — theory of adjusted estimators
- [**Jin and Ba 2023 'Toward optimal variance reduction in online controlled experiments'**](https://arxiv.org/abs/2110.13406) — closest prior optimality result, cited by the paper
- [**Hosseini and Najmi 2019 'Unbiased variance reduction in randomized experiments'**](https://arxiv.org/abs/1904.03817) — earlier work by one author

### Jargon buster

- **Delta method** — A first-order approximation for the variance of a function (such as a ratio) of sample means.
- **Control variate** — A quantity with known mean difference (here zero in expectation) subtracted to reduce estimator variance.
- **Double ML** — Using flexible ML models for nuisance functions while keeping valid inference through orthogonalization / sample splitting.
