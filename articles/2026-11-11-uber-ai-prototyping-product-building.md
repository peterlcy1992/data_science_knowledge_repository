---
id: uber-ai-prototyping-product-building
title: "AI Prototyping Is Changing How We Build Products at Uber"
source: "Uber Engineering Blog (Aayush Agrawal, Akanksha Sharma)"
url: "https://www.uber.com/us/en/blog/ai-prototyping/"
published: "2026-04"
added: "2026-11-11"
category: llm-genai
tags: [AI-prototyping, product-development, PRD, coding-assistants]
novelty: 2
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# AI Prototyping Is Changing How We Build Products at Uber

**Source:** [Uber Engineering Blog (Aayush Agrawal, Akanksha Sharma)](https://www.uber.com/us/en/blog/ai-prototyping/) · Published 2026-04 · Added 2026-11-11
**Category:** llm-genai · **Tags:** `AI-prototyping`, `product-development`, `PRD`, `coding-assistants`

## TL;DR

Two Uber product managers describe a year of AI-assisted prototyping (Lovable, Figma Make, Claude Code, Cursor): broader early exploration, faster cross-functional alignment and clearer MVP scoping. Prototypes complement rather than replace PRDs, with a prototype-first vs PRD-first checklist. Evidence is anecdotal and qualitative.

## 1. Business context

At Uber even small product changes span product, engineering, operations, policy and legal across regions, so building shared understanding is costly. The bet: make ideas tangible early so teams react to the same artifact rather than to written descriptions.

## 2. Technical details

Tools: Lovable, Figma Make, Claude Code and Cursor to generate and iterate interactive flows. Patterns reported: greater exploration (one PM explored six concepts in about 20 minutes), faster alignment, and unblocked execution via clearer MVP vs post-MVP scope. Process: problem framing → early prototyping → a sharper PRD → final designs. Prototype-first when the problem is ambiguous, needs fast alignment or leadership buy-in, or is internal/low-stakes; PRD-first when mobile-first (tools 'often underperform' there), strategic rather than UI-heavy, mature, high-risk or compliance-sensitive, or dependency-heavy. Prototyping was opened beyond product teams to engineering, platform and ops (e.g. an EMEA sales opportunity tracker).

## 3. Impact — potential & realized

Realized (anecdotal): 'Two hours of prototyping unblocked four weeks of discussion' (a Merchant-team PM); nearly 40% of global Uber tech hackathon submissions used a prototyping tool. No quantitative measurement of cycle time or outcomes is reported. Open questions they raise: the evolving role of the PRD (intent, trade-offs, success metrics), using AI to synthesise feedback faster, and moving prototypes to production.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — A readable practice note; low novelty and no measurement.

Relevance for data scientists is indirect but real: if prototypes arrive before PRDs, success metrics and experiment design need to be attached earlier too — the post itself says the PRD's value increasingly lies in capturing success metrics and decisions. A measured version (cycle time, decision reversals, experiment outcomes before/after) would be far more useful.

### Similar / related work

- [**Harbor: Stripe's AI-Assisted Prototyping Tool**](2026-09-18-stripe-harbor-ai-assisted-prototyping.md) — in this bank: Stripe's internal take on the same shift

### Jargon buster

- **PRD** — Product requirements document: the written spec of what to build and why.
- **MVP** — Minimum viable product: the smallest version worth shipping to learn from.
