---
id: doordash-llms-content-embeddings-search-recommendations
title: "Using LLMs to Build Content Embeddings for Search and Recommendations"
source: "DoorDash Engineering"
url: "https://careersatdoordash.com/blog/doordash-llms-to-build-content-embeddings-for-search-and-recommendations/"
published: "2026-05"
added: "2026-09-08"
category: personalization-recsys
tags: [llm-generated-profiles, embeddings, semantic-search, cold-start, metaflow, llm-as-judge, matryoshka-representation-learning]
novelty: 4
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Using LLMs to Build Content Embeddings for Search and Recommendations

**Source:** [DoorDash Engineering](https://careersatdoordash.com/blog/doordash-llms-to-build-content-embeddings-for-search-and-recommendations/) · Published 2026-05 · Added 2026-09-08
**Category:** Personalization & Recommender Systems · **Tags:** `llm-generated-profiles`, `embeddings`, `semantic-search`, `cold-start`, `metaflow`, `llm-as-judge`, `matryoshka-representation-learning`

## TL;DR

DoorDash replaced behavioral, co-visitation-based content embeddings with ones built from LLM-generated merchant and item profiles, finding that upgrading the *input representation* (raw metadata → LLM-written profile) mattered far more than upgrading the embedding model itself — a 31.22% Hit@5 improvement versus only 5.92% from a stronger embedding model alone — and shipped the resulting embeddings across search, homepage carousels, and co-purchase recommendations for measurable gains in null search rate, conversion, and offline precision.

## 1. Business context

DoorDash's search and recommendation quality across food, grocery, retail, and gifting verticals was stuck in a circular dependency: personalization quality depended on embedding quality, and embedding quality depended on data quality. The traditional fix — behavioral embeddings built from co-visitation patterns (which items get browsed or bought together) — broke down because DoorDash sessions are intentful and brief rather than exploratory: users don't browse widely before ordering, so there's too little engagement signal per session for co-visitation to capture real semantic similarity. Pure content-metadata approaches had the opposite problem — the raw metadata itself (titles, categories) was often too sparse or inconsistent to embed well.

## 2. Technical details

The core idea is to use LLMs to generate a rich, standardized *profile* for every merchant and item — describing cuisine, preparation method, ingredients, dietary attributes, and price point — and then embed the profile instead of the raw metadata:

- **Profile generation.** For visual content, a vision-language model first generates a text description from the item's image; that description is combined with structured metadata into one comprehensive profile per entity.
- **Orchestration.** DoorDash uses **Metaflow** to run a daily ETL pipeline that aggregates order history, ratings, and metadata, then triggers embedding inference in batch. Inference is *incremental* — an entity is only re-embedded when its underlying content actually changes, avoiding a full daily recompute of the catalog.
- **Embedding model selection.** The team's central finding: input quality dominates model choice. Moving from MiniLM on raw metadata to **gemini-embedding-001** on raw metadata (a stronger model, same weak input) improved Hit@5 by only 5.92%. Keeping MiniLM but switching to LLM-generated profiles as input improved Hit@5 by 31.22% — roughly 5x the gain from a better model alone. The team ultimately shipped gemini-embedding-001 at 256 dimensions using Matryoshka Representation Learning (MRL), with `SEMANTIC_SIMILARITY` task types for entity-to-entity comparison and asymmetric `RETRIEVAL_QUERY`/`RETRIEVAL_DOCUMENT` task types for search.
- **Evaluation.** Rather than large-scale human annotation, DoorDash built an **LLM-as-a-judge harness** that decomposes entity similarity and query relevance into facet-level comparisons (cuisine, preparation, ingredients, dietary constraints) before aggregating into an overall calibrated score.

The embeddings feed three production surfaces: item- and store-level semantic search (layered with a fine-tuned **Qwen 3 reranker** that scores candidates against query, item profiles, and store profile), co-purchase carousels (cosine-thresholded clustering over `SEMANTIC_SIMILARITY` embeddings), and generative personalized homepage carousels (an LLM writes a carousel theme from the consumer's profile and context, then nearest-neighbor retrieval finds matching stores and dishes).

## 3. Impact — potential & realized

**Realized, search:** null search rate down 3.65%; core search session conversion rate up 0.66%; dish-query nDCG up 7.8%, cuisine-query nDCG up 1.4%; 7-day active customer share up 0.0724%.

**Realized, homepage discovery:** homepage order rate up 2.4% (relative); 7-day reorder rate up 0.164%; variable profit per order up 0.32%; offline precision@10 improved from 68% to 85%.

**Realized, co-purchase carousels:** trial-merchant visit rate up 0.435%; homepage clicks per impression up 0.110%.

**Potential — cold start:** because a profile is generated from an entity's own content, a brand-new merchant or item gets a strong embedding from day one, without needing to accumulate order history first — directly countering the "rich get richer" dynamic of pure engagement-based embeddings.

**Acknowledged limitation:** the content-first approach works well for entities (merchants, items) whose meaning lives in declarative facts, but the team explicitly notes it breaks down for *consumer* representations — "a consumer's identity lives in behavior," and averaging multiple preferences and occasions into one vector loses meaningful distinctions that would require situational context conditioning to recover.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — The "input beats model" finding is the transferable lesson

The headline technique — use an LLM to enrich sparse metadata into a text profile before embedding — isn't itself new, but the quantified comparison (31.22% vs. 5.92% Hit@5 gain from better input vs. better model) is a genuinely useful, generalizable data point that most teams building recommendation embeddings should internalize: spend the effort on input quality before reaching for a bigger embedding model. Combining that with an honest, explicit acknowledgment of where the approach *doesn't* work (consumer-side representations) is the kind of transparency that makes this more valuable than a typical win-only case study.

### Similar / related work

- [**DoorDash — DashCLIP: Multimodal Semantic Embeddings**](2026-09-08-doordash-dashclip-multimodal-ad-embeddings.md) (in this bank) — the sibling DoorDash effort applying the same "content over engagement" philosophy to image+text ads embeddings via LLM-curated relevance data, rather than pure-text merchant/item profiles.
- [**Instacart — Our Early Journey to Transform Discovery Recommendations with LLMs**](2026-09-02-instacart-llm-discovery-shopping-hub.md) (in this bank) — another grocery/food-delivery company using LLM-generated content (page themes, keywords) to drive discovery, complementary to DoorDash's embedding-generation focus.
- [**CVS — Enhancing "You May Also Like" Systems Using LLMs and Word2Vec**](2026-09-01-cvs-product-rec-word2vec-llm.md) (in this bank) — a different retailer's take on combining LLM-derived signal with classical embedding techniques for product recommendations.

### Jargon buster

- **Hit@5** — an offline retrieval metric measuring how often the correct or relevant item appears in the top 5 results returned.
- **Matryoshka Representation Learning (MRL)** — a training technique that produces embeddings usable at multiple dimensionalities (e.g., truncate a 768-dim embedding to 256-dim) without retraining, trading off storage/compute cost against accuracy.
- **LLM-as-a-judge** — using a large language model to score or compare outputs (here, entity similarity and query relevance) as a substitute for large-scale human annotation.
- **Co-visitation** — a classic recommendation signal based on which items are frequently browsed, viewed, or purchased together by the same users in the same session.
