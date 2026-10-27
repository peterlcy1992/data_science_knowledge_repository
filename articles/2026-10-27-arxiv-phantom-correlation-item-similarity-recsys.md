---
id: arxiv-phantom-correlation-item-similarity-recsys
title: "Do Similarity Measures Measure Similarity? How User Activity Creates Phantom Correlation in Recommender Systems"
source: "arXiv cs.IR (Favier et al., University of Antwerp)"
url: "https://arxiv.org/abs/2610.35765"
published: "2026-10"
added: "2026-10-27"
category: personalization-recsys
tags: [item-item-similarity, collaborative-filtering, popularity-bias, rasch-model, implicit-feedback, measurement]
novelty: 4
sourced_via: "full-text fetch"
---

# Do Similarity Measures Measure Similarity? How User Activity Creates Phantom Correlation in Recommender Systems

**Source:** [arXiv cs.IR (Favier et al., University of Antwerp)](https://arxiv.org/abs/2610.35765) · Published 2026-10 · Added 2026-10-27
**Category:** personalization-recsys · **Tags:** `item-item-similarity`, `collaborative-filtering`, `popularity-bias`, `rasch-model`, `implicit-feedback`, `measurement`

## TL;DR

Even if every user consumed items completely independently and differed only in how much they consume, standard item-item similarity measures (lift, cosine, Pearson, EASE) still show strong associations. The authors call this phantom correlation, model it with a Rasch model, and show on MovieLens that activity alone explains most of the typical pair's association, so genuine taste lives in the deviations.

## 1. Business context

Item-item similarity ('consumed by the same users') underlies item-kNN, SLIM and EASE and is often the baseline for more complex recommenders. The implicit assumption is that co-occurrence reflects shared taste. User activity is highly heterogeneous (heavy-tailed history lengths), so the paper asks how much of the observed association would exist with no taste structure at all. The toy case: 100 equally liked films, half the users watch each film with probability 0.01 and half with 0.20, independently; lift still shows films appearing together about 1.82 times more often than chance.

## 2. Technical details

Three assumptions (independent consumption given an activity trait θ; activity raises the probability of every item while preserving popularity order; the count of consumed items is a sufficient statistic for θ) are shown to be equivalent to a Rasch model: logit P(X_i=1|θ)=h_i+θ, i.e. a more active user has the odds of every item multiplied by the same factor. Consequences: total item-item covariance equals Var(S) − Σ p_i(1−p_i) for any distribution (S is the basket size); every pair is non-negatively correlated under the first two assumptions; and the dependence on item popularity is derived exactly for lift (tending to 1 + Var(e^θ)/E[e^θ]² for rare items and decreasing in popularity), with cosine and Pearson following from lift. EASE is studied empirically by computing it on the model's expected Gram matrix. The model is fitted by EM with a discrete distribution over activity levels.

## 3. Impact — potential & realized

Realized (as reported): datasets MovieLens-1M and 20M (ratings ≥4 as consumption), Last.fm (each user's top 50 artists) and Amazon Books (5-core). On MovieLens-1M, 81% of item pairs have observed co-occurrence within a factor of two of what activity implies, against 35% under independence; activity removes most of the mismatch of independence on both MovieLens sets, about half on Amazon Books, and nothing on Last.fm, where lists are capped and history lengths vary less than under independence, so the model's assumptions fail. What activity does not explain: the Spearman correlation between observed and modeled lift over pairs is only 0.31 on MovieLens-1M, and only the data contain negatively correlated pairs. Implications the authors draw: cosine inherits a baseline that grows with popularity (a head start for popular items unrelated to taste), lift/PMI a baseline largest for rare items. They state they are not claiming collaborative-filtering signals are fake, are not proposing a test, and that whether the baseline biases final recommendations is future work.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A crisp, measurement-minded reframing: similarity = activity baseline + taste deviations.

This is a Simpson's-paradox-style warning that any data scientist reading co-occurrence as affinity should internalize. The practical move is to benchmark similarity scores against an activity-only null (e.g. the Rasch-based expectation) and look at deviations. It also hints at why popularity bias appears before any model is trained. It stops short of showing downstream recommendation gains, so it is a diagnostic rather than a new recommender.

### Similar / related work

- [**Hierarchical GTV Estimation: Bridging the Gap between Container-Level Ranking and Item-Level Conversion**](2026-10-26-meituan-hierarchical-gtv-estimation-hge.md) (in this bank) — another case of reading a noisy aggregate signal correctly before modelling

### Jargon buster

- **Lift** — How much more often two items co-occur than expected if they were independent; log lift is pointwise mutual information.
- **Rasch model** — A psychometric model where each person has one latent trait and the odds of every item scale by the same factor.
- **EASE** — A closed-form linear item-item recommender that regresses each item on all the others with an L2 penalty.
- **Implicit feedback** — Observed interactions (watched, clicked) with no explicit rating; a zero mixes dislike with never-seen.
