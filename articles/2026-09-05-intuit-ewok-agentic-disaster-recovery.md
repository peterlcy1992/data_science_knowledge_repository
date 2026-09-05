---
id: intuit-ewok-agentic-disaster-recovery
title: "How Intuit Built an Agentic Disaster Recovery Assistant with Amazon Bedrock"
source: "AWS Machine Learning Blog"
url: "https://aws.amazon.com/blogs/machine-learning/how-intuit-built-an-agentic-disaster-recovery-assistant-with-amazon-bedrock/"
published: "2026-09"
added: "2026-09-05"
category: ml-infra-serving
tags: [ai-agents, disaster-recovery, bedrock, guardrails, agentcore, on-call-tooling, langchain]
novelty: 3
sourced_via: "full-text fetch"
---

# How Intuit Built an Agentic Disaster Recovery Assistant with Amazon Bedrock

**Source:** [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/how-intuit-built-an-agentic-disaster-recovery-assistant-with-amazon-bedrock/) · Published 2026-09 · Added 2026-09-05
**Category:** ML Infrastructure & Serving · **Tags:** `ai-agents`, `disaster-recovery`, `bedrock`, `guardrails`, `agentcore`, `on-call-tooling`, `langchain`

## TL;DR

Intuit layered an LLM-driven "EWOK Agent" on top of its existing automated failover system so on-call engineers can trigger production disaster-recovery actions from a plain-language request instead of navigating tribal knowledge about policy exceptions — while keeping every action auditable, policy-compliant, and executed by deterministic code that the model never directly touches.

## 1. Business context

Intuit runs thousands of microservices across multiple AWS regions behind products like TurboTax, QuickBooks, and Mailchimp — 700+ services and digital experiences serving 100M+ customers, per the post. Its prior EWOK system already automated the *execution* of a regional failover once one was requested, bringing recovery time to roughly 20 minutes for supported workloads. The gap was upstream of execution: deciding whether and how to fail over required tribal knowledge — for example, knowing the specific emergency procedure for requesting a failover during a change-freeze window — that lived in experienced engineers' heads rather than in a system anyone on-call could reliably act on under pressure.

## 2. Technical details

EWOK Agent adds a model-driven decision layer in front of the existing, already-trusted execution system, built around a hard separation of concerns: **the model decides what to do; deterministic code decides how.**

- **Foundation model access.** The agent calls models through Amazon Bedrock's Converse API, treating the model choice as "a configuration value rather than an architectural commitment" so Intuit can swap or evaluate models without rearchitecting the system.
- **Skill layer.** Each capability the agent can invoke is encoded as a typed "skill" — a Markdown file pairing a YAML I/O schema with prompt instructions and explicit operation walkthroughs and error-handling rules. Skills compile into tool specifications the model can call.
- **Bounded agent loop.** Built with LangChain's `ChatBedrockConverse`, the loop calls the model with the compiled skill tools, branches on stop reasons (including guardrail interventions), executes the selected skill deterministically, feeds the structured result back to the model, and enforces a hard iteration ceiling so the loop cannot run away.
- **Execution boundary.** The model never holds AWS credentials and has no network path to the EWOK APIs; a separate executor holds credentials, calls the APIs, and returns typed JSON with explicit success/error status back to the model.
- **Layered safety controls:** Bedrock Guardrails with prompt-injection filtering on every model call; input validation of service names and regions before any API call; per-service job queues with deduplication and cool-down periods; circuit breakers against rapid repeated invocations; human-in-the-loop approval gates for critical or irreversible actions; immutable audit trails anchored to change records; least-privilege IAM scoping; and replay-attack prevention via nonces and timestamps.

## 3. Impact — potential & realized

**Realized:** the post reports that on-call teams have used EWOK Agent to run production failovers for eight months, inheriting the underlying EWOK system's ~20-minute recovery time for supported workloads. No quantitative before/after metrics (failover success rate, MTTR delta, incident count) are given — this is a qualitative case study of the architecture pattern rather than an experiment write-up.

**Potential:** the reusable takeaway is the pattern itself — encode operational capabilities as typed, schema-bound "skills"; keep the model confined to a tightly bounded decision loop; and enforce every safety-critical guarantee (credentials, auditability, rate limits) in conventional code rather than in the prompt. That template generalizes to any high-stakes operational domain (incident response, compliance actions, infrastructure changes) where teams want an LLM to reduce the cognitive load of *deciding* what to do without giving it authority over *how* it gets done.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-executed instance of an increasingly standard agentic-ops pattern

The "model proposes, deterministic code disposes, guardrails everywhere" architecture is becoming the default template for production agents that touch anything state-changing — this post doesn't introduce a new idea so much as document a clean, well-instrumented implementation of it for a genuinely high-stakes use case (regional failover). The lack of quantitative outcome metrics (vs. the qualitative "used for eight months") keeps this from scoring higher; the value is mostly in the architecture write-up itself as a reference design.

### Similar / related work

- [**Govern AI Agent Tool Access with Amazon Bedrock AgentCore Gateway**](../articles/2026-09-03-aws-bedrock-agentcore-gateway-governance.md) (in this bank) — the complementary governance layer (who/what an agent is allowed to call) to this post's execution-boundary pattern (how an approved call actually runs).
- [**How We Eliminated $1M/Year of Wasted AI Agent Spend in One Hour**](../articles/2026-09-02-databricks-agent-cost-tracing-mcp.md) (in this bank) — another production agent-ops story, focused on cost observability rather than safety-critical execution boundaries.

### Jargon buster

- **Bedrock Converse API** — Amazon Bedrock's unified interface for calling different foundation models with a consistent request/response format, so an application isn't tightly coupled to one model provider's API shape.
- **Guardrail intervention** — a case where a safety filter (e.g. Bedrock Guardrails) blocks or modifies a model's output or a tool call before it reaches the execution layer, which the agent loop here explicitly detects and branches on.
