---
id: aws-agent-evaluation-metric-multiturn
title: "Agent Evaluation Metric for Multi-Turn Conversations"
source: "AWS Machine Learning Blog"
url: "https://aws.amazon.com/blogs/machine-learning/agent-evaluation-metric-for-multi-turn-conversations/"
published: "2026-09"
added: "2026-09-16"
category: llm-genai
tags: [agent-evaluation, multi-turn, llm-as-judge, error-attribution, observability]
novelty: 3
sourced_via: "web search"
---

# Agent Evaluation Metric for Multi-Turn Conversations

**Source:** [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/agent-evaluation-metric-for-multi-turn-conversations/) · Published 2026-09 · Added 2026-09-16
**Category:** LLMs & Generative AI · **Tags:** `agent-evaluation`, `multi-turn`, `llm-as-judge`, `error-attribution`, `observability`

## TL;DR

AWS proposes the Agent Evaluation Metric (AEM), a turn-level framework that scores multi-turn agent conversations on truthfulness and completeness per turn, then attributes each failure as either a root cause or a cascading consequence of an earlier mistake — replacing single, holistic outcome scores that obscure exactly where an agent went wrong.

## 1. Business context

Multi-turn agentic assistants (AWS points to enterprise tools like Amazon Quick Suite) fail in a specific, hard-to-debug way: one early mistake — a misread parameter, a wrong tool call — quietly corrupts every downstream turn. Traditional outcome-level scoring (did the final answer look right?) treats a five-turn conversation with one root-cause error and three inherited failures as four independent problems, sending debugging effort in four directions instead of one. AWS built AEM to fix that attribution gap so teams can find and fix the minimal set of actual causes.

## 2. Technical details

AEM decomposes correctness into two independently-scored sub-metrics per turn:

- **Truthfulness** — are the values and statements in this turn factually consistent with the expected output?
- **Completeness** — are all required elements present (parameters supplied, information covered)?

Both sub-metrics apply uniformly to "response turns" (the agent replying to the user) and "action turns" (the agent invoking a tool), rather than using separate scoring schemes for each.

Equivalence between predicted and expected content is judged via **semantic similarity scoring** rather than brittle exact string matching — either fast, transparent embedding-based similarity or a more nuanced LLM-as-judge call, with a configurable threshold (default 0.5) converting the continuous similarity score into a pass/fail verdict.

The framework's central contribution is its **failure taxonomy**, used to separate root causes from cascades: structural errors (`tool_mismatch`, `action_mismatch`), truthfulness errors (`inconsistent_response`, `inconsistent_parameter_values`), completeness errors (`incomplete_response`, `missing_parameters`, `extra_parameters`), and a dedicated `prior_action_failed` label marking a turn's failure as inherited rather than original. Per-turn pass/fail verdicts then compose into a single conversation-level score — the proportion of turns that pass, or a weighted/gated variant, with the composition rule left pluggable.

The worked example in the post: a five-turn sales-report conversation where turn 2 confuses "profit" with "revenue" — a single parameter error — which then cascades into failures at turns 3 through 5. AEM's attribution isolates the one root cause instead of reporting four unrelated failures. The pipeline integrates as a custom evaluator in the Strands Agents evaluation SDK, alongside existing goal-completion and LLM-as-judge scorers, and is intended to run continuously in production, tracking correctness trends by release, by conversation/tool-chain complexity, and by failure-reason category.

Notably, the post is candid about its own limits: it provides no empirical benchmark numbers or comparative results against alternative metrics, presenting the framework conceptually via the worked example rather than validating it on a large evaluation dataset.

## 3. Impact — potential & realized

**Realized:** AEM is presented as an available custom evaluator inside AWS's Strands Agents evaluation SDK, with a documented worked example demonstrating root-cause isolation on a synthetic five-turn conversation.

**Potential:** The decompose-evaluate-compose design pattern is explicitly built to extend — AWS notes that safety, instruction retention, and reasoning depth could follow the same structure as additional sub-metrics, with a follow-up post on safety evaluation flagged as planned. For any team running production multi-turn agents, the framework offers a template for moving from "the conversation failed somewhere" to "turn 2 is the root cause" without building bespoke attribution logic from scratch.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A useful, sensible framework, presented without validation

Decomposing agent evaluation into per-turn sub-metrics and explicitly separating root causes from cascading failures is a genuinely useful idea that's underserved in most agent-evaluation tooling, which still leans heavily on end-to-end pass/fail or single LLM-judge scores. But this is a framework proposal, not a validated result: there are no benchmark numbers, no comparison against existing multi-turn eval approaches, and the worked example is synthetic. It reads as solid, exportable methodology rather than a proven advance — worth adopting for the idea, not for demonstrated superiority.

### Similar / related work

- [**How DoorDash Leverages LLMs to Evaluate Search Result Pages**](2026-09-15-doordash-autoeval-llm-search-evaluation.md) (in this bank) — another LLM-as-judge evaluation system from the same week, applied to search relevance rather than multi-turn agent conversations, useful contrast in what "evaluation" means across different product surfaces.
- [**Evaluating Netflix Show Synopses with LLM-as-a-Judge**](2026-09-14-netflix-llm-judge-show-synopses.md) (in this bank) — a single-turn LLM-as-judge application; AEM's multi-turn, cascade-aware attribution is a meaningful step beyond this kind of single-output judging.
- **Agent benchmark suites with multi-turn evaluation (e.g. τ-bench, AgentBench-style benchmarks)** — the broader body of multi-turn agent evaluation work this framework could be validated against; no specific comparison was made in the source post.

### Jargon buster

- **LLM-as-judge** — Using a language model to score or grade another model's output (e.g. for correctness or relevance) instead of, or alongside, human raters or exact-match rules.
- **Root-cause attribution** — In a sequence of dependent steps, identifying which specific step's error is the original cause versus which later failures are just downstream consequences of that same original error.
- **Semantic similarity scoring** — Comparing two pieces of text by how close their meanings are (e.g. via embedding distance) rather than requiring an exact character-for-character match, so paraphrased-but-correct answers still score as correct.
- **Strands Agents (evaluation SDK)** — AWS's SDK for building and evaluating agentic applications; AEM is implemented as a pluggable custom evaluator within it.
