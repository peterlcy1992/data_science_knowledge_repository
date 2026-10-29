---
id: arxiv-point-in-time-leakage-electricity-forecast-archives
title: "The Hidden Look-Ahead: Point-in-Time Leakage in Electricity Market Data"
source: "arXiv (energy forecasting / econometrics)"
url: "https://arxiv.org/abs/2610.25389"
published: "2026-10"
added: "2026-10-29"
category: forecasting-timeseries
tags: [data-leakage, point-in-time, backtesting, electricity-markets, training-serving-skew, weather-forecasts]
novelty: 4
sourced_via: "full-text fetch"
---

# The Hidden Look-Ahead: Point-in-Time Leakage in Electricity Market Data

**Source:** [arXiv (energy forecasting / econometrics)](https://arxiv.org/abs/2610.25389) · Published 2026-10 · Added 2026-10-29
**Category:** Forecasting & Time Series · **Tags:** `data-leakage`, `point-in-time`, `backtesting`, `electricity-markets`, `training-serving-skew`, `weather-forecasts`

## TL;DR

Studies of electricity prices say they use only information available at decision time, but forecast archives index runs by model issue time, not publication time. Matching 128,656 forecast runs from ten weather-model configurations to Great Britain's day-ahead and intraday auction gates (2022-2026), the paper finds the naive 'latest run issued before the gate' picks a not-yet-published run on more than 99% of delivery days for six of ten configurations at one of the two gates.

## 1. Business context

Backtests and published empirical studies feed trading and forecasting decisions. If the features were not actually available at the gate, backtested accuracy is overstated and a model trained on them is later served older inputs, a training-serving skew that degrades performance for no visible reason. The problem concerns reconstructed history, not live trading.

## 2. Technical details

The paper formalises three timing pitfalls: (1) confusing a run's issue time with its publication time (a run becomes available hours after its issue time and keeps changing); (2) stating auction gate closures in UTC when auctions follow local clock time; (3) using outturn series that are revised after publication without keeping earlier values. It distinguishes run-availability leakage from exposure to values revised after the gate. Data: a commercial archive with wind, solar PV and demand forecasts from ten weather-model configurations, publication and finalisation timestamps, matched to the two GB gates. It compares a naive rule against a publication rule and a finalisation rule, and proposes a protocol that audits point-in-time correctness from timestamps before any model is fitted, validated by direct observation of publication times.

## 3. Impact — potential & realized

Realized (this vendor, this market, 2022-2026): for GFS at the day-ahead gate the share of delivery days with an unpublished selected run is 0.6% in winter and 99.8% in summer (ICON: 1.0% and 23.5%); stating the gate in UTC alone makes a publication rule select an unpublished GFS run on 98.9% of summer days at the day-ahead gate; publication delays drift over time, and an action margin of a few minutes can cost a full six-hour forecast cycle. Wherever the rules choose different runs the inputs differ materially (2-7% of mean outturn for wind and solar, 1-2% for demand), yet the effect on apparent accuracy ranges from -9% to +24% across variables, models, gates and seasons, so its direction and size cannot be assumed. Leakage depends on configuration, gate and season, not on the forecast variable. The authors caution that magnitudes are specific to this archive and market, while the mechanisms are general.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Unglamorous but high-value: a measured audit showing that a very natural SQL-style query leaks future information, with a reusable timestamp-based protocol. The sign of the accuracy effect is not predictable, which is the real lesson.

Applies well beyond energy: any backtest that joins on event time rather than availability time (ML features, vendor data, revised macro series) carries the same risk. Teams should audit timestamps before trusting a backtest.

### Similar / related work

- [**Time-series foundation models for load forecasting with covariate uncertainty**](2026-10-12-arxiv-tsfm-load-forecasting-covariate-uncertainty.md) — forecast-covariate handling in energy load forecasting
- [**Volatility-corrected prediction intervals for time-series foundation models**](2026-10-23-arxiv-volatility-corrected-prediction-intervals-tsfm.md) — another evaluation-hygiene piece for forecasting

### Jargon buster

- **Point-in-time correctness** — Every feature in a historical dataset is exactly what was available at the moment of the decision.
- **Gate closure** — The deadline for submitting bids in an electricity auction.
- **Training-serving skew** — A mismatch between the data a model was trained on and what it sees in production.
