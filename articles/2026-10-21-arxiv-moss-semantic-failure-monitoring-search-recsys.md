---
id: arxiv-moss-semantic-failure-monitoring-search-recsys
title: "MOSS: A Production Framework for Monitoring and Diagnosing Semantic Failures in Search and Recommendation Systems"
source: "arXiv cs.IR (Nesen et al.)"
url: "https://arxiv.org/abs/2610.26902"
published: "2026-10"
added: "2026-10-21"
category: search-ranking
tags: [llm-as-judge, monitoring, relevance, alerting, production-evaluation]
novelty: 3
sourced_via: "web search"
---

# MOSS: A Production Framework for Monitoring and Diagnosing Semantic Failures in Search and Recommendation Systems

**Source:** [arXiv cs.IR (Nesen et al.)](https://arxiv.org/abs/2610.26902) · Published 2026-10 · Added 2026-10-21
**Category:** search-ranking · **Tags:** `llm-as-judge`, `monitoring`, `relevance`, `alerting`, `production-evaluation`

## TL;DR

MOSS (Model Sanity Service) uses LLM relevance judges to continuously monitor search and recommendation surfaces at a large US retailer, with targeted sampling, strategy-aware prompts, structured alerts and diagnostic follow-ups that classify failures into root causes.

## 1. Business context

Behavioural metrics (clicks, conversion) lag semantic failures by days, and manual review does not scale; most LLM evaluation tooling targets offline datasets, not live monitoring. The gap is detecting when a serving system starts returning irrelevant results before the business metrics move.

## 2. Technical details

Components named in the abstract: targeted sampling of traffic to judge, strategy-aware prompting (the judge is told which recommendation or search strategy produced the item), structured alerting, and diagnostic follow-up prompting that sorts failures into actionable root causes. Judge models, prompts and thresholds are not described in the abstract.

## 3. Impact — potential & realized

Reported: ran in production for over six months across recommendation, search and offer surfaces at a large U.S. retailer and surfaced two confirmed serving defects; for a backfill blending defect the proposed fix cut alert rate by 76.4% relative (quantified offline). On a 498-pair human-annotated recommendation benchmark, frontier LLM judges had higher F1 and AUC point estimates than non-LLM baselines (production embeddings, SBERT), with largest gains on strategy-dependent tasks; the same judge, scale and threshold transferred to a 466-pair, 21-query search benchmark with only a prompt adaptation.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Operationalises LLM relevance judges as live monitors with six months of production evidence.

Monitoring with an LLM judge is a pragmatic evaluation-as-measurement idea: it turns a lagging business metric into a leading semantic one. The value is in the sampling and alert-threshold design, which the abstract omits. Benchmarks are small (498 and 466 pairs) and compare point estimates, so the judge-vs-baseline advantage is not established with intervals; two confirmed defects in six months is useful but anecdotal. Novelty 3/5: the deployment evidence is the contribution rather than the technique.

### Similar / related work

- [**From IR to RecSys: Evaluating LLM-based Judges**](https://www.alphaxiv.org/abs/2511.23312) — LLM relevance judges for recommendation evaluation
- [**arXiv 2609.27953 The Recall Ceiling of LLM Recommendation Reranking**](https://arxiv.org/abs/2609.27953) — a sceptical look at LLM roles in recommendation

### Jargon buster

- **LLM-as-judge** — Using a language model to score outputs (here, relevance of items to a query or context) in place of human raters.
- **F1 / AUC** — Classification quality metrics; F1 balances precision and recall at a threshold, AUC measures ranking quality across thresholds.
