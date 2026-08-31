---
id: meta-llatte-ads-ranking-scaling-laws
title: "From User Sequences to Scaling Laws: A Multi-Stage Architecture for Meta's Ads Ranking"
source: "Engineering at Meta"
url: "https://engineering.fb.com/2026/08/05/ml-applications/from-user-sequences-to-scaling-laws-a-multi-stage-architecture-for-metas-ads-ranking/"
published: "2026-08"
added: "2026-08-31"
category: personalization-recsys
tags: [sequence-modeling, ads-ranking, scaling-laws, transformer, latency, semantic-ids]
novelty: 4
sourced_via: "web search"
---

# From User Sequences to Scaling Laws: A Multi-Stage Architecture for Meta's Ads Ranking

**Source:** [Engineering at Meta](https://engineering.fb.com/2026/08/05/ml-applications/from-user-sequences-to-scaling-laws-a-multi-stage-architecture-for-metas-ads-ranking/) · Published 2026-08 · Added 2026-08-31
**Category:** Personalization & Recommender Systems · **Tags:** `sequence-modeling`, `ads-ranking`, `scaling-laws`, `transformer`

## TL;DR

Meta introduces **LLaTTE** (LLM-style Latent Transformers for Temporal
Events), showing that sequence modeling of user interaction history in ads
recommendation follows **predictable power-law scaling** much like LLM
pretraining — but only once semantic features are added. A two-stage
architecture that offloads heavy computation to an asynchronous offline
model, deployed as Meta's largest user model, drove a **4.3% conversion
uplift on Facebook Feed and Reels**.

## 1. Business context

Meta's ranking systems process billions of daily user interactions across
products, ads, and content, and the order and timing of those interactions
carry signal about intent that flat feature aggregates lose. LLMs have shown
that simply scaling a transformer on more data and parameters reliably
improves quality (classic LLM scaling laws) — Meta's question was whether
the same predictable payoff from scale holds for **sequence models of user
behavior in latency-sensitive ads ranking**, where every millisecond of
inference cost is a hard constraint, unlike batch LLM training.

## 2. Technical details

- **LLaTTE architecture.** A scalable transformer built to model user
  behavior as sequences of temporal events (views, clicks, conversions),
  designed to serve as a shared backbone for ads ranking rather than a
  one-off task model.
- **Power-law scaling, conditional on semantic features.** Meta finds that
  sequence-model quality scales as a **predictable power law** with model
  and sequence-length capacity — similar to LLM scaling laws — but only once
  **semantic features** (richer, meaning-carrying representations of
  events, akin to semantic IDs) are included; without them the scaling
  curve bends and plateaus earlier.
- **Two-stage architecture for latency.** To capture scaling benefits under
  a hard serving-latency budget, LLaTTE splits into (1) an **online ranking
  model**, bounded by request-time latency, and (2) an **asynchronous
  offline (upstream) user model** that does the heavy long-context
  computation ahead of time and is not on the request's critical path.
  Scaling the online model yields steeper per-compute gains; scaling the
  offline model improves more gradually but avoids latency limits entirely
  because its inference is async.
- **Sequence length and diversity both matter.** Quality keeps improving as
  input sequences get longer, and a **diverse mix of action types**
  (views, clicks, conversions together) outperforms sequences built from a
  single action type — mirroring how data diversity helps LLM pretraining.

## 3. Impact — potential & realized

- **Realized:** deployed as **the largest user model at Meta**, the
  multi-stage LLaTTE framework produced a **4.3% conversion uplift on
  Facebook Feed and Reels** with minimal added serving overhead, by keeping
  the heavy computation off the latency-critical path.
- **Potential:** establishing that recommendation sequence models obey
  LLM-like scaling laws (conditional on semantic features) gives Meta — and
  by extension the field — a principled way to forecast the ROI of further
  scaling investment, rather than scaling ad hoc and hoping for gains.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a genuine scaling-law result for production ads ranking, not just a bigger model

Plenty of teams have scaled up ranking sequence models and reported a lift;
fewer have characterized the scaling behavior as a **power law conditional
on a specific design choice** (semantic features) and then engineered around
a latency constraint with an async offline/online split to actually capture
it in production. That combination — scaling-law characterization plus a
concrete serving-architecture answer to the latency problem it creates — is
a step beyond "we made the model bigger." It's not a 5 because the
LLM-scaling-law framing itself is imported from language modeling rather
than a new theoretical result.

### Similar / related work

- [**GEM Training: How Meta Doubled the Efficiency of Its LLM-Scale Ads
  Foundation Model**](2026-08-31-meta-gem-training-llm-scale-ads-efficiency.md) (in this bank) — the training-efficiency companion
  piece; GEM is the foundation model, LLaTTE is Meta's sequence-modeling
  ranking research feeding into that same ads-ranking stack.
- [**Towards Generalizable and Efficient Large-Scale Generative
  Recommenders**](https://arxiv.org/abs/2605.23312) — Netflix's own study of scaling laws for a generative
  recommender backbone (2M → 1B parameters), a close industry parallel.
- **Meta Adaptive Ranking Model** ("Bending the Inference Scaling Curve to
  Serve LLM-Scale Models for Ads," Engineering at Meta, Mar 2026) — Meta's
  earlier work on serving LLM-scale ranking models within latency budgets,
  which this async two-stage design builds on.

### Jargon buster

- **Scaling law** — an empirical relationship (often a power law) between
  model/data/compute size and resulting model quality, first popularized
  for LLM pretraining; here shown to also hold for sequence models of user
  behavior in ads ranking.
- **Semantic features** — feature representations that encode the *meaning*
  of an event (e.g., what kind of ad, what category of action) rather than
  just a raw ID, similar in spirit to semantic IDs used elsewhere in
  generative recommendation.
- **Two-stage online/offline architecture** — splitting a model into a
  latency-bounded piece that runs at request time and a heavier piece that
  runs ahead of time (asynchronously), so the expensive computation doesn't
  have to fit inside the serving latency budget.
- **Temporal events** — a user's interactions represented as a
  timestamped, ordered sequence (rather than an unordered feature bag), so
  the model can learn from the order and timing of actions, not just their
  existence.
