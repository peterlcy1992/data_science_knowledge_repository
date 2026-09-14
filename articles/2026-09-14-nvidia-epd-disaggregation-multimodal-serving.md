---
id: nvidia-epd-disaggregation-multimodal-serving
title: "When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving"
source: "NVIDIA Technical Blog"
url: "https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/"
published: "2026-09"
added: "2026-09-14"
category: ml-infra-serving
tags: [multimodal-serving, disaggregated-inference, vision-transformer, nixl, gpu-scheduling, throughput-latency]
novelty: 4
sourced_via: "full-text fetch"
---

# When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving

**Source:** [NVIDIA Technical Blog](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/) · Published 2026-09 · Added 2026-09-14
**Category:** ML Infrastructure & Serving · **Tags:** `multimodal-serving`, `disaggregated-inference`, `vision-transformer`, `gpu-scheduling`

## TL;DR

Serving multimodal LLMs on a single worker forces vision encoding, text prefill, and decode to fight over the same GPU — a media-heavy request can stall its own text generation, and unrelated text-only requests get blocked behind someone else's image encoding. NVIDIA's encode-prefill-decode (EPD) disaggregation splits the vision encoder onto independently scalable workers, and the post gives concrete, workload-dependent guidance on when that split pays off (up to 93% TTFT reduction, 70% more goodput at the same SLO) versus when it doesn't help at all.

## 1. Business context

Multimodal LLM serving (image/video-in, text-out) has a structural bottleneck that pure-text serving doesn't: before the language model can even start its prefill pass, the model has to run every image or video frame through a vision transformer (ViT) encoder, which can take hundreds of milliseconds or longer for media-heavy requests. In a traditional "aggregated" serving setup, the encoder and the LLM's prefill/decode work all share the same GPU. That coupling means a request with many images delays its own prefill, contends for GPU cycles with concurrent prefill and decode work from other requests, and — worst of all for a mixed-traffic production endpoint — blocks unrelated text-only requests that don't need any vision processing at all behind someone else's encoding work. As multimodal features (image search, video understanding, document AI) become standard product surfaces, this contention becomes a direct tax on latency and cost for every request, whether or not it touches an image.

## 2. Technical details

EPD disaggregation separates the ViT encoding stage from the LLM's prefill-and-decode (PD) stages into independently scalable serving components, transferring the resulting vision embeddings between encoder workers and PD workers over NVIDIA's Inference Transfer Library (NIXL). The post lays out three deployable topologies and gives quantitative guidance on choosing between them:

- **Aggregated** — the baseline: one worker does everything.
- **Colocated encoder** — multiple encoder processes share the same GPUs as PD workers via CUDA MPS, on homogeneous clusters where adding dedicated encoder hardware isn't practical.
- **Disaggregated encoder** — dedicated, cheaper GPUs (e.g., RTX 6000D) run encoding while higher-end GPUs (e.g., GB200) are reserved purely for PD work, so expensive PD capacity is never spent on encoding.

The benchmarks show EPD is not a universal win — it's a workload-shape decision:

- **Where it wins big:** heavy visual load (many images or high-resolution video), short-to-medium output lengths, smaller/quantized/MoE models, and mixed text+multimodal traffic where decoupling stops one traffic type from blocking the other.
- **Where it doesn't help (or hurts):** long output sequences (decode dominates total latency, so the encoding savings are a rounding error), large dense models (ViT work becomes a negligible fraction of total compute), and low media load on already-homogeneous hardware (the disaggregation overhead exceeds the gain).

An additional finding: combining EPD with quantization compounds the benefit — in the colocated-encoder configuration, goodput rose from 1.78x to 2.64x when the LLM was quantized to NVFP4 while the vision encoder stayed in BF16, since the smaller LLM footprint leaves more headroom for encoder work sharing the same GPU.

## 3. Impact — potential & realized

**Realized (benchmarked by NVIDIA):**
- Heavy visual workload (10 images/request): **50–58%** TTFT reduction.
- Very heavy load (50 requests × 128 images): **92–93%** TTFT improvement.
- End-to-end latency at 10 images + 1,024 output tokens: **~1.5x** improvement.
- **70%** more traffic served at the same latency SLO (goodput).
- Mixed 50:50 text/image traffic: **42.2%** text TTFT reduction, **30.8%** image TTFT reduction.
- Colocated EPD + NVFP4 quantization: goodput **1.78x → 2.64x**.

**Potential:** As multimodal features spread from single-purpose demos into mixed-traffic production endpoints (a support bot that occasionally gets a screenshot, a search product that occasionally gets a photo), the ability to right-size and independently scale the vision-encoding tier — on cheaper hardware, without it stalling text-only traffic — becomes a direct cost and latency lever, provided teams actually check their workload against NVIDIA's "when it helps" criteria rather than applying it blindly.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A genuinely useful architectural pattern, with unusually honest guidance on its own limits

Disaggregating prefill from decode is now a fairly well-established idea in LLM serving; extending that same logic to split out the vision encoder is a natural but non-trivial next step, and the NIXL-based transfer mechanism is a real piece of engineering. What pushes this above a routine "we disaggregated X" post is the explicit, quantified decision framework for when *not* to use it — long-output, dense-model, low-media workloads get worse, not better. That kind of self-limiting honesty is rarer than the headline benchmark numbers and makes the post far more actionable for a team deciding whether to adopt it.

### Similar / related work

- [**How Full-Stack NIM Optimizations Deliver 2.5x More Users on Nemotron 3 Ultra**](2026-09-12-nvidia-nim-nemotron3-ultra-serving-optimization.md) (in this bank) — another NVIDIA serving-optimization post from the same week, focused on speculative decoding, KV cache, and tensor parallelism for a text LLM rather than multimodal encoding.
- [**Reduce LLM Latency with Prefix-Aware Routing on Amazon SageMaker Inference**](2026-09-14-aws-sagemaker-prefix-aware-routing-llm-latency.md) (in this bank) — a different lever (routing for cache reuse) on the same prefill-latency problem, published the same week.
- [**Video and Image Search in Amazon Bedrock Knowledge Base using Marengo 3.0**](https://aws.amazon.com/blogs/machine-learning/video-and-image-search-in-amazon-bedrock-knowledge-base-using-marengo-3-0/) — a concurrent example of exactly the mixed multimodal-traffic product surface EPD disaggregation is built to serve efficiently.

### Jargon buster

- **Vision transformer (ViT)** — The neural network component that turns image/video pixels into token-like embeddings a language model can consume, run as a distinct step before the LLM's own prefill.
- **Prefill vs. decode** — Prefill is the (parallelizable) pass that processes the entire input prompt at once; decode is the (sequential) loop that generates output tokens one at a time — they have very different GPU utilization profiles, which is why serving systems increasingly split them onto different hardware.
- **Goodput** — Throughput measured only over requests that meet a latency SLO, as opposed to raw throughput that ignores whether individual requests were too slow to be useful.
