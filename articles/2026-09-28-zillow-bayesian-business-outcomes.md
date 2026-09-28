---
id: zillow-bayesian-business-outcomes
title: "How Zillow Data Science Measures Business Outcomes with Bayesian Statistics"
source: "Zillow Tech Hub"
url: "https://www.zillow.com/tech/how-zillow-data-science-measures-business-outcomes-with-bayesian-statistics/"
published: "2023-02"
added: "2026-09-28"
category: statistical-modeling
tags: [bayesian-inference, shrinkage, hierarchical-models, survival-analysis, conversion-rate, censoring]
novelty: 3
sourced_via: "web search"
---

# How Zillow Data Science Measures Business Outcomes with Bayesian Statistics

**Source:** [Zillow Tech Hub](https://www.zillow.com/tech/how-zillow-data-science-measures-business-outcomes-with-bayesian-statistics/) · Published 2023-02 · Added 2026-09-28
**Category:** Statistical Modeling · **Tags:** `bayesian-inference`, `shrinkage`, `hierarchical-models`, `survival-analysis`, `conversion-rate`, `censoring`

## TL;DR

Zillow's transaction and engagement team uses Bayesian methods — empirical-Bayes shrinkage toward a population mean and explicit modeling of censored (not-yet-completed) transactions — to measure business outcomes like agent-connection conversion rates, where raw counts are sparse, noisy, and right-skewed with many zero-observation cells.

## 1. Business context

Zillow connects home buyers and sellers with real-estate agents, and a core business question is: how well does a given connection, agent, or market segment convert to an actual transaction? The naive answer — count completed transactions divided by connections — breaks down for the same reason it breaks down in most low-volume, high-value businesses: many segments (a specific agent, a specific zip code, a specific lead source) have too few observations to produce a trustworthy raw rate. The empirical distribution of these conversion rates (CVRs) is heavily right-skewed, with a pile-up of segments showing exactly 0% simply because they haven't had a transaction yet, not because their true rate is zero. On top of that sparsity problem, a real-estate transaction is not a quick, bounded event the way an e-commerce checkout is — it can take months to close, so at the time of measurement a large share of "in-progress" connections are neither successes nor failures but censored observations whose eventual outcome is still unknown.

## 2. Technical details

Zillow's data science team addresses the sparsity problem with a Bayesian (empirical-Bayes-style) approach: rather than trusting each segment's raw observed CVR in isolation, the model treats segment-level rates as draws from a population-level distribution and computes a posterior estimate for each segment that shrinks noisy, low-sample-size raw rates toward the overall mean. The effect reported is exactly what shrinkage estimation predicts — in the posterior distribution of CVRs, the artificial pile-up of 0% estimates disappears and the extreme right-skew of the raw empirical distribution is greatly reduced, with mass moving toward the center of the distribution. This is implemented as (or extended into) a hierarchical Bayesian model, letting the degree of shrinkage vary appropriately by how much data each segment actually has — segments with more observations are trusted more and shrunk less, segments with few observations are pulled harder toward the population estimate. Separately, the team addresses the censoring problem inherent to long-cycle real-estate transactions: because a connection observed today may still convert months from now, the true/false transaction label isn't fully known at measurement time, so the model has to explicitly account for this right-censoring rather than treating an "unconverted-so-far" connection the same as a permanently failed one — the kind of treatment more familiar from survival analysis than from a standard binomial conversion-rate model.

## 3. Impact — potential & realized

The source frames this as Zillow's standard production methodology for measuring business outcomes in the transaction and engagement domain, rather than reporting a one-off experiment with headline metrics. The realized benefit described is qualitative but concrete: business-outcome estimates (like segment-level conversion rates) that are far more stable and trustworthy than raw counts, particularly for the long tail of lower-volume segments that would otherwise show spurious 0% or wildly noisy rates. The broader potential is methodological — the same shrinkage-plus-censoring pattern generalizes to any business with (a) many segments with uneven, often small sample sizes and (b) outcomes that take a long, variable time to resolve, which describes most high-consideration marketplaces (real estate, B2B sales, recruiting, big-ticket e-commerce).

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Textbook techniques, cleanly matched to a real operational pain point

Neither empirical-Bayes shrinkage nor survival-style censoring is new — both are decades-old statistical tools. The value here isn't methodological novelty; it's a clear, production-grounded description of *why* a marketplace business with long, uncertain sales cycles needs both techniques together, and what breaks (0%-inflated, right-skewed rate distributions; biased "unconverted" labels) if you skip either one. That combination is common enough in practice, and skipped often enough in practice, to be a useful reminder rather than a novel contribution.

### Similar / related work

- [**This Is How We Do Modern Frequentist Statistics: Using Fake-Data Simulation to Understand What Can Happen in a Study**](2026-09-25-gelman-fake-data-simulation-frequentist.md) (in this bank) — a different Gelman-adjacent take on making inference assumptions explicit before trusting a result, in the study-design rather than production-monitoring setting.
- [**Decoding Causal Incrementality in E-Commerce: Leveraging Bayesian Structural Time Series Model with a Real-World Example**](2026-09-19-walmart-bayesian-structural-time-series.md) (in this bank) — another production application of Bayesian modeling to a business-outcome measurement problem, using counterfactual time series rather than hierarchical shrinkage.
- **Empirical Bayes / James-Stein shrinkage estimation** (general statistical literature) — the classical result that shrinking many noisy group-level estimates toward a common mean reduces total estimation error, which is the statistical backbone of this post's approach.

### Jargon buster

- **Empirical-Bayes shrinkage** — estimating a population-level distribution from the data itself, then using it as a prior to pull individual (noisy, low-sample-size) estimates toward the population mean, reducing their variance at the cost of a little bias.
- **Hierarchical Bayesian model** — a model with multiple levels of randomness (e.g., segment-level rates drawn from a population-level distribution), which naturally implements shrinkage and lets the amount of shrinkage adapt to each segment's sample size.
- **Right-censoring** — when the true outcome of an observation isn't yet known at analysis time because the event (e.g., a transaction closing) hasn't had time to happen, so the observation can't simply be labeled a failure.
