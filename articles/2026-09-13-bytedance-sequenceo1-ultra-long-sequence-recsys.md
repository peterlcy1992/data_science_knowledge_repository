---
id: bytedance-sequenceo1-ultra-long-sequence-recsys
title: "SequenceO1: End-to-End Ultra-Long (100K) Sequence Modeling in Recommendation with Low-Rank Caching"
source: "ByteDance (arXiv / RecSys'26 Industry Track)"
url: "https://arxiv.org/abs/2609.08443"
published: "2026-09"
added: "2026-09-13"
category: personalization-recsys
tags: [sequence-modeling, long-sequence, recommendation, douyin, attention, caching, industrial-recsys]
novelty: 4
sourced_via: "full-text fetch"
---

# SequenceO1: End-to-End Ultra-Long (100K) Sequence Modeling in Recommendation with Low-Rank Caching

**Source:** [ByteDance (arXiv / RecSys'26 Industry Track)](https://arxiv.org/abs/2609.08443) · Published 2026-09 · Added 2026-09-13
**Category:** Personalization & Recommender Systems · **Tags:** `sequence-modeling`, `long-sequence`, `recommendation`, `douyin`, `attention`, `caching`, `industrial-recsys`

## TL;DR

ByteDance built SequenceO1, a "compress-then-reason" architecture that lets Douyin's ranking model condition on a user's full 100,000-event interaction history instead of truncating to a short recent window, using a fixed-size compressed sketch plus a 10K-token recent suffix — capturing 83% of the accuracy gain of naively scaling attention to 100K tokens at roughly 1/50th the training cost and 1/64th the inference cost, and shipping the win as real online engagement lifts on Douyin and Douyin Lite.

## 1. Business context

Sequential recommendation models get more accurate the more of a user's history they can see, but production ranking systems operate under hard latency, memory, inter-machine communication, and training-throughput budgets that make naively attending over very long histories (tens or hundreds of thousands of past interactions) infeasible — the compute and memory cost of standard attention grows with sequence length, and industrial ranking models must score every candidate for every request within a strict serving-latency window. Most production systems respond by truncating user history to a short recent suffix, which discards genuine long-term signal about a user's stable preferences. ByteDance's bet is that this truncation is leaving real accuracy on the table for Douyin (its short-video app) and its international counterpart, and that the fix is an architecture that reasons over ultra-long history without paying attention's usual quadratic-ish cost.

## 2. Technical details

SequenceO1 uses a two-stage, compress-then-reason design that separates a user's history into two complementary time scales:

- **Sketch Attention (SA)** — compresses the raw, arbitrarily long history (up to 100K interactions) into a fixed-size, *target-agnostic* representation built from a small set of learnable prototypes (the production configuration uses k=1K prototypes, Nsa=2 refinement iterations, and embedding dimension d=128). Being target-agnostic means the same compressed sketch can be reused across different candidate items and even different requests, which is what makes caching it cheap.
- **Stacked Target-to-History Cross-Attention (STCA)** — fuses two signals for the current candidate item: the compressed long-term sketch from Sketch Attention, and a full-resolution recent suffix of the most recent 10,000 interactions, so short-term intent is modeled at full fidelity while long-term preference is modeled at compressed fidelity.
- **Low-rank user-representation caching** — since the sketch is target-agnostic, it can be computed once per user and reused (cached) across many requests and candidates rather than recomputed per candidate, which is the main lever that makes serving-time cost tractable.
- **Multi-request batching, pipeline optimizations, and a fused FlashSA kernel** — systems-level work stacked on top of the architecture to further cut training and inference cost, including a custom fused attention kernel specialized for the Sketch Attention computation.

The model is evaluated both in a lightweight ablation setting and in ByteDance's full production ranking stack, and deployed at full production traffic on Douyin.

## 3. Impact — potential & realized

**Realized (offline):** In the lightweight ablation setting, SequenceO1 achieves +1.07% Finish AUC over a 10K-suffix-only STCA(512) baseline — retaining 83% of the gain that naively scaling STCA's attention directly to the full 100K history would give (+1.29% AUC), while being roughly 49.9x cheaper to train and 63.9x cheaper to run at inference at that 100K length. In the full production setting the reported gain is smaller but still positive: +0.29% AUC and +0.40% UAUC on the finish-prediction task.

**Realized (online, 30-day A/B):** On Douyin, +2.3256% Finish, +3.5910% Comment, +2.3617% Like, and -6.9829% Dislike; on Douyin Lite, +3.4872% Finish, +8.6132% Comment, and +2.9399% Like.

**Potential:** the general recipe — compress old history into a small, reusable, target-agnostic sketch and reserve full-resolution attention for a bounded recent window — is a template any production recommender facing the same "more history helps, but attention doesn't scale" tradeoff could adopt, independent of ByteDance's specific kernel and caching implementation. The paper was accepted as a long oral at RecSys'26's Industry Track.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A well-engineered production answer to a well-known scaling wall

Compressing long sequences into fixed-size summaries isn't itself new — memory-compression and hierarchical-attention ideas have circulated in both NLP and recsys literature — but doing it as a target-agnostic, cacheable sketch specifically so the *serving-time* cost stays flat as history length grows to 100K is a genuinely useful production-first contribution, and the reported 83%-of-the-gain-at-2%-of-the-cost tradeoff curve is the kind of concrete number other large-scale recommenders will want to replicate. The online A/B numbers (up to +8.6% Comment on Douyin Lite) are a strong existence proof that offline AUC gains at this scale translate into real engagement, though the -6.98% Dislike change on the main Douyin experiment is reported without much discussion of why the smaller Douyin Lite population didn't show a comparable Dislike shift.

### Similar / related work

- [**From Language to Behavior: Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs**](2026-09-09-bytedance-rest-sequence-transformer-ads-ranking.md) (in this bank) — a different ByteDance team's sequence-transformer work for ads ranking; both papers are ByteDance's parallel bets on how far sequence modeling can be pushed in production, one on architecture/rec-native design and this one specifically on the long-sequence compute wall.
- [**JourneyFormer: Encoding Airbnb Guest Journey with Sequence Modeling**](2026-09-06-airbnb-journeyformer-guest-sequence-search-ranking.md) (in this bank) — another industrial sequence model for user journeys, at a much shorter sequence-length regime than SequenceO1's 100K target, useful as a contrast in what "long" means across different product surfaces.
- [**TGR: Advancing Industrial Recommendation from Generative-Paradigm Ranking toward Unified Generation and Reasoning**](2026-09-09-tencent-tgr-unified-generation-reasoning-recsys.md) (in this bank) — Tencent's contemporaneous industrial recsys architecture push, part of the same 2026 wave of large Chinese platforms publishing production sequence/generative-ranking systems.

### Jargon buster

- **Sequential recommendation** — recommending based on the ordered sequence of a user's past interactions (what they watched/clicked/liked, in order), rather than treating past behavior as an unordered set.
- **Target-agnostic representation** — a summary of a user's history that doesn't depend on which specific candidate item is being scored, so it can be computed once and reused across many candidates instead of being recomputed for each one.
- **Cross-attention** — an attention mechanism where one sequence (here, the candidate item) attends to a different sequence (the user's history) to decide which parts of the history are relevant to that candidate.
- **AUC / UAUC** — Area Under the ROC Curve, a standard ranking-quality metric; "UAUC" is a user-level variant that averages AUC within each user before aggregating, which better reflects per-user ranking quality than a single pooled AUC.
