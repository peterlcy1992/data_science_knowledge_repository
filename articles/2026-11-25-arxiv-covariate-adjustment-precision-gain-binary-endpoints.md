---
id: arxiv-covariate-adjustment-precision-gain-binary-endpoints
title: "Quantifying and calibrating precision gain from covariate adjustment in clinical trials with binary endpoints"
source: "Boehringer Ingelheim (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.30845"
published: "2026-11"
added: "2026-11-25"
category: experimentation-causal
tags: [covariate-adjustment, variance-reduction, binary-outcomes, marginal-estimands, g-computation, prognostic-covariates, simulation-design, clinical-trials]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "arXiv listing (backlog stub)"
---

# Quantifying and calibrating precision gain from covariate adjustment in clinical trials with binary endpoints

**Source:** [Boehringer Ingelheim (arXiv stat.ME)](https://arxiv.org/abs/2611.30845) · Published 2026-11 · Added 2026-11-25
**Category:** Experimentation & Causal Inference · **Tags:** `covariate-adjustment`, `variance-reduction`, `binary-outcomes`, `marginal-estimands`, `g-computation`, `prognostic-covariates`, `simulation-design`, `clinical-trials`

## TL;DR

For binary outcomes, a covariate that is strongly prognostic in both arms can give no precision gain for the marginal treatment effect. The authors derive a closed-form identity for the maximum first-order variance reduction from adjustment. It depends on an estimand- and allocation-specific combination of the two arms' risk functions, not on the covariate alone. In their motivating example, a correctly specified, saturated g-computation gives −0.5% variance reduction for the risk difference but 10.1% for the risk ratio. They also give a calibration algorithm so that simulation studies can dial in population-level prognostic strength and known precision-gain potential, instead of relying on coefficient size.

## 1. Business context

Regulators encourage adjustment for prognostic baseline covariates (EMA 2015; FDA 2023). The intuition is that removing explainable outcome variation gives narrower intervals and may shorten or shrink trials. For continuous endpoints and linear models this is well understood.

Binary endpoints are harder. Logistic coefficients are *conditional* effects, while confirmatory trials usually target *marginal* (population-average) effects. With nonlinear links the two differ. So trials use model-assisted estimators of marginal effects, such as g-computation, AIPW and TMLE. The usual intuition carries over: if covariates are prognostic, adjustment should help. The authors show this need not hold. They also note that methodological simulation studies often define "strong" scenarios by coefficient size, which may not deliver the efficiency properties intended.

Related work by Li, Li & Luedtke (2023) estimates the efficiency gain for future trials from external data, with parameters defined under a sharp null. This paper is complementary. It targets simulation studies where the data-generating mechanism is set by design, and it allows the arms' risk functions to differ.

## 2. Technical details

- **Motivating example.** X ~ Bernoulli(0.85), 1:1 randomization, logit p(A,X) = 0.25 − 0.5A + 3.3X − 6.6AX. X's conditional log-odds contrast is +3.3 in control and −3.3 under treatment (odds ratios of about 27 and 1/27). Over 100,000 simulated trials with n = 500, logistic g-computation with the correct saturated model gives:
  - risk difference: variance 6.58·10⁻⁴ adjusted vs 6.55·10⁻⁴ unadjusted, i.e. **−0.5%**;
  - risk ratio: 3.60·10⁻⁴ vs 4.01·10⁻⁴, i.e. **10.1%** reduction.
- **Precision-gain identity (Proposition 1).** Take any estimand ψ = f(μ₁, μ₀) that is differentiable in the arm risks, with gradient (f₁, f₀) and allocation π. The maximum first-order absolute variance reduction is Var(√((1−π)/π)·f₁p₁(X) − √(π/(1−π))·f₀p₀(X)). The relative version divides by the unadjusted variance. The identity follows from standard semiparametric efficiency theory for randomized trials. It generalizes Moore & van der Laan (2009), whose risk-difference, equal-allocation result 4·Var{E(Y|X)} is a special case.
- **Marginal prognostic strength.** S_a = Var{p_a(X)}; the relative version divides by μ_a(1−μ_a). It is the share of arm-a outcome variance explained by the arm's risk function. It equals the population analogue of Tjur's coefficient of discrimination.
- **Coefficients ≠ prognostic strength.** For a binary X with prevalence q, S_a = q(1−q)·{p_a(1) − p_a(0)}². So it depends on baseline risk and covariate prevalence, not only on the log-odds coefficient.
- **When does prognostic strength determine gain? (Corollary 1, Table 2)** Only when X is *not predictive* on the target scale, meaning a constant RD or a constant RR across X. Then relative gain is a reverse-allocation-weighted harmonic mean of the two arms' relative prognostic strengths. This holds for RD and RR. It does not generally hold for the marginal odds ratio, even under non-predictiveness (counterexamples are in the Appendix). When X *is* predictive on the target scale, the two arms' contributions can offset.
  - Extreme example: Y¹ = X, Y⁰ = 1 − X. Prognostic strength is 1 in both arms, yet RD gain is exactly 0.
  - In the motivating example, relative prognostic strength is about 26.3% in both arms. The precision-gain potential is 0 for RD and about 10.6% for RR, closely matching the Monte Carlo −0.5% and 10.1%.
- **Structure-preserving calibration (Algorithm 1).**
  - The user fixes coefficient directions v_hom (shared) and v_het (treatment interaction), a covariate distribution and target marginal risks μ₀, μ₁.
  - A common multiplier λ scales all coefficients. The intercepts are re-solved by bisection to keep μ₀ and μ₁ fixed.
  - Proposition 2: relative prognostic strength rises strictly with λ, so it can index the path one-to-one on a bounded [0,1] scale. Proposition 3 gives its limit as λ → ∞.
  - The user picks a control-arm prognostic strength, and the algorithm reports the treatment-arm strength and the RD/RR/OR precision-gain potential.
  - Precision-gain potential is *not* monotone along the path (Appendix example), so it cannot serve as the index itself.
  - R code: github.com/Boehringer-Ingelheim/binary-dgm-calibration.

## 3. Impact — potential & realized

**Measured (illustrative application).** The example uses X₁ ~ Bernoulli(0.30) and X₂ ~ N(0,1), with h(X) = (X₁, X₂, X₁X₂²). It sets v_hom = (0.6, 0.4, 0.25) and v_het = (0, −1.1, 0), with μ₀ = 0.55 and μ₁ = 0.15. A reference sample of N = 200,000 and K = 100 grid points spans 95% of the attainable range.
- Targeting 20% control-arm prognostic strength gives λ* = 2.0932, with intercepts −0.2378 (control) and −2.9674 (treatment).
- Treatment-arm prognostic strength is then 29.8%.
- Under 1:1 allocation, the precision-gain potentials are **10.6% (RD), 13.5% (RR) and 12.2% (OR)**. The same mechanism gives different attainable gains by estimand.

**Limitations the authors state.**
- Precision-gain potential is a first-order asymptotic quantity, not a finite-sample guarantee for any particular estimator.
- The calibration uses logistic models and a common multiplier.
- Marginal prognostic strength and the calibration are tailored to binary outcomes.
- The framework assumes complete data. Time-to-event endpoints and missing data are left to future work.

**Potential.** The paper shifts the question from "is this covariate prognostic?" to "how do the arms' risk functions combine for this estimand and allocation?". It also provides a principled benchmark for simulation studies of adjusted estimators.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clean identity and a practical simulation tool, built on known efficiency theory

The identity itself is standard semiparametric efficiency for randomized trials, which the authors say openly. They present it as a generalization of Moore & van der Laan. The value is in how it is laid out. It makes visible why "strongly prognostic in both arms" can mean zero gain: the arms' risk functions cancel in the precision-relevant combination. The calibration algorithm is the more usable piece. Anyone writing a simulation study of g-computation, AIPW or TMLE on binary outcomes can now report the attainable gain of each scenario instead of hand-waving about coefficient size.

My mapping to online experimentation: conversion-rate A/B tests with CUPED-style regression adjustment are the same marginal-RD setting. The lesson transfers. When a pre-period covariate is predictive of the *treatment effect* (heterogeneity on the RD scale), its variance-reduction value can be much smaller than its predictive power suggests. The choice of reported metric (absolute vs relative lift) also changes how much adjustment helps. That application is my extrapolation; the paper is framed entirely around clinical trials and simulation design.

### Similar / related work

- [**Higher-Order Asymptotics of Regression-Adjusted Estimators in Randomized Trials**](2026-10-26-arxiv-higher-order-regression-adjustment-rct.md) (in this bank) — Kelley & Wager; when first-order gains tie, second-order terms decide between adjustment schemes. A natural complement to this first-order bound.
- [**Optimal Variance Reduction in Randomized Experiments**](2026-11-09-arxiv-optimal-variance-reduction-randomized-experiments-najmi-keselman.md) (in this bank) — derives the variance-minimizing fixed adjustment function, a convex combination of the two arms' conditional means. This is the same "arms combine" structure that drives the identity here.
- [**Unlocking 66% Faster Experiments with Covariate Adjustment**](2026-10-12-instacart-covariate-adjustment-power-analysis-clustered-data.md) (in this bank) — Instacart's production view of covariate adjustment and power analysis.
- **Estimating the efficiency gain of covariate-adjusted analyses in future clinical trials using external data** — Li, Li & Luedtke (JRSSB 2023); prospective gain estimation under a sharp null, which the authors call complementary.
- **Covariate adjustment in randomized trials with binary outcomes: targeted maximum likelihood estimation** — Moore & van der Laan (Statistics in Medicine 2009); its RD relative-efficiency result is a special case of Proposition 1.

### Jargon buster

- **Marginal vs conditional effect** — marginal is the population-average contrast of risks (e.g. μ₁ − μ₀). Conditional is the effect within covariate strata, such as a logistic coefficient. With nonlinear links they differ even without confounding.
- **Precision-gain potential** — the most first-order asymptotic variance that any regular adjusted estimator could remove versus the unadjusted one.
- **Marginal prognostic strength** — the share of an arm's outcome variance explained by its true risk function of the covariates.
- **Predictive covariate** — one associated with the size of the treatment effect, on a specific scale (RD, RR or OR).
- **g-computation (standardization)** — fit an outcome model, predict everyone's risk under each arm, and average.
- **Structure-preserving calibration** — scale all coefficients together and re-solve the intercepts so the marginal risks stay fixed, then pick the scale by target prognostic strength.
