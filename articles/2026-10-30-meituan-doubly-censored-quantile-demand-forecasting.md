---
id: meituan-doubly-censored-quantile-demand-forecasting
title: "A Deep Learning Framework for Quantile Demand Forecasting in E-commerce with Doubly Censored Data"
source: "arXiv cs.LG / CIKM '26 (Meituan)"
url: "https://arxiv.org/abs/2610.40138"
published: "2026-10"
added: "2026-10-30"
category: forecasting-timeseries
tags: [demand-forecasting, censored-data, quantile-regression, calibration, inventory, newsvendor]
novelty: 3
sourced_via: "full-text fetch"
---

# A Deep Learning Framework for Quantile Demand Forecasting in E-commerce with Doubly Censored Data

**Source:** [arXiv cs.LG / CIKM '26 (Meituan)](https://arxiv.org/abs/2610.40138) · Published 2026-10 · Added 2026-10-30
**Category:** Forecasting & Time Series · **Tags:** `demand-forecasting`, `censored-data`, `quantile-regression`, `calibration`, `inventory`, `newsvendor`

## TL;DR

Meituan's CIKM '26 paper trains deep quantile forecasters when sales are both capped by stock (right-censoring) and boosted by promotions (left-censoring). It proposes the Doubly Portnoy Estimator (DPE), an iterative re-weighting training algorithm, and Extended D-Calibration, a metric for judging calibration under double censoring, and reports an 8% lower overstock rate at a fixed stockout SKU ratio in a 7-day online A/B test.

## 1. Business context

Retail forecasting targets underlying demand, but observed sales are capped by stock and inflated by temporary promotions, so quantile regression on sales is biased; discarding censored rows throws away usable information, and ad hoc business-rule corrections cannot be verified without true demand. Quantile forecasts feed newsvendor-style inventory decisions.

## 2. Technical details

DPE borrows re-weighting ideas from survival analysis to train any deep network end-to-end with quantile (pinball-type) loss on doubly censored labels; the authors give a formal proof of its properness under double censoring. Extended D-Calibration extends D-calibration from survival analysis to assess calibration of competing models. Evaluation: 300,000 synthetic samples per run (60/20/20 split) with known oracle calibration, and two Meituan datasets, Youxuan (community group-buying; 8.52M records, 19.84% right- and 3.56% left-censored) and Maicai (online supermarket; 18.07M records, 18.52% and 6.26%). Baselines include CQRNN, an exclude-censored model, S-CRPS and LogNorm.

## 3. Impact — potential & realized

Realized (as reported): in simulation Extended D-Calibration tracks the oracle calibration best (Kendall's tau 0.740, Spearman 0.842), whereas standard ECE correlates negatively (tau -0.220). In the main comparison DPE's Extended D-Calibration exceeds the second-best by 44.16% and CRPS improves 6.52%. On Youxuan DPE ranks second on both calibration and sharpness (LogNorm has marginally lower calibration error, 0.039 vs 0.040, but 41.3% worse sharpness); on Maicai DPE has the lowest Extended D-Calibration (0.05 vs 0.07 for CQRNN). Inventory simulation: at an overstocking rate of 0.25, stockout ratio 0.23 vs 0.25 for S-CRPS. A 7-day A/B test randomising products across warehouses and subcategories reports 8% lower overstock rate at a fixed stockout SKU ratio versus the incumbent online algorithm.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid applied statistics: a survival-analysis idea ported to retail quantile forecasting with a matching metric, validated by a (short) randomised test.

The most reusable idea is the evaluation metric, since plain ECE can reward the wrong model under censoring. The online test is only 7 days and the reported unit is SKU-level overstock/stockout; the paper does not claim profit effects here.

### Similar / related work

- [**Probabilistic demand estimation with stockout substitution**](2026-10-27-arxiv-demand-estimation-stockout-substitution-exact-mle.md) (in this bank) — another censored-demand estimation paper in this bank
- [**Volatility-corrected prediction intervals for TSFMs**](2026-10-23-arxiv-volatility-corrected-prediction-intervals-tsfm.md) (in this bank) — uncertainty calibration for forecasts

### Jargon buster

- **Censoring** — The true value is only known to lie above (right) or below (left) the observed number.
- **D-calibration** — A calibration test from survival analysis checking that predicted probability mass is spread correctly.
- **Pinball loss** — The asymmetric loss minimised by a quantile.
