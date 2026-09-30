---
id: statsig-z-test-non-normal-ab-tests
title: "Why is it OK to run a z-test on a non-normal distribution for A/B tests?"
source: "Statsig Blog (Viv Magida)"
url: "https://www.statsig.com/blog/z-test-on-non-normal-distribution"
published: "2026-08"
added: "2026-09-30"
category: statistical-modeling
tags: [z-test, central-limit-theorem, ab-testing, skewed-metrics]
novelty: 2
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Why is it OK to run a z-test on a non-normal distribution for A/B tests?

**Source:** [Statsig Blog (Viv Magida)](https://www.statsig.com/blog/z-test-on-non-normal-distribution) · Published 2026-08 · Added 2026-09-30
**Category:** statistical-modeling · **Tags:** `z-test`, `central-limit-theorem`, `ab-testing`, `skewed-metrics`

## TL;DR

A Statsig explainer argues z-tests are fine on skewed or non-normal metrics because an A/B test compares means, and by the Central Limit Theorem the difference in sample means is approximately normal at typical online-experiment sample sizes.

## 1. Business context

Practitioners often worry that revenue, counts or conversions are not normally distributed and so a z-test is invalid. The post addresses that recurring objection for teams using experimentation platforms.

## 2. Technical details

The core argument: the test does not assess raw values, it compares the sampling distributions of the two group means. The CLT says the sample mean approaches normality as n grows regardless of the underlying shape, and the difference of two independent approximately-normal means is itself approximately normal, so skew is 'averaged out on both sides' before the comparison. The post says this covers Bernoulli conversions, Poisson-like counts and long-tailed revenue metrics. It states no minimum sample size; adequacy depends on the metric type.

## 3. Impact — potential & realized

Educational rather than empirical: no measured results are reported. The practical value is reassurance and a clear framing for stakeholders, with the implicit caveat that very small samples or extremely heavy tails can still break the approximation.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — A clear refresher, not new ground

The CLT justification is standard textbook material and the post gives no thresholds or simulations, so the caveats a careful analyst needs (heavy tails, small n, ratio metrics needing the delta method) are left to the reader. Useful as something to send a sceptical stakeholder.

### Similar / related work

- [**Under the Hood of Uber's Experimentation Platform**](2026-09-29-uber-under-the-hood-experimentation-platform-xp.md) — shows how a production engine picks tests per metric type (Welch, Mann-Whitney, delta method) instead of one z-test everywhere.

### Jargon buster

- **Central Limit Theorem** — The average of many independent draws is approximately normal, whatever the shape of the individual draws.
- **z-test** — A test using the normal distribution to judge whether an observed difference in means is bigger than chance.
- **Sampling distribution** — The distribution of a statistic (here, the mean difference) across hypothetical repeats of the experiment.
