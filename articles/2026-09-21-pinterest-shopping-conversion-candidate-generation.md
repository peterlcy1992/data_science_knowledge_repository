---
id: pinterest-shopping-conversion-candidate-generation
title: "From Clicks to Conversions: Architecting Shopping Conversion Candidate Generation at Pinterest"
source: "Pinterest Engineering Blog"
url: "https://medium.com/pinterest-engineering/from-clicks-to-conversions-architecting-shopping-conversion-candidate-generation-at-pinterest-04cae5e1455b"
published: "2026-04"
added: "2026-09-21"
category: personalization-recsys
tags: [candidate-generation, shopping-ads, multi-task-learning, dcn, roas, advertising]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# From Clicks to Conversions: Architecting Shopping Conversion Candidate Generation at Pinterest

**Source:** [Pinterest Engineering Blog](https://medium.com/pinterest-engineering/from-clicks-to-conversions-architecting-shopping-conversion-candidate-generation-at-pinterest-04cae5e1455b) · Published 2026-04 · Added 2026-09-21
**Category:** Personalization & Recommender Systems · **Tags:** `candidate-generation`, `shopping-ads`, `multi-task-learning`, `dcn`, `roas`, `advertising`

## TL;DR

Pinterest rebuilt the candidate-generation stage of its shopping ads pipeline to optimize directly for purchase conversion rather than clicks, first shipping in 2023 and iterating through 2025 into a unified multi-task model. The result: meaningful, compounding gains in both advertiser return-on-ad-spend and the Pinner shopping experience, showing the two goals aren't in tension when the model is built around the right objective.

## 1. Business context

Pinterest's shopping ads business depends on surfacing products that a Pinner is likely to actually buy, not just click on — a candidate-generation model optimized for clicks will surface visually engaging or curiosity-driven products that don't convert, wasting advertiser spend and eroding trust in the ad product. The business bet described in this post is that rearchitecting candidate generation to target purchase conversion as the primary signal — rather than treating conversion as something a downstream ranking stage cleans up after click-optimized retrieval — would improve advertiser ROAS (return on ad spend) without hurting, and potentially while improving, the browsing experience for Pinners.

## 2. Technical details

Pinterest's first shopping-conversion candidate generation model shipped to production in 2023. Key modeling decisions carried through its evolution:

- **Unified model across surfaces** — rather than maintaining separate candidate-generation models per placement/surface, Pinterest converged on a single model serving shopping candidates broadly.
- **Conversion- and duration-weighted engagement data** — training data weights click and click-duration signals by how predictive they are of eventual conversion, rather than treating all clicks as equally valuable positive signal.
- **Architecture** — the model uses a **Parallel DCN v2 and MLP Cross Layers** architecture (a deep cross network design for capturing feature interactions), progressing from an initial separate multi-head design (distinct heads/towers for different objectives) to a **unified multi-task architecture** that added an explicit advertiser-level matching objective, aligning candidate generation more directly with advertiser outcomes rather than only Pinner-side engagement.

## 3. Impact — potential & realized

**Realized:** the initial 2023 production launch delivered a **2.3% increase in shopping conversion volume** and a **2.7% lift in shopping impression-to-conversion rate**, alongside Pinner-experience improvements of **1.5% higher click-through rate** and **2.2% higher CTR-over-30-seconds** (a proxy for more deliberate, higher-intent clicks rather than idle ones). Continued iteration through 2025 — culminating in the unified multi-task architecture with the advertiser-matching objective — added a further **3.1% improvement in ROAS** for US shopping campaigns.

**Potential:** the trajectory across 2023–2025 is itself the interesting data point — Pinterest frames conversion-optimized candidate generation and Pinner experience as "deeply intertwined" rather than a trade-off, suggesting other ads platforms retrofitting conversion signal into click-optimized retrieval stacks could expect compounding, not just one-time, gains as they iterate the objective and architecture together.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid, multi-year production engineering rather than a new technique

Optimizing candidate generation for conversion instead of clicks, and using DCN-style architectures for feature interactions, are both established practices in ads ranking. What's valuable here is the concrete, multi-year account of how the objective and architecture co-evolved in production — from separate multi-head models to a unified multi-task design with an advertiser-matching objective — and the willingness to report the compounding results across that evolution rather than a single launch snapshot.

### Similar / related work

- [**Uber's Out-of-App Recommendation System**](2026-09-19-uber-out-of-app-marketing-personalization.md) (in this bank) — another candidate-retrieval-plus-ranking pipeline built around a business (rather than pure-engagement) objective.
- [**The Science of Unified Ranking: Integrating Ads and Organic Recommendations**](2026-09-14-flipkart-unified-ranking-ads-organic.md) (in this bank) — a related e-commerce challenge of aligning ads objectives with the broader recommendation surface, using similar cross-feature learning-to-rank techniques.
- General DCN (Deep & Cross Network) literature for CTR/conversion prediction — the architectural family this work builds on; left unlinked as a broad body of prior work rather than one paper.

### Jargon buster

- **Candidate generation** — the first stage of a two-stage recommendation/ads pipeline, responsible for narrowing a huge catalog down to a shortlist of plausible items before a heavier ranking model scores them.
- **DCN (Deep & Cross Network)** — a neural architecture that explicitly models feature crosses (interactions between pairs or higher-order combinations of features) alongside a standard deep network, popular in CTR and conversion prediction.
- **ROAS (Return on Ad Spend)** — an advertiser-side metric measuring revenue generated per dollar of ad spend; a primary business metric for any ads platform.
- **Multi-task learning** — training a single model to predict several related targets at once (e.g., click, conversion, and an advertiser-matching signal) so the shared representation benefits from all the signals rather than optimizing just one in isolation.
