---
id: etsy-variance-reduction-pre-and-in-experiment-data
title: "Variance reduction combining pre-experiment and in-experiment data"
source: "CLeaR 2026 / PMLR 323 (Zhexiao Lin, UC Berkeley; Pablo Crespo, Etsy)"
url: "https://proceedings.mlr.press/v323/lin26a.html"
published: "2026"
added: "2026-10-08"
category: experimentation-causal
tags: [cuped, cupac, variance-reduction, post-treatment-covariates, regression-adjustment, etsy]
novelty: 4
sourced_via: "full-text fetch"
---

# Variance reduction combining pre-experiment and in-experiment data

**Source:** [CLeaR 2026 / PMLR 323 (Zhexiao Lin, UC Berkeley; Pablo Crespo, Etsy)](https://proceedings.mlr.press/v323/lin26a.html) · Published 2026 · Added 2026-10-08
**Category:** experimentation-causal · **Tags:** `cuped`, `cupac`, `variance-reduction`, `post-treatment-covariates`, `regression-adjustment`, `etsy`

## TL;DR

CUPED/CUPAC only use pre-experiment data. Lin & Crespo add a second-stage linear adjustment on a vetted set of post-treatment covariates that are balanced across arms, keeping the estimator consistent and asymptotically normal, and report additional variance reduction over Etsy's CUPAC pipeline in 29 experiments using only 23 such covariates.

## 1. Business context

Online A/B tests are limited by sensitivity at fixed sample size, and more traffic is often impractical. Regression adjustment (CUPED, CUPAC) cuts variance, but its gain depends on how well pre-experiment data predicts in-experiment outcomes. Pre-period history is weak for new users and for outcomes that depend on current-session behaviour. Industry practice generally excludes in-experiment (post-treatment) variables out of fear of post-treatment bias, even though they are often much more predictive.

## 2. Technical details

Potential-outcomes setup with Bernoulli assignment. Stage one is unchanged CUPAC: a prediction f(X) from pre-treatment covariates (Etsy: a single LightGBM model on 117 pre-treatment covariates, trained on pooled data from all experiments). Stage two adds a linear adjustment on selected post-treatment covariates Z. The key condition is mean equivalence: E[Z|W=1]=E[Z|W=0] (the covariates are not moved by treatment on average), which is weaker than full independence and, unlike surrogacy or principal ignorability, is testable. The authors derive asymptotic normality and consistent variance estimators. Covariate selection uses a two-sample test of each candidate across arms (with Holm/Bonferroni for family-wise control, or TOST equivalence tests when huge samples make trivial differences significant). In the Etsy study, candidates were sparse count variables (e.g. product-view-type activity as discussed in the paper's motivation); after dropping very sparse ones, a Mann-Whitney U test per experiment was combined across experiments via Fisher's method, leaving 23 post-treatment covariates; no formal FWER correction was applied, which the authors call conservative in practice.

## 3. Impact — potential & realized

Realized: on 29 Etsy experiments run over one month (primary metric: conversion rate), the paper reports the gain in predictive accuracy (difference in sqrt(R^2) over CUPAC) ranging from 0.02 to above 0.14, and a further variance reduction over CUPAC shown per experiment, with comparable or greater reduction than CUPAC despite using 23 versus 117 covariates. Exact aggregate percentages are shown only in a figure and not quoted here. Potential: in-experiment covariates are available even for brand-new users, so the approach fits platforms running thousands of parallel experiments; the authors suggest ML-driven discovery of more safe covariates as future work. Caveat: validity rests on the mean-equivalence condition holding for the chosen covariates, so it needs ongoing diagnostics for interventions that could shift navigation behaviour.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A practical, testable way to reopen a door the field had mostly shut.

The novelty is not the regression (adding covariates is old) but the discipline: a testable, platform-level screen that separates 'post-treatment but balanced' variables from mediators, avoiding the untestable assumptions of surrogate/principal-stratification approaches. Platform teams with CUPAC pipelines are the likely copiers; the risk to watch is a treatment that quietly shifts a screened covariate in a later experiment.

### Similar / related work

- [**Ensuring Trustworthy Online A/B Testing: Addressing Five Key Questions on CUPED**](2026-10-02-arxiv-cuped-five-questions-bytedance.md) (in this bank) — the pre-experiment CUPED baseline this paper extends
- [**CUPED on Steroids: Multivariate Covariate Adjustment for Switchback Experiments**](2026-09-29-arxiv-cuped-on-steroids-switchback.md) (in this bank) — covariate adjustment in another design setting
- [**Variance reduction below the randomization grain (Instacart)**](2026-09-30-instacart-variance-reduction-below-randomization-grain.md) (in this bank) — another industry route to more sensitive tests

### Jargon buster

- **CUPED / CUPAC** — Regression adjustments that use pre-experiment data (CUPAC uses an ML prediction) to shrink the variance of the treatment-effect estimate without adding bias.
- **Post-treatment covariate** — A variable measured after assignment. If treatment changes it (a mediator), adjusting for it biases the effect; if it is balanced across arms it can safely sharpen the estimate.
- **Mean equivalence** — The condition that a covariate has the same mean in treatment and control, which the paper tests rather than assumes.
