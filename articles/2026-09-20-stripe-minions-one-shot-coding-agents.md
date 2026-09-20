---
id: stripe-minions-one-shot-coding-agents
title: "Minions: Stripe's One-Shot End-to-End Coding Agents"
source: "Stripe.dev"
url: "https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents"
published: "2026-02"
added: "2026-09-20"
category: llm-genai
tags: [agentic-coding, coding-agents, mcp, developer-productivity, legacy-codebase]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Minions: Stripe's One-Shot End-to-End Coding Agents

**Source:** [Stripe.dev](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) · Published 2026-02 · Added 2026-09-20
**Category:** LLMs & Generative AI · **Tags:** `agentic-coding`, `coding-agents`, `mcp`, `developer-productivity`, `legacy-codebase`

## TL;DR

Stripe built "Minions" — fully unattended, one-shot coding agents that take a request from Slack (or a CLI, web UI, or internal tool) and return a CI-passing pull request with zero human-written code, now merging over 1,000 minion-authored PRs per week. What makes this a harder problem than typical agentic-coding demos is the target: hundreds of millions of lines of a mature, high-stakes Ruby-and-Sorbet payments codebase with homegrown libraries LLMs have never seen, not a greenfield project.

## 1. Business context

Most agentic-coding success stories showcase building something new from scratch, where an LLM's general knowledge of popular frameworks carries most of the weight. Stripe's problem is the opposite: a codebase of hundreds of millions of lines, predominantly Ruby with Sorbet static typing (an unusual combination LLMs have comparatively little training exposure to), full of homegrown internal libraries that are unique to Stripe and therefore natively unfamiliar to any foundation model. And the stakes are real — this is payment-processing infrastructure under strict regulatory and compliance requirements, where an agent that "mostly" understands the codebase isn't good enough. Standard agentic coding tools, tuned for iterating on unfamiliar-but-conventional stacks, struggle to safely modify code this mature and this idiosyncratic.

## 2. Technical details

**One-shot, unattended design.** A minion's workflow starts with a request (most often a Slack message) and ends with a pull request that is CI-passing and ready for human review — with no human-authored code in between, and no mid-task human approval gate. Entry points include Slack (the dominant path), a CLI, a web interface, and internal applications like the docs platform, feature-flag system, and ticketing tool.

**Isolated, fast execution environments.** Minions run in isolated developer environments ("devboxes") that spin up in about 10 seconds with Stripe code and services pre-loaded, which is what makes running many minions in parallel practical without risking production access or interference between sessions.

**Agent core.** The agent loop is a fork of Block's open-source **Goose** project, customized with what Stripe calls "opinionated" orchestration — deterministic steps (git operations, linting, running tests) interleaved with the agent's own creative reasoning, rather than leaving those steps entirely up to model judgment.

**Context via MCP.** Minions pull context from distributed internal sources — documentation, ticket details, build statuses, and code intelligence via Sourcegraph — through the Model Context Protocol. Stripe built a central internal MCP server, **Toolshed**, that exposes more than 400 MCP tools spanning internal systems and SaaS platforms, so a minion (or any other internal agent) gets a single, standardized way to reach all of them.

**Conditional rules, not blanket rules.** Rather than one global set of coding rules, Stripe applies almost all agent guidance conditionally based on the subdirectory being touched — letting different parts of a codebase this large carry different conventions without conflicting instructions.

**Layered, budgeted validation.** Feedback runs in stages: a local heuristic pass (under 5 seconds) selectively runs lints on git push; CI selectively runs relevant tests out of a suite of 3+ million tests and auto-applies fixes where available; and an iterative-repair loop lets a minion attempt fixes on test failures, but is capped at **at most two** CI rounds — a deliberate speed-versus-completeness tradeoff rather than letting an agent loop indefinitely.

## 3. Impact — potential & realized

**Realized:** over 1,000 pull requests merged weekly that are entirely minion-produced, with engineers routinely running multiple minions in parallel — particularly valuable during on-call rotations, where several small, independent issues need attention at once and attention (not compute) is the constraint.

**Potential:** the harder-won lessons here — conditional rules scoped to subdirectories, a capped iterative-repair budget, and a central MCP tool server serving hundreds of internal tools uniformly — are the parts most transferable to any large, old, idiosyncratic codebase, arguably more so than the one-shot agent pattern itself, which depends on the codebase being tame enough for zero-human-intervention changes to be safe.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a strong production proof point for a known pattern, in an unusually hostile environment

Fully unattended, one-shot coding agents aren't a new idea, and forking an existing open-source agent loop (Goose) rather than building one from scratch is a pragmatic, not novel, choice. What earns this a solid-not-spectacular score is the environment it's proven in: a huge, old, Ruby+Sorbet, homegrown-library-heavy payments codebase that is close to a worst case for LLM familiarity, plus concrete engineering choices (subdirectory-scoped rules, a hard two-round CI-repair cap, a 400-tool central MCP gateway) that read as genuinely earned from production pain rather than generic best practice.

### Similar / related work

- [**Casper: Snap's Fleet of Friendly AI Teammates**](2026-09-20-snap-casper-ai-teammates.md) (in this bank) — the clearest contrast: Casper builds human approval gates into the plan/implement loop, while Minions are deliberately one-shot and unattended end to end; both converge on MCP-based tool gateways (Snap's "MCP Gateway" vs. Stripe's "Toolshed") as the way to give agents uniform access to internal systems.
- [**Coding Had a Concurrency Problem: How Mux Helped Solve It**](2026-09-11-coinbase-mux-multi-agent-coding-tool.md) (in this bank) — Coinbase's answer to running many agent sessions concurrently without collisions, the same "fleet of agents" scaling problem Minions solves via fast (~10s) isolated devboxes.
- [**Delegating Engineering Work to Cloud-Based Agents (Flux)**](2026-08-31-doordash-flux-cloud-agents-engineering.md) (in this bank) — DoorDash's cloud-agent delegation platform, another company-specific take on turning a chat request into a reviewable PR.

### Jargon buster

- **Sorbet** — a static type checker for Ruby; Stripe's large Ruby codebase uses it, which makes the stack less common in LLM training data than plain Ruby or more mainstream typed languages.
- **Devbox** — a fast-provisioning, isolated development environment pre-loaded with a codebase's code and services, used here so a minion can run in seconds without needing a shared or production environment.
- **Goose** — an open-source agent framework from Block that Stripe forked and customized as the execution loop underneath Minions.
- **MCP (Model Context Protocol)** — a standardized way for an LLM agent to call out to external tools and data sources; Stripe's internal implementation ("Toolshed") exposes 400+ internal tools through it.
- **One-shot agent** — an agent design that takes one instruction and works end-to-end to a finished result (here, a mergeable PR) without pausing for human input partway through, as opposed to an interactive or approval-gated agent.
