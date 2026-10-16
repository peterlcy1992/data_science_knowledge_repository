---
id: arxiv-mle-agents-production-search-ranking
title: "MLE Agents: Autonomous ML Engineering in Production Recommendation Systems"
source: "NeurIPS 2026 Workshop on Autonomous ML Research (Li, Liang & Guru Raj)"
url: "https://neurips.cc/virtual/2026/157618"
published: "2026-10"
added: "2026-10-16"
category: search-ranking
tags: [agents, auto-ml, search-ranking, online-ab-test]
novelty: 3
sourced_via: "web search"
---

# MLE Agents: Autonomous ML Engineering in Production Recommendation Systems

**Source:** [NeurIPS 2026 Workshop on Autonomous ML Research (Li, Liang & Guru Raj)](https://neurips.cc/virtual/2026/157618) · Published 2026-10 · Added 2026-10-16
**Category:** search-ranking · **Tags:** `agents`, `auto-ml`, `search-ranking`, `online-ab-test`

## TL;DR

Human-on-the-loop ML-engineer agents propose, implement, train and evaluate changes to a production search ranker serving over 1B requests/day. In one campaign 325 of 1,097 candidates were accepted, the win rate rose from 15.6% to 29.6%, and the best model lifted CTR 0.70% and search volume 0.23% in a ~10M-user A/B test.

## 1. Business context

Iterating on a production ranker is slow: experiments take hours, offline metrics do not always predict online impact, and returns diminish after early wins. The paper tests whether agents can take over the propose-implement-train-evaluate loop while engineers keep objective design, search direction, review and deployment.

## 2. Technical details

Agents run parallel training runs, use an objective calibrated to online impact, and rely on context engineering: a 'what didn't work' blocklist, strict output formats and an anti-staleness rule. The authors stress that the harness around the model matters as much as the model. Company not stated on the page; abstract-level read.

## 3. Impact — potential & realized

Realized (reported): 1,097 completed candidate experiments, 325 accepted; candidate win rate 15.6% to 29.6%; online A/B on ~10M users with CTR +0.70% and search volume +0.23% from the best model. Some wins were architectural changes the team had not considered. Significance levels and control details are not given.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty 3/5 - a credible production datapoint for agentic ML iteration, notable for the experiment-throughput framing; light on statistical detail.

The interesting DS angle is the experiment funnel: 30% acceptance of 1,097 trials raises multiple-testing and winner's-curse questions the abstract does not address. Worth watching for how gains hold up on re-test.

### Similar / related work

- [**WeGR: Unified Generative Retrieval for Industrial Search Systems in WeChat**](2026-10-15-arxiv-wegr-generative-retrieval-wechat-search.md) (in this bank) — search ranking with online A/B evidence
- [A Survey on LLM-powered Agents for Recommender Systems](https://arxiv.org/abs/2502.10050) — agentic recsys landscape

### Jargon buster

- **Human-on-the-loop** — Humans supervise and approve agent output rather than performing each step.
- **Context engineering** — Designing what information, constraints and history an LLM agent sees on each step.
- **Win rate (candidates)** — Share of attempted experiments that beat the baseline and are accepted.
