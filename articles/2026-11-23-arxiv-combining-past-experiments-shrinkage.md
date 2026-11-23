---
id: arxiv-combining-past-experiments-shrinkage
title: "Combining Past Experimental Data for Efficient Estimation: A Shrinkage Approach"
source: "University of Michigan Ross (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.27655"
published: "2026-11"
added: "2026-11-23"
category: experimentation-causal
tags: [shrinkage, experiment-archive, historical-experiments, bias-variance, mse, pretest-estimator, data-pooling, a-b-testing]
novelty: 4
sourced_via: "full-text fetch"
---

# Combining Past Experimental Data for Efficient Estimation: A Shrinkage Approach

**Source:** [University of Michigan Ross (arXiv stat.ME)](https://arxiv.org/abs/2611.27655) · Published 2026-11 · Added 2026-11-23
**Category:** Experimentation & Causal Inference · **Tags:** `shrinkage`, `experiment-archive`, `historical-experiments`, `bias-variance`, `mse`, `pretest-estimator`, `data-pooling`, `a-b-testing`

## TL;DR

Firms keep archives of past A/B tests on related but different interventions. This paper asks when borrowing from those biased past experiments lowers the mean squared error of a *single* new treatment-effect estimate. With known biases and variances, borrowing from even one biased experiment strictly reduces MSE. For practice it proposes three estimators: a general plug-in, a pooled plug-in and a fixed-weight estimator with a hypothesis-testing gate (FH). Which one to use depends on two features of the archive: its average bias and how dispersed the biases are.

## 1. Business context

Experimentation programs at Airbnb, Amazon, Booking.com, Google, Microsoft and Netflix collectively test more than 100,000 treatments a year (Gupta et al. 2019). Booking.com, for example, stores every experiment in a searchable repository. The authors note these archives are "typically used only qualitatively", to inform intuition, and rarely feed into the statistical estimate of a new effect.

The stated goal is better *point estimation* (MSE) of the new effect, because effect sizes drive launch prioritisation and business-impact estimates. The paper says this differs from improving confidence-interval efficiency or hypothesis tests. The obstacle is that past experiments test non-identical interventions, so their estimates are biased for the current target by unknown amounts in unknown directions. Naive averaging can make things worse.

## 2. Technical details

- **Model.** The target experiment gives i.i.d. observations with mean θ and variance σ²_A. Auxiliary experiment i gives observations with mean θ + εᵢ, where εᵢ is a fixed, unknown bias. Only finite second moments are assumed; nothing has to be Gaussian. All datasets are independent.
- **Estimator family.** θ̂(w) = (1 − Σwᵢ)·Ā + Σ wᵢ·B̄ᵢ, a linear blend of the target mean and the auxiliary means.
- **Oracle result.** With one auxiliary study, the MSE-minimising weight is w* = V_A / (ε₁² + V_A + V_B). The MSE gain over Ā is −V_A² / (ε₁² + V_A + V_B), which is strictly negative for any finite bias. With M studies, w* = V_A·Q⁻¹·1, where Q = εεᵀ + Σ + V_A·11ᵀ. The authors contrast this with James–Stein shrinkage: their estimand is univariate, so the usual dimension ≥ 3 dominance results do not apply.
- **Estimator 1: general plug-in.** Sample splitting: a pilot split estimates the study-specific biases and variances that go into the oracle weights, and an independent testing split forms the final estimate. As M → ∞ its limiting MSE depends on the average bias *e* and the bias dispersion δ (the variance of the εᵢ). The effect of δ is non-monotone. More dispersed biases give more room to reweight studies so their biases cancel. But the weights cancel *estimated* bias, not true bias, so this flexibility also leads to overfitting.
- **Estimator 2: pooled plug-in.** This limits study-specific reweighting to curb that overfitting. Relative auxiliary weights depend only on estimated precision, and its limiting MSE does not depend directly on δ.
- **Estimator 3: FH (fixed weights plus a hypothesis-testing gate).** It needs no sample split. It pools all observations with sample-size weights: θ̂_fix = (N_A·Ā + Σ N_B,i·B̄ᵢ)/(N_A + Σ N_B,i). It keeps the pooled estimate only if |B̃ − Ā| ≤ t₁₋α/₂·√(V̂_A + Û). Otherwise it falls back to Ā. This is a pretest ("test-and-pool") estimator. As |e| → ∞ its MSE returns to V_A. The cost (Proposition 6.1) is that its MSE is strictly above min{e², V_A}, so in favourable regimes it leaves gains on the table.
- **Inference.** The paper gives asymptotic CIs for the oracle estimator (fixed M) and large-M CIs for the plug-in estimators, which include a bias-shift term.
- **Simulations.** Gaussian data with θ = 10, N_A = 100, σ²_A = 64 (so V_A = 0.64), auxiliary N ∈ {100…150}, σ²_B ∈ [81, 100] and FH gate α = 0.10. There are four (e, δ) environments: (0.15, 0.05), (0.15, 12), (5, 2) and (5, 36). Nested archives grow to M = 1…80, with 50,000 Monte Carlo replications each.

## 3. Impact — potential & realized

**Measured (simulation only; no real experiment archive is analysed):**
- Small *e* and small δ: all three estimators beat no-borrowing once enough studies are added, and the general plug-in does best.
- Small *e* and large δ: the pooled plug-in beats the general plug-in.
- Large *e*: both plug-ins have "substantially higher MSE than the no-borrowing benchmark". FH detects the discrepancy and stays close to V_A.
- Finite-M curves move toward the large-M limits, but convergence is slower and more volatile when δ is large.

**Decision table (paper's Table 1):** small *e* and small δ → general plug-in; small *e* and large δ → pooled plug-in; large *e* → FH.

**Potential:** The authors argue that mature platforms sit in the favourable quadrant. They cite Kohavi et al. (2020): 80–90% of Google and Bing experiments have near-zero effects, often within 1–2% of each other. Successive iterations of a campaign on the same segment are their canonical example. An experiment archive could then become a quantitative prior for effect-size estimates rather than only a source of hypotheses.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A clean, decision-oriented answer to "can our experiment archive sharpen this estimate?"

The ingredients are known: Stein-style shrinkage, Rosenman et al.'s experimental/observational combination, and pretest estimators. The useful part is the single-estimand framing and the two-axis diagnosis (average bias vs bias dispersion). Together they produce a decision table a platform team could adopt. The non-monotone role of dispersion is a genuinely non-obvious result.

Caveats: the validation is simulation only, and the gains depend on archive studies being comparable to the target. Platforms would have to define "related experiments" carefully, since that choice effectively sets *e*. Also, an MSE-optimal point estimate shrunk toward the archive is not the same thing as a valid ship/no-ship test, and the paper says so explicitly. Expect experimentation vendors that already expose priors (Bayesian A/B tools) to find this a natural frequentist complement.

### Similar / related work

- [**Shrink Responsibly: Empirical Bayes in Economics**](2026-11-18-arxiv-shrink-responsibly-empirical-bayes-economics.md) (in this bank) — the empirical-Bayes view of the same bias-variance trade when pooling many noisy estimates.
- [**Stratified Randomization Incorporating Historical Control Data**](2026-11-17-arxiv-stratified-randomization-historical-control-data.md) (in this bank) — uses historical data at the design stage rather than in the estimator.
- [**Many Hands Make Light Work: Long-Term Effect Inference for the Experiment Reservoir**](2026-10-28-arxiv-experiment-reservoir-surrogate-long-term-effects.md) (in this bank) — another way to put an experiment archive to quantitative use.
- [**Combining Observational and Experimental Datasets Using Shrinkage Estimators**](https://arxiv.org/abs/2002.06708) — Rosenman, Basse, Owen & Baiocchi; vector-valued Stein shrinkage across subgroups that this paper contrasts itself with.

### Jargon buster

- **Shrinkage estimator** — pulls a noisy unbiased estimate toward a more stable reference, accepting some bias for lower variance.
- **MSE (mean squared error)** — bias² + variance; the paper's yardstick for estimate accuracy.
- **Bias dispersion (δ)** — how much the past experiments' biases vary around their average; distinct from how far off they are on average (*e*).
- **Pretest / test-and-pool estimator** — first test whether the auxiliary data look compatible with the target, then pool only if the test does not reject.
- **Sample splitting** — using one part of the data to choose weights and another to compute the estimate, so the weights don't overfit the estimate.
