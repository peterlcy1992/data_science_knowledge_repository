---
id: arxiv-when-listwise-deletion-works-causal-diagrams-complete-case
title: "When Listwise Deletion Works: Causal Diagrams and Complete-Case Regression"
source: "arXiv stat.ME (Wenxin Lin & Shiyao Liu, Peking University)"
url: "https://arxiv.org/abs/2611.04366"
published: "2026-11"
added: "2026-11-04"
category: statistical-modeling
tags: [missing-data, listwise-deletion, causal-dag, complete-case, ipw, adjustment-criterion]
novelty: 3
sourced_via: "full-text fetch"
---

# When Listwise Deletion Works: Causal Diagrams and Complete-Case Regression

**Source:** [arXiv stat.ME (Wenxin Lin & Shiyao Liu, Peking University)](https://arxiv.org/abs/2611.04366) · Published 2026-11 · Added 2026-11-04
**Category:** statistical-modeling · **Tags:** `missing-data`, `listwise-deletion`, `causal-dag`, `complete-case`, `ipw`, `adjustment-criterion`

## TL;DR

Most applied studies drop rows with missing values rather than impute. The paper asks when complete-case regression still consistently estimates the average treatment effect, and gives two checks: whether the covariates plus a missingness indicator satisfy the adjustment criterion in an augmented causal DAG, and whether the estimator pools within-covariate comparisons appropriately (possibly with inverse treatment-propensity weights). It argues that a missing-at-random (MAR) label alone does not settle this.

## 1. Business context

Missing data is routine in observational causal work. The authors' review of APSR and AJPS articles finds that at least 47 of 100 eligible APSR and 33 of 58 eligible AJPS articles state or imply listwise deletion (LWD), versus only 7 and 4 describing an imputation model (counts are lower bounds). Imputation guidance is framed around MAR/MNAR classes, which does not tell a practitioner whether simply dropping incomplete rows is safe for a causal target. The same question arises for any analyst fitting a regression on a table with gaps.

## 2. Technical details

Benchmark: an oracle regression, assumed to consistently estimate the population ATE if all required values were observed. Method: augment the causal DAG for (outcome, treatment, covariates) with an omnibus missing indicator M and its causes, including unobserved ones; conditioning on M=0 is selection on an observed indicator and can open non-causal paths (collider paths). Proposition 1: if {X, M} satisfies the adjustment criterion (and overlap holds), within-covariate-stratum complete-case comparisons identify stratum-specific effects. Proposition 2: with a correctly specified complete-case conditional mean, unweighted complete-case regression consistently estimates the complete-case ATE. Proposition 3: a graphical criterion for complete-case IPW regression. For heterogeneous effects, assuming conditional effects carry over to the population, comparisons are reweighted to the population covariate distribution. A motivating simulation (20,000 oracle observations, 500 replications, constant effect tau=1) compares oracle, multiple imputation under MAR, complete-case and complete-case with IPW across three missingness mechanisms (A, B, C) that are all not-MAR yet differ in validity.

## 3. Impact — potential & realized

Realized (per the paper): simulations and empirical illustrations from American politics, comparative politics and international relations show how the checks are applied; in the motivating simulation all three mechanisms are not-MAR with the same missing pattern, yet ordinary complete-case regression is consistent under A, under B saturating X or using treatment IPW fixes the pooling problem, and under C neither fixes the invalid within-X comparisons - so the NMAR label alone does not separate them. The framework is also said to reconcile differing recommendations of Pepinsky (2018) and Arel-Bundock & Pelc (2018). Recommendation: add the missing indicator and its causes to the causal model, then check adjustment and weighting for LWD. Potential: a quick pre-flight check before reaching for imputation; the results are conditional on the stated causal assumptions and on the oracle regression being valid.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A usable DAG-based check for when dropping incomplete rows is safe

Practical and well-motivated: it replaces the blunt 'is it MAR?' question with a DAG check on the missing indicator, which working analysts can actually do. It rests on strong, untestable causal assumptions about what causes missingness, and the empirical illustrations are from political science rather than product data. The authors disclose AI-assisted drafting and coding, taking responsibility for the content.

### Similar / related work

- Pepinsky (2018) and Arel-Bundock & Pelc (2018) - competing guidance on listwise deletion in regression, which the paper reconciles; not in this bank
- Hernan & Robins (2020) - the inverse-probability-weighting pseudo-population idea the paper applies among complete cases
- [Studentized inference in randomized experiments when a few units dominate the outcome variation](2026-11-03-arxiv-studentized-inference-few-units-dominate-randomized-experiments.md) (in this bank) - another statistical-practice paper on when a default analysis choice is safe

### Jargon buster

- **Listwise deletion** — Dropping every row that has any missing value in the variables used by the model (complete-case analysis).
- **Missing at random (MAR)** — Missingness depends only on observed data; the standard condition for valid imputation, but not sufficient on its own for valid complete-case causal estimates.
- **Adjustment criterion** — A graphical condition under which conditioning on a variable set removes confounding and blocks no causal paths.
- **Collider** — A variable with two arrowheads pointing into it; conditioning on it can create spurious associations.
