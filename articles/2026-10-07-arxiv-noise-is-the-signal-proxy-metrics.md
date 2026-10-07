---
id: arxiv-noise-is-the-signal-proxy-metrics
title: "The Noise Is the Signal: Correlated Sampling Error Is Rank-Informative"
source: "arXiv (Sandro Provenzano)"
url: "https://arxiv.org/abs/2610.08194"
published: "2026-10"
added: "2026-10-07"
category: product-analytics
tags: [proxy-metrics, north-star-metric, shared-sampling-error, ab-testing, metric-selection]
novelty: 4
sourced_via: "web search"
---

# The Noise Is the Signal: Correlated Sampling Error Is Rank-Informative

**Source:** [arXiv (Sandro Provenzano)](https://arxiv.org/abs/2610.08194) · Published 2026-10 · Added 2026-10-07
**Category:** product-analytics · **Tags:** `proxy-metrics`, `north-star-metric`, `shared-sampling-error`, `ab-testing`, `metric-selection`

## TL;DR

Proxy metrics and north-star metrics measured in the same experiments share sampling error. The paper argues that shared error is informative for ranking candidate proxies, and that correcting it away makes rankings worse unless you have many more experiments.

## 1. Business context

Choosing a short-term proxy for a slow, noisy north-star metric is a core product-analytics decision. Recent approaches treat the correlated sampling error between proxy and north star across experiments as contamination to be bias-corrected away.

## 2. Technical details

Using 262 experiments and 69 candidate proxies, the author compares rankings to an error-free benchmark built from disjoint customer halves within each experiment, so the agreement measure itself does not share sampling error. Simulations with known true rankings test the claim, including with accurate covariance estimates. Per the summary, the uncorrected shared error ranks proxies in similar order to error-free agreement (Spearman 0.65); correction discards signal while leaving the main noise sources in place. Held-out experiments correlate at 0.93 with the paper's predictions. Full paper not read; company/platform not identified in the material seen.

## 3. Impact — potential & realized

Realized: a decision rule for experimentation teams, namely correcting shared error pays off only with substantially more experiments, and the required number rises steeply with north-star noise. Potential: simpler, more robust proxy-selection pipelines that skip noise-correction machinery for small experiment portfolios.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Counter-intuitive and practically actionable: it says "do less" in proxy-metric selection for most teams.

Counter-intuitive and practically actionable: it says "do less" in proxy-metric selection for most teams. The key credibility device (disjoint customer halves) is sensible, but results come from one experiment portfolio, so check transfer to your own metric noise levels.

### Similar / related work

- [**Ensuring Trustworthy Online A/B Testing: Addressing Five Key Questions on CUPED**](2026-10-02-arxiv-cuped-five-questions-bytedance.md) (in this bank) — both concern what statistical adjustment actually buys in practice
- [**Accelerating A/B-Tests with Counterfactual Estimation: Reducing Variance through Policy Overlap**](2026-10-01-arxiv-policy-overlap-accelerating-ab-tests.md) (in this bank) — another variance/noise-oriented A/B paper in this bank

### Jargon buster

- **Proxy metric** — A fast, sensitive metric used as a stand-in for a slow or noisy long-term goal.
- **North-star metric** — The single top-level outcome the product is trying to move.
- **Shared sampling error** — Noise that hits both metrics because they are computed from the same users in the same experiment, making their estimated effects correlated.
- **Spearman correlation** — A rank-based correlation: 1 means identical ordering, 0 means unrelated ordering.
