---
id: doordash-flux-cloud-agents-engineering
title: "Delegating Engineering Work to Cloud-Based Agents (Flux)"
source: "DoorDash Engineering"
url: "https://careersatdoordash.com/blog/delegating-engineering-work-to-cloud-based-agents/"
published: "2026-08"
added: "2026-08-31"
category: llm-genai
tags: [coding-agents, cloud-agents, sandboxing, mcp, security, developer-productivity, code-review]
novelty: 4
sourced_via: "web search"
---

# Delegating Engineering Work to Cloud-Based Agents (Flux)

**Source:** [DoorDash Engineering](https://careersatdoordash.com/blog/delegating-engineering-work-to-cloud-based-agents/) · Published 2026-08 · Added 2026-08-31
**Category:** LLMs & Generative AI · **Tags:** `coding-agents`, `cloud-agents`, `sandboxing`, `mcp`

## TL;DR

DoorDash built **Flux**, an internal platform that runs coding agents in
isolated cloud sandboxes rather than on engineers' laptops, so agent work can
be delegated, audited, and scaled without exposing credentials or
infrastructure to an uncontrolled local environment. In one month, Flux
automated **130,000 engineering tasks** and now powers **25,000+ automated
code reviews weekly**, with a 95th-percentile sandbox setup time under five
seconds.

## 1. Business context

Cloud-based coding agents are attractive to most engineering organizations
but risky to turn on: an agent with laptop-level access to source code,
credentials, and internal tools is a large, hard-to-audit attack surface.
DoorDash's bet was that the blocker isn't agent capability but **execution
environment** — if agent work runs in a properly isolated, scoped, and
observable sandbox instead of a developer's machine, the security objection
mostly disappears, unlocking agents for high-volume background engineering
work (code review, task automation) that would be too risky to run locally
at scale.

## 2. Technical details

- **Firecracker microVM sandboxes.** Each agent task runs in an isolated
  cloud sandbox backed by **Firecracker micro virtual machines**, giving
  hardware-level isolation per task rather than shared-container isolation.
- **Fully provisioned per-task workspace.** Each sandbox is provisioned with
  the specific repositories, developer tools, secrets, and runtime
  dependencies the task needs — a complete, scoped engineering workspace,
  not a generic shared environment.
- **Four platform primitives.** Flux is built around **sandboxes**, an
  **MCP (Model Context Protocol) gateway** for tool access, **playbooks**
  (reusable task templates), and **invocation surfaces** (the entry points
  that trigger agent work) — designed to be modular so DoorDash can swap in
  third-party tools or build in-house where deeper security or performance
  ownership matters.
- **Setup latency SLO.** Flux holds a **p95 SLO of under 5 seconds** for the
  full end-to-end sandbox setup — from starting the microVM through cloning
  repos, installing build tools, and configuring the coding-agent harness.
- **Code-review-specific guardrails.** For the automated code-review use
  case, DoorDash added guardrails to prevent **false-clean reviews** (when
  analysis silently found issues), to **reconcile stale findings** when a PR
  changes mid-review, and to **collapse old comments** on re-review so
  authors see current state instead of an accumulating pile of outdated bot
  feedback.

## 3. Impact — potential & realized

- **Realized:** **130,000 engineering tasks** automated in a single month;
  **25,000+ automated code reviews per week**; **300+ unique playbooks**
  with **10,000+ invocations weekly**.
- **Realized (systems):** p95 sandbox cold-start under 5 seconds, making
  cloud-sandboxed agent execution fast enough for interactive-feeling
  workflows despite the added isolation.
- **Potential:** the sandbox/MCP-gateway/playbook/invocation-surface
  primitive split is presented as a reusable platform pattern for any org
  that wants agent autonomy without giving agents laptop-equivalent access.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a well-specified answer to the "agents need real access" security problem

The interesting idea isn't "use coding agents" — it's the explicit framing
that **the primitives around the agent** (isolation, tool gateway, workflow
templates, invocation surface) are the actual product, decoupled from which
underlying agent or model does the work. That's a production-pragmatic,
reusable architecture answer to a problem (agent security) most orgs are
still solving ad hoc, backed by concrete throughput and latency numbers.
It's not a 5 because Firecracker microVM isolation and MCP as a tool-access
layer are both existing building blocks — the contribution is the platform
composition and guardrail engineering, not a new isolation primitive.

### Similar / related work

- **DoorDash: Building a Production AI Code Review Agent with High Engineer
  Acceptance** (ZenML LLMOps Database case study) — the code-review agent
  specifically, whose guardrails (false-clean prevention, stale-finding
  reconciliation) this platform post also covers.
- [**In-House LLM Serving at Netflix**](2026-08-30-netflix-in-house-llm-serving.md) (in this bank) — a different kind of
  production LLM infrastructure investment (inference serving rather than
  agent sandboxing), similar in spirit as in-house platform building around
  LLM capability.
- General **Model Context Protocol (MCP)** ecosystem — the open tool-access
  standard Flux's gateway is built on for connecting agents to internal
  DoorDash tools.

### Jargon buster

- **Firecracker microVM** — a lightweight virtual machine technology
  (originally built for AWS Lambda) that gives near-container startup speed
  with much stronger, hardware-level isolation than a typical container.
- **MCP (Model Context Protocol)** — an open protocol standardizing how an
  AI agent discovers and calls external tools, used here to gate what
  internal DoorDash systems an agent can reach.
- **Playbook (in this context)** — a reusable, parameterized template for a
  specific kind of agent task (e.g., "update this config and open a PR"),
  so common workflows don't need to be re-specified from scratch each time.
- **p95 SLO** — a service-level objective stated as the 95th-percentile
  value (i.e., 95% of requests meet this bound), a standard way to commit to
  "almost always fast" rather than "fast on average."
