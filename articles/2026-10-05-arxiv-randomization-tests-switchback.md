---
id: arxiv-randomization-tests-switchback
title: "Randomization Tests in Switchback Experiments"
source: "arXiv (Jizhou Liu, Liang Zhong)"
url: "https://arxiv.org/abs/2602.23257"
published: "2026-02"
added: "2026-10-05"
category: experimentation-causal
tags: [switchback, randomization-test, carryover, inference, rideshare]
novelty: 3
sourced_via: "web search"
---

# Randomization Tests in Switchback Experiments

**Source:** [arXiv (Jizhou Liu, Liang Zhong)](https://arxiv.org/abs/2602.23257) · Published 2026-02 · Added 2026-10-05
**Category:** experimentation-causal · **Tags:** `switchback`, `randomization-test`, `carryover`, `inference`, `rideshare`

## TL;DR

Three randomization-based tests for switchback experiments: a conditional randomization test for the total effect, a carryover test, and a non-anticipation test, with finite-sample validity under standard assumptions on temporal interference and no parametric outcome model (v2 posted 2026-09-29).

## 1. Business context

Switchback experiments are used when markets or platforms alternate between treatment and control across time blocks because user-level randomization is infeasible, outcomes are aggregated, or interference is unavoidable. Analysts typically rely on parametric or asymptotic inference that can break with few time blocks, serial dependence, seasonality and persistent effects.

## 2. Technical details

The authors build a conditional randomization test for detecting total treatment effects that stays valid in small samples despite serial dependence, seasonality and persistent treatment effects. Two diagnostic tests complement it: a carryover test (do past assignments affect outcomes beyond a specified horizon?) and a non-anticipation test (do future assignments affect current outcomes?). They claim finite-sample validity under standard assumptions on temporal interference without a parametric outcome model, show asymptotic validity for studentized tests, and derive power approximations describing trade-offs between design choices, informative comparisons and power.

## 3. Impact — potential & realized

Numerical experiments with stylized potential outcomes and a dynamic rideshare model illustrate finite-sample performance and design implications; no real-company deployment is reported in the abstract. Potential: a checklist-style way to test the assumptions a switchback analysis silently relies on.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid, practical inference toolkit; incremental over randomization-test literature but well aimed.

Carryover and non-anticipation tests are the useful part: they make the key switchback assumptions testable. Validation is simulation-based per the abstract.

### Similar / related work

- [**Sequentially-Rerandomized Switchback Experiments**](2026-10-05-arxiv-sequentially-rerandomized-switchback.md) — in-bank: design-side companion
- [**CUPED on Steroids: Multivariate Covariate Adjustment for Switchback Experiments**](2026-09-29-arxiv-cuped-on-steroids-switchback.md) — in-bank: variance reduction for switchbacks

### Jargon buster

- **Randomization test** — A test whose null distribution comes from re-running the known random assignment mechanism, so validity does not depend on an outcome model.
- **Non-anticipation** — The assumption that future treatment assignments do not affect current outcomes.
- **Studentized test** — A test statistic divided by an estimated standard error, which helps asymptotic validity.
