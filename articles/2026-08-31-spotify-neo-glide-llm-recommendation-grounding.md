---
id: spotify-neo-glide-llm-recommendation-grounding
title: "From Models to Products: LLMs for Recommendation at Spotify Scale"
source: "Spotify Research"
url: "https://research.atspotify.com/2026/8/from-models-to-products-llms-for-recommendation-at-spotify-scale"
published: "2026-08"
added: "2026-08-31"
category: llm-genai
tags: [llm, recommendation, semantic-ids, grounding, steerability, podcast-discovery]
novelty: 4
sourced_via: "web search"
---

# From Models to Products: LLMs for Recommendation at Spotify Scale

**Source:** [Spotify Research](https://research.atspotify.com/2026/8/from-models-to-products-llms-for-recommendation-at-spotify-scale) · Published 2026-08 · Added 2026-08-31
**Category:** LLMs & Generative AI · **Tags:** `llm`, `recommendation`, `semantic-ids`, `grounding`, `steerability`

## TL;DR

Spotify Research describes two complementary efforts — **NEO**, a general
framework for language-steerable recommendation, and **GLIDE**, a production
system built on a compact 1B-parameter LLM — for using LLMs as grounded,
instruction-following recommenders. In a 21-day online A/B test, GLIDE lifted
non-habitual podcast listening by 5.4% and new-show discovery by 14.3%.

## 1. Business context

LLMs are attractive for recommendation because they can reason over language,
user context, and catalog structure jointly, and can in principle be steered
with natural-language instructions rather than retrained per objective. The
practical blocker is **grounding**: an LLM asked to recommend from a huge,
constantly-changing catalog will tend to hallucinate items that don't exist or
aren't valid candidates. Spotify's goal was to get from research demonstrations
of LLM-based recommendation to something that could actually sit in a
production surface — specifically improving discovery of podcast episodes
listeners wouldn't otherwise find through their existing habits.

## 2. Technical details

- **NEO — the general framework.** NEO treats recommendation as one instance
  of a broader problem: adapting LLMs to reason jointly over language, users,
  and structured domain entities, with the aim of building grounded,
  steerable LLMs applicable beyond recommendation to other large-scale
  discovery/retrieval problems.
- **GLIDE — the production system.** GLIDE is built on a **compact 1B-parameter
  LLM** and formulates recommendation as an **instruction-following task over
  a discretized catalog**, solving the grounding problem via **Semantic IDs
  (SIDs)** — items are represented as short discrete code sequences the model
  generates instead of free-text titles, so outputs are constrained to valid
  catalog items by construction.
- **Context conditioning.** GLIDE conditions on recent listening history and
  lightweight user context, and injects **long-term user embeddings as soft
  prompts** to preserve stable long-run preferences under tight inference
  latency constraints.
- **Deployment shape.** Rather than replacing Spotify's existing
  recommendation stack, GLIDE acts as an **additional candidate generator**,
  with its grounded recommendations passed downstream into the existing
  ranking pipeline — a low-risk integration pattern for a still-maturing LLM
  component.

## 3. Impact — potential & realized

- **Realized:** In a **21-day online A/B test on Spotify Home**, covering
  roughly **20 million impressions per experiment cell**, GLIDE increased
  **non-habitual podcast listening by 5.4%** and **new-show discovery by
  14.3%**, while meeting production latency constraints and holding engagement
  guardrails.
- **Potential:** NEO's framing — grounding LLMs in domain entities, preserving
  language capability, and steering behavior via natural-language instructions
  — is presented as a template for other large-scale discovery/retrieval
  problems beyond recommendation, and semantic IDs as a grounding mechanism
  could generalize to other catalogs Spotify or others operate.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a real production LLM recommender with a measured discovery lift

Plenty of research has proposed LLM-based recommendation; comparatively few
write-ups report a live A/B test with meaningful traffic and a genuine lift on
a hard-to-move metric like new-show discovery. The technical recipe (semantic
IDs for grounding, soft-prompted long-term embeddings, small dedicated LLM
rather than a giant general-purpose one) is a sensible, production-pragmatic
combination rather than a fundamentally new idea, which is why this lands at 4
rather than 5.

### Similar / related work

- **Deploying Semantic ID-based Generative Retrieval for Large-Scale Podcast
  Discovery at Spotify** (in this bank) — the semantic-ID retrieval work GLIDE
  builds its grounding on.
- **Balancing Multiple Objectives in Generative Recommendations with Adaptive
  Decoding** (in this bank) — a complementary Spotify technique for steering
  generative recommenders at decode time rather than through the LLM's own
  instruction-following.
- **GenRec at Netflix** (in this bank) — another production LLM-native
  recommender, using a post-trained foundation LLM as a ranker rather than a
  semantic-ID candidate generator.

### Jargon buster

- **Grounding** — constraining a generative model's output to a fixed,
  verifiable set of valid items (here, the actual podcast catalog) instead of
  letting it produce arbitrary, possibly nonexistent text.
- **Semantic ID (SID)** — a short sequence of discrete codes representing an
  item's meaning, generated by the model instead of free text, so every
  possible output maps to a real catalog item.
- **Soft prompt** — a learned vector injected into a model's input in place of
  (or alongside) natural-language tokens, used here to carry long-term user
  preference signal cheaply at inference time.
- **Candidate generator** — a stage that proposes a shortlist of items for
  downstream ranking, rather than directly producing the final shown list.
- **Non-habitual listening** — consumption of content outside a user's
  established, repeat-listening pattern, used as a proxy for genuine discovery.
