---
id: aws-physical-ai-cosmos3-sagemaker-hyperpod
title: "Build a Physical AI Model Factory with NVIDIA Cosmos 3 on SageMaker HyperPod"
source: "AWS Machine Learning Blog / NVIDIA"
url: "https://aws.amazon.com/blogs/machine-learning/build-a-physical-ai-model-factory-with-nvidia-cosmos-3-on-sagemaker-hyperpod/"
published: "2026"
added: "2026-09-10"
category: cv-multimodal
tags: [physical-ai, robotics, world-models, sagemaker-hyperpod, mixture-of-transformers, synthetic-data]
novelty: 4
sourced_via: "web search"
---

# Build a Physical AI Model Factory with NVIDIA Cosmos 3 on SageMaker HyperPod

**Source:** [AWS Machine Learning Blog / NVIDIA](https://aws.amazon.com/blogs/machine-learning/build-a-physical-ai-model-factory-with-nvidia-cosmos-3-on-sagemaker-hyperpod/) · Published 2026 · Added 2026-09-10
**Category:** Computer Vision & Multimodal · **Tags:** `physical-ai`, `robotics`, `world-models`, `sagemaker-hyperpod`, `mixture-of-transformers`, `synthetic-data`

## TL;DR

AWS and NVIDIA describe a reference architecture for running physical AI (robotics/autonomous-vehicle) model development as a continuous, closed-loop "model factory" — generating synthetic data, post-training, and evaluating in simulation — on a single shared SageMaker HyperPod cluster instead of fragmented per-stage GPU pools. The same Cosmos 3 checkpoint operates as a world model, an action-labeling model, or a deployed policy depending only on which tokens start as noise, and the post reports near-linear multi-node scaling efficiency (0.97–0.99 of linear) with roughly 1% checkpoint overhead.

## 1. Business context

Physical AI systems — robots, autonomous vehicles — don't get trained once and shipped; they need a perpetual improvement loop that ingests real-world data, generates synthetic variations to cover edge cases, post-trains updated models, and evaluates them in simulation before redeployment. The problem is that this pipeline traditionally gets fragmented across separate GPU clusters for each stage (data generation, training, evaluation), which creates expensive data movement between clusters and provisioning churn as demand shifts between stages. This post is a reference architecture for running the entire loop on one shared, persistent cluster instead.

## 2. Technical details

**NVIDIA Cosmos 3** is built around three architectural choices. A **unified token stream** carries all modalities — video, images, actions, audio, text — through a single sequence rather than separate per-modality pipelines. A **Mixture-of-Transformers (MoT)** design pairs two expert towers (a reasoner and a generator) joined by per-layer dual-stream attention, rather than bolting separately trained components together. And a **train-inference asymmetry** means training runs full denoising and video decoding, while a deployed policy runs only a handful of denoise steps and skips video decoding entirely for speed. Because of this design, the *same checkpoint* can operate in three modes purely by changing which tokens start as noise: as a **world model** (forward dynamics, generating synthetic video), as an **inverse-dynamics labeler** (auto-labeling unlabeled video with actions), or as a deployed **policy** (controlling a robot or vehicle).

Three model tiers are released: **Cosmos3-Nano** (16B parameters, built on an 8B Qwen3-VL backbone, fully fine-tuned for deployment), **Cosmos3-Super** (64B parameters, on a 32B Qwen3-VL backbone, adapted via rank-16 LoRA to preserve the teacher model while shifting toward specific domains), and **Cosmos3-Edge** (4B parameters, for on-device deployment).

The infrastructure runs on **SageMaker HyperPod with EKS**: rather than separate GPU pools per pipeline stage, one persistent Kubernetes cluster shares a single GPU node pool (`p5en.48xlarge`, 8x H200 GPUs each), unified FSx for Lustre storage with EFA low-latency interconnect, and Kubeflow PyTorchJob orchestration — enabling time-shared capacity across stages instead of dedicated, often-idle per-stage pools, which the post frames as maximizing "GPU goodput" (useful pipeline progress per reserved GPU-hour).

## 3. Impact — potential & realized

**Realized:** the post reports a reproducible "goodput methodology" rather than absolute leaderboard numbers. For the Cosmos3-Super LoRA workload on H200s, strong-scaling efficiency measured roughly 0.97–0.99 of linear from 1 to 4 nodes, with per-step time variance within about 3% across the node ladder. Model FLOPs Utilization (MFU) measured approximately 0.50 against H200 BF16 peak for the Super (64B) workload and approximately 0.24 for the lighter Nano vision workload. A checkpoint-interval optimization (via the Young/Daly formula) suggested roughly 40-minute intervals, yielding about 1% wall-clock overhead from checkpointing, and auto-resume bounds node-failure cost to at most one checkpoint interval of redone work plus reschedule latency.

**Potential:** the authors explicitly frame these as relative figures specific to their setup — reproducible in shape on comparable hardware, "not a leaderboard number" — and provide dashboard/methodology code so other teams can measure their own clusters the same way, which is arguably the most reusable part of the post for teams building similar physical-AI pipelines.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — The single-checkpoint, three-mode design is the genuinely new idea

The infrastructure pattern (one shared cluster instead of fragmented per-stage pools) is sound but incremental cluster-engineering practice. What's more novel is the Cosmos 3 model design itself: using the same checkpoint as world model, auto-labeler, and deployed policy purely by changing which tokens are noised is an elegant unification of three roles that are normally separate models trained separately. Combined with genuinely rigorous, reproducible scaling measurements (not just headline numbers), this earns a 4. It's not a 5 because Mixture-of-Transformers and token-stream unification both build on an active, fast-moving body of world-model and unified-multimodal-model research rather than starting from nothing.

### Similar / related work

- [**Deploying Qwen3.8-2.4T-A95B on Amazon SageMaker HyperPod with vLLM**](2026-09-10-aws-qwen-sagemaker-hyperpod-vllm.md) (in this bank) — another AWS/SageMaker HyperPod deployment writeup from the same week, useful to compare infrastructure patterns for a very different model family (a text/reasoning MoE model vs. Cosmos 3's multimodal world model).
- **NVIDIA Cosmos (prior generations)** — the world-model lineage Cosmos 3 extends; earlier Cosmos releases established the world-model-for-robotics premise this post builds a production factory around.
- **Qwen3-VL** — the vision-language backbone underlying both the Nano and Super Cosmos 3 tiers, adapted here for physical-AI roles rather than general multimodal chat.

### Jargon buster

- **World model** — a model trained to predict how an environment evolves (here, generating synthetic video of plausible futures), used to create training data and evaluate policies in simulation before real-world deployment.
- **Mixture-of-Transformers (MoT)** — an architecture with multiple specialized transformer "expert" towers connected by shared attention layers, rather than a single monolithic transformer or separately bolted-together models.
- **Model FLOPs Utilization (MFU)** — the fraction of a GPU's theoretical peak compute (FLOPs) actually used productively during training; higher MFU means less wasted compute capacity.
- **GPU goodput** — useful pipeline progress achieved per reserved GPU-hour, a metric that penalizes idle or misallocated GPU capacity even if raw utilization looks high.
