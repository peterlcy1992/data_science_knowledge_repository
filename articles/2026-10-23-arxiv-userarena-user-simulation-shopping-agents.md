---
id: arxiv-userarena-user-simulation-shopping-agents
title: "UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents"
source: "arXiv cs.IR (Zhao et al.)"
url: "https://arxiv.org/abs/2610.30932"
published: "2026-10"
added: "2026-10-23"
category: personalization-recsys
tags: [user-simulation, benchmark, agentic-recommendation, ab-test-validation, offline-evaluation]
novelty: 3
sourced_via: "web search"
---

# UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents

**Source:** [arXiv cs.IR (Zhao et al.)](https://arxiv.org/abs/2610.30932) · Published 2026-10 · Added 2026-10-23
**Category:** Personalization & Recsys · **Tags:** `user-simulation`, `benchmark`, `agentic-recommendation`, `ab-test-validation`, `offline-evaluation`

## TL;DR

UserArena is an e-commerce benchmark of real long-session trajectories for evaluating user simulators, validated offline against a controlled production A/B test. The authors' On-Policy Trajectory Distillation (OPTD) simulator most closely reproduces the production policy's effect among those evaluated.

## 1. Business context

Agentic recommenders make sequences of context-dependent decisions, so evaluating them needs simulated users that behave realistically over long sessions. The authors say existing resources rarely offer long fine-grained real-user trajectories, trajectory-level evaluation, or validation against production A/B results.

## 2. Technical details

UserArena pairs real e-commerce trajectories with an interactive environment: 64,729 session trajectories, 11,010 users, 566,102 items and 13 action types. It supports five-level evaluation, from output validity and local decisions through sequential behavior and personalization to outcomes. OPTD (On-Policy Trajectory Distillation) uses trajectory-level intent to provide dense teacher targets on the student simulator's own rollouts. Authors: Jujia Zhao, Jiakai Tang, Jing Yu, Wen Chen, Jian Wu, Han Zhu, Fei Sun, Suzan Verberne, Zhaochun Ren; submitted 22 Oct 2026.

## 3. Impact — potential & realized

Realized (as reported): under the benchmark protocol OPTD achieves the strongest overall fidelity among evaluated simulators and most closely reproduces the production policy effect in offline simulation. Specific fidelity scores were not visible at the abstract level. Potential: cheaper offline screening of agentic recommendation policies before an online experiment.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Anchoring a simulator benchmark to a real production A/B result is the useful part, because it checks the simulator against the measurement that matters

Novelty 3/5 - Simulator benchmarks exist; validating against an actual controlled production A/B is the differentiator and ties offline evaluation back to experimentation practice. One validation experiment cannot show the simulator ranks other policies correctly.

### Similar / related work

- [**Selling in the Wild**](2026-10-20-arxiv-selling-in-the-wild-sales-agent-field-rct.md) (in this bank) — randomized field evidence for an agent, the kind of ground truth simulators are checked against
- [**Next Best Action: Causal Constrained Offline RL for Business Action Targeting**](2026-10-20-arxiv-next-best-action-causal-constrained-offline-rl.md) (in this bank) — offline evaluation of decision policies

### Jargon buster

- **User simulator** — A model that imitates how real users behave so recommender policies can be tested without live traffic.
- **Distillation** — Training a student model to match a teacher's targets.
- **On-policy** — Training on the student's own generated rollouts rather than only on logged data.
