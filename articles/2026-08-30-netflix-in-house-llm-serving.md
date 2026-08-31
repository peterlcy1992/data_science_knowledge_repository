---
id: netflix-in-house-llm-serving
title: "In-House LLM Serving at Netflix (vLLM + Triton)"
source: "Netflix Tech Blog"
url: "https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c"
published: "2026-07"
added: "2026-08-30"
category: ml-infra-serving
tags: [llm-serving, vllm, triton, inference, grpc, constrained-decoding, gpu, mlops]
novelty: 3
sourced_via: "web search"
---

# In-House LLM Serving at Netflix (vLLM + Triton)

**Source:** [Netflix Tech Blog](https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c) · Published 2026-07 · Added 2026-08-30
**Category:** ML Infrastructure & Serving · **Tags:** `llm-serving`, `vllm`, `triton`, `constrained-decoding`

## TL;DR

Netflix's AI Platform Model Runtime team built an in-house LLM serving stack on
**vLLM** and **NVIDIA Triton**, integrated into its existing JVM production
serving layer via unified **gRPC and OpenAI-compatible APIs**. The post is a
candid tour of production concerns — model packaging, version compatibility,
zero-downtime deploys, observability, and scaling **constrained decoding** — and
of why they migrated off TensorRT-LLM once open engines closed the gap.

## 1. Business context

Netflix increasingly runs LLM-shaped workloads inside its own recommendation,
personalization, and search systems, where low latency, deep customization, and
tight integration with existing infra matter more than the convenience of a
hosted API. Self-hosting gives control over model architectures, decoding logic,
and cost, and keeps inference inside the same production environment the rest of
the stack lives in — rather than a separate ML silo. The trade-off is that
Netflix now owns the hard operational parts (packaging, upgrades, GPU
scheduling, reliability) itself.

## 2. Technical details

- **Engine choice.** The platform originally ran on **TensorRT-LLM**. By summer
  2025, open-source engines had largely closed the performance gap, and the
  workload mix had broadened (embedding generation, **prefill-only** inference
  for ranking/retrieval, autoregressive decoding, and custom models). Netflix
  made **vLLM** the paved-path engine, valuing its ability to load custom
  architectures without a multi-step compilation pipeline and its hooks for
  custom decoding.
- **Two-tier execution.** The platform builds on Netflix's existing **JVM-based
  serving layer**, which still handles routing, feature retrieval, candidate
  generation, post-processing, and logging. Smaller models run **in-process on
  CPUs**; larger requests are delegated to **MSS (Model Serving Service)**, where
  **Triton** takes over model loading, dynamic batching, and GPU scheduling.
- **Unified API surface.** Serving is exposed through unified **gRPC** and
  **OpenAI-compatible** APIs, so callers hit one contract regardless of where a
  model runs.
- **Production hardening.** The write-up details model packaging workflows,
  version-compatibility handling, **zero-downtime deployments**, and
  observability, plus scaling **constrained decoding** by moving the bottleneck
  off the critical serving path.

## 3. Impact — potential & realized

- **Realized:** a single paved-path serving platform spanning embeddings,
  prefill-only ranking inference, and full autoregressive generation, integrated
  with the existing serving layer.
- **Realized (operational):** unified APIs and zero-downtime deploys reduce the
  cost of shipping and upgrading self-hosted models.
- **Potential:** a template for other large orgs weighing self-hosting vs. hosted
  APIs — the post reads as a decision framework as much as an architecture.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — best-in-class execution of a now-standard stack

vLLM + Triton behind an OpenAI-compatible gateway is, by mid-2026, the
mainstream way to self-host. The value here isn't a new technique; it's the
honest operational detail (why they left TensorRT-LLM, how they split CPU
in-process vs. GPU-delegated work, how constrained decoding scales) that teams
rarely publish. That's genuinely useful, but it's consolidation of known
practice rather than a step change — hence a 3.

### Similar / related work

- **Scaling LLM Post-Training at Netflix** (in this bank) — the training-side
  companion; both lean on vLLM and Ray.
- **GenRec** (in this bank) — a consumer of exactly this serving path for
  LLM-native ranking.
- **NVIDIA Triton / vLLM docs and case studies** — the reference implementations
  of the components Netflix assembled.

### Jargon buster

- **vLLM** — an open-source LLM inference engine known for high throughput via
  **PagedAttention**, which manages the KV cache like virtual memory pages.
- **Triton (NVIDIA Triton Inference Server)** — a serving system that handles
  model loading, request batching, and GPU scheduling for many model types.
- **Constrained decoding** — forcing an LLM's output to obey a structure (valid
  JSON, a known schema, a fixed vocabulary) during generation.
- **Prefill-only inference** — running just the "read the prompt" phase to produce
  hidden states/embeddings, without generating tokens; useful for ranking and
  retrieval.
- **KV cache** — stored key/value tensors from earlier tokens so the model
  doesn't recompute them for each new token; the main memory cost of generation.
- **Paved path** — an internal-platform term for the supported, opinionated
  default way to do something.
