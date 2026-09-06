---
id: nvidia-speculative-decoding-model-codesign
title: "Co-Designing AI Models Using Speculative Decoding for Faster LLM Inference"
source: "NVIDIA Technical Blog"
url: "https://developer.nvidia.com/blog/co-designing-ai-models-using-speculative-decoding-for-faster-llm-inference/"
published: "2026-09"
added: "2026-09-06"
category: ml-infra-serving
tags: [speculative-decoding, llm-inference, draft-models, eagle, mtp, throughput-latency, benchmarking]
novelty: 4
sourced_via: "full-text fetch"
---

# Co-Designing AI Models Using Speculative Decoding for Faster LLM Inference

**Source:** [NVIDIA Technical Blog](https://developer.nvidia.com/blog/co-designing-ai-models-using-speculative-decoding-for-faster-llm-inference/) · Published 2026-09 · Added 2026-09-06
**Category:** ML Infrastructure & Serving · **Tags:** `speculative-decoding`, `llm-inference`, `draft-models`, `eagle`, `mtp`, `throughput-latency`, `benchmarking`

## TL;DR

NVIDIA lays out concrete, quantitative guidelines for choosing and tuning a speculative-decoding draft mechanism (external draft models, EAGLE-3, MTP, DFlash, DSpark, or n-gram methods) for a given target LLM and latency budget, backed by benchmarks on SPEED-Bench with Qwen 3.5 122B as the target model — including a formula for the ideal draft length given a model's attention-head ratio.

## 1. Business context

Autoregressive LLM decoding generates one token per forward pass, which under-utilizes GPU compute at low batch sizes because each pass is memory-bandwidth-bound rather than compute-bound. Speculative decoding — verifying several candidate tokens per pass instead of generating one — is now a standard lever for cutting inference latency and cost, but production teams face a genuinely hard choice: which draft mechanism to use, and how long a draft to generate, given a specific target model, hardware, and operating point on the throughput-latency curve. Picking wrong wastes GPU cycles on draft generation that doesn't pay off, or leaves easy wins on the table.

## 2. Technical details

Speculative decoding's two-stage process: a small "draft" model proposes several likely next tokens, and the large target model verifies them all in a single parallel forward pass, accepting the longest correct prefix. This raises arithmetic intensity per pass, letting GEMMs reach compute saturation at lower batch sizes than plain autoregressive decoding would need.

NVIDIA compares six draft-generation mechanisms directly against each other on cost, training data requirements, and achieved acceptance length (AL — how many draft tokens are typically accepted per verification round):

1. **External draft models** — independent, smaller LLMs (e.g., Qwen 3.5 35B or 4B drafting for Qwen 3.5 122B), needing 100B–10T+ training tokens but reaching the highest acceptance lengths (AL of 6 at draft length D=9 for the 35B draft; the 4B draft still exceeded AL of 5).
2. **EAGLE-3** — extra decoder layers with a linear projection layer, trained on 1–10B tokens, cheaper to build than a full external model.
3. **MTP (Multi-Token Prediction)** — co-trained with the target model and shipped inside its checkpoint, but generates draft tokens serially (D steps), and its acceptance rate plateaus earlier than external drafts.
4. **DFlash** — generates all D draft tokens in one parallel pass via KV-cache fusion rather than MTP's serial loop, cutting draft-generation overhead.
5. **DSpark** — a DFlash variant with an added Markov-correction head.
6. **Suffix/n-gram matching** — a training-free, pattern-matching approach with no acceptance-length ceiling from a model but weaker guarantees.

From these comparisons the article distills five concrete guidelines: (1) increase draft length to push the verification GEMM into a compute-bound region without inflating KV-cache pressure; (2) when attention cost dominates, set draft length D = 128/G − 1, where G is the number of query heads sharing each KV head (i.e., the grouped-query-attention ratio); (3) align draft lengths to the 128-token tile boundaries used by attention kernels to avoid wasted computation; (4) at very low latency budgets, only grow draft length if the resulting acceptance-length gain outweighs the added draft cost; (5) choose the draft mechanism itself by weighing acceptance length against draft overhead, training cost, and deployment complexity — there is no universally best choice.

## 3. Impact — potential & realized

**Realized:** On SPEED-Bench with Qwen 3.5 122B as target, external draft models (Qwen 3.5 35B and 4B) achieved the highest measured acceptance lengths (AL ≥ 5–6), while MTP and DFlash plateaued at lower AL but with far cheaper training (MTP ships with the base checkpoint; DFlash needs only 1–10B tokens). DFlash's one-shot parallel generation of D tokens (versus MTP's D serial steps) measurably reduces per-round draft overhead.

**Potential:** The D = 128/G − 1 formula and the tile-alignment guideline generalize beyond the specific models benchmarked — any team running speculative decoding on GQA-based LLMs can compute an initial draft-length target directly from their model's head configuration rather than empirically sweeping it from scratch. The mechanism-selection framework (acceptance length vs. training cost vs. deployment complexity) is a reusable decision tree for teams choosing between "buy" (external draft model), "build lightly" (EAGLE-3/DFlash), or "free" (MTP/n-gram) options.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A practical systems study, not a new algorithm

None of the six draft mechanisms is new to this article — EAGLE, MTP, and n-gram speculative decoding are all established techniques. What's genuinely useful is the head-to-head, apples-to-apples comparison plus the closed-form draft-length formula tied to a model's GQA ratio and attention-kernel tiling. That's the kind of "production-first" contribution that saves teams weeks of empirical tuning, even though it doesn't introduce a new speculative-decoding algorithm.

### Similar / related work

- [**Achieving Extreme Efficiency through Specialized GPU Kernel Generation**](2026-09-05-databricks-proteus-gpu-kernel-generation.md) (in this bank) — a complementary inference-optimization story: Databricks' Proteus targets kernel-level GPU efficiency, while this NVIDIA piece targets the decoding algorithm itself; the two levers compose.
- [**Meta Adaptive Ranking Model: Bending the Inference Scaling Curve for LLM-Scale Ads**](2026-09-05-meta-adaptive-ranking-model-inference-scaling.md) (in this bank) — another "make LLM-scale inference cheap in production" story, focused on quantization and routing rather than speculative decoding.
- **EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test** — the underlying method behind one of the six compared draft mechanisms; no single canonical arXiv id is cited in the source article, so left unlinked here.

### Jargon buster

- **Acceptance length (AL)** — the average number of draft tokens the target model actually confirms as correct per verification round; higher AL means fewer expensive target-model passes per generated token.
- **Grouped-query attention (GQA)** — an attention variant where multiple query heads share a single key/value head, reducing KV-cache memory at some cost to modeling capacity; the ratio of query heads to KV heads (G) directly affects how compute-bound a given draft length is.
- **GEMM** — General Matrix Multiply, the core compute primitive of transformer inference; whether a GEMM is "compute-bound" or "memory-bound" determines whether adding more parallel work (like verifying a longer draft) is nearly free or genuinely costly.
