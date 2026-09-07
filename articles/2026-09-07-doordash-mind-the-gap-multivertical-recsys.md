---
id: doordash-mind-the-gap-multivertical-recsys
title: "Mind the Gap: Using LLMs to Bridge Behavioral Silos in Multi-Vertical Recommendations"
source: "DoorDash Engineering / arXiv"
url: "https://arxiv.org/abs/2606.06779"
published: "2026-06"
added: "2026-09-07"
category: personalization-recsys
tags: [llm-features, rag, cold-start, multi-task-learning, cross-vertical, ranking]
novelty: 4
sourced_via: "full-text fetch"
---

# Mind the Gap: Using LLMs to Bridge Behavioral Silos in Multi-Vertical Recommendations

**Source:** [DoorDash Engineering / arXiv](https://arxiv.org/abs/2606.06779) · Published 2026-06 · Added 2026-09-07
**Category:** Personalization & Recommender Systems · **Tags:** `llm-features`, `rag`, `cold-start`, `multi-task-learning`, `cross-vertical`, `ranking`

## TL;DR

DoorDash uses an LLM-driven, hierarchical RAG pipeline to generate taxonomic user-affinity features from a data-rich vertical (restaurants) and transfer them into data-sparse verticals (grocery, retail), feeding a production multi-task ranking model to close the cold-start gap between verticals without collecting years of fresh behavioral data.

## 1. Business context

DoorDash's expansion into grocery and retail inherited a structural disadvantage: those verticals lack the years of dense order history that make restaurant recommendations work well. A user who has ordered from restaurants hundreds of times may have ordered groceries only a handful of times, so behavioral models trained per-vertical see grocery and retail as near-cold-start problems even for long-tenured users. The obvious fix — wait for more data to accumulate — is slow and costly in lost personalization quality during the interim, so the team looked for a way to transfer what's already known about a user's preferences across the vertical boundary instead of re-learning it from scratch.

## 2. Technical details

The framework has three parts. First, a hierarchical Retrieval-Augmented Generation (RAG) pipeline reads a user's restaurant order history and search queries and derives multi-level taxonomic features — structured categories and sub-categories of preference, not raw text. Second, an LLM synthesizes these into sparse, high-dimensional features that encode both long-term cross-vertical affinities (a user who orders from Italian restaurants is more likely to buy Italian grocery staples) and short-term intent signals from recent search behavior. Third, these LLM-generated features are integrated directly as inputs into DoorDash's existing production Multi-Task Learning (MTL) ranking model, rather than requiring a separate model or serving path — the transfer happens at the feature layer, so the rest of the ranking stack is unchanged.

## 3. Impact — potential & realized

The paper reports that offline and online evaluation showed the approach "significantly improves personalization and engagement in emerging business verticals" by bridging the behavioral data gap; specific lift percentages were not disclosed in the available material. The broader potential is a general recipe for any multi-vertical or multi-product platform (a marketplace expanding into a new category, a super-app adding a new service line) to bootstrap personalization in the new surface using an LLM's ability to reason across categories, instead of accepting a multi-year cold-start period for every new vertical.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A clean, generalizable answer to a real cross-vertical cold-start problem

Using an LLM as a cross-domain feature-transfer mechanism — reading dense behavior in one vertical and emitting structured taxonomic features usable in a sparse one — is a genuinely elegant reframing of cold-start as a transfer-learning problem solved at the feature layer rather than the model layer. That keeps the blast radius small (existing MTL ranker, existing serving path) which is probably why it shipped. It's not conceptually unprecedented (transfer learning across product surfaces is an old idea), but doing the transfer via LLM-synthesized taxonomic features rather than shared embeddings or a jointly-trained model is a distinctive, production-pragmatic choice.

### Similar / related work

- [**JUDE: LLM-Based Representation Learning for LinkedIn Job Recommendations**](2026-09-06-linkedin-jude-llm-job-recommendations.md) (in this bank) — another case of LLM-derived representations feeding a production ranking model, though JUDE builds embeddings rather than structured taxonomic features.
- [**Enhancing "You May Also Like" (YMAL) Systems using LLMs and Word2Vec**](2026-09-01-cvs-product-rec-word2vec-llm.md) (in this bank) — a lighter-weight precedent for using LLM output as recommendation features alongside a classical embedding method.
- [**Swiggy's In-House Predicted Lifetime Value Model for Customer Acquisition**](2026-09-04-swiggy-predicted-lifetime-value-multitask-mlp.md) (in this bank) — shares the multi-task ranking/scoring architecture this paper feeds into, in a different marketplace-personalization context.

### Jargon buster

- **Hierarchical RAG** — retrieval-augmented generation applied at multiple levels of a taxonomy (e.g., cuisine → dish type → specific item) rather than a single flat retrieval step, so the generated features preserve category structure.
- **Cold start** — the problem of making good recommendations for a user or item with little or no interaction history, here specifically "cold" within one vertical despite the user being well-known in another.
