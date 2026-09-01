---
id: deepmind-double-blind-ai-evaluations
title: "Piloting the World's First Double-Blind AI Evaluations"
source: "Google DeepMind"
url: "https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/"
published: "2026-08"
added: "2026-09-01"
category: experimentation-causal
tags: [evaluation, benchmarking, confidential-computing, trust, measurement]
novelty: 4
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Piloting the World's First Double-Blind AI Evaluations

**Source:** [Google DeepMind](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/) · Published 2026-08 · Added 2026-09-01
**Category:** Experimentation & Causal Inference · **Tags:** `evaluation`, `benchmarking`, `confidential-computing`, `trust`

## TL;DR

Google DeepMind ran what it describes as the first double-blind evaluation
of a proprietary, frontier-class AI model, using confidential computing so
neither side has to trust the other: the evaluator never sees Gemini's
weights, and Google never sees the evaluator's benchmark prompts. The pilot,
run with the Singapore AI Safety Institute, OpenMined, AVERI, and
MLCommons, tested a Gemini Flash Lite model on August 27, 2026.

## 1. Business context

Third-party AI benchmarking has historically forced a bad trade: either the
evaluator hands its test prompts to the model provider in advance — risking
the provider training to the test or otherwise inflating scores — or the
provider hands over model weights, risking its intellectual property. That
tension has made outside parties reluctant to run truly rigorous,
contamination-free evaluations of frontier models, and made model providers
reluctant to expose IP to enable them. DeepMind's stated goal is a
measurement protocol trustworthy enough that independent evaluators can
verify capability and safety claims without either party having to take the
other on faith.

## 2. Technical details

- **Confidential computing core.** The evaluation runs inside **Google
  Cloud Confidential Space**, using an **NVIDIA H100 Confidential GPU** and
  **Intel TDX** host memory encryption to isolate the workload from the
  underlying infrastructure operator.
- **Mutual blindness.** DeepMind supplies Gemini's weights and inference
  code; the evaluator supplies its benchmark prompts and evaluation code.
  Both are transmitted over encrypted connections into the confidential
  enclave, where the evaluation runs without either party gaining access to
  the other's protected assets.
- **Remote attestation.** Cryptographic remote attestation verifies that the
  software environment inside the enclave is what both parties agreed to
  run, rather than a tampered version that could leak data to either side.
- **Model and partners.** The pilot evaluated a **Gemini Flash Lite** model
  against confidential benchmarks, in collaboration with the **Singapore AI
  Safety Institute**, **OpenMined**, **AVERI**, and **MLCommons**.

## 3. Impact — potential & realized

- **Realized:** a working pilot demonstrating that a frontier-class,
  proprietary model can be benchmarked by an external party without either
  side exposing its protected assets — described as the first time this has
  been done for a model at this class.
- **Potential:** if this pattern generalizes, it could become the trust
  layer underneath independent AI safety and capability evaluation
  generally — letting safety institutes and standards bodies (MLCommons and
  similar) certify claims about proprietary models without providers having
  to choose between opacity and IP exposure. It is a pilot, though: no
  numbers on evaluation throughput, cost overhead versus an un-encrypted
  run, or scaling beyond one Flash Lite-sized model have been reported.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a genuinely new trust primitive for AI measurement, still at pilot scale

Confidential computing itself isn't new, but applying it specifically to
solve the "who do we trust with what" deadlock in third-party AI
benchmarking is a clever, previously-unaddressed application. It doesn't
introduce a new ML technique, which keeps it short of a 5, but it addresses
a real and growing problem — benchmark contamination and gameable
evaluations — that most of the field currently just lives with. If this
becomes standard practice for frontier-model certification, evaluation
bodies like MLCommons would be the most likely near-term adopters.

### Similar / related work

- **Hashmarks: Privacy-Preserving Benchmarks for High-Stakes AI
  Evaluation** ([arXiv](https://arxiv.org/pdf/2312.00645)) — an earlier
  cryptographic approach to keeping benchmark data private from model
  providers, addressing one half of the same trust problem this pilot
  solves for both sides simultaneously.
- **Shopify's Sidekick continual learning loop** ([in this
  bank](2026-09-01-shopify-sidekick-continual-learning-loop.md)) — a
  different angle on the same underlying issue (trusting an evaluation
  signal enough to act on it), there solved by calibrating an LLM-judge
  against human raters and production A/B outcomes rather than
  cryptography.

### Jargon buster

- **Confidential computing** — running a workload inside hardware-encrypted
  memory so that not even the cloud provider or infrastructure operator can
  inspect the data or code while it executes.
- **Remote attestation** — a cryptographic proof that a specific, agreed-on
  piece of software (and nothing else) is what's actually running inside a
  secure enclave.
- **Benchmark contamination** — when a model has been exposed to test
  questions (or very similar data) before evaluation, inflating its
  apparent performance without a real capability gain.
