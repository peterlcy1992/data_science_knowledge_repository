---
id: aws-bedrock-query-aware-rag-compression
title: "Reduce RAG Costs on Amazon Bedrock with Query-Aware Compression"
source: "AWS Machine Learning Blog"
url: "https://aws.amazon.com/blogs/machine-learning/reduce-rag-costs-on-amazon-bedrock-with-query-aware-compression/"
published: "2026-08"
added: "2026-09-02"
category: llm-genai
tags: [rag, context-compression, cost-optimization, bedrock, hallucination-reduction, prompt-compression]
novelty: 3
sourced_via: "web search"
---

# Reduce RAG Costs on Amazon Bedrock with Query-Aware Compression

**Source:** [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/reduce-rag-costs-on-amazon-bedrock-with-query-aware-compression/) · Published 2026-08 · Added 2026-09-02
**Category:** LLMs & Generative AI · **Tags:** `rag`, `context-compression`, `cost-optimization`, `bedrock`, `hallucination-reduction`

## TL;DR

AWS engineers Aakanksha Veesam and Amit Maindola describe a two-stage RAG pattern where a cheap model (Claude Haiku) extracts only the query-relevant verbatim spans from retrieved chunks before a larger model (Claude Sonnet) answers — cutting cost 33-36%, tokens sent to the primary model 8.6-10.1x, and hallucination rate from 51% to as low as 38%, at the price of 12-19% added latency.

## 1. Business context

RAG retrieval is tuned for high recall: a typical query returns 5-20 chunks of several thousand tokens each to maximize the chance the answer is in there somewhere. But most retrieved tokens are irrelevant to any specific question, and every one of them is billed to the expensive foundation model that generates the final answer. As RAG systems scale, that irrelevant-context tax becomes a real cost line — and, separately, irrelevant context is itself a source of hallucination, since the model has more room to latch onto tangential material.

## 2. Technical details

- **Two-stage pipeline.** A retriever returns the usual top-k chunks; an orchestrator (a single AWS Lambda function) first sends the full retrieved context and the user's query to a small, cheap model (Claude Haiku) via the Bedrock Converse API, which extracts only the verbatim spans relevant to answering the question — without paraphrasing, and preserving chunk IDs for citation.
- **Answer stage.** The compressed, span-only context is then passed to the larger primary model (Claude Sonnet) to generate the final answer, so the expensive model only ever sees the trimmed context.
- **Where the savings come from.** Because the compression step uses a much cheaper model than the answer step, trimming context before the expensive call is what generates net savings even though an extra model call is added; the pattern generalizes to any small/large model pair within a model family on Bedrock.
- **Optional reranking.** Combining the compression step with a reranking stage before it pushes savings and quality further at a small added latency cost.

## 3. Impact — potential & realized

- **Realized (benchmarked on 500+ questions across 9 enterprise document types):** **33% cost reduction** with compression alone, **36%** with reranking added; **8.6x fewer tokens** sent to the primary model with compression alone, **10.1x** with reranking; **+12-19% latency**; answer quality preserved at **97.5% of baseline** on a composite quality score; **hallucination rate down from 51% (baseline) to 44% (compression) to 38%** (compression + reranking).
- **Potential:** most useful for RAG workloads with large retrieved contexts (>5,000 tokens) and narrow questions relative to retrieval breadth — a common shape for enterprise document Q&A — where the cost/quality trade is most favorable.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a clean, well-benchmarked production recipe for a known idea

Using a cheap model to filter context before an expensive model answers isn't new (it's a variant of context compression / prompt distillation patterns already in production elsewhere), but this write-up is unusually well quantified — a real benchmark across 500+ questions and 9 document types, with cost, latency, quality, and hallucination all reported together rather than cherry-picked. That rigor, plus the incidental finding that trimming irrelevant context *reduces* hallucination rather than just cutting cost, is the useful part.

### Similar / related work

- [**Gisting: Compressing LLM Agent Context to Increase Throughput and Cut Cost**](2026-09-01-shopify-gisting-context-compression.md) (in this bank) — the same "shrink the context before the expensive call" idea applied to agent tool-use context rather than RAG retrieval context.
- [**GenRec: Towards LLM-Native Recommendation at Netflix**](2026-08-30-netflix-genrec-llm-native-recommendation.md) (in this bank) — a different context-engineering problem (fitting a huge catalog into an LLM's context) tackled with a catalog-aware model head rather than a compression pass.
- [**From Models to Products: LLMs for Recommendation at Spotify Scale**](2026-08-31-spotify-neo-glide-llm-recommendation-grounding.md) (in this bank) — grounding as a way to reduce a generative model's hallucination-like failures, there via constrained output (semantic IDs) rather than context trimming.

### Jargon buster

- **RAG (Retrieval-Augmented Generation)** — answering a question by first retrieving relevant documents/chunks and passing them to an LLM as context, rather than relying on the model's parametric knowledge alone.
- **Chunk** — a segment of a source document stored and retrieved as a unit in a RAG system.
- **Query-aware compression** — filtering retrieved context down to only the parts relevant to a specific query, rather than passing all retrieved chunks through unfiltered.
- **Reranking** — a second scoring pass over retrieved chunks to reorder them by relevance before they're used, typically with a more precise (but more expensive) model than the initial retriever.
