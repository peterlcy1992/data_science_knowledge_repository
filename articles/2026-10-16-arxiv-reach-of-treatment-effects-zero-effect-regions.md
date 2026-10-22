---
id: arxiv-reach-of-treatment-effects-zero-effect-regions
title: "The Reach of Treatment Effects: Randomization Inference for Zero-Effect Regions"
source: "arXiv stat.ME (Li & Zhang)"
url: "https://arxiv.org/abs/2610.20759"
published: "2026-10"
added: "2026-10-16"
category: experimentation-causal
tags: [randomization-inference, hte, subgroups, confidence-bound]
novelty: 3
sourced_via: "web search"
---

# The Reach of Treatment Effects: Randomization Inference for Zero-Effect Regions

**Source:** [arXiv stat.ME (Li & Zhang)](https://arxiv.org/abs/2610.20759) · Published 2026-10 · Added 2026-10-16
**Category:** experimentation-causal · **Tags:** `randomization-inference`, `hte`, `subgroups`, `confidence-bound`

## TL;DR

Instead of finding who benefits, this paper bounds how big a region of covariate space can have no effect. Local randomization tests over nearest-neighbour regions give a finite-sample valid upper confidence bound on the largest zero-effect region; a small bound means effects are broad.

## 1. Business context

Treatments often help some people and leave others unchanged. Conventional HTE work searches for responsive subgroups; this paper asks the complementary question of how far an effect reaches, which matters for rollout decisions and for claims such as 'works for everyone'.

## 2. Technical details

Efficient local randomization tests over nearest-neighbour regions test whether a candidate region has zero effect; these yield a finite-sample valid upper confidence bound on the size of the largest zero-effect region. Under a general outcome model the bound's size depends on the number of affected units, effect magnitudes and geometry of the zero-effect set. Measured as a sample fraction, the bound's excess over the truth shrinks at a minimax optimal rate up to a log factor. Paper is 57 pages; abstract-level read.

## 3. Impact — potential & realized

Realized (abstract): simulations assess coverage, power and compute cost; applications to voter turnout, an HIV clinical trial and AI-assisted writing data show large zero-effect regions can be ruled out. No numeric results are given in the abstract. Potential: a rigorous alternative to post-hoc subgroup hunting in A/B tests.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty 3/5 - a fresh, useful framing of heterogeneity (bounding null regions) with solid theory, but untested at A/B-platform scale.

The reframing is the contribution; it is a counterweight to subgroup fishing. Computation over nearest-neighbour regions may be heavy for large experiments.

### Similar / related work

- [**Identifying and Measuring Treatment-Effect Heterogeneity across Sites through Within-Site Randomization**](2026-10-15-arxiv-within-site-randomization-effect-heterogeneity.md) (in this bank) — another heterogeneity-measurement design
- [False Discovery Rate Controlled HTE Detection for Online Experiments](https://arxiv.org/abs/1808.04904) — detecting responsive cohorts with FDR control

### Jargon buster

- **Randomization inference** — Hypothesis tests whose validity comes from the random assignment itself, giving exact finite-sample guarantees without model assumptions.
- **Zero-effect region** — A set of covariate values where the treatment effect is exactly zero.
- **Minimax optimal rate** — The best convergence rate achievable in the worst case over a class of problems.
