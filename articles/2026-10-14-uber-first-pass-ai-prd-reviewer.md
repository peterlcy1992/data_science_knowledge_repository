---
id: uber-first-pass-ai-prd-reviewer
title: "Lessons from Building a First-Pass AI PRD Reviewer at Uber"
source: "Uber Blog (Lakshmi Ashok)"
url: "https://www.uber.com/us/en/blog/first-pass-prd/"
published: "2026-05"
added: "2026-10-14"
category: llm-genai
tags: [llm-application, product-requirements, metric-rigor, evaluation, internal-tools]
novelty: 3
sourced_via: "full-text fetch"
---

# Lessons from Building a First-Pass AI PRD Reviewer at Uber

**Source:** [Uber Blog (Lakshmi Ashok)](https://www.uber.com/us/en/blog/first-pass-prd/) · Published 2026-05 · Added 2026-10-14
**Category:** llm-genai · **Tags:** `llm-application`, `product-requirements`, `metric-rigor`, `evaluation`, `internal-tools`

## TL;DR

Uber built a 'PRD Evaluator' that gives product requirement documents an automated first-pass review before human checkpoints: it assembles context, classifies the proposal, scores several dimensions (including Metric and Data Rigor) and outputs a launch-readiness scorecard. Reported outcomes are qualitative; no accuracy or latency figures are given.

## 1. Business context

Uber's product development runs through structured checkpoints where PRDs circulate across design, engineering, legal, operations, science and leadership. Drafts often arrive missing context - unsupported assumptions, adjacent-system impacts, prior experiments - so reviewers spend time on basic discovery instead of higher-level trade-offs. The tool is meant to raise the quality of PRDs entering review, not to change the checkpoint process.

## 2. Technical details

The article describes a four-step workflow. (1) Knowledge-base assembly: starting from the PRD, AI searches linked documents, decks, meeting notes, prior experiments and cross-functional artifacts, plus preloaded Uber context (core principles, metric definitions, jobs to be done). (2) Classification of each proposal to set review depth: lighter for UX parity or discoverability changes, moderate for incremental workflow or internal tooling, full for net-new capabilities, and full with specialised scrutiny for policy, pricing or marketplace changes. (3) Multi-dimension assessment, including Opportunity and Hypothesis, Product Scope, User Experience and Impact, and Metric and Data Rigor (a figure shows six dimension scores rated 'Looks Good' or 'Needs Review'). (4) A scorecard with a launch-readiness rating (Ready, Ready with Caveats, Not Ready), a 'start here' pointer, and per-gap findings with missing elements, replacement text and evidence, split into critical requirements and optimisations. The post does not name the underlying model or describe prompts/architecture.

## 3. Impact — potential & realized

Realized (qualitative): early internal usage by dozens of PMs, who used it to find blind spots, pressure-test headroom assumptions and spot adjacent-system impacts; the team reports sharper, faster review discussions. No quantitative metrics are reported. Authors' stated lessons: framework-driven critique beats generic feedback, context matters as much as writing quality, hard boundaries on critical gaps stop the tool overstating readiness, prioritisation is essential, and the tool informs rather than replaces human approval.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a sensible, well-scoped LLM-as-reviewer application; the useful ideas are classification-driven review depth and a hard floor on critical gaps, not the model.

The notable DS angle is that 'Metric and Data Rigor' is a first-class review dimension: an automated check that PRDs state hypotheses, metrics and prior experiments before humans spend time. The post offers no validation (agreement with human reviewers, false-positive rates), so the 'sharper discussions' claim is anecdotal. Expect similar reviewers for experiment-design docs.

### Similar / related work

- [**Airbnb: LLM evaluation for fast iteration**](2026-09-07-airbnb-llm-eval-fast-iteration.md) — evaluation of LLM products

### Jargon buster

- **PRD** — Product requirements document: the write-up of what to build, why, and how success will be measured.
- **Launch-readiness scorecard** — A structured rating of how ready a proposal is for review, here Ready / Ready with Caveats / Not Ready.
- **Metric and Data Rigor** — The reviewed dimension that checks whether success metrics and data plans are well-defined and measurable.
