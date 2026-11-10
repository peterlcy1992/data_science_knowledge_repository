---
id: arxiv-track-conformal-prediction-multi-step-forecasting
title: "Conformal Prediction for Multi-Step Forecasting: Conditional Coverage and Sharp Score Calibration Rates"
source: "arXiv stat.ME (Siyuan He, Yuhong Yang)"
url: "https://arxiv.org/abs/2611.12004"
published: "2026-11"
added: "2026-11-10"
category: forecasting-timeseries
tags: [conformal-prediction, multi-step-forecasting, conditional-coverage, minimax, kernel-calibration]
novelty: 3
sourced_via: "full-text fetch"
---

# Conformal Prediction for Multi-Step Forecasting: Conditional Coverage and Sharp Score Calibration Rates

**Source:** [arXiv stat.ME (Siyuan He, Yuhong Yang)](https://arxiv.org/abs/2611.12004) · Published 2026-11 · Added 2026-11-10
**Category:** forecasting-timeseries · **Tags:** `conformal-prediction`, `multi-step-forecasting`, `conditional-coverage`, `minimax`, `kernel-calibration`

## TL;DR

TRACK (Time series Residual Analysis for Calibration with Kernels) builds one-step and joint multi-step prediction sets from rolling-window forecasters by kernel-estimating conditional quantiles of normalised residual scores. The paper gives finite-sample bounds accounting for temporal dependence and overlapping score windows, plus matching minimax bounds, and shows lower conditional coverage deviation on wind generation and bike-share demand.

## 1. Business context

Decisions often depend on forecasts over several horizons, and point forecasts hide uncertainty. Conformal prediction gives distribution-free guarantees under exchangeability, which time series violate; errors across horizons are dependent and differ in scale, and joint coverage across horizons is wanted.

## 2. Technical details

A normalised residual score handles heterogeneous uncertainty across horizons and reduces joint prediction to conditional quantile estimation; kernel-based calibration adapts the set to the new covariate value. The analysis allows predictor memory and horizons to grow with sample size, covers rolling-window forecasters (and predictors with an accurate rolling-window approximation), and gives (1) finite-sample calibration and marginal/group-conditional coverage bounds, (2) conditional quantile and pointwise conditional coverage bounds, (3) minimax rates over score maps with a given window span, showing that span alone does not determine calibration difficulty. Experiments: simulations, hourly generation at the Hackberry Wind Project and hourly Capital Bikeshare demand.

## 3. Impact — potential & realized

Realized (as reported): lower conditional coverage deviations, competitive marginal coverage and interval width. Potential: a principled way to attach calibrated joint intervals to existing rolling forecasters. I did not extract specific numeric results.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Theory-first contribution on a practical need; applied value depends on how well kernel conditioning scales to richer covariates.

Marginal coverage can look fine while coverage in a specific regime (e.g. low-wind hours) is off; this paper targets that gap. Useful reading for anyone shipping prediction intervals for demand or capacity planning.

### Similar / related work

- [**Adaptive Conformal Inference (Gibbs & Candès)**](https://arxiv.org/abs/2106.00170) — sequential/adaptive calibration for time series

### Jargon buster

- **Conformal prediction** — A wrapper that turns any predictor into prediction sets with finite-sample coverage guarantees under exchangeability.
- **Conditional coverage** — Coverage that holds within sub-regions of the covariate space, not just on average.
- **Minimax rate** — The best worst-case accuracy attainable over a class of problems.
