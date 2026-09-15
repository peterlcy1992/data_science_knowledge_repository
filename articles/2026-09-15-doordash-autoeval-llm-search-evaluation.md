---
id: doordash-autoeval-llm-search-evaluation
title: "How DoorDash Leverages LLMs to Evaluate Search Result Pages"
source: "DoorDash Engineering Blog"
url: "https://careersatdoordash.com/blog/doordash-llms-to-evaluate-search-result-pages/"
published: "2026-05"
added: "2026-09-15"
category: search-ranking
tags: [llm-as-judge, search-evaluation, whole-page-relevance, human-in-the-loop]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# How DoorDash Leverages LLMs to Evaluate Search Result Pages

**Source:** [DoorDash Engineering Blog](https://careersatdoordash.com/blog/doordash-llms-to-evaluate-search-result-pages/) · Published 2026-05 · Added 2026-09-15
**Category:** Search & Ranking · **Tags:** `llm-as-judge`, `search-evaluation`, `whole-page-relevance`, `human-in-the-loop`

## TL;DR

DoorDash built AutoEval, a human-in-the-loop, LLM-powered system that judges the quality of entire search result pages rather than individual results in isolation, using a custom Whole-Page Relevance (WPR) metric. It replaces the scale, latency, and consistency bottlenecks of pure human annotation with automated judgments that match or exceed crowd-annotator accuracy, cutting evaluation turnaround time by 98%.

## 1. Business context

Evaluating search relevance well has traditionally meant paying humans to review results — a process that's slow, expensive, and, importantly, inconsistent between raters and over time. That's a real constraint on how fast a search team can iterate: every new ranking model or UI change needs relevance evaluation before it can ship with confidence, and if that evaluation loop takes days or weeks and only covers a fraction of real query traffic, it becomes the bottleneck on shipping search improvements at all. DoorDash's search surface spans everything from common, high-volume queries to a long tail of rare ones, and human annotation capacity naturally concentrates on head queries, leaving torso and tail queries under-evaluated — exactly the queries where a broken result page is easiest to miss until a user hits it.

## 2. Technical details

AutoEval is built around a **Whole-Page Relevance (WPR)** metric that judges an entire search results page holistically, rather than scoring individual result-query pairs independently and rolling them up — a deliberate design choice, since a page can fail a user even if every individual item on it would look "relevant" in isolation (e.g., a page that's technically on-topic but poorly ordered, redundant, or missing an obvious best match). The system combines LLMs, prompt engineering, and expert human oversight rather than removing humans from the loop entirely: LLM judgments handle the bulk of the volume, while human expert raters stay involved for guideline development, edge cases, and calibration — keeping a human check on the parts of the evaluation process that most need judgment and consistency oversight, while automating the repetitive volume that doesn't.

## 3. Impact — potential & realized

**Realized:** AutoEval unlocked automated relevance assessment at the scale of millions of judgments per day, with a reported 98% reduction in evaluation turnaround time compared to the prior human-annotation-driven process, while matching or exceeding human rater accuracy. That combination — faster and at least as accurate — is what let DoorDash extend evaluation coverage across head, torso, and tail queries instead of concentrating human review capacity on the highest-volume queries alone.

**Potential:** Freeing expert human raters from high-volume routine judgments to focus on guideline development, edge cases, and calibration is a pattern that compounds — those raters become higher-leverage over time as the evaluation guidelines they refine make the LLM judges themselves more accurate. The whole-page evaluation framing is also broadly transferable beyond DoorDash's search surface, to any ranked-list product (feeds, marketplaces, ad slots) where the right unit of quality judgment is the assembled page a user actually sees, not any single item on it.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-executed, human-anchored LLM-judge system, not a new evaluation paradigm

LLM-as-a-judge for search relevance is now a common pattern across the industry; what distinguishes this write-up is the whole-page framing (evaluating the assembled result set rather than item-by-item) and the explicit decision to keep human raters in the loop for calibration and edge cases rather than fully automating evaluation away. That's the production-maturity signal worth copying — teams building LLM evaluators for ranked surfaces should design for whole-result-set judgment and a durable human role from the start, not bolt them on after building an item-level judge.

### Similar / related work

- [**Netflix — Evaluating Netflix Show Synopses with LLM-as-a-Judge**](2026-09-14-netflix-llm-judge-show-synopses.md) (in this bank) — a different content-evaluation domain sharing the same core discipline: calibrating an LLM judge against human raters rather than trusting it blind, though Netflix's calibration is against a fixed golden set rather than an ongoing human-in-the-loop process.
- [**Airbnb — From Weeks to a Day: How We Made LLM Evaluation Fast Enough to Iterate On**](2026-09-07-airbnb-llm-eval-fast-iteration.md) (in this bank) — another company's push to make LLM-system evaluation fast enough to unblock iteration speed, attacking the same underlying "evaluation is the bottleneck" problem from the infrastructure-noise angle rather than the whole-page-metric angle.
- **DoorDash — LLM-as-a-Judge: Evaluating natural language search** — a companion DoorDash post applying a related facet-based LLM-judge approach specifically to natural-language search queries, extending the same evaluation philosophy to a different query type.

### Jargon buster

- **LLM-as-a-judge** — Using a large language model to score or grade content (here, search result pages) against a rubric, instead of relying solely on human reviewers or simple rule-based checks.
- **Whole-Page Relevance (WPR)** — DoorDash's metric for scoring an entire assembled search results page as a single unit, rather than averaging or summing scores computed independently for each individual result.
- **Head / torso / tail queries** — A way of bucketing search queries by frequency: head queries are the most common and highest-volume, tail queries are rare and numerous, and torso sits in between — tail queries are typically hardest to get enough human evaluation coverage on.
- **Human-in-the-loop** — A system design where automation handles the bulk of a task but humans remain actively involved at specific points (here, calibration and edge cases) rather than being removed from the process entirely.
