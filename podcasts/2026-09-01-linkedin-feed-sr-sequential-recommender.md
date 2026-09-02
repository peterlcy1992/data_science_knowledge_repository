# Episode 1 — LinkedIn: A Transformer That Ranks Your Feed

- **Show:** [Data Science in the Wild](SHOW.md)
- **Company:** LinkedIn
- **Audio:** [`2026-09-01-linkedin-feed-sr-sequential-recommender.m4a`](2026-09-01-linkedin-feed-sr-sequential-recommender.m4a)
- **Cover:** [`2026-09-01-linkedin-feed-sr-sequential-recommender.cover.png`](2026-09-01-linkedin-feed-sr-sequential-recommender.cover.png)
- **Source article:** [`../articles/2026-09-01-linkedin-feed-sr-sequential-recommender.md`](../articles/2026-09-01-linkedin-feed-sr-sequential-recommender.md)

## Title

**LinkedIn — A Transformer That Ranks Your Feed (Feed SR)**

## Description

A deep dive into how LinkedIn replaced its DCNv2 feed ranker with **Feed SR** —
a decoder-only transformer that reads up to **1,000 of a member's past
impressions** as an ordered sequence, served on a disaggregated CPU/GPU stack
with custom kernels. We cover the business context (a 1.2B-member feed whose
legacy ranker couldn't model history as a sequence), the technical approach
(RoPE positional embeddings, a parallel-DCNv2 scoring head, shared-context
batching, and a custom flash-attention CUDA kernel), the honest negative
results (why a fine-tuned LLM-ranker and a TransAct-style encoder were tried
and rejected), and the realized impact: **+2.10% time spent** and **+3.52%
social actions** in a production A/B test — at roughly **0.7× the inference
energy** of the CPU-served incumbent despite being a larger model.

Based on the "An Industrial-Scale Sequential Recommender for LinkedIn Feed
Ranking (Feed SR)" write-up in the Data Science Cutting-Edge Knowledge Bank.
