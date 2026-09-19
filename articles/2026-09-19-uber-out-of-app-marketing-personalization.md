---
id: uber-out-of-app-marketing-personalization
title: "Personalized Marketing at Scale: Uber's Out-of-App Recommendation System"
source: "Uber Engineering"
url: "https://www.uber.com/blog/personalized-marketing-at-scale/"
published: "2024-06"
added: "2026-09-19"
category: personalization-recsys
tags: [out-of-app-marketing, candidate-retrieval, learning-to-rank, embeddings, feature-store]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Personalized Marketing at Scale: Uber's Out-of-App Recommendation System

**Source:** [Uber Engineering](https://www.uber.com/blog/personalized-marketing-at-scale/) · Published 2024-06 · Added 2026-09-19
**Category:** Personalization & Recommender Systems · **Tags:** `out-of-app-marketing`, `candidate-retrieval`, `learning-to-rank`, `embeddings`, `feature-store`

## TL;DR

Uber describes the recommendation system behind its out-of-app (OOA) marketing — the restaurant and merchant offer recommendations sent via email, push, and SMS to over 4 billion messages. Unlike in-app recommendations, OOA has to work without knowing when or where the user will actually engage, so the system (candidate retrieval → first-pass ranking → learning-to-rank → rule-based re-ranking/blending) leans on predicted future locations, compressed cuisine-preference embeddings, and Bayesian preference updating, reporting a 4% CTR lift in email from one specific improvement.

## 1. Business context

Out-of-app communication — email, push notifications, SMS — is a major growth lever for Uber, letting marketing, product, and operations teams reach users about promotions, favorite restaurants, and merchant offers outside the app session itself. It differs fundamentally from in-app recommendations in three ways the team calls out: there's no live context (the system doesn't know where or when the user will next open the app, unlike an in-app session where location and intent are immediately available), messages need to serve multiple, sometimes competing marketing objectives (a membership promotion push versus a neighborhood-highlight push), and cost management matters a lot — online feature storage, real-time prediction serving, and high-throughput batch processing across billions of messages are each significant expenses that have to be optimized, not just accuracy.

## 2. Technical details

The system is a multi-stage pipeline. **Candidate retrieval** draws on Uber's Local Graph knowledge base to find merchants near where the user is *predicted* to be — since OOA messages are composed without a live session, the system uses ML to forecast a user's likely next ordering location from roughly 10 compressed signals distilled from multi-year Uber and Uber Eats history, with event-based overrides for special contexts like being at an airport. **First-pass ranking** applies fast, low-cost linear scoring and deduplication across the retrieved candidates to cut the set down before expensive scoring, prioritizing recall and computational cheapness. **Second-pass ranking** is where the more sophisticated learning-to-rank models run, built on Uber's Palette Feature Store and Michelangelo ML platform. Two specific innovations here: a cuisine-preference embedding compressed to roughly 10x smaller than its original size while preserving predictive signal (validated with spectral clustering and t-SNE visualization showing the compressed embeddings still recover natural cuisine groupings), and Bayesian updating of these preferences so they shift with a user's recent behavior rather than staying static. Finally, **re-ranking and blending** runs through a rule engine (internally called Flipr) built on CEL (Common Expression Language), letting regional marketing teams adjust merchant visibility through hierarchical, inheritable configuration — so a global default can be locally overridden without duplicating logic per region.

## 3. Impact — potential & realized

**Realized:** the cuisine-preference smoothing feature (the compressed, Bayesian-updated embedding) drove a reported 4% lift in email click-through rate in online experimentation. The 10x compression of cuisine embeddings is reported to meaningfully cut storage cost while preserving recommendation quality, directly addressing the cost-management constraint called out as a core challenge for OOA at this scale.

**Potential:** the location-prediction approach for candidate retrieval (forecasting where a user will likely be, rather than requiring a live session) is a transferable pattern for any product recommending location-anchored content asynchronously — travel, local services, delivery — where the recommendation has to be composed before the moment of intent is known. The rule-engine-based re-ranking layer (Flipr) is also a reusable pattern for letting non-ML teams (regional marketing) safely adjust ML-driven output without needing to retrain or redeploy models.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a well-engineered production system, incremental on known techniques

Candidate retrieval → ranking → rule-based blending is a standard recsys pipeline shape, and nothing here is architecturally new. The genuinely interesting bit is solving for the *missing-context* problem specific to out-of-app channels — predicting where a user will be rather than knowing where they are — plus the pragmatic 10x embedding compression that's explicitly justified by the cost structure of serving billions of messages, not just by accuracy. It's a strong example of a recsys team designing for the actual constraints of their channel rather than porting an in-app recommender unchanged.

### Similar / related work

- [**Scaling Personalized Marketing for Multi-Tenant Commerce Platforms**](2026-09-18-instacart-scaling-personalized-marketing-multi-tenant.md) (in this bank) — a closely related problem (personalized marketing recommendations at scale) tackled in a multi-tenant retail-media context rather than Uber's single-platform OOA setting.
- [**Enhancing Personalized CRM Communication with Contextual Bandit Strategies**](2026-09-03-uber-crm-contextual-bandits-genai-embeddings.md) (in this bank) — Uber's own separate CRM personalization system, using contextual bandits and GenAI embeddings — a useful contrast in technique (bandit-driven exploration vs. this piece's supervised learning-to-rank pipeline) for a related communications-personalization problem within the same company.
- [**Matching LinkedIn Members with the Right Premium Products**](2026-09-02-linkedin-premium-product-two-tower-bandits.md) (in this bank) — another marketing/product-recommendation system combining retrieval-style modeling with bandit-based ranking, for a different but adjacent business problem (subscription upsell vs. restaurant discovery).

### Jargon buster

- **Out-of-app (OOA) marketing** — communications sent to users outside the app itself (email, push notifications, SMS), as opposed to in-app recommendations shown during an active session.
- **Learning-to-rank** — a class of ML models trained specifically to order a list of candidates by relevance, rather than to make an independent prediction per item; used here in the second-pass ranking stage.
- **CEL (Common Expression Language)** — a small, safe expression language (used by Google and others) for evaluating simple logic rules at runtime; here it powers Flipr, the rule engine marketing teams use to adjust recommendation output without code changes.
