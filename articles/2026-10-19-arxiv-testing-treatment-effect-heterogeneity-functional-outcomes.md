---
id: arxiv-testing-treatment-effect-heterogeneity-functional-outcomes
title: "Testing Treatment Effect Heterogeneity with Functional Outcomes"
source: "arXiv stat.ME (Feng, Li & Song)"
url: "https://arxiv.org/abs/2610.23397"
published: "2026-10"
added: "2026-10-19"
category: experimentation-causal
tags: [hte, functional-data, hypothesis-testing, smart-metering]
novelty: 3
sourced_via: "web search"
---

# Testing Treatment Effect Heterogeneity with Functional Outcomes

**Source:** [arXiv stat.ME (Feng, Li & Song)](https://arxiv.org/abs/2610.23397) · Published 2026-10 · Added 2026-10-19
**Category:** experimentation-causal · **Tags:** `hte`, `functional-data`, `hypothesis-testing`, `smart-metering`

## TL;DR

A nonparametric test for whether treatment effects on time-varying (functional) outcomes are homogeneous across individuals, without needing to estimate the unknown common effect. Applied to the Irish gas smart-metering trial.

## 1. Business context

Experiments often measure outcomes that are curves (usage over a day, engagement over time), and the first question before personalizing is whether effects differ across individuals at all. A formal heterogeneity test guards against chasing noise in subgroup analysis.

## 2. Technical details

The test compares within-arm difference distributions, which cancels the unknown common effect without estimating it. Departures are measured by an integrated squared discrepancy of characteristic functionals with a full-support Gaussian integrating measure; no moment conditions are needed and it extends to multiple arms sharing a control. An unbiased generalized U-statistic handles dependence among overlapping differences; asymptotics are derived under the null, fixed and local alternatives; inference uses a centered multiplier bootstrap. A random-direction approximation and a nine-state recursion bring computation to linear order in sample size.

## 3. Impact — potential & realized

Realized (as reported): simulations assess finite-sample performance against benchmarks, and the method is applied to the Irish gas smart-metering trial to assess heterogeneity in functional responses. No numbers were available; the preprint carries only brief proof outlines. Potential: a gatekeeping test before HTE modelling for curve-valued outcomes.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Useful framing: test for heterogeneity before estimating it.

Useful framing: test for heterogeneity before estimating it. The tooling is technical (characteristic functionals, U-statistics) and the practical audience is narrower than for scalar-outcome HTE. Caveat: abstract-level read.

### Similar / related work

- [**Identifying and Measuring Treatment-Effect Heterogeneity across Sites through Within-Site Randomization**](2026-10-15-arxiv-within-site-randomization-effect-heterogeneity.md) (in this bank) — another take on measuring effect heterogeneity
- [**Bayesian Causal Forests for Zero-Inflated Continuous Outcomes**](2026-10-16-arxiv-bcf-zero-inflated-continuous-outcomes.md) (in this bank) — estimates HTE where this paper tests for it

### Jargon buster

- **Functional outcome** — An outcome that is a whole curve per unit, such as consumption over time, rather than one number.
- **Multiplier bootstrap** — A fast resampling scheme that approximates a statistic's null distribution by randomly reweighting its components.
