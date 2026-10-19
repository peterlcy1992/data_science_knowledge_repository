---
id: arxiv-tool-recommendation-multi-step-agents
title: "Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs"
source: "arXiv cs.LG (Partee, Stevens, Damiba & Fanelle)"
url: "https://arxiv.org/abs/2610.23707"
published: "2026-10"
added: "2026-10-19"
category: llm-genai
tags: [agents, tool-retrieval, token-cost, gateway]
novelty: 3
sourced_via: "web search"
---

# Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs

**Source:** [arXiv cs.LG (Partee, Stevens, Damiba & Fanelle)](https://arxiv.org/abs/2610.23707) · Published 2026-10 · Added 2026-10-19
**Category:** llm-genai · **Tags:** `agents`, `tool-retrieval`, `token-cost`, `gateway`

## TL;DR

A deployed gateway exposes a catalog of about 8,200 tools to agents through three fixed tools and retrieves what each task needs, beating BM25 on ToolRet and cutting billed session cost by up to 40% with no change in task completion.

## 1. Business context

Agents fail when a needed tool is absent, but a roughly 8,200-tool catalog has definitions too large for any evaluated model's context window. Stuffing a fixed list wastes tokens and still misses tools.

## 2. Technical details

Tool Recommendation sits at the gateway between agent and tools and exposes the catalog through a fixed interface of three tools. Every call runs under the end user's credentials and is checked against per-service consent and the tools the agent is allowed to use. Evaluated on the public ToolRet benchmark and on paired multi-step workflows in Codex and Claude Code, against a fixed 100-tool baseline.

## 3. Impact — potential & realized

Realized (as reported): on ToolRet it places every needed tool in the top ten 57% more often than BM25 and compares favorably with published systems up to nine times its size; in Codex sessions the first recommendation covered all required tools 93% of the time; versus the 100-tool list, input tokens fell 17% (Codex) and 40% (Claude Code); total bill dropped in all 14 runs, by up to 40%, with no change in task completion. Details beyond the abstract not read.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Notable for measuring end-to-end billed cost on paired runs rather than only retrieval recall, which is the evaluation a decision-maker needs.

Notable for measuring end-to-end billed cost on paired runs rather than only retrieval recall, which is the evaluation a decision-maker needs. Only 14 paired runs and authors' own system, so treat the headline as indicative. Caveat: abstract-level read.

### Similar / related work

- [**How Stripe Is Designing Checkout for AI Agents**](2026-09-23-stripe-webmcp-checkout-ai-agents.md) (in this bank) — agent-to-tool interfaces in production

### Jargon buster

- **Tool retrieval** — Selecting, from a large catalog, the few tools an agent needs for a task so they fit in context.
- **Top-10 coverage** — Share of queries where every required tool appears in the first ten results.
