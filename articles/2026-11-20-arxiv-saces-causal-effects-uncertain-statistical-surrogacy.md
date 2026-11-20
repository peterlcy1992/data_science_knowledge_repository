---
id: arxiv-saces-causal-effects-uncertain-statistical-surrogacy
title: "Causal Effect Estimation Under Uncertain Statistical Surrogacy"
source: "Fred Hutch / Penn / NC State / Brown (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.26289"
published: "2026-11"
added: "2026-11-20"
category: experimentation-causal
tags: [surrogate-outcomes, statistical-surrogacy, efficient-influence-function, missing-outcomes, estimator-selection, long-term-effects, aipw, post-selection-inference]
novelty: 3
sourced_via: "full-text fetch"
---

# Causal Effect Estimation Under Uncertain Statistical Surrogacy

**Source:** [Fred Hutch / Penn / NC State / Brown (arXiv stat.ME)](https://arxiv.org/abs/2611.26289) · Published 2026-11 · Added 2026-11-20
**Category:** Experimentation & Causal Inference · **Tags:** `surrogate-outcomes`, `statistical-surrogacy`, `efficient-influence-function`, `missing-outcomes`, `estimator-selection`, `long-term-effects`, `aipw`, `post-selection-inference`

## TL;DR

Imposing statistical surrogacy (the outcome is independent of treatment given the surrogate and covariates) can shrink standard errors a lot, but it biases the estimate when the condition fails. SACES keeps an unrestricted efficient estimator as a robust reference and uses an estimated-MSE criterion to pick among surrogate-assisted candidates or weighted blends. Its risk is no greater than the reference's, up to a vanishing remainder. In the ACTG 175 trial, imposing surrogacy halved the effect estimate. SACES put weight 0.08 on that estimator and landed near the unrestricted estimate.

## 1. Business context

Experiments often target outcomes that are slow, costly or partly missing, such as long-term retention or week-96 clinical endpoints. Early surrogates can help in two ways: as auxiliary information (always safe under the right estimator) or by imposing Prentice-style statistical surrogacy (more efficient, but biased if the surrogate misses part of the treatment's effect). With several candidate surrogates of uncertain validity, analysts usually commit to one specification on judgment. The paper characterizes when imposing surrogacy helps or hurts, and gives a data-driven way to decide.

## 2. Technical details

- **Setup.** Data (X, A, Q, Y), with Y either fully observed or missing at random. The estimand is the ATE. Statistical surrogacy is Y ⟂ A | X, Q.
- **Theory.** The paper derives the efficiency gain from imposing surrogacy and the asymptotic bias when it fails. In the unrestricted MAR model, extra post-treatment information is not always helpful. Variables predictive of the outcome can lower the efficiency bound, while variables predictive only of missingness can raise it.
- **Reference estimator.** Standard AIPW with full outcomes. With MAR outcomes, the Kallus–Mao estimator, which uses Q without imposing surrogacy.
- **SACES.** Builds on Rothenhäusler's (2024) reference-estimator selection framework. It selects among K surrogate-assisted candidates (surrogate subsets, or blends (1−w)·θ̂_std + w·θ̂_surr on a w-grid) by minimizing a modified estimated MSE. Inference uses a post-selection CI, not a Wald interval.
- **Simulations** (500 reps, n = 1,000). DGP I has three candidate surrogates with only Q1 valid: SACES beats AIPW, all-surrogate and bad-surrogate estimators on RMSE, approaches the oracle, and most often selects {Q1}. DGP II varies surrogacy violation δ: SACES downweights θ̂_surr as δ grows. Coverage has a 'U-shape', with undercoverage under moderate violations.

## 3. Impact — potential & realized

**Measured:**
- ACTG 175 (n = 2,139; outcome week-96 CD4, 37.3% missing; surrogate week-20 CD4): AIPW without Q gives 61.99 (SE 9.60); unrestricted Kallus–Mao gives 62.08 (SE 9.21).
- Imposing surrogacy gives 31.49 (SE 3.87), about half the estimate. The plug-in bias estimate of −31.24 matches the −30.59 gap, and an F-test finds residual treatment dependence (p = 0.006).
- SACES selects w = 0.08 and estimates 59.64, with post-selection 95% CI (43.58, 82.01).

**Potential:** A guardrail for surrogate-index and long-term-effect pipelines in product experimentation: use proxy metrics for precision only when the data support it, and fall back to the robust estimator automatically when they don't.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A principled 'don't trust your proxy metric blindly' estimator, with a vivid cautionary example

The ACTG example is the selling point. A surrogate that looks great (SE drops from 9.2 to 3.9) silently halves the effect. Every team that has shipped a surrogate index for long-term metrics should run this comparison: the unrestricted vs surrogacy-imposing estimate gap is a cheap diagnostic in itself.

SACES is an application of Rothenhäusler's selection framework rather than a new principle, hence 3/5. Undercoverage under moderate violations is the practical catch, and the surrogates must be fully observed.

### Similar / related work

- [**Many Hands Make Light Work: Long-Term Effect Inference for the Experiment Reservoir**](2026-10-28-arxiv-experiment-reservoir-surrogate-long-term-effects.md) (in this bank) — surrogate-based long-term effects across many experiments, where surrogacy validity is the same weak point.
- [**Long-Term Quantile Treatment Effects with Combined Experimental and Observational Data**](2026-11-18-arxiv-long-term-quantile-treatment-effects-combined-data.md) (in this bank) — long-term effects from short-term experiments plus observational data.
- [**Estimating Treatment Effects using Multiple Surrogates: The Role of the Surrogate Score and the Surrogate Index**](https://arxiv.org/abs/1603.09326) — Athey, Chetty, Imbens & Kang's surrogate index, which relies on a surrogacy assumption of this kind.
- [**On the role of surrogates in the efficient estimation of treatment effects with limited outcome data**](https://arxiv.org/abs/2003.12408) — Kallus & Mao, the unrestricted reference estimator SACES anchors to.

### Jargon buster

- **Statistical surrogacy** — the assumption that, once you know the surrogate and baseline covariates, treatment tells you nothing more about the final outcome.
- **Surrogate-assisted estimator** — an estimator that imposes surrogacy to borrow strength from the early metric; more precise if the assumption holds, biased if not.
- **Efficient influence function (EIF)** — the building block of the most precise regular estimator under a model; estimators built on it are robust to small nuisance errors.
- **Post-selection inference** — confidence intervals that account for the data having been used to choose the estimator.
