---
id: arxiv-variance-reduction-pre-and-in-experiment-etsy
title: "Variance Reduction Combining Pre-Experiment and In-Experiment Data"
source: "arXiv / CLeaR 2026 (Lin, Crespo — Etsy)"
url: "https://arxiv.org/abs/2410.09027"
published: "2026-03"
added: "2026-09-30"
category: experimentation-causal
tags: [variance-reduction, cuped, cupac, post-treatment-covariates, ab-testing]
novelty: 4
sourced_via: "web search"
---

# Variance Reduction Combining Pre-Experiment and In-Experiment Data

**Source:** [arXiv / CLeaR 2026 (Lin, Crespo — Etsy)](https://arxiv.org/abs/2410.09027) · Published 2026-03 · Added 2026-09-30
**Category:** experimentation-causal · **Tags:** `variance-reduction`, `cuped`, `cupac`, `post-treatment-covariates`, `ab-testing`

## TL;DR

Lin (UC Berkeley) and Crespo (Etsy) extend CUPED/CUPAC by also using in-experiment (post-treatment) covariates in a way that stays unbiased, with asymptotic theory and consistent variance estimators; on several Etsy experiments it gives substantial extra variance reduction over the existing CUPAC pipeline with only a few in-experiment covariates.

## 1. Business context

Online controlled experiments have a fixed sample size, so sensitivity depends on how tightly the average treatment effect (ATE) can be estimated. CUPED and CUPAC reduce variance using pre-experiment data, but their payoff depends on how predictive that history is for the outcome measured during the test. Etsy, where many outcomes (e.g. purchases) are only weakly predicted by history, wants more power without running longer.

## 2. Technical details

The paper observes that in-experiment data is usually more strongly correlated with the outcome than pre-experiment data, but naively adjusting for arbitrary post-treatment variables can bias the ATE estimate. The authors propose a general, robust framework that combines pre-experiment and in-experiment covariates while avoiding that bias. Contributions listed: asymptotic theory for the estimator, consistent variance estimators for inference, and an implementation that is described as simple, interpretable and computationally efficient. The paper was first posted in October 2024 and revised in March 2026; it appears in the Proceedings of the 5th Conference on Causal Learning and Reasoning (CLeaR 2026). The exact form of the estimator and the conditions on admissible in-experiment covariates are not reproduced here — see the paper.

## 3. Impact — potential & realized

Reported: across multiple online experiments at Etsy, the method achieved 'substantial additional variance reduction over current pipeline' (CUPAC), even when adding only a few post-treatment covariates. Specific percentages were not available from the sources I could access. Potential: shorter experiments or detection of smaller effects at the same traffic.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A principled way to use the in-experiment signal that CUPED-style methods leave on the table

CUPED/CUPAC are near-universal; the interesting move is formalising when post-treatment covariates can be used safely rather than banning them. Combined with recent switchback and marketplace variants it points to variance reduction becoming a richer covariate-engineering problem. Peer-reviewed venue plus an industrial validation raise confidence, though headline numbers weren't visible to me.

### Similar / related work

- [**CUPED on Steroids: Multivariate Covariate Adjustment for Switchback Experiments**](2026-09-29-arxiv-cuped-on-steroids-switchback.md) — the same variance-reduction family applied to switchback designs.
- [**Under the Hood of Uber's Experimentation Platform**](2026-09-29-uber-under-the-hood-experimentation-platform-xp.md) — an earlier production stack that used CUPED.

### Jargon buster

- **CUPED** — Controlled-experiment Using Pre-Experiment Data: regresses out a pre-period covariate to shrink outcome variance.
- **CUPAC** — CUPED with an ML-model prediction of the outcome as the covariate.
- **Post-treatment covariate** — A variable measured after randomisation that the treatment may itself affect; adjusting for it naively can bias the effect estimate.
