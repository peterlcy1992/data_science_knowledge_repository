---
id: roblox-creative-pre-ranking-empirical-bayes-thompson-sampling
title: "Exploratory creative pre-ranking: Hierarchical empirical-Bayes Thompson sampling for real-time creative optimization"
source: "arXiv (UCLA Statistics & Data Science with Roblox)"
url: "https://arxiv.org/abs/2610.36020"
published: "2026-10"
added: "2026-10-29"
category: personalization-recsys
tags: [creative-optimization, thompson-sampling, empirical-bayes, hierarchical-shrinkage, cold-start, ads-ranking]
novelty: 3
sourced_via: "full-text fetch"
---

# Exploratory creative pre-ranking: Hierarchical empirical-Bayes Thompson sampling for real-time creative optimization

**Source:** [arXiv (UCLA Statistics & Data Science with Roblox)](https://arxiv.org/abs/2610.36020) · Published 2026-10 · Added 2026-10-29
**Category:** Personalization & Recommender Systems · **Tags:** `creative-optimization`, `thompson-sampling`, `empirical-bayes`, `hierarchical-shrinkage`, `cold-start`, `ads-ranking`

## TL;DR

Roblox and UCLA put a creative pre-ranker ahead of ad ranking: each creative sits in a hierarchy (segment, item, campaign, creative), borrows from its parents with a shrinkage strength set in closed form from historical logs, and is selected by one Thompson draw. On replayed Roblox Sponsored-ads traffic the shortlist lifts predicted play-through rate by 8.14% vs 2.80% for an equally sized random shortlist, forwards more than 40% fewer creatives than the full pool, and adds 0.2% serving time. After an A/B test on live traffic it serves in production.

## 1. Business context

Generative AI made ad creatives nearly free, so creative pools are larger than ad pools while feedback per creative is sparse and selection must fit a tight latency budget. Typical systems pick the creative after ranking; recent industrial work puts creative selection before ranking but with deterministic point predictors with no calibrated uncertainty, so a fresh creative is reached only through a separate exploration mechanism.

## 2. Technical details

Creatives sit in a hierarchy of audience segment, advertised item (universe), campaign and creative. A cold creative falls back on parent levels via a Beta-Bernoulli empirical-Bayes cascade whose prior strength per level (one parameter per level, nothing tuned) is estimated in closed form from historical logs using the scatter of children around the parent (a method-of-moments identity). To meet the latency budget the model predicts for an audience segment, not an individual user: single-attribute counters (m*K per node rather than m^K joint cells) give shrunk marginal lifts on the log-odds scale, combined with a linear logit model with one weight per attribute (fitted offline, a logistic regression). Selection is a single Thompson draw per creative; each campaign gets a shortlist share proportional to its pool size, filled to a global budget by round robin so uploading more creatives does not buy exposure. With one draw it is one round of Thompson sampling in a Beta-Bernoulli bandit per campaign. The authors say their contribution is the posterior construction, not a bandit analysis.

## 3. Impact — potential & realized

Realized (replay on logged Roblox Sponsored-ads requests, predicted play-through rate under the most accurate deployed ranking model, 95% request-clustered bootstrap): Algorithm 1 gives +8.14% (CI 7.64 to 8.65) vs +2.80% for round-robin random forwarding 600 creatives; a one-per-campaign Thompson variant gives +6.09% at no extra ranker load; the method recovers 44% of the gain from forwarding every creative (the oracle gives +18.36% at 83.1 ms vs about 41.6 ms) on more than 40% fewer creatives, with 0.2% extra serving time. A second deployed ranker preserved the ordering of methods. About 16.9% of candidates have no effective observations. The rewards come from logged ranker predictions, i.e. predicted rather than observed play-through, and the replay samples a few hundred requests. The live A/B result is stated only qualitatively (it now serves production); no live numbers are given in the text I read.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sensible statistics-first design: shrinkage plus one Thompson draw buys exploration almost for free. Evidence is a replay on predicted rewards, so real gain depends on the live test, which is not quantified.

The reusable idea is a closed-form, tuning-free shrinkage strength for hierarchical cold-start estimates. Likely to be copied wherever generated variants outnumber feedback (ad creatives, notification copy, thumbnails).

### Similar / related work

- [**Reinforcement Learning for Controller Parameters in the Auto-Bidding System at Pinterest**](2026-10-27-pinterest-rlbp-rl-meta-controller-auto-bidding.md) — another ad-system component with a production A/B
- [**LCM-Promo**](2026-10-28-arxiv-lcm-promo-llm-uplift-promotion-allocation.md) — decision-oriented modelling with response-curve structure

### Jargon buster

- **Empirical Bayes** — Estimating the prior (here how much a sparse item should trust its parent) from the data itself.
- **Thompson sampling** — Pick the option whose randomly drawn posterior sample is highest, balancing exploration and exploitation.
- **Pre-ranking** — A cheap stage that shortlists candidates before the expensive ranking model runs.
