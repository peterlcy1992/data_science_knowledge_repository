---
id: uber-deepett-graph-aware-traffic-forecasting
title: "Scaling Real-Time Traffic Forecasting with a Graph-Aware Transformer"
source: "Uber Engineering"
url: "https://www.uber.com/us/en/blog/scaling-real-time-traffic/"
published: "2026-05"
added: "2026-08-31"
category: forecasting-timeseries
tags: [traffic-forecasting, transformer, graph-features, real-time, streaming, eta]
novelty: 4
sourced_via: "web search"
---

# Scaling Real-Time Traffic Forecasting with a Graph-Aware Transformer

**Source:** [Uber Engineering](https://www.uber.com/us/en/blog/scaling-real-time-traffic/) · Published 2026-05 · Added 2026-08-31
**Category:** Forecasting & Time Series · **Tags:** `traffic-forecasting`, `transformer`, `graph-features`, `real-time`

## TL;DR

Uber rebuilt its decade-old traffic forecasting stack as **DeepETT** (Deep
Estimated Travel Time), a graph-aware transformer that forecasts road-segment
travel times up to three hours out, refreshed every five minutes, serving
**upwards of 2 million real-time forecasts per second**. It improved
long-trip arrival-time accuracy by **6%**, forecast variance explained by
**19%**, and is credited with roughly **$100 million** in incremental annual
value.

## 1. Business context

Traffic forecasting underlies route selection and arrival-time estimation
across Uber's core products, and the prior stack had reliably supported that
at massive scale for over a decade. But incremental improvements to a
decade-old architecture eventually hit diminishing returns, so Uber's
Traffic Forecasting and Applied AI teams launched a multi-year effort to
rebuild the system on a modern deep-learning architecture rather than
patching the legacy one further — betting that a transformer that could
natively fuse spatial (road-graph) and temporal (historical, real-time)
signal would outperform the older approach's more siloed feature pipeline.

## 2. Technical details

- **Fixed-input graph-aware transformer.** DeepETT tokenizes
  **pre-aggregated spatial and temporal observations** — segment-level,
  road-graph, regional, historical, real-time, and event features — into a
  fixed-size input, enabling **constant-time inference** regardless of how
  much raw signal feeds each forecast.
- **Continuous real-time calibration.** A **Flink-based streaming pipeline**
  continuously calibrates the model's output against observed drift, so
  forecasts adapt as real-world conditions (incidents, weather, demand
  shifts) diverge from the model's priors, rather than relying solely on
  periodic retraining.
- **Forecast cadence and horizon.** Every 5 minutes, DeepETT forecasts the
  mean estimated traversal time (ETT) for each road segment out to a
  **three-hour horizon**.
- **Throughput.** DeepETT is one of Uber's **highest-throughput deep
  learning deployments**, serving upwards of **2 million real-time
  forecasts per second**.

## 3. Impact — potential & realized

- **Realized:** **+6%** long-trip arrival-time accuracy, **+19%** forecast
  variance explained versus the prior system, and an estimated **$100
  million** in incremental annual value.
- **Realized (systems):** constant-time inference via fixed-input
  tokenization lets the model scale to millions of forecasts/second without
  per-forecast cost growing with feature richness.
- **Potential:** the pre-aggregate-then-tokenize pattern, paired with
  streaming recalibration, is a template for other real-time,
  massive-throughput spatiotemporal forecasting problems (e.g. demand or
  ETA forecasting elsewhere in the stack) that need both scale and
  freshness.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a mature, decade-refined system with a genuinely hard throughput constraint

Graph-aware and transformer-based traffic forecasting are active research
areas, so the modeling ideas here aren't new in isolation. What makes this a
strong 4 is the production engineering: fixing the input representation so
inference cost is constant regardless of upstream feature growth, then
layering a streaming (Flink) recalibration loop on top, all while sustaining
one of the highest per-second inference throughputs described in this bank.
It's an evolution of Uber's long-running DeepETA lineage rather than a new
paradigm, hence not a 5.

### Similar / related work

- **DeepETA: How Uber Predicts Arrival Times Using Deep Learning** (Uber
  Engineering) — the predecessor system DeepETT succeeds; both belong to
  the same applied-forecasting lineage at Uber.
- [**Improving ETAs with Multi-Task Models, Deep Learning, and Probabilistic
  Forecasts at DoorDash**](2026-08-30-doordash-eta-multitask-probabilistic.md) (in this bank) — a competitor's deep-learning
  approach to the closely related ETA-forecasting problem.
- **Towards Spatio-Temporal Aware Traffic Time Series Forecasting**
  (arXiv [2203.15737](https://arxiv.org/abs/2203.15737)) — general academic literature on combining spatial
  (graph) and temporal signal for traffic forecasting.

### Jargon buster

- **Graph-aware model** — a model that explicitly uses the road network's
  graph structure (which segments connect to which) as an input, rather
  than treating each road segment as an independent, unconnected signal.
- **Fixed-input tokenization** — converting variable, growing amounts of
  raw signal into a fixed-size representation before it reaches the model,
  so inference time stays constant no matter how much upstream data feeds
  each forecast.
- **ETT (Estimated Traversal Time)** — the forecasted time to traverse a
  specific road segment, the building block DeepETT predicts and which
  downstream systems sum along a route to get a full trip ETA.
- **Flink** — a stream-processing framework used here to continuously
  recalibrate forecasts against real-time observed conditions.
