---
id: uber-software-factory-efficient-agent-cost
title: "Running a Software Factory Efficiently at Uber Scale"
source: "Uber Engineering"
url: "https://www.uber.com/us/en/blog/efficient-software-factory/"
published: "2026-08"
added: "2026-09-01"
category: llm-genai
tags: [coding-agents, cost-management, model-routing, prompt-caching, mcp, developer-productivity]
novelty: 3
sourced_via: "full-text fetch"
---

# Running a Software Factory Efficiently at Uber Scale

**Source:** [Uber Engineering](https://www.uber.com/us/en/blog/efficient-software-factory/) · Published 2026-08 · Added 2026-09-01
**Category:** LLMs & Generative AI · **Tags:** `coding-agents`, `cost-management`, `model-routing`, `prompt-caching`

## TL;DR

Uber manages the cost of its internal coding-agent platform — now authoring
more than 70% of PRs and running 30,000+ skill invocations daily — by
decomposing spend as users × sessions × turns × requests × tokens × price and
optimizing each factor. Benchmark-driven model routing, prompt caching,
CLI-based tool access, and code-mode batching cut cost per 1,000 requests
34% and cost per session 52% since a June 2026 peak, even as usage grew
7-9x.

## 1. Business context

As Uber's internal coding-agent platform scaled, usage grew far faster than
anyone had budgeted for, and unmanaged frontier-model spend threatened to
grow linearly — or worse — with that usage. Uber needed a systematic
framework for attacking cost, rather than ad hoc cuts that risk degrading
the platform's usefulness.

## 2. Technical details

- **Cost decomposition.** Spend is broken down as **users × sessions ×
  turns × requests × tokens × price** — a framework for identifying which
  specific factor to attack rather than cutting broadly.
- **Benchmark-driven model routing.** Requests are routed to the cheapest
  model that still clears a quality benchmark, instead of always calling the
  top frontier model.
- **Prompt caching.** Reusing cached prompt prefixes across repeated calls
  avoids recomputing the same tokens.
- **CLI-based MCP tool access.** Rather than exposing full MCP tool schemas
  directly in the prompt — which the post notes can cost **50-70K tokens of
  overhead** — the agent gets CLI-style access to tools instead.
- **Code-mode batching.** Batches operations through code rather than one
  tool call per request/response round trip.

## 3. Impact — potential & realized

- **Realized:** **7x** growth in weekly active users and **9.4x** growth in
  weekly requests between February and August 2026; cost per 1,000 requests
  down **34%**, cost per session down **52%** from its June 2026 peak; over
  **70% of PRs** are now agent-authored, with **30,000+ daily skill runs**.
- **Potential:** a reusable multiplicative cost model for any org running a
  high-growth internal LLM-agent platform that needs to decouple cost growth
  from usage growth.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a useful operational framework, not a new technique

The multiplicative cost decomposition (users × sessions × turns × requests ×
tokens × price) is a clean, reusable mental model, and the reported numbers
are large and concrete. But most of the individual levers — model routing,
prompt caching, batching — are known cost-optimization practices applied
well at scale, rather than a new modeling or architectural idea. This is
solid platform engineering, not a research contribution.

### Similar / related work

- [**Delegating Engineering Work to Cloud-Based Agents (Flux)**](2026-08-31-doordash-flux-cloud-agents-engineering.md) (in this bank) — a
  close industry parallel: DoorDash's own cloud coding-agent platform, with
  a focus on sandboxed execution rather than cost management specifically.
- [**Sidekick's Continual Learning Loop**](2026-09-01-shopify-sidekick-continual-learning-loop.md) and
  [**Gisting**](2026-09-01-shopify-gisting-context-compression.md) (in this bank) — Shopify's cost-reduction levers for a
  different kind of high-traffic LLM agent: quality-driven RL and context
  compression, versus Uber's usage/routing-driven approach here.

### Jargon buster

- **MCP (Model Context Protocol)** — a standard protocol for exposing tools
  and data sources to an LLM agent.
- **Prompt caching** — reusing a previously processed prompt prefix on the
  model-serving side, so repeated calls don't recompute the same tokens.
- **Model routing** — dynamically choosing which model serves a given
  request based on a cost/quality tradeoff.
