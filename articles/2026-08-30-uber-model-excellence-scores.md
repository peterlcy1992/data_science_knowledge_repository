---
id: uber-model-excellence-scores
title: "Model Excellence Scores: A Framework for ML Quality at Scale at Uber"
source: "Uber Engineering"
url: "https://www.uber.com/blog/enhancing-the-quality-of-machine-learning-systems-at-scale/"
published: "2024-10"
added: "2026-08-30"
category: ml-infra-serving
tags: [ml-governance, model-quality, sla, monitoring, drift, mlops, lifecycle]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Model Excellence Scores: A Framework for ML Quality at Scale at Uber

**Source:** [Uber Engineering](https://www.uber.com/blog/enhancing-the-quality-of-machine-learning-systems-at-scale/) · Published 2024-10 · Added 2026-08-30
**Category:** ML Infrastructure & Serving · **Tags:** `ml-governance`, `model-quality`, `sla`, `drift`
_Surfaced via the Snacks Weekly on Data Science podcast._

## TL;DR

Uber's **Model Excellence Scores (MES)** turn "is this model any good?" into a
measured, monitored, enforceable number spanning the whole lifecycle —
prototyping, training, deployment, prediction — with **SLAs** on dimensions like
accuracy, **freshness**, and feature quality, so ML quality becomes governable
rather than anecdotal.

## 1. Business context

At Uber's scale, thousands of models run in production, and quality was assessed
inconsistently and mostly at training time. That left ML engineers with limited
visibility into quality across a model's life, and left leadership unable to
compare or prioritize models on quality and impact. Uber wanted a **standardized,
organization-wide** way to measure, monitor, and enforce ML quality — the ML
analog of engineering SLAs.

## 2. Technical details

- **Lifecycle dimensions.** MES defines distinct quality dimensions for each phase —
  **prototyping, training, deployment, prediction** — instead of a single
  train-time accuracy number.
- **SLA integration.** It borrows the **Service Level Agreement** concept to set
  standards a model must meet, making quality **enforceable**, not just observed.
- **Key metrics.** Examples include **training model accuracy**, **prediction
  accuracy**, **model freshness**, and **prediction feature quality** — the
  data-plane properties that actually degrade in production.
- **Position in the stack.** MES tracks **data-plane quality** (accuracy, drift) and
  **complements control-plane guardrails** — i.e. deployment-safety systems that
  gate *how* models ship. Quality-of-outputs and safety-of-rollout are treated as
  separate, complementary concerns.

## 3. Impact — potential & realized

- **Realized:** a common quality language across Uber's ML fleet — clearer visibility
  for practitioners and more informed prioritization for leadership.
- **Potential:** a template for ML governance at any org past the point where
  model count outstrips manual oversight; the SLA framing is the reusable idea.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — governance, not modeling, but a genuinely useful codification

There's no new algorithm here; the contribution is **organizational**: naming the
quality dimensions per lifecycle stage and attaching **SLAs** so quality is
measured and enforced fleet-wide. That's unglamorous and exactly what large ML
orgs need, and the clean split between **data-plane quality (MES)** and
**control-plane safety (guardrails)** is a clarifying mental model. A 3 — high
practical value, low methodological novelty.

### Similar / related work

- [**In-House LLM Serving at Netflix**](2026-08-30-netflix-in-house-llm-serving.md) (in this bank) — the serving/reliability side
  of running many models in production.
- **Uber "Raising the Bar on ML Model Deployment Safety"** — the control-plane
  guardrails MES complements.
- **Uber Michelangelo** — the platform context these quality systems sit within.

### Jargon buster

- **SLA (Service Level Agreement)** — a committed standard a service must meet (e.g.
  uptime); applied here to model-quality metrics.
- **Model freshness** — how recently a model was retrained/updated relative to how
  fast its data shifts; stale models silently decay.
- **Drift** — when live data or the target relationship moves away from what the model
  was trained on, degrading accuracy over time.
- **Data plane vs. control plane** — data plane = the quality of what the model
  actually predicts; control plane = the systems governing how models are deployed
  and rolled back.
- **ML governance** — the processes and metrics that keep a fleet of models
  accountable for quality, risk, and impact.
