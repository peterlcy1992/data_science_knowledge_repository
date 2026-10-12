---
id: uber-cart-assistant-agentic-grocery-shopping
title: "Cart Assistant: Agentic Grocery Shopping on Uber Eats"
source: "Uber Engineering Blog"
url: "https://www.uber.com/us/en/blog/uber-cart-assistant/"
published: "2026-06"
added: "2026-10-12"
category: llm-genai
tags: [agents, structured-output, llm-judge, grocery, guardrails]
novelty: 3
sourced_via: "web search"
---

# Cart Assistant: Agentic Grocery Shopping on Uber Eats

**Source:** [Uber Engineering Blog](https://www.uber.com/us/en/blog/uber-cart-assistant/) · Published 2026-06 · Added 2026-10-12
**Category:** llm-genai · **Tags:** `agents`, `structured-output`, `llm-judge`, `grocery`, `guardrails`

## TL;DR

Uber turns messy grocery intent (a handwritten list, recipe screenshot, vague goal) into a draft cart using a multi-prompt state graph that mixes LLM steps with deterministic price, quantity and assembly logic, leaving the shopper in control.

## 1. Business context

Grocery shopping starts with unstructured intent that keyword search handles poorly. The system has to understand the goal, map it to a store's inventory, choose items and quantities, and respect constraints while keeping the shopper able to edit.

## 2. Technical details

A multi-prompt state graph: an LLM with structured output makes a cart plan (items, search terms, constraints); backend search and catalog APIs retrieve and enrich candidates; an LLM applies a constrained rubric to judge semantic relevance; deterministic optimisation enforces item- and cart-level price and deal limits; an LLM reasons about quantities and deterministic arithmetic maps them to purchasable units; deterministic and LLM guardrails check schema, scope and grounding; a deterministic aggregator builds the cart and an LLM writes shopper-facing text. Items are processed in parallel so latency tracks the slowest item. Model names are not given; evaluation uses a multimodal LLM judge calibrated with human input.

## 3. Impact — potential & realized

Realized: the post reports no quantitative results, only the qualitative outcome of a reviewable draft cart. Potential: the pattern of narrow LLM steps wrapped in deterministic constraints and judge-based evaluation applies to other commerce workflows.

*Sourced from web search / abstract-level content; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Clean architecture write-up with no measured outcomes.

The useful idea is keeping money- and quantity-affecting logic deterministic and using LLMs only where judgement is needed. With no metrics reported, the effect on conversion or basket accuracy is unknown.

### Similar / related work

- [**Our Early Journey to Transform Instacart's Discovery Recommendations with LLMs**](2026-09-02-instacart-llm-discovery-shopping-hub.md) (in this bank) — another grocery LLM discovery system

### Jargon buster

- **State graph** — A workflow where each node does one task and edges define what runs next.
- **LLM judge** — A language model scoring outputs against a rubric, used for evaluation at scale.
- **Guardrail** — A check that blocks or repairs outputs that are out of scope or ungrounded.
