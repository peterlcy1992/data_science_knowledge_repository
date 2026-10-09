---
id: arxiv-blocking-online-experiments-skewed-data
title: "On the Benefit of Blocking for Online Experiments with Skewed Data"
source: "arXiv stat.AP (Zaidi, Reimherr, Friedberg, Martinez, Mudd)"
url: "https://arxiv.org/abs/2610.10435"
published: "2026-10"
added: "2026-10-09"
category: experimentation-causal
tags: [blocking, stratified-randomization, winsorization, skewed-metrics, variance-reduction]
novelty: 3
sourced_via: "web search"
---

# On the Benefit of Blocking for Online Experiments with Skewed Data

**Source:** [arXiv stat.AP (Zaidi, Reimherr, Friedberg, Martinez, Mudd)](https://arxiv.org/abs/2610.10435) · Published 2026-10 · Added 2026-10-09
**Category:** experimentation-causal · **Tags:** `blocking`, `stratified-randomization`, `winsorization`, `skewed-metrics`, `variance-reduction`

## TL;DR

For heavy-tailed online metrics, the authors argue blocked (stratified) assignment gives only a modest precision gain (about 5-10%) but beats post-hoc adjustment structurally: a fixed-weight blocked estimator targets the true average treatment effect, and blocking lets you winsorize outliers within blocks without erasing tail treatment effects.

## 1. Business context

Most online metrics (revenue, spend, usage) are highly skewed: a handful of extreme users dominate the variance, making A/B tests insensitive. Teams usually reach for post-hoc fixes (regression adjustment, global winsorization, efficiency-weighted estimators). The question here is whether changing the assignment design itself is worth the operational cost.

## 2. Technical details

The paper compares blocked (stratified) randomization with post-hoc analysis choices. Two claims from the abstract: (1) the precision gain from blocking is limited, roughly 5-10%, because discretising a continuous skewed covariate into blocks loses information; (2) the real advantages are structural. A fixed-weight blocking estimator targets the true average treatment effect (ATE), whereas efficiency-weighted combinations of block effects introduce severe bias for the ATE; and because blocks isolate extreme outliers, winsorization can be applied within each block, controlling noise without erasing tail-end treatment effects that global winsorization would clip. Specific simulation or production datasets were not visible in the abstract page; details would need the full text.

## 3. Impact — potential & realized

Realized (as stated by the authors): ~5-10% precision improvement. Potential: a principled way to handle outliers by design rather than by trimming, preserving the estimand. Unclear from the abstract: the datasets, whether results come from real company experiments, and the block-count guidance.

*Sourced from the arXiv abstract page; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Modest numbers, but a useful reframing: blocking is about estimand and outlier handling, not raw power.

The headline 5-10% is honest and unglamorous. What is interesting is the argument that the choice of weights silently changes the estimand, and that within-block winsorization keeps heavy-tail effects. Platform teams that already stratify on pre-period spend are the likely adopters. I only saw the abstract, so treat the bias claims as the authors' until checked against the full text.

### Similar / related work

- [**Measuring Gift Card Program Incrementality via Causal Data Fusion**](2026-10-07-arxiv-airbnb-gift-card-incrementality-data-fusion.md) (in this bank) — another route to better estimates; 
- [**Variance reduction combining pre-experiment and in-experiment data**](2026-10-08-etsy-variance-reduction-pre-and-in-experiment-data.md) (in this bank) — related work on the same theme
- [**Variance Reduction Below the Randomization Grain**](2026-09-30-instacart-variance-reduction-below-randomization-grain.md) (in this bank) — related work on the same theme

### Jargon buster

- **Blocking / stratified randomization** — Group similar units (e.g. by past spend) and randomize within each group so arms are balanced on that covariate by construction.
- **Winsorization** — Capping extreme values at a percentile to tame outliers; done globally it can hide real tail effects.
- **ATE** — Average treatment effect: the mean outcome difference if everyone were treated vs. not.
