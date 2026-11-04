---
id: linkedin-from-generation-to-scoring-llm-semantic-labeling
title: "From Generation to Scoring: Scaling LLM-Based Semantic Labeling at LinkedIn"
source: "arXiv cs.LG (LinkedIn)"
url: "https://arxiv.org/abs/2610.36383"
published: "2026-10"
added: "2026-11-04"
category: ml-infra-serving
tags: [llm-labeling, multiple-item-scoring, batch-inference, sglang, ray-data, linkedin]
novelty: 3
sourced_via: "full-text fetch"
---

# From Generation to Scoring: Scaling LLM-Based Semantic Labeling at LinkedIn

**Source:** [arXiv cs.LG (LinkedIn)](https://arxiv.org/abs/2610.36383) · Published 2026-10 · Added 2026-11-04
**Category:** ml-infra-serving · **Tags:** `llm-labeling`, `multiple-item-scoring`, `batch-inference`, `sglang`, `ray-data`, `linkedin`

## TL;DR

LinkedIn's profile-qualification labeler packed many candidate labels into one prompt and generated a yes/no list, coupling independent decisions. The paper reformulates it as semantic scoring - one answer-token score per profile-qualification pair from a prefill-only pass - and uses Multiple-Item Scoring (MIS) to score hundreds of candidates in one masked sequence. Reordering changes at most 0.01% of decisions, and the MIS stack raises serving throughput 1.9x under a one-second p99 target.

## 1. Business context

LinkedIn's qualification labeling identifies which skills, experience, education and licenses from a catalog are supported by a member's profile; labeling runs in offline batch inference and on a streaming path for profile changes, and downstream matching and ranking reuse the stored predictions. Each prediction should depend only on its profile-qualification pair. The existing LLM labeler used packed generation, a form of batch prompting that shares the profile encoding but makes each answer depend on the other qualifications and on earlier answers, spends decoding on the list, and relies on the list being well-formed.

## 2. Technical details

Reformulation as semantic scoring: each judgment is pointwise ranking, fine-tuned on single-candidate prompts to return its decision as one answer-token score from a prefill-only pass. Scoring one candidate per request keeps decisions independent but repeats the long profile in every request (about 90 labels/s in serving vs 2.5K for packed generation, per the paper). Multiple-Item Scoring (from the authors' prior work on online LLM ranking) scores hundreds of candidates in one sequence with attention masked between candidates, so the profile is encoded once. Engineering: for offline batch inference, MIS scoring is a reusable, model-agnostic Ray Data API (proposed upstream); for serving, MIS support was contributed to SGLang.

## 3. Impact — potential & realized

Realized (per the paper, deployed for profile qualification labeling): semantic scoring changes at most 0.01% of decisions when candidates are reordered; it matches the agreement with reference labels that packed generation reaches only with about 4.7x as many training pairs; the MIS-based stack raises throughput over the deployed stack by 1.24x offline and 1.9x in model serving under a one-second p99 latency target. Potential: the same pattern applies to other one-entity-many-candidates labeling or judging workloads; the paper scopes out the catalog and downstream models.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Independent scoring instead of list generation; good engineering, modest novelty

A solid production-engineering paper whose main idea - make independent decisions structurally independent - is sensible and verified by a reorder-invariance number. It is mostly an infra/efficiency story with less direct data-science content, and the speedups are relative to LinkedIn's own deployed stack.

### Similar / related work

- Multiple-Item Scoring for online LLM ranking (Li et al., 2026; Borisyuk et al., 2026) - the authors' prior work that this builds on; not in this bank
- [Statistical Detection of Positional Bias in LLM-Based Recommender Systems](2026-11-04-arxiv-statistical-detection-positional-bias-llm-recommender.md) (in this bank) - the order-dependence problem that independent scoring removes by design

### Jargon buster

- **Packed generation** — Putting many candidate labels in one prompt and having the LLM generate an answer list.
- **Prefill-only pass** — Reading the prompt once to produce a score, with no token-by-token generation.
- **Multiple-Item Scoring** — Scoring many candidates in one sequence with attention masked so candidates cannot see each other.
- **p99 latency** — The latency below which 99% of requests complete.
