---
id: uber-count-distinct-high-cardinality-pipelines
title: "Scaling Exact COUNT(DISTINCT) for High-Cardinality Non-Rollup Metrics in Distributed Data Pipelines"
source: "Uber Engineering"
url: "https://www.uber.com/us/en/blog/scaling-exact-count/"
published: "2026-07"
added: "2026-09-24"
category: data-engineering
tags: [count-distinct, roaring-bitmap, umetric, data-pipelines, cardinality]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Scaling Exact COUNT(DISTINCT) for High-Cardinality Non-Rollup Metrics in Distributed Data Pipelines

**Source:** [Uber Engineering](https://www.uber.com/us/en/blog/scaling-exact-count/) · Published 2026-07 · Added 2026-09-24
**Category:** Data Engineering · **Tags:** `count-distinct`, `roaring-bitmap`, `umetric`, `data-pipelines`, `cardinality`

## TL;DR

Uber's exact-distinct-count pipelines hit a hard JVM 2GB array ceiling at roughly 179 million unique identifiers, deterministically OOM-ing on non-rollup metrics like Monthly Active Users. A chunked bitmap strategy — hashing IDs into 65,536 independently-serialized `Roaring64Bitmap` chunks — pushed the safe cardinality ceiling to ~11.7 trillion identifiers and cut a two-year backfill from 8.58 to 2.96 days.

## 1. Business context

Some business metrics genuinely can't be computed by summing smaller pre-aggregated pieces: Monthly Active Users (MAU) is the canonical example, since a user active on both Monday and Wednesday must be counted once for the month, and no combination of daily active-user counts can recover that. These "non-rollup" metrics require an exact distinct count over the full underlying set of identifiers, not an approximation or a sum of partials — critical for financial and business reporting, where "approximately correct" isn't good enough. At Uber's scale (3.6 billion unique identifiers in a quarter for some metrics), any team wanting to define such a metric on Uber's uMetric platform either had to hand-write custom aggregation code or risk hitting scaling walls that took down entire pipeline runs.

## 2. Technical details

The blocking failure mode: JVM-based pipelines (Hive, Spark) that compute an aggregation as a single serialized `byte[]` state object are capped by Java's hard array-size limit. A `Bitmap-64` approach (using `Roaring64Bitmap` directly) hit that 2GB ceiling at approximately 179 million identifiers — beyond that, the job deterministically threw `OutOfMemoryError`. A `Bitmap-32` alternative avoided the memory ceiling but required sequential execution through a shared dictionary, killing parallelism.

The fix is a **chunked aggregation buffer**: instead of one monolithic bitmap, the aggregation state becomes a `Map<Integer, Roaring64Bitmap>`, where each identifier is routed to one of 65,536 chunks based on the top 16 bits of its `xxHash64` hash. Each chunk serializes independently, so peak memory is bounded by a single chunk's size rather than the total cardinality — the OOM failure mode is structurally eliminated rather than pushed further out. A magic-number header (`0xDEADBEEF`) lets the new chunked format stay backward-compatible with old single-bitmap partial results during rollout. The final output of the whole pipeline is still just an 8-byte long — the cardinality count — regardless of how the intermediate state was chunked.

## 3. Impact — potential & realized

Reported results: a two-year metric backfill dropped from 8.58 days to 2.96 days (65% reduction), with the highest-cardinality workloads improving 94%; daily pipeline runtime improved 23%; monthly metric-preparation time dropped from ~20 days to ~10 days (43%); the safe cardinality ceiling expanded roughly 65,000x, to about 11.7 trillion identifiers; and the team reports zero OOM failures post-deployment across 75 metric families. The realized win is operational: existing non-rollup metrics stopped failing and got faster. The broader potential the post claims is that this pattern generalizes beyond Uber's specific stack to any JVM-based distributed pipeline (Hive, Spark, or otherwise) computing exact aggregation state as a single serialized byte array.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clean fix for a well-known JVM ceiling

Chunking/sharding aggregation state to avoid a single-object memory limit is a standard distributed-systems pattern, and Roaring Bitmaps themselves are an established compressed-bitmap technique, not new. The value here is entirely in the specific, quantified application: identifying the exact failure boundary (179M identifiers, the JVM's 2GB array cap), engineering a hash-routed chunking scheme that preserves parallelism (unlike the sequential Bitmap-32 alternative), and reporting concrete before/after numbers across 75 production metric families. It's a solid, reusable engineering recipe rather than a new idea — teams hitting the same JVM ceiling on exact-cardinality pipelines are the direct beneficiaries.

### Similar / related work

- **Roaring Bitmaps** ([roaringbitmap.org](https://roaringbitmap.org/)) — the underlying compressed-bitmap data structure this pipeline builds on; the contribution here is the chunking scheme around it, not the bitmap format itself.
- **HyperLogLog and other probabilistic cardinality estimators** — the standard alternative for distinct counting at scale, explicitly rejected here because Uber's non-rollup metrics require exact rather than approximate counts for financial reporting.

### Jargon buster

- **Non-rollup metric** — a metric (like Monthly Active Users) that can't be derived by summing smaller time-window aggregates, because it depends on which *distinct* entities appeared across the whole window, not how many appearances there were in total.
- **Roaring Bitmap** — a compressed bitmap format that stores sets of integers efficiently by adaptively choosing between different internal representations (arrays, bitmaps, runs) depending on data density.
- **JVM array size limit** — Java arrays are indexed by a 32-bit `int`, which combined with per-element overhead caps a single `byte[]` at roughly 2GB — a hard ceiling that a monolithic bitmap eventually hits at high cardinality.
