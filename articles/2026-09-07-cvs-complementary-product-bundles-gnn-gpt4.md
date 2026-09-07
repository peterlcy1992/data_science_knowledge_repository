---
id: cvs-complementary-product-bundles-gnn-gpt4
title: "AI in CVS Front Store E-commerce: Building a Complementary Product Bundle Recommender"
source: "CVS Health Tech Blog"
url: "https://medium.com/cvs-health-tech-blog/ai-in-cvs-front-store-e-commerce-building-a-complementary-product-bundle-recommender-dc6c71dee682"
published: "2024-09"
added: "2026-09-07"
category: personalization-recsys
tags: [graph-neural-networks, gpt-4, llm-as-judge, bundle-recommendation, e-commerce]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# AI in CVS Front Store E-commerce: Building a Complementary Product Bundle Recommender

**Source:** [CVS Health Tech Blog](https://medium.com/cvs-health-tech-blog/ai-in-cvs-front-store-e-commerce-building-a-complementary-product-bundle-recommender-dc6c71dee682) · Published 2024-09 · Added 2026-09-07
**Category:** Personalization & Recommender Systems · **Tags:** `graph-neural-networks`, `gpt-4`, `llm-as-judge`, `bundle-recommendation`, `e-commerce`

## TL;DR

CVS combined a Graph Neural Network with GPT-4 to identify complementary products across a 25,000+ item front-store catalog, using GPT-4 both as a candidate-generation source (asking which products complement a given item) and as a judge that scores each resulting bundle on relevance and synergy before it ships.

## 1. Business context

Recommending complementary products — "buy this, and here's what pairs with it" — at CVS scale means reasoning across tens of thousands of front-store SKUs spanning very different categories (health, beauty, household, snacks), where co-purchase data alone is sparse for most item pairs and traditional collaborative-filtering approaches struggle to generalize to items with little transaction history. The team needed a way to identify plausible complements even for pairs that rarely or never co-occur in historical baskets, while still passing an internal bar for recommendation quality and going through CVS's AI governance review before launch.

## 2. Technical details

The pipeline pairs a Graph Neural Network — presumably built over product co-occurrence and/or catalog metadata, capturing structural relationships across the 25,000+ product catalog — with GPT-4 used in two distinct roles. First, as a generator: for a given source product, GPT-4 is asked which other products (from the available catalog) are complementary, producing candidate bundle members that go beyond what pure co-occurrence data would surface. Second, as an evaluator: GPT-4 scores each resulting bundle (one source product plus two recommended items) on a 1–5 scale across two dimensions — Relevance (is each recommended item individually complementary to the source product) and Synergy (do all items in the bundle work together as a set, not just pairwise with the source). This LLM-as-judge step acts as an automated quality gate before a bundle is considered for production, and the system went through CVS's AI governance review process to assess and mitigate risk prior to deployment.

## 3. Impact — potential & realized

The write-up reports the GNN+GPT-4 pipeline as effective at generating high-quality complementary bundles per the Relevance/Synergy scoring, though specific offline or online lift metrics were not available in the source material reviewed. The broader potential is a general recipe for cold-start-heavy bundle/cross-sell recommendation: use an LLM's world knowledge to propose candidates a co-occurrence model would miss, then use a second LLM pass as a scalable quality judge instead of requiring human review of every bundle before launch.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sensible, if now-familiar, GNN + LLM-judge combination

Using an LLM as both candidate generator and evaluator for recommendation bundles is a pattern that's become increasingly common across this bank's entries (Instacart's discovery pipeline and Shopify's Sidekick both lean on LLM-as-judge for quality gating). The specific pairing with a GNN for the underlying candidate structure is a reasonable, well-scoped design for the complementary-products problem, but the write-up doesn't disclose enough architectural or evaluation detail (GNN architecture, training data, offline/online metrics) to assess how much of the quality is coming from the graph model versus the GPT-4 layer.

### Similar / related work

- [**Enhancing "You May Also Like" (YMAL) Systems using LLMs and Word2Vec**](2026-09-01-cvs-product-rec-word2vec-llm.md) (in this bank) — the same company's earlier, lighter-weight combination of embeddings and LLM features for a related recommendation surface.
- [**Our Early Journey to Transform Instacart's Discovery Recommendations with LLMs**](2026-09-02-instacart-llm-discovery-shopping-hub.md) (in this bank) — shares the LLM-as-judge quality-gating pattern applied to a different recommendation surface (page layout vs. product bundles).
- [**Leveraging Graph Technology for Real-Time Fraud Detection and Prevention at Booking.com**](2026-08-30-booking-graph-fraud-detection.md) (in this bank) — a different application of graph-based modeling at production scale, useful context on graph-technology tradeoffs even though the use case differs.

### Jargon buster

- **Graph Neural Network (GNN)** — a model architecture that learns from data structured as a graph (here, products as nodes and relationships like co-purchase as edges), letting it capture relational patterns that flat tabular models miss.
- **LLM-as-judge** — using a large language model to score or evaluate the output of another system (here, a candidate product bundle) against defined criteria, as a scalable substitute for human review.
