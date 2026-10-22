---
id: arxiv-valid-inference-did-control-selection
title: "Valid Inference After Control Selection in Difference-in-Differences"
source: "arXiv econ.EM (Nakano & Hoshino)"
url: "https://arxiv.org/abs/2610.01464"
published: "2026-10"
added: "2026-10-22"
category: experimentation-causal
tags: [difference-in-differences, selective-inference, control-selection, confidence-intervals]
novelty: 4
sourced_via: "web search"
---

# Valid Inference After Control Selection in Difference-in-Differences

**Source:** [arXiv econ.EM (Nakano & Hoshino)](https://arxiv.org/abs/2610.01464) · Published 2026-10 · Added 2026-10-22
**Category:** experimentation-causal · **Tags:** `difference-in-differences`, `selective-inference`, `control-selection`, `confidence-intervals`

## TL;DR

Picking difference-in-differences control units by pre-treatment fit makes standard confidence intervals undercover even when parallel trends holds for every candidate. The authors give a selective-inference method that conditions on the whole selection event and restores valid intervals.

## 1. Business context

Quasi-experimental evaluations (policy changes, regional launches, marketing rollouts) often choose controls from a candidate pool by how well they track the treated unit before treatment. That data-driven step is usually ignored when intervals are reported, so analysts get confidence intervals that look tight but are not trustworthy.

## 2. Technical details

The method estimates the full covariance matrix of outcome means from the same data and conditions inference on the full control-selection event, using a joint Gaussian approximation of the outcome means. The paper claims uniform asymptotic validity, including cases of perfect fit and population ties. It extends to staggered adoption, reused observations, and finite searches over fitting rules that favour larger estimates; skewness and mean-covariance corrections give randomized tests second-order accuracy for selection and rejection probabilities. Submitted 1 Oct 2026, revised 18 Oct 2026 (v3). Read at abstract level.

## 3. Impact — potential & realized

Realized (as reported): adjusted intervals behave like known-covariance benchmarks in standard-error units and shrink with effective sample size even when regional sample shares vanish. In two applications, the adjusted interval for police deployment on car theft includes zero, while minimum-wage intervals remain consistent with larger job losses at wage increases from $5 to just under $14 per hour. Potential: a drop-in correction for any pre-fit-based control selection in geo-experiments and product-launch DiD.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Specific, empirically implementable correction for a very common analyst move (pick the best-fitting controls)

Novelty 4/5 - Specific, empirically implementable correction for a very common analyst move (pick the best-fitting controls). Caveat: abstract-level read, and the Gaussian approximation needs enough effective sample size.

### Similar / related work

- [**Anytime-Valid Inference in Linear Models with Clustered Outcomes**](2026-10-20-arxiv-anytime-valid-clustered-linear-models.md) (in this bank) — another inference-validity fix for practitioners' default procedures
- [**Conformal Policy Selection**](2026-10-19-arxiv-conformal-policy-selection-fdr-deployment.md) (in this bank) — selection-aware error control in decision settings
- [**Synthetic Difference in Differences**](https://arxiv.org/abs/1812.09970) — control reweighting that also depends on pre-period fit

### Jargon buster

- **Selective inference** — Statistics that accounts for the fact that the hypothesis or model was chosen using the same data.
- **Parallel trends** — The assumption that treated and control groups would have moved together absent treatment.
- **Undercoverage** — A nominal 95% interval that contains the true value less than 95% of the time.
