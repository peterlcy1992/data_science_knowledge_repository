---
id: arxiv-agentic-retrieval-performance-costs
title: "Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks"
source: "arXiv (Esfandiarpoor et al., NVIDIA)"
url: "https://arxiv.org/abs/2610.05750"
published: "2026-10"
added: "2026-10-06"
category: search-ranking
tags: [agentic-retrieval, ReAct, nDCG, latency-cost, BRIGHT]
novelty: 3
sourced_via: "web search"
---

# Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks

**Source:** [arXiv (Esfandiarpoor et al., NVIDIA)](https://arxiv.org/abs/2610.05750) · Published 2026-10 · Added 2026-10-06
**Category:** search-ranking · **Tags:** `agentic-retrieval`, `ReAct`, `nDCG`, `latency-cost`, `BRIGHT`

## TL;DR

A ReAct-style agentic retrieval loop on top of the same embedding model improves nDCG@10 by 8.7 points but takes about 107.4 s per query vs. 0.67 s for plain dense retrieval.

## 1. Business context

Reasoning-intensive and multimodal retrieval tasks defeat plain semantic similarity. Agentic retrieval promises better results but its cost is rarely quantified, which blocks production decisions.

## 2. Technical details

The system wraps a standard dense retriever in an LLM ReAct loop that iteratively reasons, issues queries and refines. It is evaluated on the ViDoRe v3 and BRIGHT leaderboards using identical embedding models, and the authors present it as generalizing across benchmarks where specialized retrievers struggled out of domain.

## 3. Impact — potential & realized

Reported: +8.7 nDCG@10 points; roughly 160x slower (107.4 s vs. 0.67 s per query); about 764.1K input and 5.8K output tokens per query. Code is public per the abstract. Full paper not read.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Useful because it prints the cost side of the quality-cost trade-off with real numbers.

Useful because it prints the cost side of the quality-cost trade-off with real numbers. The gain-per-token ratio looks steep for online use, so this is likelier to matter for offline or high-value queries, motivating distillation. The method itself is a known pattern.

### Similar / related work

- [**Databricks Adaptive Instructed Retriever**](2026-09-29-databricks-adaptive-instructed-retriever.md) (in this bank) — agentic retrieval with latency focus
- [**Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads**](https://arxiv.org/abs/2610.05034) — how to evaluate such systems reliably

### Jargon buster

- **ReAct** — An agent pattern interleaving reasoning steps with tool actions such as search calls.
- **nDCG@10** — A ranking-quality metric that rewards placing relevant results near the top of the first ten.
- **BRIGHT** — A benchmark of reasoning-intensive retrieval queries.
