---
id: arxiv-trustworthy-method-comparison-ai-judges
title: "Trustworthy Method Comparison with AI Judges: Estimation and Design under Order, Batch, and Aggregation Effects"
source: "arXiv (Tianxi Li, Jie Ding)"
url: "https://arxiv.org/abs/2610.07755"
published: "2026-10"
added: "2026-10-07"
category: statistical-modeling
tags: [llm-as-judge, generalized-linear-mixed-models, evaluation-design, williams-design, order-effects]
novelty: 3
sourced_via: "web search"
---

# Trustworthy Method Comparison with AI Judges: Estimation and Design under Order, Batch, and Aggregation Effects

**Source:** [arXiv (Tianxi Li, Jie Ding)](https://arxiv.org/abs/2610.07755) · Published 2026-10 · Added 2026-10-07
**Category:** statistical-modeling · **Tags:** `llm-as-judge`, `generalized-linear-mixed-models`, `evaluation-design`, `williams-design`, `order-effects`

## TL;DR

LLM-judge scoring behaves like a Markov generalized linear mixed model. Randomizing prompt order and averaging works for leaderboard ranking, but naive averaging is unreliable for group-level comparisons.

## 1. Business context

LLM judges are widely used to compare methods, models and prompts, but their scores depend on presentation order, batching and how results are aggregated, which makes comparisons less trustworthy than they look.

## 2. Technical details

The authors show that LLM evaluation mechanisms can be approximated by a class of Markov GLMMs, validated across three commercial LLMs. For leaderboard ranking, randomizing prompt sequences and averaging scores is statistically consistent under mild separation conditions, and a Williams square design improves efficiency when items are of similar quality. For group comparison, naive averaging can mislead because of nonlinearity in the response model. Inference is checked beyond first-order theory, including higher-order sequence memory. Demonstrated by comparing two graphical-model estimation methods with AI judges.

## 3. Impact — potential & realized

Realized: statistical guidance for designing judge-based comparisons (when plain averaging is fine, when it is not). Potential: judge-based evaluation with proper uncertainty quantification. No production metrics reported in the material seen.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Applies classical experimental-design thinking (order effects, Williams designs, mixed models) to an LLM-eval problem, squarely at the DS/AI boundary.

Applies classical experimental-design thinking (order effects, Williams designs, mixed models) to an LLM-eval problem, squarely at the DS/AI boundary. Pairs naturally with variance-components thinking in the agentic-RAG eval paper from yesterday.

### Similar / related work

- [**Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads**](2026-10-06-arxiv-agentic-rag-evaluation-budget-allocation.md) (in this bank) — same theme: statistical design for noisy LLM evaluation
- [**Second-Order Response Laws for LLM Judges**](https://arxiv.org/abs/2608.16253) — related work on separating sampling noise from prompt variation in judge scores

### Jargon buster

- **GLMM** — Generalized linear mixed model: a regression with both fixed effects and random effects, for non-normal outcomes.
- **Williams square design** — A crossover layout that balances order and carry-over effects across items.
- **LLM-as-judge** — Using an LLM to score or compare outputs instead of human raters.
- **Markov (sequence) effect** — Where a score depends on what the judge saw just before it.
