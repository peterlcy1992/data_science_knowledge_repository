---
id: google-nested-learning-continual-learning-paradigm
title: "Introducing Nested Learning: A New ML Paradigm for Continual Learning"
source: "Google Research"
url: "https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/"
published: "2026-08"
added: "2026-09-01"
category: research-foundational
tags: [continual-learning, catastrophic-forgetting, associative-memory, architecture, neurips]
novelty: 4
sourced_via: "full-text fetch"
---

# Introducing Nested Learning: A New ML Paradigm for Continual Learning

**Source:** [Google Research](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/) · Published 2026-08 · Added 2026-09-01
**Category:** Research & Foundational · **Tags:** `continual-learning`, `catastrophic-forgetting`, `associative-memory`, `architecture`

## TL;DR

Google Research proposes **Nested Learning**, which reframes a model's
architecture and its optimizer as the same kind of thing — nested
optimization problems updating at different frequencies — as a way to fight
catastrophic forgetting. The accompanying **Hope** architecture, built on
the prior Titans framework, beats Transformer, Samba, and Titans baselines on
perplexity and accuracy, and outperforms TTT and Mamba2 on long-context
needle-in-a-haystack tasks. The work was published at NeurIPS 2025 (Behrouz,
Razaviyayn, Zhong, and Mirrokni) and surfaced via Google's research blog in
August 2026.

## 1. Business context

Today's LLMs are largely frozen after pretraining. Teaching them new
information after the fact tends to overwrite — **catastrophically forget**
— previously learned knowledge, unlike biological brains, which continually
learn without wholesale forgetting. This blocks any deployed model from
genuinely learning over time, which matters for any long-lived agent or
assistant that should keep improving from experience rather than being
frozen at a training cutoff.

## 2. Technical details

- **Core reframing.** Nested Learning treats a model as a system of
  interconnected, multi-level optimization problems solved simultaneously.
  It argues that a model's structural design (architecture) and its training
  rule (optimizer) are "fundamentally the same concepts" — just different
  levels of the same nested optimization structure — rather than separate
  design decisions.
- **Multi-time-scale updates.** Each component updates at its own frequency,
  echoing how biological brains process information across multiple
  frequency bands rather than at one uniform rate.
- **Associative memory framing.** Backpropagation and attention are modeled
  as associative memory modules that map a data point to the value of its
  local error — a lens for describing existing mechanisms rather than a new
  mechanism itself.
- **Context flow.** Each nested optimization level learns from its own
  distinct stream of information.
- **Deep optimizers.** Standard optimizers (e.g. momentum-based ones) are
  reformulated using an **L2-regression loss** instead of dot-product
  similarity, described as more resilient to imperfect data.
- **Continuum Memory System (CMS).** Extends the Transformer's short-term
  (attention) / long-term (feedforward) memory split into a spectrum of
  memory modules, each updating at its own specific frequency, to handle
  larger context windows.
- **Hope architecture.** A self-modifying recurrent architecture built on
  the prior [Titans](https://arxiv.org/abs/2501.00663) framework, adding
  unbounded levels of in-context learning via self-referential optimization
  — the model can optimize its own memory — plus CMS blocks for larger
  context.

## 3. Impact — potential & realized

- **Realized (benchmark, not production):** Hope shows lower perplexity and
  higher accuracy than Transformer, Samba, and Titans baselines on language
  modeling and reasoning benchmarks, and consistently outperforms TTT and
  Mamba2 on long-context Needle-In-Haystack tasks across three difficulty
  levels.
- **Potential:** a genuinely different way to design architectures aimed at
  continual learning without catastrophic forgetting — if it holds up at
  larger scale and real deployment traffic, which has not yet been reported.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a genuinely different conceptual frame, not yet proven at production scale

Proposing that "architecture" and "optimizer" are really the same
nested-optimization idea, expressed at different timescales, is a different
conceptual frame from most recent recurrent/hybrid-architecture papers, which
mostly compete on attention variants or memory mechanisms within a fixed
frame of "architecture trains under an optimizer." Hope backs the framing
with head-to-head benchmarks against several strong recent baselines
(Samba, TTT, Mamba2). It stops short of a 5 because everything reported is
academic-benchmark scale (perplexity, accuracy, NIAH) — the payoff for real
continual learning at production scale, which is the actual business
motivation, hasn't been demonstrated yet.

### Similar / related work

- [**Titans: Learning to Memorize at Test Time**](https://arxiv.org/abs/2501.00663) — the prior architecture Hope
  builds directly on, adding a neural long-term memory module that learns to
  memorize at test time.
- [**Nested Learning: The Illusion of Deep Learning Architectures**](https://arxiv.org/abs/2512.24695) — the full arXiv paper behind this blog
  post, with the formal Nested Learning framework and Hope architecture.
- General continual-learning literature on catastrophic forgetting — a
  long-running research area this work is positioned against, not tied to a
  single other paper.

### Jargon buster

- **Catastrophic forgetting** — a model overwriting previously learned
  knowledge when it learns something new.
- **Associative memory** — a memory model that retrieves a stored value from
  a partial or related cue; used here as a lens for describing how
  backpropagation and attention already behave.
- **Needle-in-a-haystack (NIAH)** — a benchmark testing whether a model can
  retrieve a small piece of relevant information hidden inside a very long
  context.
