---
id: grab-agentic-analytics-autonomy-ladder
title: "How AI is Transforming Analytics at Grab"
source: "Grab Tech (Engineering Blog)"
url: "https://engineering.grab.com/how-ai-is-transforming-analytics"
published: "2026-08"
added: "2026-09-11"
category: llm-genai
tags: [ai-agents, analytics-automation, autonomy-levels, data-catalog, governance, grab]
novelty: 3
sourced_via: "web search"
---

# How AI is Transforming Analytics at Grab

**Source:** [Grab Tech](https://engineering.grab.com/how-ai-is-transforming-analytics) · Published 2026-08 · Added 2026-09-11
**Category:** LLMs & Generative AI · **Tags:** `ai-agents`, `analytics-automation`, `autonomy-levels`, `data-catalog`, `governance`, `grab`

## TL;DR

Grab adapted a five-level coding-autonomy framework to internal analytics, using agent platforms (Spartan, Scarlet), a certified-metrics catalog (ContextIQ), and a self-serve portal (BriX) to shift analysts from writing every query themselves to framing questions and reviewing agent output — cutting mechanical analyst work from 44% to 30% of tickets in four months.

## 1. Business context

Grab's analytics throughput was bottlenecked by analyst capacity: every ad-hoc question, report, or SQL pull competed for the same finite pool of people who could write the code. The team's bet is that "model capability has crossed a threshold" where routine analytical work — writing queries, validating results, drafting first-pass narratives — can be automated, freeing analysts to spend their time on problem framing, causal reasoning, and stakeholder judgment instead of artifact production.

## 2. Technical details

Grab adapted Dan Shapiro's coding-autonomy ladder to analytics, defining five levels: **L2 (AI-assisted)** — humans do every step, AI drafts SQL and suggests charts; **L3 (human plans, agent executes)** — humans frame the question and review evidence while an agent discovers data, writes and runs queries, and drafts a narrative; **L4 (agent plans)** — humans set intent and guardrails and review at defined gates while the agent orchestrates the full workflow; **L5 (end-to-end autonomous)** — humans review only exceptions while the agent detects anomalies, runs the full loop, and evolves its own metrics. Grab is explicit that human judgment stays load-bearing at every level for problem framing, metric definitions, causal reasoning, and stakeholder relationships — autonomy climbs for execution, not for deciding what matters.

The system rests on five capabilities, each with a named internal tool: **execution** via an agentic workflow stack (Spartan, with 50+ skills and 120+ analysis frameworks, and Scarlet, near-self-healing data pipelines with autonomous root-cause analysis); **knowledge** via ContextIQ, which manages the lifecycle of certified metric definitions so agents ground their answers in agreed-upon business logic rather than reinventing metrics; **control**, mechanical checks plus human review gates at defined points; **review & governance**, agents self-checking against escalation triggers before surfacing results; and **learning**, encoding failures back into context documents, datasets, and evaluation sets so mistakes don't repeat. BriX is the internal portal that exposes L3-level workflows self-serve across the company.

## 3. Impact — potential & realized

**Realized:** mechanical analyst work fell from 44% to 30% of tickets between February and June 2026; resolution cycle time dropped roughly 33%; human involvement in the self-serve channel fell from 50% (March) to 25% (May); fully-autonomous response rates rose across categories — metric questions from 53% to 67%, data pulls from 63% to 90%, SQL requests from 50% to 81%; and Grab estimates 230–470 business days of stakeholder-facing work removed from the backlog via self-serve agents.

**Potential:** the autonomy-ladder framing — separating "how much of the workflow the agent owns" from "where human judgment is non-negotiable" — is a reusable governance pattern for any team introducing agentic automation into a human analytics or operations function, not just Grab's specific tools.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clear, well-instrumented production-first take on an established framework

Adapting a coding-autonomy ladder (not Grab's own invention) to analytics work is a smart transposition rather than a new idea, and agent-assisted SQL/BI has been explored elsewhere. What earns this a 3 rather than a 2 is the rigor of the reported instrumentation — response-rate breakdowns by task type, month-over-month tracking of human-involvement percentages, and an explicit "human judgment stays at every level" governance stance that avoids the common overclaim of full autonomy. It's a genuinely useful operational case study for anyone building similar internal agent tooling.

### Similar / related work

- [**Etsy — Context Engineering for Employee Q&A**](2026-09-06-etsy-context-engineering-employee-qa.md) (in this bank) — another internal-facing LLM system built around a certified/curated knowledge layer, useful contrast on grounding strategy (context engineering vs. Grab's certified-metrics catalog).
- [**Data Mesh at Grab (Part III): Operationalizing Data Reliability with Automated DPIs**](https://engineering.grab.com/data-mesh-at-grab-part-three) — Grab's own related infrastructure piece on automated data-quality triage, which underpins the "near-self-healing pipelines" (Scarlet) referenced here.
- **"The Permission Ladder" style autonomy frameworks (general agent-ops literature)** — the broader family of staged-autonomy models (trust ladders, permission ladders) this L2–L5 framework belongs to; useful for comparing Grab's specific level definitions against others in the field.

### Jargon buster

- **Autonomy ladder** — a staged framework (here L2 through L5) describing how much of a workflow an AI agent is trusted to run end-to-end versus requiring human review at each step.
- **Certified metrics catalog** — a governed, discoverable repository of agreed-upon metric definitions that agents (and humans) query against, so "revenue" or "active users" means the same thing everywhere rather than being redefined ad hoc.
- **Self-healing data pipeline** — a pipeline that can detect its own failures (missing data, schema drift) and attempt automated root-cause analysis and remediation before a human is paged.
- **Escalation trigger** — a predefined condition (e.g., an anomaly outside expected bounds, a low-confidence answer) that forces an agent to hand off to a human rather than proceeding autonomously.
