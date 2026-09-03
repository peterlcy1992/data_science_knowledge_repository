---
id: meta-second-brain-expert-ai-agent
title: "An Organizational Second Brain: Building an AI That Learns From Experts"
source: "Engineering at Meta"
url: "https://engineering.fb.com/2026/09/02/ml-applications/organizational-second-brain-ai-learns-from-experts/"
published: "2026-09"
added: "2026-09-03"
category: llm-genai
tags: [llm-agents, knowledge-management, rag, self-improving-systems, compliance]
novelty: 3
sourced_via: "full-text fetch"
---

# An Organizational Second Brain: Building an AI That Learns From Experts

**Source:** [Engineering at Meta](https://engineering.fb.com/2026/09/02/ml-applications/organizational-second-brain-ai-learns-from-experts/) · Published 2026-09 · Added 2026-09-03
**Category:** LLMs & Generative AI · **Tags:** `llm-agents`, `knowledge-management`, `rag`, `self-improving-systems`, `compliance`

## TL;DR

Meta built an internal AI agent — first applied to compliance assessment work — that codifies specialist knowledge into a structured, dependency-tracked knowledge base, separates declarative facts from imperative reasoning "recipes" to cut prompting token cost roughly 80%, and self-improves by diagnosing expert corrections back to root causes through an automated, regression-tested edit pipeline.

## 1. Business context

Domain-expert knowledge — initially in compliance assessment — tends to live in individual people's heads, which produces two costly problems: assessments become inconsistent because different experts reason differently about similar cases, and those same experts spend a large share of their time answering routine, repetitive questions instead of doing higher-value work. Meta frames the system as generalizable beyond compliance to finance, security, and engineering-standards domains that share the same "expert bottleneck" shape.

## 2. Technical details

- **Structured knowledge base:** over 200 files organized by a taxonomy — position files capturing organizational stances, taxonomy/vocabulary files serving as authoritative glossaries, routing indexes, and gateway/threshold-test files — each declaring its dependencies in YAML frontmatter to form an auditable, bidirectional dependency graph.
- **Recipes as imperative reasoning:** "recipes" separate declarative knowledge (facts) from imperative procedures (how an expert actually works through a case), enabling "progressive disclosure" — surfacing only the instructions relevant to the current phase of reasoning instead of a single monolithic prompt. This is reported to cut token consumption by roughly 80% versus the team's earlier monolithic-prompting approach.
- **Retrieval strategy:** high-density, frequently needed material is served from a structured wiki; sparse or situational material is retrieved via a combination of semantic and lexical (hybrid) RAG search.
- **Self-improvement pipeline, four phases:** (1) diagnose an expert's correction back to its root cause, (2) compile a minimal, verified edit, (3) validate the edit via replay against past cases and regression tests, (4) incorporate the case into the test suite going forward — with independent adversarial review and deterministic structural validation to catch contradictions before they land.
- The specific underlying LLM(s) powering the system are not disclosed in the source article.

## 3. Impact — potential & realized

- **Realized:** subject-matter experts rated the system's outputs as "useful almost all the time"; assessment turnaround dropped from days to minutes; zero regressions introduced across improvement cycles in the reported period; the initial system was built in six weeks across three sprints.
- **Potential:** the write-up frames the dependency-graph knowledge base, recipe-based progressive disclosure, and root-cause-diagnosing self-improvement loop as a reusable pattern for any domain where expert reasoning is currently locked in individuals — explicitly naming finance, security, and engineering-standards work as likely next applications.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a well-engineered, disciplined take on an increasingly common RAG-agent pattern

Splitting declarative knowledge from imperative "recipes" for progressive disclosure, and building a self-improvement loop that diagnoses root causes from expert corrections rather than just appending new examples, is a genuinely disciplined piece of engineering — the 80% token reduction from progressive disclosure and the zero-regression track record from the validation pipeline are the most concrete, exportable results here. It's a 3 rather than higher because the core ingredients (structured knowledge bases, hybrid RAG, human-in-the-loop correction pipelines) are all established techniques; the contribution is in how carefully they're composed and validated for a compliance-grade use case, not a new modeling idea.

### Similar / related work

- [**How We Eliminated $1M/Year of Wasted AI Agent Spend in One Hour**](2026-09-02-databricks-agent-cost-tracing-mcp.md) (in this bank) — a different agent-operations concern (tracing and cost debugging) rather than knowledge structuring, but shares the theme of treating production agent systems as needing dedicated engineering discipline rather than ad hoc prompting.
- [**Delegating Engineering Work to Cloud-Based Agents (Flux)**](2026-08-27-doordash-flux-cloud-agents-engineering.md) (in this bank) — another production agent system built around structured process and validation guardrails, there for engineering work rather than compliance assessment.

### Jargon buster

- **Progressive disclosure** — surfacing only the information relevant to the current step of a task, rather than loading everything a system might ever need into context at once.
- **Hybrid RAG (semantic + lexical search)** — combining meaning-based embedding search with traditional keyword search when retrieving supporting documents, to catch both conceptual matches and exact-term matches.
- **YAML frontmatter** — a block of structured metadata (here, declared dependencies) placed at the top of a document, machine-readable separately from the document's main content.
- **Regression test (in an agent-correction context)** — a stored past case that a proposed knowledge-base edit must still handle correctly, used to catch edits that fix one problem while silently breaking another.
