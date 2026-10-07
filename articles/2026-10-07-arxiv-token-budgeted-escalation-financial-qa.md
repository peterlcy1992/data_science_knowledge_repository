---
id: arxiv-token-budgeted-escalation-financial-qa
title: "Token-Budgeted Escalation for Financial Document QA"
source: "arXiv (Junru Zhu, Yixin Yang, Xiaoqing Ding, Ruoyu Qi)"
url: "https://arxiv.org/abs/2610.07760"
published: "2026-10"
added: "2026-10-07"
category: llm-genai
tags: [rag, token-budget, escalation, cost-benefit, financebench]
novelty: 3
sourced_via: "web search"
---

# Token-Budgeted Escalation for Financial Document QA

**Source:** [arXiv (Junru Zhu, Yixin Yang, Xiaoqing Ding, Ruoyu Qi)](https://arxiv.org/abs/2610.07760) · Published 2026-10 · Added 2026-10-07
**Category:** llm-genai · **Tags:** `rag`, `token-budget`, `escalation`, `cost-benefit`, `financebench`

## TL;DR

For RAG over financial documents, extra-call cost is highly predictable but benefit is not. Ranking queries by predicted gain-per-token at a 10% token budget beat uniform top-5 retrieval on cost while keeping most of the quality.

## 1. Business context

RAG systems can improve answers by escalating hard queries to more retrieval, but tokens cost money. The question is which queries deserve the extra spend under a fixed budget.

## 2. Technical details

Evaluated on 150 FinanceBench questions with a two-stage setup: initial answer with top-1 retrieval, optional escalation to top-5. Escalation candidates are ranked by predicted benefit-to-cost ratio. Additional-call cost is predictable (R-squared 0.93), but predicting which queries benefit is hard (AUROC 0.60).

## 3. Impact — potential & realized

Realized: at a 10% token budget, gain-per-token prioritization improved answer quality by 0.034 points while using 46.6% fewer tokens than uniform top-5 for all queries (per the abstract). Small benchmark (150 questions); the paper itself flags benefit prediction as the bottleneck.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A decision-under-budget framing (predict cost, predict uplift, rank by ratio) that is essentially uplift-targeting applied to LLM calls.

A decision-under-budget framing (predict cost, predict uplift, rank by ratio) that is essentially uplift-targeting applied to LLM calls. Candid about the weak benefit model (AUROC 0.60), which is the useful lesson: the gain is limited by uplift estimation, not by cost estimation.

### Similar / related work

- [**Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads**](2026-10-06-arxiv-agentic-rag-evaluation-budget-allocation.md) (in this bank) — budget allocation for evaluating agentic RAG
- [**Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks**](2026-10-06-arxiv-agentic-retrieval-performance-costs.md) (in this bank) — cost/performance trade-offs of agentic retrieval

### Jargon buster

- **Escalation** — Re-running a query with a more expensive configuration (here, more retrieved passages).
- **AUROC** — Probability that a randomly chosen positive case is ranked above a randomly chosen negative; 0.5 is chance.
- **Gain-per-token** — Predicted quality improvement divided by predicted token cost.
- **FinanceBench** — A question-answering benchmark over financial filings.
