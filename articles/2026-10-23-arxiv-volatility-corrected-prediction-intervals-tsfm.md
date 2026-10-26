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
sourced_via: "full-text fetch"
---

# Volatility-Corrected Prediction Intervals: Locally Adaptive Uncertainty Quantification for Probabilistic Time-Series Forecasting

**Source:** [arXiv stat.ME (Cho & Matteson)](https://arxiv.org/abs/2610.31621) · Published 2026-10 · Added 2026-10-23
**Category:** forecasting-timeseries · **Tags:** `prediction-intervals`, `garch`, `foundation-models`, `conformal`, `calibration`

## TL;DR

Forecast intervals can hit nominal marginal coverage while still miscovering during high-volatility stretches, because forecast errors are serially dependent and heteroskedastic. VCPI is a post-hoc GARCH-based multiplicative correction on top of a forecaster's own predictive scale that makes intervals track local error variance; across three time-series foundation models and four datasets it gives the lowest rolling coverage error against conformal baselines.

## 1. Business context

Probabilistic forecasts are usually judged by marginal coverage: does 80% of the time the actual fall inside the 80% interval. Planning decisions depend on whether the interval is right now, in the current regime, and uncertainty matters most in periods of stress, peak demand or rapid regime change. The authors name the failure mode local scale miscalibration. Their motivating example is Capital Bikeshare daily rentals with rolling 16-step-ahead forecasts from Chronos, Moirai 2 and TimesFM 2.5: errors cluster in the high-demand summer months, and empirical coverage of the nominal 80% intervals, computed over 100 consecutive forecasts, drops below 60% in some periods.

## 2. Technical details

VCPI is post-hoc and keeps the forecaster's point forecast. Step 1: fit a Gaussian reference scale σ̂_t to the forecaster's reported predictive quantiles by least squares. Step 2: standardize forecast residuals by that scale (e_t = s_t·ξ_t) and model the scale correction s_t with a GARCH-family model (GARCH(1,1): s_t² = ω + a·e²_{t-1} + b·s²_{t-1}); the variance specification and the standardized error distribution F are selected jointly on a temporally ordered validation segment inside the calibration window by validation coverage error, then refitted on the full window. Step 3: the interval is f̂_t + σ̂_t·s̃_t·F̃⁻¹(α/2) to f̂_t + σ̂_t·s̃_t·F̃⁻¹(1−α/2). With the true s_t and a continuous F this has conditional coverage 1−α.

Theory: conditional on a specified shock event and under stated assumptions, after a sufficiently large upward volatility jump the first-step GARCH update is closer to the post-jump oracle interval than the analysed quantile-tracking (QT) updates, because QT reacts to whether the last interval covered rather than by how much it missed, whereas GARCH uses the squared error directly. Experiments: Chronos, Moirai and TimesFM on four datasets (Bike Rental Counts, Colorado River, Electricity Demand, NO2 Concentration), horizon blocks 1–4, 5–8, 9–16, nominal 80% coverage, against the native intervals, ACI, QT, EnbPI and SPCI. The primary metric is rolling root mean squared coverage error (RMSCE), with marginal coverage and median width as complementary summaries.

## 3. Impact — potential & realized

Realized (as reported): VCPI yields the smallest RMSCE in the paper's summary across the three models and four datasets, while remaining broadly competitive on marginal coverage and width. For example, on Bike Rental Counts at horizons 1–4, Chronos RMSCE goes from 0.079 (native) to 0.051 with VCPI, against 0.096–0.109 for the conformal baselines. Widths are comparable rather than uniformly smaller (e.g. TimesFM on Bike Rental at horizons 1–4: 2261 for VCPI versus 2051 native), and the conformal methods sometimes undercover marginally (e.g. EnbPI and SPCI near 0.73–0.77 at longer horizons on bike rentals).

Stated limitations: VCPI relies on a parametric GARCH-family scale model and a parametric standardized error distribution, so misspecification can leak into the intervals; multi-step GARCH forecasts mean-revert to the unconditional variance quickly, degrading the correction beyond roughly 4–8 steps; and 95% tail coverage is more sensitive to distributional misspecification than moderate coverage. Potential: a drop-in uncertainty layer on any forecaster that reports quantiles.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sensible, cheap combination of classical GARCH volatility modelling with forecast-interval calibration, aimed at an under-checked failure of marginal coverage.

Local coverage is a known weakness of conformal intervals, and GARCH-style scaling is classical; the contribution is documenting local scale miscalibration in foundation-model intervals and showing a small post-hoc layer fixes much of it. The honest reading of the results is 'more stable local coverage at comparable width', not uniformly tighter intervals. Forecasting teams already using TSFMs for demand or load planning are the likely adopters, and the RMSCE-style rolling-coverage check is worth borrowing even without VCPI.

### Similar / related work

- [**Online Conditional Vine Copulas: Forecasting Electricity Demand**](2026-10-19-arxiv-online-conditional-vine-copulas-electricity.md) (in this bank) — another distributional-forecasting approach in this bank
- [**Conformal Policy Selection**](2026-10-19-arxiv-conformal-policy-selection-fdr-deployment.md) (in this bank) — conformal methods for decisions rather than intervals
- [**Probabilistic Forecasting of Electric Vehicle Charging in a Time-varying Hierarchical Infrastructure**](2026-10-15-arxiv-conformal-hierarchical-ev-charging-forecast.md) (in this bank) — conformal calibration for hierarchical probabilistic forecasts

### Jargon buster

- **Marginal coverage** — The fraction of all observations that fall inside the interval, averaged over time.
- **Local scale miscalibration** — Coverage that is right on average but alternates between over- and undercoverage as the error scale changes.
- **GARCH** — A model where today's error variance depends on recent squared errors and past variance, capturing volatility clustering.
- **RMSCE** — Rolling root mean squared coverage error: how far windowed empirical coverage strays from the nominal level.
- **Time-series foundation model** — A large pretrained forecaster (e.g. Chronos, Moirai, TimesFM) applied across datasets without per-series training.
