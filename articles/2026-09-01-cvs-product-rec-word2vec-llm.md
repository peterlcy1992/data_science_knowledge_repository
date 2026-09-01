---
id: cvs-product-rec-word2vec-llm
title: "Enhancing \"You May Also Like\" (YMAL) Systems using LLMs and Word2Vec"
source: "CVS Health Tech Blog"
url: "https://medium.com/cvs-health-tech-blog/enhancing-you-may-also-like-ymal-systems-using-llms-and-word2vec-0340280019d2"
published: "2025-04"
added: "2026-09-01"
category: personalization-recsys
tags: [embeddings, word2vec, llm-features, recommendation, ecommerce]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Enhancing "You May Also Like" (YMAL) Systems using LLMs and Word2Vec

**Source:** [CVS Health Tech Blog](https://medium.com/cvs-health-tech-blog/enhancing-you-may-also-like-ymal-systems-using-llms-and-word2vec-0340280019d2) · Published 2025-04 · Added 2026-09-01
**Category:** Personalization & Recommender Systems · **Tags:** `embeddings`, `word2vec`, `llm-features`

## TL;DR

CVS Health improved its "You May Also Like" (YMAL) product-recommendation
system by embedding products with **Word2Vec** and **Euclidean distance**
over titles, brands, and categories, then enriching thin product metadata
with **GPT-4-generated 200-word summaries** used as extra embedding
features — targeting the system's two main failure modes: missing
recommendations and poor-quality ones.

## 1. Business context

CVS's e-commerce "You May Also Like" widget suggests similar products
across a large, heterogeneous retail catalog. Two problems limited it:
**bad coverage** (many products got no recommendations at all) and **bad
relevance** (recommended products didn't actually match well). A root cause
of both is that many product titles are short and low-information, giving a
title-based embedding model too little signal to place a product
meaningfully close to genuinely similar ones.

## 2. Technical details

- **Baseline embedding.** Products are embedded from titles, brands,
  categories, and sub-categories using **Word2Vec**, with similarity scored
  by **Euclidean distance** between embeddings.
- **LLM-generated summaries as features.** To counter thin/short product
  titles, CVS used **OpenAI GPT-3.5 Turbo and GPT-4** to generate concise
  ~200-word product description summaries from existing metadata, adding
  richer, more consistent context than the raw catalog text provides.
- **Feature fusion.** These LLM-generated summaries are folded in as
  additional features feeding the same Word2Vec-based embedding /
  similarity pipeline, rather than replacing it with an LLM-native
  retrieval system.

## 3. Impact — potential & realized

- **Realized:** the source describes qualitative improvements to
  recommendation coverage and relevance from adding LLM-generated summary
  features; no specific offline or online metrics (e.g. coverage %, CTR,
  precision) are reported in the material available.
- **Potential:** a low-lift pattern for any catalog with sparse or
  low-information item text — use an LLM once, offline, to enrich item
  metadata before it ever reaches a classical embedding pipeline, rather
  than re-architecting the whole recommender around an LLM.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — a practical but well-trodden pattern

Using an LLM purely as an offline feature-enrichment step ahead of a
classical Word2Vec/distance-based recommender is a sensible, low-risk way
to graft LLM context onto legacy infrastructure, and it's a pattern many
teams with thin catalog metadata have converged on independently. It's a
solid engineering choice for a constrained, legacy-system context, but it
isn't introducing a new technique, and the lack of any reported
quantitative lift makes it hard to judge how much the LLM step actually
helped.

### Similar / related work

- **Instacart's ads retrieval rebuild** ([in this
  bank](2026-09-01-instacart-ads-retrieval-rebuild.md)) — also modernizes a
  legacy retrieval system's inputs, though there via a generative retrieval
  model succeeding a BERT-like system rather than an LLM-as-feature-
  generator pattern.
- General "LLM-as-feature-enrichment" pattern (using an LLM offline to
  densify sparse item/text metadata before a classical embedding model)
  — a widely-used production pattern rather than a single citable source.

### Jargon buster

- **Word2Vec** — a technique that learns dense vector embeddings for
  discrete items (here, products) such that items appearing in similar
  contexts end up with similar vectors.
- **Euclidean distance** — the straight-line distance between two points
  (here, two product embedding vectors); smaller distance means the
  recommender treats the products as more similar.
- **Coverage (in recommender systems)** — the fraction of catalog items for
  which the system is able to produce any recommendation at all.
