---
id: arxiv-anytime-valid-clustered-linear-models
title: "Anytime-Valid Inference in Linear Models with Clustered Outcomes: Exact Multivariate Tests and Cluster-Robust Confidence Sequences"
source: "arXiv stat.ME (Lindon)"
url: "https://arxiv.org/abs/2610.25613"
published: "2026-10"
added: "2026-10-20"
category: experimentation-causal
tags: [anytime-valid, e-values, confidence-sequences, multivariate-outcomes, cluster-robust]
novelty: 4
sourced_via: "web search"
---

# Anytime-Valid Inference in Linear Models with Clustered Outcomes: Exact Multivariate Tests and Cluster-Robust Confidence Sequences

**Source:** [arXiv stat.ME (Lindon)](https://arxiv.org/abs/2610.25613) · Published 2026-10 · Added 2026-10-20
**Category:** experimentation-causal · **Tags:** `anytime-valid`, `e-values`, `confidence-sequences`, `multivariate-outcomes`, `cluster-robust`

## TL;DR

Extends anytime-valid sequential inference to units with several correlated outcomes and clustered data: exact Gaussian e-values and sequential Hotelling/MANOVA tests, plus an asymptotic cluster-robust e-process, giving simultaneous confidence sequences for a vector of average treatment effects.

## 1. Business context

Experiments usually track several metrics per user, and users are often clustered (markets, stores, sessions). Peeking at results is routine, yet most sequential tools handle one independent scalar outcome. This paper targets the joint multi-metric, clustered, continuously-monitored case.

## 2. Technical details

Parametric case: a multivariate linear model with unstructured error covariance, a right-Haar nuisance prior and a matrix-normal mixture alternative give a closed-form Bayes factor that is an exact e-value and test martingale at every sample size, yielding sequential Hotelling and MANOVA tests with exact confidence sequences. Clustered case: under a common within-cluster design the cluster-robust Wald statistic equals Hotelling's T-squared on per-cluster least-squares summaries (G-1 degrees of freedom). Nonparametric case: the sandwich statistic is an asymptotic e-process needing no Gaussian, common-design or linearity assumptions. Growth and expected-stopping-time results are given, including a growth-optimal fixed mixture precision under stronger regularity. Applied to randomized experiments, it produces joint tests, confidence ellipsoids and simultaneous confidence sequences for the average-treatment-effect vector using OLS and cluster-robust SEs. Explicit formulas were not read.

## 3. Impact — potential & realized

Reported: theoretical guarantees only; no numerical experiments appear on the abstract page. Potential: always-valid dashboards for multi-metric, clustered experiments that control error under peeking and across metrics at once.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Combining exact multivariate e-values with a cluster-robust asymptotic e-process is a practical gap-filler for experimentation platforms, though anytime-validity itself is established (this author has prior work on it).

Combining exact multivariate e-values with a cluster-robust asymptotic e-process is a practical gap-filler for experimentation platforms, though anytime-validity itself is established (this author has prior work on it). Theory-only and abstract-level read, so finite-sample behavior of the robust version and software availability are unknown.

### Similar / related work

- [**Design-Driven Inference for Online Experiments**](2026-10-07-arxiv-design-driven-inference-online-experiments.md) (in this bank) — another e-value / anytime-valid take on experiment design
- [**Neutral Is Not Free: Evaluating Downside Risk in Neutral Launches**](2026-10-09-arxiv-neutral-launches-expected-bayesian-loss.md) (in this bank) — multi-metric launch decisions under uncertainty
- [**Within-site randomization**](2026-10-15-arxiv-within-site-randomization-effect-heterogeneity.md) (in this bank) — clustered experiment design

### Jargon buster

- **E-value / test martingale** — A nonnegative evidence measure whose expectation is at most 1 under the null; because it stays valid however you stop, it supports peeking.
- **Confidence sequence** — A confidence interval that is valid simultaneously at all sample sizes.
- **Hotelling's T-squared** — The multivariate analogue of the t-test, testing a vector of means at once.
