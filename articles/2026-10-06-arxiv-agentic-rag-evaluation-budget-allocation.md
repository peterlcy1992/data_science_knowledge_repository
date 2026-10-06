---
id: arxiv-agentic-rag-evaluation-budget-allocation
title: "Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads"
source: "arXiv (Jingjie Ning, Xueqi Li, Yibo Kong)"
url: "https://arxiv.org/abs/2610.05034"
published: "2026-10"
added: "2026-10-06"
category: llm-genai
tags: [llm-evaluation, generalizability-theory, variance-components, agentic-rag, measurement]
novelty: 4
sourced_via: "web search"
---

# Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads

**Source:** [arXiv (Jingjie Ning, Xueqi Li, Yibo Kong)](https://arxiv.org/abs/2610.05034) · Published 2026-10 · Added 2026-10-06
**Category:** llm-genai · **Tags:** `llm-evaluation`, `generalizability-theory`, `variance-components`, `agentic-rag`, `measurement`

## TL;DR

Applies generalizability theory to agentic-RAG evaluation to decide how to split a fixed token budget between more questions, more trajectories per question, and repeated reads: at roughly 34M tokens, broader question coverage cuts standard error by 33% vs. five reads and 12.6% vs. three trajectories.

## 1. Business context

Evaluating agentic RAG systems is noisy: an agent can follow different search trajectories and the judge can read the same trajectory differently. Teams with a fixed evaluation budget have little guidance on whether to buy more questions or more repeats, so many default to repeated runs that mostly re-measure noise.

## 2. Technical details

The study uses generalizability theory and repeated sampling on HotpotQA and MuSiQue to decompose evaluation variance into question, trajectory and read components, then predicts the standard error of different allocations. It reports predictive models for budget allocation with 3.5-4.0% accuracy, and shows that setting temperature to zero (vs. default) reduced answer disagreement from 14.3% to 3.4%.

## 3. Impact — potential & realized

Reported: broader question coverage lowers standard error by 33% vs. five reads and 12.6% vs. three trajectories at about 34M model tokens; single-read variance penalties ranged from 0 to 9.9% relative to optimal allocations; at lower API price tiers the cost analysis still favors adding questions. Results are on two multi-hop QA benchmarks (full paper not read), so allocation ratios may shift for other tasks.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A statistician's answer to an LLM-eval question: variance components and sample-size allocation, the same logic as clustered A/B power analysis, applied to agent evals.

A statistician's answer to an LLM-eval question: variance components and sample-size allocation, the same logic as clustered A/B power analysis, applied to agent evals. The headline ("more questions beats more repeats") is intuitive but quantifying it is what makes it actionable. Only two benchmarks, so treat the exact numbers as indicative. Likely to be copied by eval teams.

### Similar / related work

- [**Grab-Bench: evaluating AI on production work**](2026-09-29-grab-bench-evaluating-ai-production-work.md) (in this bank) — agent evaluation in practice
- [**Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks**](https://arxiv.org/abs/2610.05750) — same-day paper on agentic retrieval cost
- **Generalizability theory (Cronbach et al.)** — the measurement framework used (no specific URL linked)

### Jargon buster

- **Generalizability theory** — A framework that splits measurement variance into facets (here questions, trajectories, reads) to plan reliable measurement.
- **Trajectory** — One full sequence of searches and reasoning steps an agent takes on a question.
- **Standard error** — The uncertainty of the measured average score; smaller means a more reliable evaluation.
