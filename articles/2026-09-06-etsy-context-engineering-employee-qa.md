---
id: etsy-context-engineering-employee-qa
title: "Context Engineering Case Studies: Etsy-Specific Question Answering"
source: "Etsy Engineering (Code as Craft)"
url: "https://www.etsy.com/codeascraft/context-engineering-case-studies-etsy-specific-question-answering"
published: "2026-07"
added: "2026-09-06"
category: llm-genai
tags: [context-engineering, prompt-engineering, hallucination-detection, rag, employee-tools, evaluation]
novelty: 3
sourced_via: "web search"
---

# Context Engineering Case Studies: Etsy-Specific Question Answering

**Source:** [Etsy Engineering (Code as Craft)](https://www.etsy.com/codeascraft/context-engineering-case-studies-etsy-specific-question-answering) · Published 2026-07 · Added 2026-09-06
**Category:** LLMs & Generative AI · **Tags:** `context-engineering`, `prompt-engineering`, `hallucination-detection`, `rag`, `employee-tools`, `evaluation`

## TL;DR

Etsy piloted LLM-based question answering over Etsy-specific documents (starting with employee travel-and-expense policy, then seller/employee community-forum posts) and found that context engineering — feeding an off-the-shelf LLM well-chosen task-specific text rather than fine-tuning it — worked reasonably well, with one specific technique standing out for catching hallucinations: asking the model to cite the exact source snippet it used for each answer.

## 2. Technical details

Etsy compared two ways of specializing an LLM for internal question answering: fine-tuning (updating model weights on internal documents) versus context/prompt engineering (keeping the model frozen and supplying task-specific documents as context at inference time). They chose the prompt-engineering route as the pilot approach since it only requires assembling an adequate representation of the task-specific documents, avoiding the cost and operational overhead of fine-tuning. The pilot tested models from OpenAI's o-series and Google's Gemini family.

The first case study scoped narrowly to the Travel & Entertainment (T&E) section of Etsy's internal employee policies — a well-circumscribed domain with clear, unambiguous rules — and evaluated the system against a manually curated set of 40 question-and-answer pairs. Etsy then expanded the approach to a second, harder case study: mining both seller and employee posts in Etsy's public community forums to answer common seller-onboarding questions, a domain with far less clean, more conversational and inconsistent source material than a formal policy document.

Across both studies, techniques like explicitly allowing the model to express uncertainty, providing additional surrounding context, and asking the model to explain its reasoning were tried but were not consistently effective at improving reliability. The one technique that clearly helped: requiring the model to quote the specific source snippet it drew an answer from, which surfaced likely hallucinations — if the model couldn't point to a real source snippet supporting its claim, the answer was probably fabricated.

## 1. Business context

Employee and seller onboarding at a company Etsy's size runs into the same wall repeatedly: policies and procedures live scattered across internal wikis, formal documents, and community forum threads, and giving every new hire or seller a fast, reliable, self-serve way to get accurate answers is expensive to do with static documentation or a human support queue. LLM-based question answering is an obvious fit if — and only if — its answers can be trusted not to hallucinate policy details that never existed.

## 3. Impact — potential & realized

**Realized:** Etsy reports that prompt/context engineering worked "reasonably well" as a lower-cost alternative to fine-tuning across the two piloted domains (formal T&E policy and community-forum seller Q&A), and identifies source-snippet citation as a practical, low-cost hallucination-detection signal usable in future LLM QA systems. Specific accuracy numbers on the 40-question T&E benchmark were not disclosed in the source material.

**Potential:** The article frames its negative results — uncertainty prompts, added context, and explanation requests not reliably improving accuracy — as being as valuable as the positive one. That's a useful data point for any team defaulting to "just add more prompting tricks" before validating each one actually moves the needle on a held-out benchmark.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid, honestly-reported production engineering, not a new technique

Citing source snippets to catch hallucinations is a known RAG-adjacent pattern (attribution/grounding checks), not a novel invention. What makes this entry worth reading is Etsy's willingness to report which "obvious" prompting tricks (uncertainty framing, added context, chain-of-thought-style explanations) did *not* reliably help — that kind of negative result is underrepresented in company engineering blogs, which tend to only publish what worked.

### Similar / related work

- [**Reduce RAG Costs on Amazon Bedrock with Query-Aware Compression**](2026-09-02-aws-bedrock-query-aware-rag-compression.md) (in this bank) — another team's approach to grounding and hallucination control in a RAG-style pipeline, at a much larger scale.
- [**Our Early Journey to Transform Instacart's Discovery Recommendations with LLMs**](2026-09-02-instacart-llm-discovery-shopping-hub.md) (in this bank) — also layers an LLM-as-judge over generated content specifically to catch quality/faithfulness failures before they reach users.
- [**Sidekick's Continual Learning Loop**](2026-09-01-shopify-sidekick-continual-learning-loop.md) (in this bank) — a much more heavyweight approach (a calibrated LLM-judge plus RL) to the same underlying trust problem: how do you know an LLM's output is actually correct.

### Jargon buster

- **Context engineering** — the practice of deliberately curating and structuring the text supplied to an LLM at inference time (documents, instructions, examples) to steer its output, as an alternative to changing the model's weights.
- **Fine-tuning** — updating a pretrained model's internal weights on task-specific data, as opposed to leaving the weights frozen and relying purely on prompt content.
- **Hallucination** — an LLM generating a plausible-sounding but factually incorrect or fabricated statement, especially dangerous in a policy-answering context where wrong answers have real consequences.
