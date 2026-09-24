---
id: uber-taming-ml-firehose-feature-consistency
title: "Taming the ML Firehose: Scaling Feature Consistency"
source: "Uber Engineering"
url: "https://www.uber.com/us/en/blog/taming-ml-firehose/"
published: "2026-09"
added: "2026-09-24"
category: data-engineering
tags: [feature-store, training-serving-skew, flink, kafka, rocksdb, feature-freshness]
novelty: 3
sourced_via: "full-text fetch"
---

# Taming the ML Firehose: Scaling Feature Consistency

**Source:** [Uber Engineering](https://www.uber.com/us/en/blog/taming-ml-firehose/) · Published 2026-09 · Added 2026-09-24
**Category:** Data Engineering · **Tags:** `feature-store`, `training-serving-skew`, `flink`, `kafka`, `rocksdb`, `feature-freshness`

## TL;DR

Uber's ML models suffered training-serving skew — online feature values didn't match what offline pipelines later reconstructed for training, from locale formatting mismatches ("en-US" vs "en") to multi-day-stale features. The fix logs the exact features seen at inference time as the canonical training source, filtered down to the ~5% of predictions that actually reach a user, cutting mismatch rates from over 10% to 0% on key features.

## 1. Business context

Uber runs a large surface of production ML models (pricing, matching, recommendations) where features are computed twice: once online at serving time and once offline when reconstructing training data from raw event logs. Any divergence between those two paths — a different locale string, a stale join, a fragile ETL step — silently degrades model quality and is notoriously hard to debug, since the mismatch only shows up as unexplained accuracy loss weeks later. The team frames this as a "firehose" problem: at Uber's request volume, capturing every feature for every prediction is prohibitively expensive, so the challenge is building a feature-logging pipeline that is both trustworthy (an exact record of what the model actually saw) and affordable at scale.

## 2. Technical details

The core design principle is to make the **online feature values themselves** the source of truth for training data, rather than reconstructing them later from raw logs. Several techniques bring the volume down to something tractable:

- **Feature allow lists** restrict logging to only the features a given model actually consumes, cutting logged payload size 4–5x.
- **Feature name aliasing via enums** replaces verbose string feature names with compact integer IDs before serialization, shrinking payloads further.
- **Impression filtering with Apache Flink**: rather than logging every prediction, a Flink job performs time-windowed joins between prediction logs (from Kafka) and client-side impression events, keeping only the roughly 5% of predictions that were actually shown to a user — the rest are discarded before they ever hit storage.
- **Array feature flattening**, tuned specifically for transformer-based models that consume sequence-shaped features.

Scaling the Flink layer itself required standard but carefully-tuned stream-processing work: profiling individual operators at 512–768 parallelism, aggressive state eviction and deduplication, a custom RocksDB state-backend tuning strategy to handle the data volume, and sharding Kafka across multiple clusters to avoid a single point of contention.

## 3. Impact — potential & realized

Reported results: mismatch rates on key features that previously exceeded 10% dropped to 0%; feature freshness for priority features improved from multi-day lag to hours; peak consumer lag in the processing pipeline fell by roughly 70%; and the impression-filtering step drives meaningful infrastructure cost savings by discarding ~95% of predictions before they're persisted. The realized win is a debuggable, trustworthy feature pipeline for existing models. The broader potential is that any team onboarding a new model at Uber inherits consistency-by-construction rather than having to independently solve training-serving skew — a class of bug that is otherwise expensive to detect and easy to reintroduce.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-engineered instance of a known pattern

"Log what the model saw online, use that as training data" is an established idea in ML infrastructure (feature stores from Databricks, SageMaker, and others exist partly to solve this). What's genuinely useful here is the scaling recipe: impression-filtered Flink joins to cut 95% of volume before it's persisted, plus concrete before/after numbers (0% mismatch, 70% lag reduction) that most write-ups on this topic leave out. Teams running high-QPS recommendation or pricing models with strict latency budgets are the most likely to reuse the impression-filtering trick specifically.

### Similar / related work

- [**How Databricks Feature Store Serves Features with Sub-Second Freshness**](2026-08-30-databricks-feature-store-subsecond-freshness.md) (in this bank) — attacks the same online/offline feature-freshness problem from the serving-latency side rather than the logging/consistency side.
- [**Amazon SageMaker Feature Store Introduces UpdateRecord for Feature-Level Writes**](2026-09-17-aws-sagemaker-feature-store-updaterecord-partial-writes.md) (in this bank) — a complementary feature-store primitive (partial writes) aimed at the same class of freshness/consistency pain.

### Jargon buster

- **Training-serving skew** — when the feature values a model sees in production differ from the values it was trained on, degrading accuracy in ways that are hard to detect because the model still runs without errors.
- **Impression filtering** — discarding logged predictions that a user never actually saw, so storage and processing costs scale with real exposure rather than raw request volume.
- **RocksDB state backend** — an embedded key-value store Flink uses to hold the intermediate state of a streaming job (e.g., open time-window joins) on local disk, tuned here to survive Uber's data volume without falling behind.
