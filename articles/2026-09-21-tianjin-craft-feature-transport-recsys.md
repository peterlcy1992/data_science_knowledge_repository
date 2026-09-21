---
id: tianjin-craft-feature-transport-recsys
title: "From Feature Interaction to Feature Transport: A Unified Block for Scalable Recommendation Models"
source: "arXiv (Tianjin University)"
url: "https://arxiv.org/abs/2609.01655"
published: "2026-09"
added: "2026-09-21"
category: personalization-recsys
tags: [feature-interaction, ctr-prediction, sequence-modeling, model-scaling, advertising, architecture]
novelty: 3
sourced_via: "web search"
---

# From Feature Interaction to Feature Transport: A Unified Block for Scalable Recommendation Models

**Source:** [arXiv (Tianjin University)](https://arxiv.org/abs/2609.01655) · Published 2026-09 · Added 2026-09-21
**Category:** Personalization & Recommender Systems · **Tags:** `feature-interaction`, `ctr-prediction`, `sequence-modeling`, `model-scaling`, `advertising`, `architecture`

## TL;DR

Unified recommendation models have to jointly process multi-field, non-sequential features (like user demographics) and sequential behavior (like click history) in the same network, and most existing architectures do this by mixing all the tokens together inside each layer. Tianjin University researchers argue that's the wrong unit of design — what matters is how intent information is carried, filtered, and preserved *across* stacked layers — and propose CRAFT, a block that treats non-sequential context as an active controller reshaping sequence representations as they pass through the network, validated with a leaderboard-topping result on the TAAC2026 advertising competition.

## 1. Business context

Modern industrial recommendation and ads-ranking models are "unified" in the sense that a single network has to consume both non-sequential, multi-field features (age, device, static profile attributes) and sequential behavioral signals (the order and timing of past clicks or purchases) to predict something like click-through rate. Getting the interaction between these two feature families right matters directly for ranking quality and ad revenue, and the dominant architectural approach — mixing heterogeneous feature tokens together within each transformer-style layer — treats every layer's job as a fresh, local interaction problem. The paper's business-relevant claim is that this local, per-layer framing under-uses model depth: it doesn't explicitly manage how useful signal should be carried forward, filtered, or preserved as it moves through a stack of many layers, which becomes a growing limitation as production models get deeper and wider.

## 2. Technical details

The paper introduces **feature transport** as an alternative framing: instead of treating each layer as an isolated feature-mixing step, it models the deep network as a **discrete context-conditioned representation evolution process**, where information about user intent is explicitly transported, filtered, and preserved across stacked blocks rather than re-derived from scratch at each layer.

The concrete architectural unit is the **CRAFT block** (Contextual Residual Adaptive Feature Transport):

- It aggregates the non-sequential, multi-field features into a single **reliability-aware contextual field** — a summary representation of the static context, weighted by how reliable/informative each field is.
- That contextual field is then used to generate two signals applied to the sequence (behavioral) representation as it passes through the block: a **residual displacement** signal that adjusts the representation, and a **memory-preserving** signal that protects useful information from being overwritten layer to layer.
- Architecturally, this reframes non-sequential context from a passive object that gets mixed with sequence tokens into an **active controller** that steers how the sequence representation evolves through the network.

This is positioned as a shift from *interaction-centric* design (mix features together per layer) to *transport-centric* design (manage what persists and what changes as representations move through depth).

## 3. Impact — potential & realized

**Realized:** CRAFT was evaluated on the **TAAC2026** industrial advertising-recommendation competition, achieving a test AUC of **0.838090**, surpassing the previous leaderboard-best of 0.83798. The paper reports it scales further with more capacity — six stacked blocks reached 0.838148 AUC, and increasing hidden dimension reached 0.838106 AUC — showing the architecture keeps improving with both added depth and added width rather than saturating quickly, which is a common failure mode for feature-interaction architectures at scale.

**Potential:** if the transport-centric framing generalizes beyond this one competition benchmark, it offers production ranking teams a principled way to keep scaling unified recommendation models deeper without the diminishing returns that plague many feature-interaction architectures — directly relevant to any team currently investing in bigger ranking or ads models and hitting a scaling wall.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid architectural idea, validated only on one competition benchmark so far

The core reframing — think about what persists across depth, not just what mixes within a layer — is a genuinely useful lens, and the reported scaling behavior (AUC keeps improving with more blocks and wider hidden dimensions) is a meaningful signal that the approach isn't just a one-off tweak. That said, this is an academic paper out of a single university lab, validated on one advertising competition's leaderboard rather than a live production system with online metrics, so it sits closer to "promising direction other industrial teams may want to test" than a proven production technique.

### Similar / related work

- [**SequenceO1: End-to-End Ultra-Long (100K) Sequence Modeling in Recommendation with Low-Rank Caching**](2026-09-13-bytedance-sequenceo1-ultra-long-sequence-recsys.md) (in this bank) — another recent industrial-scale approach to managing sequential behavioral representations efficiently, though focused on sequence length rather than feature-interaction architecture.
- [**UniRec: Cross-stage Multi-Task Fusion with Preference Alignment for Cascaded Recommender Systems**](2026-09-14-kuaishou-unirec-cross-stage-recommendation-fusion.md) (in this bank) — a different approach to unifying signal across stages of a recommendation pipeline, complementary to CRAFT's within-model layer-to-layer framing.
- General feature-interaction literature for CTR prediction (e.g., DCN-style cross networks and their successors) — the established baseline family CRAFT positions itself against; left unlinked as a broad body of prior work rather than one paper.

### Jargon buster

- **Feature interaction** — the modeling problem of capturing how different input features combine to affect a prediction (e.g., how a user's device type and time-of-day jointly affect click probability), central to CTR/ranking models.
- **AUC (Area Under the ROC Curve)** — a standard metric for classification quality (like click-vs-no-click prediction) where 1.0 is perfect and 0.5 is random guessing; in mature industrial CTR models, gains are often measured in the third decimal place because the baselines are already strong.
- **Residual connection** — a network design where a layer's output is added back to its input rather than replacing it, which helps preserve information as it passes through many stacked layers; CRAFT's "memory-preserving signal" builds on this idea in a feature-transport-specific way.
- **TAAC2026** — an industrial advertising-recommendation competition (Tencent Advertising Algorithm Competition) used here as a public, leaderboard-ranked benchmark for comparing ranking-model architectures.
