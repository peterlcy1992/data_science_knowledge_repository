---
id: wantedly-retention-focused-recommendation-job-matching
title: "Not All Matches Are Equally Valuable: An Online Experiment of Retention-Focused Recommendation in a Job-Matching Platform"
source: "Wantedly (arXiv paper)"
url: "https://arxiv.org/abs/2609.01652"
published: "2026-09"
added: "2026-09-04"
category: experimentation-causal
tags: [recsys, churn, online-experiment, job-matching, reranking, ab-testing]
novelty: 3
sourced_via: "web search"
---

# Not All Matches Are Equally Valuable: An Online Experiment of Retention-Focused Recommendation in a Job-Matching Platform

**Source:** [Wantedly (arXiv paper)](https://arxiv.org/abs/2609.01652) · Published 2026-09 · Added 2026-09-04
**Category:** Experimentation & Causal Inference · **Tags:** `recsys`, `churn`, `online-experiment`, `job-matching`, `reranking`, `ab-testing`

## TL;DR

Researchers at Wantedly (a job-matching platform) ran a live online experiment testing whether reranking recommendations to boost matches for at-risk (low-match) users — instead of optimizing purely for match quality — reduces user churn; the treatment group showed directionally lower churn than the match-focused control, though the effect was not statistically significant at conventional levels, and employer-side churn did not worsen.

## 1. Business context

Most production recommender systems, including job-matching platforms, are tuned to maximize immediate engagement or match-quality metrics like click-through or match rate. But a platform's real objective is often retention: keeping users active long enough to eventually find (or fill) a good match. The authors observed that on their platform, users who receive very few recent matches are substantially more likely to leave, while giving *more* matches to users who are already getting plenty of high-quality matches adds little additional retention value — the marginal value of an extra match is not uniform across users. This motivated testing a policy that explicitly reallocates recommendation attention toward users at risk of churning, rather than treating every match opportunity as equally valuable.

## 2. Technical details

- **Approach:** a post-processing reranking layer applied on top of the platform's existing match-focused ranking — rather than retraining the base ranking model, the team adjusted final scores to boost visibility for users identified as being at higher churn risk (operationalized via recent match count).
- **Signal used:** recent match count as a proxy for churn risk — users with very few recent matches were identified as the population where additional matches were hypothesized to have outsized retention value.
- **Experiment design:** a live online A/B experiment on the production job-matching platform (not an offline simulation), comparing the retention-focused reranking treatment against the standard match-quality-focused control.
- **Metrics tracked:** user-side churn (the primary retention outcome) and employer-side churn (a guardrail metric, to check the intervention doesn't harm the employer side of the marketplace by, e.g., diluting match relevance).
- **Venue:** submitted to RecSys in HR '26, the workshop on recommender systems for human resources, held alongside ACM RecSys 2026 in Minneapolis (Sept 28 – Oct 2, 2026).

## 3. Impact — potential & realized

- **Realized:** the treatment group showed directionally lower user churn than the match-focused control group, but the estimated effect was **not statistically significant at conventional levels** — an honest, inconclusive-but-suggestive result rather than a confirmed win. Employer-side churn did not deteriorate, meaning the reallocation toward at-risk users did not measurably hurt the marketplace's other side.
- **Potential:** the core idea — that the marginal value of a recommendation is heterogeneous across users, and that optimizing for retention risk rather than uniform match quality can be tested live without harming the platform's other side — generalizes to any two-sided marketplace (dating, marketplace lending, gig work) where naive engagement-metric optimization may over-serve already-satisfied users at the expense of retaining at-risk ones.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a well-designed live experiment on a genuinely underexplored question, with an honest null-ish result

The idea that recommendation value is heterogeneous by user retention-risk, not just by predicted relevance, is not brand new in the causal/uplift-modeling literature, but running it as a real online A/B test on a live two-sided job-matching marketplace — and reporting a statistically inconclusive result rather than overselling a directional trend — is a genuinely useful, honest data point that's rarer than it should be in industry writing. It's a 3 rather than higher because the effect itself wasn't confirmed at conventional significance, which limits how much can be concluded from this specific deployment.

### Similar / related work

- [**Bandits for Marketing Optimization at Instacart**](2026-08-30-instacart-bandits-marketing-optimization.md) (in this bank) — another case of a company moving from a "treat everyone the same" optimization target to one that accounts for individual-level marginal value.
- [**The Quest to Understand Metric Movements**](2026-08-31-pinterest-metric-movements-root-cause-analysis.md) (in this bank) — a different experimentation-adjacent problem (diagnosing *why* a metric moved) from the same broad discipline of rigorous, honest measurement in production systems.
- [**Off-Policy Evaluation and Learning for Matching Markets**](https://arxiv.org/pdf/2507.13608) — related work from overlapping authors on evaluating and learning policies specifically for matching-market settings like job platforms.

### Jargon buster

- **Churn** — a user leaving or becoming inactive on a platform; the primary outcome this experiment tries to reduce.
- **Reranking (post-processing)** — adjusting a ranking model's output scores after the fact (rather than retraining the underlying model) to account for an additional objective, here retention risk.
- **Guardrail metric** — a secondary metric tracked during an experiment specifically to catch unintended harm from the treatment (here, employer-side churn, to ensure the change didn't hurt the marketplace's other side even while helping the metric being optimized).
- **Statistical significance** — a threshold (conventionally p < 0.05) for judging whether an observed effect is unlikely to be due to chance alone; a "directional but not significant" result means the data trend the expected way but isn't strong enough to rule out chance.
