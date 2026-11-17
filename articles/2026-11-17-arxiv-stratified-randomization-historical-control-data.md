---
id: arxiv-stratified-randomization-historical-control-data
title: "Stratified Randomization Incorporating Historical Control Data"
source: "Hokkaido University / HHU Düsseldorf (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.17875"
published: "2026-11"
added: "2026-11-17"
category: experimentation-causal
tags: [hybrid-control, historical-controls, stratified-randomization, covariate-adaptive-randomization, borrowing, propensity-score-matching, effective-sample-size, trial-design]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "catalog backlog (arXiv stat.ME scan)"
---

# Stratified Randomization Incorporating Historical Control Data

**Source:** [Hokkaido University / HHU Düsseldorf (arXiv stat.ME)](https://arxiv.org/abs/2611.17875) · Published 2026-11 · Added 2026-11-17
**Category:** Experimentation & Causal Inference · **Tags:** `hybrid-control`, `historical-controls`, `stratified-randomization`, `covariate-adaptive-randomization`, `borrowing`, `propensity-score-matching`, `effective-sample-size`, `trial-design`

## TL;DR

A stratified block randomization for hybrid-control trials that uses historical controls at the *allocation* stage: within each stratum, over-allocate concurrent subjects to treatment and fill the gap with historical controls so treatment and hybrid control are 1:1, reverting to 1:1 once the stratum's historical supply or a trial-wide cap is used up. In simulation, the sampling variant kept type I error without heterogeneity or unmeasured covariates and matched or beat propensity score matching on power, especially when historical controls were unevenly spread across strata.

## 1. Business context

RCTs are often infeasible in rare diseases (small eligible populations, cost, duration). Hybrid designs add historical controls from earlier trials or real-world data to a concurrent control arm. Existing approaches such as propensity score matching borrow only at the analysis stage with a fixed allocation ratio, discarding unmatched historical controls and leaving arms imbalanced within strata when historical controls are unevenly distributed. Approaches that adapt the ratio to outcome commensurability depend on accumulated outcomes, raising the temporal-trend and type I error concerns of response-adaptive randomization. The analogue for product teams is borrowing past control data (or holdouts) to shrink a concurrent control arm.

## 2. Technical details

- **Allocation.** K strata from observed baseline factors; stratum quota h_k historical candidates; borrowed b_k ≤ h_k, total b ≤ trial-wide cap b^max. Blocks in strata with available historical controls assign more concurrent subjects to treatment than to concurrent control (simulated block parameters (r,s)=(4,1)); historical controls fill the hybrid control arm so it is 1:1 with treatment within stratum. When the quota or cap is reached, allocation returns to 1:1.
- **Covariate-adaptive, not response-adaptive.** Allocation depends on strata and historical availability only, so model-assisted estimators with large-sample theory under covariate-adaptive randomization apply.
- **Two ways to use historical controls.** *Sampling* draws b_k historical controls per stratum; *weighting* uses all h_k with weight w_k = b_k/h_k. Weighting's effective sample size (n_C + Σh_k w_k)² / (n_C + Σ b_k²/h_k) is ≥ the sampling ESS n_C + b and grows with the historical pool.
- **Simulation.** Seven scenarios: ideal alignment; lack of strata support in historical or concurrent data; measured covariate shift; unmeasured covariate shift; effect-modification heterogeneity; stratification factors dichotomized from continuous covariates. Concurrent n = 120, cap 40, continuous outcome, three strong stratification factors; compared against PSM with fixed 2:1 allocation.

## 3. Impact — potential & realized

**Measured (simulation):**
- Sampling method: maintained type I error when there was neither outcome-model heterogeneity nor unmeasured covariates; power comparable to or greater than PSM, particularly when historical controls were unevenly distributed across strata (Scenarios 2–3, where fixed 2:1 PSM could not match borrowed controls to the strata that needed them).
- Weighting method: power increased with pooled historical size, but type I error was inflated when covariates beyond the stratification factors were present or when strata were dichotomized from continuous covariates (Scenarios 4 and 7; Scenario 7 also lost power).
- Unmeasured confounding and differing covariate effects (Scenarios 5–6) inflated type I error for *all* borrowing methods, PSM included; the cap b^max limits the size of that bias.
- Limitations stated: one concurrent size, one cap and block setting, one effect size, continuous outcome only; the exchangeability assumption is unverifiable; no guidance yet on choosing b^max.

**Potential:** a simple design-stage lever to save concurrent controls when historical data exist, with a built-in bound (the cap) on how much a bad historical cohort can hurt.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Move borrowing upstream, keep it covariate-adaptive

The idea is simple and sensible: if you know where historical controls are plentiful, randomize fewer concurrent patients to control there. Keeping allocation outcome-blind sidesteps the response-adaptive pitfalls. The evidence is a narrow simulation grid, and the weighting variant's type I error inflation is a warning that "more borrowing" quietly leans on stratification being sufficient. For online experimentation, the same trade-off appears whenever teams want to reuse long-running holdouts as controls.

### Similar / related work

- [**Covariate-adaptive randomization using historical data and bootstrap-based inference**](2026-10-20-arxiv-covariate-adaptive-randomization-historical-data.md) (in this bank) — another design that uses historical data during allocation.
- [**Randomization protects the average, not the trial**](2026-11-17-arxiv-randomization-protects-average-chance-covariate-imbalance.md) (in this bank) — why within-stratum balance and pre-specified adjustment matter.
- Hybrid control / external control literature (Pocock 1976 onward) — the borrowing designs this extends.

### Jargon buster

- **Hybrid control arm** — a control group combining concurrently randomized controls with controls from historical data.
- **Stratum quota** — how many historical controls are available in a given stratum.
- **Covariate-adaptive randomization** — allocation probabilities depend on baseline characteristics, never on observed outcomes.
- **Effective sample size** — the number of unweighted observations that would carry the same information as a weighted sample.
