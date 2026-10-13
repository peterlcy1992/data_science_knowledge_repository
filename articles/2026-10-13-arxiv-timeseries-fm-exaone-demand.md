---
id: arxiv-timeseries-fm-exaone-demand
title: "EXAONE Demand 1.0: A Time Series Foundation Model for Demand Forecasting"
source: "arXiv cs.AI (Lee et al., LG AI Research)"
url: "https://arxiv.org/abs/2609.30880"
published: "2026-09"
added: "2026-10-13"
category: forecasting-timeseries
tags: [time-series-foundation-model, demand-forecasting, intermittent-demand, lora-adapter, synthetic-data]
novelty: 3
sourced_via: "web search"
---

# EXAONE Demand 1.0: A Time Series Foundation Model for Demand Forecasting

**Source:** [arXiv cs.AI (Lee et al., LG AI Research)](https://arxiv.org/abs/2609.30880) · Published 2026-09 · Added 2026-10-13
**Category:** forecasting-timeseries · **Tags:** `time-series-foundation-model`, `demand-forecasting`, `intermittent-demand`, `lora-adapter`, `synthetic-data`

## TL;DR

EXAONE Demand pairs a 11.3M-series demand corpus with demand-aware low-rank adapters on a frozen general TSFM backbone, and reports beating 36 other time-series foundation models on 22 held-out datasets.

## 1. Business context

General time-series foundation models are pretrained mostly on non-demand data. Demand series have short histories, frequent zeros, stock-out censoring and unrecorded exogenous events, so zero-shot general models can be a poor fit for retail and supply-chain forecasting.

## 2. Technical details

Two components. (1) A demand corpus of 11.3M series and 48.4B observations from 73 sources, plus a synthetic generator for behaviours underrepresented in open data. (2) A demand-aware adapter: low-rank branches attached to a frozen general-domain backbone, one per demand class (smooth, intermittent, erratic, lumpy), with a router that weights the branches using eight scale-free statistics of the input series. Two variants: real+synthetic and synthetic-only.

## 3. Impact — potential & realized

Realized (abstract): both variants outperform 36 TSFMs on 22 held-out datasets, and adding real demand data beats synthetic-only. The abstract gives no error metrics (MAE/WAPE/CRPS) or effect sizes, so the size of the gain is unclear. Potential: class-aware adapters are a cheap way to specialise a general model to intermittent demand.

*Sourced from web search / abstract-level content; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Using the classic smooth/intermittent/erratic/lumpy demand taxonomy as a routing signal is a nice bridge between forecasting practice and foundation models.

Using the classic smooth/intermittent/erratic/lumpy demand taxonomy as a routing signal is a nice bridge between forecasting practice and foundation models. Without reported metrics, and with a corpus the authors control, the headline is hard to weigh; the useful test is against tuned local statistical baselines (e.g. Croston-type methods) on your own data.

### Similar / related work

- [**Benchmarking Time Series Foundation Models for Load Forecasting Under Covariate Uncertainty**](2026-10-12-arxiv-tsfm-load-forecasting-covariate-uncertainty.md) (in this bank) — TSFM benchmark in this bank
- [**t0: A Time-Series Foundation Model for Forecasting with Context**](https://arxiv.org/abs/2609.24559) — another open TSFM, covariate-aware

### Jargon buster

- **Intermittent demand** — Series with many zero periods and occasional sales, which break standard error metrics and models.
- **Low-rank adapter** — A small trainable add-on (low-rank matrices) on a frozen model, used to specialise it cheaply.
- **Censoring (stock-out)** — When sales are capped by available stock, observed sales understate true demand.
