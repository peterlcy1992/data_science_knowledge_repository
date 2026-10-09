---
id: arxiv-backbone-evolution-llm-relevance-assessments
title: "The Impact of Backbone Evolution on LLM-Based Relevance Assessments"
source: "arXiv cs.IR (Yu, Zuccon, Leelanupab)"
url: "https://arxiv.org/abs/2610.09820"
published: "2026-10"
added: "2026-10-09"
category: search-ranking
tags: [llm-as-judge, relevance-judgments, umbrela, exam, model-drift]
novelty: 3
sourced_via: "web search"
---

# The Impact of Backbone Evolution on LLM-Based Relevance Assessments

**Source:** [arXiv cs.IR (Yu, Zuccon, Leelanupab)](https://arxiv.org/abs/2610.09820) · Published 2026-10 · Added 2026-10-09
**Category:** search-ranking · **Tags:** `llm-as-judge`, `relevance-judgments`, `umbrela`, `exam`, `model-drift`

## TL;DR

Holding prompts fixed and swapping in successive versions of Gemini, GPT, Qwen and Llama models, the authors find no consistent evidence that newer models are better relevance judges; aggregate agreement can hold steady while individual judgments change.

## 1. Business context

IR evaluation increasingly replaces human relevance labels with LLM judges. Teams assume that upgrading the backbone only helps. If judge behaviour shifts across versions, historical evaluation numbers stop being comparable.

## 2. Technical details

Two judging prompts, UMBRELA (single prompt) and EXAM (rubric-based), are held fixed across sequential versions of commercial (Gemini, GPT) and open-weight (Qwen, Llama) families. Agreement with human judgments is checked in aggregate and per judgment. Result: no consistent improvement with newer versions; some answers an earlier version got right are lost in later ones even when aggregate scores are similar or better. The authors examine causes of these regressions and conclude that a prompt validated on one model version cannot be assumed to work as well after an update.

## 3. Impact — potential & realized

Realized: empirical caution against assuming monotone improvement. Potential: motivates re-validating judges (and freezing versions) as part of evaluation governance. No figures in the abstract.

*Sourced from the arXiv abstract page; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Small but practical: treat the LLM judge as a measurement instrument that needs recalibration.

For anyone tracking a metric over months with an LLM judge, this is a drift warning. The per-judgment vs. aggregate distinction mirrors a measurement-validity point: equal averages can hide different errors.

### Similar / related work

- [**LLM-based Relevance Assessment for Web-Scale Search Evaluation at Pinterest**](2026-10-08-pinterest-llm-relevance-assessment-search-evaluation.md) (in this bank) — related work on the same theme
- [**Trustworthy Method Comparison with AI Judges**](2026-10-07-arxiv-trustworthy-method-comparison-ai-judges.md) (in this bank) — related work on the same theme
- [**How DoorDash Leverages LLMs to Evaluate Search Result Pages**](2026-09-15-doordash-autoeval-llm-search-evaluation.md) (in this bank) — related work on the same theme

### Jargon buster

- **UMBRELA / EXAM** — Two LLM-based relevance-assessment prompting schemes: a single-prompt judge and a rubric-based one.
- **Backbone** — The underlying LLM used to power a judge or system.
