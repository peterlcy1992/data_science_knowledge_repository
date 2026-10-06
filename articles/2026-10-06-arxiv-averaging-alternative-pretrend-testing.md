---
id: arxiv-averaging-alternative-pretrend-testing
title: "An Averaging Alternative to Pre-Trend Testing"
source: "arXiv (Nicholas L. Brown, Qiushi Bu)"
url: "https://arxiv.org/abs/2610.05705"
published: "2026-10"
added: "2026-10-06"
category: experimentation-causal
tags: [difference-in-differences, pre-trend-testing, model-averaging, parallel-trends, post-selection-inference]
novelty: 3
sourced_via: "web search"
---

# An Averaging Alternative to Pre-Trend Testing

**Source:** [arXiv (Nicholas L. Brown, Qiushi Bu)](https://arxiv.org/abs/2610.05705) · Published 2026-10 · Added 2026-10-06
**Category:** experimentation-causal · **Tags:** `difference-in-differences`, `pre-trend-testing`, `model-averaging`, `parallel-trends`, `post-selection-inference`

## TL;DR

Proposes the Model Averaged DID (MADID) estimator: instead of pre-testing parallel trends and then picking a specification, it averages candidate 2×2 DID estimators with exponential weights based on their residual sums of squares, sidestepping the bias that pre-trend testing can induce.

## 1. Business context

Difference-in-differences is a workhorse for evaluating launches, policy changes and marketing interventions when randomization is not possible. A standard routine is to test for pre-trends and proceed only if the test passes. The paper builds on Roth (2022), who showed that this pre-test can itself induce bias, leaving analysts without a clean, practical alternative.

## 2. Technical details

MADID is a weighted average of the candidate 2×2 DID estimators. The weights are normalized exponential functions of each candidate's residual sums of squares, so no formal specification test is run during implementation. Per the abstract, the estimator is consistent when parallel trends holds for at least one pre-treatment period. The joint limiting distribution across post-treatment periods is generally non-Gaussian, so inference needs subsampling or simulation-based methods. The paper is classified under both statistics methodology and econometrics.

## 3. Impact — potential & realized

Theory-focused (abstract-level read; full paper not read). I could not confirm simulation sizes or an empirical application from the abstract. Potential: a way to report DID effects without a pass/fail pre-trend gate, at the cost of non-standard inference.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sensible model-averaging answer to the pre-test problem, but non-Gaussian inference makes it harder to adopt than a drop-in robust estimator.

A sensible model-averaging answer to the pre-test problem, but non-Gaussian inference makes it harder to adopt than a drop-in robust estimator. Pre-trend testing is a common practitioner habit that the recent DiD literature has been attacking; this offers another route alongside sensitivity-analysis approaches. Evidence is theoretical from the abstract, so wait for simulation and application detail before changing workflows.

### Similar / related work

- [**Risk-Set Transported Synthetic Control with Difference-in-Differences Adjustment under Staggered Treatment Adoption**](2026-10-02-arxiv-rt-sc-did-staggered-synthetic-control.md) (in this bank) — another recent DiD/synthetic-control inference paper
- **Roth (2022) pre-testing and pre-trend literature** — the bias-from-pretesting result this paper builds on (no specific URL linked)
- [**Shared-Donor Inference for Fixed-Set Heterogeneity in Synthetic Difference-in-Differences**](https://arxiv.org/abs/2607.08324) — inference when synthetic-control donors are reused

### Jargon buster

- **Parallel trends** — The DID identifying assumption: absent treatment, treated and control outcomes would have moved in parallel.
- **Pre-trend test** — A test of whether treated and control groups moved in parallel before treatment; passing it is often used as a gate for running DID.
- **Model averaging** — Combining several candidate estimators with data-driven weights instead of choosing one.
