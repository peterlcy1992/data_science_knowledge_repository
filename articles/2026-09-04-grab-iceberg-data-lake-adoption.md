---
id: grab-iceberg-data-lake-adoption
title: "Scaling Grab's Data Lake: Our Journey to Apache Iceberg Adoption"
source: "Grab Engineering"
url: "https://engineering.grab.com/our-journey-to-apache-iceberg-adoption"
published: "2026-07"
added: "2026-09-04"
category: data-engineering
tags: [apache-iceberg, data-lake, lakehouse, table-format, migration]
novelty: 2
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Scaling Grab's Data Lake: Our Journey to Apache Iceberg Adoption

**Source:** [Grab Engineering](https://engineering.grab.com/our-journey-to-apache-iceberg-adoption) · Published 2026-07 · Added 2026-09-04
**Category:** Data Engineering · **Tags:** `apache-iceberg`, `data-lake`, `lakehouse`, `table-format`, `migration`

## TL;DR

Grab migrated its petabyte-scale, billions-of-S3-objects data lake from directory-based Hive Parquet tables to Apache Iceberg, driven by four compounding pain points (catalog latency, small files, operational toil, and catalog-storage drift), building an open-sourced `UnifiedSparkCatalog` tool to make the migration transparent to users — and reporting roughly 10x query-runtime improvements, up to 95% lower S3 API costs, and about 50% lower compute usage on migrated workloads.

## 1. Business context

At Grab's scale — petabytes of data across billions of S3 objects — the data lake had run for years on Hive Parquet tables managed via Hive Metastore with a directory-based layout. That approach was showing its age: query planning time scaled linearly with the number of partitions, causing latency spikes under concurrent load; datasets fragmented into huge numbers of tiny files (some ML datasets averaged under 1MB per file across thousands of files per partition), driving up both S3 API costs and scan times; engineers had to manually register partitions and work around the lack of native ACID transaction support; and because the Metastore was the system of record while data was frequently modified directly in S3, the catalog regularly drifted out of sync with what was actually on disk. Apache Iceberg — an open table format with native ACID support, metadata-based (not listing-based) file discovery, and no partition-registration step — directly targets these four problems.

## 2. Technical details

- **Prior architecture:** Hive Parquet tables, Hive Metastore as catalog, directory-based (partition-path) layout — the traditional Hadoop-lakehouse pattern.
- **Four pain points that drove the migration:** (1) catalog latency — query planning time scaled linearly with partition count; (2) the small-file problem — some datasets had sub-1MB files, thousands per partition; (3) operational toil — manual partition registration and no native ACID support meant complex workarounds for data changes; (4) catalog-storage sync drift — direct S3 modifications left the Metastore stale relative to actual on-disk state.
- **Migration strategy:** rather than a big-bang conversion, Grab prioritized migrating the highest-value tables first, to avoid disrupting downstream consumers still depending on the existing Hive tables during the transition.
- **UnifiedSparkCatalog:** a custom, open-sourced Spark catalog that transparently routes queries to the correct underlying format-specific catalog (Iceberg, Delta, Hudi, or Hive) based on the table, without requiring users to know or specify the table format (e.g., no `iceberg_catalog.schema.table`-style prefixing needed) — letting teams keep writing standard SQL/Spark queries across a mixed-format lake during and after migration.
- **Performance techniques:** Iceberg's metadata-based file pruning plus Z-ordering and data-skipping were used to cut query scan volume on migrated tables.

## 3. Impact — potential & realized

- **Realized:** on a navigation dataset, query runtime dropped roughly 10x (from about 70 seconds to about 6 seconds) via Z-ordering and data skipping; daily S3 API costs on heavily-queried operations tables dropped up to 95% through larger files and eliminated directory listings; funnel-analysis workloads saw cluster resource usage reduced by roughly half.
- **Potential:** the `UnifiedSparkCatalog` pattern — abstracting away table-format differences behind one catalog interface — is a reusable template for any organization running a mixed-format lakehouse (Iceberg alongside legacy Hive/Delta/Hudi tables) during a multi-year migration, letting format modernization proceed incrementally without breaking downstream query authors.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — excellent execution of an industry-standard migration, not a new idea

Migrating from Hive/Parquet directory-based tables to Apache Iceberg is now a well-trodden industry path (multiple large companies have published similar migrations), and the underlying pain points — catalog latency, small files, partition-registration toil, catalog-storage drift — are exactly the problems Iceberg was designed to solve. Grab's write-up is genuinely useful as an operational playbook (the phased, highest-value-tables-first rollout and the `UnifiedSparkCatalog` abstraction for a mixed-format transition period are both practical, reusable details), but it doesn't introduce new techniques — it's a recap of established lakehouse migration practice done well at scale, which is why it scores a 2 rather than higher.

### Similar / related work

- [**How Databricks Feature Store Serves Features with Sub-Second Freshness**](2026-08-30-databricks-feature-store-subsecond-freshness.md) (in this bank) — a different data-infrastructure modernization effort (feature serving rather than the lake's table format) from the same broad "lakehouse-era" wave of infrastructure investment.
- **Using Grab's Trust Counter Service to Detect Fraud Successfully** ([Grab Engineering](https://engineering.grab.com/using-grabs-trust-counter-service-to-detect-fraud-successfully)) — a different Grab data-infrastructure system (a real-time counter service for fraud detection), useful context on the surrounding data platform this Iceberg migration underpins.

### Jargon buster

- **Apache Iceberg** — an open table format for large analytic datasets that tracks table state (schema, partitioning, snapshots) via metadata files rather than directory listings, enabling ACID transactions, schema evolution, and fast metadata-based query planning on top of plain object storage like S3.
- **Small-file problem** — a performance and cost issue in distributed data systems where data is fragmented into many tiny files rather than fewer, larger ones, increasing the number of storage-API calls and per-file overhead needed to read a dataset.
- **Z-ordering** — a technique for physically co-locating rows with similar values across multiple columns within data files, so queries that filter on those columns can skip reading irrelevant files.
- **Catalog (in a data lake)** — the system of record that tracks which files make up which tables/partitions; Hive Metastore is one implementation, and Iceberg's own metadata layer is another, more consistent alternative.
