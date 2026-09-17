---
id: microsoft-taxonomies-unstructured-text-llms
title: "From Chaos to Clarity: Building Taxonomies from Unstructured Text Using LLMs"
source: "Data Science + AI at Microsoft (Medium)"
url: "https://medium.com/data-science-at-microsoft/from-chaos-to-clarity-building-taxonomies-from-unstructured-text-using-large-language-models-c1303db3adb1"
published: "2026-01"
added: "2026-09-17"
category: llm-genai
tags: [taxonomy-generation, text-clustering, embeddings, topic-modeling, llm-labeling]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# From Chaos to Clarity: Building Taxonomies from Unstructured Text Using LLMs

**Source:** [Data Science + AI at Microsoft (Medium)](https://medium.com/data-science-at-microsoft/from-chaos-to-clarity-building-taxonomies-from-unstructured-text-using-large-language-models-c1303db3adb1) · Published 2026-01 · Added 2026-09-17
**Category:** LLMs & Generative AI · **Tags:** `taxonomy-generation`, `text-clustering`, `embeddings`, `topic-modeling`, `llm-labeling`

## TL;DR

Microsoft lays out two complementary LLM-assisted methods for turning large volumes of unstructured text into an interpretable taxonomy — a **bottom-up** pipeline (extract signal, embed, cluster, interpret, meta-categorize) for when the category space is unknown, and a **top-down** approach for imposing a hierarchy when some business structure already exists — arguing LLMs make the decades-old taxonomy-building problem newly tractable without eliminating the need for human review.

## 1. Business context

Organizations routinely sit on large volumes of unstructured text — support tickets, reviews, free-text survey responses, open-ended feedback — that would be far more useful if organized into a consistent taxonomy: a defined set of categories analysts and downstream systems can report against, route on, or trend over time. Taxonomy building has traditionally been a slow, manual process requiring domain experts to read samples, propose categories, and iteratively refine them — expensive to do well and hard to keep current as language and topics drift. The pitch here is that LLMs' ability to capture semantic intent and generalize across phrasing — without heavy labeled-data requirements — makes this old problem newly tractable at scale.

## 2. Technical details

Microsoft describes two pipelines, suited to different starting conditions:

**Bottom-up (category space unknown).** Five stages: (1) *semantic extraction* — pull the meaningful signal out of raw text; (2) *embeddings* — represent that signal numerically; (3) *clustering* — group semantically similar items without predefined labels; (4) *cluster interpretation* — have an LLM read representative examples from each cluster and describe what it's about; (5) *meta-categorization* — group related clusters into a higher-level taxonomy structure. This mirrors the "extract, embed, cluster" pattern seen elsewhere in industry, extended with an explicit interpretation and roll-up step so the output is a labeled hierarchy rather than just clusters.

**Top-down (some structure already exists).** Rather than discovering categories from scratch, this approach imposes a hierarchy informed by existing business context — a known set of product categories, complaint types, or organizational structure — giving a more controlled result when the taxonomy doesn't need to be fully rediscovered.

The piece is explicit that neither pipeline removes the need for human judgment: LLMs have not eliminated the underlying difficulty of taxonomy building, and both methods' outputs still benefit from expert review and domain-knowledge input before the taxonomy is treated as final.

## 3. Impact — potential & realized

**Realized:** The article presents both pipelines as methodology rather than reporting a specific production deployment's metrics — no accuracy, coverage, or before/after efficiency numbers are given for either approach.

**Potential:** As a reusable methodology, this pattern applies broadly wherever an organization needs to go from a pile of unstructured text to a structured, reportable category system — customer feedback analysis, support-ticket routing, content moderation category design, or any other domain where the "extract → embed → cluster → interpret" shape recurs, provided a human review step is kept in the loop.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — A clear, well-organized recap of an established pattern

Embedding-and-clustering unstructured text, then having an LLM label the resulting clusters, is now a fairly standard pattern across the industry (see Airbnb's Insight Miner in this bank for a near-identical extract/embed/cluster backbone). This piece's contribution is mainly clarity of exposition — cleanly separating the bottom-up and top-down cases and being upfront that human review remains necessary — rather than introducing a new technique.

### Similar / related work

- [**Beyond the Model: Engineering AI Infra with Scientific Judgement**](2026-09-17-airbnb-insight-miner-agent-harness-scientific-judgement.md) (in this bank) — Airbnb's Insight Miner uses the same extract-embed-cluster backbone as this piece's bottom-up pipeline, but wraps it in a full agent harness with methodology-as-infrastructure framing rather than presenting it as a standalone method.
- **BERTopic and other embedding-based topic modeling toolkits** — the broader pre-LLM lineage of the bottom-up pipeline's embed-then-cluster stages, which this approach extends with LLM-based cluster interpretation and meta-categorization.

### Jargon buster

- **Bottom-up taxonomy** — Building the category structure by discovering it from the data itself (via clustering) rather than starting from a predefined hierarchy.
- **Top-down taxonomy** — Imposing a category structure informed by existing business knowledge, rather than discovering it purely from the data.
- **Meta-categorization** — Grouping already-formed clusters or categories into a higher, more general layer of the hierarchy (e.g. rolling up "late delivery" and "wrong item" into "fulfillment issues").
