---
id: arxiv-long-term-quantile-treatment-effects-combined-data
title: "Long-Term Quantile Treatment Effects with Combined Experimental and Observational Data"
source: "Xiamen / Shandong / Vanderbilt / SMU (arXiv econ.EM)"
url: "https://arxiv.org/abs/2611.22984"
published: "2026-11"
added: "2026-11-18"
category: experimentation-causal
tags: [long-term-effects, quantile-treatment-effects, data-combination, latent-unconfoundedness, double-machine-learning, efficient-influence-function, multiplier-bootstrap, uniform-inference]
novelty: 3
sourced_via: "full-text fetch"
---

# Long-Term Quantile Treatment Effects with Combined Experimental and Observational Data

**Source:** [Xiamen / Shandong / Vanderbilt / SMU (arXiv econ.EM)](https://arxiv.org/abs/2611.22984) · Published 2026-11 · Added 2026-11-18
**Category:** Experimentation & Causal Inference · **Tags:** `long-term-effects`, `quantile-treatment-effects`, `data-combination`, `latent-unconfoundedness`, `double-machine-learning`, `efficient-influence-function`, `multiplier-bootstrap`, `uniform-inference`

## TL;DR

Extends the "combine a short-term experiment with long-term observational data" literature from average effects to the whole distribution: identification, a semiparametrically efficient estimator, and simultaneous confidence bands for the long-term quantile treatment effect (LTQTE) curve under Athey, Chetty & Imbens' latent unconfoundedness framework. Simulations show the combined-data estimator covers at nominal rates while an observational-only QTE badly undercovers.

## 1. Business context

Experiments give clean assignment but rarely run long enough to see long-term outcomes (attrition, cost); observational data have long follow-up but confounded treatment. Recent work (Athey, Chetty & Imbens 2025; Athey, Chetty, Imbens & Kang 2025; Chen & Ritzwoller 2023) combines the two but focuses on *average* long-term effects. When a decision depends on distributional impact — e.g. does a product change help heavy users and hurt light ones over a year — quantile effects are the natural target. This is a methods paper; there is no empirical application.

## 2. Technical details

- **Data structure.** An experimental sample (G=0) observes short-term outcome S, treatment W and covariates X; an observational sample (G=1) also observes the long-term outcome Y. The target is the LTQTE in the observational population at quantile τ.
- **Assumptions (adopted from the literature).** Experimental validity; external validity (same conditional potential-outcome distributions across samples); **latent unconfoundedness** — the short-term *potential* outcome S(w) summarises confounding in the observational sample; overlap; plus smoothness/density conditions for quantiles. Unlike statistical surrogacy, LU does not require short-term outcomes to be sufficient surrogates, and lets treatment affect Y through channels S doesn't capture. The authors note these assumptions "can be demanding".
- **Identification and efficiency.** IPW moment conditions identify the potential-outcome quantiles; the paper derives their efficient influence functions (EIFs), which are Neyman-orthogonal and doubly robust (consistent if either propensity-type or outcome-regression nuisances are correct).
- **Estimation.** Standard DML for quantiles would need a nonparametric quantile-density estimate. Instead they adapt the two-step gradient approach of Jiang, Phillips, Tao & Zhang (2023): evaluate nuisances at a consistent preliminary quantile, giving a convex score and closed-form estimators in both original and bootstrap samples; DML2 cross-fitting. Asymptotic normality and attainment of the efficiency bound are shown; primitive conditions are verified for indicator-response Lasso.
- **Uniform inference.** A multiplier bootstrap gives simultaneous confidence bands over a continuum of quantile indices.

## 3. Impact — potential & realized

**Measured (simulations, n=500, 1,000 replications, 5-fold CV Lasso nuisances, propensities trimmed to [0.05, 0.95]):** pointwise 95% coverage of the combined-data estimator is 0.926–0.957 across τ ∈ {0.1, …, 0.9} and implementations, versus 0.793–0.903 for the observational-only QTE. Over an 81-point quantile grid, the bootstrap critical value gives uniform coverage of 0.957 (full sample), 0.963 (K=2) and 0.976 (K=3) — slightly conservative — whereas using 1.96 gives 0.490–0.523; the observational-only estimator reaches only 0.494–0.528 even with the bootstrap critical value, because its bias isn't fixed by a wider band.

**Potential:** distributional long-term effect estimates (with honest simultaneous bands) for settings where a short experiment and a long observational panel are both available.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A careful, expected extension

The contribution is the quantile counterpart of Chen & Ritzwoller's efficient average-effect estimator under latent unconfoundedness, with a practical trick (avoiding quantile-density estimation) and uniform bands. Solid econometrics, but simulation-only and reliant on strong assumptions — especially that experiment and observational populations share conditional potential-outcome laws. For product teams the relevance is conceptual: if you already combine short experiments with long observational data for averages, this shows how to ask "who gains, at which quantile" with valid simultaneous inference.

### Similar / related work

- [**Many Hands Make Light Work: Long-Term Effect Inference for the Experiment Reservoir**](2026-10-28-arxiv-experiment-reservoir-surrogate-long-term-effects.md) (in this bank) — long-term effects from many short experiments via surrogates.
- [**Reward Innovation for Long-Term Member Satisfaction**](2026-09-12-netflix-reward-innovation-long-term-satisfaction.md) (in this bank) — an industry take on optimising toward long-term outcomes from short-term signals.
- [**Estimating Treatment Effects using Multiple Surrogates: The Role of the Surrogate Score and the Surrogate Index**](https://arxiv.org/abs/1603.09326) (Athey, Chetty, Imbens & Kang) — the statistical-surrogacy approach this paper contrasts with latent unconfoundedness.

### Jargon buster

- **Quantile treatment effect (QTE)** — the difference between the τ-th quantile of outcomes with and without treatment, e.g. the effect on the median or 90th percentile.
- **Latent unconfoundedness** — the assumption that, given covariates, the short-term potential outcome captures everything that drives selection into treatment in the observational data.
- **Efficient influence function** — the per-observation contribution that defines the lowest-variance regular estimator; using it yields orthogonal, doubly robust estimating equations.
- **Uniform (simultaneous) confidence band** — a band that covers the whole curve at once with 95% probability, wider than pointwise intervals.
