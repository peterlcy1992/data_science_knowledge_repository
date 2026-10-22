---
id: arxiv-bcf-zero-inflated-continuous-outcomes
title: "Bayesian Causal Forests for Zero-Inflated Continuous Outcomes"
source: "arXiv stat.ML (Souto, Wang & Shuryak)"
url: "https://arxiv.org/abs/2610.18889"
published: "2026-10"
added: "2026-10-16"
category: statistical-modeling
tags: [bayesian-causal-forests, hte, zero-inflated, two-part-model]
novelty: 3
sourced_via: "web search"
---

# Bayesian Causal Forests for Zero-Inflated Continuous Outcomes

**Source:** [arXiv stat.ML (Souto, Wang & Shuryak)](https://arxiv.org/abs/2610.18889) · Published 2026-10 · Added 2026-10-16
**Category:** statistical-modeling · **Tags:** `bayesian-causal-forests`, `hte`, `zero-inflated`, `two-part-model`

## TL;DR

ZIC-BCF-Smear estimates heterogeneous treatment effects on outcomes with a point mass at zero plus a skewed positive part (think spend, days of events). It fits a probit BCF for 'any outcome at all' and a Gaussian BCF for the positive part, then maps back to the original scale with Duan's smearing.

## 1. Business context

Many product and clinical outcomes are semicontinuous: a large share of exact zeros (about 25% of patients in the application) and a skewed positive tail. Typical HTE tooling either ignores the zero mass, leans on fragile parametric assumptions, or is costly and noisy because of data augmentation. This matters for any analysis of revenue per user, sessions, or usage days where most units record nothing.

## 2. Technical details

Decoupled two-part estimator. (1) A Probit Bayesian Causal Forest on the full sample models participation (non-zero vs zero). (2) A Gaussian BCF on the active subpopulation models positive intensity. Subpopulation Propensity Adjustment addresses regularization-induced confounding inside the active group. Duan's smearing retransforms predictions to the outcome scale nonparametrically, with no parametric scale factor. Full text not read; details are from the abstract.

## 3. Impact — potential & realized

Realized (as reported): in simulations it performs about as well as correctly specified parametric models without needing their assumptions, and stays stable and calibrated on nonlinear data where competitors diverge or over-cover (no specific metrics on the page I read). Applied to individual-participant data from the SPECTRUM phase III head-and-neck trial (panitumumab + chemotherapy vs control, days with severe toxicity), the estimated effect is roughly +10 days per patient, concentrated in the positive-intensity component. Potential: the same recipe transfers to spend/usage outcomes in product experiments.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty 3/5 - a sensible, well-motivated composition of known pieces (BCF, two-part models, smearing); value is in the practical fit for zero-heavy outcomes.

Mostly a careful recombination: two-part models, BCF and smearing all exist. What is useful is the explicit handling of regularization bias in the active subgroup. Caveat: abstract-level read, and the trial application uses differential treatment duration, so the clinical effect is not a clean causal contrast for product use.

### Similar / related work

- [Bayesian Causal Forests](https://arxiv.org/abs/1706.09523) — the BCF base model with propensity-aware regularization
- [**Variance reduction combining pre-experiment and in-experiment data**](2026-10-08-etsy-variance-reduction-pre-and-in-experiment-data.md) (in this bank) — another approach to noisy, skewed experiment outcomes

### Jargon buster

- **Zero-inflated / semicontinuous outcome** — An outcome with a spike at exactly zero and a continuous positive distribution, e.g. spend per user.
- **Duan's smearing** — A nonparametric way to back-transform predictions from a modeled scale to the original scale using the empirical residual distribution.
- **Regularization-induced confounding** — Bias that appears when a shrinkage prior on the outcome model absorbs part of the confounding signal; BCF counters it with a propensity-score covariate.
