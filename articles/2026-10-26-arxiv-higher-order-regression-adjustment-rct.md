---
id: arxiv-higher-order-regression-adjustment-rct
title: "Higher-Order Asymptotics of Regression-Adjusted Estimators in Randomized Trials"
source: "arXiv stat.ME (Kelley & Wager)"
url: "https://arxiv.org/abs/2610.32023"
published: "2026-10"
added: "2026-10-26"
category: experimentation-causal
tags: [regression-adjustment, variance-reduction, ab-testing, asymptotic-deficiency, robust-standard-errors]
novelty: 4
sourced_via: "full-text fetch"
---

# Higher-Order Asymptotics of Regression-Adjusted Estimators in Randomized Trials

**Source:** [arXiv stat.ME (Kelley & Wager)](https://arxiv.org/abs/2610.32023) · Published 2026-10 · Added 2026-10-26
**Category:** experimentation-causal · **Tags:** `regression-adjustment`, `variance-reduction`, `ab-testing`, `asymptotic-deficiency`, `robust-standard-errors`

## TL;DR

In 50-50 randomized experiments, simple and interacted (Lin) regression adjustment have the same first-order variance, so the choice is a second-order question. The paper shows the winner depends on feature skewness, effect heterogeneity, heteroskedasticity and misspecification, and that simple regression can beat interacted regression by a material amount when features are skewed and outlying values carry more noise.

## 1. Business context

Regression adjustment (the family that includes CUPED-style covariate adjustment) is a standard way to sharpen the precision of average treatment effect estimates from randomized trials; the paper cites FDA guidance encouraging adjustment for strongly prognostic baseline covariates. Lin (2013) showed that interacted regression, with full treatment-by-covariate interactions, weakly dominates both the difference in means and simple regression at leading (root-n) order. But 50-50 allocation is the default in most experiments, and there the first-order asymptotic variance of the two regressions is identical, so first-order theory gives no guidance on which to use.

## 2. Technical details

The authors compare the two estimators through higher-order (second-order) expansions of mean-squared error, framed with Hodges-Lehmann asymptotic deficiency: if both MSEs are V/n + c/n² terms, the difference (c_B − c_A)/V is the fixed number of extra samples the less accurate estimator needs. To keep rare blow-ups from dominating, they work with a capped MSE. The main theorem covers a completely randomized trial with n₁ = ⌊n/2⌋, IID sampling and finite 12th moments, and gives the n⁻² MSE difference in terms of whitened-feature moments, effect-heterogeneity coefficients and heteroskedasticity terms.

A motivating example: log(X) ~ N(0, 1.1²) and Y(w) = 0.9X + w + (1+X)U with U ~ N(0,1); at n = 500 interacted regression has 7% higher mean-squared error for the ATE than simple regression. The paper then studies feasible inference with HC1 and jackknife/HC3 heteroskedasticity-robust standard errors for both point estimators.

## 3. Impact — potential & realized

Realized (theory plus simulation, as reported): the relative performance can favor either estimator depending on feature skewness, treatment-effect heterogeneity, heteroskedasticity and nonlinear misspecification; in some practically important settings, including skewed features where outlying values go with higher outcome noise, simple regression outperforms interacted regression by a material amount. HC1 standard errors can undercover substantially under skewed, tail-heteroskedastic covariates for both point estimates; the jackknife improves coverage in most designs, especially at lower nominal levels, but can still undercover with rare outliers or large heterogeneity. In a typical low-heterogeneity regime, simple regression with the jackknife reached at least nominal 95% coverage in all of the authors' designs, with intervals no wider than interacted regression under either variance estimator.

Potential: a more grounded default for covariate-adjusted A/B analysis with heavy-tailed pre-experiment metrics. The authors flag that their analysis assumes IID sampling and that a design-based analysis could give different second-order results.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A rigorous answer to a question practitioners hit constantly (interact or not?), with a counter-intuitive result that Lin's dominance does not always carry over to finite samples.

Experimentation platforms often implement the fully interacted regression because it is theoretically 'free'. This paper is a reminder that 'weakly dominates' is a statement about leading order, and with skewed revenue-like covariates and 50-50 splits the extra parameters can cost real precision. Worth checking your platform's default on your own heavy-tailed metrics, using robust standard errors with a small-sample correction rather than plain HC1.

### Similar / related work

- [**Unlocking 66% Faster Experiments with Covariate Adjustment: Power Analysis for Clustered Data, Ratio Metrics, and OLS Regression**](2026-10-12-instacart-covariate-adjustment-power-analysis-clustered-data.md) (in this bank) — Instacart's covariate-adjustment power analysis — the applied side of the same variance-reduction idea
- [**Ensuring Trustworthy Online A/B Testing: Addressing Five Key Questions on CUPED**](2026-10-02-arxiv-cuped-five-questions-bytedance.md) (in this bank) — Five questions on CUPED — practical trustworthiness questions for covariate adjustment
- [**Covariate Selection for Doubly Robust Double/debiased Machine Learning Estimators for Causal Inference**](2026-10-01-arxiv-covariate-selection-doubly-robust-dml.md) (in this bank) — Covariate selection for DML — which covariates to adjust for

### Jargon buster

- **Interacted regression (Lin)** — Regress the outcome on treatment, centered covariates and their interactions, so each arm gets its own covariate slope.
- **Asymptotic deficiency** — The extra sample size the worse of two first-order-equivalent estimators needs to match the better one.
- **HC1 / jackknife (HC3)** — Heteroskedasticity-robust standard-error formulas; the jackknife version is more conservative with outliers and small samples.
- **Completely randomized trial** — A design where a fixed number of units are assigned to treatment uniformly at random.
