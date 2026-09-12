---
id: grab-data-mesh-dpi-automated-reliability
title: "Data Mesh at Grab (Part III): Operationalizing Data Reliability with Automated DPIs"
source: "Grab Engineering Blog"
url: "https://engineering.grab.com/data-mesh-at-grab-part-three"
published: "2026-08"
added: "2026-09-12"
category: data-engineering
tags: [data-mesh, data-quality, data-contracts, incident-automation, observability, grab]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Data Mesh at Grab (Part III): Operationalizing Data Reliability with Automated DPIs

**Source:** [Grab Engineering Blog](https://engineering.grab.com/data-mesh-at-grab-part-three) · Published 2026-08 · Added 2026-09-12
**Category:** Data Engineering · **Tags:** `data-mesh`, `data-quality`, `data-contracts`, `incident-automation`, `observability`, `grab`

## TL;DR

Grab built a four-stage Data Production Issue (DPI) lifecycle — triage, diagnosis, ownership routing, and auto-resolution — that turns data-contract breaches into structured, owned incidents instead of silent quality drift, and reports that 86.9% of DPIs now resolve automatically with a 6x faster mean time to resolve than manually-raised issues.

## 1. Business context

Grab had already invested in certifying data products against reliability standards (per earlier parts of this Data Mesh series), but certification alone didn't stop production failures: freshness delays, upstream outages, and data-quality violations kept eroding trust in "certified" data. The gap wasn't detection — contract tests could catch a violation — it was everything downstream of detection: distinguishing a real breach from noise, figuring out who actually owns the fix across a highly heterogeneous set of platforms, and closing the loop without every incident consuming scarce engineering time.

## 2. Technical details

Grab's answer is a four-stage Data Production Issue (DPI) lifecycle:

1. **Triage** — an incident orchestrator (internally "Kinabalu") evaluates contract test results against defined reliability expectations, explicitly separating individual test failures from overall pipeline health, deduplicating repeated alerts, and gathering surrounding context before promoting anything to a confirmed contract breach.
2. **Diagnosis & ownership routing** — a Data Health API classifies each failure into one of four categories — `UPSTREAM_ERROR`, `PLATFORM_ERROR`, `JOB_ERROR`, `DATA_ERROR` — and uses that taxonomy to route the issue to whichever team can actually fix the root cause, rather than defaulting to the nominal data-asset owner who may have no control over an upstream dependency.
3. **Diagnosis architecture ("Hugo")** — a three-stage internal system: collect signals from multiple sources, apply specialized diagnosis logic per alert type, and persist a structured result that includes a recommended fix.
4. **Auto-resolution** — Hugo executes remediation strategies (retries, waiting on dependencies, custom resolvers per failure type), verifies that the issue actually recovered, and escalates to a human only for the residual complex cases that don't fit a known playbook.

## 3. Impact — potential & realized

**Realized:** 86.9% of DPIs are resolved automatically without human intervention; more than 95% of DPIs are now raised automatically by the system rather than reported manually; automatically-raised DPIs resolve roughly 6x faster (mean time to resolve) than manually-raised ones.

**Potential:** the four-stage lifecycle and, specifically, the failure-category taxonomy for ownership routing are presented as reusable patterns for any data-mesh organization where data products span many teams and platforms and where "who owns this fix" is often a harder problem than "what broke."

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid operational engineering, with the ownership-routing taxonomy as the standout idea

Automated remediation and alert deduplication are well-trodden territory in data-quality tooling; what's more distinctive here is the explicit four-category failure taxonomy used purely to solve *ownership routing* in a decentralized data-mesh org — a problem that's organizational as much as technical, and one most data-quality write-ups gloss over in favor of the detection/remediation mechanics. The 86.9% auto-resolution rate is a strong number, though it's worth noting that figure describes DPIs the system chose to attempt auto-resolution on; the article doesn't break out how many total contract violations were filtered out before reaching that stage.

### Similar / related work

- **Glassdoor — Data Quality and Anomaly Detection at Petabyte Scale** — a comparable data-quality-at-scale problem tackled with data contracts, static analysis, and LLM-based logic checks rather than Grab's incident-lifecycle-and-ownership-routing angle; still a backlog lead in this bank as of this writing, no specific URL known yet.
- [**AutoLR: Automating the Path from Research to Launch Review**](2026-09-08-netease-autolr-agentic-recsys-launch-review.md) (in this bank) — a different domain (recsys launches rather than data pipelines) that shares this article's core idea of routing evidence-backed decisions through automated stages with human escalation only for genuinely ambiguous cases.
- **Data contract / data mesh literature (general)** — the broader data-mesh and data-contract movement this multi-part Grab series is itself building on; no single canonical source.

### Jargon buster

- **Data contract** — a formal agreement (often machine-checkable) about the shape, freshness, and quality guarantees a data producer commits to for a given dataset, which downstream consumers can rely on.
- **Data Production Issue (DPI)** — Grab's internal term for a confirmed, structured incident raised when a data product breaches its contract, as opposed to a raw, unfiltered alert.
- **Mean time to resolve (MTTR)** — the average time between an issue being detected/raised and it being confirmed resolved; a standard operational-reliability metric borrowed here from classic incident management.
