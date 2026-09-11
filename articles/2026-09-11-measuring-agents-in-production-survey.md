---
id: measuring-agents-in-production-survey
title: "Measuring Agents in Production"
source: "ICML 2026 (oral)"
url: "https://arxiv.org/abs/2512.04123"
published: "2025-12"
added: "2026-09-11"
category: research-foundational
tags: [llm-agents, production-ml, empirical-study, evaluation, reliability]
novelty: 4
sourced_via: "web search"
---

# Measuring Agents in Production

**Source:** [ICML 2026 (oral)](https://arxiv.org/abs/2512.04123) · Published 2025-12 · Added 2026-09-11
**Category:** Research & Foundational · **Tags:** `llm-agents`, `production-ml`, `empirical-study`, `evaluation`, `reliability`

## TL;DR

A mixed-methods study of 20 in-depth case studies and an 86-practitioner survey across 26 domains finds that real production LLM agents are far simpler than the research literature's frontier designs — most take at most 10 steps before human intervention, rely on prompting rather than fine-tuning, and are evaluated mostly by humans — with reliability, not capability, the dominant open problem.

## 1. Business context

There is a wide gap between what gets published about agentic AI architectures — elaborate multi-agent orchestration, long autonomous horizons, sophisticated memory systems — and what organizations actually run in production. This paper exists to close that gap empirically: rather than proposing a new agent architecture, it asks practitioners why they build agents, how they actually build them, how they evaluate them, and what their biggest open problems are, so that the field's assumptions about "how agents are built" can be checked against reality.

## 2. Technical details

The study combines 20 in-depth interviews (qualitative case studies with agent developers) with a broader survey of 86 practitioners running deployed agent systems, spanning 26 different application domains — giving both depth (how specific teams reason about their design choices) and breadth (whether patterns generalize). The headline findings describe a field that has converged on simplicity over sophistication: 68% of production agents execute at most 10 sequential steps before requiring human intervention, meaning long, fully autonomous run loops are the exception rather than the norm; 70% rely on prompting off-the-shelf foundation models rather than fine-tuning model weights, meaning most teams are choosing prompt engineering and scaffolding over the cost and complexity of custom training; and 74% depend primarily on human evaluation to judge agent quality, rather than automated benchmarks or LLM-as-judge pipelines. Across both the interviews and the survey, reliability — defined as consistent, correct behavior over time rather than peak capability on a single task — surfaces as the top development challenge, and the paper reports that practitioners are currently addressing it through systems-level design (guardrails, scoping, human checkpoints) rather than waiting on model-level improvements.

## 3. Impact — potential & realized

**Realized:** the paper provides the field with grounded, survey-backed numbers (68%, 70%, 74%) that can be cited in place of anecdote when discussing how agents are actually built and evaluated in industry — useful ammunition against over-engineered agent designs that assume production teams want maximal autonomy and minimal human oversight.

**Potential:** the finding that reliability is being solved with systems-level design rather than model improvements is a signal to the field about where research effort is most needed — evaluation methodology, guardrail design, and human-in-the-loop workflow patterns may matter more to practitioners right now than raw agent capability gains.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Rare, rigorous empirical grounding for a field full of assumptions

Most "state of AI agents" content is vendor marketing, single-company case studies, or capability benchmarks — this is a genuine mixed-methods empirical study (20 interviews plus an 86-practitioner survey across 26 domains) accepted as an ICML oral, which is a meaningfully higher bar than the typical blog-post survey. It doesn't introduce a new architecture or technique, which caps it below a 5, but as a corrective to hype about long-horizon autonomous agents, it's one of the more citation-worthy pieces of 2026 for anyone deciding how much agent complexity their own production system actually needs.

### Similar / related work

- [**How Fast Do Agents Rot? An Empirical Study of Long-Horizon Degradation**](2026-09-09-how-fast-do-agents-rot-long-horizon-degradation.md) (in this bank) — another empirical (rather than architectural) study of agent behavior in practice; this paper's "68% stop at ≤10 steps" finding is a natural complement to that paper's degradation-over-longer-horizons results.
- [**Building an MCP Ecosystem at Pinterest**](2026-09-10-pinterest-mcp-ecosystem-ai-agents.md) (in this bank) — a concrete production case study that matches this paper's pattern almost exactly: prompting-based agents, human-in-the-loop confirmation gates, and directional rather than rigorous metrics.
- **"Empowering Real-World: A Survey on the Technology, Practice, and Evaluation of LLM-driven Industry Agents"** — a broader literature survey covering similar ground from the technology-taxonomy angle rather than this paper's empirical-fieldwork angle; useful as a complementary read.

### Jargon buster

- **Human-in-the-loop evaluation** — judging an agent's output quality by having a person review it, as opposed to an automated metric, benchmark, or another LLM acting as judge.
- **Reliability (in agent systems)** — the property of behaving correctly and consistently across repeated runs and edge cases over time, distinct from an agent's peak capability on any single benchmark task.
- **Systems-level design (as a reliability lever)** — improving an agent's real-world dependability through surrounding scaffolding (guardrails, scoped permissions, checkpoints, retries) rather than through improving the underlying model itself.
- **Fine-tuning vs. prompting** — fine-tuning updates a model's weights on task-specific data; prompting instead steers an unmodified, off-the-shelf model's behavior purely through the instructions and context given at inference time.
