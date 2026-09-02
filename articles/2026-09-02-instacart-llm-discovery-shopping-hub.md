---
id: instacart-llm-discovery-shopping-hub
title: "Our Early Journey to Transform Instacart's Discovery Recommendations with LLMs"
source: "Instacart Tech"
url: "https://tech.instacart.com/our-early-journey-to-transform-instacarts-discovery-recommendations-with-llms-cf4591a8602b"
published: "2026-02"
added: "2026-09-02"
category: llm-genai
tags: [generative-ui, llm-agents, rag, llm-as-judge, personalization, discovery]
novelty: 4
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Our Early Journey to Transform Instacart's Discovery Recommendations with LLMs

**Source:** [Instacart Tech](https://tech.instacart.com/our-early-journey-to-transform-instacarts-discovery-recommendations-with-llms-cf4591a8602b) · Published 2026-02 · Added 2026-09-02
**Category:** LLMs & Generative AI · **Tags:** `generative-ui`, `llm-agents`, `rag`, `llm-as-judge`, `personalization`

## TL;DR

Instacart's Shopping Hub (the discovery page shown after picking a retailer) rebuilt itself around a four-phase generative pipeline — an LLM page-design agent generates personalized shopping themes top-down, RAG-constrained keyword generation maps them to real inventory, multiple LLM-judge/embedding filters enforce quality and diversity, and existing ranking services handle final product selection — replacing a static, manually curated content library.

## 1. Business context

Instacart's Shopping Hub is the primary discovery surface a shopper sees right after choosing a retailer, and it shapes the entire shopping session that follows. It historically relied on static content libraries built by human curation, which created two structural problems: personalization didn't really scale, because authoring customized placements for different user segments, seasons, or business objectives was slow and labor-intensive; and the page lacked cohesion, because different teams built placements independently, producing a fragmented experience rather than a page that reads as a single, intentional whole. Instacart wanted a system that could generate the page itself, personalized per user, while staying coherent and controllable.

## 2. Technical details

- **Two generation paradigms considered.** The team weighed a **bottoms-up** approach (generate candidate products first, then cluster them into placements) against a **top-down** approach (generate the page's placements/themes first, then populate each with products). They chose top-down as the better balance of personalization, page-level cohesion, and adaptability, given real-time latency limits and a catalog that turns over frequently.
- **Phase 1 — page design and theme generation.** A page-design LLM agent generates personalized, high-level shopping themes (e.g., "Breakfast" tailored differently per user) from the shopper's purchase history and engagement signals, producing structured output for the phases downstream.
- **Phase 2 — retrieval keyword generation.** Each theme is mapped to retrieval-compatible descriptors via a teacher-student fine-tuned model combined with retrieval-augmented generation; RAG constrains candidate keywords using catalog embeddings, which alone cut generation cost 15-20% per generation by narrowing what the model has to consider.
- **Phase 3 — quality and diversity filtering.** Guardrails prevent redundant or off-brand placements using embedding-based deduplication, LLM-as-a-judge scoring across dimensions like cohesion, diversity, brand alignment, and theme-product match, plus a fine-tuned cross-encoder for relevance classification.
- **Phase 4 — product and page-wise ranking.** The filtered, cached placements are handed to Instacart's existing ranking services for final product selection and page ordering, rather than having the generative pipeline pick final products itself.
- **Evaluation, treated as a first-class problem.** Three complementary layers: a rich **LLM-as-a-judge** suite auditing page/placement/product levels; a **fine-tuned DeBERTa model** for product-title relevance classification, giving a claimed **99% cost reduction** versus using a closed-weight LLM for the same classification at scale; and classical proxy signals (purchase-history overlap, predicted engagement, placement density).

## 3. Impact — potential & realized

- **Realized:** qualitative shift from rigid, single-category placements to multi-category, history-aware ones (e.g., a "Breakfast" placement that differs meaningfully by shopper); the team reports initial A/B experiment results as "quite promising," though it does not disclose specific lift numbers, and frames the rollout as early-stage rather than a completed system overhaul.
- **Potential:** a reusable pattern — LLM-generated page structure, RAG-grounded content generation, and existing ranking infrastructure kept as the final arbiter — for any discovery surface currently built on static, manually curated content, plus the reusable evaluation discipline (LLM-judge, cheap fine-tuned classifiers, classical proxies together) as a template for teams building generative-UI systems that need trustworthy, affordable evals at scale.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a genuinely new generative-UI architecture, honestly reported as still early

Generating page structure top-down with an LLM agent, then constraining content generation with RAG before handing off to existing ranking infrastructure, is a real architectural departure from both "static curated content" and "LLM picks final products directly." The three-pronged evaluation strategy — especially distilling a cheap classifier (DeBERTa, 99% cheaper than LLM inference) to do relevance filtering at scale — is a smart, exportable pattern for keeping generative-UI systems affordable. It's a 4 rather than 5 because the write-up is explicit that this is early: no hard lift numbers are disclosed, and the team frames it as one experiment on the way to a fuller rebuild rather than a finished, proven system.

### Similar / related work

- [**GenRec: Towards LLM-Native Recommendation at Netflix**](2026-08-30-netflix-genrec-llm-native-recommendation.md) (in this bank) — another production system putting an LLM in the recommendation loop, there as a ranker over a catalog-aware head rather than a page-structure generator.
- [**From Models to Products: LLMs for Recommendation at Spotify Scale**](2026-08-31-spotify-neo-glide-llm-recommendation-grounding.md) (in this bank) — a different grounding strategy (semantic IDs constraining generation to valid catalog items) versus this system's RAG-constrained keyword generation plus a downstream ranking-service handoff.
- [**Enhancing "You May Also Like" (YMAL) Systems using LLMs and Word2Vec**](2026-09-01-cvs-product-rec-word2vec-llm.md) (in this bank) — a much lighter-weight use of LLMs (offline metadata enrichment feeding a classical embedding model) versus this system's LLM-driven page generation and multi-stage LLM-judge evaluation.

### Jargon buster

- **Generative UI** — a user interface (here, a page's layout and content) that is generated per-user by a model at request time, rather than assembled from a fixed set of pre-built components.
- **Retrieval-augmented generation (RAG)** — constraining an LLM's output by first retrieving relevant, grounded information (here, real catalog items via embeddings) and conditioning generation on it.
- **LLM-as-a-judge** — using an LLM to score the quality of generated content along specified dimensions, as a scalable substitute for exhaustive human review.
- **Cross-encoder** — a model that scores a pair of inputs (here, a product title and a theme) jointly rather than embedding each separately, typically more accurate but more expensive than embedding-based similarity.
- **Teacher-student fine-tuning** — training a smaller "student" model to imitate a larger "teacher" model's outputs, used here to make keyword generation cheaper to run at scale.
