---
id: pinterest-3tower-engagement-cotrain
title: "Beyond Two Towers: Launching the 3-Tower Engagement Co-Train Model (Part 2)"
source: "Pinterest Engineering Blog"
url: "https://medium.com/pinterest-engineering/beyond-two-towers-launching-the-3-tower-engagement-co-train-model-part-2-0b96167d2c14"
published: "2026-09"
added: "2026-09-25"
category: personalization-recsys
tags: [ads-ranking, two-tower, co-training, model-serving, ctr-prediction]
novelty: 3
sourced_via: "web search"
---

# Beyond Two Towers: Launching the 3-Tower Engagement Co-Train Model (Part 2)

**Source:** [Pinterest Engineering Blog](https://medium.com/pinterest-engineering/beyond-two-towers-launching-the-3-tower-engagement-co-train-model-part-2-0b96167d2c14) · Published 2026-09 · Added 2026-09-25
**Category:** Personalization & Recommender Systems · **Tags:** `ads-ranking`, `two-tower`, `co-training`, `model-serving`, `ctr-prediction`

## TL;DR

Pinterest co-trains a fast two-tower ranking model and a richer three-tower model inside a single network, then serves the cheap two-tower score for every ad candidate and the expensive three-tower score only for a selected subset — cutting three-tower offline loss by roughly 30% and delivering about 1% online gains in CTR and related engagement metrics with a matching ~1% CPC reduction, at only a modest GPU cost increase.

## 1. Business context

Ads ranking systems face a fundamental latency/quality trade-off: a two-tower architecture (separate user and item towers whose outputs are combined cheaply, often via a dot product) scores every candidate fast enough for real-time serving across a huge candidate set, but its architecture limits how richly it can model interactions between a user and an ad compared to a full cross-feature model. Pinterest's prior two-tower production ranker (the subject of "Part 1" in this series) was fast but capped in prediction quality; simply swapping in a fully cross-featured model for every candidate would blow the latency and compute budget of real-time ads ranking at Pinterest's scale. The goal was to get closer to cross-featured-model quality without paying its full serving cost on every candidate.

## 2. Technical details

Pinterest's solution co-trains two prediction heads inside one network: a fast two-tower prediction that uses a truncated (first 64 dimensions) slice of the model's engagement-task representation, and a richer three-tower prediction that uses the full representation plus additional cross-features between the user and item towers. Because both heads share the same underlying network and are trained together, the fast two-tower head benefits from the shared representation learning even though it only sees a compressed slice of it. In serving, this lets Pinterest use a two-stage approach: the cheap two-tower score runs against every ad candidate (preserving the low-latency, high-throughput property the original two-tower model was chosen for), while the more expensive three-tower score is computed only for a narrowed subset of top candidates where the extra compute buys the most ranking-quality improvement — a classic "spend compute where it matters" retrieval-then-rerank pattern applied within a single co-trained model rather than across two independently-trained ones.

## 3. Impact — potential & realized

Offline, the co-trained approach maintained two-tower prediction quality on the full candidate set while achieving roughly a 30% reduction in loss for the three-tower predictions on the engagement tasks, compared to the prior production model. In online A/B testing on standard ads, the three-tower co-train model delivered around 1% gains in CTR, gCTR30, and oCTR (three related click-through-rate engagement metrics), along with close to a 1% reduction in cost-per-click (CPC) — a rare case where an ads-ranking improvement moves both engagement and cost efficiency in the advertiser-friendly direction simultaneously — at only a modest increase in GPU serving spend.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-executed, production-proven instance of the retrieval-then-rerank pattern applied inside a single co-trained model

Two-stage retrieval/reranking and co-training shared representations across prediction heads are both established patterns in large-scale ranking systems — the specific contribution here is engineering execution: getting the fast and rich heads to share a network cleanly enough that the fast head doesn't regress, and getting real online A/B numbers (not just offline loss) to confirm the extra three-tower compute pays for itself in CTR and CPC. That said, the roughly 1% online lift, while real money at Pinterest's ad volume, is an incremental rather than a step-change result — solid engineering on a known architecture pattern rather than a new idea.

### Similar / related work

- [**Bypassing Inference Bottlenecks: Accelerating Complex AI Search with Retrieve-for-Train**](2026-09-24-google-retrieve-for-train-fanout-retrieval.md) (in this bank) — a different domain (search query fan-out) applying a similar principle of pushing expensive computation into training/offline distillation so serving stays cheap.
- [**Improving Uber Eats Home Feed Recommendations via Debiased Relevance Predictions**](2026-09-24-uber-debiased-position-bias-eats-feed.md) (in this bank) — another engagement-ranking production system reporting real online A/B metric movement, useful point of comparison for typical online-lift magnitudes in mature ranking systems.
- **Two-tower retrieval architecture literature** (the standard production pattern Pinterest's own "Part 1" post and much of the recsys industry builds on) — the baseline this co-trained model extends.

### Jargon buster

- **Two-tower model** — a ranking architecture with separate neural networks ("towers") encoding the user and the item independently, combined via a cheap operation like a dot product — fast to serve but limited in how richly it can model user-item interaction.
- **Co-training** — training two (or more) prediction heads together inside a shared network, so they benefit from a common learned representation even though they're used differently at serving time.
- **CTR / gCTR30 / oCTR / CPC** — click-through rate and related engagement metrics (gCTR30 and oCTR are Pinterest-specific engagement-rate variants); CPC is cost-per-click, an advertiser-facing efficiency metric that moving in the opposite direction from CTR (down, while CTR goes up) generally signals a genuinely better-targeted ad match rather than just more clicks at any cost.
