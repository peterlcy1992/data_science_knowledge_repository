---
id: arxiv-what-should-experiment-measure-long-term-effects
title: "What Should an Experiment Measure? Combining a Short-Term Experiment with Confounded Observational Data to Identify Long-Term Treatment Effects"
source: "Graduate School of Economics, The University of Tokyo (arXiv econ.EM)"
url: "https://arxiv.org/abs/2611.30599"
published: "2026-11"
added: "2026-11-24"
category: experimentation-causal
tags: [long-term-effects, data-combination, experimental-design, latent-unconfoundedness, measurement-error, proxy-variables, inverse-problems, efficient-influence-function]
novelty: 3
sourced_via: "full-text fetch"
---

# What Should an Experiment Measure? Combining a Short-Term Experiment with Confounded Observational Data to Identify Long-Term Treatment Effects

**Source:** [Graduate School of Economics, The University of Tokyo (arXiv econ.EM)](https://arxiv.org/abs/2611.30599) · Published 2026-11 · Added 2026-11-24
**Category:** Experimentation & Causal Inference · **Tags:** `long-term-effects`, `data-combination`, `experimental-design`, `latent-unconfoundedness`, `measurement-error`, `proxy-variables`, `inverse-problems`, `efficient-influence-function`

## TL;DR

Observational data often record the long-term outcome but are confounded. A randomized experiment removes the confounding but would need years of follow-up. This paper asks what a *short-term* experiment should measure so that, combined with the observational data, it identifies the average long-term effect in the observational population. The answer: collect the same coarse post-treatment measurement the observational data already record, add a more detailed measurement that removes confounding, and distinguish no more levels than the coarse measurement can separate. A debiased Tikhonov-penalized series estimator has smaller absolute bias and coverage closer to nominal than the competing estimators in simulations and a Job Corps illustration.

## 1. Business context

The paper's motivating examples are policy questions: job training and earnings years later, or class size and high school graduation. Administrative records link the treatment to the long-term outcome. But selection into treatment depends on characteristics the records do not hold, such as a worker's earnings prospects or a student's need for support. Comparisons stay biased after adjusting for recorded covariates.

Recent work combines short-term experiments with observational data to estimate long-term effects. Athey, Chetty & Imbens (2025) assume latent unconfoundedness given a short-term outcome that both datasets record (their experimental selection correction, ESC). The surrogate index of Athey et al. (2026) instead relies on surrogacy. Here the setting differs. The observational data record only a *coarse* post-treatment measurement M, such as a routine test score or the share of weeks worked. Conditioning on M does not remove confounding, because M records the underlying characteristic with noise.

The paper frames the combination as an *experimental design* problem: the researcher chooses what the experiment measures, given what the observational data already contain.

## 2. Technical details

- **Data structure.** The experiment records (X, T, M, S): covariates, randomized treatment, the coarse measurement and a detailed measurement S that only the experiment collects. The observational data record (X, T, M, Y), where Y is the long-term outcome. S and Y are never observed together. The target is τ = E[Y(1) − Y(0) | observational population].
- **Standard assumptions.** Consistency, overlap, randomization in the experiment (possibly given X), and transportability: given X, the joint distribution of (S(t), M(t)) is the same in both populations. These parallel Athey, Chetty & Imbens, with the characteristic S in place of their short-term outcome.
- **Three key conditions.**
  - *Latent unconfoundedness given S:* T ⟂ Y(t) | S(t), X in the observational population.
  - *Two exclusion restrictions:* once S and X are fixed, M carries no further information about selection into treatment or about the mean long-term outcome. Both hold when M is a noisy record of the characteristic and the noise affects neither selection nor the outcome.
  - *Completeness:* the distribution of S(t) given M(t) must vary enough with M(t). With finitely many values, this holds iff the matrix of P(S | M) has full column rank, so M must take at least as many values as S.
- **Identification (Theorem 2.1).** Two moment equations link the populations through M. The left sides are observational moments of M (and of Y·M). The right sides involve the selection probability π_t(s, x) and ν_t = π_t·μ_t as functions of S, weighted by the experimental joint distribution of (S, M). Recovering these functions is a linear inverse problem, as in nonparametric IV: M plays the instrument and S the endogenous variable. Then μ_t = ν_t/π_t, which is averaged over S in each experimental arm and over the observational X distribution.
- **Design implications.** (1) Collect the same coarse measurement, scored the same way. (2) Measure the characteristic in enough detail that, given S and X, M is uninformative about selection and the long-term outcome mean. (3) Do not distinguish more levels of S than M can separate.
- **Estimator.** X takes finitely many values. Because μ_t is a ratio of two unknown functions, a plug-in estimator is shifted to first order by errors in both. The estimator adds corrections built from two "weight functions" derived from the efficient influence function. This makes it insensitive to first-order nuisance errors. π̂ is truncated below at a constant a.
- **Theory.** Asymptotic normality holds under product-rate conditions in the style of Chernozhukov et al. (2018), e.g. each nuisance error o_p(N^−1/4), plus Donsker/Glivenko–Cantelli conditions for the version without sample splitting. A cross-fitted version needs only the rate conditions. The estimator attains the semiparametric efficiency bound when the weight functions are unique and a tangent-space condition holds. In the discrete case, uniqueness needs M to have *at most* as many values as S. With completeness, that means both must have the same number of values.
- **Implementation.** Series estimates with a Tikhonov (ridge-type) penalty chosen from 10⁻⁶ to 10⁰ by two-fold validation of the moment conditions.
- **Extension.** Remark 2.1 and Supplementary Material 1 handle a *pretreatment* proxy shared by both samples (e.g. earnings before random assignment) instead of a post-treatment one.

## 3. Impact — potential & realized

**Measured (simulation):** n_E = n_O ∈ {1,000, 2,000, 4,000, 8,000}, 1,000 replications each, true τ = 3.30. Selection depends on the characteristic, and M records it with uniform error.
- *Continuous design:* the Tikhonov estimator's absolute bias falls from 0.519 to 0.074. Its coverage is 78.8% at 1,000 and 86.5–89.6% at the larger sizes. ESC and ESC Imputation (computed with M in place of S) stay biased by about 0.47, and observational regression by about 0.94, with coverage falling toward zero (0.1% and 0.0% at 8,000). The Tikhonov estimator is far more variable, though. Its RMSE (9.243 → 0.567) is above ESC's (0.550 → 0.479) at every sample size. At 1,000, ESC also has slightly smaller absolute bias.
- *Discrete design (three-valued characteristic):* the Tikhonov version has the smallest absolute bias of the seven estimators at every size: 0.422 at 1,000 and under 0.04 at the larger sizes. Coverage rises from 83.1% to 92.8%. The comparison estimators have bias ≥ 1.54 and coverage ≤ 2.1%.
- Cross-fitting (2 or 4 folds) did not improve performance uniformly. It had larger absolute bias than the no-split version at every size, and 77.6–86.1% coverage at 8,000. The unpenalized version is not reported in the continuous design because its matrix is nearly singular (condition number ≥ 10¹⁰ in 990–1,000 of 1,000 replications). The author recommends the Tikhonov version without sample splitting.

**Measured (Job Corps illustration):** both samples are built from the 9,084 people in the public Job Corps experiment (offer of enrollment randomized), so selection is *constructed*, not real. S is the year-3 weekly earnings category (none / ≤ median of about $188 / above). M is the year-3 share of weeks worked in three levels. Y is year-4 weekly earnings. X has six gender × age cells. Each replication draws 4,500 + 4,500 people, with 1,000 replications under three selection rules. The pseudo-true value is $19.50/week.
- Tikhonov bias is −4.09, 3.33 and −5.21, with coverage of 92.9%, 92.4% and 93.6%.
- ESC and ESC Imputation have biases whose sign follows the direction of selection, with coverage of 60.3–77.4%. Observational regression has bias of 27.32, −28.76 and 10.74, with coverage of 0.5%, 0.2% and 51.1%.
- The 4-fold cross-fitted version covers at 94.6–95.8%.
- On RMSE, ESC is lower than Tikhonov under rules A (8.81 vs 9.97) and C (10.17 vs 10.57). Tikhonov is lower under rule B (8.51 vs 9.92).
- The outcome exclusion restriction holds only approximately in these data. Earnings categories explain 26.7% of the variance of Y within cells and arms, and M adds 0.6 percentage points. The implied shift in the population value is about a third of the estimator's SD, which under a normal approximation lowers coverage by less than two percentage points.

**Potential:** The paper offers a checklist for designing short-term experiments meant to be linked to existing long-term observational data. The weakest link is completeness: the coarse shared measurement must still separate the levels of the detailed one.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A useful design question and a clean identification result, with a variance price

The reframing is the contribution. Instead of "given these datasets, which estimator?", it asks "what should the experiment record so the datasets can be combined?" The answer is crisp: share the coarse metric, add a richer one, and don't over-refine. The machinery (NPIV-style completeness, proximal-style integral equations, a DML-style orthogonal estimator) is borrowed from known literatures. The paper says so, citing Newey & Powell, Miao et al., Cui et al. and Chernozhukov et al. So this is a solid recombination, not a new paradigm.

My own framing for tech teams: the observational side looks like historical product logs with a coarse engagement metric and a long-run outcome such as retention. The design advice would then be to log that same coarse metric in the experiment, plus a richer measurement of the latent trait that drives self-selection. That analogy is mine. The paper's examples are training and schooling.

The results need careful reading. The new estimator mainly removes bias. In the continuous simulation it never beats ESC on RMSE, and its coverage tops out near 90%. Ill-posedness is real here: the unpenalized version breaks down, and results depend on the Tikhonov penalty. The Job Corps exercise is a constructed-selection benchmark, not a real confounded observational study.

### Similar / related work

- [**The Experimental Selection Correction Estimator: Using Experiments to Remove Biases in Observational Estimates**](https://www.nber.org/papers/w33817) — Athey, Chetty & Imbens (NBER WP 33817); latent unconfoundedness given a short-term outcome recorded in both samples. This paper's main comparator (ESC).
- [**Long-Term Quantile Treatment Effects with Combined Experimental and Observational Data**](2026-11-18-arxiv-long-term-quantile-treatment-effects-combined-data.md) (in this bank) — extends the Athey–Chetty–Imbens combined-data setup from average to quantile effects.
- [**Proximal Difference-in-Differences for Causal Learning under Confounding and Outcome Drift**](2026-11-12-arxiv-proximal-did-long-term-effects-outcome-drift.md) (in this bank) — also uses proxies of unmeasured confounding to extend a short experiment with external observational data.
- [**Many Hands Make Light Work: Long-Term Effect Inference for the Experiment Reservoir**](2026-10-28-arxiv-experiment-reservoir-surrogate-long-term-effects.md) (in this bank) — a different route to long-term effects, learning from a reservoir of past long-run experiments.

### Jargon buster

- **Latent unconfoundedness** — treatment choice in the observational data is as good as random once you fix a (possibly unrecorded) characteristic and the covariates.
- **Completeness** — the coarse measurement varies enough with the detailed one that a function of the detailed measurement can be pinned down from its averages given the coarse one; in the discrete case, a full-rank matrix condition.
- **Linear inverse problem** — recovering an unknown function from equations that only give its weighted averages; often unstable without regularization.
- **Tikhonov penalty** — a ridge-style penalty on series coefficients that stabilizes an ill-posed inverse problem.
- **Efficient influence function** — the first-order "sensitivity" of the target; building an estimator from it removes first-order nuisance bias and, under conditions, achieves the lowest possible asymptotic variance.
