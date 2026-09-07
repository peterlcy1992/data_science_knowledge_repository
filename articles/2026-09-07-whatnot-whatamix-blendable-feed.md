---
id: whatnot-whatamix-blendable-feed
title: "Whatamix: Blendable Feed Construction"
source: "Whatnot Engineering"
url: "https://medium.com/whatnot-engineering/whatamix-blendable-feed-construction-2c94c21f6635"
published: "2025-11"
added: "2026-09-07"
category: personalization-recsys
tags: [dag-orchestration, feed-construction, retrieval, blending, ab-testing, reusability]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Whatamix: Blendable Feed Construction

**Source:** [Whatnot Engineering](https://medium.com/whatnot-engineering/whatamix-blendable-feed-construction-2c94c21f6635) · Published 2025-11 · Added 2026-09-07
**Category:** Personalization & Recommender Systems · **Tags:** `dag-orchestration`, `feed-construction`, `retrieval`, `blending`, `ab-testing`, `reusability`

## TL;DR

Whatnot built Whatamix, a DAG-based orchestration layer that represents each stage of feed construction — retrieval, feature hydration, scoring, filtering, blending — as a reusable, composable node, letting teams assemble new feeds by wiring nodes together instead of writing bespoke pipeline code per use case.

## 1. Business context

Whatnot runs multiple distinct feeds (e.g., different discovery surfaces mixing live shopping streams, video, and product content), and before Whatamix each feed's construction logic — retrieval from various candidate sources, scoring, filtering, and blending into a final ranked list — was largely bespoke per surface. That meant duplicated engineering effort, inconsistent observability and A/B testing support across feeds, and slow iteration whenever a team wanted to add a new candidate source or blending rule, since there was no shared abstraction to build on.

## 2. Technical details

Whatamix models a feed as a directed acyclic graph (DAG), where common feed-construction steps are implemented as modular, interchangeable nodes: candidate retrieval from different sources, feature hydration, model scoring, filtering, and blending. Independent branches of the graph — for example, retrieval from two unrelated candidate sources — are automatically executed asynchronously since the DAG structure makes their independence explicit, rather than requiring a developer to hand-write concurrency logic. The platform bakes in cross-cutting concerns that used to be reimplemented per feed: observability (metrics and logging attached to each node), A/B testing via configurable "feed params" that can vary node behavior per experiment arm, and error handling at the node boundary. Teams can build self-contained sub-DAGs for their own use case and contribute new reusable nodes back to the shared node library, so the framework's coverage grows organically as more feeds are built on it.

## 3. Impact — potential & realized

The write-up frames the benefits primarily in engineering-velocity terms: new feed logic is assembled from existing nodes rather than built from scratch, independent retrieval branches parallelize automatically, and every feed built on Whatamix inherits consistent observability and experimentation support rather than each team reinventing it. No specific latency, engagement, or adoption metrics were disclosed in the available material. The broader potential is a shared feed-construction substrate that lowers the marginal cost of Whatnot launching or iterating on a new discovery surface.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid platform engineering, a known pattern applied well

DAG-based orchestration of retrieval/scoring/blending stages is a well-established pattern in large-scale recommender infrastructure — Meta, LinkedIn, and others have published variations of the same idea (declarative pipelines composed of reusable, independently-testable stages). Whatamix's contribution is a clean, well-scoped implementation of that pattern for a mid-size company's multi-feed reality, with the practical wins (auto-parallelism from DAG structure, built-in experimentation) rather than a new algorithmic idea.

### Similar / related work

- [**Engineering the Next Generation of LinkedIn's Feed**](2026-09-03-linkedin-feed-llm-retrieval-gr-ranking.md) (in this bank) — a much larger-scale feed-ranking rebuild that shares the retrieval → ranking → blending pipeline shape.
- [**From Scoring to Spelling: Rebuilding Ads Retrieval at Instacart**](2026-09-01-instacart-ads-retrieval-rebuild.md) (in this bank) — another retrieval-pipeline rebuild focused on modularity and reuse across use cases.
- [**Pinner Progression: Better Use-Case Representation Driving Weekly Active User Growth**](2026-08-31-pinterest-pinner-progression-use-case-representation.md) (in this bank) — a candidate-generation and blending problem in the same feed-construction space, different specific technique.

### Jargon buster

- **DAG (Directed Acyclic Graph)** — a set of steps with dependencies but no cycles, so the system can automatically figure out which steps can run in parallel versus which must wait on another's output.
- **Feed params** — configuration values that can be varied per A/B test arm to change how a node in the DAG behaves (e.g., which scoring weights to use) without changing code.
