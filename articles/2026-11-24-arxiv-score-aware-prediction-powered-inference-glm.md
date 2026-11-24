---
id: arxiv-score-aware-prediction-powered-inference-glm
title: "Score-aware nonparametric adaptation of prediction-powered inference"
source: "Washington University in St. Louis (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.31138"
published: "2026-11"
added: "2026-11-24"
category: statistical-modeling
tags: [prediction-powered-inference, semi-supervised-inference, glm, dimension-reduction, single-index-model, b-splines, efficiency, confidence-intervals]
novelty: 3
sourced_via: "full-text fetch"
---

# Score-aware nonparametric adaptation of prediction-powered inference

**Source:** [Washington University in St. Louis (arXiv stat.ME)](https://arxiv.org/abs/2611.31138) · Published 2026-11 · Added 2026-11-24
**Category:** Statistical Modeling · **Tags:** `prediction-powered-inference`, `semi-supervised-inference`, `glm`, `dimension-reduction`, `single-index-model`, `b-splines`, `efficiency`, `confidence-intervals`

## TL;DR

Prediction-powered inference (PPI) uses an external model's predictions on unlabelled data, plus a small labelled sample, to estimate regression coefficients more efficiently. The optimal version needs E(Y | f, X), a regression on all covariates plus the prediction, which is hard to learn from few labels. SAN-PPI squeezes (f, X) into one scalar index with an augmented GLM, then fits a spline in that index. It is guaranteed asymptotically no worse than labelled-only inference, and in simulations its RMSE was within about 1% of the best competitor.

## 1. Business context

A common setup: a few hundred labelled units, many more unlabelled ones, and a pretrained model that predicts the outcome for all of them. The model may use extra inputs, such as unstructured data, that are not in the regression. The analyst wants GLM coefficients (linear or logistic regression) with valid confidence intervals.

Treating predictions as real outcomes introduces bias. Original PPI (Angelopoulos et al., 2023) corrects that bias with the labelled sample, but it can be *less* efficient than just using the labels when predictions are weak. Later methods (PPI++, PDC, PSPA and others) adapt how much the predictions count. Recalibrated PPI (Ji et al., 2025) characterised the optimal use of predictions, but it needs a multivariate conditional mean estimated from the labelled sample. The authors say this "can be difficult when the labelled sample is limited, or when the covariate dimension is moderately high". SAN is built "to mitigate the resulting curse of dimensionality".

## 2. Technical details

- **Target.** Coefficients θ* of a working GLM with canonical link. The model may be misspecified, in which case θ* is the pseudo-true parameter. Labelled data are (Y, f, X), unlabelled data are (f, X), and the two samples are i.i.d. and independent. Here f is a scalar external prediction.
- **Optimal predicted score.** Following Ji et al., the variance-minimising score is (1 − ρ)·X̃·{E(Y | f, X) − μ_θ*}, where ρ = n/(n+N). The hard part is E(Y | f, X).
- **Dimension reduction.** Fit an *augmented GLM* of Y on (1, τ(f), X) using the labelled sample. τ is a one-to-one transform, by default the inverse link (e.g. logit for probabilities), or the identity for binary f. Its fitted mean S is a scalar index. E(Y | f, X) is then approximated by a B-spline in S.
- **Safety by construction.** The predicted-score class is spanned by X̃·[μ_θ, b_K(S)ᵀ]. Coefficients β = 0 recover the labelled-only estimator. β is chosen to minimise the estimated trace of the asymptotic covariance, which is quadratic with a closed-form solution (Proposition 1). The estimate is plugged into a one-step update from the labelled-only fit.
- **Inference.** Plug-in sandwich covariance with a heuristic n/(n − d_eff) finite-sample multiplier, where d_eff = 2p + K + 2, and Wald intervals.
- **Theory.** Theorem 1 gives asymptotic normality and an asymptotic covariance trace no greater than labelled-only, "even when the dimension reduction is insufficient". It requires a spline dimension with K⁵/n → 0, among other conditions. Corollary 1 gives consistent variance estimation and nominal Wald coverage. Proposition 2 says the index is *sufficient*, i.e. E(Y | S) = E(Y | f, X), under a single-index model with elliptical (τ(f), X) and a nondegeneracy condition (Li & Duan, 1989). Remark 2 shows a Gaussian stylised model of modality mismatch or distribution shift satisfies these conditions.
- **Simulation design.** Linear and logistic regression with 5 covariates, plus 10 auxiliary predictors W that enter only the prediction model. Marginals are Student t₁₀ and Bernoulli(0.25), joined by a Gaussian copula. There are two mean specifications, linear or quadratic in the index on the link scale. n = 600 labelled (n = 300 also run), N ∈ {500, 1000, 2000, 4000}, 1,000 replications. f comes from a scikit-learn random forest (100 trees) trained on an independent external sample of 5,000. Two scenarios: *modality mismatch*, where the forest sees only W, and *distributional shift*, where it sees X and W but Y | (X, W) differs from the study population. SAN uses cubic B-splines with K = 4.
- **Baselines.** Labelled-only, PPI, PPI++, PDC, PSPA, SEMI (Song et al.), RePPI (Ji et al.), and a five-fold cross-fitted random forest estimate of E(Y | f, X) with no dimension reduction (CF–RF).

## 3. Impact — potential & realized

**Measured (simulation only; no real dataset is analysed):**
- Across all settings, the minimum RMSE ratio of any competitor to SAN-PPI (full coefficient vector) was about 0.990. The authors read this as SAN being "comparable to the best-performing estimator among those considered".
- SAN's 95% Wald intervals had coverage close to nominal. RePPI intervals showed "some undercoverage, possibly due to the relatively small labelled sample size".
- Results at n = 300 were similar to n = 600.
- Against an approximate oracle (a random forest for E(Y | f, X) trained on 12,000 extra labelled observations), SAN's RMSE was the closest of all methods. It had negligible empirical bias, and its estimated SEs were close to empirical SDs.
- Spline-size sensitivity: for K ∈ {5, 6, 7} relative to K = 4, RMSE ratios ranged from 0.987 to 1.009 and coverage moved by less than 1.1 percentage points.
- τ(f) was strongly right-skewed under the second mean specification, yet efficiency gains held. The authors say this "suggest[s]" the method can remain effective beyond the ellipticity assumption.

**Potential:** A drop-in PPI variant for GLM coefficients when labels are few and covariates are more than a handful. Its no-worse-than-labelled-only guarantee holds even when the single-index approximation is wrong. How large the gain is depends on how well the index captures E(Y | f, X).

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sensible single-index fix for the nuisance-estimation bottleneck in optimal PPI

The building blocks are known: Ji et al.'s optimal predicted score, the Li–Duan result that a misspecified GLM still recovers a single-index direction, and the "include the zero solution and minimise variance" safety trick from the PPI++/PDC line. The contribution is putting them together cleanly. The result is a low-dimensional, closed-form way to approximate the optimal score, and the safety guarantee survives when the approximation fails. The trade-off is that the gain is only as good as the index.

The evidence is thin. It is one simulation family with 5 covariates, a single prediction model type, and no real-data application. A ~1% RMSE edge, or parity, over CF–RF and RePPI is "competitive", not dominant. The more practical selling point is better coverage than RePPI at small n. Teams already using PPI for regression on LLM- or model-labelled data could try it cheaply, since it is a one-step update plus a spline fit.

### Similar / related work

- [**Prediction-Powered Inference**](https://arxiv.org/abs/2301.09633) — Angelopoulos et al.; the original bias-corrected framework that SAN adapts.
- [**Predictions as surrogates: revisiting surrogate outcomes in the age of AI**](https://arxiv.org/abs/2501.09731) — Ji, Lei & Zrnic; derives the optimal predicted score (RePPI) whose conditional mean SAN approximates with a scalar index.
- [**Covariance-Calibrated Prediction-Powered Inference**](2026-10-16-arxiv-covariance-calibrated-prediction-powered-inference.md) (in this bank) — another efficiency refinement of PPI, tuning the GMM weight with unlabelled prediction scores instead of reducing the nuisance dimension.
- [**Another look at inference after prediction**](https://arxiv.org/abs/2411.19908) — Gronsbell et al.; one of the adaptive methods cited as guarding PPI against efficiency loss.

### Jargon buster

- **Prediction-powered inference (PPI)** — combine model predictions on lots of unlabelled data with a small labelled sample that corrects the predictions' bias, so inference stays valid even if the model is poor.
- **Predicted score** — the stand-in for the estimating-equation term (the "score") on units without a label; choosing it well is what makes PPI efficient.
- **Single-index model** — the outcome depends on many inputs only through one linear combination of them, which turns a p-dimensional regression into a one-dimensional curve.
- **Asymptotic covariance trace** — the sum of the coefficient variances in large samples; SAN picks its weights to minimise this.
- **B-spline basis** — a set of smooth, piecewise-polynomial bumps used to fit a flexible curve with a small number of coefficients (here K = 4).
