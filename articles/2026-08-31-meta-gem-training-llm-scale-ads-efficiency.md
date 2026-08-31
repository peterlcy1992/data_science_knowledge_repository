---
id: meta-gem-training-llm-scale-ads-efficiency
title: "GEM Training: How Meta Doubled the Efficiency of Its LLM-Scale Ads Foundation Model"
source: "Engineering at Meta"
url: "https://engineering.fb.com/2026/08/03/ml-applications/training-gem-at-llm-scale-meta-ads-recommendation-foundation-model/"
published: "2026-08"
added: "2026-08-31"
category: llm-genai
tags: [foundation-model, ads, training-efficiency, mfu, parallelism, mixed-precision, kernels, gpu]
novelty: 4
sourced_via: "web search"
---

# GEM Training: How Meta Doubled the Efficiency of Its LLM-Scale Ads Foundation Model

**Source:** [Engineering at Meta](https://engineering.fb.com/2026/08/03/ml-applications/training-gem-at-llm-scale-meta-ads-recommendation-foundation-model/) · Published 2026-08 · Added 2026-08-31
**Category:** LLMs & Generative AI · **Tags:** `foundation-model`, `ads`, `training-efficiency`, `mfu`, `parallelism`

## TL;DR

Meta describes how it trains **GEM** (its Generative Ads Recommendation Model,
the foundation model behind ads ranking across Instagram and Facebook) at
LLM scale on thousands of GPUs. By co-designing custom kernels, mixed
ultra-low precision, and topology-aware parallelism, Meta **doubled
end-to-end training efficiency to 20–25% Model FLOPs Utilization (MFU) while
scaling total training FLOPs 4x** over twelve months.

## 1. Business context

GEM is the foundation model Meta positions as the "central brain" behind ads
recommendation — a single hybrid model, trained once and adapted downstream,
replacing narrower task-specific ranking models. Training it well is
expensive: unlike a typical LLM, GEM combines **trillions of sparse embedding
parameters** (one per ad/user/context feature) with **billions of dense
parameters**, and is trained on a mix of **sequence features** (user activity
history) and **non-sequence features** (location, ad creative
representation). As Meta scaled GEM's training compute toward LLM-class
budgets, keeping GPU utilization high — rather than leaving expensive
clusters idle waiting on memory, communication, or precision bottlenecks —
became the binding cost constraint.

## 2. Technical details

- **Hybrid architecture at LLM scale.** GEM blends sparse embedding tables
  (trillions of parameters) with a dense LLM-style backbone (billions of
  parameters), trained on several thousand of the latest-generation GPUs.
- **Custom recommendation kernels.** Meta built **Jagged Flash Attention**,
  **Generalized Dot-Product Attention**, and **BlockAttention** — attention
  kernels adapted to recommendation's ragged, variable-length sequence
  features rather than the fixed-length sequences typical LLM kernels assume.
- **Mixed ultra-low precision.** Training uses **MXFP8** (a microscaled 8-bit
  floating point format) to cut memory and compute cost while preserving
  training stability.
- **Topology-aware 5D parallelism.** Model, data, and communication are
  partitioned across five parallelism dimensions, tuned to the physical GPU
  cluster topology so that inter-GPU communication follows fast network
  paths rather than crossing slower links.
- **Co-design, not point fixes.** The efficiency gains came from optimizing
  kernels, precision, parallelism, networking, and memory **together** rather
  than independently — a change in one (e.g., precision) reshapes what's
  optimal in another (e.g., parallelism layout).

## 3. Impact — potential & realized

- **Realized:** end-to-end training efficiency doubled to **20–25% MFU**
  while total training FLOPs scaled **4x** over the prior twelve months —
  i.e., Meta trained a much bigger model on much more compute without a
  proportional cost increase.
- **Realized (product):** Meta reports GEM driving **5% conversion increases
  on Instagram and 3% on Facebook** (per the broader GEM initiative this
  training work supports).
- **Potential:** the kernel/precision/parallelism co-design recipe is a
  template for any org merging LLM-style dense backbones with
  recommendation-style sparse embeddings — a combination standard LLM
  training stacks aren't built for.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — genuinely hard systems co-design, reported with real numbers

Recommendation models with huge sparse embedding tables and LLMs with dense
transformer backbones have historically been trained on different stacks
with different bottlenecks. Merging them and reporting a concrete **20–25%
MFU at 4x more FLOPs** is a specific, verifiable systems result rather than a
qualitative claim. It lands at 4 rather than 5 because the individual
techniques (FlashAttention variants, FP8 training, multi-dimensional
parallelism) are each established in the broader LLM-training literature —
the contribution here is adapting and co-designing them for recommendation's
ragged, embedding-heavy workload at this scale.

### Similar / related work

- [**Scaling LLM Post-Training at Netflix**](2026-08-30-netflix-scaling-llm-post-training.md) (in this bank) — a different
  production ML org's take on training-infrastructure efficiency (sequence
  packing rather than precision/parallelism co-design), for a different
  training stage.
- [**Towards Generalizable and Efficient Large-Scale Generative Recommenders**](https://arxiv.org/abs/2605.23312) — Netflix's own
  study of scaling a generative recommender backbone from 2M to 1B
  parameters, a close research parallel to GEM's scale-up.
- **Meta's earlier GEM introduction** ("Meta's Generative Ads Model: The
  Central Brain Accelerating Ads Recommendation AI Innovation," Engineering
  at Meta, Nov 2025) — the model-architecture piece this training post
  complements.

### Jargon buster

- **MFU (Model FLOPs Utilization)** — the fraction of a GPU cluster's
  theoretical peak compute that training actually achieves; higher is more
  efficient. LLM training commonly runs 30-50%+ MFU, so 20-25% for a
  sparse+dense hybrid is a meaningful jump from a harder starting point.
- **MXFP8** — a microscaled 8-bit floating-point number format that packs
  more values per byte than standard 16/32-bit formats, cutting memory and
  bandwidth needs at some precision cost, managed carefully to avoid
  destabilizing training.
- **Sparse embedding parameters** — one learned vector per discrete feature
  value (e.g., per ad ID or user ID); these tables can hold trillions of
  parameters but only a tiny slice is touched per training example, unlike
  a dense LLM backbone where every parameter is used on every forward pass.
- **5D parallelism** — splitting a training job across five different axes
  (e.g., data, tensor, pipeline, expert, and sequence dimensions) so no
  single GPU has to hold the whole model or the whole batch.
