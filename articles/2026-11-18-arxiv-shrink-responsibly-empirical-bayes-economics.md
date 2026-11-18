---
id: arxiv-shrink-responsibly-empirical-bayes-economics
title: "Shrink Responsibly: Empirical Bayes in Economics"
source: "Hull (Brown) & Kolesár (Princeton) (arXiv econ.EM)"
url: "https://arxiv.org/abs/2611.21230"
published: "2026-11"
added: "2026-11-18"
category: statistical-modeling
tags: [empirical-bayes, shrinkage, value-added, compound-decisions, npmle, fixed-effects, ranking, review]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "catalog backlog (arXiv econ.EM scan)"
---

# Shrink Responsibly: Empirical Bayes in Economics

**Source:** [Hull (Brown) & Kolesár (Princeton) (arXiv econ.EM)](https://arxiv.org/abs/2611.21230) · Published 2026-11 · Added 2026-11-18
**Category:** Statistical Modeling · **Tags:** `empirical-bayes`, `shrinkage`, `value-added`, `compound-decisions`, `npmle`, `fixed-effects`, `ranking`, `review`

## TL;DR

A practitioner-oriented review of empirical Bayes (eB) for unit-level causal effects — teachers, schools, hospitals, neighbourhoods — organised around the OLS fixed-effects regression that produces the noisy estimates. Classic normal-normal shrinkage improves compound decisions (estimating all units' effects, picking top or bottom performers) even when its parametric assumptions fail, provided outliers don't have larger standard errors; but low-dimensional summaries (the variance of effects, regressions of effects on characteristics) should be estimated directly rather than from shrunk estimates. Illustrated with Charlotte-Mecklenburg school value-added.

## 1. Business context

Policymakers publish unit-level causal measures for high-stakes decisions (the paper notes New York City posts eB school value-added on its School Performance Dashboard). OLS fixed-effect estimates are unbiased under selection-on-observables but noisy because each unit's effect rests on a small effective sample: is a low estimate an underperformer or a bad draw? The same question arises in industry whenever a DS ranks stores, sellers, campaigns, creatives or experiment arms by noisy per-unit effects.

## 2. Technical details

- **Setup.** Y_i = D_i′θ + W_i′β + ε_i with J treatment dummies (or exposures) and controls; OLS via Frisch–Waugh–Lovell. Running example: Deming (2014) public replication data on 36,262 elementary and middle school students in Charlotte-Mecklenburg Schools (CMS).
- **Two-step logic.** Use known estimation noise (standard errors) to estimate the distribution of true effects, then use it for compound decisions — typically shrinking each estimate toward the mean, more so when its standard error is large.
- **Robustness of linear shrinkage.** Normal-normal shrinkage remains a good approach when normality fails and even for a frequentist who treats effects as fixed, for a broad class of compound decision problems (estimating all effects, classifying high/low performers), so long as precision doesn't depend on the effect (no "outliers have larger SEs").
- **Extensions.** Precision dependence handled with CLOSE (conditional location-scale) eB; nonparametric priors via NPMLE (grid of 1,601 points; CLOSE-NPMLE for middle schools).
- **When not to shrink.** For the variance of true effects, how well effects predict long-run outcomes, regressions of effects on unit characteristics, or a single unit's effect, estimate directly from microdata — this needs fewer assumptions, can account for noise in standard errors (e.g. Kline et al. 2020-style corrections), and yields standard errors. Robust procedures are also reviewed for testing the exogeneity of value-added and for ranking. Some direct microdata procedures and SE formulas appear to be novel, the authors say.

## 3. Impact — potential & realized

**Empirical illustration (CMS):** conventional value-added models yield highly variable school estimates, and a significant share of the variation remains after eB adjustment; shrinkage matters more for elementary schools, where estimates are noisier. Middle-school low performers are estimated with more noise (positive precision dependence), so the robustness condition appears to hold for elementary but not middle schools; accounting for it, the average prior SD for middle schools falls to around 0.090–0.095, while for elementary schools it stays similar at 0.108. Nonparametric (NPMLE) and Gaussian posteriors correlate above 0.99 for both levels — minimal gains from nonparametric methods here. Popularity measures (e.g. share ranking a school first) are mostly uncorrelated with value-added, selectivity measures strongly predict it, attending a high value-added elementary school predicts substantially higher later test scores, and lottery-based tests following Deming (2014) find no evidence of forecast bias in elementary or middle school and no evidence of school-level bias in middle school.

**Potential:** a clear decision rule for when shrinkage helps and when it quietly biases downstream analyses.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A review, but a sharply argued one

Mostly a synthesis (the authors point to Efron, Koenker & Gu and Walters for broader coverage), yet its organising idea — tie eB back to the regression that generated the estimates, and separate "decisions about units" from "summaries of the distribution" — is exactly the guidance analytics teams lack. The most actionable warning: don't regress shrunk estimates on covariates or compute their variance and call it the truth. Directly transferable to seller/store/creative leaderboards and multi-arm experiment readouts.

### Similar / related work

- [**SOTA or Luck? The Winner's Curse in LLM Leaderboards**](2026-11-18-arxiv-sota-or-luck-winners-curse-llm-leaderboards.md) (in this bank) — corrects selection bias of ranked noisy scores by bootstrap instead of shrinkage.
- [**Large-scale inference: empirical Bayes methods for estimation, testing, and prediction**](https://doi.org/10.1017/CBO9780511761362) (Efron, 2010) — the statistical monograph the review builds on.
- Chetty, Friedman & Rockoff (2014) teacher value-added — the canonical shrink-then-decide policy application discussed throughout.

### Jargon buster

- **Empirical Bayes** — estimate the prior (distribution of true effects) from the data itself, then compute each unit's posterior.
- **Compound decision** — many parallel decisions (one per unit) judged by their combined performance, where pooling information across units helps.
- **Value-added model (VAM)** — a regression estimating each teacher's or school's causal contribution to outcomes, controlling for prior achievement.
- **NPMLE** — nonparametric maximum likelihood estimate of the prior distribution, with no shape assumed.
