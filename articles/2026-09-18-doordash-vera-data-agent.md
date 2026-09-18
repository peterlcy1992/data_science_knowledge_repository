---
id: doordash-vera-data-agent
title: "Inside Vera, DoorDash's Data Agent"
source: "DoorDash Engineering Blog"
url: "https://careersatdoordash.com/blog/inside-vera-doordashs-data-agent/"
published: "2026-09"
added: "2026-09-18"
category: llm-genai
tags: [data-agent, agent-harness, text-to-sql, claude-code, codex, business-analytics, evaluation]
novelty: 3
sourced_via: "web search"
---

# Inside Vera, DoorDash's Data Agent

**Source:** [DoorDash Engineering Blog](https://careersatdoordash.com/blog/inside-vera-doordashs-data-agent/) · Published 2026-09 · Added 2026-09-18
**Category:** LLMs & Generative AI · **Tags:** `data-agent`, `agent-harness`, `text-to-sql`, `claude-code`, `codex`, `business-analytics`, `evaluation`

## TL;DR

DoorDash built Vera, a purpose-built data agent, to answer business questions like "why did order volume dip in California last week?" directly against its fragmented, semi-structured data estate. In a head-to-head test on the same underlying model, Vera scored a 73% pass rate versus 48% for Claude Code wired up with the same SQL tools — evidence that harness design, not raw model choice, is what currently separates a usable data agent from a generic coding agent.

## 1. Business context

DoorDash's Data organization exists to give every business function — ops, marketing, finance, product — fast, accurate answers to ad hoc questions about the business. Historically this meant a human data analyst tracing the question through DoorDash's sprawling, "super-fragmented" upstream data sources: dozens of tables and pipelines spread across teams, each with its own conventions, freshness guarantees, and undocumented gotchas. General-purpose coding-agent harnesses such as OpenAI's Codex and Claude Code are strong at writing and running code, and it's tempting to assume they can be pointed at a data warehouse and just work. DoorDash's experience says otherwise at this scale: agentic models given only generic SQL tool access perform suboptimally against a large, semi-structured, fragmented data footprint, because success depends less on the model's raw reasoning and more on whether it has the business context, data-modeling knowledge, and validation scaffolding to avoid confidently wrong answers.

## 2. Technical details

Vera is a data agent built on top of frontier agentic models, but the DoorDash team's central finding is that the **harness** around the model — not the model itself — is the dominant lever for quality. To isolate that variable, they ran a controlled comparison: they gave Claude Code the same model (Opus 4.8), the same SQL access tools, and the same skills that Vera uses, then measured both systems on the same evaluation set. Claude Code scored 2.16/3.0 (a 48% pass rate); Vera scored 2.60/3.0 (a 73% pass rate) — a large gap attributable entirely to harness differences rather than model capability.

The harness additions that DoorDash calls out as the dominant vector for improvement are: injecting business context so the agent knows what a metric or entity actually means inside DoorDash; a knowledge-retrieval layer over data documentation and past query patterns; explicit data-modeling guidance so the agent picks the right joins and grain instead of a plausible-looking wrong one; and SQL validation and execution guardrails that catch malformed or semantically invalid queries before they produce a confidently wrong answer. The team also studied performance across different underlying models and reasoning-effort settings, treating the choice of harness component as at least as important as which model or reasoning budget is selected.

## 3. Impact — potential & realized

**Realized:** the controlled Vera-vs-Claude-Code comparison on a shared model shows a 25-point pass-rate gap (73% vs. 48%) driven purely by harness engineering, giving DoorDash a reusable, quantified argument for where to invest engineering effort on future agents.

**Potential:** the harness pattern — business context injection, retrieval over data documentation, explicit data-modeling rules, and SQL validation — is a template DoorDash and other teams building "talk to your data warehouse" agents can reuse regardless of which frontier model or coding-agent CLI sits underneath, and it suggests that data-agent quality will keep improving even without waiting for better base models.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-instrumented confirmation of a pattern the field is converging on

The finding that "the harness matters more than the model" is not new in the abstract — it echoes what production coding-agent teams (including DoorDash's own prior work) have been saying all year. What is genuinely useful here is the controlled experiment: holding the model and base tools fixed and swapping only the harness, then reporting a specific, reproducible number (73% vs. 48%) rather than an anecdote. That is a solid production-first contribution, not a new paradigm.

### Similar / related work

- [**Agentic Machine Learning Modeling at Instacart**](2026-09-15-instacart-agentic-machine-learning-modeling.md) (in this bank) — another company quantifying what agentic harnesses can and can't be trusted to do unsupervised in a data/ML context.
- [**CORAL: An LLM-Native Harness for Production Recommender Systems**](2026-09-10-meta-coral-llm-agent-recsys-harness.md) (in this bank) — a parallel argument that a closed-loop harness around an LLM, not the LLM alone, is what makes agentic systems production-viable.
- [**Beyond the Model: Engineering AI Infra with Scientific Judgement**](2026-09-17-airbnb-insight-miner-agent-harness-scientific-judgement.md) (in this bank) — Airbnb's version of the same thesis applied to unstructured-data investigation rather than SQL analytics.

### Jargon buster

- **Agent harness** — the scaffolding (tools, prompts, retrieval, validation) wrapped around a raw LLM to turn it into a reliable agent for a specific task.
- **Reasoning effort** — a configurable setting on some frontier models that trades inference cost/latency for more deliberate, multi-step reasoning before answering.
