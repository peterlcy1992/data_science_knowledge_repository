---
id: databricks-southern-company-scout-storm-intelligence
title: "Southern Company's SCOUT: Completing the Storm Intelligence Story"
source: "Databricks Blog"
url: "https://www.databricks.com/blog/southern-companys-scout-completing-storm-intelligence-story"
published: "2026-09"
added: "2026-09-08"
category: data-engineering
tags: [lakehouse, unity-catalog, real-time-data, utilities, disaster-response, data-governance, operational-analytics]
novelty: 2
sourced_via: "web search"
---

# Southern Company's SCOUT: Completing the Storm Intelligence Story

**Source:** [Databricks Blog](https://www.databricks.com/blog/southern-companys-scout-completing-storm-intelligence-story) · Published 2026-09 · Added 2026-09-08
**Category:** Data Engineering · **Tags:** `lakehouse`, `unity-catalog`, `real-time-data`, `utilities`, `disaster-response`, `data-governance`, `operational-analytics`

## TL;DR

Southern Company built SCOUT, a real-time storm-operations application on Databricks, to close the last gap in its storm-response pipeline — live visibility during an active storm — after already having pre-storm forecasting (SPEAR) and post-storm reliability analysis (RAMP). SCOUT unifies outage, customer, GIS, weather, terrain, and crew data into one governed lakehouse, and had 1,139 employees on it with 250+ using it during a single peak storm day in June.

## 1. Business context

Southern Company already had two pieces of its storm-response stack automated: SPEAR for pre-storm forecasting and resource staging, and RAMP for post-storm reliability analysis. The gap was the middle of the timeline — the active storm itself — when dispatchers and field crews had to pull outage data, customer records, terrain details, and crew assignments out of multiple disconnected legacy systems under time pressure. That fragmentation is a real operational cost during restoration: every extra minute spent cross-referencing systems is a minute not spent dispatching a crew or communicating a restoration estimate to affected customers. SCOUT is built to close that gap by giving dispatchers, storm-center leadership, and field teams one real-time operational view spanning Southern Company's operating businesses (Georgia Power, Alabama Power, Southern Company Services, Mississippi Power, and Southern LINC).

## 2. Technical details

SCOUT is built on Databricks' lakehouse stack rather than a bespoke real-time system:

- **Delta Lake** provides the underlying resilient storage for outage, customer, GIS, weather, terrain, and operational-hierarchy data, ingested into one unified lakehouse instead of being scattered across separate source systems.
- **Databricks Lakehouse warehouses** serve the application's real-time queries, refreshed on a roughly one-minute cadence — the mechanism that lets dispatchers see near-live outage and crew state rather than stale extracts.
- **Unity Catalog** provides centralized governance, with role-based, service-principal-driven access control across the different operating businesses that need to see (and be restricted from seeing) different slices of the data.
- **Collaborative notebooks** and **Genie Code** were used to accelerate building custom pipelines and application features, such as restoration-effort charts, without a from-scratch application-engineering build.

The source gives one illustrative example of the platform's query power: identifying every customer running a car wash, their associated transformers, and related downstream infrastructure — a cross-system query that used to require manual, ad hoc lookups — was completed in roughly two hours on SCOUT.

## 3. Impact — potential & realized

**Realized:** 1,139 employees across Southern Company's operating businesses had adopted SCOUT, with more than 250 using it concurrently during a single peak storm day in June. The platform won the 2025 S.E.E. (Southeastern Electric Exchange) Industry Excellence Award for improving outage-information accessibility.

**Potential:** Southern Company is exploring two extensions — AI-assisted dispatch recommendations (crew location, travel time, equipment, skills, and safety-policy matching), explicitly framed as keeping a human dispatcher in control rather than automating the decision away, and integrating Skydio autonomous drones for live damage assessment and video streaming directly into SCOUT during active events.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — A strong operational win, but standard lakehouse engineering

There's no new modeling technique or algorithm here — this is a case study in consolidating fragmented operational data onto a governed lakehouse and building a real-time application layer on top of it, which is exactly the pattern Databricks has published many times before (including this bank's own entry on Databricks Feature Store's sub-second freshness, and Discovery Bank's hyper-personalization platform). What makes it a worthwhile catalog entry is the concrete, credible adoption numbers — a named employee count, a named peak-usage figure during a real storm — rather than a vague "customers love it" claim, and the honest framing of AI as advisory-only for the dispatch-recommendation extension. That's good practice worth noting, but it's incremental engineering, not a new technique.

### Similar / related work

- [**Databricks — How Databricks Feature Store Serves Features with Sub-Second Freshness**](2026-08-30-databricks-feature-store-subsecond-freshness.md) (in this bank) — the same "lakehouse-as-real-time-operational-system" theme applied to ML feature serving instead of storm operations.
- [**Databricks — How Discovery Bank Delivers Hyper-Personalized Banking at Scale**](2026-09-03-databricks-discovery-bank-hyperpersonalization.md) (in this bank) — another Databricks customer story combining governed data (Unity Catalog) with an operational, customer-facing application layer.
- [**Google — Introducing WeatherNext 3**](2026-09-03-google-weathernext3-weather-forecasting.md) (in this bank) — a complementary piece of the same broader problem (weather-driven operational response), though WeatherNext 3 is about the forecasting model itself while SCOUT is about the operational data platform consuming forecasts and outage data during the event.

### Jargon buster

- **Lakehouse** — a data architecture that combines the low-cost, flexible storage of a data lake with the transactional guarantees and structure of a data warehouse, letting the same data serve both analytics and operational applications.
- **Unity Catalog** — Databricks' governance layer for managing data access, lineage, and permissions centrally across an organization's lakehouse.
- **Delta Lake** — the open storage format underlying Databricks' lakehouse, adding ACID transactions and versioning on top of files stored in cloud object storage.
- **Service principal** — a non-human identity (as opposed to a named user account) used to grant an application or pipeline scoped, auditable access to data.
