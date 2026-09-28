---
id: airbnb-eval-driven-development-genai
title: "Eval-Driven Development: Lessons from Evaluating GenAI at Scale"
source: "Airbnb Tech Blog"
url: "https://airbnb.tech/ai-ml/eval-driven-development-lessons-from-evaluating-genai-at-scale/"
published: "2026-07"
added: "2026-09-28"
category: llm-genai
tags: [llm-evaluation, eval-driven-development, generative-ai, testing, failure-modes, production-ml]
novelty: 3
sourced_via: "web search"
---

# Eval-Driven Development: Lessons from Evaluating GenAI at Scale

**Source:** [Airbnb Tech Blog](https://airbnb.tech/ai-ml/eval-driven-development-lessons-from-evaluating-genai-at-scale/) · Published 2026-07 · Added 2026-09-28
**Category:** LLMs & Generative AI · **Tags:** `llm-evaluation`, `eval-driven-development`, `generative-ai`, `testing`, `failure-modes`, `production-ml`

## TL;DR

Airbnb argues that shipping trustworthy generative-AI features requires treating evaluation as a first-class engineering discipline rather than an afterthought, and proposes "eval-driven development" (EDD) — the GenAI analogue of test-driven development — as the practice: build infrastructure and team habits to continuously discover, encode, and test for failure modes as they're found, rather than trying to enumerate every failure mode upfront.

## 1. Business context

Generative AI features are fundamentally harder to validate before shipping than traditional software: outputs are non-deterministic, "correct" is often subjective or context-dependent, and a model that looks fine on a handful of manual spot-checks can fail in ways engineers never anticipated once it meets real users and real edge cases. Traditional software testing assumes you can write a fixed set of test cases upfront and get a pass/fail signal; that assumption doesn't transfer cleanly to LLM-based features, where failure modes are often discovered only in production and where a single "correct" answer frequently doesn't exist. Airbnb's stated problem is building GenAI products (spanning things like customer support automation and conversational features) that teams and users can actually trust, which requires a different development discipline than teams are used to.

## 2. Technical details

Eval-driven development (EDD), as described, is the GenAI analogue of test-driven development: instead of writing all your tests upfront and coding to make them pass, teams build the infrastructure and organizational habits to keep discovering new failure modes, encode each one as a concrete evaluation case, and continuously re-test against the growing eval suite as the product evolves. The authors (Rohit Girme, Dan Miller, Mia Zhao, Lifan Yang, and Clint Kelly) frame this as an ongoing loop rather than a one-time setup: failure modes surface from production usage, human review, or targeted probing; each one gets turned into a reusable, automatable eval; and the eval suite becomes the regression-test backbone that lets the team iterate on prompts, models, and system design without re-litigating previously-fixed failures. The piece explicitly contrasts this against the naive alternative of treating evaluation as a one-off pre-launch checklist, arguing that because LLM outputs are non-deterministic and correctness is often subjective, a static, upfront test set gives false confidence — the eval suite has to be a living asset that keeps growing as new failure modes are discovered.

## 3. Impact — potential & realized

The post is framed as lessons learned from evaluating GenAI products at scale inside Airbnb, presented as organizational and engineering practice rather than a single launch with headline metrics. The realized benefit described is process-level: teams that adopt EDD get a durable, growing regression-test suite specific to their product's actual failure modes, rather than a generic benchmark that may not reflect how the feature is really used or misused. The broader potential is that this discipline generalizes to any team shipping LLM-based features in production — the core insight (evaluation must be continuous and failure-mode-driven, not a fixed pre-launch gate) applies regardless of the specific product surface.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-packaged framework for a practice many teams already do ad hoc

"Keep adding test cases as you find bugs" isn't a new idea in software engineering, and treating LLM evaluation as an evolving suite rather than a fixed benchmark is already common informal practice at companies shipping GenAI features. What this piece adds is a clean name, a TDD-parallel framing that makes the discipline easier to sell internally, and Airbnb's specific account of doing it at production scale — useful for teams that haven't yet formalized what they're already half-doing, but not a new technique.

### Similar / related work

- [**Building Ask DoorDash (Part 3): Evaluation**](2026-09-22-doordash-ask-doordash-part3-evaluation.md) (in this bank) — DoorDash's parallel account of building LLM-as-judge and regression-testing infrastructure for a conversational AI product, a close industry analogue to Airbnb's EDD framing.
- [**A Simulation and Evaluation Flywheel to Develop LLM Chatbots**](2026-09-18-doordash-simulation-evaluation-flywheel-llm-chatbots.md) (in this bank) — another continuous-evaluation loop (simulated users plus LLM judges) aimed at the same underlying problem of non-deterministic, hard-to-benchmark LLM outputs.
- **Test-driven development (TDD)** (general software-engineering practice) — the traditional-software discipline this post explicitly positions eval-driven development as the GenAI analogue of.

### Jargon buster

- **Eval-driven development (EDD)** — a development discipline where an evolving suite of evaluation cases, built from real discovered failure modes, drives and gates iteration on an LLM-based feature, analogous to how a test suite drives traditional TDD.
- **LLM-as-judge** — using a large language model to score or grade another model's outputs against a rubric, often used to scale up evaluation of subjective or hard-to-automate criteria.
- **Non-determinism (in LLM outputs)** — the property that the same prompt can produce different outputs on different runs, which undermines simple fixed-input/fixed-output test assertions common in traditional software testing.
