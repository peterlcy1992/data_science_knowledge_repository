---
id: booking-graph-fraud-detection
title: "Leveraging Graph Technology for Real-Time Fraud Detection and Prevention at Booking.com"
source: "Booking.com Engineering"
url: "https://medium.com/booking-com-development/leverage-graph-technology-for-real-time-fraud-detection-and-prevention-438336076ea5"
published: "2024-07"
added: "2026-08-30"
category: data-engineering
tags: [graph, fraud-detection, real-time, graph-features, bfs, entity-resolution, ml]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Leveraging Graph Technology for Real-Time Fraud Detection and Prevention at Booking.com

**Source:** [Booking.com Engineering](https://medium.com/booking-com-development/leverage-graph-technology-for-real-time-fraud-detection-and-prevention-438336076ea5) · Published 2024-07 · Added 2026-08-30
**Category:** Data Engineering · **Tags:** `graph`, `fraud-detection`, `real-time`, `graph-features`
_Surfaced via the Snacks Weekly on Data Science podcast._

## TL;DR

Booking.com models requests as a graph of shared identifiers, computes
**graph features** in real time via breadth-first traversal of connected
entities, and feeds those features to an ML fraud model — capturing the
**interconnected** nature of fraud that a per-request model misses.

## 1. Business context

Fraud is rarely a lone event: fraudsters reuse **linked actors, identifiers, and
requests**, so signals emerge from **shared data points** — a flagged email today
predicts risk for accounts connected to it tomorrow. A model that scores each
request in isolation cannot see those links. Booking.com wanted a **real-time**
platform that exploits the relational structure of fraud while still making a
fast, reliable per-request decision.

## 2. Technical details

- **Graph construction.** A **Graph Service** inserts request **identifiers as
  nodes** and adds **edges** between related identifiers, building a continuously
  updated graph of who/what is connected.
- **Real-time graph features.** For an incoming request, the service performs a
  **breadth-first search (BFS)** to fetch the **network of connected identifiers**,
  then **computes graph features** (properties of that local neighborhood) and
  returns them to the Fraud Detection Service.
- **ML on top of the graph.** Crucially, **querying the graph and finding a link is
  not enough** to call something fraud — the graph features feed **ML models** in
  the Fraud Detection Service that predict whether a request is fraudulent. Graph +
  ML, not graph rules alone.
- **Platform framing.** The graph database and traversal are one component of a
  larger fraud-prevention platform, designed for low-latency scoring at request
  time.

## 3. Impact — potential & realized

- **Realized:** a real-time fraud platform that turns relationship structure into
  predictive features, catching ring/linked fraud that isolated-request models
  miss.
- **Potential:** the "graph features → ML model" pattern generalizes to abuse,
  account-takeover, collusion, and trust-and-safety problems across marketplaces.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a well-executed instance of a proven pattern

Graph-based fraud detection is established (financial services, marketplaces), and
the architecture here — identifiers as nodes, BFS for the neighborhood, graph
features into an ML model — is the canonical design done cleanly and in real time.
The valuable, transferable emphasis is the discipline that **a link alone isn't a
verdict**: graph structure is *features*, and an ML model makes the call. Solid and
instructive, but it's applying a known blueprint rather than advancing it — a 3.
(A move to learned graph representations / GNNs would push it higher.)

### Similar / related work

- **NVIDIA: fraud detection with Graph Neural Networks** — the learned-representation
  direction beyond hand-computed graph features.
- **detectGNN** (arXiv 2503.22681) — GNNs for credit-card fraud, a research analog.
- **Databricks Feature Store: Sub-Second Freshness** (in this bank) — the real-time
  feature-serving discipline this depends on, applied to graph features.

### Jargon buster

- **Graph database** — a store optimized for nodes and the edges (relationships)
  between them, so "who is connected to whom" queries are fast.
- **Breadth-first search (BFS)** — a traversal that explores a node's immediate
  neighbors first, then their neighbors, etc.; used here to gather the local network
  around a request.
- **Graph features** — numeric summaries of a node's neighborhood (size, density,
  presence of flagged entities) used as model inputs.
- **Entity resolution** — deciding when different records (emails, devices, cards)
  refer to the same real-world actor; what makes the edges meaningful.
- **Graph Neural Network (GNN)** — a model that *learns* representations of nodes from
  the graph directly, rather than relying on hand-designed graph features.
