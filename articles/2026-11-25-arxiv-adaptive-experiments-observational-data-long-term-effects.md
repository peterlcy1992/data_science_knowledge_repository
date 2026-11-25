---
id: arxiv-adaptive-experiments-observational-data-long-term-effects
title: "Adaptive experiments with observational data: Efficient experimental design and asymptotic time-uniform inference for long-term treatment effects"
source: "Graduate School of Economics, The University of Tokyo (arXiv econ.EM)"
url: "https://arxiv.org/abs/2611.30595"
published: "2026-11"
added: "2026-11-25"
category: experimentation-causal
tags: [long-term-effects, surrogate-index, data-combination, adaptive-experiments, neyman-allocation, experimental-design, confidence-sequences, anytime-valid, efficient-influence-function]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "arXiv listing (backlog stub)"
---

# Adaptive experiments with observational data: Efficient experimental design and asymptotic time-uniform inference for long-term treatment effects

**Source:** [Graduate School of Economics, The University of Tokyo (arXiv econ.EM)](https://arxiv.org/abs/2611.30595) · Published 2026-11 · Added 2026-11-25
**Category:** Experimentation & Causal Inference · **Tags:** `long-term-effects`, `surrogate-index`, `data-combination`, `adaptive-experiments`, `neyman-allocation`, `experimental-design`, `confidence-sequences`, `anytime-valid`, `efficient-influence-function`

## TL;DR

In surrogate-index setups, an observational sample links short-term surrogates to the long-term outcome, and an experiment records only the surrogates. This paper uses that pre-existing observational data to *design* the experiment as well as to identify the effect. Minimizing the efficiency bound gives a Neyman-style assignment rule and a covariate sampling rule. Both depend on how variable the *surrogate index*, not any single short-term outcome, is within each arm. A sequential procedure learns this design during the experiment and attains the oracle variance. An asymptotic confidence sequence allows checking after every participant and stopping early. In a coupon-style simulation, the learned design cuts Monte Carlo variance by 13.1% against a 50/50 baseline. A design built on immediate purchases instead raises it by 9.8%.

## 1. Business context

Long-term outcomes take time to observe, which delays evaluation and decisions. The paper's running example is a marketer offering coupons to new customers. The marketer cares about sustained purchasing, not just immediate purchases. Historical customer records may link early behaviour (purchase frequency, spending, composition) to later purchasing. The author notes that the same idea extends to education, labour and development.

The surrogate index of Athey et al. (2026) combines the two sources. The experiment shows how treatment moves short-term surrogates S. The observational data show how the long-term outcome Y relates to S and covariates X. Chen & Ritzwoller (2023) derive the efficiency bound for this setting. This paper asks the next question: *given* observational data available before the experiment, whom should the experiment recruit, and how should it assign treatment, to estimate the long-term effect most precisely? Because participants arrive over time and surrogates are observed quickly, the design can be learned sequentially. An experimenter would also like to stop once the evidence is clear, since recruitment and measurement cost money.

## 2. Technical details

- **Data and target.** The observational sample records (X, S, Y). The experiment records (X, W, S). No sample has all of W, S and Y. The target is τ = E[Y(1) − Y(0) | observational population].
- **Assumptions.** Consistency, conditional randomization in the experiment, statistical surrogacy (W ⟂ Y | S, X in the experiment), conditional external validity, conditional outcome comparability across samples, and overlap/positivity/surrogate support. These follow Chen & Ritzwoller and Athey et al. Theorem 2.1 restates known identification results, including an augmented (doubly robust–style) representation used for estimation.
- **Efficiency bound as a function of the design (Theorem 3.1).** On the √N_E scale, the bound is V^exp(f_X|E, p) + κ·V^obs, where κ = lim N_E/N_O.
  - Only V^exp depends on the design. It is the target-weighted average of (f_X|O/f_X|E)·{v₁(x)/p(x) + v₀(x)/(1−p(x))}.
  - v_w(x) is the conditional variance of the surrogate index μ(S, X) within arm w.
  - The bound coincides with Chen & Ritzwoller's pooled bound after rescaling.
- **Optimal fixed design (Theorem 3.2).**
  - *Assignment:* p*(x) = √v₁(x) / (√v₁(x) + √v₀(x)). This is Neyman allocation on the surrogate index.
  - *Sampling:* f*_X|E(x) ∝ f_X|O(x)·(√v₁(x) + √v₀(x)). It oversamples covariate regions that are common in the target and where the index is more variable. The estimator reweights by the density ratio.
  - The minimum is V^exp,* = {E[√v₁ + √v₀ | O]}².
  - The closest design counterpart is Kato et al. (2024), who jointly optimize sampling and assignment when the outcome is observed in the experiment.
- **Why the surrogate index, not a short-term outcome.** In the coupon story, the variance ordering between arms for immediate purchases can be the *opposite* of that for the surrogate index within the same usage stratum. A design that optimizes a convenient short-term endpoint can then push allocation the wrong way.
- **Sequential procedure (Algorithm 5).**
  - Before the experiment, the observational sample is used to estimate the target covariate density and the surrogate index. These fits stay fixed.
  - Before each round, earlier participants are used to estimate the arm-specific mean and variance of the fitted index. These are plugged into p* and f*, and the round's score is computed from pre-round quantities only.
  - This predictability makes the experimental error a martingale average (Lemma 6.1). The observational sample is placed at the start of the history so that one martingale CLT covers both error sources.
  - The surrogate representer α (a density ratio) can be estimated directly or via four classification probabilities (Remark 5.2).
- **Asymptotic normality (Theorem 6.1).** √N_E(τ̂ − τ) → N(0, V^exp,* + κV^obs) under DML-style product-rate conditions, with time-averaged consistency of the learned variances. Learning the design does not increase the limiting variance relative to an oracle that knew the optimal design.
- **Asymptotic confidence sequence (Theorem 7.1, Corollary 7.1).**
  - The interval is τ̂_t ± σ̂_t·h_α(ω/σ̂²_t), with σ̂²_t = V̂^exp_t/t + V̂^obs/N_O. It uses the two-sided normal-mixture boundary from Ville's inequality (Howard et al., 2021).
  - The key difficulty is that the observational error is *shared* across all monitoring times. The standardized errors behave like one Brownian motion.
  - Coverage holds simultaneously for all t ≥ a prespecified start t₀ (e.g. ⌈N_O^{3/4}⌉). It has an asymptotic lower limit ≥ 1 − α and extends to data-dependent stopping, such as "stop when the interval excludes zero."
  - The tuning variable ω is chosen once at t₀ to make the interval narrowest at a target round (Remark 7.1). Coverage holds for any valid choice.
  - Remark 7.2 links how late monitoring must start to the nuisance-estimation rates.

## 3. Impact — potential & realized

**Measured (Monte Carlo, coupon-style DGP).**
- *Setup.* X is prior usage; S⁽¹⁾ is immediate purchases, S⁽²⁾ short-term repeat purchases, and Y long-term cumulative purchases. Y = S⁽¹⁾ + 4S⁽²⁾ + X + noise, and τ = 1, about 0.08 SD. N_O = 5,000 and up to N_E = 5,000, with 2,000 replications.
- The design is constructed so that the S⁽¹⁾ and surrogate-index criteria push assignment in opposite directions.
- Feasible designs use 15 strata and an initial 50/50 period of at least 200 participants. The SI joint design's first adaptive round has median 518.
- *At 5,000 participants*, bias is near zero and 95% coverage is 95.1–96.4% for every design. MC variance vs baseline:
  - S⁽¹⁾ joint design: **+9.8%** (population benchmark +4.1%);
  - S⁽²⁾ joint: −12.7%; surrogate-average joint: −11.2%;
  - SI assignment-only: +1.1%; SI sampling-only: −13.2%; SI joint: **−13.1%** (benchmark −17.9%); stratified-oracle SI joint: −13.1%.
  - Sampling, not assignment, drives most of the gain. The SI joint design has 20.8% smaller variance than the S⁽¹⁾ joint design.
- *Sequential monitoring (90% time-uniform interval, t = 595…5,000).*
  - Simultaneous coverage is 95.2–96.4% for all designs, above the nominal 90%.
  - The SI joint design raises detection from 95.4% to 98.2%. It cuts mean stopping size from 2,062.4 to 1,846.1 and the median from 1,727.0 to 1,564.5.
  - The S⁽¹⁾ joint design is worse than baseline: 94.6% detection and a mean stop of 2,090.1.
  - Coverage stays above nominal under other target rounds (95.0–97.1%) and planning values.

**Measured (retrospective design illustration, Pakistan Graduation experiment).**
- *Data.* 854 households (446 treated, 408 control) from Banerjee et al. (2015), using Chen & Ritzwoller's cleaned data. S is 21 two-year variables; Y is monthly consumption per capita at three years; X is 20 pretreatment variables.
- *Method.* There are 1,000 treatment-stratified splits into 427 + 427 households, with W masked in one half and Y in the other. The designs are constant within five quantile strata of a single covariate. Assignment is clipped to [0.1, 0.9] and the density ratio to [1/5, 5].
- *Household asset index:* the joint design cuts the plug-in variance criterion by **8.23%** on average (median 4.91%). This is mostly through sampling: 262 instead of 200 households per 1,000 from the top stratum, with a median density ratio of 1.24, above 1 in 98% of splits.
- *Monthly nonfood consumption:* a 7.72% mean reduction, mainly through assignment. The second stratum assigns 131 of 207 households to treatment, with a median p of 0.61, above ½ in 97% of splits.
- These reductions are in-sample plug-in criterion values, non-negative by construction, not realized variance from a new experiment.

**Potential.** The paper gives a recipe for planning a short-term experiment whose purpose is a long-term effect: learn where the surrogate index is noisy, then oversample and Neyman-allocate there. It also allows continuous monitoring with early stopping while keeping asymptotic coverage. The author notes the coverage guarantee is asymptotic, holds only after the prescribed start, and is a lower bound. Exact-level intervals are left open.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-built synthesis of surrogate-index efficiency, Neyman-style adaptive design and confidence sequences

Each ingredient is known. The bound is Chen & Ritzwoller's. Joint sampling-plus-assignment optimization mirrors Kato et al. (2024). The boundary is Howard et al.'s normal mixture, made asymptotic as in Waudby-Smith et al. The new work is in fitting them together where the observational data are reused in every round and its error is shared across monitoring times. Handling that carefully, with one martingale CLT and one Brownian-motion limit, is real technical work. The design insight is the most portable part: **optimize the experiment for the variance of the surrogate index, not of a headline short-term metric.** The coupon simulation shows how wrong the shortcut can go, with +9.8% variance.

Same author as yesterday's in-bank entry on what a short-term experiment should *measure* (Kentaro Kawato, University of Tokyo). Together they form a pair. That paper asks which variables to collect when the observational data are confounded. This one assumes statistical surrogacy holds and asks whom to recruit and how to assign treatment.

Practical caveats, in my view.
- Most of the simulated gain comes from *covariate sampling*. Many product experiments cannot choose whom they recruit, since traffic arrives as it does. Assignment-only gave roughly no gain there.
- The confidence sequence was conservative in simulation: about 95–96% coverage for a nominal 90%.
- The Graduation numbers are plug-in criterion reductions on a small completed trial, not realized savings.
- Everything rests on statistical surrogacy and cross-sample comparability, which remain untestable.

### Similar / related work

- [**What Should an Experiment Measure? Combining a Short-Term Experiment with Confounded Observational Data to Identify Long-Term Treatment Effects**](2026-11-24-arxiv-what-should-experiment-measure-long-term-effects.md) (in this bank) — same author; it covers the *measurement* side of design under latent unconfoundedness, where this paper covers sampling and assignment under statistical surrogacy.
- [**Long-Term Quantile Treatment Effects with Combined Experimental and Observational Data**](2026-11-18-arxiv-long-term-quantile-treatment-effects-combined-data.md) (in this bank) — same data-combination family, extended from averages to quantiles.
- [**Many Hands Make Light Work: Long-Term Effect Inference for the Experiment Reservoir**](2026-10-28-arxiv-experiment-reservoir-surrogate-long-term-effects.md) (in this bank) — a different route to long-term effects. It regresses long-term ATEs on short-term ATEs across a reservoir of past long-run experiments.
- [**Anytime-Valid Inference in Linear Models with Clustered Outcomes**](2026-10-20-arxiv-anytime-valid-clustered-linear-models.md) (in this bank) — confidence sequences for A/B tests, the monitoring tool adapted here to a two-sample, data-combination estimator.
- [**Efficient Adaptive Experimental Design for Average Treatment Effect Estimation**](https://arxiv.org/abs/2002.05308) — Kato, Ishihara, Honda & Narita; efficient estimation in multi-stage adaptive experiments, cited as part of the adaptive-design strand.
- **Semiparametric estimation of long-term treatment effects** — Chen & Ritzwoller (Journal of Econometrics 2023); source of the efficiency bound and of the cleaned Graduation data.

### Jargon buster

- **Surrogate index** — the predicted long-term outcome given short-term surrogates and covariates, learned from observational data.
- **Statistical surrogacy** — in the experiment, once you know the surrogates and covariates, treatment carries no extra information about the long-term outcome.
- **Neyman allocation** — assign more units to the arm whose outcome (here, the surrogate index) is more variable, in proportion to its standard deviation.
- **Sampling density ratio** — how much more or less often the experiment recruits a covariate type than the target population contains it; the estimator reweights by its inverse.
- **Predictable score** — each round's contribution is built only from information available before that participant arrives. This is what makes the errors a martingale despite the adaptivity.
- **Asymptotic confidence sequence** — a sequence of intervals that, in large samples, contain the true effect at *all* monitoring times at once, so peeking and early stopping keep coverage.
- **Ville's inequality** — a nonnegative martingale starting at 1 exceeds 1/α at any time with probability at most α. It is the basis for time-uniform bounds.
