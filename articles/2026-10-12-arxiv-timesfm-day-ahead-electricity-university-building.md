---
id: arxiv-timesfm-day-ahead-electricity-university-building
title: "Machine Learning and Time-Series Foundation Models for Day-Ahead Electricity Forecasting in a University Building"
source: "arXiv cs.LG (Vasulkar, Kernan Freire, de Leeuw, Salcedo-Rahola)"
url: "https://arxiv.org/abs/2610.12638"
published: "2026-10"
added: "2026-10-12"
category: forecasting-timeseries
tags: [timesfm, xgboost, day-ahead-forecasting, seasonal-naive, covariates]
novelty: 3
sourced_via: "web search"
---

# Machine Learning and Time-Series Foundation Models for Day-Ahead Electricity Forecasting in a University Building

**Source:** [arXiv cs.LG (Vasulkar, Kernan Freire, de Leeuw, Salcedo-Rahola)](https://arxiv.org/abs/2610.12638) · Published 2026-10 · Added 2026-10-12
**Category:** forecasting-timeseries · **Tags:** `timesfm`, `xgboost`, `day-ahead-forecasting`, `seasonal-naive`, `covariates`

## TL;DR

On one university building, TimesFM 3.0 with covariates cuts MAE about 43% versus a weekly seasonal-naive baseline, but paired daily comparisons show XGBoost is not clearly worse, and covariates help mainly on holidays.

## 1. Business context

Day-ahead electricity forecasts let building operators plan heating, ventilation and other services. The practical question is whether a pretrained foundation model is worth using over a locally fitted model.

## 2. Technical details

Per the abstract, statistical, machine-learning, recurrent (LSTM) and pretrained TimesFM models are compared using chronological validation, with every configuration scored on the same 57 test days split into workdays, weekends and holidays. Weather covariates use retrospective observations, and fit/forecast times are recorded. A historical evaluation shows seasonal variation, and swapping weather sources changes the chosen TimesFM configuration only slightly.

## 3. Impact — potential & realized

Realized (abstract): TimesFM 3.0 with covariates has the lowest overall errors, about 43% lower MAE than weekly seasonal-naive. XGBoost is competitive, with no clear MAE advantage for TimesFM in paired daily comparisons. TimesFM also does well using only past consumption and needs no building-specific training; XGBoost is fast to fit and run; the LSTM is slower and not better. Covariates improve holiday forecasts but slightly worsen workday and weekend ones, so overall MAE barely moves. Potential: pretrained TimesFM as a strong first baseline for new buildings.

*Sourced from web search / abstract-level content; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Sensible small-scale baseline study; single building limits generality.

Its most useful habits are the paired daily comparison and the seasonal-naive reference, which stop a 43% headline from overstating a gap that a tuned gradient-boosted model largely closes. One building and 57 test days means conclusions are specific to this site.

### Similar / related work

- [**TimesFM-3: A Zero-Shot Foundation Model for Multivariate Forecasting**](2026-09-03-google-timesfm3-multivariate-forecasting.md) (in this bank) — the model family evaluated here
- [**Buy One Get One Free: Promotion-Aware Demand Forecasting for Groceries**](2026-09-23-afresh-promotion-aware-demand-forecasting.md) (in this bank) — covariate-aware forecasting where exogenous inputs matter in specific regimes

### Jargon buster

- **Seasonal-naive** — Forecast equal to the value from the same time one season (here a week) earlier.
- **MAE** — Mean absolute error, the average size of forecast misses in the original units.
- **Paired comparison** — Comparing two models day by day on the same days, so shared difficulty cancels out.
