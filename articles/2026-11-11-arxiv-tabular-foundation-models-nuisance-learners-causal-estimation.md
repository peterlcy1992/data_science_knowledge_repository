---
id: arxiv-tabular-foundation-models-nuisance-learners-causal-estimation
title: "Does Predictive Performance Translate to Causal Performance? Evaluating tabular foundation models as nuisance learners for causal effect estimation"
source: "arXiv stat.ME (Weckstein, Dahabreh, Zitnik, Hernández-Díaz, Schneeweiss; Harvard)"
url: "https://arxiv.org/abs/2611.11381"
published: "2026-11"
added: "2026-11-11"
category: experimentation-causal
tags: [TabPFN, doubly-robust, AIPW, TMLE, cross-fitting, Super-Learner, nuisance-estimation]
novelty: 4
sourced_via: "full-text fetch"
---

# Does Predictive Performance Translate to Causal Performance? Evaluating tabular foundation models as nuisance learners for causal effect estimation

**Source:** [arXiv stat.ME (Weckstein, Dahabreh, Zitnik, Hernández-Díaz, Schneeweiss; Harvard)](https://arxiv.org/abs/2611.11381) · Published 2026-11 · Added 2026-11-11
**Category:** experimentation-causal · **Tags:** `TabPFN`, `doubly-robust`, `AIPW`, `TMLE`, `cross-fitting`, `Super-Learner`, `nuisance-estimation`

## TL;DR

Used untuned as the propensity and outcome learner inside AIPW and TMLE, the tabular foundation model TabPFN (and Mitra) matched correctly specified regressions in simple settings and beat richly specified Super Learner ensembles in complex ones, for both bias and confidence-interval coverage. The failure mode: at n = 200 and in higher-dimensional semi-synthetic settings without cross-fitting, propensity overfitting consistent with memorising treatment labels in-context.

## 1. Business context

Doubly robust estimation of average treatment effects from observational data — the workhorse for quasi-experimental product and policy analyses — depends on nuisance models for the propensity score and outcome. Flexible ML helps when the true structure is unknown but brings overfitting and invalid-uncertainty risks; standard practice is diverse Super Learner ensembles plus cross-fitting, which require manual library selection and tuning. Tabular foundation models (prior-data fitted networks, PFNs) predict well in-context out of the box; the question is whether that translates into accurate causal estimates and valid inference.

## 2. Technical details

Estimators: AIPW and TMLE (with influence-curve SEs), with and without cross-fitting; g-computation and IPW as sensitivity analyses. Learners: GLMs, random forest and highly adaptive lasso (some CV tuning), TabPFN v3 out-of-the-box, Mitra (secondary), and three Super Learner ensembles — 'SL Flexible' (random forests, XGBoost, GAMs) and 'SL Lightweight' (GLM, stepwise, MARS, mean), the top performers in prior studies of this setting, plus the tmle/SuperLearner R defaults.

Simulation 1 (synthetic): the simple and complex confounding designs of Naimi et al., adapted from Kang & Schafer — four standard-normal confounders, constant effect ψ = 6; in the complex case only nonlinear transforms of covariates are observed. 200 replicates at n = 200, 1,200, 5,000. Simulation 2 (plasmode): ACIC 2016 competition design on real Collaborative Perinatal Project covariates, 44 DGPs × 50 replicates (2,200 datasets), ATE and ATT. Metrics: relative bias, RMSE, 95% CI coverage, SE calibration ratio, run time.

## 3. Impact — potential & realized

Realized (simulations only): in simple parametric settings PFNs were competitive with correctly specified GLMs; in complex settings they outperformed all conventional learners including Super Learners, and as n grew only TabPFN and Mitra consistently approached nominal coverage. In simulation 2 with TMLE + cross-fitting, TabPFN had the lowest macro-average RMSE and about half the bias of the next best learner (0.8% vs 1.6% ATE; 0.9% vs 1.7% ATT), the lowest mean RMSE in 35/35 ATE-identified and 38/44 ATT-identified DGPs, and coverage not significantly below nominal in at least 94% of DGPs (91% SL Default, 89% parametric, whose intervals were over 4× wider). Cross-fitting generally helped flexible learners; for PFNs it was sometimes unnecessary at n = 1,200/5,000 but important at n = 200 and for TMLE-TabPFN in simulation 2.

Limitations stated by the authors: simulations only; ATE/ATT with binary treatment and continuous outcome; identifiability guaranteed by design; large foundation models may be impractical for big or high-dimensional data.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Practically important evidence that an off-the-shelf tabular foundation model can be a strong default nuisance learner — with cross-fitting still recommended at small n.

For applied DS, this suggests TabPFN-in-AIPW/TMLE as a serious low-effort baseline next to a hand-built Super Learner, and a reminder that cross-fitting is cheap insurance: the in-context memorisation failure is exactly the kind of thing that silently breaks coverage. I would want to see binary outcomes, poor overlap and larger n (where PFN context limits bite) before swapping it in as the default. Strong design choice: benchmarking against the ensembles that won previous studies of the same simulations.

### Similar / related work

- [**When Sample-Splitting Choices Matter in TMLE and AIPW: Cross-Fitting, Targeting, and Repetition**](2026-10-15-arxiv-tmle-aipw-sample-splitting-cross-fitting.md) — in this bank: the cross-fitting choices this paper stress-tests with a new learner class
- [**Introduction to Causal Inference Using Double Machine Learning**](2026-09-22-microsoft-double-machine-learning.md) — in this bank: practitioner primer on ML nuisance models inside causal estimators
- [**From "What Happened?" to "What Will Happen?": Genie + TabPFN for conversational predictive BI**](2026-10-06-databricks-genie-tabpfn-predictive-bi.md) — in this bank: TabPFN on the predictive side in an analytics product

### Jargon buster

- **Nuisance function** — A quantity you must estimate (propensity score, outcome regression) but don't care about for its own sake.
- **Doubly robust (AIPW/TMLE)** — Estimators that stay consistent if either the propensity or the outcome model is right.
- **Cross-fitting** — Fit nuisance models on one fold and predict on another, rotating, to avoid overfitting bias.
- **PFN / TabPFN** — A transformer pre-trained on millions of synthetic tables that predicts on a new dataset in one forward pass using the labeled rows as context.
- **Plasmode simulation** — Simulation that keeps real covariates but generates treatment and outcome from known models so ground truth is available.
