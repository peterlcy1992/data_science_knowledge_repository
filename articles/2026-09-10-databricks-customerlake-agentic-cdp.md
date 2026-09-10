---
id: databricks-customerlake-agentic-cdp
title: "Introducing CustomerLake: The Agentic CDP Embedded in Databricks"
source: "Databricks Blog"
url: "https://www.databricks.com/blog/introducing-customerlake-agentic-cdp"
published: "2026"
added: "2026-09-10"
category: data-engineering
tags: [customer-data-platform, ai-agents, unity-catalog, identity-resolution, martech, lakehouse]
novelty: 3
sourced_via: "web search"
---

# Introducing CustomerLake: The Agentic CDP Embedded in Databricks

**Source:** [Databricks Blog](https://www.databricks.com/blog/introducing-customerlake-agentic-cdp) · Published 2026 · Added 2026-09-10
**Category:** Data Engineering · **Tags:** `customer-data-platform`, `ai-agents`, `unity-catalog`, `identity-resolution`, `martech`, `lakehouse`

## TL;DR

Databricks launched CustomerLake, a Customer Data Platform (CDP) embedded natively in the lakehouse rather than bolted on as a separate system, built around autonomous Profile Agents (which unify customer records via "Agentic Identity Resolution") and Campaign Agents (which run continuous "infinity campaigns" instead of one-off blasts) — both operating on Unity Catalog-governed data with Lakehouse Federation reaching across Snowflake, BigQuery, and other stores without duplicating data.

## 1. Business context

Traditional CDPs sit outside a company's core data platform, so building a "golden record" customer profile means duplicating and reconciling data across systems — a process the post says can take months — and every new marketing tool added creates its own silo requiring separate security and governance. On top of that, static, one-off campaign workflows can't keep pace with AI-era customer expectations for continuous, personalized, real-time engagement. CustomerLake is Databricks' bet that a CDP embedded directly in the lakehouse, governed by the same catalog as the rest of the company's data, solves both the fragmentation and the staleness problems at once.

## 2. Technical details

**Profile Agents** transform raw customer data into "Customer 360" profiles directly within Databricks, using what the post calls **Agentic Identity Resolution (AIR)** — combining deterministic matching rules, probabilistic matching models, and agentic (LLM-driven) reasoning to unify disconnected records that reference the same underlying customer. The agents also flag data-quality issues, support pulling in third-party enrichment data, and maintain continuous feedback loops that improve profile accuracy over time rather than treating profile-building as a one-time batch job.

**Campaign Agents** run what Databricks calls "infinity campaigns" — continuous engagement loops that replace traditional one-off campaign sends. They draw on the same governed customer context (attributes, behavioral signals, predictive model outputs, eligibility rules, operational context) to build target audiences, recommend next-best actions per customer, activate messaging across channels, and continuously optimize based on real-time performance feedback.

The whole system is **embedded natively in the lakehouse** and governed through **Unity Catalog** — the same governance layer covering the rest of a customer's Databricks data estate (and the subject of Databricks' companion governance-framework post this week). **Lakehouse Federation** lets CustomerLake read customer data living in Databricks, Snowflake, BigQuery, cloud storage, or operational databases without copying it into a separate CDP-specific store, and bidirectional **Reverse ETL** pipelines connect out to martech partners including Adobe, Meta, Braze, and LiveRamp for activation.

## 3. Impact — potential & realized

**Realized:** this is a product-launch announcement; the post reports no quantitative benchmarks, customer case-study numbers, or before/after comparisons, beyond an aspirational framing of delivering "the perfect customer experience — a billion times a day."

**Potential:** if the no-duplication, catalog-governed approach works as described, it removes a structural pain point of traditional CDPs (maintaining a separately governed copy of customer data) — which would matter most to companies already standardized on Databricks and Unity Catalog for their broader data estate, since the value proposition depends heavily on already being inside that ecosystem.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sound integration play, not a new capability category

Identity resolution and campaign orchestration are mature CDP capabilities, and "embed the CDP in the data platform instead of bolting it on" is a natural, expected move for a company that already owns the underlying lakehouse and catalog — not a conceptual breakthrough. What earns this a 3 rather than lower is that the integration removes a real, specific pain point (duplicated, separately governed customer data) rather than just repackaging existing CDP features, and ties cleanly into the same governance framework Databricks is pushing this week. It's a strong product move within Databricks' existing platform strategy rather than something genuinely new to the CDP category.

### Similar / related work

- [**Governance Beyond Security: Knowledge, Context & Ontology on the Lakehouse**](2026-09-10-databricks-governance-knowledge-context-ontology-lakehouse.md) (in this bank) — the governance framework CustomerLake is built on top of; read together, they show Databricks' broader thesis that Unity Catalog governance is what makes trustworthy agentic products like CustomerLake possible.
- [**The 40-Year-Old Database Rule Agents Just Broke: How LTAP Unifies OLTP and OLAP Workloads**](2026-09-10-databricks-ltap-unify-oltp-olap-agents.md) (in this bank) — a third Databricks post from the same week arguing AI agents require rethinking established data-infrastructure assumptions, here about storage architecture rather than governance or customer data.
- **Traditional CDP category (Segment, Adobe RTCDP, mParticle)** — the established category CustomerLake positions itself against, differentiated primarily by native lakehouse embedding rather than a fundamentally different capability set.

### Jargon buster

- **Customer Data Platform (CDP)** — software that unifies customer data from multiple sources into a single profile per customer, typically used to power marketing personalization and targeting.
- **Agentic Identity Resolution (AIR)** — CustomerLake's term for combining deterministic rules, probabilistic matching, and LLM-agent reasoning to decide which scattered records belong to the same real customer.
- **Lakehouse Federation** — a Databricks capability that lets queries reach data living in other systems (Snowflake, BigQuery, cloud storage) without copying it into Databricks first.
- **Reverse ETL** — pipelines that push data *out* of a central warehouse/lakehouse into operational tools (here, marketing platforms like Adobe or Braze), the inverse direction of typical ETL that pulls data in.
