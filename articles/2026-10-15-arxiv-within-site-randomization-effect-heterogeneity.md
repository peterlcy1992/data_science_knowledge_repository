---
id: arxiv-within-site-randomization-effect-heterogeneity
title: "Identifying and Measuring Treatment-Effect Heterogeneity across Sites through Within-Site Randomization"
source: "arXiv stat.ME (Hoshino)"
url: "https://arxiv.org/abs/2610.15531"
published: "2026-10"
added: "2026-10-15"
category: experimentation-causal
tags: [cluster-randomized, site-heterogeneity, variance-components, experiment-design]
novelty: 3
sourced_via: "web search"
---

# Identifying and Measuring Treatment-Effect Heterogeneity across Sites through Within-Site Randomization

**Source:** [arXiv stat.ME (Hoshino)](https://arxiv.org/abs/2610.15531) · Published 2026-10 · Added 2026-10-15
**Category:** Experimentation & Causal Inference · **Tags:** `cluster-randomized`, `site-heterogeneity`, `variance-components`, `experiment-design`

## TL;DR

Parallel cluster-randomized designs can estimate how effects vary with site characteristics but cannot identify the residual, unexplained heterogeneity across sites. Randomizing participants within selected sites supplies the missing same-site cross-arm information, enabling unbiased moment estimators and an optimized choice of which sites to pair.

## 1. Business context

Multi-site experiments (clinics, villages, and by analogy markets or stores) are used to decide where an intervention works. A standard parallel cluster design gives mean effects by observed site traits, but a decision-maker also wants to know how much site-to-site variation remains after those traits, and how accurate any site-level effect prediction is. Without that, targeting rules for rollout rest on an unmeasured error term.

## 2. Technical details

The author randomizes participants within a subset of sites (paired sites with both arms observed) alongside the usual site-level design. Under randomized site selection and compatible participant reference distributions and intervention versions, the paper gives conditions under which quadratic targets (residual cross-site variance of effects, absolute prediction error of site-effect predictions) are identified, allowing unrestricted joint distributions of site response means. It proposes unbiased moment estimators from finite independent participant samples with exact covariances, proves consistency as the number of informative paired sites grows with fixed within-site sample sizes, and optimizes paired-site selection and unequal cell sizes given corrected risk variance, pilot error and cost.

## 3. Impact — potential & realized

Reported (retrospective data exercises, not new field trials): in an information-deletion experiment on the International Stroke Trial, pilot-informed allocation cut the conditional variance of reconstructing the full-information corrected-risk estimate by 34.3% versus uniform allocation at equal expected cost. In a 40-village Honduras dataset with a fixed explanatory basis, the correction lowered estimated residual variation from 0.04081 to 0.00282 (squared log-consumption units); the author attributes the uncorrected figure to participant sampling noise inflating residual variance. Potential: a principled design for deciding how much of a rollout effect is predictable from site traits.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a solid design-and-identification result for a real gap; narrow audience and abstract-level read only.

A useful reminder that naive between-site variance of estimated effects mixes true heterogeneity with sampling noise, and that the design (not just the estimator) determines whether the residual is identifiable. Directly relevant to market- or store-level experiments where teams want to know how targetable effects are. Caveat: abstract-level read only; the empirical evidence is reconstructions on existing datasets and I could not check regularity conditions or the simulations.

### Similar / related work

- [**Shared-Donor Inference for Fixed-Set Heterogeneity in Synthetic Difference-in-Differences**](2026-10-14-arxiv-shared-donor-inference-synthetic-did.md) (in this bank) — same author; inference for heterogeneity across many units
- [**On the Benefit of Blocking for Online Experiments with Skewed Data**](2026-10-09-arxiv-blocking-online-experiments-skewed-data.md) (in this bank) — design-side variance reduction in experiments

### Jargon buster

- **Cluster-randomized trial** — An experiment that assigns whole groups (sites, villages, markets) to arms rather than individuals.
- **Residual heterogeneity** — Variation in effects across sites that remains after accounting for observed site characteristics.
- **Quadratic target** — A quantity like a variance, which depends on squared effects rather than a simple mean.
