---
id: arxiv-hierarchical-eb-sparse-counts-airline-demand
title: "Hierarchical Empirical-Bayes Forecasting of Sparse Counts with Exposure: An Application to Airline Demand and Premium-Cabin Capacity Sharing"
source: "arXiv stat.AP (Irakli Gudavadze)"
url: "https://arxiv.org/abs/2611.14530"
published: "2026-11"
added: "2026-11-16"
category: forecasting-timeseries
tags: [intermittent-demand, empirical-bayes, poisson-gamma, negative-binomial, partial-pooling, probabilistic-forecasting, airline-revenue-management, overdispersion]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "arXiv stat.AP listing (backlog stub)"
---

# Hierarchical Empirical-Bayes Forecasting of Sparse Counts with Exposure: An Application to Airline Demand and Premium-Cabin Capacity Sharing

**Source:** [arXiv stat.AP (Irakli Gudavadze)](https://arxiv.org/abs/2611.14530) · Published 2026-11 · Added 2026-11-16
**Category:** forecasting-timeseries · **Tags:** `intermittent-demand`, `empirical-bayes`, `poisson-gamma`, `negative-binomial`, `partial-pooling`, `probabilistic-forecasting`, `airline-revenue-management`, `overdispersion`

## TL;DR

For thin markets with many zeros and varying exposure, a hierarchical exposure-adjusted Poisson–Gamma (HEPG) model gives closed-form partial pooling: Gamma posteriors and negative-binomial predictive distributions. An adaptive variant (A-HEPG) adds a moment-matched negative-binomial variance correction when extra-Poisson variation remains. In synthetic experiments with 400 markets it beats complete pooling and route-level Poisson MLE on log score; a premium-cabin example turns the predictive distribution into a seat-protection rule. Evaluation is synthetic only.

## 1. Business context

Sparse-count forecasting shows up whenever events are rare relative to opportunities: failures, claims, intermittent purchases, low-frequency booking requests. In airline revenue management it appears at fine granularity (origin–destination market, fare family, booking-window interval, new routes), where forecasts feed seat protection, availability and pricing. Route-level maximum-likelihood estimates collapse to zero for zero-history or low-exposure units, while complete pooling ignores real heterogeneity. A related operational problem is premium-cabin capacity sharing — selling extra economy seats when premium seats are expected to stay empty, at the risk of displacing later premium demand. The paper's contribution is deliberately narrow: show how a sparse premium-demand predictive distribution can feed a transparent protection rule whose aggressiveness changes with the premium–economy fare gap.

## 2. Technical details

- **Model.** Conditional counts are Poisson with an exposure offset and pooled calendar effects; unit-specific baseline intensities get a Gamma prior whose hyperparameters are estimated empirically across the population (empirical Bayes). Posterior is Gamma; posterior predictive is negative binomial — closed-form shrinkage and explicit propagation of parameter uncertainty.
- **A-HEPG.** Uses the HEPG posterior mean as the stable route intensity, diagnoses residual extra-Poisson variation, and applies a moment-matched negative-binomial variance correction — framed as diagnostic model escalation rather than a new model.
- **Comparators.** Pooled Poisson, route-level Poisson MLE, a weak-prior Poisson–Gamma, HEPG, A-HEPG; scored by average negative log predictive probability (NLL) and other metrics.
- **Decision layer.** A premium-cabin seat-protection rule based on predictive survival probabilities and fare ratios.

## 3. Impact — potential & realized

**Measured (synthetic, 400 heterogeneous markets):**
- At a mean latent rate of 0.15 requests per exposure unit, NLL is 0.525 for HEPG vs 0.585 pooled Poisson and 0.731 route-level Poisson MLE (weak-prior PG 0.530).
- Under negative-binomial misspecification, A-HEPG and HEPG are nearly identical at mild overdispersion (k=5); at k=2 A-HEPG lowers NLL from 0.529 to 0.524; under strong overdispersion (k=0.8) from 0.552 to 0.529.

**Not measured:** no real airline data and no revenue result. **Potential:** a cheap, auditable baseline for any intermittent-demand problem with exposure (claims, spare parts, new SKUs), and a clean example of wiring a predictive distribution into a decision rule rather than a point forecast.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Textbook Poisson–Gamma, well framed for a real decision

Poisson–Gamma empirical Bayes is decades old; the value is in packaging it for exposure-varying, zero-heavy units, the "escalate only if the diagnostics ask" stance, and the direct link to a seat-protection decision. Synthetic-only evaluation caps the score. Forecasting teams tempted to throw a foundation model at intermittent demand should benchmark against exactly this first.

### Similar / related work

- [**The Forecast Says Zero. The Warehouse Says Otherwise.**](2026-09-25-nixtla-intermittent-demand-zero-forecast-trap.md) (in this bank) — the same zero-forecast trap from the inventory side.
- [**Exploratory creative pre-ranking: Hierarchical empirical-Bayes Thompson sampling**](2026-10-29-roblox-creative-pre-ranking-empirical-bayes-thompson-sampling.md) (in this bank) — hierarchical EB shrinkage for sparse data in an ads/creative setting.
- [**Partial pooling beats synthetic respondents as estimators, not as covariates**](2026-11-13-arxiv-partial-pooling-vs-synthetic-respondents-small-area.md) (in this bank) — partial pooling winning in small samples, in survey estimation.

### Jargon buster

- **Exposure offset** — a term that scales the expected count by opportunity (e.g. number of flights or days on sale), so rates are compared fairly.
- **Partial pooling** — estimating each unit between its own data and the population average, weighted by how much data it has.
- **Negative binomial predictive** — the count distribution you get when a Poisson rate is itself uncertain (Gamma), producing extra variance.
- **Log score / NLL** — average negative log probability assigned to what actually happened; lower means better-calibrated probabilistic forecasts.
