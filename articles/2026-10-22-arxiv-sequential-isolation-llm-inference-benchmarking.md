---
id: arxiv-sequential-isolation-llm-inference-benchmarking
title: "Reproducible LLM Inference Benchmarking: A Sequential Isolation Protocol for Regression Testing"
source: "arXiv cs.PF (Olympio et al.)"
url: "https://arxiv.org/abs/2610.09778"
published: "2026-10"
added: "2026-10-22"
category: ml-infra-serving
tags: [benchmarking, variance, vllm, latency, regression-testing]
novelty: 3
sourced_via: "web search"
---

# Reproducible LLM Inference Benchmarking: A Sequential Isolation Protocol for Regression Testing

**Source:** [arXiv cs.PF (Olympio et al.)](https://arxiv.org/abs/2610.09778) · Published 2026-10 · Added 2026-10-22
**Category:** ml-infra-serving · **Tags:** `benchmarking`, `variance`, `vllm`, `latency`, `regression-testing`

## TL;DR

A controlled benchmarking protocol cuts run-to-run variability in LLM serving measurements from an average coefficient of variation of 15.2% to 2.2%, making latency regressions detectable.

## 1. Business context

Teams choosing or upgrading LLM serving stacks compare latency and cost, but repeated runs of the same benchmark vary with execution and system state, so small regressions are indistinguishable from noise.

## 2. Technical details

The 'Sequential Isolation Methodology' controls the measurement environment in stages while intentionally varying workload concurrency. Design: 6 context sizes x 8 concurrency levels x 3 open-source models = 144 configurations, 5 repetitions each, on one NVIDIA A100 80GB with vLLM 0.9.1. Variance is the CV across the five per-repetition median time-to-first-token values. Infrastructure-as-Code and scripts are provided. Submitted 7 Oct 2026; model names are not in the abstract.

## 3. Impact — potential & realized

Realized (as reported): average CV fell from 15.2% in the least-controlled stage to 2.2% in the final stage; 113 of 144 configurations (78.5%) reached CV below 3%. A latency transition appears between 200 and 500 concurrent users on the tested stack; P99 differences across models are descriptive, and a cost break-even model is sensitive to API pricing. The authors say it is a reference for regression testing, not a predictor of uncontrolled production traffic.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Measurement hygiene applied to LLM serving; useful but single-GPU, single-stack, with results the authors themselves scope narrowly

Novelty 3/5 - Measurement hygiene applied to LLM serving; useful but single-GPU, single-stack, with results the authors themselves scope narrowly.

### Similar / related work

- [**MOSS: Monitoring Semantic Failures in Search and Recommendation**](2026-10-21-arxiv-moss-semantic-failure-monitoring-search-recsys.md) (in this bank) — production monitoring that also needs noise control

### Jargon buster

- **Coefficient of variation** — Standard deviation divided by the mean; a unit-free measure of relative noise.
- **Time to first token (TTFT)** — Latency from request to the first generated token.
- **P99 latency** — The latency below which 99% of requests complete.
