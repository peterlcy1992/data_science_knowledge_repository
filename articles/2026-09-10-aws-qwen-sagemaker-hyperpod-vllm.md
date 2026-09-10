---
id: aws-qwen-sagemaker-hyperpod-vllm
title: "Deploying Qwen3.8-2.4T-A95B on Amazon SageMaker HyperPod with vLLM"
source: "AWS Machine Learning Blog"
url: "https://aws.amazon.com/blogs/machine-learning/deploying-qwen3-8-2-4t-a95b-on-amazon-sagemaker-hyperpod-with-vllm/"
published: "2026-09"
added: "2026-09-10"
category: ml-infra-serving
tags: [llm-serving, vllm, sagemaker-hyperpod, mixture-of-experts, speculative-decoding, quantization, blackwell]
novelty: 3
sourced_via: "full-text fetch"
---

# Deploying Qwen3.8-2.4T-A95B on Amazon SageMaker HyperPod with vLLM

**Source:** [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/deploying-qwen3-8-2-4t-a95b-on-amazon-sagemaker-hyperpod-with-vllm/) · Published 2026-09 · Added 2026-09-10
**Category:** ML Infrastructure & Serving · **Tags:** `llm-serving`, `vllm`, `sagemaker-hyperpod`, `mixture-of-experts`, `speculative-decoding`, `quantization`, `blackwell`

## TL;DR

AWS walks through deploying Qwen3.8-2.4T-A95B — a 2.4-trillion-parameter, 95B-activated-parameter open-weight MoE model — on a single 8-GPU SageMaker HyperPod node using vLLM, NVFP4 quantization, and native multi-token-prediction speculative decoding. Combining tensor parallelism, expert parallelism, and MTP together cut time-to-first-token by ~59.7% and improved throughput ~12.6% over a bare tensor-parallel baseline.

## 1. Business context

Open-weight frontier-scale models keep growing past what a single accelerator, or even a single node's naive configuration, can serve efficiently. Qwen3.8-2.4T-A95B is large enough (2.4T total parameters) that hosting it isn't a matter of calling an API — it requires real infrastructure orchestration: picking the right instance type, quantizing the weights to fit in GPU memory, and tuning the serving stack's parallelism strategy. AWS positions this as a reference deployment for teams who need to self-host a model at this scale rather than consume it as a hosted API, on hardware and a serving stack (vLLM) that's become a de facto standard.

## 2. Technical details

**Model:** Qwen3.8-2.4T-A95B is a fine-grained Mixture-of-Experts model — 2.4T total parameters, 95B activated per token — with a hybrid attention design combining Gated DeltaNet (linear attention) layers with full-attention layers, a native 262K-token context window (extensible to 1M), and built-in reasoning, tool calling, and multi-token prediction (MTP) support.

**Hardware:** a single `ml.p6-b300.48xlarge` instance with 8 NVIDIA B300 Blackwell Ultra GPUs (2.1TB aggregate GPU memory), provisioned through AWS Flexible Training Plans, orchestrated via SageMaker HyperPod's Inference Operator on Amazon EKS.

**Serving stack:** vLLM with tensor parallelism across all 8 GPUs, NVFP4 (W4A4) quantization shrinking the weights to roughly 1.2TB, prefix caching for conversation efficiency, and native MTP speculative decoding with configurable draft-token counts, exposed via an OpenAI-compatible API with structured tool calling and separated reasoning output.

The post benchmarks four configurations — tensor parallelism (TP) alone, TP+MTP, TP+expert parallelism (TP+EP), and TP+EP+MTP — using 512 requests with 1,024 input/output tokens and 32 concurrent sequences.

## 3. Impact — potential & realized

**Realized:** relative to the TP-only baseline, TP+MTP cut time-to-first-token (TTFT) by 58.7% and improved throughput 6.2%, while contributing only modest latency gains. TP+EP alone gave smaller across-the-board improvements (-3.5% TTFT, +1.0% throughput). Combining all three (TP+EP+MTP) delivered the best results: -59.7% TTFT, -12.2% end-to-end latency, and +12.6% throughput. Initial model download and startup takes 15–30 minutes, with subsequent restarts substantially faster via NVMe caching.

**Potential:** the post frames MTP as the dominant lever for latency (specifically TTFT) at this scale, with EP contributing smaller, complementary throughput gains — a useful prioritization for any team tuning a similar MoE deployment, since it suggests where to spend tuning effort first.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid, well-measured reference deployment, not a new technique

Nothing here is conceptually new — NVFP4 quantization, tensor/expert parallelism, and MTP speculative decoding are all established techniques that AWS and NVIDIA have published on separately. What earns this a 3 rather than a 2 is the clean ablation across four configurations with consistent measurement, which makes it a genuinely useful reference for anyone standing up a similarly sized MoE model on Blackwell-class hardware — the kind of practical "here's what actually moves the needle and by how much" writeup that's more useful in practice than a novel technique with weaker evidence.

### Similar / related work

- [**Build a Physical AI Model Factory with NVIDIA Cosmos 3 on SageMaker HyperPod**](2026-09-10-aws-physical-ai-cosmos3-sagemaker-hyperpod.md) (in this bank) — another SageMaker HyperPod deployment writeup from the same AWS/NVIDIA partnership, useful to compare infrastructure patterns (shared persistent clusters vs. this post's single-node focus) across two different model families.
- [**3 Ways NVFP4 Accelerates AI Training and Inference**](https://developer.nvidia.com/blog/3-ways-nvfp4-accelerates-ai-training-and-inference/) — NVIDIA's own explainer on the NVFP4 quantization format this deployment relies on.
- [**Co-Designing AI Models Using Speculative Decoding for Faster LLM Inference**](https://developer.nvidia.com/blog/co-designing-ai-models-using-speculative-decoding-for-faster-llm-inference) — background on the speculative-decoding family of techniques that MTP belongs to.

### Jargon buster

- **Mixture of Experts (MoE)** — an architecture where only a subset of the model's total parameters ("experts") activate for any given token, letting total parameter count grow far larger than the compute cost per token would otherwise allow.
- **NVFP4 (W4A4) quantization** — representing both weights and activations in 4-bit floating point, roughly halving memory footprint versus 8-bit formats while aiming to preserve accuracy.
- **Multi-token prediction (MTP) speculative decoding** — a technique where the model proposes several tokens at once and a cheaper verification pass confirms them, reducing the number of expensive full forward passes needed per generated token.
- **Tensor vs. expert parallelism** — tensor parallelism splits individual matrix operations across GPUs; expert parallelism instead splits an MoE model's distinct experts across GPUs, routing each token to whichever GPU holds its selected expert.
