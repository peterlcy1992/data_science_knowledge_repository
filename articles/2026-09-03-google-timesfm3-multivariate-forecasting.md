---
id: google-timesfm3-multivariate-forecasting
title: "TimesFM-3: A Zero-Shot Foundation Model for Multivariate Forecasting"
source: "Google Research"
url: "https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/"
published: "2026-08"
added: "2026-09-03"
category: forecasting-timeseries
tags: [foundation-model, time-series, zero-shot, multivariate-forecasting, transformer]
novelty: 4
sourced_via: "full-text fetch"
---

# TimesFM-3: A Zero-Shot Foundation Model for Multivariate Forecasting

**Source:** [Google Research](https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/) · Published 2026-08 · Added 2026-09-03
**Category:** Forecasting & Time Series · **Tags:** `foundation-model`, `time-series`, `zero-shot`, `multivariate-forecasting`, `transformer`

## TL;DR

TimesFM-3 is the third generation of Google's time-series foundation model and the first version trained natively for multivariate, zero-shot forecasting — jointly forecasting multiple correlated series plus known and historical covariates (like promotions or weather) without any fine-tuning — and it currently ranks first on three major forecasting leaderboards.

## 1. Business context

Real-world forecasting problems — retail demand, financial series, infrastructure observability, manufacturing throughput — rarely involve a single isolated series. They involve several correlated series (e.g., sales across related SKUs) plus external covariates that shift the outcome (a promotion, a weather event, foot traffic). Prior forecasting foundation models, including earlier TimesFM generations, were built primarily for univariate series and needed per-task fine-tuning or bespoke feature engineering to bring covariates in. TimesFM-3 targets forecasting teams who want a single pretrained model that already understands cross-series correlation and covariates out of the box.

## 2. Technical details

- **Architecture:** a 330M-parameter decoder-only transformer with alternating causal temporal attention (across time within a series) and full variate attention (across correlated series at the same time step).
- **Pretraining scale:** over 1 trillion real and synthetic time points.
- **Decoding:** non-autoregressive, single-pass decoding via a technique the team calls "Contiguous Patch Masking," processing the forecast horizon in 32-step patches rather than one step at a time — a departure from the step-by-step autoregressive decoding common in earlier time-series foundation models.
- **Probabilistic output:** produces 9 quantiles (10th to 90th percentile) per target series, giving a native probabilistic forecast rather than a single point estimate.
- **Covariate support:** natively supports both historical-only covariates and known-future covariates (e.g., a scheduled promotion or forecasted weather) without any fine-tuning step.
- **Availability:** released on GitHub and Hugging Face, with BigQuery integration described as planned.

## 3. Impact — potential & realized

- **Realized:** ranks first among pretrained foundation models on the Gift-Eval, FEV-Bench, and TIME leaderboards, for both point and probabilistic forecasting; matches competing models' accuracy even when run in univariate-only mode, with additional gains unlocked in multivariate mode.
- **Potential:** a genuinely zero-shot multivariate forecaster removes a real integration cost for teams that currently either fine-tune per-task models or drop covariates entirely because wiring them in was expensive — retail demand planning with promotions, observability with correlated infrastructure metrics, and manufacturing lines with shared upstream drivers are the kinds of problems the write-up frames as directly addressable.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a genuine architectural step for zero-shot forecasting, not just a bigger model

Native zero-shot multivariate forecasting with built-in covariate support is a real capability gap that earlier time-series foundation models (including TimesFM-2 and comparable models like Chronos) mostly left to fine-tuning or manual feature pipelines. The full variate attention plus non-autoregressive patch decoding is a specific, well-motivated architectural choice rather than a scale-up of an existing recipe. It's a 4 rather than a 5 because leaderboard-topping claims from the model's own creators warrant some independent replication before treating this as a settled result, and the underlying idea of applying transformer-style cross-series attention to time series builds on an active existing research direction rather than inventing a new one from scratch.

### Similar / related work

- [**Introducing WeatherNext 3**](2026-09-03-google-weathernext3-weather-forecasting.md) (in this bank) — a sibling Google forecasting foundation model from the same week, but domain-specific (global weather, satellite-fed) rather than TimesFM-3's general-purpose, zero-shot design across arbitrary time-series domains.
- **Chronos** (Amazon Science) — a comparable open time-series foundation model family that TimesFM-3 is implicitly benchmarked against via the shared leaderboards (Gift-Eval, FEV-Bench); unlinked here as no specific URL was confirmed in this research pass.

### Jargon buster

- **Zero-shot forecasting** — producing a forecast for a new series or domain the model was never specifically fine-tuned on, relying only on pretraining.
- **Variate attention** — an attention mechanism that lets the model look across multiple correlated time series at the same time step, rather than only along time within one series.
- **Covariate** — an external variable (e.g., a promotion flag, a weather forecast) that influences the series being forecast but is not itself the forecast target.
- **Non-autoregressive decoding** — generating an entire forecast horizon (or large chunks of it) in one pass, instead of predicting one time step at a time and feeding each prediction back in.
