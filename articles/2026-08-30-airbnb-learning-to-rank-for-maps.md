---
id: airbnb-learning-to-rank-for-maps
title: "Learning to Rank for Maps at Airbnb"
source: "Airbnb Tech Blog / arXiv"
url: "https://medium.com/airbnb-engineering/improving-search-ranking-for-maps-13b03f2c2cca"
published: "2024-07"
added: "2026-08-30"
category: search-ranking
tags: [learning-to-rank, maps, user-attention, ndcg, two-tower, ux, experimentation]
novelty: 4
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Learning to Rank for Maps at Airbnb

**Source:** [Airbnb Tech Blog](https://medium.com/airbnb-engineering/improving-search-ranking-for-maps-13b03f2c2cca) · also [arXiv 2407.00091](https://arxiv.org/pdf/2407.00091) · Published 2024-07 · Added 2026-08-30
**Category:** Search & Ranking · **Tags:** `learning-to-rank`, `maps`, `user-attention`, `ndcg`
_Surfaced via the Snacks Weekly on Data Science podcast._

## TL;DR

Ranking for a map is not ranking for a list. Airbnb found that the list-ranking
assumption — attention decays down a ranked order — is simply false on a map,
where attention decays radially from the center. Re-deriving the objective for
map geometry, and introducing "mini-pins" to redirect attention, produced one of
the largest booking gains in Airbnb ranking history.

## 1. Business context

Maps account for roughly **80% of search interactions** on Airbnb, yet map
ranking had long reused the assumptions of **feed/list ranking**. On a list, the
standard recipe works: sort by booking probability, because user attention
decays with list position. On a map there is **no ranked list and no positional
decay**, so sorting pins by booking probability doesn't place the best listings
where users actually look. The mismatch showed up when the team examined
**NDCG** for maps. A map-specific ranking approach was needed to convert that 80%
of interaction into bookings.

## 2. Technical details

- **Attention model for maps.** User attention is **maximum at the center** of the
  map and **decays radially outward**. On desktop, a grid of listings to the left
  of the map exerts an additional **leftward pull** on attention. The ranking
  objective is re-derived around this spatial attention distribution instead of a
  linear position-decay curve.
- **Two-tier pin system.** Listings with the **highest booking probabilities** show
  as regular oval **price pins**; listings with lower probabilities show as smaller
  **mini-pins** without price. Mini-pins deliberately draw less attention —
  click-through is about **8× lower** than regular pins — so high-value listings
  keep the visually dominant, central real estate.
- **Restricting what competes for attention.** Rather than only reordering, the
  system controls *how much attention each listing can capture*, aligning the most
  attention-grabbing treatment with the highest-value inventory.

## 3. Impact — potential & realized

- **Realized:** launching the restricted (mini-pin) version drove **one of the
  largest bookings improvements in Airbnb ranking history**, with gains in
  **quality bookings** (more trips earning 5-star ratings).
- **Potential:** a general lesson for any non-list surface (maps, grids, carousels,
  spatial canvases) — model where attention actually goes before optimizing what
  to rank, and treat the *presentation* of a result as a ranking lever, not just
  its order.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — reframes the ranking objective instead of tuning the model

Most ranking write-ups tweak features or losses. This one questions the
foundational assumption — that attention decays by position — and shows it's
wrong for a whole class of UI. Modeling radial attention and then using pin
*styling* (mini-pins) as a control on attention is a genuinely fresh, deployable
idea with a rare "largest in company history" result. Not a 5 because the
underlying learning-to-rank machinery is standard; the insight is where it's
applied.

### Similar / related work

- [**MAPS: Multimodal Asset Personalization at Netflix**](2026-08-30-netflix-maps-multimodal-asset-personalization.md) (in this bank) — also about
  *presentation* (artwork) as a personalization lever, not just item order.
- [**GenRec at Netflix**](2026-08-30-netflix-genrec-llm-native-recommendation.md) (in this bank) — ranking-stage rethink, from the LLM angle.
- **Airbnb Relevance team publications** — the broader body of Airbnb ranking work
  this belongs to.

### Jargon buster

- **Learning to rank (LTR)** — training a model to order a set of items to maximize
  a ranking metric, rather than predicting each item's score in isolation.
- **NDCG (Normalized Discounted Cumulative Gain)** — a ranking-quality metric that
  rewards putting relevant items where users are most likely to look; the
  "discount" encodes the attention model.
- **Positional decay** — the assumption that users pay less attention to items
  further down a list; the thing that breaks on a map.
- **Click-through rate (CTR)** — the fraction of shown items that get clicked; used
  here to quantify how much attention mini-pins draw versus full pins.
