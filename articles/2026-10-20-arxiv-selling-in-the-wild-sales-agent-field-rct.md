---
id: arxiv-selling-in-the-wild-sales-agent-field-rct
title: "Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations"
source: "arXiv cs.IR (Tannenbaum)"
url: "https://arxiv.org/abs/2610.25461"
published: "2026-10"
added: "2026-10-20"
category: llm-genai
tags: [field-experiment, rct, non-inferiority, sales-agent, guardrails]
novelty: 4
sourced_via: "web search"
---

# Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations

**Source:** [arXiv cs.IR (Tannenbaum)](https://arxiv.org/abs/2610.25461) · Published 2026-10 · Added 2026-10-20
**Category:** llm-genai · **Tags:** `field-experiment`, `rct`, `non-inferiority`, `sales-agent`, `guardrails`

## TL;DR

A sales agent (Javo) fine-tuned on 4.6M consented commercial conversations was tested in a randomized field trial across 100 live websites and about 14.8M visitors, with revenue lift versus no agent, conversion versus a frontier-model agent, and a prespecified non-inferiority test against human associates.

## 1. Business context

Conversational sales agents are widely deployed, but evidence is mostly benchmark scores or vendor claims. The paper asks the commercial question directly: does a purpose-trained agent outsell no agent, a general frontier-model agent in the same interface, and the site's own human staff?

## 2. Technical details

Four studies. (1) Benchmarks: Javo scored on SalesLLM and SmartSalesBench against 10 frontier and open-weight models. (2) RCT: 100 live websites across 14 industries, 1 May to 30 September 2026; about 14.8M visitors randomized to no agent, Javo, or a frontier-model agent using the same interface, catalog tools and guardrails. (3) Model effect: Javo arm versus frontier-agent arm, isolating the model. (4) Human comparison on 20 sites with staffed live chat, tested for non-inferiority against a prespecified -7% margin. Guardrails (return rates, unsupported product claims, complaints) were prespecified. Method detail comes from the abstract only.

## 3. Impact — potential & realized

Reported: revenue per visitor +10.0% versus no agent (95% CI +5.1 to +14.9); engaged-visitor conversion +21.6% versus the frontier-model agent (95% CI +16.9 to +26.3); engaged conversion 11.26% for Javo versus 11.20% for humans, meeting the non-inferiority margin (one-sided p = 0.004) without showing superiority; cost per conversation 1.8% of the human cost; guardrails met. Unclear from the abstract: how 'engaged' visitors are defined, how cost was computed, and the author's relationship to Javo.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Randomized, large-scale, prespecified guardrails and a non-inferiority design are rare in LLM-agent papers, which usually stop at benchmarks.

Randomized, large-scale, prespecified guardrails and a non-inferiority design are rare in LLM-agent papers, which usually stop at benchmarks. The RCT design is the contribution; the model is incidental. Caveats: single-author, abstract-level read, the engaged-visitor subset analyses are post-randomization conditioning, and the author's tie to the product is unstated. Expect more vendors to copy the three-arm (none / generic / specialised) design.

### Similar / related work

- [**Neutral Is Not Free: Evaluating Downside Risk in Neutral Launches**](2026-10-09-arxiv-neutral-launches-expected-bayesian-loss.md) (in this bank) — non-inferiority and downside-risk thinking for 'is it at least as good' claims
- [**MLE Agents: Autonomous ML Engineering in Production Recommendation Systems**](2026-10-16-arxiv-mle-agents-production-search-ranking.md) (in this bank) — another agent claim judged by production online tests
- [**Measuring Gift Card Program Incrementality via Causal Data Fusion**](2026-10-07-arxiv-airbnb-gift-card-incrementality-data-fusion.md) (in this bank) — incrementality measurement for a commercial program

### Jargon buster

- **Non-inferiority test** — A test that the new option is not worse than the incumbent by more than a prespecified margin, rather than a test that it is better.
- **Revenue per visitor** — Total revenue divided by all randomized visitors, so it includes people who never engaged; a conservative intent-to-treat style metric.
- **Engaged-visitor conversion** — Conversion among visitors who interacted with the agent; conditioning on engagement can break randomization balance, so read it with care.
