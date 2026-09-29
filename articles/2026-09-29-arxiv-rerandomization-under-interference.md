---
id: arxiv-rerandomization-under-interference
title: "Rerandomization under Interference"
source: "arXiv (Yuan, Li, Li)"
url: "https://arxiv.org/abs/2609.33730"
published: "2026-09"
added: "2026-09-29"
category: experimentation-causal
tags: [rerandomization, interference, experimental-design, covariate-balance, hajek-estimator]
novelty: 4
sourced_via: "web search"
---

# Rerandomization under Interference

**Source:** [arXiv (Yuan, Li, Li)](https://arxiv.org/abs/2609.33730) · Published 2026-09 · Added 2026-09-29
**Category:** experimentation-causal · **Tags:** `rerandomization`, `interference`, `experimental-design`, `covariate-balance`, `hajek-estimator`

## TL;DR

Ziang Yuan, Xinran Li and Shuangning Li show that rerandomization — restricting assignments to those with small covariate imbalance — still improves precision of the Hájek estimator when units interfere with each other, without having to specify the interference structure. They also give a conservative variance estimator for when a dependence graph is known.

## 1. Business context

Randomized experiments on networks and marketplaces (social feeds, two-sided platforms) routinely violate SUTVA: one unit's outcome depends on others' assignments. Practitioners use covariate information to gain precision, but most design-stage tools (rerandomization, stratification) were justified only assuming no interference. The paper asks whether that design-stage precision gain survives interference.

## 2. Technical details

The paper studies rerandomization — a design-stage procedure that draws assignments from a Bernoulli design but accepts only those with covariate imbalance below a threshold — while staying largely agnostic about the interference structure. The estimand is the expected average treatment effect, estimated with the Hájek estimator. The authors prove that rerandomization can improve estimation precision asymptotically relative to unrestricted Bernoulli randomization under only mild conditions on dependence between units, and that it retains the 'no-harm' property (covariate adjustment does not hurt). The framework allows covariates that themselves depend on the assignment vector, such as the proportion of treated neighbours. When a dependence graph is available, they propose an optimization-based conservative variance estimator for inference.

## 3. Impact — potential & realized

Reported result is theoretical: an asymptotic precision gain with the no-harm guarantee under interference, plus a usable conservative variance estimator. The source summary I could reach does not report empirical numbers, so none are given here. The potential is a principled way to use pre-experiment covariates in network/marketplace tests without committing to a specific interference model.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Practical design-stage variance reduction for the settings where CUPED-style analysis is hardest

Design-stage covariate balancing is cheap and well loved, but its guarantees have mostly assumed no interference. Extending them to an interference-agnostic setting, including assignment-dependent covariates like treated-neighbour share, is a real contribution for platform experimenters, though it is a methods paper without a reported production case. Score reflects solid relevance and rigor rather than a paradigm shift.

### Similar / related work

- [**Robust A/B Decisions**](2026-09-28-arxiv-robust-ab-decisions-farrell-misra.md) — adjacent: decision rules on top of experiment output; this paper is about getting the estimate more precisely.
- [**Beyond the A/B Test: Experiment Designs for Your Toughest Questions**](2026-09-25-statsig-beyond-ab-test-designs.md) — covers switchback and other designs for interference-prone settings.

### Jargon buster

- **Interference** — A unit's outcome depends on other units' treatment assignments, breaking the standard no-spillover assumption (SUTVA).
- **Rerandomization** — Draw random assignments repeatedly and keep only one whose covariates are balanced enough between arms, improving precision.
- **Hájek estimator** — A ratio-style (normalised) weighted mean estimator of the average treatment effect, more stable than the plain inverse-probability estimator.
