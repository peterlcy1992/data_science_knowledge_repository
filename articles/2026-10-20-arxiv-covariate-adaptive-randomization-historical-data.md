---
id: arxiv-covariate-adaptive-randomization-historical-data
title: "Covariate-adaptive randomization using historical data and bootstrap-based inference"
source: "arXiv stat.ME (Seya, Taguri, Togo & Kamatani)"
url: "https://arxiv.org/abs/2610.26254"
published: "2026-10"
added: "2026-10-20"
category: experimentation-causal
tags: [covariate-adaptive-randomization, prognostic-score, bootstrap, experiment-design, variance-reduction]
novelty: 3
sourced_via: "web search"
---

# Covariate-adaptive randomization using historical data and bootstrap-based inference

**Source:** [arXiv stat.ME (Seya, Taguri, Togo & Kamatani)](https://arxiv.org/abs/2610.26254) · Published 2026-10 · Added 2026-10-20
**Category:** experimentation-causal · **Tags:** `covariate-adaptive-randomization`, `prognostic-score`, `bootstrap`, `experiment-design`, `variance-reduction`

## TL;DR

Balances treatment arms on a prognostic score learned from historical data rather than on raw covariates, and pairs it with a design-mirroring bootstrap for inference.

## 1. Business context

Balancing many covariates at assignment can hurt finite-sample precision, and existing optimal designs assume the outcome is linear in the balanced features. Inference after adaptive assignment is also awkward because assignments are dependent.

## 2. Technical details

Three covariate-adaptive randomization methods each build the imbalance measure on a prognostic score (a one-dimensional summary learned from individual-level historical data that weights covariates by their outcome association). Inference uses unequal-probability resampling that mirrors the design, so treatment is not reassigned inside each bootstrap sample, which sidesteps trouble with continuous covariates. The arXiv comment says theoretical results are still to be added.

## 3. Impact — potential & realized

Reported qualitatively: in simulations and a clazosentan trial application, the methods reduced prognostic imbalance and improved precision versus existing designs, and the bootstrap tracked the design-induced distribution. No numbers were available on the page; behavior when historical data differ from the trial population is not described.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Moving the CUPED idea from analysis time to assignment time is sensible and useful, but it is incremental, currently lacks theory, and relies on historical data being representative.

Moving the CUPED idea from analysis time to assignment time is sensible and useful, but it is incremental, currently lacks theory, and relies on historical data being representative.

### Similar / related work

- [**On the Benefit of Blocking for Online Experiments with Skewed Data**](2026-10-09-arxiv-blocking-online-experiments-skewed-data.md) (in this bank) — blocking as another assignment-time precision lever
- [**Variance reduction combining pre-experiment and in-experiment data**](2026-10-08-etsy-variance-reduction-pre-and-in-experiment-data.md) (in this bank) — the analysis-time counterpart (CUPED/CUPAC) of using prognostic information
- [**Unlocking 66% Faster Experiments with Covariate Adjustment**](2026-10-12-instacart-covariate-adjustment-power-analysis-clustered-data.md) (in this bank) — regression adjustment for precision

### Jargon buster

- **Prognostic score** — A model-predicted outcome (e.g. from historical data) used as a single covariate summarising how outcome-relevant the covariates are.
- **Covariate-adaptive randomization** — Assigning treatment sequentially to keep arms balanced on chosen covariates instead of purely at random.
- **Design-based bootstrap** — Resampling that reproduces how treatment was actually assigned, so uncertainty reflects the design.
