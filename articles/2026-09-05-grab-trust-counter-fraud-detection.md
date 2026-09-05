---
id: grab-trust-counter-fraud-detection
title: "Using Grab's Trust Counter Service to Detect Fraud Successfully"
source: "Grab Engineering"
url: "https://engineering.grab.com/using-grabs-trust-counter-service-to-detect-fraud-successfully"
published: "2019-10"
added: "2026-09-05"
category: data-engineering
tags: [fraud-detection, self-service-rules, real-time-counters, scylladb, streaming, trust-and-safety]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Using Grab's Trust Counter Service to Detect Fraud Successfully

**Source:** [Grab Engineering](https://engineering.grab.com/using-grabs-trust-counter-service-to-detect-fraud-successfully) · Published 2019-10 · Added 2026-09-05
**Category:** Data Engineering · **Tags:** `fraud-detection`, `self-service-rules`, `real-time-counters`, `scylladb`, `streaming`, `trust-and-safety`

## TL;DR

Grab built a self-service Counter Service that lets data scientists and fraud analysts define real-time, streaming-aggregated counters (like "cashless driver-passenger pairs in the last hour") through a UI, then feed those counters straight into fraud rules — removing the two-plus-week engineer-in-the-loop bottleneck that previously gated every new detection idea.

## 1. Business context

The article cites industry-wide fraud losses in the billions of dollars, and estimates organizations lose around 5% of annual revenue to fraud. At Grab's scale, a common fraud pattern is a single person masquerading as both driver and passenger on the same trip to exploit promotions or payment incentives — a pattern that's easy to describe ("this pair of accounts transacts suspiciously often") but expensive to detect if every new rule requires a data scientist to hand a spec to an engineer, who then builds bespoke streaming logic. That round trip took two or more weeks per rule, which is far too slow against fraud patterns that mutate quickly.

## 2. Technical details

The Counter Service turns "count how often X happens" into a self-service primitive:

- **Self-service counter creation.** Analysts define counters through a UI — specifying the event stream(s) to watch and the aggregation expression — without needing an engineer to write or deploy new code.
- **Counter Processor.** A component that monitors multiple configured event streams, enriches events with data from upstream services (e.g. Grab's core data service, the passenger service), and computes the aggregated counter values.
- **Storage layer.** Aggregated values are persisted in Grab-Stats, backed by ScyllaDB — chosen because it is roughly 10x cheaper than AWS ElastiCache at comparable reliability for this workload. Queries are bucketed into time windows (15 minutes, 1 hour, 1 day) to keep both writes and time-range reads efficient.
- **Rule evaluation.** Counters become inputs to fraud rules: e.g., a counter tracking cashless driver-passenger transaction pairs feeds a rule that flags the pair as fraudulent once the counter crosses a predefined threshold.

## 3. Impact — potential & realized

**Realized:** the article reports concrete production load figures — total incoming stream throughput of roughly 5,000 QPS at peak, about 4,000 counter writes per second to the storage tier, ScyllaDB read p99 latency under 150ms, and a target design capacity of 100,000 QPS — plus the qualitative outcome that data scientists could now design and ship new fraud counters without waiting on engineering cycles.

**Potential:** the article flags two forward-looking directions: integrating with Grab's Griffin rule engine for more expressive rule composition, and a "time traveler" capability for replaying historical data to backtest new counters/rules and support more automated ML pipeline iteration.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-executed, foundational self-service-analytics pattern rather than a novel algorithm

There's no new modeling idea here — this is a case study in *organizational* leverage: turning a slow, engineer-gated workflow into a self-service one so that domain experts (fraud analysts) can iterate directly. That pattern (self-service streaming aggregation feeding rule engines) is now a standard building block across the industry, which is why this scores a solid-but-incremental 3 rather than higher, but it's exactly the kind of "boring infrastructure that removes a real bottleneck" story that's easy to underrate.

### Similar / related work

- [**Leveraging Graph Technology for Real-Time Fraud Detection and Prevention at Booking.com**](../articles/2026-08-30-booking-graph-fraud-detection.md) (in this bank) — a complementary fraud-detection approach using graph relationships rather than streaming counters, useful contrast in how different companies structure real-time fraud signals.
- [**How Databricks Feature Store Serves Features with Sub-Second Freshness**](../articles/2026-08-30-databricks-feature-store-subsecond-freshness.md) (in this bank) — a more general-purpose version of the same underlying need (self-service, low-latency, streaming-aggregated signals feeding downstream decisioning).

### Jargon buster

- **ScyllaDB** — a distributed NoSQL database compatible with Cassandra's API but written for higher throughput and lower latency on the same hardware, used here as a cheaper, comparably reliable alternative to a managed in-memory cache.
- **Griffin (rule engine)** — referenced as Grab's system for composing and evaluating fraud rules; the Counter Service is designed to plug counters into it as one of the inputs a rule can reference.
