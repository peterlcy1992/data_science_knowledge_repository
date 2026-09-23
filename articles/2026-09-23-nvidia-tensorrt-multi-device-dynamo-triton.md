---
id: nvidia-tensorrt-multi-device-dynamo-triton
title: "Simplifying Model Serving Across Multiple GPUs with NVIDIA TensorRT Multi-Device Integration in NVIDIA Dynamo-Triton"
source: "NVIDIA Technical Blog"
url: "https://developer.nvidia.com/blog/simplifying-model-serving-across-multiple-gpus-with-nvidia-tensorrt-multi-device-integration-in-nvidia-dynamo-triton/"
published: "2026-09"
added: "2026-09-23"
category: ml-infra-serving
tags: [inference, multi-gpu, tensorrt, triton, video-generation, context-parallelism, nccl]
novelty: 3
sourced_via: "full-text fetch"
---

# Simplifying Model Serving Across Multiple GPUs with NVIDIA TensorRT Multi-Device Integration in NVIDIA Dynamo-Triton

**Source:** [NVIDIA Technical Blog](https://developer.nvidia.com/blog/simplifying-model-serving-across-multiple-gpus-with-nvidia-tensorrt-multi-device-integration-in-nvidia-dynamo-triton/) · Published 2026-09 · Added 2026-09-23
**Category:** ML Infrastructure & Serving · **Tags:** `inference`, `multi-gpu`, `tensorrt`, `triton`, `video-generation`, `context-parallelism`, `nccl`

## TL;DR

NVIDIA's TensorRT 11.0 can now compile a single network to run across multiple GPUs with NCCL-backed collectives baked directly into the plan, and Dynamo-Triton 26.07 exposes that as one `KIND_MODEL` instance behind a single gRPC endpoint. On an 8-GPU Cosmos 3 Nano video-generation workload, end-to-end latency drops from 156.6s to 34.2s (4.58x) with a 6.09x speedup on the core transformer RPC.

## 1. Business context

Generative media models (video generation in this case) increasingly exceed what a single GPU can hold or serve fast enough, but scaling inference across GPUs traditionally means either hand-rolled distributed-serving glue outside the inference engine, or giving up TensorRT's engine-level optimizations to use a more flexible-but-slower multi-GPU framework. For latency-sensitive generative workflows, both are costly: one adds engineering and operational surface area, the other leaves performance on the table. NVIDIA's integration targets teams who want TensorRT's compiled-kernel performance without writing their own multi-GPU orchestration layer.

## 2. Technical details

**TensorRT multi-device inference** (new in TensorRT 11.0) lets a single TensorRT network execute across multiple GPUs using NCCL-backed distributed collectives, with the collective communication operations compiled directly into the TensorRT plan alongside the compute graph — so distribution isn't a separate runtime layer bolted on afterward.

**Dynamo-Triton release 26.07** exposes this at the serving layer: a single `KIND_MODEL` instance can own multiple GPUs, create a per-rank TensorRT execution context, set up its own CUDA streams and NCCL communicators, and launch all ranks together for each incoming request — all behind one gRPC endpoint, so callers don't need to know the model is sharded. Enabling it is a configuration change (`enable_multi_device: "true"`, `multi_device_gpus: "0,1,2,3,4,5,6,7"`).

For the video-generation case study, the team used **Ulysses context parallelism**: rather than splitting the model's layers across GPUs, each GPU processes the full video-token sequence but only a subset of attention heads, with distributed-collective layers wrapped around standard attention (per request: 2 reduce-scatters + 108 all-to-alls + 1 all-gather) to redistribute activations between the sequence-parallel and head-parallel views. The workload partitioned 44,160 video tokens across up to eight GPUs this way.

## 3. Impact — potential & realized

Reported results on Cosmos 3 Nano video generation:

| GPUs | End-to-end latency | E2E speedup | Core RPC speedup |
|---|---|---|---|
| 1 (baseline) | 156.6 s | 1.00x | 1.00x |
| 2 | 88.0 s | 1.78x | 1.89x |
| 4 | 53.1 s | 2.95x | 3.43x |
| 8 | 34.2 s | 4.58x | 6.09x |

Scaling is sub-linear (4.58x on 8 GPUs, not 8x) — expected given communication overhead from the reduce-scatter/all-to-all/all-gather pattern — but the RPC-level 6.09x shows the core compute path scales better than the end-to-end number, implying non-parallelized overhead (setup, I/O) is an increasing share of latency at 8 GPUs. The realized win is a single-endpoint, config-driven path to multi-GPU serving without a bespoke distributed-inference stack; the broader potential is that any latency-bound generative model exceeding single-GPU capacity gets a supported scale-out path inside the existing TensorRT/Triton toolchain.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Productionizes known parallelism into the standard serving stack

Context/sequence parallelism (Ulysses-style) and NCCL collectives are established distributed-training techniques; the contribution here is compiling them into TensorRT's plan format and exposing multi-GPU model instances as a first-class, single-endpoint Triton concept rather than requiring a hand-built proxy layer. That's a meaningful production-engineering step — it moves multi-GPU serving from "custom infra project" to "config flag" — but it isn't a new algorithmic idea. Teams running large generative-media or long-context models on NVIDIA's stack are the most likely near-term adopters.

### Similar / related work

- [**How Full-Stack NIM Optimizations Deliver 2.5x More Users on Nemotron 3 Ultra**](2026-09-12-nvidia-nim-nemotron3-ultra-serving-optimization.md) (in this bank) — same NVIDIA serving-stack lineage, focused on single-model throughput optimization rather than multi-GPU scale-out.
- [**When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving**](2026-09-14-nvidia-epd-disaggregation-multimodal-serving.md) (in this bank) — another NVIDIA approach to splitting a serving workload across GPUs/stages, disaggregation by pipeline phase rather than by attention head.
- **DeepSpeed Ulysses** — Microsoft's original sequence-parallelism technique this case study's parallelization strategy is named after and modeled on, developed for long-context LLM training.

### Jargon buster

- **NCCL** — NVIDIA's library for fast collective communication (all-reduce, all-to-all, etc.) between GPUs, the standard low-level building block for any multi-GPU distributed workload.
- **Context/sequence parallelism** — splitting a single input sequence (here, video tokens) across GPUs by portion of the sequence or by attention head, so no single GPU needs to hold the full activation set, unlike splitting by model layer (pipeline parallelism).
- **KIND_MODEL instance (Triton)** — Triton's abstraction for a deployed model instance; letting one such instance span multiple GPUs (instead of one instance per GPU) is what allows a single gRPC endpoint to front a distributed model.
