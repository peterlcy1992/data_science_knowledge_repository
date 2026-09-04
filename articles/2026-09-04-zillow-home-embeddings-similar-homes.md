---
id: zillow-home-embeddings-similar-homes
title: "Home Embeddings for Similar Home Recommendations"
source: "Zillow Tech Hub"
url: "https://www.zillow.com/tech/embedding-similar-home-recommendation/"
published: "2025-12"
added: "2026-09-04"
category: personalization-recsys
tags: [embeddings, siamese-network, cold-start, real-estate, similarity-search]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Home Embeddings for Similar Home Recommendations

**Source:** [Zillow Tech Hub](https://www.zillow.com/tech/embedding-similar-home-recommendation/) · Published 2025-12 · Added 2026-09-04
**Category:** Personalization & Recommender Systems · **Tags:** `embeddings`, `siamese-network`, `cold-start`, `real-estate`, `similarity-search`

## TL;DR

Zillow built a Siamese-network embedding model that maps home listings into a shared vector space where cosine similarity captures "similar home" relationships, trained with triplet loss on user co-click data and blending collaborative signal with content features (location, price, size, property type) — a design that, unlike pure collaborative filtering, naturally handles cold-start listings by generating an embedding from content alone.

## 1. Business context

Recommending "similar homes" is a core discovery surface for Zillow: when a shopper views a listing, the platform needs to suggest comparable homes they might also like. A pure collaborative-filtering approach (based on which listings get co-clicked together) struggles with cold start — brand-new listings have no click history yet, but real-estate inventory turns over constantly, so a similarity system that can't handle new listings on day one is a poor fit for the domain. Zillow needed a similarity model that captures genuine behavioral co-click patterns where available, while still producing sensible recommendations for newly listed homes.

## 2. Technical details

- **Architecture:** a Siamese network — two identical sub-networks (shared weights, several fully connected layers) that each map a home's content-feature vector into a low-dimensional embedding space (e.g., N=25 dimensions), where cosine similarity between two homes' embeddings can be computed directly.
- **Training signal:** user co-click data (positive pairs — homes co-clicked in the same session — and sampled negative pairs) trains the network via a **triplet loss**, which pulls embeddings of co-clicked home pairs closer together while pushing embeddings of dissimilar (negative) pairs apart.
- **Input features:** each home's content vector includes location (zip code, city, coordinates), price, size (square footage, room counts), property type, and neighborhood features; categorical features are embedded via a skip-gram approach, and numerical features are preprocessed with log transforms and min-max scaling before being fed into the sub-network.
- **Cold-start handling:** because the embedding is generated purely from a listing's content features rather than requiring click history, a brand-new listing gets a meaningful embedding — and therefore meaningful similarity recommendations — from the moment it's listed.
- **Baseline comparison:** the Siamese embedding with triplet loss outperformed simpler alternatives the team compared against, including raw cosine similarity on content features, linear models, and random forests.

## 3. Impact — potential & realized

- **Realized:** the Siamese-embedding approach outperformed content-only cosine similarity, linear models, and random-forest baselines on the similarity-recommendation task, and the resulting embeddings power Zillow's similar-home recommendation engine in production.
- **Potential:** the same embedding-space design pattern — blend collaborative signal into training while keeping inference content-based enough to handle cold start — generalizes to any marketplace with high inventory turnover (used-goods marketplaces, rental listings, job postings) where pure collaborative filtering would leave new items with no meaningful recommendations.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a well-executed, standard pattern for a domain where cold start really matters

Siamese networks with triplet loss for learned similarity are a well-established technique across many recommendation and search domains; Zillow's contribution here is applying it thoughtfully to real estate specifically, where the cold-start problem is unusually acute (nearly every listing is "new" at some point, and inventory constantly turns over) and where blending structured content features (price, location, size) with behavioral co-click signal is a sensible, if not novel, design choice. It's a solid 3: good production engineering and domain fit, but the modeling technique itself isn't new.

### Similar / related work

- [**MAPS: Multimedia Asset Personalization via Multimodal Embeddings at Netflix**](2026-08-30-netflix-maps-multimodal-asset-personalization.md) (in this bank) — another company using learned embeddings to solve a cold-start-adjacent personalization problem, though for media assets rather than real-estate listings.
- **Improving Recommendation Quality by Tapping into Listing Text** ([Zillow Tech Hub](https://medium.com/zillow-tech-hub/improving-recommendation-quality-by-tapping-into-listing-text-8407959b1711)) — Zillow's follow-up work extending this same recommendation system with listing-text embeddings.
- Airbnb's "Listing Embeddings in Search Ranking" (well-known industry work, no single specific URL tracked here) — the widely-cited Airbnb approach to learning listing embeddings from click sessions, a close conceptual sibling from a different marketplace domain.

### Jargon buster

- **Siamese network** — a neural network architecture where two (or more) identical sub-networks with shared weights each process one input, producing embeddings that can be directly compared (e.g., via cosine similarity) — commonly used for similarity and matching tasks.
- **Triplet loss** — a training objective that takes an anchor example, a positive example (similar to the anchor), and a negative example (dissimilar), and pushes the embedding space to place the anchor closer to the positive than to the negative by some margin.
- **Cold start** — the problem of making good recommendations for a new item (or user) that has no interaction history yet; content-based embeddings mitigate this because they don't require historical clicks to produce a useful representation.
- **Skip-gram embedding** — a technique (originally from word2vec) for learning dense vector representations of categorical values from their co-occurrence patterns, applied here to categorical listing features like property type.
