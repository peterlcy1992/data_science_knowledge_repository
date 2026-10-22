---
id: arxiv-onetrans-v2-unified-transformer-recsys
title: "OneTrans-V2: Unifying Retrieval, Pre-rank, and Fine-rank with One Transformer in Industrial Recommender"
source: "arXiv cs.IR (Cao et al.)"
url: "https://arxiv.org/abs/2609.28589"
published: "2026-09"
added: "2026-10-13"
category: personalization-recsys
tags: [unified-transformer, cascade-ranking, generative-retrieval, moe, distillation]
novelty: 4
sourced_via: "web search"
---

# OneTrans-V2: Unifying Retrieval, Pre-rank, and Fine-rank with One Transformer in Industrial Recommender

**Source:** [arXiv cs.IR (Cao et al.)](https://arxiv.org/abs/2609.28589) · Published 2026-09 · Added 2026-10-13
**Category:** personalization-recsys · **Tags:** `unified-transformer`, `cascade-ranking`, `generative-retrieval`, `moe`, `distillation`

## TL;DR

OneTrans-V2 keeps the retrieval → pre-rank → fine-rank cascade but serves all three stages from one Transformer that encodes a user's behaviour sequence once. The abstract reports +9.74% GMV in production and 3.2x the throughput of the separate per-stage models on the same hardware.

## 1. Business context

Industrial recommenders usually run a cascade of retrieval, pre-rank and fine-rank, each trained and served as a separate model. That repeats user-sequence encoding, isolates optimisation per stage and duplicates engineering. The bet is that one shared model removes the redundancy and lets stages improve each other.

## 2. Technical details

One Transformer covers all three stages. The user behaviour sequence is encoded once as shared context, while stage-specific candidate features and computation are kept. Stages are trained jointly, with in-model distillation from fine-rank to pre-rank. The backbone is scaled with sparse mixture-of-experts (bounded activated compute) and stabilised with μP-style parameterisation. For retrieval, Decision-Conditioned Generative Retrieval (DCGR) predicts a decision prefix describing the upcoming interaction and then generates items conditioned on it, so business objectives can steer one generative process. Sequence-Native Training (SNT) organises training around each user's lifelong sequence and amortises its encoding across exposures. A co-designed serving stack accompanies the model. Layer counts, expert configuration and ablations were not available from the abstract.

## 3. Impact — potential & realized

Realized (abstract): deployed across all three stages of a large-scale industrial system, +9.74% GMV, and 3.2x throughput versus the separate per-stage models under the same hardware budget. The abstract does not name the platform, the baseline or the A/B design, and no confidence intervals are given. Potential: fewer separately maintained models and a single place to inject business objectives.

*Sourced from web search / abstract-level content; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Serving the whole cascade from one model is a credible direction (shared-context batching and generative retrieval are both live trends), and the throughput claim is as interesting as the GMV claim.

Serving the whole cascade from one model is a credible direction (shared-context batching and generative retrieval are both live trends), and the throughput claim is as interesting as the GMV claim. But +9.74% GMV is a very large number reported without baseline or experiment details; read it as a claim until the full paper's A/B setup is checked. For DS practitioners the lesson is measurement: when stages are jointly trained, offline per-stage metrics stop being separable and online experimentation has to carry the evidence.

### Similar / related work

- [**Feed SR (LinkedIn)**](https://arxiv.org/abs/2602.12354) — another sequence-native industrial ranker

### Jargon buster

- **Cascade ranking** — Retrieval narrows millions of items to thousands, pre-rank to hundreds, fine-rank orders the final few; each stage is usually a separate model.
- **Mixture-of-experts (MoE)** — A model with many sub-networks of which only a few activate per input, adding capacity without proportional compute.
- **μP** — A parameterisation that lets hyperparameters tuned on small models transfer to larger ones, stabilising scaling.
