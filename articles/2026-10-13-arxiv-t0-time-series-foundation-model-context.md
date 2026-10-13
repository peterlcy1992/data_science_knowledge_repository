---
id: arxiv-t0-time-series-foundation-model-context
title: "t0: A Time-Series Foundation Model for Forecasting with Context"
source: "arXiv cs.LG (Meyer et al.)"
url: "https://arxiv.org/abs/2609.24559"
published: "2026-09"
added: "2026-10-13"
category: forecasting-timeseries
tags: [time-series-foundation-model, covariates, probabilistic-forecasting, gift-eval, open-weights]
novelty: 3
sourced_via: "web search"
---

# t0: A Time-Series Foundation Model for Forecasting with Context

**Source:** [arXiv cs.LG (Meyer et al.)](https://arxiv.org/abs/2609.24559) · Published 2026-09 · Added 2026-10-13
**Category:** forecasting-timeseries · **Tags:** `time-series-foundation-model`, `covariates`, `probabilistic-forecasting`, `gift-eval`, `open-weights`

## TL;DR

t0 is an open-weight family (102M and 256M parameters) of forecasting foundation models that condition on past and known-future covariates and emit quantile forecasts. t0-beta ranks third on GIFT-Eval, within 4.0% of the best zero-shot TSFM, per the abstract.

## 1. Business context

Most zero-shot forecasting models are univariate, yet real forecasts depend on covariates such as weather, prices and calendars. A model that uses covariates without per-task retraining would make foundation models more useful for operational forecasting such as energy.

## 2. Technical details

t0-alpha (102M) and t0-beta (256M) take target history, past covariates and known-future covariates; layers alternate attention across time and across variates; output is quantile (probabilistic) forecasts. Pretraining mixes curated public data with synthetic generators built to contain covariate→target dependencies. The authors analyse calibration, long-horizon rollout and robustness to missing data.

## 3. Impact — potential & realized

Realized (abstract): GIFT-Eval CRPS 0.4941 (alpha) and 0.4738 (beta), beta MASE 0.6865 and third place on both; fev-bench skill 42.2 / 46.7 (beta third, 2.0 points behind the leader); known-future covariates add 6.3 percentage points of skill across 30 tasks; both models cut MAE of a lagged-price baseline by 38% on 29 months of ERCOT hourly prices (independent evaluation). Potential: covariate-aware zero-shot forecasting for energy and demand.

*Sourced from web search / abstract-level content; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Third place, not first, but with open weights and explicit covariate conditioning, which is where practitioners usually need help.

Third place, not first, but with open weights and explicit covariate conditioning, which is where practitioners usually need help. The covariate gain (6.3 pp) and the 38% ERCOT improvement over a lagged-price baseline are worth testing, though a lagged-price baseline is weak; compare against a regression with the same covariates.

### Similar / related work

- [**Machine Learning and Time-Series Foundation Models for Day-Ahead Electricity Forecasting in a University Building**](2026-10-12-arxiv-timesfm-day-ahead-electricity-university-building.md) (in this bank) — TSFM vs XGBoost on covariates
- [**EXAONE Demand 1.0: A Time Series Foundation Model for Demand Forecasting**](https://arxiv.org/abs/2609.30880) — demand-specialised TSFM

### Jargon buster

- **CRPS** — Continuous Ranked Probability Score: scores a whole predictive distribution, lower is better.
- **Known-future covariates** — Inputs known ahead of time for the forecast horizon, such as calendar or scheduled prices.
- **Zero-shot** — Forecasting a new series with no training on it.
