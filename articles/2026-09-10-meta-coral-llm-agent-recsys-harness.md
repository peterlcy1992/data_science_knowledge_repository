---
id: meta-coral-llm-agent-recsys-harness
title: "CORAL: An LLM-Native Harness for Production Recommender Systems"
source: "Meta AI / arXiv"
url: "https://arxiv.org/abs/2609.02730"
published: "2026-09"
added: "2026-09-10"
category: personalization-recsys
tags: [ai-agents, agentic-harness, recommender-systems, production-optimization, closed-loop, in-context-learning]
novelty: 4
sourced_via: "web search"
---

# CORAL: An LLM-Native Harness for Production Recommender Systems

**Source:** [Meta AI / arXiv](https://arxiv.org/abs/2609.02730) · Published 2026-09 · Added 2026-09-10
**Category:** Personalization & Recommender Systems · **Tags:** `ai-agents`, `agentic-harness`, `recommender-systems`, `production-optimization`, `closed-loop`, `in-context-learning`

## TL;DR

Meta's CORAL (Constraint-Optimized Recommender via an Agentic Loop) puts an LLM agent in a continual closed loop directly over a live production recommender, observing operating signals each cycle, reasoning over a memory of past decisions and outcomes, and invoking a numerical optimizer that keeps changes within a fixed operating budget. A/B tests on two large-scale social platforms show it improving engagement without added serving cost on one platform, and cutting serving cost without hurting engagement on the other — with performance improving across iterative cycles.

## 1. Business context

Production recommender systems shape what billions of people see, and sustaining their performance requires continual optimization — of ranking configuration, serving parameters, and operating tradeoffs — under real budget constraints (compute, latency, cost). Doing this by hand means engineers continually watching dashboards, hypothesizing tweaks, and validating them, a labor-intensive loop that doesn't scale with the number of knobs or surfaces a large platform needs to keep tuned. CORAL is Meta's attempt to hand much of that continual tuning loop to an LLM agent operating directly against production.

## 2. Technical details

CORAL frames the problem as a **partially observed, non-stationary, constrained optimization**: the agent doesn't have full visibility into the system, the underlying platform and user behavior keep shifting, and every proposed change has to respect a fixed operating budget. Each cycle, the agent:

- **Observes** operating signals from the live recommender.
- **Reasons** over a memory of past decisions and their measured outcomes — an in-context learning loop where the policy improves without any parameter updates to the LLM itself.
- **Invokes tools**, including a numerical optimizer that keeps proposed changes within the declared operating budget rather than letting the LLM freely reconfigure the system.

The system was evaluated via A/B experiments on two large-scale social platforms (reported in the abstract as "two large-scale social platforms," without naming them), with performance reported to improve iteratively as the agent accumulates more cycles of observed outcomes. The paper was accepted at the RecSys '26 OARS (Online and Agentic Recommender Systems) workshop.

## 3. Impact — potential & realized

**Realized:** in production A/B tests, CORAL improved engagement without increasing serving cost on one platform, and reduced serving cost without degrading engagement on the other — two different operating points on the same underlying cost/engagement tradeoff, both moved favorably by the same agent framework.

**Potential:** because the optimization loop is framed generically (observe signals → reason over memory → invoke constrained tools), the approach in principle generalizes to any production system with a measurable engagement/cost tradeoff and a well-defined operating budget, not just recommenders specifically — though the paper's own evidence is limited to two recommender deployments.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A rigorous, budget-constrained entry in a fast-growing genre

Agent-driven continual optimization of production recommenders is now a genre with several strong entries in this bank (NOVA, AgentX, AutoLR), and CORAL's core idea — a closed observe/reason/act loop with a memory of past outcomes — sits within that broader trend. What distinguishes it is the explicit framing as constrained optimization under a fixed operating budget, with a dedicated numerical-optimizer tool rather than letting the LLM freely propose changes, plus genuine A/B evidence across two separate platforms showing the same framework moving the cost/engagement tradeoff in the desired direction each time. It doesn't reach a 5 because the abstract's reported detail is thinner than some peers here (no named platforms, no specific percentage lifts), leaving some of the "how much" unanswered.

### Similar / related work

- [**NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems**](2026-09-09-nova-verification-aware-agent-harness-recsys.md) (in this bank) — a closely related agent-harness approach focused on architecture-change verification rather than continual operating-parameter tuning; useful contrast on what part of the recommender an agent is allowed to touch.
- [**AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems**](2026-09-09-agentx-agent-driven-self-iteration-recsys.md) (in this bank) — a four-stage self-iterating loop covering the full research-to-deployment cycle, a broader scope than CORAL's tighter observe/optimize loop.
- [**AutoLR: Automating the Path from Research to Launch Review in Industrial Recommender Systems**](2026-09-08-netease-autolr-agentic-recsys-launch-review.md) (in this bank) — NetEase's parallel system, which deliberately restricts LLM agents to proposals while routing all state changes through deterministic controllers, a similar guardrail philosophy to CORAL's dedicated numerical-optimizer tool.

### Jargon buster

- **In-context learning (agent policy)** — the agent's behavior improves cycle-over-cycle purely by reading its own accumulated memory of past decisions and outcomes in its prompt context, without any weight updates or fine-tuning.
- **Partially observed, non-stationary, constrained optimization** — a formal way of saying: the agent can't see everything, the environment keeps changing, and every action must respect a fixed resource budget.
- **Operating budget** — a fixed limit (e.g., on serving cost or compute) within which any proposed recommender change must stay, enforced here by a dedicated numerical optimizer tool rather than left to the LLM's judgment.
- **RecSys OARS workshop** — "Online and Agentic Recommender Systems," a workshop track at the ACM RecSys conference focused specifically on this emerging genre of agent-operated recommenders.
