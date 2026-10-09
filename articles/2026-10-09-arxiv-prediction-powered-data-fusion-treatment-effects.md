---
id: arxiv-prediction-powered-data-fusion-treatment-effects
title: "Prediction-Powered Data Fusion for Treatment Effect Estimation"
source: "arXiv stat.ML (Yonghan Jung, Shu Yang)"
url: "https://arxiv.org/abs/2610.12332"
published: "2026-10"
added: "2026-10-09"
category: experimentation-causal
tags: [data-fusion, rct-plus-observational, prediction-powered-inference, cate, aipw]
novelty: 3
sourced_via: "web search"
---

# Prediction-Powered Data Fusion for Treatment Effect Estimation

**Source:** [arXiv stat.ML (Yonghan Jung, Shu Yang)](https://arxiv.org/abs/2610.12332) · Published 2026-10 · Added 2026-10-09
**Category:** experimentation-causal · **Tags:** `data-fusion`, `rct-plus-observational`, `prediction-powered-inference`, `cate`, `aipw`

## TL;DR

Small RCTs are unbiased but imprecise; large observational datasets are precise but possibly confounded. The paper proposes a fusion framework that keeps the RCT estimate unbiased, assumes nothing special about the observational data, and uses it only to gain precision, giving AIPW-Fusion (ATE) plus DR-Fusion and R-Fusion (CATE learners).

## 1. Business context

Product and clinical teams often have a small randomized experiment and a large pile of observational logs. Existing combination methods either assume the observational data are unconfounded, use them too conservatively, or trade bias for variance. A method that cannot be worse in bias than the RCT alone is attractive.

## 2. Technical details

Following prediction-powered inference, the observational data inform a prediction/adjustment component while the RCT anchors identification, so unbiasedness comes from randomization alone. Outputs per the abstract: AIPW-Fusion, an ATE estimator with closed-form weights and confidence intervals, and two CATE learners, DR-Fusion and R-Fusion. The authors say experiments support the findings and link code (CausalDataScience/DataFusionPPI on GitHub). The abstract page reports no effect sizes or datasets.

## 3. Impact — potential & realized

Realized: not quantified in the abstract. Potential: tighter confidence intervals from existing observational logs without new traffic, extended to heterogeneous effects (CATE), which earlier fusion work covered less.

*Sourced from the arXiv abstract page; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid methodological addition; wins come from the 'no confounding assumption needed' guarantee.

This sits in the same family as the Airbnb gift-card fusion paper in this bank, but with a different safety argument: there the invariance assumption does the work, here randomization does and the observational data can only help precision. The practical caveat is that gains depend on how predictive the observational data are of RCT outcomes. Likely adopters: teams with lots of logs and expensive experiments.

### Similar / related work

- [**Measuring Gift Card Program Incrementality via Causal Data Fusion**](2026-10-07-arxiv-airbnb-gift-card-incrementality-data-fusion.md) (in this bank) — fusion with an invariance assumption; 
- [**Augmented Hypothesis Testing with Persona-Based LLM Simulations**](2026-09-25-amazon-ppi-persona-llm-ab-testing.md) (in this bank) — another prediction-powered inference use; 
- [**Variance reduction combining pre-experiment and in-experiment data**](2026-10-08-etsy-variance-reduction-pre-and-in-experiment-data.md) (in this bank) — variance reduction via extra covariates; 

### Jargon buster

- **Prediction-powered inference** — Use a (possibly imperfect) predictive model on abundant data to tighten estimates, with a correction from gold-standard data so validity is preserved.
- **AIPW** — Augmented inverse-probability weighting: a doubly robust estimator combining an outcome model and propensity weights.
- **CATE** — Conditional average treatment effect: the treatment effect for a subgroup defined by covariates.
