---
id: arxiv-proportion-outcomes-interrupted-time-series
title: "Proportion Outcomes in Interrupted Time Series Analysis: Why Both Boundedness and Autocorrelation Matter"
source: "arXiv stat.AP (Linden)"
url: "https://arxiv.org/abs/2610.31969"
published: "2026-10"
added: "2026-10-26"
category: statistical-modeling
tags: [interrupted-time-series, beta-regression, fractional-regression, autocorrelation, teaching]
novelty: 3
sourced_via: "full-text fetch"
---

# Proportion Outcomes in Interrupted Time Series Analysis: Why Both Boundedness and Autocorrelation Matter

**Source:** [arXiv stat.AP (Linden)](https://arxiv.org/abs/2610.31969) · Published 2026-10 · Added 2026-10-26
**Category:** statistical-modeling · **Tags:** `interrupted-time-series`, `beta-regression`, `fractional-regression`, `autocorrelation`, `teaching`

## TL;DR

A teaching article arguing that proportion outcomes in interrupted time series need two separate checks: whether the model respects the 0–1 range, and whether residuals are serially dependent. Fixing one does not fix the other. Two reanalysed published healthcare studies illustrate each failure.

## 1. Business context

Interrupted time series analysis (ITSA) is a workhorse for evaluating a policy or product change when randomization is not feasible: observations before and after the intervention give a baseline level and trend, an immediate level change and a change in trend. Proportions (a conversion-like or compliance-like share) are very common outcomes, yet the default is often segmented linear regression, which ignores bounded support, and often without reporting any test for autocorrelation. The article is explicitly conceptual and practical rather than a new method.

## 2. Technical details

The mean structure is g(μ_t) = β0 + β1·T_t + β2·X_t + β3·(T_t − T0)·X_t (baseline, pre-trend, immediate level change, trend change). Example 1 reanalyses a Kenyan hospital surgical-antibiotic-prophylaxis policy (Thika Hospital; 26 weekly pre-intervention and 40 post-intervention observations) whose proportions sit near 0 and 1; the original used segmented linear regression, reanalysed here with fractional logistic regression, which keeps the conditional mean in the unit interval and allows exact zeros and ones. Example 2 reanalyses monthly proportions (Jan 2000–Dec 2009) from a Veterans Health Administration directive on controlled-release oxycodone issued July 2003, where all values lie strictly in (0,1), so beta regression applies; diagnostics (residual ACF/PACF, Ljung–Box, Cumby–Huizinga) pointed to AR(1) and a beta-AR(1) model was fitted (Stata betark).

The author also states the scope limits: both examples are illustrative, not a systematic review, so no claim is made about how common the problems are; boundary values combined with complex serial dependence may need other methods; and the applications are single-group ITSA.

## 3. Impact — potential & realized

Realized (as reported): in Example 1, segmented linear regression produced six fitted values below zero, and 35 of 66 confidence intervals extended beyond the permissible range. The fractional logistic model showed a large immediate increase after the policy (logit-scale β2 = 5.069, P = .001), no pre-trend (β1 = 0.191, P = .195), no change in trend (β3 = −0.152, P = .308), and no residual autocorrelation (Ljung–Box Q12 = 1.45, P > .99). In Example 2, linear ITSA looked plausible visually, but Ljung–Box at lag 1 gave Q1 = 4.93 (P = .026); the beta-AR(1) model estimated ρ1 = 0.263 (95% CI 0.093–0.432; P = .002), an immediate increase (β2 = 0.162, P = .040) and a reduction in post-intervention trend (β3 = −0.0096, P = .004), with no remaining autocorrelation in conditional residuals (Q12 = 15.59, P = .211). Coefficients are on the logit scale, so they are not percentage-point changes.

Potential: a checklist for any before/after evaluation with a rate or share as the metric, and a classroom exercise using the public collection of published ITSA datasets.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Not a new method, but a clear, reusable checklist for a very common analysis that is often done with the wrong default.

The most transferable lesson is that a plausible-looking fitted line is not a diagnostic: in Example 2 the linear and beta-AR(1) fits look alike while the autocorrelation is real. For product analytics teams evaluating a launch with a daily or weekly share metric (activation rate, opt-in rate), both checks are cheap. Two reanalyses are anecdotes, as the author says, so read this as guidance rather than evidence on how widespread the problem is.

### Similar / related work

- [**Valid Inference After Control Selection in Difference-in-Differences**](2026-10-22-arxiv-valid-inference-did-control-selection.md) (in this bank) — Valid inference after control selection in DiD — another non-randomized evaluation design
- [**Synthetic Control under Out-of-Span Common Shocks: Diagnosis, Exposure Balance and Correction**](2026-10-06-arxiv-synthetic-control-out-of-span-shocks.md) (in this bank) — Synthetic control under out-of-span shocks — the multi-unit cousin of single-series ITSA

### Jargon buster

- **ITSA** — Interrupted time series analysis: model a series before and after an intervention to estimate a level shift and trend change.
- **Fractional logistic regression** — A logit-link model for outcomes in [0,1], allowing exact 0s and 1s.
- **Beta-AR(1) regression** — A beta regression for outcomes strictly in (0,1) with first-order autoregressive dependence.
- **Ljung–Box test** — A portmanteau test for whether residual autocorrelations up to some lag are jointly zero.
