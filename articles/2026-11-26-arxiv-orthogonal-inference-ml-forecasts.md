---
id: arxiv-orthogonal-inference-ml-forecasts
title: "Orthogonal inference for machine learning forecasts"
source: "Erasmus School of Economics, Erasmus University Rotterdam (arXiv econ.EM)"
url: "https://arxiv.org/abs/2611.33187"
published: "2026-11"
added: "2026-11-26"
category: forecasting-timeseries
tags: [forecast-evaluation, diebold-mariano, neyman-orthogonality, locally-robust-estimation, predictive-ability-tests, lasso, neural-probability-forecasts, long-run-variance, time-series-inference]
novelty: 3
sourced_via: "full-text fetch"
---

# Orthogonal inference for machine learning forecasts

**Source:** [Erasmus School of Economics, Erasmus University Rotterdam (arXiv econ.EM)](https://arxiv.org/abs/2611.33187) · Published 2026-11 · Added 2026-11-26
**Category:** Forecasting & Time Series · **Tags:** `forecast-evaluation`, `diebold-mariano`, `neyman-orthogonality`, `locally-robust-estimation`, `predictive-ability-tests`, `lasso`, `neural-probability-forecasts`, `long-run-variance`, `time-series-inference`

## TL;DR

ML forecasts are often trained on one loss, such as squared error, and judged on another, such as an asymmetric cost or a state-weighted loss. The paper shows that estimation error can then "create spurious evidence of predictive superiority, even with out-of-sample evaluation". Alberto Quaini adds a locally robust correction to the Diebold–Mariano loss contrast. The correction removes first-order sensitivity to estimation and stays valid with overlapping rolling windows and refitting at every date. In lasso simulations, false rejections at a 5% nominal level fall from 33.9–53.6% to 7.2–8.6%. Bootstrapping the raw scores does not reproduce this gain.

## 1. Business context

Forecast comparisons drive investment and other economic decisions. The training objective often differs from the loss that matters for the decision. Examples from the paper: a conditional mean fitted by squared loss but judged on asymmetric costs, Huber-trained return forecasts judged by squared error, or least-squares forecasts judged by investment utility. Persistent regularization penalties and evaluation focused on particular economic states also break the alignment.

When training and evaluation are aligned, the evaluation risk has zero derivative at the training optimum. Estimation error then enters only at second order. Escanciano and Parra (2026) give predictive-risk inference for ML forecasts in that zero-derivative case. When the derivative is nonzero, "regularization bias and limited learning accuracy can invalidate uncorrected inference". Classical West-style adjustments instead need an asymptotic description of the fitted parameters, which ML learners rarely provide.

The target is the difference in *population* evaluation risks of the two rules' population training solutions, in the tradition of West (1996). This differs from Giacomini–White fixed-window comparisons, where estimation uncertainty remains part of the target.

## 2. Technical details

- **Target.** Loss contrast g_t = q_t[ℓ(Y_t, F₁(η₁)) − ℓ(Y_t, F₂(η₂))], with θ₀ = E g_t at the population training solutions. The instrument q_t allows comparisons within prespecified economic states; q_t = 1 gives ordinary expected losses. The rules may differ in training objective, prediction class and information set, and need not be nested.
- **Orthogonal score.** For each rule, a representer α relates the evaluation derivative to the training Hessian. The corrected score subtracts the training score in direction α: φ_t = g_t − Σ_j s_{j,t}(η_j)[α_j]. Training first-order conditions preserve the target. The remaining mean error is bounded by squared forecast error plus the product of forecast and representer errors (Prop. 1). Both errors at o(n⁻¹ᐟ⁴) suffice.
- **Variance changes too.** The corrected long-run covariance includes both corrections and their cross-covariances with the raw contrast. It "need not be larger or smaller than the raw covariance". Even identical population forecasts can have a nondegenerate corrected contrast (Example 1). Conversely, a nonzero evaluation derivative does not guarantee a nondegenerate covariance, which Wald inference needs.
- **Chronological inference (main contribution).** Fits use only past data with a gap b_n before each evaluation block. Windows may overlap, and an evaluation outcome may enter later training windows. Under geometric β-mixing, Theorem 2 gives asymptotic normality when n·β(b_n) → 0, √(b_n+1)·ρ_n → 0 and √n·B_n → 0. The proof groups evaluation dates by residue class modulo b_n+1. This permits K_n = n refits with "no additional algebraic factor" in the rate conditions. No limiting distribution for the learners is required.
- **Covariance and uniformity.** A Bartlett long-run covariance estimator is consistent if additionally √L_n·ρ_n → 0; L_n = ⌈n¹ᐟ⁴⌉ is admissible when n¹ᐟ⁸ρ_n → 0. Prop. 2 gives uniform coverage over classes of data-generating processes, given uniform learning bounds and a covariance eigenvalue bounded away from zero.
- **Uncorrected test (Prop. 3).** The raw statistic carries an accumulated drift Δ_n. Under the null its Wald test converges to a noncentral χ² and over-rejects whenever the drift limit is nonzero.
- **Lasso implementation.** Forecast by lasso, then estimate the representer by a second lasso on a generated response (the evaluation-loss derivative at the fitted forecast) on the *same* window. No extra cross-fitting is used. Corollary 2 gives simultaneous rates over overlapping windows, extended to approximate sparsity in ℓ_q balls.
- **Neural implementation.** For binary outcomes trained by squared loss and evaluated by cost-weighted loss (1+τY)(Y−p)², the correction is analytic: A_τ(p) = −2τp(1−p). It needs "neither an auxiliary regression nor a Hessian with respect to network weights". Corollary 3 gives a simultaneous learning bound split into approximation error, class complexity and an assumed optimization gap.
- **Simulations.** Four tests: Raw, Bootstrap Raw, Orthogonal and Bootstrap Orthogonal. The circular block bootstrap holds fitted objects fixed. Lasso: an omitted state × signal interaction creates the mismatch, with p ∈ {32, 128, 256}, chronological CV tuning and 77,250 replications. Neural: two hidden ReLU layers of width 8 with a skip connection (134 parameters), trained with Adam, τ = 4, and 7,168 replications.

## 3. Impact — potential & realized

**Measured (lasso, n = 1,000, five fits, nominal 5%):**
- T = n: raw rejection rises from 33.9% to 53.6% as p grows, versus 7.2–8.6% after correction. Bootstrap Raw stays at 30.8–48.7%.
- T = 2n: corrected 5.6–6.4%, raw 20.9–31.8%. T = 0.5n: corrected 9.9–13.2%, raw 54.9–80.5%.
- At T = n, p = 32: mean √n-scaled drift falls from 1.69 to 0.17. 95% interval coverage rises from 66.1% to 92.8%, with mean length almost unchanged (0.139 → 0.138).
- Repeated refitting (one fit, five fits, every 25 dates): orthogonal 7.2–7.4% vs raw 33.0–35.1%. Refitting at every date (n = T = 500, 250 replications): 5.2% vs 36.4%.
- Size-adjusted power at δ = −0.7 rises from 1.2% to 8.4%; at δ = +0.7 it is 13.4% raw vs 11.0% corrected. The gain "is not uniform across signs".
- Under an information-criterion penalty selector at p = 256, T = n, correction does not help (Raw 44.4%, Orthogonal 47.1%). "Orthogonality still requires sufficiently accurate estimates."

**Measured (neural, n = 1,000, T = 4,000):**
- Raw and Bootstrap Raw both reject 14.7%, Orthogonal 7.8% and Bootstrap Orthogonal 7.9%. Gains are smaller at n = 500 and with longer training (T = 8,000), where the paired difference is not significant.
- Size-adjusted power at δ = −0.6 falls from 30.5% (raw) to 17.8% (corrected). "Better size need not imply greater size-adjusted power."

**Potential:** valid tests of "is model A really better under the loss we care about" when models are trained on a convenient surrogate loss, refit on rolling windows and tuned by CV. The author concludes that orthogonality "removes first-order sensitivity, but does not ensure accurate finite-sample inference or uniform power gains". Replication code is at github.com/a91quaini/replicate-oos-ml-test.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Standard DML machinery, carefully transplanted to rolling-window forecast evaluation

The score itself is the textbook locally robust/Riesz construction, as the paper openly says. The new part is the dependence argument. It allows overlapping chronological windows, evaluation outcomes that re-enter training, and refitting at every date without a penalty on the number of fits. That is a real gap in existing time-series DML, which uses leave-out blocks or a fixed number of folds. The paper is also candid about limits: residual over-rejection with short training, failure under one tuning rule, and a power loss in the neural design.

Practitioner mapping (mine): this applies whenever a team backtests a model trained on MSE or log-loss, then reports wins on a business-weighted metric. Examples are asymmetric over/under-forecast costs in inventory, peak-hour-weighted error, or segment-restricted accuracy. A Diebold–Mariano test there can be badly oversized, and a block bootstrap will not fix it. For squared-loss training the correction is cheap: one extra regression of the loss derivative on the features, or a closed form for probability forecasts. The main practical demands are a gap between train and test windows and a corrected-score long-run variance. I expect forecast-evaluation libraries to adopt the asymmetric-loss and Brier-weighted corrections.

### Similar / related work

- **Extending the Scope of Inference About Predictive Ability to Machine Learning Methods** — Escanciano & Parra (JBES 2026). Predictive-risk inference for ML forecasts when the evaluation derivative is zero. This paper handles the nonzero case.
- [**Double/Debiased Machine Learning for Treatment and Structural Parameters**](https://arxiv.org/abs/1608.00060) — Chernozhukov et al. The Neyman-orthogonal score and localization framework adapted here to chronological forecast fits.
- [**The Statistical Cost of Second-Order Orthogonality**](2026-11-23-arxiv-statistical-cost-second-order-orthogonality.md) (in this bank) — studies the quadratic bias left after first-order orthogonalization. That bias is the same term that drives this paper's residual over-rejection at short training windows.
- [**What a Forecasting Leaderboard Can Establish: Resolution Reporting for Zero-Shot Time-Series Models**](2026-11-25-arxiv-forecasting-leaderboard-resolution-zero-shot-time-series.md) (in this bank) — another look at when forecast-model rankings are statistically supported. It works at the level of benchmark leaderboards rather than paired risk tests.

### Jargon buster

- **Diebold–Mariano test** — a test of whether two forecasts have equal expected loss, built from the time series of their loss differences and its long-run variance.
- **Neyman orthogonality / locally robust score** — a moment whose expectation does not change, to first order, when plug-in estimates are slightly wrong. Small learning errors then bias the result only at second order.
- **Representer** — here, the direction that converts the evaluation-loss derivative into the training-objective geometry. Subtracting the training score along it cancels the first-order estimation effect.
- **Size distortion** — a test rejecting a true null more often than its nominal level, for example 34% instead of 5%.
- **β-mixing** — a measure of how fast dependence between distant time points decays. "Geometric" means it decays exponentially with the gap.
- **Bartlett long-run covariance** — a HAC variance estimator that sums down-weighted autocovariances, so standard errors account for serial correlation.
