---
id: arxiv-cluster-switchback-airline-pricing
title: "Cluster-Level Experiments using Temporal Switchback Designs"
source: "arXiv (Ferrari-Ortiz, Orellana-Montini, Abbiasov, Garkavenko, Lit)"
url: "https://arxiv.org/abs/2603.04252"
published: "2026-03"
added: "2026-10-05"
category: experimentation-causal
tags: [switchback, cluster-experiments, two-way-fixed-effects, airline-pricing, power]
novelty: 3
sourced_via: "web search"
---

# Cluster-Level Experiments using Temporal Switchback Designs

**Source:** [arXiv (Ferrari-Ortiz, Orellana-Montini, Abbiasov, Garkavenko, Lit)](https://arxiv.org/abs/2603.04252) · Published 2026-03 · Added 2026-10-05
**Category:** experimentation-causal · **Tags:** `switchback`, `cluster-experiments`, `two-way-fixed-effects`, `airline-pricing`, `power`

## TL;DR

Using airline ancillary pricing as the case study, temporal switchback designs cut standard errors by up to 67% versus conventional cluster-level experiments; the paper gives a unified two-way fixed effects view of how switching frequency interacts with temporal patterns.

## 1. Business context

Many business decisions, such as pricing by route or market, cannot be randomized at the individual level, so teams run cluster-level (often geographic) experiments, which have few units and low power. The paper asks how much alternating clusters over time can recover.

## 2. Technical details

The authors give a unified Two-Way Fixed Effects (TWFE) interpretation of temporal switchback designs that clarifies how switching frequency interacts with temporal patterns to determine precision. They compare weekly and daily switching using synthetic calibrations and real airline ancillary pricing data.

## 3. Impact — potential & realized

Reported (abstract): standard errors fall by up to 67% on operational airline data. Daily switching gave the largest efficiency gains over short periods; weekly switching was a simpler, operationally easier option with strong performance. 'Up to' means best case; carryover handling was not covered in the abstract I read.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Useful quantification of the switchback precision gain with a clean TWFE framing.

The TWFE lens is helpful for power planning, and the daily-vs-weekly trade-off is directly actionable. Single industry setting, so generalization is unproven.

### Similar / related work

- [**Sequentially-Rerandomized Switchback Experiments**](2026-10-05-arxiv-sequentially-rerandomized-switchback.md) — in-bank: smarter assignment for switchbacks
- [**Randomization Tests in Switchback Experiments**](2026-10-05-arxiv-randomization-tests-switchback.md) — in-bank: inference and carryover diagnostics

### Jargon buster

- **Two-Way Fixed Effects** — A regression with unit and time fixed effects that absorbs stable unit differences and common time shocks.
- **Cluster-level experiment** — Randomizing groups (regions, markets) rather than individuals.
