---
id: arxiv-proximal-did-long-term-effects-outcome-drift
title: "Proximal Difference-in-Differences for Causal Learning under Confounding and Outcome Drift"
source: "arXiv stat.ME (NC State & Eli Lilly: Park, Yang, Lipkovich, Ye, Shan)"
url: "https://arxiv.org/abs/2611.10310"
published: "2026-11"
added: "2026-11-12"
category: experimentation-causal
tags: [long-term-effects, proximal-causal-inference, difference-in-differences, data-fusion, external-controls, doubly-robust, outcome-drift]
novelty: 3
sourced_via: "full-text fetch"
---

# Proximal Difference-in-Differences for Causal Learning under Confounding and Outcome Drift

**Source:** [arXiv stat.ME (NC State & Eli Lilly: Park, Yang, Lipkovich, Ye, Shan)](https://arxiv.org/abs/2611.10310) · Published 2026-11 · Added 2026-11-12
**Category:** experimentation-causal · **Tags:** `long-term-effects`, `proximal-causal-inference`, `difference-in-differences`, `data-fusion`, `external-controls`, `doubly-robust`, `outcome-drift`

## TL;DR

To extend a short randomized experiment's control arm into the long run using external observational data, the authors relax parallel trends to hold only conditional on observed and latent factors, and use proxy variables (proximal inference) to handle unmeasured confounding and inter-study outcome drift. A doubly robust, locally efficient estimator stays near-unbiased in simulations where synthetic DiD, matrix completion and a prior proximal method are biased.

## 1. Business context

Long-term effects matter for regulators and for tech: the paper notes that online A/B tests measure immediate responses but often miss long-term goals like customer lifetime value, and long experiments are precluded by cost, attrition or ethics. In clinical trials, open-label extensions let control patients cross over to treatment after the blinded phase, censoring the long-term control trajectory. The standard fix — borrow controls from external observational data (EHRs, or historical user logs in tech) — assumes exchangeability that fails under latent confounding and under 'outcome drift' (external units trend differently due to placebo effects, study bias, or platform evolution). The authors map the setting explicitly: the 'RCT' is the A/B test and the 'external control' is historical logs.

## 2. Technical details

**Target.** The long-term average effect on the trial population; the hard part is τ = E[Y₀ under continued control | trial], since the treated long-term mean is observed.

**Identification.** A new assumption, Conditional Parallel Trend given Latent factors (CPTL): the trial-vs-external bias b(X,U) is constant across periods given observed X and latent U. This allows time-varying latent effects and X–U interactions, generalizes the linear factor model and additive equiconfounding, and reduces to exchangeability when b=0. It is untestable; a falsification test using multiple trial-period outcomes is given in the appendix.

**Proxies and bridge functions.** A trend-confounding bridge d(W,X) and a source-confounding bridge q(Z,X) connect U to observed proxies without modelling U. The method models a single bridge for the outcome *change* Y₀ − Y_pre rather than two for levels, and the proxy Z need only be observed in the external data. This yields proximal outcome-regression (POR), proximal IPW (PIPW) and a doubly robust (PDR) estimator from the efficient influence function, consistent if either bridge is correctly specified, with rate conditions allowing ML nuisances under cross-fitting (bridges estimated with neural networks via a minimax approach in the experiments).

## 3. Impact — potential & realized

**Realized (simulation only).** 500 replications at n=500: PDR shows the expected double robustness when at least one bridge is right, with modest finite-sample bias and slight undercoverage in the more nonlinear setting (γ=2); POR and PIPW are biased under misspecification; SDID, MC-NNM and minimal-bridge (MB) baselines have larger bias and lower coverage, and fail to recover the counterfactual mean in the nonlinear setting. In a plasmode simulation built on a Phase 3 Alzheimer's trial and the GERAS observational study, bias was −0.005 for PDR vs −0.896 (MB), −0.607 (SDID) and −0.537 (MC-NNM), with bootstrap SEs 0.478, 0.430, 0.974 and 0.371; MB's ±2 SE interval missed the truth.

**Potential.** A framework for extending short experiments with historical logs while allowing drift and latent confounding; an appendix extends it to missing outcomes.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A principled extension of DiD-style data fusion for long-term effects; the tech application is argued, not demonstrated.

For experimentation teams the relevant question is 'can I use pre-experiment or historical users as long-run controls once my holdout ends?' This paper gives a more forgiving assumption than parallel trends, but swaps it for the need to find valid proxies (W, Z) — in product data, think pre-period engagement signals that are affected by the latent intent but not directly by cohort. That is the hard part and the paper doesn't show a tech example. Evidence is simulations plus a plasmode, so treat it as a method to keep in the toolkit, alongside surrogate-index approaches, rather than a drop-in.

### Similar / related work

- [**Many Hands Make Light Work: Long-Term Effect Inference for the Experiment Reservoir**](2026-10-28-arxiv-experiment-reservoir-surrogate-long-term-effects.md) — in this bank: surrogate-based long-term effect inference for online experiments, the alternative route
- [**When Covariates Mask Pre-Trends**](2026-11-06-arxiv-when-covariates-mask-pre-trends-honest-did.md) — in this bank: another look at what conditional parallel trends does and doesn't buy
- [**Synthetic Difference-in-Differences**](https://arxiv.org/abs/1812.09970) — Arkhangelsky et al.'s SDID, one of the baselines
- [**Long-term causal inference under persistent confounding via data combination**](https://arxiv.org/abs/2202.07234) — Imbens et al.'s proximal long-term approach, which the authors contrast with theirs

### Jargon buster

- **Proximal causal inference** — Using two kinds of proxy variables for an unmeasured confounder to identify effects without measuring the confounder itself.
- **Bridge function** — A function of observed proxies that stands in for the unobserved confounder's effect in an outcome or weighting model.
- **Outcome drift** — Systematic differences in untreated trajectories between the experiment and the external data, e.g. from platform changes.
- **Plasmode simulation** — A semi-synthetic study that generates data to mimic real-data features so the truth is known.
