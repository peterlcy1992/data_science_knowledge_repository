---
id: databricks-feature-store-subsecond-freshness
title: "How Databricks Feature Store Serves Features with Sub-Second Freshness"
source: "Databricks Blog"
url: "https://www.databricks.com/blog/how-databricks-feature-store-serves-features-sub-second-freshness"
published: "2026-08"
added: "2026-08-30"
category: ml-infra-serving
tags: [feature-store, streaming, real-time, spark-rtm, lakebase, feature-views, kafka, unity-catalog]
novelty: 3
sourced_via: "web search"
---

# How Databricks Feature Store Serves Features with Sub-Second Freshness

**Source:** [Databricks Blog](https://www.databricks.com/blog/how-databricks-feature-store-serves-features-sub-second-freshness) · Published 2026-08 · Added 2026-08-30
**Category:** ML Infrastructure & Serving · **Tags:** `feature-store`, `streaming`, `spark-rtm`, `lakebase`

## TL;DR

Databricks Feature Store can now serve **streaming aggregations from Kafka at
~200ms p99**, collapsing feature lag from minutes/hours to milliseconds. It
rests on three pieces: **Spark Real-Time Mode** (per-event processing), **Lakebase**
(a serverless Postgres online layer), and **Feature Views** (author a feature once,
use it in batch, experimentation, and real-time serving).

## 1. Business context

Real-time ML — fraud scoring, ranking, personalization — is only as good as the
freshness of its features. The classic feature-store split (batch offline store
for training, low-latency online store for serving) tends to leave a lag between
when an event happens and when its aggregated feature is servable, and it forces
teams to author features twice (batch vs. streaming), inviting **training–serving
skew**. Databricks' goal is fresh features (sub-second) with a single feature
definition reused everywhere, operated as managed infrastructure.

## 2. Technical details

- **Spark Real-Time Mode (RTM).** Instead of waiting for microbatches, RTM
  processes rows **continuously**, updates rolling-window aggregates **per event**,
  and amortizes checkpointing to keep stateful streaming latency low. This is what
  makes windowed aggregations fresh to the millisecond.
- **Lakebase online layer.** **Lakebase** is a **serverless Postgres** database
  built into the Databricks platform that powers the **Online Feature Store**. By
  separating compute and storage it reduces **write amplification** for frequent
  small upserts, so fresh values land quickly for low-latency inference. Reported
  serving latency: **~200ms p99** for streaming aggregations from Kafka.
- **Feature Views.** A **Feature View** lets you author a feature **once** and use it
  across experimentation, batch, and real-time serving without operating the
  plumbing yourself — the abstraction that fights training–serving skew.
- **Governance.** In 2026 the Feature Store is deeply integrated with **Unity
  Catalog** and the broader Lakehouse, with online serving from Lakebase.

## 3. Impact — potential & realized

- **Realized:** ~200ms p99 online serving of Kafka-sourced streaming aggregations;
  feature lag reduced from minutes/hours to milliseconds.
- **Realized (developer):** one feature definition across batch/experiment/real-time,
  reducing skew and duplicate authoring.
- **Potential:** brings genuinely real-time features to teams that can't run a
  bespoke streaming + online-store stack, by making it managed and governed.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — closing a well-known gap with a strong managed implementation

Feature stores, online/offline duality, and streaming aggregation are mature
ideas (Tecton, Feast, Uber's Michelangelo Palette all trod this ground). The news
here is execution and integration: per-event Spark RTM plus a serverless-Postgres
online layer hitting 200ms p99, all inside Unity Catalog governance. That's
valuable and lowers the bar for real-time ML, but it's catching a known frontier
rather than defining a new one — a solid 3.

### Similar / related work

- **Airbnb Zipline** (declarative feature engineering) — the "author once, serve
  batch + streaming" lineage this extends.
- **Uber Michelangelo Palette / Tecton / Feast** — the feature-store prior art.
- [**In-House LLM Serving at Netflix**](2026-08-30-netflix-in-house-llm-serving.md) (in this bank) — the serving-latency
  discipline, applied to features rather than models.

### Jargon buster

- **Feature store** — a system that computes, stores, and serves the input features
  ML models need, keeping training-time and serving-time values consistent.
- **Online vs. offline store** — offline holds large historical features for
  training; online holds the latest values for low-latency inference.
- **Training–serving skew** — bugs from computing a feature one way in training and
  a slightly different way at serving, degrading live model quality.
- **Microbatch vs. per-event (RTM)** — classic Spark Streaming groups events into
  small batches; Real-Time Mode processes each event as it arrives for lower
  latency.
- **Write amplification** — when one logical update triggers much more physical I/O
  than the data itself; costly for frequent tiny upserts.
- **p99 latency** — the latency below which 99% of requests complete; a tail-latency
  measure that matters more than the average for user-facing serving.
- **Upsert** — insert-or-update: write a row, replacing it if the key already
  exists.
