---
id: uber-under-the-hood-experimentation-platform-xp
title: "Under the Hood of Uber's Experimentation Platform"
source: "Uber Engineering Blog"
url: "https://www.uber.com/us/en/blog/xp/"
published: "2018-08"
added: "2026-09-29"
category: experimentation-causal
tags: [experimentation-platform, statistics-engine, cuped, sequential-testing, multiple-comparisons, bandits]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Under the Hood of Uber's Experimentation Platform

**Source:** [Uber Engineering Blog](https://www.uber.com/us/en/blog/xp/) · Published 2018-08 · Added 2026-09-29
**Category:** experimentation-causal · **Tags:** `experimentation-platform`, `statistics-engine`, `cuped`, `sequential-testing`, `multiple-comparisons`, `bandits`

## TL;DR

Uber's XP platform runs over 1,000 concurrent experiments across rider, driver, Eats and Freight apps, with a statistics engine that picks the test by metric type, applies CUPED and Benjamini-Hochberg, monitors outages with mSPRT, and falls back to synthetic control and diff-in-diff when randomisation isn't possible.

## 1. Business context

Uber uses XP to launch, debug, measure and monitor product features, marketing campaigns, promotions and ML models. At 1,000+ concurrent experiments across several apps, the goal was 'one-size-fits-most' hypothesis testing methodology that teams across the company could use without bespoke statistics.

## 2. Technical details

Statistics engine, by metric type: Welch's t-test for continuous metrics (e.g. gross bookings), chi-squared for proportions (e.g. retention), delta method and bootstrap for ratio metrics (e.g. trip completion), and Mann-Whitney U for skewed data. It automatically detects sample imbalance and 'flickers' (units switching groups). Quality/power features: clustering-based outlier detection, CUPED variance reduction, diff-in-diff correction for pre-experiment bias, and Benjamini-Hochberg correction for A/B/N tests. For real-time monitoring of outages it uses mixture SPRT (mSPRT) with delete-a-group jackknife variance estimation to handle correlated observations across days. Beyond randomised tests: causal inference methods (synthetic control, diff-in-diff) where a counterfactual is otherwise unavailable, and multi-armed bandits, including contextual MAB with Bayesian optimisation for hyperparameter tuning and content personalisation. A metrics-discovery recommender (item-based collaborative filtering using Jaccard co-selection popularity and absolute Pearson correlation) helps experimenters find relevant metrics among 1,000+.

## 3. Impact — potential & realized

Realized: a shared platform supporting 1,000+ simultaneous experiments across four apps. The post is from 2018 and does not report a single headline metric lift; its value is as a reference design for a production statistics engine.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Dated but still a good checklist for what a mature stats engine needs

Individually the methods are standard today, but the post is a compact reference of a full stack: test-per-metric-type, SRM/flicker detection, CUPED, multiplicity control, sequential monitoring and quasi-experimental fallbacks under one roof. Novelty is modest because it dates to 2018 and later platforms (see related) went further.

### Similar / related work

- [**Beyond the A/B Test: Experiment Designs for Your Toughest Questions**](2026-09-25-statsig-beyond-ab-test-designs.md) — modern vendor view of designs beyond the plain A/B test.
- [**Optimizing at the Edge: Using Regression Discontinuity Designs to Power Decision-Making**](2026-09-25-instacart-quasi-experiment-rdd.md) — another quasi-experimental method for when randomisation isn't available.
- [**CUPED on Steroids: Multivariate Covariate Adjustment for Switchback Experiments**](2026-09-29-arxiv-cuped-on-steroids-switchback.md) — a recent extension of the CUPED technique XP already used.

### Jargon buster

- **mSPRT** — Mixture Sequential Probability Ratio Test: a sequential test that stays valid when you peek at results continuously.
- **Benjamini-Hochberg** — A procedure controlling the false discovery rate when comparing many arms or metrics.
- **Flicker** — A unit that appears in both treatment and control over the experiment, contaminating the comparison.
