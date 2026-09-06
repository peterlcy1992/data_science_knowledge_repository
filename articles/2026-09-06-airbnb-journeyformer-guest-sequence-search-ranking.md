---
id: airbnb-journeyformer-guest-sequence-search-ranking
title: "JourneyFormer: Encoding Airbnb Guest Journey with Sequence Modeling"
source: "Airbnb Tech Blog / arXiv (KDD 2026)"
url: "https://arxiv.org/abs/2606.19108"
published: "2026-06"
added: "2026-09-06"
category: personalization-recsys
tags: [sequence-modeling, transformer, search-ranking, s2cell, embeddings, ablation, kdd]
novelty: 4
sourced_via: "full-text fetch"
---

# JourneyFormer: Encoding Airbnb Guest Journey with Sequence Modeling

**Source:** [Airbnb Tech Blog / arXiv (KDD 2026)](https://arxiv.org/abs/2606.19108) · Published 2026-06 · Added 2026-09-06
**Category:** Personalization & Recommender Systems · **Tags:** `sequence-modeling`, `transformer`, `search-ranking`, `s2cell`, `embeddings`, `ablation`, `kdd`

## TL;DR

Airbnb replaced hand-crafted aggregate features of guest history with JourneyFormer, a 4-layer transformer that directly encodes up to 7 years of booking/review events and 21 days of browsing as two sequences. It shipped +1.48% offline NDCG and, in a 3-week online A/B test, +0.55–0.90% on bookers/booked-nights/views for search ranking and a +5.04% lift in email views for email ranking.

## 1. Business context

Airbnb's search ranker had long captured "what a guest likes" through hundreds of hand-engineered aggregate statistics (e.g., average price booked, preferred room type) computed over a guest's history. As the feature count grew, this approach became harder to scale and increasingly limited in expressiveness — aggregates throw away order, recency, and co-occurrence information that a raw event sequence preserves. Guest journeys are also unusually hard to model directly: sequences span years, mix rare, high-value booking events with an abundance of low-signal browsing events, and the label of interest (an eventual booking) is extremely sparse relative to views. Airbnb needed a sequence model that could exploit that raw history for ranking without an explosion of training or serving cost.

## 2. Technical details

JourneyFormer splits a guest's history into two complementary sequences rather than one long stream:

- **Long-term sequence** — non-view events (bookings, reviews, cancellations) from the past 7 years, capped at 80 events.
- **Short-term sequence** — view events from the past 21 days, capped at 200 events.

Feature encoding: ID features (listing, host, S2Cell location IDs) share unified embedding tables with hashing to control table size; categorical features use standard embedding tables; continuous features go through batch normalization with an optional log transform. Location is represented hierarchically across all 14 S2Cell levels (0–13) to capture both coarse (city/region) and fine (block-level) geography simultaneously — an ablation showed using only the finest level underperforms the multi-level representation.

The sequence encoder itself is a 4-layer transformer with 128-dimensional embeddings, multi-head self-attention with causal masking (so no event can attend to future events), and positional encoding with residual connections. Notably, the team found that removing the feed-forward sublayers actually *improved* performance — a counterintuitive deviation from the standard transformer block that they attribute to the sparse-label, long-sequence regime. Output embeddings are downscaled to 32 dimensions before being written to storage, controlling the cost of serving the resulting user representation across production ranking surfaces.

Labels use a 7-day attribution window (a search's positive label is a listing booked within 7 days of that search), and training caps the data to 4 searches per guest per day to bound sequence-label volume.

Training at this scale (years of events, hundreds of millions of guests) required specific throughput work: batching searches together, bucketizing sequences by length, and sparse computation over padded regions. Removing any one of these separately cost 20–75% of training throughput; combined, they gave roughly a 4x speedup over a naive implementation.

## 3. Impact — potential & realized

**Realized (offline):** NDCG improved +0.44% (long-term sequence only), +1.30% (short-term only), and +1.48% (both combined) over the production baseline.

**Realized (online, 3-week A/B):**
- Search ranking, full model: +0.55% bookers (p<0.01), +0.82% booked nights (p<0.01), +0.90% views (p<0.01).
- Search ranking, long-term-only variant: +0.31% bookers (p<0.05), +0.28% booked nights (not significant), +0.38% views (p<0.01).
- Email ranking, full model: +0.16% bookers (p<0.05), +0.23% booked nights (p<0.05), +5.04% email views (p<0.01).

**Potential:** The ablations point to a reusable recipe for anyone serving long, sparse-label user histories — hierarchical geo IDs, removing feed-forward layers, and short/long sequence separation. Airbnb also reports the model's gains were stable for at least 30 days post-training with under 0.1% decline, suggesting the representation is robust to distribution shift over a meaningful window, which matters for retraining cadence decisions.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A strong production-first take on sequence modeling for ranking

The building blocks (transformers over user event sequences, hierarchical geo embeddings) are established in the recsys literature, but the specific engineering choices here are genuinely interesting: dropping feed-forward layers is not something you'd guess a priori, and the explicit long/short sequence split with different retention windows and caps is a sensible answer to the "guest journeys are long and sparse" problem that a lot of "just throw a transformer at it" papers gloss over. The throughput ablations (batching, bucketization, sparse computation) are the kind of detail that makes this a credible production system rather than a research demo.

### Similar / related work

- [**Learning to Rank for Maps at Airbnb**](2026-08-30-airbnb-learning-to-rank-for-maps.md) (in this bank) — same team's prior work on ranking; JourneyFormer extends the user-representation side of that pipeline.
- [**An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking (Feed SR)**](2026-09-01-linkedin-feed-sr-sequential-recommender.md) (in this bank) — a comparable decoder-only transformer over user history for feed ranking, with the same RoPE-style attention-over-history idea applied to a different surface.
- [**Towards Generalizable and Efficient Large-Scale Generative Recommenders**](2026-09-01-netflix-generalizable-generative-recommenders.md) (in this bank) — another large-scale sequence model discussion, useful for contrasting generative retrieval vs. this ranking-focused sequence encoder.

### Jargon buster

- **S2Cell** — Google's hierarchical geospatial indexing scheme that divides the Earth's surface into a quadtree of cells at multiple zoom levels, letting a single location be represented at coarse and fine granularity simultaneously.
- **NDCG (Normalized Discounted Cumulative Gain)** — a ranking-quality metric that rewards placing relevant results near the top of a list, discounted by position.
- **Causal masking** — an attention mechanism constraint that prevents a sequence position from "seeing" any position that comes after it, preserving the correct temporal order of information flow.
