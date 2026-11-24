---
id: arxiv-informative-late-propensity-scores
title: "Informative Local Average Treatment Effects Using Propensity Scores"
source: "University of Fribourg / UC Irvine (arXiv econ.EM)"
url: "https://arxiv.org/abs/2611.25253"
published: "2026-11"
added: "2026-11-24"
category: experimentation-causal
tags: [instrumental-variables, late, complier-heterogeneity, marginal-treatment-effects, propensity-score, doubly-robust, local-linear-regression, generated-regressors]
novelty: 3
sourced_via: "full-text fetch"
---

# Informative Local Average Treatment Effects Using Propensity Scores

**Source:** [University of Fribourg / UC Irvine (arXiv econ.EM)](https://arxiv.org/abs/2611.25253) · Published 2026-11 · Added 2026-11-24
**Category:** Experimentation & Causal Inference · **Tags:** `instrumental-variables`, `late`, `complier-heterogeneity`, `marginal-treatment-effects`, `propensity-score`, `doubly-robust`, `local-linear-regression`, `generated-regressors`

## TL;DR

With a binary instrument, comparing conditional LATEs (CLATEs) across covariate values mixes two things: real effect heterogeneity in the covariates, and changes in *who the compliers are*. Huber and Lee propose "informative" conditional LATEs (ICLATEs). These also condition on the two treatment propensity scores, under Z = 0 and Z = 1. That holds fixed the range of unobservables that defines compliance. The ICLATEs are identified nonparametrically, linked to marginal treatment effects (MTEs), and give a testable implication of two homogeneity restrictions even with a single binary instrument. Estimation is by cross-fitted ML scores plus local linear regression. In a Job Corps illustration, the effect is significant at age 20 but the pointwise results do not establish differences across ages.

## 1. Business context

Instrumental variables are the standard tool when treatment take-up is imperfect, for example when an offer is randomized but participation is chosen. A binary instrument identifies the local average treatment effect (LATE) for compliers, the units whose treatment responds to the instrument (Imbens & Angrist 1994). Analysts then ask how that effect varies with covariates and estimate CLATEs.

The paper argues the CLATE is "only partially informative". The complier population changes with the covariates being conditioned on, because the first-stage effect of the instrument varies with them. Apparent heterogeneity may therefore reflect the covariates, unobservables that differ across complier populations, or both. The authors stress that this is a problem of interpretation, not estimation, so more flexible CLATE estimators do not fix it.

Running example: Card's (1995) college-proximity instrument. The return to college by parental earnings mixes a covariate effect with a shift in the range of unobserved high-school quality that defines compliance.

## 2. Technical details

- **Threshold-crossing model.** Under the usual monotonicity (no defiers) assumption, treatment follows D = 1{π(Z, X) ≥ V̄}, with V̄ uniform and independent of (Z, X) (Vytlacil 2002). Compliers are exactly those with π(0, X) < V̄ ≤ π(1, X). So fixing the pair of propensity scores Q = (π(0, X), π(1, X)) fixes the range of unobservables defining compliance.
- **Three parameters.** X̃ is a subset of covariates of interest.
  - *ICLATE₁:* the complier effect given X̃ = x̃ and Q = (π′, π″). It holds both X̃ and the unobservable range fixed.
  - *ICLATE₂:* given Q only. It holds the unobservable range fixed and averages over covariates.
  - *ICLATE₃:* given X̃ only. This is closest to prior work (Ogburn et al. 2015; Athey et al. 2019).
  - None of them holds fixed the identity of compliers or the distribution of covariates outside X̃. Those can still shift.
- **Identification (Theorem 1).** It uses the conditional LATE assumptions of Abadie (2003) and Frölich (2007) plus a support condition. ICLATE₁ is the ratio of conditional expectations of the doubly robust scores ψ^Y and ψ^D given R = (X̃, π(0, X), π(1, X)). No effect-homogeneity restriction is needed. The support condition requires covariates *excluded* from X̃ to generate variation in both propensity scores. If X̃ = X, ICLATE₁ collapses to the CLATE.
- **MTE link (Proposition 1).** ICLATE₁ and ICLATE₂ average the MTE over a *fixed* interval (π′, π″]. ICLATE₃, like the CLATE, averages over a covariate-dependent interval and weights cells by the local complier share.
- **Two homogeneity restrictions.**
  - *Assumption 6:* no effect heterogeneity in the unobservable. This is what allows extrapolation from compliers to the ATE.
  - *Assumption 7:* no heterogeneity across the excluded covariates.
  - Neither implies the other. Jointly they imply ICLATE₁ is constant across propensity-score pairs at fixed x̃ (Proposition 2), which is testable. Maintaining either restriction attributes a rejection to the other.
  - Under Assumption 7 alone, the MTE curve at the level of X̃ is identified on the interior of the supported interval (Theorem 2). "Interval additivity" (Proposition 3) is then a further testable restriction.
- **Estimator.**
  - Step 1: cross-fit the nuisances μ(z, x), π(z, x) and p(x), using parametric, nonparametric or ML methods.
  - Step 2: run a pooled local linear regression of the estimated scores on the *estimated* index R̂.
  - The complication is that π enters both the scores and the conditioning index, i.e. generated regressors. This is handled with partial-L₂ product-rate conditions, uniform first-stage accuracy (a_n/h → 0 and √(nh^d)·a_n → 0), and local continuity of an "index-bias" projection, which may be nonzero.
  - Under undersmoothing, the result is pointwise asymptotic normality with the same first-order expansion as an oracle using the true nuisances, plus a consistent variance estimator.
  - To reduce sensitivity to the fold split, the procedure is repeated over S random partitions and the median is taken (Chernozhukov et al. 2018). Joint Wald tests at finitely many prespecified points allow tests of constancy and interval additivity.
- **Rate notes.** A uniform O_p(n^−1/4) first stage suffices for d = 3 or 4 under the paper's bandwidth rule, but not for d = 2. Logistic lasso can meet the uniform-accuracy requirement under stated conditions. An ordinary L₂ prediction rate alone does not establish it.

## 3. Impact — potential & realized

**Measured (simulation):** X ∈ ℝ¹⁰, n ∈ {4,000, 20,000}, 500 replications per design. There are two designs with zero and nonzero index bias but the same true ICLATE₁ at (π′, π″) = (0.40, 0.70), with x̃ ∈ {−0.5, 0, 0.5} (true values ≈ −0.564, −0.064, 0.436). Nuisances are fit by correctly specified probit and linear regressions, with 5-fold cross-fitting repeated over 11 partitions.
- Absolute bias is below 0.09 and below 11% of the empirical SD in every configuration. RMSE is close to the SD.
- Going from n = 4,000 to 20,000 cuts SDs to about 0.55–0.72 of their earlier values, broadly consistent with the 5^(−17/70) ≈ 0.68 implied by the theory.
- Mean standard errors exceed the empirical SDs by up to about 16%. Coverage is 0.948–0.980, mostly above 0.95. The authors note they do not isolate the repeated-partition adjustment's contribution to this overcoverage.

**Measured (Job Corps):** 9,240 observations. Z is random assignment to eligibility, D is participation in academic or vocational training in year 1, and Y is weekly earnings in year 4 (USD). There are 28 baseline covariates, and X̃ is age. The evaluation pair (0.45, 0.85) implies a complier share of 0.40. Attainable complier shares have a median of 0.34 and an IQR of 0.26–0.43.
- *ICLATE₁ by age 17/18/19/20:* 111.2 / 16.0 / 33.5 / 198.7, with SEs 83.6 / 54.3 / 54.7 / 74.1. Only age 20 is significant (p = 0.007). Effective local sample sizes are 236–417.
- *ICLATE₂ across π′ = 0.35 / 0.45 / 0.55 (π″ = 0.85):* 68.4 / 73.9 / 96.3. One of the three is significant at the 10% level (p = 0.060).
- *ICLATE₃ by age:* 58.4 / 33.3 / 13.9 / 94.7. Age 20 is significant at 1% (p = 0.001) and age 17 at 10% (p = 0.068). The SEs are roughly a third to a half of ICLATE₁'s, because the conditioning set is one-dimensional.
- The authors state that the pointwise results do not establish statistically significant differences across ages.

**Potential:** The paper offers a way to report covariate heterogeneity of IV effects that does not silently change the complier population, plus a test of homogeneity with a single binary instrument. The price is precision: conditioning on two extra continuous scores sharply cuts the effective sample size.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sharp interpretive fix for CLATE comparisons, but expensive in data

The core observation is simple and, once stated, hard to unsee. The two propensity scores *are* the complier boundaries in V̄-space, so conditioning on them holds the unobservable window fixed. The pieces are known: MTE theory, Tan/Ogburn-style doubly robust scores, DML cross-fitting and generated-regressor asymptotics. The contribution is assembling them into usable parameters, a single-instrument testable implication, and careful inference with an estimated conditioning index. That is solid, not field-shifting.

My own read for practitioners: this matters whenever an experiment randomizes an *offer* or *encouragement* and you want to slice the complier effect by user segment. That is a common pattern in product experimentation, but it is my framing; the paper's application is a training program. The practical hurdles are real. You need excluded covariates that move both propensity scores. Support must be checked against the fitted scores. Effective local samples were a few hundred even with 9,240 units. The Job Corps tables show the cost: ICLATE₁ is noisy enough that the age pattern cannot be distinguished. Expect ICLATE₃ and the CLATE to remain the default, with ICLATE₁ used as a diagnostic.

### Similar / related work

- [**Instrumental variables with treatment clusters**](2026-11-13-arxiv-instrumental-variables-treatment-clusters.md) (in this bank) — another paper on what a LATE-type estimand actually averages over and which assumptions make it interpretable.
- [**Design-Based Inference for Fuzzy Difference-in-Differences**](2026-11-19-arxiv-design-based-inference-fuzzy-did.md) (in this bank) — imperfect take-up again, where the Wald-type estimand is a complier effect plus contamination terms.
- [**Nonparametric estimation of causal heterogeneity under high-dimensional confounding**](https://arxiv.org/abs/1908.08779) — Zimmert & Lechner; the "ML scores + kernel regression on a low-dimensional conditioning set" template this estimator builds on (selection on observables).
- [**Automatic locally robust GMM with machine-learning-generated regressors**](https://arxiv.org/abs/2301.10643) — Escanciano & Pérez-Izquierdo; related treatment of ML-generated regressors that the paper cites.

### Jargon buster

- **LATE / complier** — the average effect among units whose treatment status is switched by the instrument; compliers take treatment only when encouraged.
- **CLATE** — the LATE conditional on covariates; its complier population can differ from one covariate value to another.
- **Marginal treatment effect (MTE)** — the average effect for units at a given point of the unobserved "resistance to treatment"; LATEs are averages of MTEs over intervals.
- **Generated regressor** — a regressor that is itself estimated (here, the fitted propensity scores), whose estimation error must be accounted for in inference.
- **Undersmoothing** — choosing a kernel bandwidth smaller than MSE-optimal so smoothing bias vanishes faster than the standard error and confidence intervals stay centered.
