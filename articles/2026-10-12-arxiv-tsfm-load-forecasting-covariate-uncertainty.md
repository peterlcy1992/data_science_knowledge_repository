---
id: arxiv-tsfm-load-forecasting-covariate-uncertainty
title: "Benchmarking Time Series Foundation Models for Load Forecasting Under Covariate Uncertainty"
source: "arXiv cs.LG (Kaljevic, Arzola, Zhang)"
url: "https://arxiv.org/abs/2610.07232"
published: "2026-10"
added: "2026-10-12"
category: forecasting-timeseries
tags: [time-series-foundation-models, load-forecasting, covariates, chronos-2, benchmark]
novelty: 3
sourced_via: "web search"
---

# Benchmarking Time Series Foundation Models for Load Forecasting Under Covariate Uncertainty

**Source:** [arXiv cs.LG (Kaljevic, Arzola, Zhang)](https://arxiv.org/abs/2610.07232) · Published 2026-10 · Added 2026-10-12
**Category:** forecasting-timeseries · **Tags:** `time-series-foundation-models`, `load-forecasting`, `covariates`, `chronos-2`, `benchmark`

## TL;DR

Four from-scratch models and four time-series foundation models are benchmarked for short-term load forecasting across three real datasets, varying whether future covariates are unavailable, known, or only noisily forecast. Chronos-2 wins when covariates are good but degrades as covariate forecasts get noisier; TimesNet is more robust under severe uncertainty.

## 1. Business context

Short-term load forecasting underpins reliable and efficient power-system operation. Foundation models for time series have done well on general forecasting tasks, but how they behave under realistic operating conditions, where weather and calendar inputs are themselves forecasts, has been little explored.

## 2. Technical details

Per the abstract, the study compares four models trained from scratch (the search summary names DLinear, PatchTST, Informer and TimesNet) with four foundation models (TimesFM 2.5, Chronos-2, Moirai 2.0, TiRex) on three real-world load datasets, in zero-shot and fine-tuned settings. Three covariate scenarios are tested: no future covariates, perfectly known covariates, and covariates available only as noisy forecasts.

## 3. Impact — potential & realized

Realized (abstract): Chronos-2 gives the best results in both zero-shot and fine-tuned settings when future covariates are available or accurately forecast, but its accuracy falls as covariate forecasts become noisier; TimesNet is more robust under severe covariate uncertainty. Potential: a template for stress-testing forecasters against realistic input noise rather than oracle covariates. No error figures were available from the abstract page; full text not reviewed.

*Sourced from web search / abstract-level content; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Useful honest-inputs benchmark, incremental in method.

The contribution is the evaluation design: scoring models when covariates are noisy forecasts, which is how deployment works, instead of with oracle weather. The ranking will not necessarily transfer beyond load data, and the abstract gives no error magnitudes, so treat the conclusion as directional.

### Similar / related work

- [**TimesFM-3: A Zero-Shot Foundation Model for Multivariate Forecasting**](2026-09-03-google-timesfm3-multivariate-forecasting.md) (in this bank) — another zero-shot forecasting foundation model, here compared head-to-head
- [**Running Demand Forecasting Machine Learning Models at Scale**](2026-09-19-picnic-scalable-demand-forecasting.md) (in this bank) — production forecasting at scale; contrast with benchmark conditions

### Jargon buster

- **Covariate uncertainty** — Inputs such as temperature that are known only through their own forecasts at prediction time.
- **Zero-shot** — Forecasting a series with a pretrained model without fitting to that series.
- **Short-term load forecasting** — Predicting electricity demand over the next hours to days.
