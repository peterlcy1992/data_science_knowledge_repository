---
id: aws-agentcore-evaluations-framework-agnostic
title: "Evaluate Any Agent Framework with Amazon Bedrock AgentCore Evaluations"
source: "AWS Machine Learning Blog"
url: "https://aws.amazon.com/blogs/machine-learning/evaluate-any-agent-framework-with-amazon-bedrock-agentcore-evaluations/"
published: "2026-09"
added: "2026-10-02"
category: llm-genai
tags: [agent-evaluation, llm-as-judge, opentelemetry, observability]
novelty: 3
sourced_via: "web search"
---

# Evaluate Any Agent Framework with Amazon Bedrock AgentCore Evaluations

**Source:** [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/evaluate-any-agent-framework-with-amazon-bedrock-agentcore-evaluations/) · Published 2026-09 · Added 2026-10-02
**Category:** llm-genai · **Tags:** `agent-evaluation`, `llm-as-judge`, `opentelemetry`, `observability`

## TL;DR

AgentCore Evaluations decouples agent assessment from framework choice by reading OpenTelemetry spans, so the same evaluators (goal success, correctness, helpfulness, custom LLM-as-judge) run on agents built with LangGraph, LlamaIndex, OpenAI Agents SDK, Google ADK or Claude Agent SDK, both in CI and on sampled production traffic.

## 1. Business context

Evaluation tooling is usually coupled to a specific SDK or LLM client, so teams that mix agent frameworks end up with fragmented, non-comparable quality measurement.

## 2. Technical details

Agents emit OTLP telemetry to AWS Distro for OpenTelemetry, which routes spans to CloudWatch. The service rebuilds sessions from three span types: invoke-agent (prompt and final response), inference (model calls and message history) and execute-tool (tool name, parameters, results). Frameworks are identified via the scope.name attribute and routed to OpenTelemetry GenAI or OpenInference parsing paths. Built-in evaluators: GoalSuccessRate (session level), Correctness and Helpfulness (trace level), plus custom LLM-as-a-judge evaluators at session, trace or tool level. Two modes: on-demand (CI/CD with ground-truth expectations) and online (sampled production monitoring streamed to CloudWatch).

## 3. Impact — potential & realized

Per the post: removes framework-specific evaluation code and gives CI scores that are directly comparable to production metrics since both use the same pipeline. No quantitative benchmarks were reported in the summary reviewed.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid standards-based plumbing; the DS question of judge validity is left to the user.

Telemetry-level decoupling is the right abstraction. For data scientists the open issues are the usual ones: calibrating LLM judges against human labels and putting uncertainty on online sampled scores.

### Similar / related work

- [**Monitoring Production Agent Lifecycle with AWS DevOps Agent and AgentCore Evaluations**](2026-09-12-aws-devops-agent-agentcore-evaluations-monitoring.md) — in-bank sibling on the same service

### Jargon buster

- **OpenTelemetry** — Vendor-neutral standard for emitting traces, metrics and logs.
- **LLM-as-a-judge** — Using an LLM to score another model's outputs against a rubric.
- **Span** — One timed unit of work in a trace, e.g. a model call or tool call.
