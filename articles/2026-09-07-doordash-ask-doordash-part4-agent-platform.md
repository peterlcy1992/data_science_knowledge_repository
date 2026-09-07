---
id: doordash-ask-doordash-part4-agent-platform
title: "Building Ask DoorDash (Part 4): A Platform for Building and Evolving Agents"
source: "DoorDash Engineering"
url: "https://careersatdoordash.com/blog/building-ask-doordash-part-four-a-platform-for-building_and_evolving_agents/"
published: "2026-07"
added: "2026-09-07"
category: llm-genai
tags: [ai-agents, agent-platform, conversational-commerce, latency, evaluation, gateway]
novelty: 4
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Building Ask DoorDash (Part 4): A Platform for Building and Evolving Agents

**Source:** [DoorDash Engineering](https://careersatdoordash.com/blog/building-ask-doordash-part-four-a-platform-for-building_and_evolving_agents/) · Published 2026-07 · Added 2026-09-07
**Category:** LLMs & Generative AI · **Tags:** `ai-agents`, `agent-platform`, `conversational-commerce`, `latency`, `evaluation`, `gateway`

## TL;DR

DoorDash built a shared platform underneath Ask DoorDash that separates domain-specific agent behavior (Restaurant, Grocery, Reservations) from common execution and production infrastructure, so a new domain agent takes about a week to add instead of the roughly two months the first two domains took — and model upgrades can be evaluated and shipped within a week of release.

## 1. Business context

Ask DoorDash launched with Restaurant and Grocery domain agents in roughly two months, but building each domain agent from scratch meant re-solving the same execution, evaluation, and infrastructure problems every time a new domain (or a new LLM) needed to be supported. The team explicitly judged the platform on two practical outcomes: how fast new features and domains could be added, and how fast quality, cost, and latency improvements (like a new model release) could be evaluated and released — both proxies for whether the underlying platform, not just the individual agents, was actually paying off.

## 2. Technical details

The core architectural move is separating domain-specific agent behavior from shared execution and production capabilities used across every domain agent. A Gateway component handles streaming communication between agents and clients, decoupling the domain logic from the transport and session-management concerns. New domains plug into this shared substrate rather than reimplementing streaming, evaluation harnesses, and deployment tooling, which is what let the third domain (Reservations) ship roughly 10x faster than the first two. The same shared evaluation and deployment path is also what let the team adopt new underlying LLMs quickly: within a week of a new model's release, they evaluated it against production quality bars and deployed it.

## 3. Impact — potential & realized

Realized: Ask DoorDash has handled more than two million conversations since launch. Adding the Reservations domain agent took about one week versus roughly two months for the initial Restaurant/Grocery build — a ~10x speedup attributed to the shared platform. Two successive LLM upgrades, evaluated and shipped within about a week of release each, cut p50 turn latency by 35% and then a further 40%, with no drop in quality scores. The potential is the platform pattern itself: once the shared execution/evaluation layer exists, both "add a new business domain" and "adopt a new model" become platform operations rather than one-off engineering projects, which should keep compounding as DoorDash adds more agent surfaces.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — The clearest quantified case yet for "build the platform, not just the agent"

Plenty of teams claim a shared agent platform speeds up adding new domains; DoorDash's own before/after numbers (two months vs. one week) are an unusually concrete, self-reported data point for that claim, and the latency wins from fast model-upgrade adoption (35% then 40% p50 turn-latency cuts within a week of each release) are a genuinely strong result for an evaluation/deployment pipeline. The architecture itself (shared gateway + execution layer, pluggable domain logic) is a sound but not conceptually new pattern — the novelty here is mostly in how cleanly the write-up ties platform investment to measured velocity and latency outcomes.

### Similar / related work

- [**Building Ask DoorDash (Part 5): A Grounded Interface For Shopping Agents**](2026-09-06-doordash-ask-doordash-grounded-shopping-interface.md) (in this bank) — the next installment in the same series, covering the UI-generation layer built on top of this platform.
- [**Meet Stripe's Knowledge AI Platform**](2026-09-07-stripe-kai-knowledge-ai-platform.md) (in this bank) — a comparable shared-platform-plus-pluggable-agents architecture, aimed at internal employees rather than customers.
- [**Delegating Engineering Work to Cloud-Based Agents (Flux)**](2026-08-31-doordash-flux-cloud-agents-engineering.md) (in this bank) — the same company's platform approach to a different agent surface (internal engineering work vs. customer-facing conversations).

### Jargon buster

- **p50 turn latency** — the median (50th-percentile) time it takes the agent to respond to one turn of a conversation; a "turn" is one round-trip of user message to agent response.
- **Gateway (agent platform)** — a shared component that handles the mechanics of streaming a conversation between client and agent, so individual domain agents don't each need their own connection-handling code.
