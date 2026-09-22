---
id: doordash-ask-doordash-part3-evaluation
title: "Building Ask DoorDash (Part 3): Evaluation"
source: "DoorDash Engineering Blog"
url: "https://careersatdoordash.com/blog/building-ask-doordash-part-three-evaluation/"
published: "2026-06"
added: "2026-09-22"
category: llm-genai
tags: [llm-evaluation, agent-evaluation, llm-as-judge, regression-testing, conversational-ai]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Building Ask DoorDash (Part 3): Evaluation

**Source:** [DoorDash Engineering Blog](https://careersatdoordash.com/blog/building-ask-doordash-part-three-evaluation/) · Published 2026-06 · Added 2026-09-22
**Category:** LLMs & Generative AI · **Tags:** `llm-evaluation`, `agent-evaluation`, `llm-as-judge`, `regression-testing`, `conversational-ai`

## TL;DR

DoorDash's Ask DoorDash conversational agent had a quality-signal problem: before this work, the team's daily view into how well the agent was actually performing came from roughly one employee-submitted feedback report a day. Their evaluation harness — combining OpenTelemetry-based transcript reconstruction, repeatable conversation simulators, rubric-based scoring, and calibrated LLM judges — scaled that to 2,000 auto-graded sessions per day and cut full regression testing from over 6 hours of manual work to about 20 minutes, directly enabling an 8-point quality-score improvement ahead of a nationwide launch.

## 1. Business context

Ask DoorDash is a conversational AI assistant, and like most LLM-powered products, its failure modes are often subtle — not a crash, but a response that's technically well-formed yet unhelpful, evasive, or wrong in a way that quietly erodes user trust rather than triggering an obvious error. Catching those failures at meaningful scale requires being able to grade conversations automatically and continuously, not wait for the rare employee who happens to notice and file feedback. Before this evaluation harness, DoorDash's quality signal was effectively ~1 feedback report/day — nowhere near enough coverage to catch regressions before they reached users, and nowhere near enough to support fast iteration on the agent as new capabilities shipped. This is also a prerequisite problem: launching an LLM-powered assistant nationwide requires confidence that quality won't silently regress as usage scales, and that confidence has to come from measurement, not intuition.

## 2. Technical details

The evaluation harness has four main components working together:

1. **Transcript builders.** Reconstruct full conversational sessions from **OpenTelemetry traces** — the same observability data already being emitted for operational monitoring gets repurposed as the raw material for quality evaluation, avoiding the need for a separate logging pipeline just for eval.
2. **Conversation simulators.** Generate repeatable test scenarios from fixtures, letting the team run the same defined set of test conversations against a new model or prompt version every time, rather than relying only on whatever real traffic happens to occur.
3. **Rubric-based evaluation criteria.** Explicit, structured grading criteria define what "good" looks like for a given conversation type, giving the automated grading step a concrete standard to grade against rather than an open-ended quality judgment.
4. **Calibrated LLM judges.** LLMs automate the actual grading against those rubrics, with the judges calibrated against **human-labeled** examples so their scores track what a human rater would actually say — the calibration step is what makes it credible to trust LLM-graded scores as a stand-in for the human feedback that used to be the only signal.

Together, these let the team run both **continuous production monitoring** (auto-grading a sample of real sessions daily) and **on-demand regression testing** (running the simulator's fixture set against a candidate change before shipping it) off the same underlying evaluation infrastructure.

## 3. Impact — potential & realized

**Realized:** the harness scaled daily quality-monitoring coverage from **~1 employee-submitted feedback report** to **2,000 auto-graded sessions per day**, and cut comprehensive regression testing from **more than 6 hours** of manual work down to **about 20 minutes**. The broadened signal let the team catch trust-damaging failure modes sooner and prioritize fixing the most frequently recurring ones, contributing to an **8-point improvement in agent quality scores** and roughly **halving the error rate**, which the team credits with getting the assistant to the quality bar needed ahead of its nationwide launch.

**Potential:** the four-part pattern here — reuse existing observability traces for eval, maintain a repeatable simulated test suite, ground grading in explicit rubrics, and calibrate LLM judges against human labels rather than trusting them blind — is a directly transferable blueprint for any team building conversational or agentic LLM products that need both continuous production quality monitoring and fast pre-ship regression testing from one shared evaluation system.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid, well-instrumented engineering rather than a new evaluation technique

LLM-as-judge grading, rubric-based evaluation, and regression test suites are all established practice individually — the value here isn't a new evaluation method but the specific engineering choice to reuse existing OpenTelemetry observability data as the substrate for transcript reconstruction, unifying production monitoring and pre-ship regression testing on one pipeline instead of building them as separate systems. The reported scale jump (1/day to 2,000/day) and the concrete business outcome (8-point quality improvement ahead of a real launch deadline) make this a credible, well-quantified case study of eval infrastructure actually mattering operationally, even if the individual techniques are familiar.

### Similar / related work

- [**Building Ask DoorDash (Part 4): A Platform for Building and Evolving Agents**](2026-09-07-doordash-ask-doordash-part4-agent-platform.md) (in this bank) — the next installment in the same series, covering the platform that builds on this evaluation foundation to develop and evolve the agent further.
- [**Building Ask DoorDash (Part 5): A Grounded Interface For Shopping Agents**](2026-09-06-doordash-ask-doordash-grounded-shopping-interface.md) (in this bank) — a later installment applying the Ask DoorDash platform to a shopping-agent interface, downstream of the evaluation work described here.
- [**A Simulation and Evaluation Flywheel to Develop LLM Chatbots**](2026-09-18-doordash-simulation-evaluation-flywheel-llm-chatbots.md) (in this bank) — a closely related DoorDash evaluation system covering similar simulation-plus-grading territory, worth reading alongside this one for how the company's eval approach evolved across products.

### Jargon buster

- **OpenTelemetry** — an open-source observability standard for capturing traces, metrics, and logs from running systems; here, traces originally captured for operational monitoring are repurposed to reconstruct full conversation transcripts for evaluation.
- **LLM-as-judge** — using a large language model to automatically grade the quality of another model's (or agent's) output against defined criteria, in place of (or to scale up) human review.
- **Calibration (of an LLM judge)** — the process of checking and adjusting an LLM judge's scores against a set of human-labeled examples, to confirm the automated grades actually track what a human evaluator would conclude before trusting the judge to grade at scale.
- **Rubric-based evaluation** — grading against an explicit, structured set of criteria for what counts as a good or bad response, rather than an open-ended subjective judgment, which makes automated grading more consistent and auditable.
