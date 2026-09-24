---
id: swiggy-instamart-picker-batching-optimization
title: "Optimising the Picking Process to Enable Faster Deliveries for Instamart"
source: "Swiggy Bytes"
url: "https://bytes.swiggy.com/optimizing-the-picking-process-to-enable-faster-deliveries-for-instamart-93de0fe9d819"
published: "2024-07"
added: "2026-09-24"
category: ml-infra-serving
tags: [order-batching, dark-store, assignment-optimization, quick-commerce, operations]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Optimising the Picking Process to Enable Faster Deliveries for Instamart

**Source:** [Swiggy Bytes](https://bytes.swiggy.com/optimizing-the-picking-process-to-enable-faster-deliveries-for-instamart-93de0fe9d819) · Published 2024-07 · Added 2026-09-24
**Category:** ML Infrastructure & Serving · **Tags:** `order-batching`, `dark-store`, `assignment-optimization`, `quick-commerce`, `operations`

## TL;DR

Swiggy Instamart's dark-store pickers were assigned incoming orders one-at-a-time on a round-robin basis, causing significant delays during peak demand. Batching orders with overlapping items and assigning whole batches to pickers — so a picker collects similar items in one store pass instead of walking the store separately per order — targets those peak-time delays directly.

*Note: this entry is built from search-surfaced summaries of the source article (the underlying Medium-hosted domain returned an unavailable response when fetched directly), so the description below is necessarily higher-level than a full-text read would allow. Quantitative results were not surfaced in available summaries and are therefore omitted rather than estimated.*

## 1. Business context

Instamart's dark-store fulfillment model depends on pickers physically walking the store to collect items for an order, then handing it off to a delivery partner. Under the prior system, whichever picker became free next was assigned the next incoming order on a simple round-robin basis, one order at a time. That works fine at low order volume, but during demand spikes (peak meal times, promotions), the queue of orders waiting for a free picker grows faster than pickers can clear it, and each picker still has to walk the full store layout for every single order — even when several queued orders share overlapping items. The business cost is direct: picking delay is a large share of the total delivery-time budget in quick commerce, where the entire value proposition is speed measured in minutes.

## 2. Technical details

The proposed fix is **order batching for pickers**: instead of assigning one order per picker per trip, the system groups multiple orders that share overlapping items into a batch and assigns the whole batch to a single picker. The core intuition is that a picker collecting for a batch of similar orders can pick all instances of a shared item in one pass through that part of the store, rather than re-walking to the same shelf separately for each order — converting redundant walking time into shared, amortized walking time across the batch. This is conceptually the picking-side analog of delivery-partner order batching (bundling multiple deliveries heading the same direction into one trip), applied instead to the in-store collection step.

## 3. Impact — potential & realized

The source material available does not surface specific quantitative results (e.g., picking-time reduction, throughput gains) for this Instamart implementation, so none are reported here rather than estimated from general industry batch-picking benchmarks. Directionally, the stated goal is reducing peak-time picking delays, and the mechanism (reducing redundant in-store travel by exploiting item overlap across queued orders) is a standard lever in warehouse-operations research for doing exactly that. The broader potential is straightforward: any dark-store or micro-fulfillment operation with a round-robin, single-order picker-assignment baseline has the same overlap-exploitation opportunity available.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — A standard warehouse-operations technique applied to quick commerce

Batch order picking is a long-established technique in warehouse and fulfillment-center operations research, predating quick commerce by decades; the contribution here is applying it to the dark-store/quick-commerce context rather than inventing a new method. Without disclosed metrics in the surfaces available, it's hard to assess how sophisticated the actual batching algorithm is (e.g., whether it's a simple greedy grouping by item overlap, or a more principled optimization considering picker load balancing and batch size limits) — the described approach reads as the straightforward version of the idea.

### Similar / related work

- [**Open-Sourcing Rebalancer: A Generic, High-Performance Library for Solving Assignment Problems**](2026-09-22-meta-rebalancer-assignment-optimization.md) (in this bank) — a general-purpose assignment-optimization library from Meta; the kind of tooling a more sophisticated version of this picker-batching problem (jointly optimizing batch composition and picker assignment) would sit on top of.
- Warehouse batch-order-picking optimization literature (e.g., genetic-algorithm and heuristic approaches to the batch order-picking problem) — the broader operations-research field this technique draws from; left unlinked as general body-of-work rather than a single citable source.

### Jargon buster

- **Dark store** — a small, local warehouse stocked with high-demand items and not open to walk-in customers, used purely to fulfill online quick-commerce orders quickly.
- **Order batching (picking)** — grouping multiple orders that share items so a single picker collects for all of them in one pass through the store, instead of doing a separate full walk per order.
- **Round-robin assignment** — the simplest possible task-assignment policy, where the next free worker (here, picker) simply takes the next item in the queue, with no consideration of workload similarity or optimization.
