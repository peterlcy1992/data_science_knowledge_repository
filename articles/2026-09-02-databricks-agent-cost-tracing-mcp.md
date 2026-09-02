---
id: databricks-agent-cost-tracing-mcp
title: "How We Eliminated $1M/Year of Wasted AI Agent Spend in One Hour"
source: "Databricks Blog"
url: "https://www.databricks.com/blog/how-we-eliminated-1-million-year-wasted-ai-agent-spend-one-hour"
published: "2026-09"
added: "2026-09-02"
category: ml-infra-serving
tags: [agent-observability, mcp, opentelemetry, cost-optimization, tracing, ai-agents]
novelty: 3
sourced_via: "web search"
---

# How We Eliminated $1M/Year of Wasted AI Agent Spend in One Hour

**Source:** [Databricks Blog](https://www.databricks.com/blog/how-we-eliminated-1-million-year-wasted-ai-agent-spend-one-hour) · Published 2026-09 · Added 2026-09-02
**Category:** ML Infrastructure & Serving · **Tags:** `agent-observability`, `mcp`, `opentelemetry`, `cost-optimization`, `tracing`

## TL;DR

Databricks engineers used trace data from its Unity Gateway (OpenTelemetry traces of every MCP tool call) plus a natural-language query interface to find seven silent bugs in tool servers that were causing AI agents to burn tokens and developer time on failing retries — an estimated $1.2M/year in waste, found and fixed within an hour of looking.

## 1. Business context

AI agents that call external tools via the Model Context Protocol (MCP) don't fail loudly when a tool call goes wrong — they retry, work around the error, or silently give a degraded answer, so the extra tokens and latency show up on a dashboard only as generic "usage growth," not as an identifiable defect. That makes agent cost bloat easy to miss: nobody is paged when an agent quietly retries a malformed tool call ten times before giving up. Databricks wanted to know whether trace data it was already collecting could surface these hidden failures without a dedicated cost-audit project.

## 2. Technical details

- **Unity Gateway tracing.** Every MCP tool invocation automatically emits an OpenTelemetry trace capturing the tool name, arguments, errors, token counts, latency, and session ID — instrumentation that was already running, not built specifically for this investigation.
- **Genie One as the query interface.** Rather than writing SQL against the trace tables, the team used Genie One's natural-language interface to ask questions of the trace data directly, which is what let the investigation move from "we suspect waste" to "here are seven named bugs" in about an hour.
- **Failure pattern.** The costliest failures came from tools that accepted only rigid input formats while the calling model reasonably inferred more flexible, equally valid alternatives — a Jira integration bug caused 535 failures/day, and a Google Drive tool bug caused failures on 49.6% of its calls.

## 3. Impact — potential & realized

- **Realized:** seven tool-server bugs identified and fixed, an estimated **$499K/year in wasted tokens**, roughly **12,000 engineering-hours/year** lost to agent wait time, for a combined **~$1.2M/year** in estimated waste — found and resolved within one hour of starting to look.
- **Potential:** a template for treating existing agent observability data (traces already being collected for other reasons) as a first-class cost-debugging surface, rather than building bespoke cost-monitoring tooling — and for using an LLM-driven query interface to make that data actually get looked at.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a compelling case study in a discipline more teams should already be practicing

There's no new technique here — OpenTelemetry tracing and natural-language BI interfaces both predate this post. The value is entirely in the demonstration: agent cost waste hides in silent retries that standard usage dashboards can't distinguish from legitimate growth, and the fix was cheap once someone actually queried the trace data. That's a useful wake-up call for any team running MCP-based agents at scale, but it's an application of existing tools to a real problem rather than a new idea.

### Similar / related work

- [**Sidekick's Continual Learning Loop**](2026-09-01-shopify-sidekick-continual-learning-loop.md) (in this bank) — a different, deeper lever on agent serving cost (RL-tuned model quality rather than tool-call bug fixing), but the same underlying concern of agent cost bloat at scale.
- [**Gisting: Compressing LLM Agent Context to Increase Throughput and Cut Cost**](2026-09-01-shopify-gisting-context-compression.md) (in this bank) — another agent cost-reduction lever, there attacking token volume directly via context compression rather than eliminating failed calls.
- [**Running a Software Factory Efficiently at Uber Scale**](2026-08-31-uber-software-factory-efficient-agent-cost.md) (in this bank) — a companion piece on managing coding-agent costs, there via model routing and prompt caching rather than tracing-driven bug hunts.

### Jargon buster

- **MCP (Model Context Protocol)** — a standard protocol that lets an LLM agent call external tools (e.g., Jira, Google Drive) in a structured way.
- **OpenTelemetry trace** — a structured record of an operation (here, one tool call) capturing timing, inputs, outputs, and errors, usable for debugging and analytics.
- **Genie One** — Databricks' natural-language query interface, letting users ask questions of tabular data without writing SQL.
