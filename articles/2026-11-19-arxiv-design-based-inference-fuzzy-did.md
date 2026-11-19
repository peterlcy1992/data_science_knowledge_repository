---
id: arxiv-design-based-inference-fuzzy-did
title: "Design-Based Inference for Fuzzy Difference-in-Differences"
source: "Picchetti (PUC-Chile) (arXiv econ.EM / stat.ME)"
url: "https://arxiv.org/abs/2611.24402"
published: "2026-11"
added: "2026-11-19"
category: experimentation-causal
tags: [difference-in-differences, fuzzy-did, design-based-inference, instrumental-variables, weak-instruments, anderson-rubin, sensitivity-analysis, noncompliance]
novelty: 3
sourced_via: "full-text fetch"
---

# Design-Based Inference for Fuzzy Difference-in-Differences

**Source:** [Picchetti (PUC-Chile) (arXiv econ.EM / stat.ME)](https://arxiv.org/abs/2611.24402) · Published 2026-11 · Added 2026-11-19
**Category:** Experimentation & Causal Inference · **Tags:** `difference-in-differences`, `fuzzy-did`, `design-based-inference`, `instrumental-variables`, `weak-instruments`, `anderson-rubin`, `sensitivity-analysis`, `noncompliance`

## TL;DR

In fuzzy DiD a policy changes the incentive to take a treatment, but take-up is imperfect. Treating only the policy assignment as random, with heterogeneous unknown probabilities, the Wald-DiD estimand equals an assignment-weighted complier effect plus contamination from switchers, drifting always-taker effects and untreated trends. The paper gives a necessary-and-sufficient condition for a clean interpretation, a weak-IV-robust Anderson–Rubin test, and a breakdown-value sensitivity analysis. It is illustrated on the Oregon Medicaid lottery.

## 1. Business context

Many DiD analyses are "fuzzy". A rollout changes eligibility or incentives, some exposed units don't take the treatment, and some unexposed units take it anyway. Examples include feature availability with opt-in adoption, region-level policy changes, and encouragement designs. The standard estimator is the Wald-DiD ratio: DiD in outcomes divided by DiD in treatment rates. In the usual sampling framework, de Chaisemartin & D'Haultfœuille (2018) showed it identifies a LATE only under strong homogeneity assumptions. This paper follows the design-based turn (Rambachan & Roth, 2026): potential outcomes are fixed, and only the policy assignment is random with unit-specific, possibly unknown probabilities.

## 2. Technical details

- **Setup.** A two-period balanced panel, with a policy available in period 1 and treatment monotone in assignment and time. Units are never-takers, always-takers, compliers, or **switchers** (adopt in period 1 regardless of assignment).
- **Decomposition.** The Wald-DiD design estimand = an **assignment-probability-weighted complier effect** + three contamination terms: switchers' effects, the change over time in always-takers' effects, and untreated-outcome trends. Each enters through its **finite-population covariance with the assignment probabilities**, and all vanish under complete randomization.
- **Interpretation condition.** The estimand equals the weighted complier effect iff the assignment probabilities are uncorrelated with a single **contamination index**. This is necessary and sufficient, and strictly weaker than design-based parallel trends in both outcomes and treatment.
- **Inference.** An Anderson–Rubin-type test based on a difference in means of the null-adjusted outcome change, with a conservative Neyman variance (its slack is characterized). It is valid under rejective sampling regardless of first-stage strength. Inverting it gives Fieller-type sets, which are unbounded exactly when the first stage is insignificant.
- **Sensitivity.** Bounds on the two contamination covariances give a closed-form identified set and a weak-IV-robust confidence set. Whether a complier effect exists depends only on the reduced-form contamination, which yields a **breakdown value**. When assignment probabilities are known (stratified experiments, lotteries), the contamination is estimable and the complier effect is point-identified.

## 3. Impact — potential & realized

**Measured:**
- **Simulations** redraw only the assignment 5,000 times from a fixed finite population. Coverage is close to nominal: for example, 0.96 for the AR and sensitivity sets in the reported design D1 with N = 1,000.
- **Oregon Health Insurance Experiment** (24,615 individuals in 22,159 households; Medicaid application rights allocated by lottery). Selection probabilities differed by number of household members on the list (0.344 / 0.571 / 0.885), and 15.1% of non-selected people enrolled (switchers). The first stage is 0.241. For ED visits per year, the stratified complier effect is **0.292 (SE 0.077)**, against a non-selected mean of 0.64, while the pooled Wald-DiD gives 0.266 (0.077). Estimated contamination is small, and the breakdown value (0.028) is about four times the estimated reduced-form contamination. An analyst who didn't know the design but bounded contamination at a few hundredths of a visit would still correctly conclude that Medicaid increases ED use among compliers.

**Potential:** principled inference for rollout and encouragement designs with imperfect compliance and uneven exposure probabilities. Staggered adoption, clustered assignment and covariate adjustment are listed as next steps.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Makes fuzzy DiD's hidden assumptions a single, checkable covariance

The useful idea for applied teams is that every way fuzzy DiD can go wrong collapses into one question: do the units more likely to be exposed differ in a single contamination index? A breakdown value then tells you how much such correlation would overturn the sign. That's a sensitivity statement stakeholders can understand. Weak-IV-robust inference matters in product settings where opt-in rates are low.

Limits: two periods, monotone treatment, no covariates yet, and an application that is a benchmark (known probabilities) rather than a true quasi-experiment.

### Similar / related work

- [**Positive Weights Do Not Certify TWFE Inference: A Design Diagnostic under Treatment-Effect Heterogeneity**](2026-11-16-arxiv-positive-weights-do-not-certify-twfe-inference.md) (in this bank) — another diagnostic of what DiD estimands actually identify under heterogeneity.
- [**Instrumental variables with treatment clusters**](2026-11-13-arxiv-instrumental-variables-treatment-clusters.md) (in this bank) — complier-effect interpretation of IV with many treatments.
- [**Fuzzy Differences-in-Differences**](https://arxiv.org/abs/1510.01757) — de Chaisemartin & D'Haultfœuille (2018), the sampling-based analysis this revisits.
- **Rambachan & Roth (2026), design-based quasi-experiments with unknown assignment probabilities** — the framework this extends to fuzzy designs.

### Jargon buster

- **Fuzzy DiD** — a difference-in-differences design where the policy shifts treatment take-up only partly, so you scale the outcome change by the take-up change.
- **Design-based inference** — treat potential outcomes as fixed and get all randomness from how treatment or policy was assigned.
- **Switchers** — units that take treatment in the second period whether or not the policy reached them.
- **Anderson–Rubin test** — a test for IV-type effects that stays valid even when the first stage (take-up response) is weak.
- **Breakdown value** — the amount of assumption violation needed to overturn a conclusion.
