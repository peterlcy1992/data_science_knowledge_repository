---
id: instacart-variance-reduction-below-randomization-grain
title: "Variance Reduction Below the Randomization Grain"
source: "Instacart Tech Blog"
url: "https://tech.instacart.com/variance-reduction-below-the-randomization-grain-31719f87a7d2"
published: "2026"
added: "2026-09-30"
category: experimentation-causal
tags: [variance-reduction, cuped, cluster-randomization, marketplace, spillover]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Variance Reduction Below the Randomization Grain

**Source:** [Instacart Tech Blog](https://tech.instacart.com/variance-reduction-below-the-randomization-grain-31719f87a7d2) · Published 2026 · Added 2026-09-30
**Category:** experimentation-causal · **Tags:** `variance-reduction`, `cuped`, `cluster-randomization`, `marketplace`, `spillover`

## TL;DR

Instacart shows that order-level ML predictions, aggregated up to the (coarse) randomization unit, can be used CUPED-style to cut variance in cluster-randomized marketplace experiments, shortening experiment time.

## 1. Business context

Instacart's dispatch system solves a bipartite matching problem between shoppers and orders, so assignments are global and interdependent: changing handling of one order ripples to nearby orders and can contaminate controls. That forces cluster-level randomization, which sharply reduces the number of independent units and statistical power, slowing experimentation.

## 2. Technical details

The post's idea: although randomization happens at a coarse level, outcomes are predictable at a finer grain. Order-level predictions are aggregated to the randomization unit and used as a covariate in a CUPED-like adjustment, keeping CUPED's structure while exploiting finer-grained covariate information. Authors: Sergio Camelo, Caitlin Kearns, Matias Cersosimo and Tilman Drerup. I could not retrieve the full post (HTTP 403), so model details and figures are from search-surfaced summaries and are omitted where unclear.

## 3. Impact — potential & realized

Per the post's summary, this yields considerable reductions in experimentation time. Exact variance-reduction percentages were not available to me. Potential: makes cluster-randomized marketplace tests practical at more granular decisions.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A practical fix for the power problem in cluster-randomized marketplaces

The insight — fine-grained predictability can rescue power at coarse randomization — is intuitive and likely transferable to any marketplace with interference. Novelty is moderate because it builds on CUPED/CUPAC, and I could not verify the quantitative results.

### Similar / related work

- [**Variance Reduction Combining Pre-Experiment and In-Experiment Data**](2026-09-30-arxiv-variance-reduction-pre-and-in-experiment-etsy.md) — another CUPED extension that adds covariate sources.
- [**CUPED on Steroids: Multivariate Covariate Adjustment for Switchback Experiments**](2026-09-29-arxiv-cuped-on-steroids-switchback.md) — variance reduction for another interference-driven design.
- [**Rerandomization under Interference**](2026-09-29-arxiv-rerandomization-under-interference.md) — design-stage approach to the interference problem.

### Jargon buster

- **Randomization grain** — The unit at which treatment is assigned (e.g. a region-time cluster rather than an individual order).
- **Cluster randomization** — Assigning whole groups of units to the same arm to avoid spillover, at the cost of fewer effective samples.
- **Interference** — When one unit's treatment affects other units' outcomes.
