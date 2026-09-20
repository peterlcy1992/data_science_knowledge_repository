---
id: snap-casper-ai-teammates
title: "Casper: Snap's Fleet of Friendly AI Teammates"
source: "Snap Engineering"
url: "https://eng.snap.com/casper"
published: "2026-09"
added: "2026-09-20"
category: llm-genai
tags: [agentic-coding, coding-agents, identity-and-permissions, developer-productivity, mcp]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Casper: Snap's Fleet of Friendly AI Teammates

**Source:** [Snap Engineering](https://eng.snap.com/casper) · Published 2026-09 · Added 2026-09-20
**Category:** LLMs & Generative AI · **Tags:** `agentic-coding`, `coding-agents`, `identity-and-permissions`, `developer-productivity`, `mcp`

## TL;DR

Snap built Casper, a fleet of always-on, remotely-triggered AI coding agents that engineers summon from Slack to handle repetitive engineering work — flaky tests, dependency bumps, lint fixes, on-call triage — and that now produce thousands of mergeable pull requests a week. The most distinctive part isn't the coding loop itself but the identity and permissions model underneath it: agent actions never use raw credentials, and the triggering engineer's identity travels through every downstream tool call so existing access controls still apply.

## 1. Business context

Snap's codebase spans thousands of interconnected services, and engineer attention — not compute — was the bottleneck on the kind of work that's necessary but not interesting: fixing a flaky test, bumping a dependency, cleaning up a lint violation, building a small on-call helper. Snap's answer was to build a system that could pick up that class of work end-to-end (plan the change, implement it, validate it, open a PR) without an engineer babysitting each step, while still fitting inside the company's existing security and code-review model rather than creating a new, less-trusted path into production code.

## 2. Technical details

**Agent lifecycle.** A Casper agent spins up in an isolated sandbox under its own agent identity, gathers context from Slack threads, Jira tickets, linked documents, and repository-level guidance, then plans and implements a change with human approval gates along the way. It runs the team's own validation (tests, builds, linters), iterates on failures, and produces a PR that follows team conventions. Before a human ever sees it, the PR is run through **CodePal**, Snap's separate automated code-review agent (part 1 of the same three-part series), and Casper agents also lean on **Code Search** (part 2) for cross-repository context discovery.

**Identity and security model.** This is the architecturally interesting part: agent processes are never handed raw credentials. Instead, a "trusted controller" exposes a narrow set of operations — checkout, code search, push, PR creation — and authorizes each call against the session's identity rather than a shared service credential. Snap describes this as "identity travels the whole chain": a user's authentication flows from Slack or the internal Agents Portal into the sandboxed session, and every downstream tool call carries that user's identity forward, so the agent can never do more than the triggering engineer is already permitted to do.

**Access patterns.** Engineers reach Casper three ways: direct Slack messages or @-mentions (the most common path, with collaborators able to join an in-progress session), the web-based Agents Portal for viewing session history and live progress, and event/schedule triggers that let teams configure agents to fire on Slack channel activity or on a cron-like schedule.

**Customization and integration.** Teams can specialize an agent via a template: a custom system prompt encoding team conventions, a restricted tool set, a custom runtime container image, model choice and cost attribution, and access boundaries (which Slack channels, which schedules, manual-only). An internal "MCP Gateway" gives every Casper agent standardized access to Snap's internal systems (Jira, A/B testing platforms, data query tools) via the Model Context Protocol, so adding a new capability doesn't require wiring it into every agent individually. Sessions are also durable across compute restarts, so an engineer can step away mid-task and reattach later rather than losing state.

## 3. Impact — potential & realized

**Realized:** Casper is now producing thousands of mergeable PRs per week across Snap's engineering org, with hundreds of custom Casper agents created by teams since general availability. Snap specifically calls out teams building specialized on-call agents in hours that would previously have taken weeks to stand up as a bespoke tool.

**Potential:** the identity-propagation pattern is arguably more transferable than the coding-agent use case itself — any org deploying fleets of autonomous agents against internal systems needs an answer to "what can this agent actually do, and as whom," and Snap's answer (no standing agent credentials, only forwarded user identity through a narrow trusted controller) is a reusable blueprint for agent security independent of what the agents are coding.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — the coding loop is familiar; the identity model is the real contribution

Plan → implement → validate → PR is now a well-trodden pattern (Coinbase's Mux, DoorDash's Flux, and Stripe's Minions are all variations on it), so Casper's core loop isn't new. What stands out is the explicit "identity travels the whole chain" design: rather than granting agents their own service-account-style credentials (a common and risky shortcut), every action is authorized against the human who triggered it, propagated through a trusted controller. That's a production-first security answer to a problem most agentic-coding write-ups gloss over, which is why this scores above a pure recap despite the familiar high-level workflow.

### Similar / related work

- [**Coding Had a Concurrency Problem: How Mux Helped Solve It**](2026-09-11-coinbase-mux-multi-agent-coding-tool.md) (in this bank) — Coinbase's infrastructure for running many concurrent coding-agent sessions without collisions; a complementary scaling problem to Casper's identity/permissions problem, both about building the surrounding platform for fleets of agents rather than just the agent loop.
- [**Delegating Engineering Work to Cloud-Based Agents (Flux)**](2026-08-31-doordash-flux-cloud-agents-engineering.md) (in this bank) — DoorDash's cloud-agent platform for delegating engineering tasks, the closest direct analog to Casper's Slack-triggered, sandboxed agent model.
- [**Minions: Stripe's One-Shot End-to-End Coding Agents**](2026-09-20-stripe-minions-one-shot-coding-agents.md) (in this bank) — a contrasting design point: Stripe's minions are fully unattended one-shot agents (no mid-task human approval gates), whereas Casper builds in human approval checkpoints during planning and implementation.

### Jargon buster

- **Sandbox** — an isolated compute environment where an agent can run code, tests, and builds without touching production systems or other engineers' work.
- **Trusted controller** — a narrow, audited service that exposes only specific operations (like "push to this branch") and checks the caller's identity before executing them, rather than letting callers run arbitrary privileged commands directly.
- **MCP (Model Context Protocol)** — an open protocol for connecting an LLM-based agent to external tools and data sources through a standardized interface, so new integrations don't need bespoke, per-agent glue code.
- **Agent identity propagation** — the practice of carrying a human user's authentication/authorization context through every layer of an automated system, so an agent acting "on behalf of" that user can never exceed what the user themselves is allowed to do.
