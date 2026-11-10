---
id: arxiv-average-vs-expected-causal-effects-under-interference
title: "Average versus Expected Causal Effects under Interference: Modeling Assumptions and Estimation Bottlenecks"
source: "arXiv stat.ME (Karwa, Airoldi, Rubin)"
url: "https://arxiv.org/abs/2611.12690"
published: "2026-11"
added: "2026-11-10"
category: experimentation-causal
tags: [interference, network-experiments, spillover, Horvitz-Thompson, graph-cluster-randomization, potential-outcomes]
novelty: 3
sourced_via: "full-text fetch"
---

# Average versus Expected Causal Effects under Interference: Modeling Assumptions and Estimation Bottlenecks

**Source:** [arXiv stat.ME (Karwa, Airoldi, Rubin)](https://arxiv.org/abs/2611.12690) · Published 2026-11 · Added 2026-11-10
**Category:** experimentation-causal · **Tags:** `interference`, `network-experiments`, `spillover`, `Horvitz-Thompson`, `graph-cluster-randomization`, `potential-outcomes`

## TL;DR

Under interference (one unit's outcome depends on others' assignments) the paper separates three modelling layers - interference neighborhoods, exposure mappings, outcome models - and two estimand classes: average causal effects (fixed contrasts) and expected causal effects (contrasts under an allocation policy). Variance bounds show graph-unaware designs can need sample sizes exponential in the interference degree for ACEs, whereas polynomial growth can suffice for design-aligned ECEs.

## 1. Business context

Marketplace, social and network A/B tests routinely violate no-interference. The paper argues the literature often conflates which units can affect whom, how exposures are summarised, what functional form is assumed, which estimand is targeted, and which design and estimator are used, making it hard to tell why methods differ. It supplies a common vocabulary to reason about that.

## 2. Technical details

The 'table of science' (finite-population potential outcomes) is the primitive object. Given an interference neighborhood and exposure mapping, potential outcomes admit a nonparametric decomposition into direct, spillover and treatment-spillover interaction components. ACEs (direct, total effects) contrast outcomes under fixed treatment-exposure conditions; ECEs (expected direct and indirect effects) contrast expectations under a specified allocation policy. The Horvitz-Thompson variance is bounded by three terms: a diagonal weight term, a term from overlapping interference neighborhoods, and a residual design-dependence term. Under neighborhood interference the authors construct graph-aware independent-set designs with variance bounds polynomial in the maximum degree for direct and total effects on every graph, versus graph cluster randomization, which can incur worst-case variance exponential in the degree.

## 3. Impact — potential & realized

Realized: theoretical bounds (upper and lower); I did not extract empirical results from the text. Potential: guidance on which estimand and design are feasible at a given network density, and a reason to prefer policy-level (ECE) estimands when degree is high.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A conceptual and bounds paper that organises the interference literature and sharpens when estimation is intrinsically hard; practical impact depends on adoption of the independent-set designs.

Useful mainly as a map: it tells you that asking for a fixed-allocation contrast (ACE) can be exponentially more expensive than asking for the effect of a policy you will actually deploy (ECE). Read it before choosing a cluster-randomized design for a network experiment.

### Similar / related work

- [**Selective randomization inference under interference**](2026-11-04-arxiv-selective-randomization-inference-interference-pretest.md) — in this bank: randomization inference with interference
- [**Power-Optimal Covariate Adjustment for Switchback Experiments**](2026-11-09-doordash-power-optimal-cupac-switchback-experiments.md) — in this bank: switchbacks as a design response to interference

### Jargon buster

- **Interference** — A unit's outcome depends on other units' treatment assignments, violating SUTVA.
- **Exposure mapping** — A function summarising the assignments around a unit into a low-dimensional exposure.
- **Horvitz-Thompson estimator** — An inverse-probability-weighted estimator that is design-unbiased given known assignment probabilities.
