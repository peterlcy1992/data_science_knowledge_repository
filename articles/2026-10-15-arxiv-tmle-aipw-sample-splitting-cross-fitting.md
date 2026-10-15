---
id: arxiv-tmle-aipw-sample-splitting-cross-fitting
title: "When Sample-Splitting Choices Matter in TMLE and AIPW: Cross-Fitting, Targeting, and Repetition"
source: "arXiv stat.ME (Karim & Fu)"
url: "https://arxiv.org/abs/2610.16192"
published: "2026-10"
added: "2026-10-15"
category: statistical-modeling
tags: [TMLE, AIPW, doubly-robust, cross-fitting, simulation-study]
novelty: 3
sourced_via: "web search"
---

# When Sample-Splitting Choices Matter in TMLE and AIPW: Cross-Fitting, Targeting, and Repetition

**Source:** [arXiv stat.ME (Karim & Fu)](https://arxiv.org/abs/2610.16192) · Published 2026-10 · Added 2026-10-15
**Category:** Statistical Modeling · **Tags:** `TMLE`, `AIPW`, `doubly-robust`, `cross-fitting`, `simulation-study`

## TL;DR

A known-truth simulation study of eight TMLE/AIPW variants with machine-learning nuisance models shows that fitting the propensity model in-sample with a flexible learner can destroy confidence-interval coverage, while cross-fitting both nuisance models restores it. Under near-positivity violations all estimators undercover, with AIPW doing better than TMLE with an unweighted fluctuation.

## 1. Business context

Doubly robust estimators (AIPW, TMLE) with ML nuisance models are the default for observational causal effect estimation, including analyses of launches that were never randomized. Practitioners face undocumented choices: cross-fit or not, pool or split the targeting step, repeat the splits. This paper asks which choices actually change the validity of intervals.

## 2. Technical details

Variants differ in (1) where nuisance models are fit (in-sample vs cross-fitting), (2) targeting (pooled vs fold-specific bias correction), and (3) whether sample splits are repeated. Eight headline estimators share the same learner library, inner folds and truncation bound. Simulations use a binary-outcome average treatment effect with known truth; coverage is judged against a prespecified two-percentage-point margin. Two real-data analyses illustrate sensitivity; code is on GitHub and a 30-page supplement is provided.

## 3. Impact — potential & realized

Reported results: with a low-complexity library and good overlap (n = 3000), nearly all estimators covered at about 0.93 (a half-sample baseline excepted). With random forests in the primary design, in-sample propensity fitting undercovered severely (0.12-0.48) while cross-fitting both nuisance models gave 0.91-1.00 (two estimators overcovering). Near positivity violations, every AIPW estimator beat every TMLE using the unweighted fluctuation (about 0.91 vs 0.66-0.81) yet all undercovered; looser truncation widened the gap. Under extreme weights pooled targeting was 1.7-1.8x as dispersed as fold-specific. Repeated splits reduced partition dependence but made several intervals conservative. Recommendation: cross-fit both nuisance models when empirical-process conditions cannot be justified, and check sensitivity to truncation and AIPW vs TMLE under poor overlap.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — careful, useful empirical guidance on implementation choices rather than a new estimator.

Practical, checklist-style guidance a working analyst can apply directly: cross-fit both nuisance models, and report truncation sensitivity. The simulation design is one binary-outcome ATE setup, so generalisation to continuous outcomes or other DGPs is untested here. I only saw the abstract-level summary, not the tables.

### Similar / related work

- [**Bayesian Causal Forests for Zero-Inflated Continuous Outcomes**](https://arxiv.org/abs/2610.18889) — other recent causal-estimation methods paper
- [**Double/debiased machine learning (Chernozhukov et al.)**](https://arxiv.org/abs/1608.00060) — the cross-fitting framework these estimators build on

### Jargon buster

- **Cross-fitting** — Fitting nuisance models on one part of the data and evaluating them on another, to avoid overfitting bias.
- **Positivity / overlap** — Every unit must have a non-trivial probability of each treatment; near violations produce extreme weights.
- **TMLE** — Targeted maximum likelihood estimation: a doubly robust estimator that updates an initial outcome model toward the target parameter.
