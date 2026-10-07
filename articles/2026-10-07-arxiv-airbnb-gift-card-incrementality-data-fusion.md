---
id: arxiv-airbnb-gift-card-incrementality-data-fusion
title: "Measuring Gift Card Program Incrementality via Causal Data Fusion"
source: "arXiv (Whitehouse, Betz, Zhang, Coles, Johari, Syrgkanis)"
url: "https://arxiv.org/abs/2610.08558"
published: "2026-10"
added: "2026-10-07"
category: experimentation-causal
tags: [data-fusion, incrementality, observational-plus-experimental, airbnb, heterogeneous-effects]
novelty: 4
sourced_via: "web search"
---

# Measuring Gift Card Program Incrementality via Causal Data Fusion

**Source:** [arXiv (Whitehouse, Betz, Zhang, Coles, Johari, Syrgkanis)](https://arxiv.org/abs/2610.08558) · Published 2026-10 · Added 2026-10-07
**Category:** experimentation-causal · **Tags:** `data-fusion`, `incrementality`, `observational-plus-experimental`, `airbnb`, `heterogeneous-effects`

## TL;DR

Airbnb-linked researchers estimate how much revenue gift cards actually add by fusing a large observational dataset with a smaller experiment from a different population, under an invariance assumption on the relative treatment effect.

## 1. Business context

Gift card possession is only observed when a purchase happens, so treatment status is censored and counterfactual spending is not directly visible. Marketing needs incrementality, not raw gift-card revenue, to judge programs and channels.

## 2. Technical details

The authors combine a large observational dataset of real customer behavior with a smaller experimental dataset from a different population. Identification rests on the assumption that the conditional relative treatment effect of receiving a gift card on the decision to purchase is invariant across the two populations. The paper is 80 pages with 9 figures and 13 tables; details beyond the abstract were not read.

## 3. Impact — potential & realized

Realized (Airbnb application, per the abstract): treatment-effect heterogeneity is meaningful. Third-party distribution channels are more incremental than direct channels, and customers identified as self-gifters show stronger incremental effects than the general population. Specific dollar figures were not seen.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A good applied template for the common situation where experiments are small or off-population and observational data is rich but confounded by censored treatment.

A good applied template for the common situation where experiments are small or off-population and observational data is rich but confounded by censored treatment. The whole result hinges on the transportability assumption, which deserves scrutiny in any reuse. Authors include Johari and Syrgkanis, strong signal on rigor.

### Similar / related work

- [**Accelerating A/B-Tests with Counterfactual Estimation: Reducing Variance through Policy Overlap**](2026-10-01-arxiv-policy-overlap-accelerating-ab-tests.md) (in this bank) — leveraging extra structure/data to sharpen experiment-based estimates
- [**Debiased/Double Machine Learning (Chernozhukov et al.)**](https://arxiv.org/abs/1608.00060) — the semiparametric toolkit underlying much causal data fusion

### Jargon buster

- **Data fusion** — Combining datasets with different strengths (e.g., big observational + small randomized) to identify an effect neither identifies alone.
- **Incrementality** — The extra outcome caused by a program, versus what would have happened anyway.
- **Transportability / invariance** — The assumption that an effect (or a relative effect) learned in one population carries over to another.
- **Censored treatment** — Treatment status is only observed under some conditions, here when a purchase occurs.
