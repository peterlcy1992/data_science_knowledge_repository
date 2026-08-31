---
id: netflix-maps-multimodal-asset-personalization
title: "MAPS: Multimedia Asset Personalization via Multimodal Embeddings at Netflix"
source: "Netflix Tech Blog / arXiv"
url: "https://arxiv.org/abs/2608.18322"
published: "2026-08"
added: "2026-08-30"
category: cv-multimodal
tags: [multimodal, embeddings, clip, two-tower, cold-start, artwork, embedding-store, foundation-model]
novelty: 4
sourced_via: "web search"
---

# MAPS: Multimedia Asset Personalization via Multimodal Embeddings at Netflix

**Source:** [Netflix Tech Blog / arXiv 2608.18322](https://arxiv.org/abs/2608.18322) · Published 2026-08 · Added 2026-08-30
**Category:** Computer Vision & Multimodal · **Tags:** `multimodal`, `embeddings`, `clip`, `two-tower`, `cold-start`

## TL;DR

Netflix rebuilt artwork personalization around shared multimodal embeddings
instead of per-surface bespoke models. Adding CLIP image embeddings to a
two-tower recommender lets a single model personalize all five artwork "canvas"
types at once — replacing five separately trained models and markedly improving
cold-start — and a decoupled Embedding Store lets new foundation models drop in
without touching downstream training or serving.

## 1. Business context

The image ("artwork") shown for a title is one of Netflix's highest-leverage
personalization surfaces: the same show can be sold to different members with
different framing. Historically each artwork placement — the different canvas
shapes and sizes across the UI — was served by its own separately trained
model. That is expensive to maintain, duplicates effort, and struggles with
**cold-start**: brand-new titles and freshly created artwork have little
interaction history, exactly when good personalization matters most for
launches. Netflix wanted one approach that generalizes across surfaces, handles
new assets gracefully, and lets the org reuse its growing stable of foundation
models without re-plumbing every downstream system.

## 2. Technical details

- **Two-tower + CLIP.** The core recommender is a two-tower model (a member/context
  tower and an item/asset tower) augmented with **CLIP image embeddings** for
  the artwork. Because CLIP places images and text in a shared space, the same
  representation serves multiple purposes.
- **One model, five canvases.** The CLIP-augmented model serves all five artwork
  canvas types with a single trained model, replacing five per-canvas models and
  substantially improving cold-start performance for new artwork/titles.
- **Query-aware artwork in search.** A lightweight extension reuses CLIP's joint
  text–image space so artwork personalization can be made **query-aware** in
  search — the image shown can reflect the user's text query, not just their
  taste profile.
- **MediaFM foundation model.** Beyond CLIP, Netflix uses **MediaFM**, an in-house
  multimodal foundation model that fuses **visual, audio, and timed-text**
  signals, trained on a large corpus of shots from the Netflix catalog.
- **Embedding Store decoupling.** The key architectural move: foundation-model
  outputs are registered as embeddings in a central **Embedding Store**. Any
  downstream personalization system consumes embeddings from the store, so a new
  or upgraded foundation model can be integrated **without modifying downstream
  training or serving infrastructure**.

## 3. Impact — potential & realized

- **Realized:** collapsing five per-canvas models into one; substantial cold-start
  improvements for new artwork and titles; query-aware artwork in search.
- **Realized (operational):** far less model sprawl to maintain and retrain.
- **Potential:** the Embedding Store pattern turns "adopt a new foundation model"
  from a cross-team re-integration project into a registration step, which is the
  reusable lesson Netflix explicitly frames for other practitioners moving to
  foundation-model embeddings.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — the paradigm is known; the productionization is the contribution

Two-tower recommenders and CLIP embeddings are both well established, so the
individual ingredients aren't new. What earns the 4 is the *systems* framing:
using one shared multimodal representation to retire a whole family of bespoke
models, and — more importantly — the **Embedding Store as a decoupling layer** so
foundation models become swappable dependencies. That is the part other large
recommender orgs will copy, because model sprawl and re-integration cost are
universal pains. It stops short of 5 because it's an integration/architecture
advance rather than a new modeling result.

### Similar / related work

- [**GenRec: An LLM-backed recommendation ranker at Netflix**](2026-08-30-netflix-genrec-llm-native-recommendation.md) (in this bank) —
  the LLM-native counterpart to this embedding-native approach.
- [**Deploying Semantic ID-based Generative Retrieval at Spotify**](2026-08-30-spotify-semantic-id-generative-retrieval-podcasts.md) (in this bank) —
  another "shared representation across surfaces" strategy, via semantic IDs.
- **Scaling Media Machine Learning at Netflix** (Netflix Tech Blog) — the
  media-understanding pipeline that produces the shot-level signals MediaFM
  trains on.

### Jargon buster

- **Two-tower model** — a retrieval/ranking architecture with two neural
  networks: one encodes the user/context, one encodes the item, and relevance is
  the dot product of the two vectors. Fast because item vectors can be
  precomputed.
- **CLIP** — a model trained to put images and their text descriptions into the
  same vector space, so you can compare "does this image match this text"
  directly. Great for cold-start because it understands an image without needing
  click history.
- **Cold-start** — the problem of recommending something (or with something) that
  has little or no interaction data yet, e.g. a brand-new title or freshly made
  artwork.
- **Embedding** — a fixed-length vector of numbers that represents an item's
  meaning; similar items have nearby vectors.
- **Embedding Store** — a central service that holds precomputed embeddings so
  many downstream systems can read the same representation instead of each
  recomputing it.
- **Foundation model** — a large model pretrained on broad data (here, catalog
  media) whose representations are reused across many tasks.
