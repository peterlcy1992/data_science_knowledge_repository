---
id: aws-model-agnostic-pii-detection-llms
title: "Model-Agnostic PII Detection with LLMs"
source: "AWS Machine Learning Blog"
url: "https://aws.amazon.com/blogs/machine-learning/model-agnostic-pii-detection-with-llms/"
published: "2026-09"
added: "2026-09-24"
category: llm-genai
tags: [pii-detection, prompt-engineering, bedrock, responsible-ai, privacy]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Model-Agnostic PII Detection with LLMs

**Source:** [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/model-agnostic-pii-detection-with-llms/) · Published 2026-09 · Added 2026-09-24
**Category:** LLMs & Generative AI · **Tags:** `pii-detection`, `prompt-engineering`, `bedrock`, `responsible-ai`, `privacy`

## TL;DR

AWS researchers show that PII detection logic can live entirely in an LLM prompt instead of a model's trained weights, making the detector swappable across backends (Bedrock-managed or self-hosted) and extensible to new, domain-specific entity types without retraining — extended-entity F1 jumped from ~12% to ~73% just by adding custom categories to the prompt.

## 1. Business context

Detecting personally identifiable information in free-text data — before it's used for training, analytics, or shared downstream — has traditionally relied on token-classification models with a fixed set of entity types baked in at training time. Adding a new entity type (say, an internal employee ID format, or a domain-specific medical record number) means retraining and redeploying the model, which is slow and creates a maintenance burden any time detection requirements shift. That rigidity is a bigger problem than it looks: PII requirements vary by industry, jurisdiction, and even by internal data-governance policy, and a detector that can't adapt without a retraining cycle becomes a bottleneck for any team trying to ship compliant data pipelines quickly.

## 2. Technical details

The core design choice is to make **detection logic prompt-resident rather than weight-resident**: the LLM is given the text plus instructions defining the target entity types and the expected JSON output schema, and it returns structured detections directly, with no fine-tuning step. Two architectural principles keep this practical in production:

- **Instruction-driven detection** — because the entity definitions live in the prompt, switching to a new entity type or domain is a prompt edit, not a training run.
- **A uniform "Inferencer" interface** — a configurable backend abstraction lets the same detector code call either Amazon Bedrock-managed models or self-hosted open models interchangeably, so the detection logic is genuinely model-agnostic, not just entity-agnostic.

A post-processing layer recovers exact character offsets for each detected span (since LLMs return text, not indices) and reconciles label variations through morphological matching and alias tables — necessary because different LLMs may name the same entity type slightly differently (e.g., "PERSON" vs. "PERSON_NAME").

The team evaluated nine LLM-based detectors across five public datasets (49,365 records, 222,114 ground-truth spans, eight languages), and separately tested how well the approach handled custom, non-standard entity categories added purely via prompt instructions.

## 3. Impact — potential & realized

Reported results: core-entity F1 ranged 74.9–83.1% across the nine detectors tested, roughly matching a dedicated baseline tool (PrivacyFilter at 80.7% F1); the best-performing open model tested (OSS-GPT 20B) scored 81.6% F1 self-hosted on EC2 and 81.3% via Bedrock — near-parity between the two backends, supporting the model-agnostic claim. The standout result is extensibility: F1 on extended, domain-specific entity categories rose from roughly 12% to roughly 73% simply by adding those categories to the prompt, with zero retraining. Latency ranged 0.43–15.31 seconds per detection depending on model choice — a real cost that would matter for high-throughput pipelines. The realized value is a detector that adapts to new entity types on the same day requirements change; the broader potential is treating PII/compliance detection as a prompt-engineering problem across any regulated-data pipeline, not a model-training problem.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sensible application, not a new detection method

Using LLMs as zero-shot/few-shot entity extractors is now a well-worn pattern; what's specific and useful here is the systematic evaluation across nine detectors and eight languages, and the clean quantification of the extensibility win (12% → 73% F1 on custom entities with zero retraining) — a number that makes a concrete case for prompt-resident detection over classifier retraining that most practitioners will recognize as directly actionable. The core-entity F1 numbers (mid-70s to low-80s) aren't a leap over specialized NER-based PII tools; the pitch is operational flexibility, not raw accuracy, and that's a fair trade for teams with entity requirements that change often.

### Similar / related work

- **Microsoft Presidio** ([github.com/microsoft/presidio](https://github.com/microsoft/presidio)) — the closest widely-used open-source PII-detection toolkit, built on a fixed-recognizer architecture (rule-based plus classical NER) that this LLM-prompt approach trades accuracy-per-entity for reconfigurability against.
- General LLM-as-annotator / zero-shot NER literature — the broader body of work this technique builds on, applying instruction-following LLMs to structured extraction tasks without task-specific fine-tuning.

### Jargon buster

- **PII (Personally Identifiable Information)** — any data that could identify a specific individual (names, emails, ID numbers, etc.), which regulated pipelines must detect and typically redact or mask before further use.
- **Token classification (NER)** — the traditional approach to this problem: a model trained to label each word/token in text with an entity type, requiring retraining whenever the entity taxonomy changes.
- **Model-agnostic** — here, meaning the detection logic (the prompt) is independent of which underlying LLM executes it, so swapping the backend model doesn't require rewriting the detector.
