---
id: uber-eats-halving-search-latency
title: "Halving the Time: How Uber Eats Rebuilt Its Search Pipeline"
source: "Uber Engineering Blog"
url: "https://www.uber.com/us/en/blog/uber-eats-search-pipeline/"
published: "2026-09"
added: "2026-09-16"
category: search-ranking
tags: [search-latency, microbatching, embeddings, ranking, ads-serving, gpu-serving]
novelty: 3
sourced_via: "web search"
---

# Halving the Time: How Uber Eats Rebuilt Its Search Pipeline

**Source:** [Uber Engineering Blog](https://www.uber.com/us/en/blog/uber-eats-search-pipeline/) · Published 2026-09 · Added 2026-09-16
**Category:** Search & Ranking · **Tags:** `search-latency`, `microbatching`, `embeddings`, `ranking`, `ads-serving`, `gpu-serving`

## TL;DR

Uber Eats cut its end-to-end search latency in half through dozens of parallel, stacked optimizations across retrieval, ranking, ads, and infrastructure — not one silver bullet. The team also used an AI coding agent, armed with production profiling tools and automated benchmarking, to help find and land many of the smaller wins.

## 1. Business context

Search is the entry point to almost every Uber Eats order, and the team frames the stakes bluntly: "every millisecond of search latency is product latency" — it affects conversion, how deep users browse, and whether they order at all. The Uber Eats catalog spans several billion items across retrieval, ranking, hydration, and presentation stages, so a latency win anywhere in that chain compounds across enormous request volume. Rather than chase one big architectural rewrite, the team set out to systematically squeeze latency out of every stage of the pipeline at once.

## 2. Technical details

The post organizes the work by pipeline stage:

**UX-first metric shift.** Instead of optimizing raw backend API response time, the team switched their primary metric to ATF (above-the-fold) completion — how fast the visible part of the results actually renders. Server-side pagination with caching and a move to async template rendering with vertical scaling delivered a 200ms+ improvement on this metric alone.

**Retrieval.** Low-yield lexical retrieval strategies were removed (120ms reduction), chain-store deduplication was improved, and — notably — product-level embeddings replaced item-level lookups, cutting data-lookup volume by roughly 100x (50ms reduction). This mirrors a broader theme in the industry of collapsing near-duplicate catalog entries (many store-specific SKUs of the same underlying product) before they ever reach the expensive parts of the pipeline.

**Ranking and hydration.** The team split a monolithic hydration step into parallel ranking and presentation phases (100ms+ reduction), eliminated false dependencies in the pipeline's execution DAG (35ms), added request hedging across presentation-layer calls (40ms), and upgraded ranking model serving to GPUs.

**Ads.** The ads subsystem moved from row-oriented to column-oriented data layout, relocated ad-specific data into application memory, and removed redundant serialization cycles — a combined 130ms reduction.

**Infrastructure.** Lower-level tuning included parallelizing result encoding/decoding (50ms), reducing embedding precision and compression footprint (46% smaller), opening additional service-mesh connections (up to 53ms), and converting Go objects from pointer to value types to cut garbage-collection overhead.

**Agentic optimization loop.** Layered on top of the manual work, the team deployed an AI coding agent wired into production profiling tools, code generation, and automated benchmarking, using an LLM-based quality-evaluation framework to vet its suggestions. The agent was pointed at the long tail of small, tedious wins — redundant work, blocking metrics calls, repeated config fetches, allocation patterns — that are individually minor but numerous enough to add up.

## 3. Impact — potential & realized

**Realized:** The team reports roughly 900ms+ of measurable, documented latency reductions across the workstreams above, cutting overall search latency in half, with no measurable regression in conversion or result quality.

**Potential:** The post lists several follow-on initiatives not yet fully shipped: end-to-end microbatching so retrieval, hydration, and ranking overlap instead of running strictly in sequence (100ms+ estimated); moving to product-level (rather than item-level) search, which shrinks the effective corpus ~100x and has shown 50%+ p99 latency reduction in early observation; "zero-pass ranking" that filters candidates at the index layer before they reach scoring (30–50ms potential); and streaming responses via HTTP multi-part replies for progressive rendering.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Excellent production engineering, not a new idea

None of the individual techniques here — microbatching, GPU-serving upgrades, column-oriented ad data, embedding dedup — are novel on their own; this is a well-executed, well-measured latency-optimization sprint of the kind most large-scale search teams eventually run. What's genuinely interesting is the framing: treating an AI coding agent as a standing member of the optimization team, specifically for the long tail of small, tedious wins that are individually not worth a senior engineer's time but collectively material at Uber's scale. That's a believable, production-first use of agentic coding tools that goes beyond writing tests or boilerplate.

### Similar / related work

- [**When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving**](2026-09-14-nvidia-epd-disaggregation-multimodal-serving.md) (in this bank) — a different serving-latency problem (multimodal inference) solved with a similarly stage-by-stage disaggregation mindset: break a monolithic pipeline into independently scaled phases.
- [**Reduce LLM Latency with Prefix-Aware Routing on Amazon SageMaker Inference**](2026-09-14-aws-sagemaker-prefix-aware-routing-llm-latency.md) (in this bank) — another latency-driven infra piece from the same week, focused specifically on request routing rather than the full search stack.
- **Search/ranking system-design write-ups from DoorDash and Instacart on query pipeline latency** — the broader body of applied-search engineering this post sits alongside; no single comparable post was identified with a stable URL.

### Jargon buster

- **ATF (above-the-fold) completion** — How long it takes for the portion of a page visible without scrolling to finish rendering; a user-perceived latency metric, distinct from raw backend response time.
- **Microbatching** — Processing requests in small batches that flow through pipeline stages as soon as they're ready, rather than waiting for an entire batch or an entire prior stage to finish, so stages can overlap instead of running strictly in sequence.
- **DAG (directed acyclic graph)** — A dependency graph describing which computation steps must finish before others can start; a "false dependency" in a DAG is one that forces two steps to run in sequence even though they don't actually depend on each other's output.
- **Zero-pass ranking** — Filtering out clearly irrelevant candidates at the retrieval/index layer, before they ever reach the (more expensive) ranking model, to shrink the set of items the rest of the pipeline has to process.
