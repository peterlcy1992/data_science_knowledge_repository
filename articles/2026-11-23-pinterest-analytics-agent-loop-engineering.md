---
id: pinterest-analytics-agent-loop-engineering
title: "How Pinterest Improved Analytics Agent Compliance with Loop Engineering"
source: "Pinterest Engineering Blog"
url: "https://medium.com/pinterest-engineering/how-pinterest-improved-analytics-agent-compliance-with-loop-engineering-d3c52d0abaa2"
published: "2026-11"
added: "2026-11-23"
category: llm-genai
tags: [analytics-agent, agent-evaluation, prompt-optimization, regression-testing, eval-noise, holdout, data-discovery, llm-labeler]
novelty: 3
sourced_via: "full-text fetch"
---

# How Pinterest Improved Analytics Agent Compliance with Loop Engineering

**Source:** [Pinterest Engineering Blog](https://medium.com/pinterest-engineering/how-pinterest-improved-analytics-agent-compliance-with-loop-engineering-d3c52d0abaa2) · Published 2026-11 · Added 2026-11-23
**Category:** LLMs & Generative AI · **Tags:** `analytics-agent`, `agent-evaluation`, `prompt-optimization`, `regression-testing`, `eval-noise`, `holdout`, `data-discovery`, `llm-labeler`

> Fetching note: the Medium page returned 403; the full post text was read from the Pinterest Engineering RSS feed's full-content field.

## TL;DR

Pinterest's Analytics Agent answers data questions by searching tables, dashboards and metrics. It sometimes skipped required steps, such as inspecting table metadata before writing SQL. Manual prompt edits were trial and error, so the team built a "loop engineering" process. For each compliance rule, paired *required* and *skip* test suites plus a regression suite gate automated edits to prompts, skills, context and tools, with a final holdout. A first run scored 89.3%, but most of the gain came from one edit. Two runs of the same code flipped 10.3% of case verdicts, which led the team to judge changes case by case rather than by aggregate score.

## 1. Business context

The agent is "compliant" when it identifies and follows the steps that apply to a question:
- read the data-discovery skill when needed;
- inspect table metadata before SQL;
- search every relevant source type (tables, dashboards, metrics).

Skipping a step can produce a confident but wrong answer, using the wrong definition, pipeline stage or window. In chat logs, table searches outnumbered chart and dashboard searches by more than 10×. Even after manual instruction revisions, compliance on the read-the-skill rule was 64% across a broader population of chats. Manual edits also backfired: a scope guardrail caused the agent to decline an in-scope storage-cost question without searching.

## 2. Technical details

- **Paired suites per rule.** A focused LLM labeler, with humans reviewing its labels, decides (1) whether the rule applies and (2) whether the agent followed it. Applicable chats go to the *required* suite and the rest to the *skip* suite, so a chat passes if the agent followed the rule when required or skipped it when not. In one example, an edit fixed one required-dashboard chat but triggered unnecessary dashboard searches in two skip chats. Only the skip suite revealed the regressions.
- **Regression suite.** A much larger set; any change that drops it below the required level is rejected.
- **Loop design.** A persistent session accumulated too much context. A memoryless "Ralph Wiggum" loop cut estimated model cost about fivefold but repeated earlier mistakes. The final design starts each iteration fresh and passes a compact structured handoff: current scores, failing cases and their likely causes, best change so far, what not to repeat, suspected test problems, and what must not regress, with file and line limits.
- **Per iteration.** Draft up to four edits to the system prompt, skills, context layer or tools. Race them on the same ~dozen-case sample and keep the winner, preferring smaller edits on ties. Score the winner on the full tuning and validation suites. Cases are split into tuning, validation and a final holdout, which is opened once at the end.
- **Three rejection checks.** A repair/break gate (fixed more than it broke?), an acceptance critic (general fix, or hard-coded test answers?) and a regression guard. Edits are capped at a few files and a few dozen lines, and the cap shrinks over the run, so the loop cannot change application code to pass its own tests.

## 3. Impact — potential & realized

**Measured (Pinterest internal evaluation, Jul–Sep 2026, one trial per case, one base model "Claude 4.7 Opus Fast"; the LLM labeler is not calibrated against human labels):**
- The first large run reached 89.3% pooled pass rate across tuning and validation cases. There were 30 iterations and 4 accepted edits. The first edit did most of the work, and nothing was kept after iteration 20.
- Re-running the same code over the same cases flipped 23 verdicts, 10.3% of cases, while aggregate totals barely moved. Over all 223 cases, that is about one chance flip per ~12-case sample.
- The loop improved compliance on required cases while preserving the skip and regression suites. The skill-read suite was a separate 41-case set built from known failures, with a 0% baseline by design. The source-type improvement came from a backend change to the agent's search process, after two labeled datasets, a dozen iterations and two verification runs.
- The post states it has not measured answer quality directly.

**Potential:** A template for treating agent-prompt changes like experiments: paired positive and negative suites, holdouts, regression guards, and noise-aware acceptance.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Unusually honest about eval noise; the statistics are the story

Automated prompt optimization is not new. What stands out is the footnoted candour: one trial per case, an uncalibrated labeler, one model, and a 10.3% verdict-flip rate that makes small score gains meaningless. That flip rate is the eval equivalent of an A/A test. A natural next step is to treat it formally, with repeated trials per case, paired tests on fail→pass versus pass→fail flips (McNemar-style), and power calculations for the ~12-case racing sample. The required/skip pairing is a nice analogue to guardrail metrics in experimentation.

### Similar / related work

- [**Inside Vera, DoorDash's Data Agent**](2026-09-18-doordash-vera-data-agent.md) (in this bank) — another production analytics/data agent.
- [**Using MemAlign to Improve Evaluation of Traditional Machine Learning in Genie Code**](2026-09-18-databricks-memalign-llm-judges.md) (in this bank) — aligning LLM judges for data-science agents.
- [**Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads**](2026-10-06-arxiv-agentic-rag-evaluation-budget-allocation.md) (in this bank) — the statistics of how many trials an agent eval needs.

### Jargon buster

- **Compliance (agent)** — following the procedural steps that apply to a given question, and skipping those that don't.
- **Skip suite** — test cases where a rule should *not* fire; catches over-eager fixes.
- **Ralph Wiggum loop** — a memoryless agent loop that restarts from a fresh context every iteration.
- **Verdict flip rate** — the share of cases whose pass/fail changes between identical runs; a measure of eval noise.
