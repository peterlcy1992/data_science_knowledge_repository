---
id: swiggy-predicted-lifetime-value-multitask-mlp
title: "Swiggy's In-House Predicted Lifetime Value Model for Customer Acquisition"
source: "Swiggy (via InfoQ)"
url: "https://www.infoq.com/news/2026/09/swiggy-pltv-multitask-mlp/"
published: "2026-09"
added: "2026-09-04"
category: personalization-recsys
tags: [pltv, multi-task-learning, marketing-optimization, customer-acquisition, ads-bidding]
novelty: 3
sourced_via: "web search"
---

# Swiggy's In-House Predicted Lifetime Value Model for Customer Acquisition

**Source:** [Swiggy (via InfoQ)](https://www.infoq.com/news/2026/09/swiggy-pltv-multitask-mlp/) · Published 2026-09 · Added 2026-09-04
**Category:** Personalization & Recommender Systems · **Tags:** `pltv`, `multi-task-learning`, `marketing-optimization`, `customer-acquisition`, `ads-bidding`

## TL;DR

Swiggy replaced third-party predicted-lifetime-value (pLTV) platforms with an in-house multi-task MLP that estimates a prospective customer's value before their first order, using 350+ pre-order features and an order-count auxiliary task that cut the model's parameter count by 63% while improving accuracy — the resulting signal now feeds Google Target ROAS bidding for acquisition marketing.

## 1. Business context

Swiggy (Indian food delivery and quick-commerce) spends on paid acquisition across its Food delivery and Instamart (quick commerce) businesses, and wants to bid more for prospective customers likely to become high-value long-term users rather than bidding uniformly. Prior to this work, Swiggy relied on third-party pLTV platforms to estimate a prospect's future value from pre-order signals, at additional platform cost and without full control over feature access or ranking quality. Building the model in-house let Swiggy fold in proprietary data (device/fraud signals, category affinity, socioeconomic indicators) that a third-party vendor would not have access to, and tie the resulting score directly into paid-media bidding.

## 2. Technical details

- **Architecture:** a multilayer perceptron with three shared hidden layers, followed by four task-specific heads — value prediction for Food, value prediction for Instamart, and order count as an auxiliary prediction task for each business unit.
- **Features:** 350+ pre-order features spanning acquisition channel, device and fraud signals, geography, complaint history, category affinity, payment patterns, and socioeconomic indicators — all available before a prospect places their first order.
- **Auxiliary-task trick:** adding order count as a secondary prediction target (rather than training only on the value regression target) let Swiggy shrink the shared representation substantially: total parameters dropped from 363,000 to 135,000 (a 63% reduction) while producing marginally better value predictions — a case of an auxiliary task acting as a strong regularizer on the shared layers.
- **Evaluation approach:** rather than standard regression error metrics, Swiggy evaluated whether the model correctly *ranks* customers by value — splitting predicted and actual values into ten quantile (decile) groups and measuring how often a customer's predicted decile matches their actual decile. This is a better fit than raw regression error for a value distribution dominated by many zero-value users and a long tail of high-value users. The model achieved a Spearman correlation above 0.75 for both business units and 70-80% decile-diagonal coverage.
- **Serving:** the resulting pLTV score is used as a bidding signal fed into Google's Target ROAS (return on ad spend) bidding for customer acquisition campaigns.

## 3. Impact — potential & realized

- **Realized:** the in-house model delivered higher retention and gross order value per acquired user compared to the third-party pLTV platform it replaced, without incurring the third party's platform fees. Spearman correlation above 0.75 and 70-80% decile-diagonal coverage on both Food and Instamart.
- **Potential:** Swiggy states it plans to move from point predictions toward probabilistic predictions that carry uncertainty into the bidding decision itself — letting the bidding system account for confidence, not just a point estimate of value, when spending marketing budget.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a clean production pattern, not a new idea

pLTV modeling with multi-task MLPs is well-established (both in industry practice and in the academic CLV literature); Swiggy's specific contribution is the disciplined production execution — the auxiliary order-count task as an explicit parameter-reduction lever, the quantile-ranking evaluation suited to a zero-inflated, long-tailed target, and the direct wiring into a live bidding system rather than a static score. That is genuinely useful applied engineering, but it is a strong production-first take on known techniques rather than a new modeling idea, which is why it lands at a 3.

### Similar / related work

- [**Bandits for Marketing Optimization at Instacart**](2026-08-30-instacart-bandits-marketing-optimization.md) (in this bank) — another production marketing-optimization system, using contextual bandits rather than a supervised pLTV score, for a related "who to spend acquisition/promo budget on" decision.
- [**Enhancing Personalized CRM Communication with Contextual Bandit Strategies**](2026-09-03-uber-crm-contextual-bandits-genai-embeddings.md) (in this bank) — Uber's marketing-decisioning system, a useful contrast in how two companies wire ML signals into downstream marketing spend decisions.
- [**Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou**](https://arxiv.org/pdf/2208.13358) — an earlier industrial CLV paper covering similar multi-task and long-tail-distribution challenges at a different company.

### Jargon buster

- **pLTV (predicted lifetime value)** — a model's estimate, made before or shortly after a customer's first interaction, of how much total value (orders, revenue, retention) that customer will generate over their lifetime with the product.
- **Multi-task learning** — training one shared network to predict several related targets at once (here, Food value, Instamart value, and order count), which can improve generalization and, as seen here, let a smaller shared representation suffice.
- **Target ROAS bidding** — a Google Ads bidding strategy where the advertiser gives Google a target return-on-ad-spend ratio and lets the auction system pace and price bids to hit it; feeding in a per-prospect pLTV score lets bids vary by expected value rather than being uniform.
- **Spearman correlation** — a statistic measuring how well the *rank order* of two variables agrees, used here to judge whether the model correctly orders customers from low to high value even if its absolute value predictions are imperfect.
