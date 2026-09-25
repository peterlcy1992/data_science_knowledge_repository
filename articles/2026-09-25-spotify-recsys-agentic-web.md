---
id: spotify-recsys-agentic-web
title: "Who Are We Recommending To? Recommender Systems in the Agentic Web"
source: "arXiv / Spotify Research (RecSys 2026 Past-Present-Future track)"
url: "https://arxiv.org/abs/2609.11945"
published: "2026-07"
added: "2026-09-25"
category: llm-genai
tags: [recommender-systems, ai-agents, evaluation, metrics, agentic-web]
novelty: 4
sourced_via: "web search"
---

# Who Are We Recommending To? Recommender Systems in the Agentic Web

**Source:** [arXiv / Spotify Research (RecSys 2026 Past-Present-Future track)](https://arxiv.org/abs/2609.11945) · Published 2026-07 · Added 2026-09-25
**Category:** LLMs & Generative AI · **Tags:** `recommender-systems`, `ai-agents`, `evaluation`, `metrics`, `agentic-web`

## TL;DR

Two decades of recommender-system design implicitly assumed a human directly reads and reacts to each recommendation — but LLM-powered agents now increasingly act on a person's behalf, breaking that assumption. This position paper (highlighted by Spotify Research ahead of RecSys 2026) proposes a "delegation spectrum," based on how specifiable, verifiable, and consequential a decision is, for deciding when a recommender should target the agent versus the human, and argues this forces a rethink of optimization objectives, evaluation metrics, and even what "engagement" means.

## 1. Business context

Recommender systems have historically been built and measured around a single, stable assumption: the person seeing a ranked list of items is the one deciding what to click, buy, or play. As AI agents increasingly complete transactional tasks (routine purchases, travel booking) on a user's behalf, that assumption stops holding for a growing share of interactions — the "consumer" of a recommendation is sometimes now a delegate agent optimizing for whatever objective it was given, not a human directly weighing options. If a platform keeps optimizing and measuring recommendations as if a human is always the audience, it risks tuning its systems around signals (dwell time, scroll behavior, aesthetic appeal) that are meaningless to an agent, while missing what actually determines whether an agent picks — and a human ultimately accepts — a recommended item.

## 2. Technical details

The paper's central move is bifurcating recommendation contexts into two regimes. In "delegable" contexts — routine purchases, travel logistics, other transactional tasks where preferences are relatively easy to specify and outcomes are objectively checkable — an agent becomes the primary operational consumer of the recommendation, and the system should optimize for what makes an agent's decision correct and efficient (structured, verifiable outputs; machine-readable justifications) rather than for human-engagement proxies. In "experiential" contexts — entertainment, art, and other subjective choices — a human remains the final arbiter, with an agent at most filtering or narrowing options rather than deciding outright. The paper formalizes where a given recommendation context falls along this "delegation spectrum" using three dimensions: preference specifiability (how clearly a user's want can be articulated to an agent), outcome verifiability (whether recommendation quality can be objectively checked after the fact), and decision stakes (how consequential and reversible the choice is). Higher specifiability, verifiability, and lower stakes push a context toward agent-led delegation; low specifiability, unverifiable subjective quality, and high stakes keep it human-led. The paper then works through implications across several recommender-system design surfaces: optimization objectives that need to differ for agent- vs. human-facing recommendations, interaction protocols for dual-audience scenarios (machine-readable preference protocols like MCP/A2A alongside human-readable ones), evaluation criteria that go beyond engagement metrics to capture agent decision quality and trust/accountability, and new manipulation risks specific to an "agent attention economy" (optimizing to be picked by an agent's selection heuristic rather than to genuinely serve the underlying human).

## 3. Impact — potential & realized

As a position/perspective paper rather than a system with reported production metrics, its "impact" is conceptual and forward-looking: it gives recommender-system teams a structured vocabulary (the delegation spectrum and its three dimensions) for deciding, context by context, whether their current human-engagement-centric metrics and objectives still apply, or whether they need agent-facing counterparts. The potential impact is significant if agentic commerce and agentic browsing continue growing, since it directly targets a measurement gap this bank's own scope statement cares about — evaluation and decision-making rigor — rather than treating "agents as new users" as a detail that existing engagement metrics will handle automatically.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A genuinely useful reframing that lands squarely on a live measurement problem, even without new empirical results

This is a position paper, not a new algorithm or a production system with numbers — so it's not "field-shifting" in the sense of introducing new technique — but the delegation-spectrum framing is a clean, actionable way to reason about a problem most recommender teams are currently handling ad hoc (if at all): as agentic shopping and browsing assistants become more common, "engagement" as historically measured (scroll depth, dwell time, aesthetic appeal) stops being a reliable proxy for a growing share of traffic. Naming the three axes (specifiability, verifiability, stakes) gives a team a concrete diagnostic rather than a vague "think about agents" mandate, which is exactly the kind of measurement/evaluation-first thinking this bank tries to prioritize over pure model-architecture novelty.

### Similar / related work

- [**Tie Handling Is Part of the Evaluation Protocol: An Order-Invariance Audit for Tie-Heavy Recommender Scores**](2026-09-25-arxiv-tie-handling-recsys-evaluation.md) (in this bank) — a different but complementary evaluation-rigor concern for recommender systems: getting the *measurement mechanics* right, versus this paper's concern with getting the *measurement target* (human vs. agent) right.
- [**How Stripe Is Designing Checkout for AI Agents**](2026-09-23-stripe-webmcp-checkout-ai-agents.md) (in this bank) — a concrete production instance of exactly the "delegable, transactional" context this paper describes, redesigning an interface for an agent as the operational consumer rather than a human.
- [**An Efficient and Effective Agentic Group Shilling Attack on Recommender Systems**](2026-09-20-arxiv-agentic-group-shilling-attack-recsys.md) (in this bank) — a concrete realization of the "agent attention economy" manipulation risk this paper flags conceptually: AI agents deliberately gaming a recommender's trust/selection mechanisms.

### Jargon buster

- **Delegation spectrum** — this paper's framework for classifying a recommendation context by how much decision authority a human hands to an AI agent, ranging from fully human-led to fully agent-led.
- **Preference specifiability** — how precisely and unambiguously a user's actual preferences can be communicated to an agent (e.g., "book the cheapest direct flight under $400" is highly specifiable; "recommend a movie I'll love tonight" is not).
- **Outcome verifiability** — whether it's possible to objectively check, after the fact, whether a recommended/chosen item actually satisfied the requirement (a booked flight either meets the stated constraints or it doesn't; whether a song "hit the mood" is much harder to verify).
