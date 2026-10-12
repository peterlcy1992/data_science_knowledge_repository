---
id: instacart-covariate-adjustment-power-analysis-clustered-data
title: "Unlocking 66% Faster Experiments with Covariate Adjustment: Power Analysis for Clustered Data, Ratio Metrics, and OLS Regression"
source: "Instacart Tech Blog (Tim Hesterberg, Benjamin Knight)"
url: "https://tech.instacart.com/unlocking-66-faster-experiments-with-covariate-adjustment-power-analysis-for-clustered-data-3a0c11c7baa6"
published: "2024-06"
added: "2026-10-12"
category: experimentation-causal
tags: [covariate-adjustment, power-analysis, clustered-standard-errors, ratio-metrics, ols]
novelty: 3
sourced_via: "web search"
---

# Unlocking 66% Faster Experiments with Covariate Adjustment: Power Analysis for Clustered Data, Ratio Metrics, and OLS Regression

**Source:** [Instacart Tech Blog (Tim Hesterberg, Benjamin Knight)](https://tech.instacart.com/unlocking-66-faster-experiments-with-covariate-adjustment-power-analysis-for-clustered-data-3a0c11c7baa6) · Published 2024-06 · Added 2026-10-12
**Category:** experimentation-causal · **Tags:** `covariate-adjustment`, `power-analysis`, `clustered-standard-errors`, `ratio-metrics`, `ols`

## TL;DR

Instacart describes one residual-based way to compute standard errors for A/B tests with clustered data, ratio metrics and covariate adjustment, usable for both pre-experiment power analysis and post-experiment inference. It reports a median 66% variance reduction on a key metric from covariate adjustment, which would shorten experiments by about that much.

## 1. Business context

Most off-the-shelf power tools assume independent observations and plain t-tests, which does not fit Instacart: customers place multiple orders, so order-level metrics are clustered, and many key metrics are ratios. Without correct standard errors, power analysis is misleading and experiments run longer than needed.

## 2. Technical details

Per the search-surfaced summary, the authors give a single framework based on the sample variance of certain residuals. It covers clustered data, ratio metrics and OLS covariate adjustment without computing covariance matrices, and is numerically stable so it can plug into standard tooling. Formulas were not available; the post itself returned HTTP 403 to direct fetch.

## 3. Impact — potential & realized

Realized (authors' own estimate): covariate adjustment gives a median 66% variance reduction for a key metric, implying experiments could run roughly that much shorter. Potential: accurate power calculations on historical data and consistent inference after the test from the same code path. No independent evaluation seen.

*Sourced from web search / abstract-level content; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid practitioner reference; not a new idea.

Correct clustered, ratio-metric inference is a place where many in-house platforms are quietly wrong, so a documented, matrix-free recipe is valuable. The 66% figure is a median on one metric at one company and should not be assumed elsewhere. Published in 2024, so this is a catch-up entry rather than fresh news.

### Similar / related work

- [**Variance reduction combining pre-experiment and in-experiment data**](2026-10-08-etsy-variance-reduction-pre-and-in-experiment-data.md) (in this bank) — extends regression adjustment with vetted in-experiment covariates

### Jargon buster

- **Clustered data** — Observations grouped by a unit, such as orders within a customer, that are not independent.
- **Ratio metric** — A metric defined as one total divided by another, such as revenue per order.
- **Covariate adjustment** — Regressing the outcome on pre-experiment variables to remove explainable variance.
