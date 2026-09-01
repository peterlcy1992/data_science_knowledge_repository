---
id: shopify-sidekick-continual-learning-loop
title: "Sidekick's Continual Learning Loop"
source: "Shopify Engineering"
url: "https://shopify.engineering/sidekicks-continual-learning-loop"
published: "2026-08"
added: "2026-09-01"
category: llm-genai
tags: [continual-learning, llm-judge, dspy, grpo, reinforcement-learning, agent, cost-efficiency]
novelty: 5
sourced_via: "full-text fetch"
---

# Sidekick's Continual Learning Loop

**Source:** [Shopify Engineering](https://shopify.engineering/sidekicks-continual-learning-loop) · Published 2026-08 · Added 2026-09-01
**Category:** LLMs & Generative AI · **Tags:** `continual-learning`, `llm-judge`, `dspy`, `grpo`, `reinforcement-learning`

## TL;DR

Shopify rebuilt the improvement loop for Sidekick, its AI agent, around a
four-stage flywheel — a human-calibrated quality rubric, an LLM judge
calibrated against that rubric and against real A/B outcomes, automated
prompt/tool research, and continual learning via GRPO fine-tuning against the
calibrated judge as reward. For a GraphQL agent handling 2,000 requests/min,
this cut serving cost roughly **96%, from ~$27M to ~$1M/year**.

## 1. Business context

Sidekick is Shopify's AI agent. Relying purely on ever-larger frontier-model
prompting to improve its quality gets expensive fast and hits diminishing
returns — you can't keep buying quality by upgrading models forever. Shopify
wanted a way to keep improving Sidekick without perpetually scaling frontier
model spend, and to do so against a quality signal it could actually trust,
rather than informal judgment calls about whether a change "felt" better.

## 2. Technical details

The loop has four stages:

- **1. Human-calibrated quality rubric.** A rubric for scoring Sidekick
  responses is calibrated against human raters using **Cohen's kappa**, an
  inter-rater agreement statistic that corrects for chance agreement — the
  point is to get a rubric whose scores genuinely agree with human judgment,
  not one that merely looks plausible.
- **2. Judge calibration.** A **DSPy**-based pipeline tunes an LLM-as-judge
  against that rubric, using reflective prompt-optimization techniques
  (**GEPA** and **ACE**) to iteratively refine the judge's own prompt based on
  feedback rather than by hand. Crucially, the judge is then validated against
  **production A/B test outcomes** — checked to actually predict real-world
  quality, not just to correlate with the rubric on paper — before it's
  trusted as a reward signal.
- **3. Prompt/tool "autoresearch."** An automated search process explores
  prompt and tool configurations for Sidekick.
- **4. Continual learning.** Production failures are mined and used for
  **SFT**, followed by **GRPO** (Group Relative Policy Optimization)
  fine-tuning that uses the calibrated judge itself as the reward signal —
  reinforcement learning against an automated, outcome-validated judge rather
  than a hand-written reward function.

The system serves a GraphQL agent at **2,000 requests/minute**.

## 3. Impact — potential & realized

- **Realized:** serving cost for the GraphQL agent fell roughly **96%, from
  ~$27M to ~$1M/year**.
- **Potential:** a template for any team running a high-traffic LLM agent
  that wants compounding quality improvements without linear cost growth from
  continually upgrading to bigger frontier models — as long as it invests in
  a genuinely validated judge first.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 5/5 — the calibration-before-reward discipline is the real contribution

LLM-as-judge, DSPy prompt optimization, and GRPO fine-tuning are each
individually known techniques. What makes this loop stand out is the
discipline of calibrating the judge against human raters *and* against real
production A/B outcomes before ever using it as an RL reward signal — that
step is what separates this from "just do RLHF against an LLM judge," which
tends to reward models for gaming an uncalibrated judge rather than for
actually getting better. A verifiable, large production cost number (~96%
reduction) for a real high-traffic agent is rare enough on its own to merit
the top of the scale.

### Similar / related work

- [**Gisting: Compressing LLM Agent Context to Increase Throughput and Cut
  Cost**](2026-09-01-shopify-gisting-context-compression.md) (in this bank) — Shopify's companion piece; a different
  cost-reduction lever (context compression) for the same underlying
  problem of expensive high-traffic LLM agent serving.
- [**Running a Software Factory Efficiently at Uber Scale**](2026-09-01-uber-software-factory-efficient-agent-cost.md) (in this bank) — a
  different company's cost-management framework for a coding-agent
  platform, attacking usage/routing economics rather than model quality
  via RL.
- [**Delegating Engineering Work to Cloud-Based Agents (Flux)**](2026-08-31-doordash-flux-cloud-agents-engineering.md) (in this bank) — another
  production LLM agent platform operating at scale, though focused on
  sandboxed execution rather than a continual-learning loop.

### Jargon buster

- **Cohen's kappa** — a statistic measuring agreement between raters that
  corrects for the agreement expected by chance alone, used here to validate
  that a quality rubric matches human judgment.
- **LLM-as-judge** — using an LLM to score another model's outputs as a
  scalable stand-in for human evaluation.
- **DSPy** — a framework for programmatically optimizing prompts and
  multi-step LLM pipelines against a metric, instead of hand-tuning them.
- **GEPA / ACE** — reflective prompt-optimization algorithms used within
  DSPy that iteratively refine a prompt based on feedback signals rather than
  manual editing.
- **GRPO (Group Relative Policy Optimization)** — a reinforcement-learning
  fine-tuning method that scores a group of sampled outputs relative to each
  other, rather than requiring a separately trained value function.
