---
id: arxiv-covariate-selection-doubly-robust-dml
title: "Covariate Selection for Doubly Robust Double/debiased Machine Learning Estimators for Causal Inference"
source: "arXiv (Kwon, Steiner)"
url: "https://arxiv.org/abs/2609.17238"
published: "2026-09"
added: "2026-10-01"
category: statistical-modeling
tags: [causal-inference, doubly-robust, covariate-selection, lasso, double-machine-learning]
novelty: 3
sourced_via: "web search"
---

# Covariate Selection for Doubly Robust Double/debiased Machine Learning Estimators for Causal Inference

**Source:** [arXiv (Kwon, Steiner)](https://arxiv.org/abs/2609.17238) · Published 2026-09 · Added 2026-10-01
**Category:** statistical-modeling · **Tags:** `causal-inference`, `doubly-robust`, `covariate-selection`, `lasso`, `double-machine-learning`

## TL;DR

Kwon and Steiner show that for doubly robust estimators, re-estimating both the propensity and outcome models on the union of covariates selected by either model reduces confounding bias more than selecting separately, and that post-Lasso beats plain Lasso.

## 1. Business context

Observational causal analyses increasingly use ML to pick adjustment variables, but the selected set from each nuisance model is often used only in that model, leaving residual confounding bias.

## 2. Technical details

The proposal: select covariates with the propensity-score ML model and the outcome ML model, take the union, and re-estimate both models with that union before the doubly robust (DR/DML) estimate. A simulation study compares this to separate selection and to non-ML DR estimators.

## 3. Impact — potential & realized

Simulation findings only: union selection consistently reduces confounding bias; ML does not uniformly outperform traditional DR estimation even under favourable conditions; post-Lasso reduces more bias than standard Lasso. No real-data application was reported in the summary reviewed.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Practical, narrow methodological tip backed by simulation only.

Useful rule of thumb for analysts running DML on observational product data, but simulation-only evidence means it should be sanity-checked on your own data generating assumptions.

### Similar / related work

- [**Introduction to Causal Inference Using Double Machine Learning**](2026-09-22-microsoft-double-machine-learning.md) — DML in practice (in this bank)

### Jargon buster

- **Doubly robust estimator** — Combines a propensity model and an outcome model; consistent if either is correct.
- **Post-Lasso** — Use Lasso to choose variables, then refit without shrinkage to reduce bias.
- **Nuisance model** — A model fitted only as an input to the causal estimate (propensity or outcome model).
