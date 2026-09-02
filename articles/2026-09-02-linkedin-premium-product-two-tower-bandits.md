---
id: linkedin-premium-product-two-tower-bandits
title: "Matching LinkedIn Members with the Right Premium Products"
source: "LinkedIn Engineering"
url: "https://www.linkedin.com/blog/engineering/machine-learning/matching-linkedin-members-with-the-right-premium-products"
published: "2024-05"
added: "2026-09-02"
category: personalization-recsys
tags: [two-tower, contextual-bandits, thompson-sampling, multi-armed-bandit, personalization]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Matching LinkedIn Members with the Right Premium Products

**Source:** [LinkedIn Engineering](https://www.linkedin.com/blog/engineering/machine-learning/matching-linkedin-members-with-the-right-premium-products) · Published 2024-05 · Added 2026-09-02
**Category:** Personalization & Recommender Systems · **Tags:** `two-tower`, `contextual-bandits`, `thompson-sampling`, `multi-armed-bandit`, `personalization`

## TL;DR

LinkedIn built a two-tower neural network plus Neural Thompson Sampling to jointly pick the best Premium product, creative, and channel for each member, treating every (product, creative, channel) combination as a bandit "arm" — lifting platform conversion 0.7% and cutting experiment-launch time enough to run 4x more experiments in two months.

## 1. Business context

LinkedIn offers four Premium product tiers and can reach members through multiple channels with many possible creatives (messaging/design variants). Picking badly on any of the three dimensions — wrong product, wrong message, wrong channel, or wrong timing — risks annoying the member and losing a real opportunity to show them something valuable. Treating product choice, creative choice, and channel choice as three separate optimization problems misses interactions between them, and manually authoring and testing every combination doesn't scale to the full space of options.

## 2. Technical details

- **Framing as a bandit problem.** Every valid (product, creative, channel) triplet is treated as one "arm." The system's job on each impression is to choose the arm expected to maximize a combined objective of lifetime value (LTV), conversion probability, and member-reward signals.
- **Two-tower architecture.** A **member tower** encodes profile data, activity history, derived AI signals, and context (device, time of day); an **arm tower** encodes the creative's text (via LLM embeddings), the product as a one-hot feature, and the channel as a one-hot feature. Both towers can be pre-computed offline, keeping online serving latency low.
- **Deep matching layer.** Dense layers combine the member and arm embeddings to predict interaction probability, trained so that embeddings for well-matched (member, arm) pairs cluster together in the shared space.
- **Neural Thompson Sampling.** Explore/exploit is handled via Thompson Sampling using a last-layer weight approximation, letting the system keep gathering information on under-explored arms while naturally narrowing exploration as confidence grows — without a separate, hand-tuned exploration schedule.
- **Training and serving.** The model retrains on a batch cadence of every few hours; new arms can be scored immediately via their encoded attributes, without needing to retrain first. Initial data collection used random arm assignment to avoid bootstrapping bias, and automated A/B comparisons gate each model update before it reaches production.

## 3. Impact — potential & realized

- **Realized:** platform conversion rate up **+0.7%** without hurting member retention; experimentation velocity up **10x**, enabling four production experiments across hundreds of creatives and multiple channels within two months — a pace the prior per-arm manual process couldn't support.
- **Potential:** the team describes a path toward Deep Q-Networks for optimizing over a member's longer career trajectory (rather than single-impression reward), and toward using generative AI to scale creative authoring itself, beyond the current manually authored creative set.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid contextual-bandit engineering, not a new method

Two-tower retrieval and Thompson Sampling are both well-established techniques; the contribution here is combining them into a single system that jointly optimizes product, creative, and channel as one bandit action space, and getting real production lift and a large experimentation-velocity gain out of it. It's a well-executed, LinkedIn-scale application rather than a new algorithmic idea, which is why it sits at 3 rather than higher — though the reported 10x jump in experiment throughput is a genuinely useful practical result.

### Similar / related work

- [**Bandits for Marketing Optimization at Instacart**](2026-08-30-instacart-bandits-marketing-optimization.md) (in this bank) — the same explore/exploit bandit framing applied to marketing spend allocation rather than product/creative/channel selection.
- [**Enhancing "You May Also Like" (YMAL) Systems using LLMs and Word2Vec**](2026-09-01-cvs-product-rec-word2vec-llm.md) (in this bank) — a different, much simpler use of LLM-derived features (product-description embeddings) inside a classical recommender, versus this system's use of LLM embeddings inside a bandit arm tower.

### Jargon buster

- **Multi-armed bandit** — a decision-making framework for repeatedly choosing among options ("arms") with unknown reward, balancing trying new options (explore) against picking known-good ones (exploit).
- **Thompson Sampling** — a bandit algorithm that samples from each arm's estimated reward distribution and picks the highest sample, naturally balancing exploration and exploitation as uncertainty shrinks.
- **Two-tower model** — an architecture with two separate neural encoders (here, member and arm) that map inputs into a shared embedding space, so similarity/relevance can be computed cheaply, often with one side pre-computed offline.
- **Lifetime value (LTV)** — a prediction of the total value a customer will generate over their relationship with a product, used here as part of the optimization objective alongside immediate conversion.
