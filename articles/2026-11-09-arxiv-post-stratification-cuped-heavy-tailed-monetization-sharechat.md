---
id: arxiv-post-stratification-cuped-heavy-tailed-monetization-sharechat
title: "Variance Reduction for Heavy-Tailed Monetization Metrics in Ranking Experiments via Post-Stratification"
source: "arXiv cs.LG / SIGIR '26 (ShareChat, Aampe, Simulacra Research)"
url: "https://arxiv.org/abs/2606.04110"
published: "2026-06"
added: "2026-11-09"
category: experimentation-causal
tags: [post-stratification, cuped, heavy-tailed-metrics, variance-reduction, a-b-testing, ranking-experiments]
novelty: 4
sourced_via: "full-text fetch"
---

# Variance Reduction for Heavy-Tailed Monetization Metrics in Ranking Experiments via Post-Stratification

**Source:** [arXiv cs.LG / SIGIR '26 (ShareChat, Aampe, Simulacra Research)](https://arxiv.org/abs/2606.04110) · Published 2026-06 · Added 2026-11-09
**Category:** experimentation-causal · **Tags:** `post-stratification`, `cuped`, `heavy-tailed-metrics`, `variance-reduction`, `a-b-testing`, `ranking-experiments`

## TL;DR

ShareChat combines post-stratification (strata from pre-period GMV, aggregated with full-platform weights) with CUPED to analyse heavy-tailed monetization metrics in ranking A/B tests. Across 40+ production experiments (each >1M users) it reports equivalent confidence with about 45% less traffic than the raw metric, versus about 17% for CUPED alone, at the cost of a Type-I error of 6.1% (vs 5% nominal) and a deliberately down-weighted view of the very top spenders.

## 1. Business context

ShareChat's live-streaming product lets users buy virtual currency and gift it to creators; GMV (total recharge amount in the experiment window) is the primary monetization metric and is a downstream outcome of retrieval, ranking and diversification components. Ranking changes are validated by user-randomized A/B tests, but GMV is heavy-tailed: the top 0.01% of users dominate the variance. The authors report that A/A simulations show the CLT converging slowly (satisfactory only at 50% traffic or more), with false-positive rates of 2-4% against a nominal 5%, i.e. the test is conservative and badly underpowered at the 5-10% traffic allocations typical in practice. Extending duration or traffic did not fix it, which slowed iteration on ranking improvements.

## 2. Technical details

Target estimand: the population ATE of post-experiment GMV, randomized at the user level. Workflow: (1) collect raw and pre-experiment GMV per user; (2) winsorize or drop values beyond the 99.999th percentile (typically fewer than 5 users); (3) assign users to behavioural strata (tail, non-tail, new users/non-spenders) from 30-day historical GMV, with thresholds computed on the pre-period population and frozen before outcomes are seen; (4) CUPED-adjust GMV within each stratum using centred pre-period GMV; (5) compute the post-stratified mean and variance with full-platform stratum weights w_s = N_s/N (variance = sum of w_s^2 sigma_s^2 / n_s); (6) z-test. Because strata use only pre-treatment information, the estimator is unbiased (the authors cite Miratrix et al. 2013). The variance gain comes from putting the tail in a tiny-weight stratum (w around 0.0001, so its variance contribution is scaled by about 1e-8). Robustness checks reported: tail cutoffs from the 99.9th to 99.995th percentile all gave over 95% variance reduction (95.2% to 99.7%) with identical ship/no-ship decisions in 95% of experiments; feature-based strata (creator status, quality-DAU flags, new rechargers) gave 25-35% variance reduction and k-means clustering increased variance, whereas simple percentile strata on pre-period GMV dominated.

## 3. Impact — potential & realized

Realized (as reported): over 40+ production A/B tests on ShareChat and Moj live-streaming ranking, variance reduction vs raw GMV was about 48% for CUPED alone and 99.3% (winsorized) / 99.7% (raw tails) for post-stratification with CUPED; median relative z was 1.10 (CUPED) and 1.35-1.36 (post-strat), i.e. about 17% vs about 45% less traffic for the same confidence. At 10% traffic the MDE falls from about 136% of the mean (raw) to about 10%. Effects detected in week 1 kept 91% directional agreement in week 2; the authors saw no launch that failed to reproduce at higher traffic or needed rollback, and average time-to-decision fell by about 50%. Post-stratified GMV became the default for monetization experiments and was extended to gaming revenue and coins earned. Costs the authors state: empirical Type-I error 6.1% across the production tests (vs 1.0% raw and 2.6% CUPED, which they argue reflects low power rather than good calibration), a 0% rate in static A/A simulations, and an estimand that is insensitive to effects concentrated in the top spenders; they treat it as sufficient for low-risk ranking changes, recommend longer confirmation for high-risk launches, advise against it for whale-targeted features, and surface raw and post-stratified metrics side by side.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — practical and well-evidenced

A useful, honest production note: the classical survey-sampling trick is cheap to implement and the traffic savings are large for a metric where CUPED alone cannot help much. The caveat is the estimand: down-weighting the tail changes what question the test answers, and the elevated Type-I error means it is a tool for low-risk decisions, not a free lunch. The paper is a short industry paper, with confidential axes and no code. Likely to be copied by any team with revenue-like metrics.

### Similar / related work

- [**Regression Adjustment for Ratios of Treatment Effects in Randomized Experiments**](2026-10-27-arxiv-regression-adjustment-ratios-treatment-effects.md) (in this bank) — covariate adjustment in randomized experiments
- [**Studentized inference in randomized experiments when a few units dominate the outcome variation**](2026-11-03-arxiv-studentized-inference-few-units-dominate-randomized-experiments.md) (in this bank) — inference when a few units dominate the outcome variation
- **Deng et al. 2013 'Improving the sensitivity of online controlled experiments by utilizing pre-experiment data'** — the original CUPED paper

### Jargon buster

- **Post-stratification** — Splitting units into groups after the experiment using pre-treatment traits, estimating the effect inside each group, then re-weighting by population shares.
- **CUPED** — Subtracting a pre-experiment covariate's predictable part from the metric to cut variance without bias.
- **MDE** — Minimum detectable effect: the smallest true effect the test can reliably detect at a given sample size.
