---
id: uber-cost-efficient-export-workloads
title: "Running Cost-Efficient Export Workloads at Uber"
source: "Uber Engineering"
url: "https://www.uber.com/us/en/blog/running-cost-efficient-export/"
published: "2026-08"
added: "2026-09-01"
category: data-engineering
tags: [lakehouse, hudi, data-pruning, compliance, storage-optimization, gcs]
novelty: 3
sourced_via: "full-text fetch"
---

# Running Cost-Efficient Export Workloads at Uber

**Source:** [Uber Engineering](https://www.uber.com/us/en/blog/running-cost-efficient-export/) · Published 2026-08 · Added 2026-09-01
**Category:** Data Engineering · **Tags:** `lakehouse`, `hudi`, `data-pruning`, `compliance`

## TL;DR

Uber cuts the cost of "needle in haystack" compliance and export queries —
like Data Subject Access Requests — against its GCS-backed Apache Hudi
lakehouse by combining Hudi's column-stats file pruning with table
sorting/clustering on the columns those queries filter on, achieving a
**24.8% disk reduction** on sorted partitions versus an alternative
secondary-index approach.

## 1. Business context

Compliance and export queries — for example, Data Subject Access Requests
(DSARs), which look up all the data a company holds on one specific
individual — touch a tiny number of specific records. But run against a
lakehouse tuned for large scans, they were triggering full-table scans,
defeating Uber's storage tiering and driving up compute and cloud-storage
egress cost for what should be cheap, targeted point lookups.

## 2. Technical details

- **Column-stats file pruning.** Apache Hudi stores per-file column
  statistics (e.g. min/max values); at query time, files that can't possibly
  contain a matching row are skipped without being read.
- **Table sorting/clustering.** Sorting and clustering the table on the
  specific columns export queries filter on physically co-locates the
  relevant rows, making the column-stats pruning far more effective, since
  matching rows are concentrated into few files instead of spread across
  many.
- **Comparison point.** Uber evaluated this sorting-plus-pruning approach
  against an alternative design using a **secondary index**.

## 3. Impact — potential & realized

- **Realized:** a **24.8% disk reduction** on sorted partitions, along with
  reduced GCS egress and metadata costs, compared to the secondary-index
  alternative.
- **Potential:** a reusable pattern for any lakehouse that mixes rare,
  sparse point-lookup workloads (compliance, support, debugging) into a
  system otherwise tuned for large analytical scans.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid, well-evaluated engineering on established techniques

Column-stats pruning and clustering/sorting for predicate locality are
well-established lakehouse techniques, not new ideas. The value here is
Uber's specific, measured comparison against a plausible alternative
(secondary indexing) and a concrete number for a real workload class — good,
useful engineering, but an application of known techniques rather than a new
one.

### Similar / related work

- [**How Databricks Feature Store Serves Features with Sub-Second
  Freshness**](2026-08-30-databricks-feature-store-subsecond-freshness.md) (in this bank) — a different lakehouse-adjacent optimization
  problem (feature freshness for serving, not compliance point lookups) on a
  similar class of infrastructure.
- Uber's own COUNT(DISTINCT) high-cardinality pipeline work (still a
  `catalog.json` backlog stub) — a related Uber data-pipeline efficiency
  problem, not yet written up.

### Jargon buster

- **Apache Hudi** — an open table format for building lakehouses, with
  support for indexing, clustering, and incremental data processing.
- **Column-stats pruning** — skipping a file at query time using stored
  min/max statistics per column, without having to read the file's contents.
- **Data Subject Access Request (DSAR)** — a legally mandated request for
  all the personal data a company holds on a specific individual.
