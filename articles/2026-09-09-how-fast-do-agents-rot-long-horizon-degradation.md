---
id: how-fast-do-agents-rot-long-horizon-degradation
title: "How Fast Do Agents Rot? An Empirical Study of Long-Horizon Degradation in LLM Agents for Production Decision-Making"
source: "Microsoft / arXiv"
url: "https://arxiv.org/abs/2609.01660"
published: "2026-09"
added: "2026-09-09"
category: llm-genai
tags: [ai-agents, reliability, long-horizon-tasks, evaluation, benchmarking, production-decision-making]
novelty: 4
sourced_via: "web search"
---

# How Fast Do Agents Rot? An Empirical Study of Long-Horizon Degradation in LLM Agents for Production Decision-Making

**Source:** [Microsoft / arXiv](https://arxiv.org/abs/2609.01660) · Published 2026-09 · Added 2026-09-09
**Category:** LLMs & Generative AI · **Tags:** `ai-agents`, `reliability`, `long-horizon-tasks`, `evaluation`, `benchmarking`, `production-decision-making`

## TL;DR

An empirical study spanning 9 models (6 open-source from 1.2B to 671B parameters, plus 3 proprietary systems), 4 task families, 5 task horizons, 3 context regimes, and 10,664 trajectories finds that every tested agent — including deployed production systems — degrades from near-perfect success to near zero within about sixteen sequential steps, following a geometric law governed by a single per-step reliability parameter. Benchmarks that top out around GAIA-length horizons (roughly 0.42 success) look far rosier than hundred-step production scenarios (roughly 0.24 success), and the authors argue current evaluation practice is measuring the wrong thing.

## 1. Business context

Benchmark leaderboards for LLM agents keep climbing, but production teams routinely report that agents which look strong on standard benchmarks fail once deployed on real, longer workflows. The paper's motivating claim is that this gap is not primarily about model capability shortfalls on any single step — it's an artifact of **task horizon**: most public agent benchmarks are dominated by short-to-medium sequences of dependent steps, while production workloads (multi-step data pipelines, long customer-support resolutions, extended coding tasks) routinely demand an order of magnitude more dependent steps than the benchmarks that get quoted in model cards and comparison tables.

## 2. Technical details

The authors run a large, controlled empirical study rather than proposing a new architecture:

- **Scope:** 9 models spanning 1.2B to 671B parameters among open-source systems, plus 3 proprietary/deployed agent systems; 4 distinct task families including genuine tool-use scenarios (not just single-turn Q&A); 5 different task horizons (i.e., varying the number of sequential dependent steps required); and 3 different context-length regimes. In total, 10,664 trajectories were collected and analyzed.
- **Core finding — the geometric law:** agent success across a task with $n$ dependent steps follows a geometric decay governed by a single per-step reliability parameter $p$ — i.e., overall success behaves like $p^n$. Under this law, even a per-step reliability that looks impressive in isolation (say, 95%) compounds into near-total failure once a task chains together enough sequential steps.
- **Where the decay comes from:** step count, not context length, is the dominant driver. The paper reports that artificially limiting available context actually *steepens* the decay rather than easing it (statistically significant at p = 3×10⁻⁶) — i.e., cramming for shorter context doesn't rescue long-horizon reliability, and may hurt it, contradicting an intuition that shorter contexts should be easier for a model to reason over.
- **Scale helps, but saturates:** reliability increases with model scale across the 1.2B–671B range, but the per-step reliability parameter saturates well below 1.0 even for the strongest models tested — meaning no amount of scaling tested here fully solves the compounding-failure problem.

## 3. Impact — potential & realized

**Realized (measurement, not a fix):** the paper quantifies the benchmark/production gap directly — roughly 0.42 success at GAIA-benchmark-length horizons versus roughly 0.24 success at hundred-step production-scenario horizons, using the same underlying models. All tested models, deployed production systems included, collapse from near-perfect to near-zero success within about sixteen sequential steps.

**Potential:** the authors' actionable recommendation is to replace aggregate pass-rate metrics with **horizon-aware evaluation and reliability budgeting** — reporting a model's per-step reliability parameter and using the geometric law to forecast expected success at the actual horizon length a production workflow requires, rather than reporting a single benchmark score and assuming it generalizes to longer chains.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Turns a widely-felt production complaint into a measurable law

"Agents fall apart on long workflows" is a complaint every team running agents in production has made informally; what earns this a 4 is turning that complaint into a specific, testable model (a geometric decay with one fitted per-step reliability parameter) validated across 10,664 trajectories and multiple model families, including production systems rather than only research benchmarks. The context-length finding — that limiting context steepens rather than eases decay — cuts directly against a common mitigation strategy (aggressively trim context to reduce confusion) and is the single most actionable, counterintuitive result in the paper. It's not a 5 because the geometric-decay framing itself, and the idea that benchmarks under-sample real task horizons, both build on an existing and growing critique of agent evaluation rather than introducing a wholly new concept.

### Similar / related work

- [**What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets**](2026-09-09-dxrg-llm-trading-agents-production-record.md) (in this bank) — a complementary empirical study of agents in a real, high-stakes production setting, though focused on decision quality and risk behavior rather than step-count degradation.
- [**AutoLR: Automating the Path from Research to Launch Review in Industrial Recommender Systems**](2026-09-08-netease-autolr-agentic-recsys-launch-review.md) (in this bank) — a production agent system that, by design, keeps LLM agents restricted to short proposal steps and routes all state-changing, multi-step execution through deterministic controllers; read alongside this paper, that architectural choice looks like a direct (if implicit) mitigation for the horizon-decay problem documented here.
- **AlphaEval: Evaluating Agents in Production** — another recent effort at production-grounded (rather than purely benchmark-grounded) agent evaluation; complements this paper's horizon-aware framing with a broader evaluation methodology. (No specific public write-up beyond the arXiv preprint was located; referenced here for context, not as a linked source.)

### Jargon buster

- **Task horizon** — the number of sequential, dependent steps a task requires an agent to complete correctly in a row before it counts as a success.
- **Geometric law / geometric decay** — a mathematical pattern where overall success equals a per-step success probability raised to the power of the number of steps; small per-step error rates compound multiplicatively and collapse quickly as step count grows.
- **GAIA** — a widely used general AI-assistant benchmark; the paper uses "GAIA-length horizons" as shorthand for the (comparatively short) task lengths typical of popular public agent benchmarks.
- **Reliability budgeting** — the paper's proposed practice of forecasting expected end-to-end success for a specific production task length using a model's measured per-step reliability, rather than trusting an aggregate benchmark score to generalize.
