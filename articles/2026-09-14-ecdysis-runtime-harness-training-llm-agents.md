---
id: ecdysis-runtime-harness-training-llm-agents
title: "Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents"
source: "arXiv"
url: "https://arxiv.org/abs/2609.11677"
published: "2026-09"
added: "2026-09-14"
category: llm-genai
tags: [ai-agents, harness-evolution, agentic-training, failure-analysis, reasoning, generalization]
novelty: 4
sourced_via: "full-text fetch"
---

# Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents

**Source:** [arXiv](https://arxiv.org/abs/2609.11677) · Published 2026-09 · Added 2026-09-14
**Category:** LLMs & Generative AI · **Tags:** `ai-agents`, `harness-evolution`, `agentic-training`, `failure-analysis`

## TL;DR

Self-evolving agent "harnesses" — the scaffolding of prompts, tools, and control flow around an LLM — usually improve by iteratively testing one task at a time, which is slow and prone to overfitting to whatever failures happened to occur. Ecdysis instead aggregates failure evidence across a whole batch of tasks before deciding what to fix, and uses a multi-role diagnosis step to tell genuine harness bugs apart from failures that are really just a specific model's weaknesses — delivering up to 1.84x faster harness training and an 18.56% accuracy improvement, with better generalization to unseen tasks.

## 1. Business context

An LLM agent's real-world performance depends heavily on more than the base model: the "harness" — the system prompt, tool definitions, retry logic, memory management, and control flow wrapped around the model — often determines whether an agent actually completes a task reliably. Teams increasingly try to evolve that harness automatically rather than hand-tuning it, using the agent's own execution feedback to revise prompts and tool logic. The paper identifies two costs in how this is normally done: it's slow, because iterative per-task search means repeatedly re-running the agent and re-editing code for every single failure observed; and it's fragile, because optimizing against isolated failures tends to produce narrow fixes that overfit to the specific tasks and failure patterns seen during training, generalizing poorly to tasks the harness wasn't tuned against. A more subtle problem underlies both: without a principled way to diagnose *why* something failed, harness-evolution methods can't tell a genuine harness-level bug (fix the scaffolding) from a model-specific limitation (which needs a model-specific workaround, not a harness rewrite) — so fixes end up being unnecessary, narrow patches rather than durable improvements.

## 2. Technical details

Ecdysis restructures harness evolution around two ideas:

- **Batch-level cross-instance failure aggregation.** Instead of analyzing and reacting to one failed task instance at a time, Ecdysis jointly analyzes failure evidence gathered across a whole batch of task instances at once, looking for recurring patterns rather than one-off anomalies before deciding what in the harness to change.
- **Failure-Driven Collaborative Refinement (FDCR).** A multi-role diagnosis process examines the aggregated failure evidence and iteratively refines the harness modification specification, explicitly distinguishing failures that call for model-specific accommodation from failures that indicate a genuine, harness-level problem worth repairing structurally.

By diagnosing at the batch level with multiple roles cross-checking the failure cause, Ecdysis avoids both the wasted repeated agent executions of per-task iterative search and the narrow, single-failure-driven patches that don't transfer to new tasks.

## 3. Impact — potential & realized

**Realized:** Across experiments spanning multiple LLMs and benchmarks, Ecdysis achieves up to a **1.84x speedup** in harness training time compared to existing harness-evolution methods, while improving the reasoning accuracy of the resulting harnesses by **18.56%**. Harnesses trained with Ecdysis also generalize better across different LLMs and reduce inference-time token consumption compared to the baseline evolution methods.

**Potential:** As more products ship agentic features built on a harness layered over an off-the-shelf model, the ability to evolve that harness automatically — cheaply and without overfitting to a narrow training set — becomes a direct lever on both agent reliability and iteration speed. The core diagnostic move (aggregate failures across many tasks before diagnosing, and explicitly separate "fix the model prompt" from "fix the scaffolding") is a reusable discipline for any team building agent-evaluation and improvement loops, independent of Ecdysis's specific implementation.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A meaningfully better diagnostic framework for a fast-moving problem

Harness/scaffolding evolution for LLM agents is a young and crowded area right now, and most approaches in it are still doing per-instance iterative search. Ecdysis's real contribution isn't the aggregation mechanic alone — it's insisting on separating model-specific failure from harness-level failure *before* acting, which is a genuinely useful discipline that most existing methods skip past. That said, this is still evaluated on benchmarks rather than a disclosed production deployment, so its real-world durability is unproven.

### Similar / related work

- [**How Fast Do Agents Rot? An Empirical Study of Long-Horizon Degradation in LLM Agents for Production Decision-Making**](2026-09-09-how-fast-do-agents-rot-long-horizon-degradation.md) (in this bank) — a complementary empirical look at where and why production agents fail over long horizons, which is exactly the kind of failure evidence a system like Ecdysis would need to diagnose.
- **Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents** — [arXiv:2605.22166](https://arxiv.org/abs/2605.22166) — a closely related prior approach to harness-level (rather than model-level) adaptation for agent reliability.
- **EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning** — [arXiv:2606.03108](https://arxiv.org/abs/2606.03108) — a different strategy for the same underlying goal, jointly evolving the policy and the harness rather than diagnosing and patching the harness alone.

### Jargon buster

- **Harness (agent harness)** — The non-model scaffolding around an LLM in an agentic system: system prompts, tool/function definitions, retry and error-handling logic, memory management, and control flow.
- **Harness evolution** — Automatically revising that scaffolding based on observed execution outcomes, as opposed to fine-tuning or retraining the underlying model.
- **Failure aggregation** — Analyzing evidence from many failed task attempts together to find recurring, systematic causes, rather than reacting to each failure individually and risking overfitting to one-off cases.
