---
id: arxiv-looking-forward-better-causal-comparisons-prognostic-scores
title: "Looking Forward to Constructing Better Causal Comparisons"
source: "arXiv econ.EM (Augusto Cerqua, Sapienza University of Rome)"
url: "https://arxiv.org/abs/2611.02061"
published: "2026-11"
added: "2026-11-12"
category: experimentation-causal
tags: [prognostic-scores, matching, entropy-balancing, difference-in-differences, TabPFN, observational-causal-inference, LaLonde-NSW]
novelty: 3
sourced_via: "full-text fetch"
---

# Looking Forward to Constructing Better Causal Comparisons

**Source:** [arXiv econ.EM (Augusto Cerqua, Sapienza University of Rome)](https://arxiv.org/abs/2611.02061) · Published 2026-11 · Added 2026-11-12
**Category:** experimentation-causal · **Tags:** `prognostic-scores`, `matching`, `entropy-balancing`, `difference-in-differences`, `TabPFN`, `observational-causal-inference`, `LaLonde-NSW`

## TL;DR

Instead of choosing control units by covariate balance or pre-trends, choose them by prognostic scores — predicted untreated outcomes (levels for matching, changes for DiD) — estimated with TabPFN 3.5, while still estimating effects from observed outcomes. An exact decomposition splits estimation error into score imbalance and forecast-error differences; on the NSW/CPS-1 benchmark, outcome-trained scores land closest to the experimental estimates, but purely historical scores do poorly.

## 1. Business context

Constructing a credible comparison group is the central problem of observational causal inference — in policy evaluation and equally in product launches that can't be randomized. Practitioners assess comparability through covariate balance or similar pre-treatment trends, yet identification depends on untreated outcomes *after* treatment, which neither diagnostic establishes (parallel pre-trends are neither necessary nor sufficient). The paper proposes a forward-looking criterion: compare units on what they were expected to do without treatment.

## 2. Technical details

**Scores.** Following Hansen (2008), a prognostic score is a prediction of the untreated outcome Y₁(0). The relevant score depends on the design: s^Level = m̂ for level comparisons (matching), s^DiD = m̂ − Y₀ for DiD. Scores are estimated either (a) from post-treatment outcomes of untreated units (the conventional route, with cross-fitting to avoid a control predicting itself) or (b) exclusively from pre-treatment history (learn the −1→0 transition, apply it at 0), which needs ≥2 pre-periods and stable relationships.

**Decomposition.** With Y₁(0) = m̂ + r, the level and DiD estimators satisfy τ̂ − τ_T = Δ_ω s + Δ_ω r exactly: score imbalance plus the difference in forecast errors between treated and weighted controls. Exact score balance removes the first term, but unbiasedness still needs comparable forecast errors — so neither predictive accuracy nor score balance alone guarantees identification. Common shocks cancel because forecasts choose controls while observed outcomes estimate effects.

**Implementation.** TabPFN 3.5 (four ensemble members, ≤2,048 context rows each) beat OLS and random forest out of sample on CPS-1 earnings, though RMSE gains over OLS were small (0.34% and 0.83%). Controls are selected by 1:1 nearest-neighbour matching with replacement or entropy balancing on the first two score moments, versus a replicated Dehejia–Wahba propensity score; all specifications were fixed before comparing to the benchmark.

## 3. Impact — potential & realized

**Realized (one benchmark).** NSW (185 treated men) vs 15,992 CPS-1 controls; experimental benchmarks $1,794.34 (levels) and $1,529.20 (DiD). Levels: NN matching on the outcome-trained level score gives $1,651.17; the propensity score $1,990.77; entropy balancing on the level score $1,422.98. DiD: entropy balancing on the outcome-trained *level* score gives $1,468.45, closest; the predicted-change score — the one aligned with DiD — is further off ($1,374.61 EB, $1,326.41 NN); propensity matching $1,919.48. Purely pre-treatment scores perform poorly (levels $1,135.40 NN, $684.51 EB; DiD $994.04 and $929.80), which the author attributes to using a one-year forecast as a proxy for a three-year horizon. Stronger pre-treatment covariate balance did not necessarily yield estimates closer to the benchmark.

**Potential.** The author suggests the approach could extend to RDD and IV; positioned as a proof of concept, not proof of superiority.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A useful reframing — pick controls on predicted untreated outcomes — with an exact error decomposition, but thin empirical support from a single benchmark.

The decomposition is the keeper: it makes explicit that a great forecaster can still give a biased effect if forecast errors differ between groups, which is a good antidote to 'just plug in a foundation model'. For product analysts doing geo or cohort comparisons, building controls on predicted counterfactual KPIs is natural (it's close to what synthetic control and imputation DiD do). But the evidence is one famous 1970s dataset where propensity matching also does fine, the 'aligned' DiD score underperformed, and TabPFN's predictive edge over OLS was well under 1% — so the foundation-model angle is not what drives the results.

### Similar / related work

- [**Does Predictive Performance Translate to Causal Performance? Evaluating tabular foundation models as nuisance learners for causal effect estimation**](2026-11-11-arxiv-tabular-foundation-models-nuisance-learners-causal-estimation.md) — in this bank: the same TabPFN-for-causal question, asked about nuisance models
- [**When Covariates Mask Pre-Trends**](2026-11-06-arxiv-when-covariates-mask-pre-trends-honest-did.md) — in this bank: why pre-trend diagnostics can mislead, the problem this paper starts from
- [**Honest Inference for Synthetic Controls with Imperfect Fit: Time-Split Validity and the Choice of Anchor**](2026-10-26-arxiv-honest-inference-synthetic-controls-imperfect-fit.md) — in this bank: another forecast-based comparison design for panels

### Jargon buster

- **Prognostic score** — A prediction of a unit's outcome without treatment, used to find comparable controls (vs a propensity score, which predicts treatment).
- **Entropy balancing** — Reweighting controls so chosen moments (here, mean and variance of the score) exactly match the treated group.
- **NSW / LaLonde benchmark** — A 1970s job-training experiment whose randomized estimate is used to test observational methods.
- **TabPFN** — A tabular foundation model that predicts via in-context learning on the supplied dataset, without task-specific training.
