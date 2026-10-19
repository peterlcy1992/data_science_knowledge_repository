---
id: arxiv-jev-llm-judge-reranker-portuguese-ir
title: "Jev-as-a-Judge for Brazilian Portuguese Information Retrieval: Relevance Assessment and Reranking"
source: "arXiv cs.IR (Fernandes & Pereira)"
url: "https://arxiv.org/abs/2610.23346"
published: "2026-10"
added: "2026-10-19"
category: search-ranking
tags: [llm-as-judge, relevance-labels, reranking, evaluation]
novelty: 3
sourced_via: "web search"
---

# Jev-as-a-Judge for Brazilian Portuguese Information Retrieval: Relevance Assessment and Reranking

**Source:** [arXiv cs.IR (Fernandes & Pereira)](https://arxiv.org/abs/2610.23346) · Published 2026-10 · Added 2026-10-19
**Category:** search-ranking · **Tags:** `llm-as-judge`, `relevance-labels`, `reranking`, `evaluation`

## TL;DR

Tests the Jev model as both an LLM relevance judge and a reranker on Brazilian Portuguese retrieval collections: its labels reproduce official system rankings (Kendall's tau 0.90-0.93) and reranking BM25 candidates sharply lifts nDCG@10 on Quati.

## 1. Business context

Building relevance judgments (qrels) by hand is expensive, especially in lower-resource languages. If an LLM judge yields the same system ordering as human labels, teams can evaluate retrieval changes far more cheaply.

## 2. Technical details

Jev is described as a 'System One' model for fast, structured decisions. As a judge it labels four Brazilian Portuguese IR collections, compared against official judgments; as a reranker it reorders the top 1,000 BM25 candidates per query (Quati, 50 test queries). Architecture, prompts and exact judging protocol were not described on the page I read.

## 3. Impact — potential & realized

Realized (as reported): exact agreement with official labels of 52.9-64.9%, quadratic weighted Cohen's kappa 0.52-0.82, and at least 94.5% of annotations exact or within one relevance level. Judge-generated labels give system rankings with Kendall's tau 0.90-0.93 on NormasTCU and Ulysses-RFCorpus. On Quati, nDCG@10 rose from 0.3329 to 0.6331 (+90.2%) and MRR from 0.6852 to 0.9033 (+31.8%). Label-level agreement is moderate even though system-level ranking agreement is high.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — The DS-relevant lesson is the gap between label agreement (about 53-65% exact) and ranking agreement (tau about 0.

The DS-relevant lesson is the gap between label agreement (about 53-65% exact) and ranking agreement (tau about 0.9): a judge can be fine for comparing systems while still noisy per item. Novelty is modest; the value is the language-specific validation. Caveat: abstract-level read.

### Similar / related work

- [**From a Large-Scale Teacher to Efficient Multimodal Students for Search Relevance Prediction**](2026-10-15-arxiv-multimodal-students-llm-judge-search-relevance.md) (in this bank) — LLM-as-judge for search relevance at industrial scale

### Jargon buster

- **Qrels** — Human relevance judgments mapping query-document pairs to relevance grades, the ground truth for IR evaluation.
- **Kendall's tau** — A rank-correlation measure; 1 means two orderings of systems agree perfectly.
- **nDCG@10** — Ranking quality over the top 10 results, rewarding relevant items placed higher.
