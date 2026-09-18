---
id: grab-agent-platform-llm-kit-part-1
title: "Agent Platform (Part 1): How We Help Grab Build and Run AI Agents at Scale"
source: "Grab Engineering Blog"
url: "https://engineering.grab.com/how-grab-builds-and-runs-ai-agents-at-scale"
published: "2026-07"
added: "2026-09-18"
category: ml-infra-serving
tags: [agent-platform, mcp, llm-gateway, observability, internal-tooling, langgraph]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Agent Platform (Part 1): How We Help Grab Build and Run AI Agents at Scale

**Source:** [Grab Engineering Blog](https://engineering.grab.com/how-grab-builds-and-runs-ai-agents-at-scale) · Published 2026-07 · Added 2026-09-18
**Category:** ML Infrastructure & Serving · **Tags:** `agent-platform`, `mcp`, `llm-gateway`, `observability`, `internal-tooling`, `langgraph`

## TL;DR

Grab built LLM-Kit, an internal framework that standardizes the "everything around the agent" work — auth, model access, observability, config — so teams across Grab's 500+ services don't each reinvent it. Day-one setup for a new agent dropped from about two weeks to roughly one hour, and the framework now underpins 50+ registered MCP servers and a company-wide LLM gateway handling billions of tokens a month.

## 1. Business context

As AI agents moved from prototypes to production across Grab's engineering organization, the team's core realization was that "the hard part of building an agent was not the agent itself, but everything around it": evaluation beyond informal manual testing, switching between model providers without rewriting application code, fragmented observability across agent workflows and tool calls, and the routine production plumbing (authentication, secrets, configuration) that every team was independently re-solving. Left unaddressed, that overhead meant each of Grab's 500+ services building an agent would pay the same integration tax from scratch.

## 2. Technical details

LLM-Kit is designed as a reusable framework rather than a restrictive platform — teams adopt pieces of it rather than being forced onto one opinionated stack. It provides template-based scaffolding: a FastAPI service pre-wired with production essentials (auth, logging, health checks) so a new agent starts with those solved. All LLM calls route through the **GrabGPT Gateway**, giving centralized control over which model/provider backs a given agent without requiring application-code changes when that changes. Built-in observability uses OpenTelemetry instrumentation that auto-correlates logs and traces across FastAPI, HTTP calls, LangChain, and MCP components, so a single trace can be followed across the whole agent call chain. Configuration is managed through environment-specific INI files with HashiCorp Vault secret interpolation, keeping secrets out of code and config files uniform across environments.

On the agent-architecture side, LLM-Kit supports single-agent ReAct loops implemented in LangGraph, with tool discovery happening through remote MCP servers rather than hardcoded tool lists — 30-second per-step timeouts and built-in retry policies are part of the default template. Inter-service connectivity uses gRPC alongside FastAPI, with auto-discovery via Istio/Consul and health-checking, and generated, typed Protocol Buffer SDKs so services never hardcode each other's addresses. Evaluation isn't bolted on separately either: built-in evaluation endpoints (ROUGE, BLEU, LLM-as-judge) ship as part of the standard templates.

## 3. Impact — potential & realized

**Realized:** over 500 services now build on the internal agent framework, with 50+ MCP servers registered on the remote MCP framework and a single LLM gateway handling billions of tokens per month across the company. Day-one setup time for a new agent dropped from roughly two weeks to about one hour.

**Potential:** by centralizing model access, observability, and evaluation into reusable framework pieces rather than a top-down platform mandate, Grab has set up a structure where new teams building agents inherit production-grade infrastructure by default — likely to matter more as the number of internal agents (and the surface area for something to go wrong across them) keeps growing.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid internal-platform engineering, following an emerging industry pattern rather than inventing one

"Standardize the scaffolding around agents so teams stop reinventing observability and model access" is a pattern showing up across large tech companies building internal agent platforms this year. What Grab adds isn't a new idea so much as a concretely reported, large-scale execution of it — the 2-weeks-to-1-hour onboarding number and the 500-service adoption figure are the kind of evidence that's often missing from similar announcements elsewhere.

### Similar / related work

- [**How AI is Transforming Analytics at Grab**](2026-09-11-grab-agentic-analytics-autonomy-ladder.md) (in this bank) — a sibling Grab effort applying agentic AI to analytics workflows, likely built atop the same underlying platform investment.
- [**Building an MCP Ecosystem at Pinterest**](2026-09-10-pinterest-mcp-ecosystem-ai-agents.md) (in this bank) — a similar internal MCP-based tooling ecosystem at a different company, with more emphasis on security/governance of tool access.
- [**Solving the Identity Crisis for AI Agents**](2026-09-12-uber-agent-identity-crisis-trust-platform.md) (in this bank) — Uber's parallel infrastructure investment in agent trust/identity, a complementary concern to the plumbing LLM-Kit standardizes.

### Jargon buster

- **ReAct loop** — an agent pattern that interleaves "reason" (think about what to do next) and "act" (call a tool) steps, repeating until the task is done.
- **LLM gateway** — a centralized service that all of a company's LLM calls route through, giving one place to manage provider choice, rate limits, cost tracking, and logging.
- **OpenTelemetry** — an open standard for collecting traces, logs, and metrics from distributed systems, letting different tools and services share a common observability format.
