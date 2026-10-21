---
id: arxiv-rerandomization-assignment-dependent-covariates-network-interference
title: "Rerandomization and high-dimensional adjustment with assignment-dependent auxiliary variables under network interference"
source: "arXiv stat.ME (Zhang, Wei & Liu)"
url: "https://arxiv.org/abs/2610.27741"
published: "2026-10"
added: "2026-10-21"
category: experimentation-causal
tags: [rerandomization, network-interference, lasso-adjustment, horvitz-thompson, covariate-adjustment]
novelty: 3
sourced_via: "web search"
---

# Rerandomization and high-dimensional adjustment with assignment-dependent auxiliary variables under network interference

**Source:** [arXiv stat.ME (Zhang, Wei & Liu)](https://arxiv.org/abs/2610.27741) · Published 2026-10 · Added 2026-10-21
**Category:** experimentation-causal · **Tags:** `rerandomization`, `network-interference`, `lasso-adjustment`, `horvitz-thompson`, `covariate-adjustment`

## TL;DR

Extends rerandomization and regression adjustment to network experiments where auxiliary variables (e.g. treated-neighbour summaries) depend on the assignment, showing the two are asymptotically equivalent and adding Lasso adjustment for high-dimensional covariates.

## 1. Business context

Network experiments (social products, vaccine trials) violate no-interference, and natural covariates like neighbour treatment summaries are themselves functions of the assignment, which breaks standard rerandomization and adjustment theory.

## 2. Technical details

Uses Mahalanobis-distance-based rerandomization and derives asymptotic distributions of the Horvitz-Thompson and Hajek estimators under approximate neighbourhood interference. At analysis, they adjust directly on estimation errors in the auxiliary exposure effects, needing no normalization and optimal among linear adjustments. Rerandomization and adjustment become asymptotically equivalent as the threshold approaches zero. For high-dimensional covariates, Lasso-adjusted estimators are shown jointly asymptotically normal under sparsity and keep that distribution with fixed-dimension rerandomization.

## 3. Impact — potential & realized

Reported: simulations and a social-network application illustrate precision gains. The abstract gives no figures. Potential: tighter confidence intervals in network experiments without more users.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Unifies rerandomization and Lasso adjustment for network experiments with assignment-dependent covariates.

Incremental but practical for social/marketplace experimenters: it clarifies that design-time and analysis-time adjustment buy the same thing, so choose by convenience. Overlaps with an entry already in the bank on rerandomization under interference. Abstract-level read; theory-heavy (43 pages) with small empirical evidence. Novelty 3/5.

### Similar / related work

- [**Rerandomization under Interference**](2026-09-29-arxiv-rerandomization-under-interference.md) — earlier entry on the same design problem (in this bank)
- [**Sequentially Rerandomized Switchback**](2026-10-05-arxiv-sequentially-rerandomized-switchback.md) — rerandomization for interference in switchback experiments (in this bank)

### Jargon buster

- **Rerandomization** — Redrawing the random assignment until covariates are acceptably balanced, then analysing with that in mind.
- **Network interference** — One unit's outcome depends on treatments of connected units.
- **Hajek estimator** — A ratio (normalized) version of the Horvitz-Thompson inverse-probability-weighted mean.
