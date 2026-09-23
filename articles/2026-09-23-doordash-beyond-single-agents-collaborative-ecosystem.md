---
id: doordash-beyond-single-agents-collaborative-ecosystem
title: "Beyond Single Agents: How DoorDash Is Building a Collaborative AI Ecosystem"
source: "DoorDash Engineering Blog"
url: "https://careersatdoordash.com/blog/beyond-single-agents-doordash-building-collaborative-ai-ecosystem/"
published: "2026-09"
added: "2026-09-23"
category: ml-infra-serving
tags: [agents, multi-agent, langgraph, mcp, agent-to-agent, platform]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Beyond Single Agents: How DoorDash Is Building a Collaborative AI Ecosystem

**Source:** [DoorDash Engineering Blog](https://careersatdoordash.com/blog/beyond-single-agents-doordash-building-collaborative-ai-ecosystem/) · Published 2026-09 · Added 2026-09-23
**Category:** ML Infrastructure & Serving · **Tags:** `agents`, `multi-agent`, `langgraph`, `mcp`, `agent-to-agent`, `platform`

## TL;DR

DoorDash lays out a four-stage maturity model for its internal AI agent platform — deterministic workflows, single ReAct agents, hierarchical "deep agents," and peer-to-peer "agent swarms" — built on LangGraph, MCP for tool access, and the Agent-to-Agent protocol for inter-agent communication, surfaced through a conversational web UI, Slack, and a Cursor IDE integration.

## 1. Business context

DoorDash had already shipped several single-purpose agents (Vera for data questions, Ask DoorDash for customer support, various coding agents), but single agents hit a ceiling on complex, multi-step requests that need decomposition, delegation, and shared state across sub-tasks. Rather than building one increasingly complex monolithic agent per use case, DoorDash frames the problem as an architecture-maturity ladder and invests in the platform primitives (shared memory, standardized protocols) that let specialized agents compose into larger systems.

## 2. Technical details

The four stages DoorDash describes:

1. **Workflows** — deterministic, repeatable automation with no dynamic reasoning.
2. **Single agents (ReAct)** — one agent reasoning and acting in a loop, sufficient for tasks that don't need decomposition.
3. **Deep agents** — a hierarchical architecture where a manager agent decomposes a complex request into subtasks, a progress agent tracks completion and dependencies, and specialist agents execute individual actions. A persistent shared workspace lets one agent's output (a dataset, a piece of code) become another agent's input, functioning as more than a virtual file system.
4. **Agent swarms** — the most advanced stage DoorDash is exploring: peer agents collaborating asynchronously with no centralized controller, where no single agent holds the complete picture but coherent outcomes emerge from local interactions.

The technical substrate: LangGraph for the underlying computational graphs, Model Context Protocol (MCP) for standardized tool access (the same protocol used in DoorDash's feature-flag cleanup agents), and the Agent-to-Agent (A2A) protocol for inter-agent communication. Access surfaces span a conversational web UI acting as a marketplace for discovering specialized agents, direct Slack integration, and a Cursor IDE integration for engineering workflows.

## 3. Impact — potential & realized

The post is framed as an architectural account rather than a single-metric case study, so realized impact is qualitative: it explains the platform choices behind DoorDash's growing family of production agents (Vera, Ask DoorDash, the feature-flag cleanup system) rather than reporting a standalone before/after number. The potential impact is platform leverage — by standardizing on MCP for tools and A2A for agent communication, DoorDash positions each new specialized agent to plug into the same shared-memory and orchestration substrate instead of being built from scratch, which is the difference between one-off agent projects and a compounding agent platform.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clear maturity model, still early on the most novel stage

The workflows → single agent → deep agent → swarm progression is a genuinely useful framing for thinking about where an org's agent investment sits, and DoorDash's willingness to name the protocols (LangGraph, MCP, A2A) makes this more concrete than most "we're building agents" posts. The swarm stage — decentralized, no single agent with the full picture — is the most novel and least proven part of the story; it's presented as exploratory, not yet shipped at the reliability level of the other three stages. Worth revisiting once DoorDash publishes swarm-stage production results.

### Similar / related work

- [**Automating Feature-Flag Cleanup at Scale with a Multi-Agent LLM System**](2026-09-23-doordash-feature-flag-cleanup-multi-agent-llm.md) (in this bank) — a concrete "deep agent" instance (orchestrator + parallel specialist workers) built on the same MCP substrate this platform post describes.
- [**Inside Vera, DoorDash's Data Agent**](2026-09-18-doordash-vera-data-agent.md) (in this bank) — one of the specialized single/deep agents that plugs into the collaborative ecosystem this post describes.
- [**Xirp: A Vendor-Neutral Agentic Development Environment**](2026-09-23-spotify-xirp-agentic-dev-environment.md) (in this bank) — Spotify's parallel infrastructure investment for managing many concurrent agent sessions, a different layer of the same "agents at organizational scale" stack.

### Jargon buster

- **ReAct agent** — an agent architecture that interleaves reasoning ("thinking out loud") with acting (calling tools), looping until it reaches an answer — the standard baseline pattern for a single LLM agent.
- **Agent-to-Agent (A2A) protocol** — an open standard for how separate AI agents discover each other's capabilities and exchange messages, distinct from MCP (which standardizes agent-to-tool, not agent-to-agent, communication).
- **Agent swarm** — a decentralized set of agents that coordinate through local interactions rather than a central controller, analogous to swarm intelligence in biological systems (ant colonies, flocking) applied to AI agents.
