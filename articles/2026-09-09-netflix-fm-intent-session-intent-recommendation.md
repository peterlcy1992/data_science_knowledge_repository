---
id: netflix-fm-intent-session-intent-recommendation
title: "FM-Intent: Predicting User Session Intent with Hierarchical Multi-Task Learning"
source: "Netflix Technology Blog"
url: "https://netflixtechblog.com/fm-intent-predicting-user-session-intent-with-hierarchical-multi-task-learning-94c75e18f4b8"
published: "2025-05"
added: "2026-09-09"
category: personalization-recsys
tags: [multi-task-learning, session-intent, foundation-model, transformer, user-modeling, netflix]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# FM-Intent: Predicting User Session Intent with Hierarchical Multi-Task Learning

**Source:** [Netflix Technology Blog](https://netflixtechblog.com/fm-intent-predicting-user-session-intent-with-hierarchical-multi-task-learning-94c75e18f4b8) · Published 2025-05 · Added 2026-09-09
**Category:** Personalization & Recommender Systems · **Tags:** `multi-task-learning`, `session-intent`, `foundation-model`, `transformer`, `user-modeling`, `netflix`

## TL;DR

Netflix extended its recommendation foundation model with FM-Intent, which explicitly predicts *why* a user is engaging in a session — discovery versus continuation, genre preference, content-type preference, and new-versus-old content — and then feeds that predicted intent into next-item recommendation as a hierarchical input, rather than treating intent and item prediction as separate, parallel tasks. The result was a statistically significant 7.4% improvement in next-item prediction accuracy over Netflix's previous state of the art (TransAct) in offline experiments.

## 1. Business context

Netflix's foundation model was already good at predicting *what* a member might watch next, but it had no explicit model of *why* — whether the member was in the mood to discover something new, continue a show they'd started, revisit a favorite genre, or catch up on recent releases versus older catalog titles. That gap matters commercially because the "why" changes what a good recommendation looks like even when the raw watch-history signal is similar: a member in discovery mode and a member in continuation mode should see different rankings even from the same starting point. FM-Intent's premise is that making this latent intent explicit, and structurally central to the recommendation pipeline, produces better recommendations than leaving it as an implicit pattern the model has to infer indirectly.

## 2. Technical details

FM-Intent defines user intent along four key metadata dimensions: **action type** (discovery vs. continuation), **genre preference**, **movie/show (content type) preference**, and **time-since-release** (new content vs. older catalog titles). The architecture is explicitly hierarchical rather than multi-task-in-parallel:

- **Feature engineering:** categorical embeddings and numerical features derived from interaction metadata are combined into rich behavioral representations of what a user has been doing in the current and recent sessions.
- **Intent prediction module:** Transformer encoders with multi-head attention process the interaction sequence and generate predictions across the four intent dimensions, using both short-term (this session) and long-term (historical) implicit signals as proxies for latent intent — there's no direct label for "user intent," so the model learns to predict it from downstream behavioral signals.
- **Attention-based aggregation:** the four individual intent predictions are synthesized into a single intent embedding via attention, capturing which of the intent signals matters most for the current context.
- **Hierarchical next-item prediction:** rather than predicting intent and next-item as two parallel heads off a shared trunk (a more typical multi-task setup), FM-Intent's intent embedding is combined with the input features and explicitly informs the final next-item prediction — the hierarchy is the point, not an implementation detail.

Netflix also applied K-means clustering to the learned intent representations post hoc, surfacing interpretable user segments such as discovery-focused viewers, genre enthusiasts, and viewers with distinct time-since-release patterns.

## 3. Impact — potential & realized

**Realized:** a statistically significant 7.4% improvement in next-item prediction accuracy versus TransAct, Netflix's previous state-of-the-art baseline, in offline experiments. Netflix reports the model has been integrated into production.

**Potential:** beyond the direct recommendation-accuracy gain, Netflix lists several downstream applications the intent signal unlocks: personalized UI optimization (surfacing different layouts or shelves depending on inferred intent), analytics (understanding aggregate shifts in what members are trying to do), enhanced recommendation signals more broadly, and search-result prioritization — treating predicted intent as a general-purpose signal usable well beyond the single next-item-prediction task it was trained for.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clean, well-executed hierarchical take on an established idea

Multi-task learning that predicts an auxiliary signal (intent, mood, context) alongside the primary recommendation objective is well established in industrial recsys — Netflix itself and others have published variants of this before (see IntentRec below, which appears to be an earlier/academic version of closely related work). What FM-Intent adds is the explicit hierarchy — intent predictions feed forward into item prediction rather than sitting as a parallel head — and the four-dimensional intent taxonomy tuned specifically to Netflix's catalog structure (genre, content type, recency, discovery-vs-continuation). That's solid, well-executed production engineering with a real accuracy gain and genuine downstream reuse (UI, analytics, search), which is why it sits at 3 rather than lower, but it's an incremental architectural refinement of a known pattern rather than a new paradigm.

### Similar / related work

- **IntentRec: Predicting User Session Intent with Hierarchical Multi-Task Learning** (arXiv, 2024) — the closely related, earlier academic paper covering very similar ground (same title structure, same core idea of hierarchical multi-task intent prediction); FM-Intent's blog post appears to be Netflix's later, production-framed writeup of this line of work. Left unlinked here since the exact relationship between the two publications (revision vs. distinct follow-on) isn't stated in the source.
- [**Towards Generalizable and Efficient Large-Scale Generative Recommenders**](https://arxiv.org/abs/2605.23312) — Netflix's separate, more recent bet on generative-style recommendation, worth reading alongside FM-Intent as two different eras of Netflix's recommendation-model architecture.
- [**JourneyFormer: Encoding Airbnb Guest Journey with Sequence Modeling**](2026-09-06-airbnb-journeyformer-guest-sequence-search-ranking.md) (in this bank) — Airbnb's comparable move toward reading raw user sequences directly rather than hand-engineered aggregate features; a useful cross-company comparison of how different platforms model session-level user state.

### Jargon buster

- **Foundation model (in Netflix's recsys context)** — Netflix's term for a shared, general-purpose recommendation model trained on broad interaction data that specialized models (like FM-Intent) build on top of, rather than every recommendation task training its own model from scratch.
- **Hierarchical multi-task learning** — a multi-task setup where one task's output explicitly feeds into and informs another task's prediction, as opposed to "flat" multi-task learning where multiple tasks share a trunk but don't feed into each other.
- **TransAct** — Netflix's previous state-of-the-art recommendation baseline that FM-Intent is compared against; used here as the accuracy benchmark for the reported 7.4% improvement.
- **K-means clustering (as used here)** — an unsupervised algorithm used post hoc on the model's learned intent embeddings to group users into interpretable segments, not part of the model's training objective itself.
