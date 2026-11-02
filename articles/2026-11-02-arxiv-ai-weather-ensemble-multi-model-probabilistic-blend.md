---
id: arxiv-ai-weather-ensemble-multi-model-probabilistic-blend
title: "Value of Adding AI Weather Model Ensembles to a Multi-model Probabilistic Blend"
source: "arXiv physics.ao-ph (Exeter / Met Office)"
url: "https://arxiv.org/abs/2610.42130"
published: "2026-10"
added: "2026-11-02"
category: forecasting-timeseries
tags: [forecast-blending, ensemble, crps, calibration, emos, probabilistic-forecasting]
novelty: 3
sourced_via: "full-text fetch"
---

# Value of Adding AI Weather Model Ensembles to a Multi-model Probabilistic Blend

**Source:** [arXiv physics.ao-ph (Exeter / Met Office)](https://arxiv.org/abs/2610.42130) · Published 2026-10 · Added 2026-11-02
**Category:** forecasting-timeseries · **Tags:** `forecast-blending`, `ensemble`, `crps`, `calibration`, `emos`, `probabilistic-forecasting`

## TL;DR

Blending the AI ensemble AIFS-CRPS with the Met Office physics-based MOGREPS-UK raises probabilistic skill over UK site temperature forecasts, and a CRPS decomposition shows gains come from weighting skilful models more and from diverse (complementary) errors. Calibrating sources before blending and the blend afterwards helps further.

## 1. Business context

Weather centres blend ensembles from different systems for accuracy. Deterministic AI models have been blended with physics-based ones before, but adding an ensemble AI model, and the role of post-processing before and after blending, had not been studied. The lessons apply to any forecast-combination problem.

## 2. Technical details

Data: site screen temperature (10 m wind speed in the appendix) at 130 UK sites, 1 Oct 2024–31 Jan 2025 (123 days), 00Z validity, daily lead times. Models: MOGREPS-UK, MOGREPS-G, IFS and AIFS-CRPS (trained with CRPS as loss). Processing uses the Met Office's open-source IMPROVER system; calibration by ensemble model output statistics (EMOS); the blend is a linear pool with skill-based weights (e.g. 80/20 for two models; 50/30/20 MOGREPS-UK/IFS/AIFS for three). Scores: CRPS, RMSE, Brier score with Murphy decomposition (reliability/resolution), spread–skill ratio. The blend's CRPS is decomposed as the weighted mean of component CRPS minus a non-negative diversity term built from pairwise differences in component errors across thresholds.

## 3. Impact — potential & realized

Realized (per the paper): the AIFS-CRPS + MOGREPS-UK blend improves skill across space, lead times and thresholds when weights follow relative skill, improving both reliability and resolution; the three-model blend gives the largest gain, especially days 2–5. A MOGREPS-UK blend with either AIFS-CRPS or IFS beats an IFS + AIFS-CRPS blend, which have less diverse errors. Calibrating AIFS-CRPS with EMOS yields skill gains comparable to calibrated physics-based ensembles, and calibrating both before and after blending improves accuracy further. Limits: one region, about four months, temperature and wind only.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Methodologically tidy for anyone combining forecasts: the diversity term gives a concrete reason to pick complementary models rather than the two best ones.

Methodologically tidy for anyone combining forecasts: the diversity term gives a concrete reason to pick complementary models rather than the two best ones. Narrow evaluation window, so treat magnitudes as indicative.

### Similar / related work

- [**The Hidden Look-Ahead: Point-in-Time Leakage in Electricity Market Data**](2026-10-29-arxiv-point-in-time-leakage-electricity-forecast-archives.md) (in this bank) — forecast evaluation hygiene
- [**Can We Trust Evaluations of AI Weather Forecasts for Extremes?**](https://arxiv.org/abs/2610.31237) — evaluation protocols for AI weather models

### Jargon buster

- **CRPS** — Continuous ranked probability score: squared distance between the forecast CDF and the observed outcome, integrated over thresholds; lower is better.
- **EMOS** — Ensemble model output statistics: regression-based calibration of ensemble forecasts.
- **Linear pool** — A weighted average of forecast distributions.
