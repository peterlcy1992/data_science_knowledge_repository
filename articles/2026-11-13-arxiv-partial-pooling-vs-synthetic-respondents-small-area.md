---
id: arxiv-partial-pooling-vs-synthetic-respondents-small-area
title: "Partial pooling beats synthetic respondents as estimators, not as covariates: a preregistered small-sample tournament"
source: "arXiv stat.AP (Howard Kim, Seoul Cyber University)"
url: "https://arxiv.org/abs/2611.14526"
published: "2026-11"
added: "2026-11-13"
category: statistical-modeling
tags: [small-area-estimation, MRP, multilevel-models, synthetic-respondents, LLM-personas, preregistration, survey-calibration, interval-coverage]
novelty: 3
sourced_via: "full-text fetch"
---

# Partial pooling beats synthetic respondents as estimators, not as covariates: a preregistered small-sample tournament

**Source:** [arXiv stat.AP (Howard Kim, Seoul Cyber University)](https://arxiv.org/abs/2611.14526) · Published 2026-11 · Added 2026-11-13
**Category:** statistical-modeling · **Tags:** `small-area-estimation`, `MRP`, `multilevel-models`, `synthetic-respondents`, `LLM-personas`, `preregistration`, `survey-calibration`, `interval-coverage`

## TL;DR

A preregistered head-to-head of ten segment-level survey estimators on a Korean media panel, including LLM-generated synthetic respondents attached as a prior or as a bias correction. A multilevel partial-pooling (MRP-family) model led every calibration-only estimator at every budget — at 100 real respondents it matched what direct estimation reaches with roughly four times as many — and no registered synthetic-panel advantage over MRP survived the decision rule. But an exploratory hybrid that enters the synthetic cell rates as a *covariate inside* the multilevel model did improve on MRP for segments the survey never observed.

## 1. Business context

Surveys are routinely asked for estimates at a finer grain than they were designed for — adoption among men in their twenties, or women over seventy. Fourteen sex × age cells from a national sample leave some cells small and direct estimates noisy. Small-area methods (Fay–Herriot, MRP) "borrow strength" across cells. A fast-growing literature proposes LLM synthetic respondents to fill such gaps, but, the author argues, has not compared them with the small-area estimators a survey methodologist would actually use, at affordable sample sizes, for segments the survey may not reach. The same question faces product teams tempted to replace user research or segment surveys with LLM personas.

## 2. Technical details

**Data.** Korea Media Panel Survey (KISDI) 2023–2025 waves; the 2024 analysis sample is 8,675 individuals in 4,016 households (2025: 8,395). Outcomes are eight binary usage items (e.g. AI services, OTT, YouTube, short-form video); the primary scoring plane is the six items also present in 2023. Synthetic data are public persona responses from the author's earlier study, generated from NVIDIA's Nemotron-Personas-Korea set by two models — Gemini and EXAONE — analysed separately, never averaged.

**Design (preregistered at OSF).** Identical household-clustered splits (200 per condition); calibration budgets n ∈ {50, 100, 200, 400, 800} real respondents; three holdout regimes — no holdout, cell holdout (each of the 14 cells withheld in turn, i.e. an unobserved segment) and temporal holdout. Ten estimators: direct estimation, raking, regression, MRP, fully Bayesian beta-binomial shrinkage, previous-wave carry-forward (as a prior and as a correction), and the synthetic panel attached as a bias correction and as a Bayesian prior (each split by generating model). Primary metric: cell MAE (also RMSE, worst-cell error, interval coverage). Decision rule: a contrast must be "split-stable" and reach a prespecified smallest effect of interest of 1.0 percentage point.

## 3. Impact — potential & realized

**Findings (as reported).**
- MRP led every calibration-only estimator at every budget; MRP at n = 100 ≈ direct estimation at n ≈ 400.
- On unobserved segments, information fixed as a **per-segment prior is inert** — it returns the prior unchanged with error flat in the budget — for both the synthetic panel and the previous wave; priors that pool across cells keep learning.
- **Bias correction transfers but imports estimation noise:** it pays only when the source's bias is large relative to the noise of estimating it — at every budget for a heavily biased synthetic panel, only past several hundred respondents for an accurate previous wave.
- A synthetic panel can't represent a segment its persona source lacks: the persona set has no one under 19, so the "teens" cell (10–19 in the survey) is really nineteen-year-olds.
- No registered synthetic advantage over MRP survived the paired decision rule.
- **Exploratory hybrid** (registered MRP + synthetic cell rates as a covariate): under cell holdout the Gemini-based hybrid beat the registered MRP at every budget, by 2.75 points at n = 50 falling to 0.93 at n = 800; the EXAONE-based hybrid gained 0.83 and 0.50 points at n = 50 and 100 (below the 1-point threshold). At n = 50 under cell holdout: Gemini hybrid 8.33, corrected EXAONE panel 9.52, strengthened MRP 9.86, EXAONE hybrid 10.26, registered MRP 11.09 (cell MAE, points).
- Interval coverage stayed below nominal throughout and, contrary to the preregistered prediction, worsened with budget for partial pooling.

**Potential.** The author proposes that any method attaching external information to survey estimation be evaluated on unobserved segments and across a budget range, since neither the inertness of fixed priors nor the conditionality of correction shows up on observed segments at one sample size.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A carefully preregistered reality check: the right baseline for synthetic respondents is MRP, and the right place for them is as a covariate.

The useful lesson is about *how* external information is attached, not whether LLM personas are "good": as a fixed per-cell prior they can't learn, as a correction they add noise, but as a predictor inside a hierarchical model the data decide how much to trust them. That is standard MRP practice (group-level predictors) applied to a new information source, and it generalizes to any proxy signal — LLM-scored labels, third-party panels, last year's survey. Caveats: one dataset, one country, two generating models, and the winning hybrid was built after the tournament; under-coverage of every interval method is its own warning.

### Similar / related work

- [**It's Fine to Use Computer-Generated Survey Responses — If You Don't Care About the Data Anyway**](2026-09-28-gelman-junk-polls-ai-survey-data.md) — in this bank: Gelman's sceptical take on synthetic survey data
- [**From More to Better: Causal Inference and Digital Experimentation in the Age of AI**](2026-11-13-arxiv-cider-causal-inference-digital-experimentation-age-of-ai.md) — in this bank: industry roundtable listing synthetic-evidence validity as contested
- [**Covariance-Calibrated Prediction-Powered Inference**](2026-10-16-arxiv-covariance-calibrated-prediction-powered-inference.md) — in this bank: another principled way to combine model predictions with a small labelled sample
- **Poststratification into many categories using hierarchical logistic regression (Gelman & Little, 1997)** — the origin of MRP

### Jargon buster

- **MRP (multilevel regression and poststratification)** — Fit a hierarchical model across demographic cells, then reweight cell predictions to the population.
- **Partial pooling** — Shrinking each cell's estimate toward the overall mean, more so for cells with little data.
- **Small-area estimation** — Methods for estimating quantities in subgroups too small for reliable direct estimates.
- **Cell holdout** — Evaluating a cell with none of its respondents in the calibration sample, mimicking an unobserved segment.
- **Preregistration** — Fixing design, estimators, metrics and decision rule publicly before seeing results.
