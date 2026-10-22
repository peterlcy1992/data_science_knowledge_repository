---
id: arxiv-prompts-to-posteriors-llm-bayesian-inference
title: "From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?"
source: "arXiv cs.AI (Filbry, Melo & Gal)"
url: "https://arxiv.org/abs/2610.29331"
published: "2026-10"
added: "2026-10-22"
category: llm-genai
tags: [bayesian-inference, llm-evaluation, tool-use, belief-updating, reasoning]
novelty: 4
sourced_via: "web search"
---

# From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?

**Source:** [arXiv cs.AI (Filbry, Melo & Gal)](https://arxiv.org/abs/2610.29331) · Published 2026-10 · Added 2026-10-22
**Category:** llm-genai · **Tags:** `bayesian-inference`, `llm-evaluation`, `tool-use`, `belief-updating`, `reasoning`

## TL;DR

LLMs used for hypothesis generation and experiment design need to update beliefs as evidence arrives. The authors test whether they do so in a Bayes-consistent way: without tools they generally violate Bayes' rule, but reasoning plus code execution markedly improves results, even approximating intractable posteriors.

## 1. Business context

LLM agents are increasingly used in scientific and analytical workflows: reviewing literature, generating hypotheses, designing experiments. Each requires continually revising beliefs, which Bayesian inference formalizes. Prior work assumed LLMs cannot do principled Bayesian updating in context and relied on heuristics around them; this paper checks that assumption.

## 2. Technical details

The evaluation framework has three parts: (1) qualitative epistemological examples probing probabilistic coherence, (2) quantitative benchmarks of Bayesian inference ability, assessing both internal consistency and recovery of an externally determined posterior, and (3) analysis of how non-Bayesian updates affect downstream task performance. Submitted 21 Oct 2026 (10 pages, 6 figures). The abstract does not name the models, datasets or metrics, so those are not reported here.

## 3. Impact — potential & realized

Realized (as reported): without tools LLMs generally violate Bayes' rule when updating in context; with modern reasoning abilities and code execution, performance improves substantially. The authors argue tool-equipped LLMs could already support complex belief updates in scientific work. Numbers were not available at abstract level. Potential: a template for auditing agentic analysis assistants on inference quality, not just answer accuracy.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Frames a testable, DS-relevant question (do agents update like a Bayesian?) and the headline, tools rescue what raw reasoning lacks, is practical

Novelty 4/5 - Frames a testable, DS-relevant question (do agents update like a Bayesian?) and the headline, tools rescue what raw reasoning lacks, is practical. Caveat: abstract-level read with no model names or numbers visible.

### Similar / related work

- [**Selling in the Wild**](2026-10-20-arxiv-selling-in-the-wild-sales-agent-field-rct.md) (in this bank) — evaluating LLM agents with controlled evidence rather than vibes
- [**Neutral Launches and Expected Bayesian Loss**](2026-10-12-arxiv-neutral-launches-expected-bayesian-loss.md) (in this bank) — Bayesian decision framing for experiment readouts
- [**ACED-Bench: Evaluating How LLM Agents Acquire and Act on Causal Evidence**](https://arxiv.org/abs/2610.14381) — sibling benchmark on agents' use of evidence

### Jargon buster

- **Posterior** — The updated probability distribution over an unknown after combining prior belief with observed evidence.
- **In-context updating** — Revising beliefs from evidence placed in the prompt, without retraining the model.
- **Intractable posterior** — One with no closed form, usually approximated by sampling or numerical methods, which code execution makes feasible for an agent.
