---
id: arxiv-ab-agent-self-evolving-strategy-iteration
title: "A/B Agent: A Self-Evolving Agent for Strategy Iteration in Industrial A/B Testing"
source: "arXiv (Kuaishou E-commerce; Jiang et al.)"
url: "https://arxiv.org/abs/2608.04625"
published: "2026-08"
added: "2026-10-01"
category: llm-genai
tags: [agents, ab-testing, recsys-strategy, tree-rag, self-evolution]
novelty: 4
sourced_via: "web search"
---

# A/B Agent: A Self-Evolving Agent for Strategy Iteration in Industrial A/B Testing

**Source:** [arXiv (Kuaishou E-commerce; Jiang et al.)](https://arxiv.org/abs/2608.04625) · Published 2026-08 · Added 2026-10-01
**Category:** llm-genai · **Tags:** `agents`, `ab-testing`, `recsys-strategy`, `tree-rag`, `self-evolution`

## TL;DR

Jiang et al. build an LLM agent that proposes and tunes recommendation strategies from a hierarchical 'experience tree' of past A/B experiments, then learns from live A/B feedback. On a short-video e-commerce platform they report a +4.829% GMV improvement with guardrail metrics held positive.

## 1. Business context

Industrial recommender teams iterate by running many A/B tests on strategies (retrieval, ranking, blending). Choosing the next strategy depends on scarce expert intuition and on knowledge scattered across hundreds of past experiments. The paper asks whether that experiment history can be turned into an automated strategy-generation loop.

## 2. Technical details

Three components: (1) Historical knowledge organisation — past strategies are arranged in a hierarchical experience tree keyed by business scenario, recommendation stage and optimisation objective; (2) Autonomous generation — multi-path Tree-RAG retrieval pulls relevant prior strategies to propose actionable new ones; (3) Self-evolution — continuous A/B feedback drives parameter tuning and knowledge updates. The authors built an industrial benchmark from 310 historical recommendation strategies across three Kuaishou E-commerce scenarios (retrieval, ranking, blending and other components).

## 3. Impact — potential & realized

Reported: in a real deployment on a short-video e-commerce platform, a +4.829% GMV improvement while guardrail metrics stayed positive, with offline and online evaluations both supportive. Details on the experiment design (duration, traffic, confidence intervals, multiple-testing handling) were not available in the abstract-level sources reviewed, so the headline lift should be read as an author-reported number.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Treats the A/B-test log itself as a training corpus for an agent, which is the measurement-aware angle the agent-for-recsys wave has mostly lacked.

An experiment archive as retrieval corpus is a neat, practical idea, but an agent that runs many A/B tests creates a selection problem: the winning strategy among many tried is biased upward (winner's curse), and the paper's headline gain needs multiple-testing and holdout-validation context before it can be trusted. Likely to be copied by other large recsys teams with deep experiment histories.

### Similar / related work

- [**AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems**](https://arxiv.org/abs/2606.26859) — closed-loop agent proposing, implementing and A/B-judging recsys changes
- [**AutoLR: Automating the Path from Research to Launch Review in Industrial Recommender Systems**](https://arxiv.org/abs/2609.04871) — multi-expert council plus exploration-exploitation selector over a limited experiment budget
- [**Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents**](https://arxiv.org/abs/2602.10226) — LLM agents optimising YouTube models with online experiments

### Jargon buster

- **Experience tree** — A hierarchy of past experiments grouped by scenario, stage and objective so an agent can retrieve similar prior strategies.
- **Tree-RAG** — Retrieval-augmented generation that walks a tree of knowledge nodes (several paths at once) instead of a flat document index.
- **Winner's curse** — When you pick the best of many noisy test results, the chosen one's measured lift overstates its true lift.
