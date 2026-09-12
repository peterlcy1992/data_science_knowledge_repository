---
id: confluent-agentic-soc-streaming-investigation
title: "Building an Agentic SOC on a Stream"
source: "Confluent Blog"
url: "https://www.confluent.io/blog/building-an-agentic-soc-on-a-stream"
published: "2026-09"
added: "2026-09-12"
category: llm-genai
tags: [agentic-ai, security-operations, streaming, kafka, flink, multi-agent, alert-triage]
novelty: 3
sourced_via: "full-text fetch"
---

# Building an Agentic SOC on a Stream

**Source:** [Confluent Blog](https://www.confluent.io/blog/building-an-agentic-soc-on-a-stream) · Published 2026-09 · Added 2026-09-12
**Category:** LLMs & Generative AI · **Tags:** `agentic-ai`, `security-operations`, `streaming`, `kafka`, `flink`, `multi-agent`, `alert-triage`

## TL;DR

Confluent's own security team rebuilt their Security Operations Center's alert pipeline as a streaming multi-agent system on Kafka and Flink, and in a 30-day run it fully investigated all ~4,700 incoming alerts — versus roughly 3% previously reaching a human analyst — surfacing 250+ true positives from the low-priority tail that used to go unreviewed.

## 1. Business context

Detection was never the bottleneck for Confluent's SOC — generating alerts is easy; investigating every one of them at human speed is not. Over a 30-day baseline period, the team received roughly 4,700 alerts, but only about 3% reached on-call analyst review; the rest, especially lower-priority classes like Data Loss Prevention warnings, went essentially unreviewed. That's the classic "denominator problem" in security operations: attackers who understand this dynamic deliberately hide in the high-volume, low-fidelity alert stream that humans don't have time to check.

## 2. Technical details

Rather than organizing agents by detection source, Confluent organized them by evidence domain:

- **Triage Coordinator** — reviews incoming alerts and routes anything non-trivial into deeper investigation.
- **Evidence agents** — specialists for particular evidence types (e.g., endpoint forensics, cloud audit trails) that gather and interpret domain-specific signal.
- **Evaluator agent** — performs adversarial review of the investigation's conclusions, specifically hunting for unsupported claims before anything gets escalated.
- **Self-learning knowledge base** — a hybrid vector-plus-keyword search store that accumulates investigation history over time.

The whole pipeline runs on **Confluent Cloud with Apache Flink** for stream processing and **Apache Kafka** topics for agent telemetry, with priority-based routing so critical alerts bypass queued lower-priority volume. A "Real-Time Context Engine" streams live SOC state to agents within seconds, so an agent's evidence-gathering reflects near-current system state rather than a stale snapshot. Investigations are genuine hypothesis-driven work rather than simple classification — the system forms a hypothesis and queries systems for supporting or contradicting evidence, which the write-up notes takes minutes per alert rather than the seconds a classifier would take, in exchange for substantive reasoning behind each verdict. Low-severity conclusions can auto-close; anything higher-severity still requires human sign-off before action.

## 3. Impact — potential & realized

**Realized:** over the 30-day measurement period, 100% of the roughly 4,700 incoming alerts received full investigation (versus ~3% reaching human review previously), with about 5% of investigated alerts escalated and more than 250 true positives surfaced — concentrated in exactly the low-priority alert classes that had previously gone unreviewed.

**Potential:** the evidence-domain agent organization (rather than detection-source organization) plus the streaming substrate is offered as a general pattern for any high-volume, low-fidelity alert environment, not specific to Confluent's own tooling — the core claim is that a streaming architecture lets full-coverage investigation scale to alert volumes that would otherwise force selective triage.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-instrumented production case study of an increasingly common pattern

Multi-agent alert triage with an adversarial evaluator step is becoming a recognizable pattern in agentic security tooling; what's distinctive here is building it natively on a streaming substrate (Kafka/Flink) rather than a batch or request-response pipeline, which is a sensible fit for a security vendor that already sells that substrate. The reported jump from 3% to 100% alert coverage is a meaningful operational result, though it's a vendor's own dogfooding case study on their own infrastructure — the numbers describe outcomes for Confluent's SOC specifically, and how the ~5% escalation rate and true-positive count would transfer to a different alert mix or a different organization's tooling isn't established here.

### Similar / related work

- [**Monitoring Production Agent Lifecycle with AWS DevOps Agent and AgentCore Evaluations**](2026-09-12-aws-devops-agent-agentcore-evaluations-monitoring.md) (in this bank) — a similar autonomous-investigation pattern applied to infrastructure incidents rather than security alerts, useful contrast on webhook-triggered vs. continuous-streaming architectures for the same "autonomous on-call investigator" idea.
- [**AutoLR: Automating the Path from Research to Launch Review**](2026-09-08-netease-autolr-agentic-recsys-launch-review.md) (in this bank) — a different domain (recsys launch review) that shares this article's core structural idea of an adversarial evaluator agent checking another agent's conclusions before anything ships or escalates.
- **Security Operations Center (SOC) alert fatigue literature** — a broad, well-established body of security-operations research on the "denominator problem" this article frames its motivation around; no single canonical URL.

### Jargon buster

- **SOC (Security Operations Center)** — the team and tooling responsible for monitoring, triaging, and responding to security alerts across an organization's systems.
- **Adversarial review (in an agent pipeline)** — a dedicated step where a separate agent actively tries to find flaws or unsupported claims in another agent's conclusion, rather than simply approving it.
- **Apache Kafka / Apache Flink** — Kafka is a distributed event-streaming platform for passing high-volume message streams between systems; Flink is a stream-processing engine that computes over those streams in near real time, together forming the backbone this pipeline uses instead of a batch job.
