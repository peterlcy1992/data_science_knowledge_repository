---
id: pinterest-near-linear-foundation-model-training
title: "Achieving Near-Linear Training Scalability for Pinterest's Foundation Models"
source: "Pinterest Engineering Blog"
url: "https://medium.com/pinterest-engineering/achieving-near-linear-training-scalability-for-pinterests-foundation-models-14d4f59fe6f6"
published: "2026-06"
added: "2026-09-22"
category: ml-infra-serving
tags: [distributed-training, foundation-models, embedding-tables, gpu-networking, 2d-parallelism]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Achieving Near-Linear Training Scalability for Pinterest's Foundation Models

**Source:** [Pinterest Engineering Blog](https://medium.com/pinterest-engineering/achieving-near-linear-training-scalability-for-pinterests-foundation-models-14d4f59fe6f6) · Published 2026-06 · Added 2026-09-22
**Category:** ML Infrastructure & Serving · **Tags:** `distributed-training`, `foundation-models`, `embedding-tables`, `gpu-networking`, `2d-parallelism`

## TL;DR

Pinterest's multi-node training of its recommendation foundation models started out badly sub-linear — adding a second node barely helped — because most of the wall-clock time was going to cross-node embedding-table communication, not compute. By profiling the bottleneck down to bytes-on-the-wire and redesigning the parallelism topology so expensive embedding traffic stays inside a node (a "2D Parallel" scheme), they drove scaling from that poor starting point up to roughly 7.5x at 8 nodes — close to the 8x that perfectly linear scaling would give.

## 1. Business context

Training larger foundation models for recommendation faster is directly a cost and iteration-speed problem: if adding more GPU nodes to a training job doesn't proportionally speed it up, teams either eat the extra cost for diminishing returns or cap how large/fast their training runs can be. Pinterest's initial multi-node training exhibited exactly that failure — scaling was far from linear, meaning additional hardware wasn't buying proportional additional throughput. Fixing that unlocks faster iteration on foundation models without a corresponding blowup in training cost per improvement.

## 2. Technical details

The team's starting point, profiling single-node and two-node training traces, identified **distributed embedding communication** as the root cause: Pinterest's foundation models rely on large embedding tables that, in a naive multi-node setup, get sharded across *all* GPUs in the cluster, meaning every training step requires an all-to-all exchange of embedding data across node boundaries — expensive, high-latency cross-node network traffic that dominated wall-clock time and choked scaling.

The fix, applied as a sequence of optimization passes rather than one big rewrite, followed a consistent framework: **profile the actual bottleneck → reduce bytes on the wire → reshape payloads to fit bandwidth constraints → redesign topology to keep expensive traffic local.** Concretely:

- **2D Parallel topology.** Instead of sharding embedding tables across every GPU in the cluster, GPUs are divided into groups (typically one group per node); tables are sharded across the GPUs *within* a group, and each group holds a full model replica. This confines the expensive embedding all-to-all exchange to intra-node NVLink traffic, with only lightweight synchronization needing to cross the network between nodes.
- **Payload and communication-overlap optimizations.** Reducing embedding payload size/shape and starting communication operations concurrently rather than serially cut measured per-step communication wall time substantially (the team reports the relevant communication phase dropping from roughly 25.68ms to 16.98ms in their profiling).
- **Iterative validation.** Each optimization pass was measured against actual multi-node scaling factors rather than assumed, with the team reporting successive passes lifting scaling from a poor starting point through intermediate stages and ultimately to **~7.5x at 8 nodes** — Pinterest doesn't claim the intermediate per-stage numbers precisely track a single clean progression, but the overall trajectory is a large, staged improvement from a badly sub-linear starting point toward near-linear scaling.

A stated design goal throughout was **hardware-agnosticism**: because the fixes remove cross-node traffic structurally (via topology redesign) rather than relying on faster interconnects to paper over the same traffic pattern, the approach is meant to transfer directly to future hardware generations rather than needing to be re-derived each time.

## 3. Impact — potential & realized

**Realized:** Pinterest reports reaching **~7.5x scaling at 8 nodes**, up from a starting point the team describes as roughly 0.2x-scale-factor territory — i.e., adding nodes initially bought almost none of the expected additional throughput, and the fixes closed most of that gap toward the 8x a perfectly linear system would deliver.

**Potential:** the general framework — profile to find the real bottleneck (often communication, not compute, in embedding-heavy models), then attack bytes-on-the-wire, payload shape, and topology in that order — is reusable well beyond Pinterest's specific models, for any team training large embedding-table-heavy recommendation or foundation models across multiple nodes. The hardware-agnostic framing also means the fix is meant to keep paying off as Pinterest moves to newer GPU/networking generations rather than needing to be redone.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — excellent systematic engineering on a well-known bottleneck class

Cross-node embedding all-to-all being the dominant cost in distributed recommendation-model training, and 2D/hybrid parallelism schemes to localize that traffic, are known patterns in the large-scale recommendation systems literature — this isn't a new algorithmic idea. What makes the write-up worth having in the bank is the discipline of the diagnosis-first methodology (profile before optimizing) and the demonstrated end-to-end payoff at real fleet scale (0.2x-ish to ~7.5x at 8 nodes), which is a useful concrete data point and template for any team hitting the same "adding nodes doesn't help" wall in their own embedding-heavy training jobs.

### Similar / related work

- [**Evolving Pinterest's Embedding Retrieval Platform**](2026-09-15-pinterest-evolving-embedding-retrieval-platform.md) (in this bank) — a related Pinterest infrastructure investment in the same embedding-heavy systems space, though focused on serving/retrieval rather than training.
- Two-dimensional and hybrid sparse-parallelism approaches for large-scale recommendation model training (an active area in industrial ML-systems research covering embedding-table sharding strategies) — broad prior art in the same problem space; left unlinked as a general body of work rather than one specific paper.
- [**Balancing Multiple Objectives in Generative Recommendations with Adaptive Decoding**](2026-08-31-spotify-adaptive-decoding-multiobjective-generative-recsys.md) (in this bank) — a different production recommendation-systems scaling problem (serving-time decoding) at another company, illustrative of the same broader theme of squeezing more out of large model infrastructure.

### Jargon buster

- **All-to-all communication** — a network communication pattern where every participant (GPU, in this case) must send data to and receive data from every other participant; expensive because its cost grows with cluster size and it saturates network bandwidth if not carefully managed.
- **NVLink** — NVIDIA's high-bandwidth, low-latency interconnect between GPUs within the same physical server/node, dramatically faster than typical cross-node networking — which is why keeping embedding traffic "intra-node" (over NVLink) rather than "inter-node" is the key lever here.
- **2D Parallel (in this context)** — a training-parallelism scheme that groups GPUs (e.g., one group per node) and shards data two ways: within a group for expensive local traffic, and across groups only for lightweight synchronization, as opposed to naively sharding everything across the entire cluster.
- **Near-linear scaling** — a measure of distributed-training efficiency: if adding N times more GPUs makes training close to N times faster, scaling is "near-linear"; a scaling factor far below the node count (like Pinterest's poor starting point) means most of the added hardware isn't contributing proportional speedup.
