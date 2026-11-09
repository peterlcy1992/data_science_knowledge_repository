---
id: doordash-power-optimal-cupac-switchback-experiments
title: "Power-Optimal Covariate Adjustment for Switchback Experiments"
source: "arXiv stat.ME (Sergei Pankratev, DoorDash)"
url: "https://arxiv.org/abs/2607.27376"
published: "2026-07"
added: "2026-11-09"
category: experimentation-causal
tags: [switchback, cupac, variance-reduction, marketplace-experiments, cluster-randomization]
novelty: 4
sourced_via: "full-text fetch"
---

# Power-Optimal Covariate Adjustment for Switchback Experiments

**Source:** [arXiv stat.ME (Sergei Pankratev, DoorDash)](https://arxiv.org/abs/2607.27376) · Published 2026-07 · Added 2026-11-09
**Category:** experimentation-causal · **Tags:** `switchback`, `cupac`, `variance-reduction`, `marketplace-experiments`, `cluster-randomization`

## TL;DR

In switchback experiments (randomization unit = region x time window) with unequal cell sizes, power is governed by between-cell variance, yet standard CUPAC trains its control variate on unit-level MSE and estimates the adjustment coefficient with unit-level OLS. The paper derives a composite training loss and a matched analysis-time coefficient that re-weight the between-cell component, and validates them in Monte Carlo simulation only.

## 1. Business context

Switchback experiments are a standard design for marketplace features where user-level randomization would suffer interference. The randomization unit is a spatial cluster crossed with a time window (a 'cell'), and cells vary widely in event counts. The author argues the resulting between-cell variation, not within-cell idiosyncratic noise, dominates the variance of the treatment-effect estimator, so power is limited. Variance reduction by CUPED/CUPAC is a mature tool in standard A/B tests, but its default form was developed for independent user-level randomization.

## 2. Technical details

CUPED adjusts the outcome with a pre-experiment covariate; CUPAC replaces it with a machine-learned prediction of the outcome. The paper decomposes the variance of the switchback treatment-effect estimator exactly into a within-cell and a between-cell part. Because the design averages away within-cell noise inside each cell but cannot average away between-cell variation, the between-cell part governs power, and its weight relative to the within-cell part grows with mean cell size and cell-size imbalance. The author proves that the two default stages (a unit-level MSE-trained covariate and the unit-level OLS coefficient) each under-weight this macro component by a factor of 1 + n-bar(1 + cv^2), where n-bar is mean cell size and cv the coefficient of variation of cell size, which the paper says is typically two to three orders of magnitude. The proposed framework replaces both stages: a power-optimal composite loss (shown to be a tight upper bound on the deployed variance, with gradient-Hessian and closed-form Ridge formulations) that up-weights between-cell error, and a design-weighted adjustment coefficient estimated under the same loss. Practical caveats the paper names: bias of the between-cell target in small cells and overfitting risk from concentrating the objective on a limited number of cells. Per the paper, splitting the macro term further (cluster, time of day, interaction) gives no additional benefit because the sub-components share the same multiplier.

## 3. Impact — potential & realized

Realized (as reported): validation is a Monte Carlo simulation study across designs from balanced to heavily within-cell-dominated; the aligned framework recovers substantial power where the theory predicts (as within-cell noise dominates) and adds little where standard CUPAC already suffices. The paper explicitly leaves validation on production metrics and integration into a production training workflow to future work, so no production gains are claimed. Where gains are expected: metrics with large within-cell noise (low intraclass correlation) and high cell density. The paper notes that with ample model capacity (e.g. boosted trees without depth limits or early stopping) the covariate can drive both loss components toward their floor, and all reasonable losses converge to the same variance reduction; the benefit is then training efficiency. Potential: a drop-in change to how control variates are trained and applied for any switchback or cluster-randomized program.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — practical and well-evidenced

A neat, well-argued point: when the analysis unit and the randomization unit differ, the variance-reduction objective should follow the design. The 1 + n-bar(1 + cv^2) factor is an intuitive diagnostic of how much standard CUPAC is mis-aimed. The main limit is evidentiary: simulation only, a single-author working paper, and with flexible models the gap may close. Worth testing by any marketplace team running switchbacks.

### Similar / related work

- [**Regression Adjustment for Ratios of Treatment Effects in Randomized Experiments**](2026-10-27-arxiv-regression-adjustment-ratios-treatment-effects.md) (in this bank) — regression adjustment in randomized experiments
- [**Higher-Order Asymptotics of Regression-Adjusted Estimators in Randomized Trials**](2026-10-26-arxiv-higher-order-regression-adjustment-rct.md) (in this bank) — theory of regression-adjusted estimators
- **Bojinov, Simchi-Levi and Zhao 2023 'Design and analysis of switchback experiments'** — switchback design and analysis (Management Science)
- [**Guo et al. 2021 'Machine learning for variance reduction in online experiments'**](https://arxiv.org/abs/2106.07263) — ML control variates

### Jargon buster

- **Switchback experiment** — Randomizing whole region-by-time-window cells between treatment and control, used when users interfere with each other.
- **CUPAC** — CUPED where the covariate is a machine-learned prediction of the outcome.
- **Between-cell variance** — Variation in cell-level means across cells, which a switchback cannot average away within a cell.
