---
id: arxiv-volatility-corrected-prediction-intervals-tsfm
title: "Volatility-Corrected Prediction Intervals: Locally Adaptive Uncertainty Quantification for Probabilistic Time-Series Forecasting"
source: "arXiv stat.ME (Cho & Matteson)"
url: "https://arxiv.org/abs/2610.31621"
published: "2026-10"
added: "2026-10-23"
category: forecasting-timeseries
tags: [prediction-intervals, garch, foundation-models, conformal, calibration]
novelty: 3
sourced_via: "web search"
---

# Volatility-Corrected Prediction Intervals: Locally Adaptive Uncertainty Quantification for Probabilistic Time-Series Forecasting

**Source:** [arXiv stat.ME (Cho & Matteson)](https://arxiv.org/abs/2610.31621) · Published 2026-10 · Added 2026-10-23
**Category:** Forecasting & Time Series · **Tags:** `prediction-intervals`, `garch`, `foundation-models`, `conformal`, `calibration`

## TL;DR

Forecast intervals can hit nominal marginal coverage while still miscovering during high-volatility stretches, because forecast errors are serially dependent and heteroskedastic. VCPI is a post-hoc GARCH-based multiplicative correction that makes intervals track local error variance.

## 1. Business context

Probabilistic forecasts are usually judged by marginal coverage (does 90% of the time the actual fall inside the 90% interval). Planning decisions, though, depend on whether the interval is right now, in the current regime. The authors show intervals can look calibrated overall while alternating between overcoverage and undercoverage over shorter windows.

## 2. Technical details

The authors name the failure mode local scale miscalibration and observe it in the native intervals of time-series foundation models. Volatility-Corrected Prediction Intervals (VCPI) is post-hoc: it takes the base forecaster's predictive scale as a baseline, models the volatility of standardized forecast residuals with a GARCH model, and applies a multiplicative correction to produce locally adaptive intervals. It is compared with model-agnostic conformal methods, and the paper includes a theoretical analysis of how intervals adapt after abrupt volatility changes. Experiments use Chronos, Moirai and TimesFM on four real-world datasets (not named in the abstract page I read). Authors: Jason B. Cho and David S. Matteson; submitted 22 Oct 2026.

## 3. Impact — potential & realized

Realized (as reported): VCPI gives more stable local coverage than conformal baselines while keeping near-nominal marginal coverage and comparable interval width. No quantitative coverage or width figures were visible at the abstract level. Potential: a drop-in uncertainty layer on top of any foundation-model forecaster.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sensible, cheap combination of GARCH volatility modelling with forecast-interval calibration, aimed at an under-checked failure of marginal coverage

Novelty 3/5 - Local coverage is a known weakness of conformal intervals, and GARCH-style volatility scaling is classical; the contribution is applying it as a post-hoc layer on foundation-model forecasters and showing the local miscalibration. Forecasting teams already using TSFMs are the likely adopters.

### Similar / related work

- [**Online Conditional Vine Copulas: Forecasting Electricity Demand**](2026-10-19-arxiv-online-conditional-vine-copulas-electricity.md) (in this bank) — another distributional-forecasting approach in this bank
- [**Conformal Policy Selection**](2026-10-19-arxiv-conformal-policy-selection-fdr-deployment.md) (in this bank) — conformal methods for decisions rather than intervals

### Jargon buster

- **Marginal coverage** — The fraction of all observations that fall inside the interval, averaged over time.
- **GARCH** — A model where today's error variance depends on recent squared errors and past variance, capturing volatility clustering.
- **Time-series foundation model** — A large pretrained forecaster (e.g. Chronos, Moirai, TimesFM) applied across datasets without per-series training.
