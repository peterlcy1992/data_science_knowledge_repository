---
id: google-weathernext3-weather-forecasting
title: "Introducing WeatherNext 3, Our Most Advanced and Accurate Global Weather AI Model"
source: "Google (DeepMind / Google Research)"
url: "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-weathernext-3/"
published: "2026-09"
added: "2026-09-03"
category: forecasting-timeseries
tags: [weather-forecasting, foundation-model, satellite-data, generative-network, geospatial]
novelty: 4
sourced_via: "full-text fetch"
---

# Introducing WeatherNext 3, Our Most Advanced and Accurate Global Weather AI Model

**Source:** [Google (DeepMind / Google Research)](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-weathernext-3/) · Published 2026-09 · Added 2026-09-03
**Category:** Forecasting & Time Series · **Tags:** `weather-forecasting`, `foundation-model`, `satellite-data`, `generative-network`, `geospatial`

## TL;DR

WeatherNext 3 is Google DeepMind/Research's third-generation weather AI model, moving from forecasts updated every 6 hours to forecasts that refresh hourly by ingesting live geostationary satellite imagery through a single Functional Generative Network mesh-transformer, producing forecasts roughly five times sharper than WeatherNext 2 with meaningfully better precipitation accuracy.

## 1. Business context

Weather forecasting underpins renewable-energy planning (wind turbine output, solar radiation), agriculture, aviation, and emergency response, but prior model generations — including WeatherNext 2 — only produced new forecasts every 6 hours, using data available at that fixed cadence. That leaves a gap between fast-moving real-world weather (a storm intensifying, a front shifting) and how often a model can update its picture of the world. WeatherNext 3 targets that gap directly: it ingests satellite data as soon as it is available and issues an updated global forecast every hour instead of every six.

## 2. Technical details

- **Single-architecture Functional Generative Network (FGN):** a mesh-transformer architecture that unifies the modeling approach, rather than stitching together separate specialized models for different variables or lead times.
- **Live satellite ingestion:** the model consumes 1-hour geostationary satellite mosaics as they arrive, combined with historical analysis data, letting it update its state hourly rather than waiting for the next 6-hour analysis cycle.
- **Multi-format output:** WeatherNext 3 produces dense gridded fields (temperature, wind, precipitation, etc.), discrete cyclone tracks, and sparse station-level coordinate forecasts from the same model.
- **Resolution:** 5km for surface temperature and moisture, 10km for other surface variables, and 25km for atmospheric/wind variables — described as roughly five times sharper than WeatherNext 2.
- **Training data:** NASA IMERG precipitation data, satellite-radar-based global precipitation reanalysis, and sparse weather-station observations, in addition to the live satellite feeds used at inference time.
- **Distribution:** outputs feed Google Search, the Gemini app, Google Maps and the Maps Platform Weather API, and Earth Engine, and are queryable directly via BigQuery and Google Cloud Storage.

## 3. Impact — potential & realized

- **Realized:** up to 60% more accurate precipitation forecasts versus the IMERG reference dataset, 30% more accurate versus MRMS radar-based estimates, and 10% more accurate than rain-gauge observations at early lead times; up to 50% more accurate day-ahead precipitation forecasts; forecast refresh cadence improved from every 6 hours to hourly.
- **Potential:** the hourly-refresh, live-satellite-ingestion approach is framed as a template for near-real-time environmental monitoring more broadly — renewable-energy siting and dispatch, agricultural planning around short-notice weather shifts, and faster emergency-response lead times where a 6-hour-stale forecast is a real operational cost.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a real cadence and resolution step-change, built on an established idea

Feeding live satellite data into a weather foundation model to shrink the forecast-update interval is a genuine advance over the 6-hour-cycle norm that WeatherNext 2 and most numerical weather prediction systems still use — this is the kind of improvement that changes what the forecast is useful for (short-notice operational decisions), not just how accurate a fixed-cadence forecast is. It's a 4 rather than a 5 because AI weather foundation models (GraphCast, WeatherNext 2, and others) already established the core paradigm of learned, gridded global forecasting; this is Google's own next iteration on that paradigm rather than a new one, and the write-up doesn't disclose parameter counts or training compute that would let readers judge how much of the gain is architecture versus more/better data.

### Similar / related work

- [**TimesFM-3: A Zero-Shot Foundation Model for Multivariate Forecasting**](2026-09-03-google-timesfm3-multivariate-forecasting.md) (in this bank) — a sibling Google forecasting foundation model released the same week, but general-purpose and zero-shot across domains rather than weather-specific and pretrained on satellite/reanalysis data.
- **GraphCast** (DeepMind, 2023) — the earlier DeepMind weather model that established graph-neural-network-based global forecasting as competitive with traditional numerical weather prediction; WeatherNext is DeepMind's successor lineage to this work, unlinked here as no specific URL was confirmed in this research pass.

### Jargon buster

- **Functional Generative Network (FGN)** — a generative model architecture (here, a mesh transformer) that outputs a distribution over possible future states rather than a single deterministic forecast.
- **Geostationary satellite mosaic** — an image built by stitching together views from satellites that stay fixed relative to a point on Earth, giving continuous coverage of a region.
- **IMERG** — NASA's Integrated Multi-satellitE Retrievals for GPM, a global precipitation estimate dataset combining data from multiple satellites, used here both as training data and as an accuracy benchmark.
