---
id: arxiv-conformal-hierarchical-ev-charging-forecast
title: "Probabilistic Forecasting of Electric Vehicle Charging in a Time-varying Hierarchical Infrastructure"
source: "arXiv stat.AP (Principato et al.)"
url: "https://arxiv.org/abs/2610.13588"
published: "2026-10"
added: "2026-10-15"
category: forecasting-timeseries
tags: [hierarchical-forecasting, conformal-prediction, prediction-intervals, energy-demand]
novelty: 3
sourced_via: "web search"
---

# Probabilistic Forecasting of Electric Vehicle Charging in a Time-varying Hierarchical Infrastructure

**Source:** [arXiv stat.AP (Principato et al.)](https://arxiv.org/abs/2610.13588) · Published 2026-10 · Added 2026-10-15
**Category:** Forecasting & Time Series · **Tags:** `hierarchical-forecasting`, `conformal-prediction`, `prediction-intervals`, `energy-demand`

## TL;DR

Combines hierarchical forecasting with conformal prediction that tolerates missing data to produce valid prediction intervals at every node of a charging network (charge point to national) even as stations are added and removed. The CP-MNR-Nested algorithm handles the time-varying hierarchy.

## 1. Business context

EV charging demand is a source of power-system flexibility only if operators can quantify uncertainty, not just point forecasts. Demand is naturally hierarchical (charge points, sites, regions, national), and the hierarchy itself changes as stations come and go, which breaks standard reconciliation and calibration assumptions.

## 2. Technical details

The study uses a large dataset of public charging stations in Scotland. It couples hierarchical forecasting with conformal prediction methods that accommodate missing data, yielding valid intervals at every hierarchy node; the CP-MNR-Nested algorithm accounts for the time-varying structure. The abstract does not specify the base forecasting models, conformal variants, or evaluation setup (34 pages, full text not read).

## 3. Impact — potential & realized

The abstract states valid prediction intervals at all levels and a method that copes with a changing hierarchy; it reports no quantitative results. Potential: the same recipe applies to any hierarchical demand series with churn in the leaves, such as stores, SKUs or listings.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a sensible combination (hierarchical forecasting + missing-data-aware conformal) applied to a real network; abstract-level read only.

Distribution-free coverage at every level of a changing hierarchy is the practically attractive bit, and is the kind of guarantee demand planners rarely get. Without the numbers I can't judge interval width or efficiency, which is where conformal methods often pay a price.

### Similar / related work

- [**Benchmarking Time Series Foundation Models for Load Forecasting Under Covariate Uncertainty**](2026-10-12-arxiv-tsfm-load-forecasting-covariate-uncertainty.md) (in this bank) — energy forecasting with uncertainty
- **Conformal prediction (Vovk et al.)** — general conformal literature

### Jargon buster

- **Hierarchical forecasting** — Forecasting series that aggregate (e.g. charge point to region) so that forecasts at different levels stay consistent.
- **Conformal prediction** — A distribution-free way to wrap any forecaster with prediction intervals that have guaranteed coverage under exchangeability-type assumptions.
