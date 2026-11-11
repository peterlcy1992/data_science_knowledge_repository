---
id: uber-file-semantic-analyzer-outbound-data
title: "Building a File Semantic Analyzer: Guarding Outbound Data at Scale with AI"
source: "Uber Engineering Blog (Deepak Sharma, Aditya Kumar, Shubham Sonkar)"
url: "https://www.uber.com/us/en/blog/ubers-file-analyzer/"
published: "2026-06"
added: "2026-11-11"
category: llm-genai
tags: [data-loss-prevention, LLM-classification, summarization, human-in-the-loop, security]
novelty: 2
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Building a File Semantic Analyzer: Guarding Outbound Data at Scale with AI

**Source:** [Uber Engineering Blog (Deepak Sharma, Aditya Kumar, Shubham Sonkar)](https://www.uber.com/us/en/blog/ubers-file-analyzer/) · Published 2026-06 · Added 2026-11-11
**Category:** llm-genai · **Tags:** `data-loss-prevention`, `LLM-classification`, `summarization`, `human-in-the-loop`, `security`

## TL;DR

Uber's security team replaced keyword/pattern-based DLP triage with an LLM pipeline that extracts, chunks, summarises and classifies outbound files as business-critical, personal or neutral, with explanations feeding a rule engine and human review. Reported: 97% fewer false positives, ~5 minutes saved per file and incident response cut from hours to minutes.

## 1. Business context

Files leave the company via email, cloud uploads and USB drives; traditional DLP works on keywords and patterns, which the post says produces high false positives and false negatives (a personal note marked 'confidential' vs a sensitive plan with no keywords), causing alert fatigue for security analysts. The goal: classify outbound files by meaning and give analysts a human-readable summary.

## 2. Technical details

Labelled ground truth: an anonymised file set labelled by subject-matter experts as Business Critical, Personal or Neutral. Pre-processing: ingestion from sources such as Google Drive and internal file shares, text extraction across PDFs, docs, spreadsheets, presentations and HTML, OCR for images, and chunking by paragraphs, sections or semantic topics to stay within token limits.

Interpretation engine: each chunk goes to a fine-tuned large LLM that summarises, extracts entities and sensitive key phrases, relates information across sections, and gives a probabilistic assessment of intent/criticality with an explanation. Outputs feed a rule-based policy engine (e.g. alert if an 'Unreleased Product Specification' goes to an external domain; don't alert on 'Personal Vacation Photos'). High-fidelity findings go to analysts, whose feedback refines prompts and fine-tuning. The post names hallucination, context loss and autonomous errors as risks and the explanation requirement, chunking and human review as mitigations. The specific model is not named.

## 3. Impact — potential & realized

Realized (as reported by Uber, no evaluation methodology given): false positives cut by 97% with 'fewer missed true positives'; incident response for data exfiltration from multiple hours to a few minutes per case; ~5 minutes saved per file at an expected 150,000 files/year, which they put at 4 person-years. Potential: multimodal analysis of images, video and audio, and replacing keyword matching in DLP enforcement with semantic classification.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — A clear production pattern (LLM triage + rules + human review), light on measurement detail.

The architecture is sensible and generic; the interesting DS angle is what's missing — how the 97% false-positive reduction and recall were measured, on what sample, against which baseline. Anyone building similar LLM triage should treat the SME-labelled set as an evaluation asset with fixed splits and report precision/recall by class, not only alert-volume reductions.

### Similar / related work

- [**From Generation to Scoring: Scaling LLM-Based Semantic Labeling at LinkedIn**](2026-11-04-linkedin-from-generation-to-scoring-llm-semantic-labeling.md) — in this bank: LLM-based semantic classification at scale
- [**Auditing LLM Pseudo-Label Distillation for Review Informativeness at E-Commerce Scale**](2026-11-11-hepsiburada-auditing-llm-pseudo-label-distillation-review-informativeness.md) — in this bank: a contrasting example of rigorous evaluation of LLM labels

### Jargon buster

- **DLP** — Data loss prevention: tooling that detects and blocks sensitive data leaving an organisation.
- **Chunking** — Splitting a long document into coherent segments that fit an LLM's context window.
- **Human-in-the-loop** — Routing model outputs to people for validation before action, with their feedback used to improve the system.
