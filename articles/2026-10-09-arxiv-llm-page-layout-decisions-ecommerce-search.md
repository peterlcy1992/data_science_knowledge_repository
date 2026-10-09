---
id: arxiv-llm-page-layout-decisions-ecommerce-search
title: "Language Models for Page-Level Layout Decisions in E-commerce Search"
source: "arXiv cs.LG / RecSys 2026 OARS workshop (Joshi, Song, Zhai)"
url: "https://arxiv.org/abs/2610.10920"
published: "2026-10"
added: "2026-10-09"
category: search-ranking
tags: [offline-evaluation, llm-as-judge, page-layout, embeddings, ecommerce-search]
novelty: 3
sourced_via: "web search"
---

# Language Models for Page-Level Layout Decisions in E-commerce Search

**Source:** [arXiv cs.LG / RecSys 2026 OARS workshop (Joshi, Song, Zhai)](https://arxiv.org/abs/2610.10920) · Published 2026-10 · Added 2026-10-09
**Category:** search-ranking · **Tags:** `offline-evaluation`, `llm-as-judge`, `page-layout`, `embeddings`, `ecommerce-search`

## TL;DR

Deciding whether and where to insert a secondary product stack on a search page normally needs costly online A/B tests. The authors compare three ways to use language models as offline evaluators and find representation-based approaches beat prompt-based judging at predicting user engagement.

## 1. Business context

E-commerce search pages now mix ranked results with recommender modules. A well-placed stack can lift engagement; a badly placed one disrupts browsing and hurts primary results. Ranking can be evaluated offline (e.g. interleaving), but page-level layout decisions have mostly required online A/B tests.

## 2. Technical details

Three approaches to language models as scalable evaluators are compared: direct prompt-based judging, prompt-derived features, and representation-based methods. Target: predict user engagement for a given stack-and-position decision. Finding: representation-based methods consistently outperform prompt-based judging. No metrics or datasets are given on the abstract page.

## 3. Impact — potential & realized

Realized: relative ranking of the three approaches only (no numbers visible). Potential: cheaper screening of layout candidates before spending A/B traffic.

*Sourced from the arXiv abstract page; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Workshop-level but a useful negative for zero-shot LLM judging.

The takeaway that learned representations trained against engagement beat zero-shot LLM judgement matches the broader pattern that judges need calibration against behavioural outcomes. Without numbers, I would not generalise beyond this setting.

### Similar / related work

- [**LLM-based Relevance Assessment for Web-Scale Search Evaluation at Pinterest**](2026-10-08-pinterest-llm-relevance-assessment-search-evaluation.md) (in this bank) — related work on the same theme
- [**How DoorDash Leverages LLMs to Evaluate Search Result Pages**](2026-09-15-doordash-autoeval-llm-search-evaluation.md) (in this bank) — related work on the same theme
- [**Using MemAlign to Improve Evaluation of Traditional Machine Learning in Genie Code**](2026-09-18-databricks-memalign-llm-judges.md) (in this bank) — related work on the same theme

### Jargon buster

- **Interleaving** — Online ranking evaluation by mixing two rankers' results in one list and observing which gets clicked.
- **Representation-based method** — Use embeddings from a model as features for a supervised predictor, rather than asking the model for a verdict.
