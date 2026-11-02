---
id: arxiv-etz-counterfactual-individual-benefit-proportion-benefiting
title: "From Average Effects to Proportions Benefiting: A Tutorial on ETZ-Powered Counterfactual Individual Benefit Analysis"
source: "arXiv stat.ME (Wang, Han, Liu, Tang, Hsu)"
url: "https://arxiv.org/abs/2610.33600"
published: "2026-10"
added: "2026-11-02"
category: statistical-modeling
tags: [individual-treatment-effect, counterfactual, potential-outcomes, uncertainty-quantification, clinical-trials, heterogeneity]
novelty: 3
sourced_via: "full-text fetch"
---

# From Average Effects to Proportions Benefiting: A Tutorial on ETZ-Powered Counterfactual Individual Benefit Analysis

**Source:** [arXiv stat.ME (Wang, Han, Liu, Tang, Hsu)](https://arxiv.org/abs/2610.33600) · Published 2026-10 · Added 2026-11-02
**Category:** statistical-modeling · **Tags:** `individual-treatment-effect`, `counterfactual`, `potential-outcomes`, `uncertainty-quantification`, `clinical-trials`, `heterogeneity`

## TL;DR

Average treatment effects cannot answer 'do at least 80% of patients benefit by a meaningful margin?'; the answer also depends on response variability and the dependence between potential outcomes. The tutorial presents two metrics, the individual benefit probability and the individual benefit lower bound, with confidence-based decisions and type I error control, illustrated on a Phase II randomized trial.

## 1. Business context

Personalized medicine needs claims about how many individuals benefit, but conventional efficacy analyses compare means. The paper argues that even with the true mean effects known exactly, the answer to a proportion question could be yes or no, depending on variability in responses and dependence between each patient's potential outcomes. The same logic applies to product experiments where a positive average effect may hide many users who are worse off.

## 2. Technical details

The framework tests whether Pr(D>δ) ≥ β, where D is the benefit of Rx over C and δ a clinically meaningful margin, using the individual benefit probability p_ib and the individual benefit lower bound L, in both a factual random-pair setting and a counterfactual same-patient setting. The ETZ decomposition goes beyond a mixed-model repeated-measures split of between- vs within-patient variability by further separating within-patient uncertainty into before-treatment patient variability and after-treatment disease-trajectory variability; in the same-patient counterfactual estimand the common baseline measurement error cancels, reducing uncertainty. A Normal working model is adopted. The authors contrast it with optimal individualized treatment rules (which maximize conditional expected outcomes) and with conformal inference (intervals for a future patient's outcome or effect), and state the paper covers the overall population, not biomarker-defined subgroups.

## 3. Impact — potential & realized

Realized (per the paper): counterexamples show a favourable mean treatment effect can coexist with a much less favourable individual benefit probability, so a substantial share of patients may not benefit from the treatment a mean-based rule selects. The method is illustrated with patient-level data from the Phase II randomized trial in Schnell et al. (2017) and controls the incorrect-decision probability at a prespecified level. Potential: proportion-based efficacy claims and narrower confidence bounds when the Normal and ETZ assumptions hold; subgroup extensions are left to future work.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A tutorial rather than a new result, from a clinical-trial setting, but the core lesson transfers to experimentation: means do not identify the share of units helped, and the cross-world dependence is the unidentified part, so any such claim rests on modelling assumptions.

A tutorial rather than a new result, from a clinical-trial setting, but the core lesson transfers to experimentation: means do not identify the share of units helped, and the cross-world dependence is the unidentified part, so any such claim rests on modelling assumptions. Treat the narrower bounds as conditional on the Normal/ETZ model.

### Similar / related work

- **Conformal inference of counterfactuals and individual treatment effects (Lei & Candès)** — the interval-for-one-patient alternative the paper contrasts itself with
- [**Treatment Effect Modification by Latent Classes**](https://arxiv.org/abs/2610.10851) — heterogeneous effects from a different angle

### Jargon buster

- **Individual benefit probability** — Probability that a randomly chosen patient gains more than a margin δ from Rx versus C.
- **ETZ decomposition** — Splits within-patient outcome variability into pre-treatment variability and post-treatment trajectory variability.
- **Potential outcomes** — The outcomes a patient would have under each treatment; only one is ever observed.
