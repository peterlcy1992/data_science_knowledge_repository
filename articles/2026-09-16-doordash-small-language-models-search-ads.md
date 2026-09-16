---
id: doordash-small-language-models-search-ads
title: "Using Small Language Models to Serve More Relevant DoorDash Search Ads"
source: "DoorDash Engineering Blog"
url: "https://careersatdoordash.com/blog/small-language-models-to-serve-more-relevant-doordash-search-ads/"
published: "2026"
added: "2026-09-16"
category: search-ranking
tags: [small-language-models, knowledge-distillation, bi-encoder, ads-ranking, low-latency-serving]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Using Small Language Models to Serve More Relevant DoorDash Search Ads

**Source:** [DoorDash Engineering Blog](https://careersatdoordash.com/blog/small-language-models-to-serve-more-relevant-doordash-search-ads/) · Published 2026 · Added 2026-09-16
**Category:** Search & Ranking · **Tags:** `small-language-models`, `knowledge-distillation`, `bi-encoder`, `ads-ranking`, `low-latency-serving`

## TL;DR

DoorDash replaced a gradient-boosted decision tree model for sponsored-search query-item relevance with a distilled small language model: a fine-tuned LLM labels 700,000 query-item pairs offline, and a compact bi-encoder trained on those labels serves relevance predictions online under strict latency budgets — landing a 5.2% relative gain in Precision@2 with 97% validation accuracy.

## 1. Business context

Sponsored search results only work commercially if they're relevant — a mismatched ad erodes trust in search and, ultimately, ad revenue. DoorDash's prior relevance model was a gradient-boosted decision tree, a solid but representationally limited approach for judging semantic fit between a search query and a listed item. Stronger language understanding was available from large language models, but running a large LLM online for every search-ads request was a non-starter under DoorDash's latency budget — so the challenge was capturing LLM-level relevance judgment without paying LLM-level inference cost at serving time.

## 2. Technical details

DoorDash used a two-stage teacher/student setup. A large language model was fine-tuned on 700,000 human-labeled query-item pairs and used **offline** to generate relevance labels at scale — the "teacher," unconstrained by serving latency. A compact small language model — the "student" — was then trained on those LLM-generated labels to reproduce the same relevance judgments in a form cheap enough to run online.

For the production student model, DoorDash chose a **bi-encoder architecture**: the query and the item are each passed through independent BERT-based encoder towers, producing a dense vector per side, with relevance scored by comparing the two vectors — a design chosen specifically for its latency profile (the item-side embedding can largely be precomputed) over a cross-encoder, which would jointly process query and item together for a richer but much slower comparison. The team evaluated several BERT-based backbones — DistilBERT, DeBERTa, RoBERTa, ALBERT, TinyBERT, and E5 — along with different pooling strategies (CLS-token pooling vs. mean pooling), to map out the quality/latency tradeoff before settling on a DistilBERT-based bi-encoder with 64-dimensional output embeddings.

## 3. Impact — potential & realized

**Realized:** The production small language model reached 97% validation accuracy and delivered a 5.2% relative improvement in Precision@2 compared to the prior gradient-boosted decision tree baseline, while meeting DoorDash's low-latency serving requirements for search ads.

**Potential:** The teacher/student pattern — fine-tune a large model offline for label quality, distill into a small, latency-appropriate model for serving — is directly reusable anywhere DoorDash (or a similar marketplace) needs semantic judgment at request-time scale: broader search relevance, content moderation, or other ranking signals where a full LLM call per request isn't affordable.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clean, by-the-book application of an established distillation pattern

LLM-teacher-to-small-model-student distillation for latency-constrained ranking is a well-established pattern at this point (seen repeatedly across search and recsys write-ups this year). The value here isn't a new technique but the thoroughness of the backbone/pooling sweep before choosing the production architecture, and the concrete before/after metric (GBDT → bi-encoder SLM, +5.2% relative Precision@2) that makes the payoff legible. Solid, unglamorous production ML.

### Similar / related work

- [**Scaling Up Efficient Small Language Models Serving and Deployment for Semantic Job Search**](2026-09-15-linkedin-slm-serving-semantic-job-search.md) (in this bank) — another small-language-model production deployment from the same week, focused on serving throughput and compression rather than distillation from an LLM teacher, but the same broader SLM-in-production theme.
- [**The Science of Unified Ranking: Integrating Ads and Organic Recommendations**](2026-09-14-flipkart-unified-ranking-ads-organic.md) (in this bank) — a different angle on ads ranking (unifying ads and organic scoring) from the same week, complementary to DoorDash's focus on the relevance signal itself.
- **Knowledge distillation literature (Hinton et al., and bi-encoder vs. cross-encoder retrieval work)** — the general technique this post applies; no single paper URL was specified in the source.

### Jargon buster

- **Bi-encoder** — A model architecture with two independent encoder towers (here, for query and item) that each produce a vector, with similarity scored by comparing the vectors — fast because one side (typically the item) can be precomputed and cached ahead of query time.
- **Cross-encoder** — A model that processes two inputs (e.g. query and item) jointly in a single forward pass, usually more accurate than a bi-encoder but far more expensive, since nothing can be precomputed ahead of a specific query-item pair.
- **Knowledge distillation** — Training a smaller "student" model to reproduce the outputs of a larger "teacher" model, so the student captures much of the teacher's judgment quality at a fraction of the inference cost.
- **Precision@2** — Of the top 2 results shown, the fraction that are actually relevant — a ranking-quality metric focused specifically on what a user sees first.
