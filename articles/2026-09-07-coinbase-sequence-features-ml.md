---
id: coinbase-sequence-features-ml
title: "How Coinbase Builds Sequence Features for Machine Learning"
source: "Coinbase Blog"
url: "https://www.coinbase.com/blog/how-coinbase-builds-sequence-features-for-machine-learning"
published: "2025-09"
added: "2026-09-07"
category: data-engineering
tags: [feature-store, tecton, streaming, sequence-features, fraud-detection, recommendations, lstm, transformer]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# How Coinbase Builds Sequence Features for Machine Learning

**Source:** [Coinbase Blog](https://www.coinbase.com/blog/how-coinbase-builds-sequence-features-for-machine-learning) · Published 2025-09 · Added 2026-09-07
**Category:** Data Engineering · **Tags:** `feature-store`, `tecton`, `streaming`, `sequence-features`, `fraud-detection`, `recommendations`, `lstm`, `transformer`

## TL;DR

Coinbase built a declarative framework — jointly owned by ML Platform, ML Risk, Recommendations, and Data Platform — that lets engineers specify a topic, event schema, and sequence semantics, and have the system automatically generate the streaming data sources and Tecton feature views needed to serve real-time sequence features to fraud and recommendation models.

## 1. Business context

Fraud detection and recommendation models both benefit from features that capture a user's behavior as an ordered sequence (login sessions, trading patterns, page visits) rather than flattened aggregates, but building a production streaming pipeline for a new sequence feature was previously a bespoke, multi-team effort every time — slow enough that teams either did without sequence features or shipped them late. The four-team ownership split (ML Platform, ML Risk, Recommendations, Data Platform) signals how broadly this bottleneck was felt across Coinbase's ML surfaces.

## 2. Technical details

The framework's design goal is that a Machine Learning Engineer only has to declare three things — the topic, the event schema, and the desired sequence semantics — and the system handles the rest: automatically creating the underlying data sources and the corresponding Tecton feature views that implement that sequence. Under the hood it combines Tecton (the feature store layer) and Databricks (batch/streaming compute) to capture rich behavioral event streams — login sessions, trading activity — in real time, and serve the resulting sequence features with millisecond latency into downstream deep learning models, specifically LSTMs and Transformers, used for fraud detection and personalized recommendations.

## 3. Impact — potential & realized

The team reports that sequence features built this way improved model performance for both fraud detection and recommender systems, and are now "among the top contributors to model performance globally at Coinbase." The business impact is quantified as "tens of millions of dollars" over the past year attributed to these features across key business metrics — though the write-up does not break that figure down by model or metric. The potential is a reusable declarative pattern: any team needing a new behavioral sequence feature no longer needs to design a bespoke streaming pipeline, which should compound the framework's value as more sequence-based use cases are added.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Good engineering, declarative feature generation over a known stack

Declarative feature specification over an existing feature store (Tecton) and compute layer (Databricks) is an incremental, if valuable, abstraction — the novelty is in automating the boilerplate of building a new streaming sequence pipeline, not in a new modeling or serving technique. The reported "tens of millions of dollars" and "top global contributor" framing is a strong signal of realized value, but without a metric breakdown it's hard to independently assess how much is attributable to the framework itself versus the underlying sequence-modeling approach (LSTM/Transformer) it feeds.

### Similar / related work

- [**How Databricks Feature Store Serves Features with Sub-Second Freshness**](2026-08-30-databricks-feature-store-subsecond-freshness.md) (in this bank) — a parallel real-time feature-serving story on a different but architecturally similar stack (Spark RTM, Kafka, Unity Catalog vs. Tecton/Databricks here).
- [**Using Grab's Trust Counter Service to Detect Fraud Successfully**](2026-09-05-grab-trust-counter-fraud-detection.md) (in this bank) — a different real-time feature approach (self-service counters vs. declarative sequence features) aimed at the same fraud-detection problem.
- [**An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking (Feed SR)**](2026-09-01-linkedin-feed-sr-sequential-recommender.md) (in this bank) — shares the sequence-as-transformer-input modeling approach these features are built to feed.

### Jargon buster

- **Tecton** — a commercial feature store platform that manages defining, computing, and serving ML features (including streaming/real-time ones) with a declarative API.
- **Sequence feature** — a model input that preserves the order and timing of a user's past events (e.g., "logged in, viewed asset, placed order" in that order) rather than collapsing them into a single aggregate number like "order count."
