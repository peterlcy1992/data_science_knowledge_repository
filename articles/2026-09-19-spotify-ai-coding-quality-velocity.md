---
id: spotify-ai-coding-quality-velocity
title: "AI Changed How Spotify Builds: What We Learned (and Fixed) About Quality at Higher Velocity"
source: "Spotify Engineering"
url: "https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity"
published: "2026-09"
added: "2026-09-19"
category: llm-genai
tags: [agentic-coding, engineering-velocity, quality-engineering, reliability, ai-coding-agents]
novelty: 3
sourced_via: "web search"
---

# AI Changed How Spotify Builds: What We Learned (and Fixed) About Quality at Higher Velocity

**Source:** [Spotify Engineering](https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity) · Published 2026-09 · Added 2026-09-19
**Category:** LLMs & Generative AI · **Tags:** `agentic-coding`, `engineering-velocity`, `quality-engineering`, `reliability`, `ai-coding-agents`

## TL;DR

As AI-assisted and agentic coding roughly doubled Spotify's merged-change volume year over year, quality problems that used to surface slowly started compounding faster than review, testing, rollout, and observability systems could catch them. Spotify's investigation found AI-authored code was not the direct cause — the surrounding delivery infrastructure simply hadn't been built for the new velocity — and it walks through the fixes across four incident classes: content-processing delays, fleet-update failures, compute shortages, and mobile quality regressions.

## 1. Business context

Spotify, like many engineering organizations in 2026, leaned hard into AI-assisted and agentic coding to accelerate delivery. The immediate effect was a step change in throughput: total merged changes more than doubled year over year in August (from roughly 8,100 to 17,000), and the share of that work classified as quality/optimization work rose from 27% to 31% — meaning engineers put more than twice as much absolute effort into quality-related work as the year before, yet still saw a cluster of production incidents. Four areas were hit: media content processing fell behind and delayed availability, automated fleet updates began causing production failures, compute capacity ran short during peak load, and mobile app quality regressions accumulated faster than existing detection systems could flag them. The business risk was that AI coding velocity would be blamed and throttled, when the actual gap was between how fast code could now be produced and how fast the surrounding delivery systems (monitoring, rollout safety, capacity planning, regression detection) could absorb it.

## 2. Technical details

Spotify's engineering team dug into whether AI-authored code itself was the quality culprit, tracking a rework-rate metric (how much recently written code gets modified again) rather than raw code churn, since churn alone rises naturally with AI-assisted editing patterns. They found their rework rate showed no corresponding rise relative to the broader industry-wide increase in code churn — i.e., no evidence of accumulating "AI-induced quality debt." Instead, each of the four incident classes traced back to delivery infrastructure that hadn't scaled with throughput:

- **Content processing** — added end-to-end monitoring across the pipeline, fixed underlying scheduling bugs, implemented workload prioritization so higher-priority jobs weren't starved, and increased transcoding capacity.
- **Fleet updates** — strengthened rollout safeguards and expanded rollback capacity, and moved risky scheduling changes to team working hours so failures could be caught and reverted quickly by the people who understood them.
- **Compute management** — doubled reserved edge capacity and redesigned failover mechanisms to gracefully degrade lower-tier services under load rather than failing outright.
- **Mobile quality** — broadened the set of quality signal metrics tracked and incorporated longer-term trend analysis, so slow-accumulating regressions (individually invisible, cumulatively significant) would surface before they became user-facing incidents.

The throughline is treating AI-driven velocity as a capacity-planning and observability problem rather than a code-authorship problem: the fixes are almost entirely in infrastructure and process (monitoring coverage, rollback capacity, capacity headroom, longer detection windows), not in constraining how code gets written.

## 3. Impact — potential & realized

**Realized:** merged changes roughly doubled year over year (8,100 → 17,000 in August) while the rework-rate metric — Spotify's chosen quality signal — showed no corresponding increase, i.e., no measurable rise in AI-induced rework relative to the industry-wide code-churn trend. The four incident classes (content processing, fleet updates, compute capacity, mobile quality) were each addressed with specific infrastructure fixes described above.

**Potential:** the piece is a useful "second-order" case study for any organization scaling agentic coding adoption — the failure mode isn't necessarily code quality itself, but the delivery, rollout, and observability systems built for a slower cadence. It offers rework-rate (not raw churn) as a better AI-quality signal, and argues against reflexively tightening review thresholds in response to a volume increase, since that treats a capacity problem as an authorship problem.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid production learnings, not a new technique

There's no new model, architecture, or algorithm here — this is an engineering-culture and reliability-engineering retrospective. What makes it worth reading is the discipline of separating "AI wrote more code" from "AI wrote worse code," and choosing a metric (age-weighted rework rate) that actually tests that distinction rather than reaching for the more alarming but less precise raw-churn number. That's a production-first, empirically grounded take on a question — does agentic coding hurt quality? — that a lot of organizations are currently answering with anecdote.

### Similar / related work

- [**Coding Had a Concurrency Problem: How Mux Helped Solve It**](2026-09-11-coinbase-mux-multi-agent-coding-tool.md) (in this bank) — Coinbase's infrastructure response to a different agentic-coding scaling problem (concurrent agent sessions colliding), the same broader theme of building supporting infrastructure around AI coding agents rather than treating them as drop-in replacements for the old workflow.
- [**Delegating Engineering Work to Cloud-Based Agents (Flux)**](2026-08-31-doordash-flux-cloud-agents-engineering.md) (in this bank) — DoorDash's cloud agent platform, another example of an org restructuring engineering infrastructure (not just tooling) around high-volume agentic code generation.
- **"1,500+ PRs Later: Spotify's Journey with Our Background Coding Agent (Honk)"** — [Spotify Engineering](https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1) — Spotify's own earlier post on the background coding agent (Honk) whose adoption is the direct cause of the throughput increase analyzed in this article.

### Jargon buster

- **Rework rate** — the fraction of recently-written code that gets modified again soon after, used here as a quality proxy; Spotify specifically age-weights it rather than using raw code churn, since churn rises mechanically with faster editing regardless of quality.
- **Fail-open / graceful degradation** — a system design pattern where, under overload, lower-priority services are deliberately degraded or shed first so core functionality keeps working, instead of the whole system failing outright.
- **Agentic coding** — AI coding tools that operate with more autonomy than autocomplete-style assistants, capable of planning and executing multi-step changes (e.g., opening PRs) with limited human intervention per change.
