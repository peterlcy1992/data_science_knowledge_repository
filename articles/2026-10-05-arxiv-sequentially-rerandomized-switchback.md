---
id: arxiv-sequentially-rerandomized-switchback
title: "Sequentially-Rerandomized Switchback Experiments"
source: "arXiv (Zeng, Adjaho, Bucarey, Qin, Zhang, Hoban, Johari, Wager)"
url: "https://arxiv.org/abs/2604.02489"
published: "2026-04"
added: "2026-10-05"
category: experimentation-causal
tags: [switchback, rerandomization, interference, carryover, marketplace-experiments]
novelty: 4
sourced_via: "web search"
---

# Sequentially-Rerandomized Switchback Experiments

**Source:** [arXiv (Zeng, Adjaho, Bucarey, Qin, Zhang, Hoban, Johari, Wager)](https://arxiv.org/abs/2604.02489) · Published 2026-04 · Added 2026-10-05
**Category:** experimentation-causal · **Tags:** `switchback`, `rerandomization`, `interference`, `carryover`, `marketplace-experiments`

## TL;DR

SRSB re-randomizes treatment assignment across units at every time step while forcing balance on covariates derived from history, giving finite-sample and asymptotic inference for platform experiments with few units, heterogeneity, non-stationarity and carryover.

## 1. Business context

Large platforms and marketplaces often cannot randomize at the user level, so they test new policies by randomizing operational units (geographies, regions, clusters) over many time periods. The source names the hard parts: a limited number of units, substantial cross-unit heterogeneity, non-stationarity, and potential carryover across periods. Plain switchbacks pay for all of these in noisy, hard-to-defend estimates.

## 2. Technical details

Sequentially-Rerandomized Switchback (SRSB) re-randomizes treatment assignment at each time step while keeping the assignment balanced on predetermined variables derived from historical data. The authors develop both finite-sample inference and asymptotic inference as the number of periods grows. For settings where past treatment affects current outcomes they add a blocked SRSB variant that rerandomizes within strata defined by the previous treatment, forming stable and comparable 'stay' groups.

## 3. Impact — potential & realized

Per the abstract, simulation studies show practical improvements and robustness relative to traditional switchback designs. No production deployment or specific effect sizes are reported in the abstract I could access (33 pages, 10 figures; full paper not read). Potential: tighter, valid inference for marketplace policy tests (pricing, dispatch) run with a handful of regions.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A design-stage fix (rerandomization on history) rather than another estimator, from the Stanford/Wager-Johari group with industry co-authors.

Rerandomization is well studied for cross-sectional trials; applying it sequentially in switchbacks, with inference that stays valid under carryover, addresses a gap practitioners hit constantly. Evidence here is simulation-only as far as the abstract shows, so treat magnitude claims as unproven. Likely to be copied by marketplace experimentation teams.

### Similar / related work

- [**CUPED on Steroids: Multivariate Covariate Adjustment for Switchback Experiments**](2026-09-29-arxiv-cuped-on-steroids-switchback.md) — in-bank: covariate adjustment, the analysis-stage counterpart to SRSB's design-stage balancing
- [**Randomization Tests in Switchback Experiments**](2026-10-05-arxiv-randomization-tests-switchback.md) — in-bank: finite-sample tests for the same designs
- [**Cluster-Level Experiments using Temporal Switchback Designs**](2026-10-05-arxiv-cluster-switchback-airline-pricing.md) — in-bank: switching cadence and precision

### Jargon buster

- **Switchback experiment** — Alternating an entire unit (market, platform) between treatment and control over time blocks, used when user-level randomization is infeasible or interference is unavoidable.
- **Carryover** — Treatment in one period still influencing outcomes in later periods, which biases naive switchback comparisons.
- **Rerandomization** — Redrawing a random assignment until it is balanced on chosen covariates, improving precision while preserving randomization-based inference.
