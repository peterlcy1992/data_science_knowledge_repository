---
id: arxiv-conformal-policy-selection-fdr-deployment
title: "Conformal Policy Selection: When to Deploy AI Decisions for Targeted Intervention"
source: "arXiv stat.ME (Cao, Gao, Saar-Tsechansky & Yin)"
url: "https://arxiv.org/abs/2610.22930"
published: "2026-10"
added: "2026-10-19"
category: experimentation-causal
tags: [conformal, fdr, off-policy, targeting, doubly-robust]
novelty: 4
sourced_via: "web search"
---

# Conformal Policy Selection: When to Deploy AI Decisions for Targeted Intervention

**Source:** [arXiv stat.ME (Cao, Gao, Saar-Tsechansky & Yin)](https://arxiv.org/abs/2610.22930) · Published 2026-10 · Added 2026-10-19
**Category:** experimentation-causal · **Tags:** `conformal`, `fdr`, `off-policy`, `targeting`, `doubly-robust`

## TL;DR

Instead of asking whether an AI targeting policy is better on average, Conformal Policy Selection decides unit by unit where to deploy it, treating each decision as a hypothesis test and controlling the false discovery rate among the units selected.

## 1. Business context

Targeted interventions (treatments, offers, outreach) are usually approved on average uplift, which can hide a subpopulation where a globally trained policy generalizes badly and does harm. The paper frames deployment as a per-individual safety question: for which units can we be confident the outcome under the AI policy exceeds a user-specified threshold?

## 2. Technical details

For each candidate unit the method tests whether the outcome under the target (AI) policy exceeds a threshold. It builds **weighted conformal p-values** that correct for distribution shift from the behavior policy that generated the data to the target policy, then applies a two-step selection-and-pruning procedure to control FDR over the selected set. The authors prove finite-sample FDR control and a **doubly robust** asymptotic guarantee: FDR is controlled if either the outcome model or the propensity model is correctly specified. Detailed algorithm steps were not read (abstract-level).

## 3. Impact — potential & realized

Realized (as reported in the abstract): synthetic experiments confirm the guarantees across four misspecification regimes; a semi-synthetic study on real electronic-health-record covariates shows FDR control acting as a deployment safety gate that stops a globally trained policy from giving harmful treatments to a high-risk subpopulation where it generalizes poorly. No numeric results were available to me. Potential: a statistically principled go/no-go gate for personalized offers, notifications or clinical-style interventions.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Treating per-unit deployment as multiple testing with FDR control is a neat reframing: it turns 'is the model good on average?' into a calibrated list of units where it is safe to act.

Treating per-unit deployment as multiple testing with FDR control is a neat reframing: it turns 'is the model good on average?' into a calibrated list of units where it is safe to act. Weighted conformal under policy shift plus a doubly robust guarantee is a real combination, though conformal and FDR ideas are individually established. Caveat: abstract-level read; practical power (how many units survive selection) is unknown.

### Similar / related work

- [**Covariance-Calibrated Prediction-Powered Inference**](2026-10-16-arxiv-covariance-calibrated-prediction-powered-inference.md) (in this bank) — another recent stat.ME piece on valid inference with model-generated quantities
- [**Probabilistic Forecasting of Electric Vehicle Charging in a Time-varying Hierarchical Infrastructure**](2026-10-15-arxiv-conformal-hierarchical-ev-charging-forecast.md) (in this bank) — conformal machinery applied to forecasting rather than decisions
- [Conformal prediction under covariate shift](https://arxiv.org/abs/1904.06019) — Tibshirani et al.: the weighted-conformal foundation this builds on

### Jargon buster

- **FDR (false discovery rate)** — The expected share of selected units that are false positives, i.e. where the policy was not actually good enough.
- **Weighted conformal p-value** — A distribution-free p-value reweighted to account for the data coming from a different policy than the one being evaluated.
- **Doubly robust** — Valid if either of two nuisance models (outcome or propensity) is right, not necessarily both.
