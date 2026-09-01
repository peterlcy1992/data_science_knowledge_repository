---
id: shopify-gisting-context-compression
title: "Gisting: Compressing LLM Agent Context to Increase Throughput and Cut Cost"
source: "Shopify Engineering"
url: "https://shopify.engineering/gisting"
published: "2026-08"
added: "2026-09-01"
category: llm-genai
tags: [context-compression, knowledge-distillation, latency, throughput, inference-efficiency, agent]
novelty: 4
sourced_via: "full-text fetch"
---

# Gisting: Compressing LLM Agent Context to Increase Throughput and Cut Cost

**Source:** [Shopify Engineering](https://shopify.engineering/gisting) · Published 2026-08 · Added 2026-09-01
**Category:** LLMs & Generative AI · **Tags:** `context-compression`, `knowledge-distillation`, `latency`, `throughput`

## TL;DR

Shopify compresses Sidekick's roughly 6,000-token system prompt into about
1,500 learned "gist" tokens via knowledge distillation, swapping them in at
inference time in place of the full prompt. At 350 requests/minute on
identical hardware, median time-to-first-token dropped from 438ms to 354ms,
median end-to-end latency fell from 6.8s to 4.2s, and throughput rose from
20.2 to 23.4 QPS.

## 1. Business context

Sidekick's system prompt carries substantial instructions and tool
definitions. At production request volume, the fixed cost of processing that
prompt on every single call adds up — both in latency per request and in
aggregate compute cost across millions of requests. Shopify wanted to shrink
that fixed overhead without changing how the agent actually behaves.

## 2. Technical details

- **Gist tokens.** Knowledge distillation compresses the long system prompt
  into a short sequence of learned embeddings — "gist" tokens — trained so
  that the model's behavior when conditioned on the gist tokens mirrors its
  behavior when conditioned on the full original prompt.
- **Compression ratio.** The system prompt shrinks from roughly **6,000
  tokens to roughly 1,500 gist tokens**, a 4x reduction in what has to be
  processed on every request.
- **Deployment.** The gist tokens are swapped in at inference time in place
  of the real prompt text, with no other change to how Sidekick is served.

## 3. Impact — potential & realized

- **Realized:** at **350 requests/minute** on identical hardware — median
  time-to-first-token **438ms → 354ms** (-19%), median end-to-end latency
  **6.8s → 4.2s** (-38%), throughput **20.2 → 23.4 QPS**.
- **Potential:** applicable to any LLM agent carrying a large, mostly-static
  system or tool-definition prompt that gets paid for on every request.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a clean production measurement of a known technique

Compressing a long prompt into a small number of learned "gist" tokens isn't
a new research idea — it's a known technique in the prompt/context
compression literature. What's valuable here is a clean, concrete production
measurement of the latency and throughput payoff at a real agent's traffic
volume, which is comparatively rare to see reported with actual before/after
numbers. Not a 5 because the core method is an application of an existing
idea rather than a new one.

### Similar / related work

- [**Sidekick's Continual Learning Loop**](2026-09-01-shopify-sidekick-continual-learning-loop.md) (in this bank) — Shopify's
  companion piece; a different cost-reduction lever (quality-driven
  reinforcement learning against a calibrated judge) for the same
  underlying problem of expensive, high-traffic LLM agent serving.
- [**GEM Training: How Meta Doubled the Efficiency of Its LLM-Scale Ads
  Foundation Model**](2026-08-31-meta-gem-training-llm-scale-ads-efficiency.md) (in this bank) — a different flavor of production
  LLM efficiency work (training-time systems co-design rather than
  inference-time context compression).

### Jargon buster

- **Gist tokens** — a small number of learned embeddings trained to stand in
  for (compress) a much longer prompt while preserving its effect on model
  behavior.
- **Knowledge distillation** — training a smaller or cheaper representation
  to reproduce the behavior of a larger, more expensive one.
- **Time to first token (TTFT)** — the latency from when a request starts to
  when the model produces its first output token.
