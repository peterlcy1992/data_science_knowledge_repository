---
id: arxiv-time-varying-recalibration-forecast-distributions
title: "Time-Varying Recalibration of Forecast Distributions"
source: "UCL Statistical Science (arXiv stat.ME, Int. J. Forecasting)"
url: "https://arxiv.org/abs/2611.19452"
published: "2026-11"
added: "2026-11-18"
category: forecasting-timeseries
tags: [density-forecasting, forecast-combination, calibration, pit, linear-pool, score-driven-models, splines, bayesian-predictive-synthesis]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "catalog backlog (arXiv stat.ME scan)"
---

# Time-Varying Recalibration of Forecast Distributions

**Source:** [UCL Statistical Science (arXiv stat.ME, Int. J. Forecasting)](https://arxiv.org/abs/2611.19452) · Published 2026-11 · Added 2026-11-18
**Category:** Forecasting & Time Series · **Tags:** `density-forecasting`, `forecast-combination`, `calibration`, `pit`, `linear-pool`, `score-driven-models`, `splines`, `bayesian-predictive-synthesis`

## TL;DR

A post-processing layer that recalibrates *any* combined density forecast by applying a time-varying monotone map to its probability integral transform (PIT), leaving the combination weights untouched. The map is a Beta CDF or a rational quadratic spline, updated by score-driven (GAS) filters with dynamic model averaging, or by a "convolution" update whose inner map is set by a neural network from features of the current forecast's shape. On G10 exchange rates and US inflation, recalibration improves PIT uniformity; accuracy gains appear mainly where the original forecasts were miscalibrated.

## 1. Business context

Central banks and forecasters publish probabilistic forecasts, usually combinations of several models. Linear pools — the workhorse — are miscalibrated in general: even if every component is calibrated, diverse component means inflate the pool's variance (over-dispersion), and misspecified components distort location, spread or shape. Existing fixes (beta-transformed linear pool, Dirichlet-process mixtures of Betas, isotonic recalibration) are mostly static maps estimated once, which correct the *average* miscalibration and are wrong whenever it drifts; a two-parameter Beta can't fix multimodal PIT distortions. Adaptive conformal inference corrects intervals, not the full distribution.

## 2. Technical details

- **Framework.** Recalibrated CDF = map ∘ combined CDF. The recalibrated log score equals the original log score plus the log derivative of the map at the realised PIT, so the map can be updated sequentially; the expected gain is bounded by the divergence of the PIT distribution from uniformity.
- **Map families.** Beta CDF (location/spread errors) and rational quadratic spline (RQS; K=4–5 bins) for multimodal distortions.
- **Updates.** (i) Score-driven/GAS filters on map parameters, combined with dynamic model averaging over settings; (ii) a convolution method: an inner map whose parameters are produced by a small neural network (H=4–6 hidden units, refitted every 10–50 periods) from features describing the current forecast's shape, with a GAS map on top for what the shape doesn't reveal — so changes in miscalibration that follow changes in pool weights can be anticipated before they show up in PITs.
- **Evaluation.** PIT uniformity (KS, AD, χ² and other calibration tests), log score, CRPS, interval scores (IS90/IS95), and localized scores (CSLL/CSLR), with HAC Giacomini–White tests. Base forecasts: the Loss Discounting Framework (LDF) linear pool and Bayesian predictive synthesis (BPS).

## 3. Impact — potential & realized

**Simulations:** the RQS map corrects bimodal/trimodal miscalibration the Beta map can't; when miscalibration switches between regimes, the convolution update gives the largest log-score gains; with constant miscalibration a static map on an expanding window is hard to beat. **Exchange rates (nine G10):** the raw LDF pool is close to calibrated (KS doesn't reject any currency) and no method improves its log score significantly at 5% — significant changes are all losses, e.g. Static-RQS loses about 0.04 per month for NOK and CAD; Beta-GAS and Beta-Con never lose significantly; JPY, the most miscalibrated pool, rises from two to five passed calibration tests under every method. BPS is over-dispersed (90% intervals cover up to 96%) and gains: Beta-GAS and Beta-Con raise the log score for EUR, CHF and JPY by up to 0.05 per month and improve IS90 by about 7% for JPY. **US inflation (1961Q1–2014Q4, four-model pool):** the raw pool fails KS, AD and χ² at every discount factor (it tends to over-predict, with too heavy an upper tail); recalibration substantially improves PIT uniformity; on the shorter BPS window, adaptive maps improve the LDF pool's 95% interval score (Beta-GAS by 0.089), while static maps are worst. Code and data are public.

**Potential:** a drop-in calibration layer for production forecast ensembles (demand, capacity, finance) without re-estimating the combination.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Useful plumbing with an honest scorecard

The convolution idea — predict miscalibration from the shape of today's forecast instead of waiting for bad PITs — is the new piece; the rest is a careful combination of known parts. The empirical results are refreshingly candid: recalibrating an already-calibrated pool mostly adds noise, and gains track the original miscalibration. That gives practitioners a clean rule: test PIT uniformity first, and only add an adaptive map (Beta first, spline if PITs are multimodal) when the test fails or calibration drifts.

### Similar / related work

- [**Conformal Prediction for Multi-Step Forecasting: Conditional Coverage and Sharp Score Calibration Rates**](2026-11-10-arxiv-track-conformal-prediction-multi-step-forecasting.md) (in this bank) — interval-level calibration for forecasts, the alternative this paper contrasts with.
- [**How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration**](2026-11-03-arxiv-ctr-recalibration-temporal-evaluation-fresh-data.md) (in this bank) — post-hoc recalibration under drift in an ML setting.
- [**Accurate Uncertainties for Deep Learning Using Calibrated Regression**](https://arxiv.org/abs/1807.00263) (Kuleshov et al.) — static isotonic recalibration of predictive CDFs, cited as a limitation case.

### Jargon buster

- **PIT (probability integral transform)** — the forecast CDF evaluated at the realised outcome; uniform on (0,1) if the forecast is calibrated.
- **Linear pool** — a weighted average of component forecast distributions.
- **Score-driven (GAS) filter** — updates parameters each period in the direction of the gradient of the log score of the latest observation.
- **Bayesian predictive synthesis** — a combination method that models agents' biases and dependence through a dynamic latent factor model.
