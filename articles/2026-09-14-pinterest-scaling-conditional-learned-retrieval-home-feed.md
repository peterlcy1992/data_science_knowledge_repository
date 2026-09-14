---
id: pinterest-scaling-conditional-learned-retrieval-home-feed
title: "Scaling Conditional Learned Retrieval for Pinterest Home Feed"
source: "Pinterest Engineering Blog"
url: "https://medium.com/pinterest-engineering/scaling-conditional-learned-retrieval-for-pinterest-home-feed-ecfba7e5a426"
published: "2026-08"
added: "2026-09-14"
category: personalization-recsys
tags: [two-tower, candidate-generation, conditional-retrieval, embeddings, home-feed, pinterest]
novelty: 3
sourced_via: "web search"
---

# Scaling Conditional Learned Retrieval for Pinterest Home Feed

**Source:** [Pinterest Engineering Blog](https://medium.com/pinterest-engineering/scaling-conditional-learned-retrieval-for-pinterest-home-feed-ecfba7e5a426) · Published 2026-08 · Added 2026-09-14
**Category:** Personalization & Recommender Systems · **Tags:** `two-tower`, `candidate-generation`, `conditional-retrieval`, `embeddings`, `home-feed`

## TL;DR

Pinterest users chase several intents at once — renovation ideas, recipes, travel, fashion — but a standard two-tower retrieval model collapses all of that into a single user embedding. Conditional Learned Retrieval (CLR) conditions the user tower on an explicit "retrieval context" so it can produce several intent-aware embeddings per user instead of one, and Pinterest describes the work needed to scale that idea to full home-feed traffic.

## 1. Business context

Pinterest's home feed candidate generation is a large-scale User-to-Pin retrieval problem: a two-tower model encodes the user on one side and candidate Pins on the other, and approximate nearest-neighbor search finds Pins whose embeddings sit close to the user's. The limitation of that classic setup is that it produces one user vector, which has to average over everything the user might currently want. When a user is simultaneously planning a home renovation and saving recipes, a single embedding tends to blur toward the statistical center of their interests rather than representing either intent sharply — a diversity and relevance problem that shows up as a feed that feels generic rather than sharply personalized to any one of the user's active projects.

## 2. Technical details

CLR extends the two-tower architecture by conditioning the user tower on an explicit retrieval context signal, rather than requiring the tower to produce a single fixed embedding for a user regardless of context. In practice, this lets the same user tower emit multiple condition-aware embeddings — one that leans into "home renovation," another into "recipes" — while every embedding stays grounded in the user's overall behavioral history so the retrieval doesn't drift into implausible territory.

The blog post (a follow-up to Pinterest's earlier work establishing large-scale learned retrieval and embedding-based retrieval systems at Pinterest Homefeed) focuses specifically on what it took to *scale* CLR from an idea to production home-feed traffic: making condition-aware retrieval both more *expressive* (able to represent a richer set of conditions per user, on the modeling side) and more *efficient* (able to practically evaluate many conditions per request within Pinterest's latency and cost budget, on the infrastructure side). The source does not disclose the specific serving architecture changes (e.g., how many conditions are evaluated per request, or ANN index changes) in public detail.

## 3. Impact — potential & realized

**Realized:** Pinterest reports that offline and online A/B experiments show "significant improvements in user engagement and content diversity," framing increased retrieval diversity as a reliable lever for downstream engagement because it gives the ranking and blending stages a richer pool of candidates to work with. The post does not publish specific percentage lifts.

**Potential:** The framing generalizes well beyond Pinterest — any product where users hold multiple concurrent, weakly-related intents (a grocery app balancing meal-planning and pantry restocking, a video platform balancing "background" vs. "focused" viewing) faces the same single-embedding averaging problem that CLR is designed to solve, and the "condition-aware towers, evaluated at scale" pattern is directly reusable.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sensible, well-motivated production extension of two-tower retrieval

Conditioning a retrieval embedding on context isn't new in the literature, but making it work at Pinterest's home-feed scale — where every additional condition per user multiplies serving cost — is a genuine production engineering problem, and this is Pinterest's second public iteration on it (following their earlier CLR bootstrap work), which suggests it earned its way from pilot to scaled system. The lack of published metrics keeps this from scoring higher.

### Similar / related work

- **Bootstrapping Conditional Retrieval for User-to-Item Recommendations** — [arXiv:2508.16793](https://arxiv.org/abs/2508.16793) — appears to be Pinterest's earlier, foundational CLR paper that this post scales up.
- [**Ad Relevance: Integrating Real-Time Context into Sequential Recommender Models**](2026-09-05-pinterest-ad-relevance-realtime-context-sequential.md) (in this bank) — another Pinterest system using context signals to sharpen relevance, in the ads-ranking rather than retrieval stage.
- [**JourneyFormer: Encoding Airbnb Guest Journey with Sequence Modeling**](2026-09-06-airbnb-journeyformer-guest-sequence-search-ranking.md) (in this bank) — a different approach (sequence modeling instead of conditioning) to the same underlying goal of capturing a user's multiple, evolving intents.

### Jargon buster

- **Two-tower model** — A retrieval architecture with two separate neural networks (a "user tower" and an "item tower") that each output an embedding; matches are found by nearest-neighbor search between the two embedding spaces.
- **Conditional retrieval** — Retrieval where the query embedding depends on an extra context signal (a "condition"), so the same user can produce different embeddings depending on which aspect of their intent is being served.
- **Candidate generation** — The first, high-recall stage of a recommender funnel that narrows a huge catalog down to a smaller candidate set for more expensive downstream ranking.
