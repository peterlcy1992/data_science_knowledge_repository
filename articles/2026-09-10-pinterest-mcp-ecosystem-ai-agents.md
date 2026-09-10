---
id: pinterest-mcp-ecosystem-ai-agents
title: "Building an MCP Ecosystem at Pinterest"
source: "Pinterest Engineering Blog"
url: "https://medium.com/pinterest-engineering/building-an-mcp-ecosystem-at-pinterest-d881eb4c16f1"
published: "2026-03"
added: "2026-09-10"
category: ml-infra-serving
tags: [mcp, ai-agents, internal-tooling, security, developer-productivity, pinterest]
novelty: 3
sourced_via: "web search"
---

# Building an MCP Ecosystem at Pinterest

**Source:** [Pinterest Engineering Blog](https://medium.com/pinterest-engineering/building-an-mcp-ecosystem-at-pinterest-d881eb4c16f1) · Published 2026-03 · Added 2026-09-10
**Category:** ML Infrastructure & Serving · **Tags:** `mcp`, `ai-agents`, `internal-tooling`, `security`, `developer-productivity`, `pinterest`

## TL;DR

Pinterest built a production-grade Model Context Protocol (MCP) ecosystem to let internal AI agents safely automate engineering tasks, choosing multiple domain-specific cloud-hosted MCP servers (Presto, Spark, Airflow, Knowledge, and more) connected via a central registry over a single monolithic server. A two-layer JWT/service-mesh authorization model with fine-grained per-tool policies and mandatory security review governs access, and the post reports directional metrics of roughly 66,000 monthly invocations, 844 monthly active users, and about 7,000 hours of estimated monthly time saved.

## 1. Business context

Pinterest needed to move past one-off, hand-built integrations between LLMs and each internal system they wanted an agent to touch. The goal was a standardized, scalable, and secure way to connect LLMs to internal infrastructure — data querying (Presto), compute jobs (Spark), pipeline orchestration (Airflow), and internal documentation — without every team reinventing authentication, logging, and access control for their own tool integration. MCP (Model Context Protocol), the open standard for connecting LLMs to external tools and data, gave them a common interface to standardize around.

## 2. Technical details

Pinterest deliberately chose **cloud-hosted** MCP servers over local deployments, and **multiple domain-specific servers** rather than one monolithic server — each server owns a small, coherent set of tools tied to a single infrastructure domain (Presto for data queries, Spark for compute jobs, Airflow for pipeline orchestration, Knowledge for documentation retrieval, and others). A **central registry** acts as the source of truth for which MCP servers are approved and how AI clients — an internal AI chat platform, agents on the internal communications platform, and IDE integrations — discover and validate them. A unified deployment pipeline handles the infrastructure for standing up new servers, with shared library functions providing consistent logging and telemetry across all of them.

**Security** runs on a two-layer authorization model: an end-user flow using JWT-based authentication through Pinterest's internal auth stack (with Envoy validating tokens and extracting identity/group membership into request headers), and a SPIFFE-based service-mesh authentication layer for lower-risk, read-only scenarios. Access to sensitive servers like Presto is gated by business group (restricted to Ads, Finance, and specific infrastructure teams), enforced further by fine-grained, tool-level authorization decorators, with mandatory human-in-the-loop confirmation before any sensitive action executes. Every production MCP server requires team ownership and must clear tickets from Security, Legal/Privacy, and GenAI review teams before approval — governance built into the onboarding process itself, not bolted on after.

## 3. Impact — potential & realized

**Realized:** the post reports monthly-snapshot metrics of roughly 66,000 invocations, 844 active users, and an estimated 7,000 hours of monthly time saved, with Presto (data querying) the highest-traffic server and Spark (job debugging/log summarization) and Knowledge (documentation retrieval) as other heavy-use surfaces. Pinterest explicitly characterizes these numbers as "directional signals of value" and "order-of-magnitude views" derived from owner-provided metadata rather than rigorously measured figures.

**Potential:** the domain-specific-servers-plus-central-registry pattern, paired with the two-layer authorization model, is a reusable blueprint for any organization standing up internal AI-agent tooling that needs governed access to sensitive systems (data warehouses, compute schedulers) rather than open-ended access.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid production engineering on a fast-standardizing protocol, not a new idea

MCP itself is an external standard Pinterest adopted rather than invented, and "multiple domain-specific servers behind a central registry with per-tool authorization" is a sensible but not surprising application of established microservice and API-gateway patterns to the agent-tooling problem. What makes it worth a 3 is the honesty about metric quality (explicitly flagged as directional rather than rigorous) and the concrete security architecture (JWT + SPIFFE two-layer auth, tool-level policy decorators, mandatory human-in-the-loop gates) — a genuinely useful reference for any team building internal agent tooling at similar scale, even without headline-grabbing numbers.

### Similar / related work

- [**Coding Had a Concurrency Problem: How Mux Helped Solve It**](https://www.coinbase.com/blog/coding-had-a-concurrency-problem-how-mux-helped-solve-it) — Coinbase's parallel internal-tooling story for multi-agent coding orchestration, a comparable "internal AI-agent infrastructure grew organically to hundreds of users" narrative from a different company.
- [**Automating Risk Model Retrain Loop with Agentic Skills**](https://www.coinbase.com/blog/automating-risk-model-retrain-loop-with-agentic-skills) — a different flavor of governed, human-gated agent automation (a specific ML retraining loop rather than general-purpose tool access), useful contrast on scope.
- **Model Context Protocol (Anthropic)** — the underlying open standard Pinterest built this ecosystem around, worth reading directly for the base protocol Pinterest's registry and server pattern extend.

### Jargon buster

- **Model Context Protocol (MCP)** — an open standard defining how LLM applications connect to external tools, data sources, and systems through a common interface, rather than each integration being bespoke.
- **SPIFFE** — Secure Production Identity Framework For Everyone, a standard for issuing cryptographic identities to workloads in a service mesh, used here for service-to-service (rather than end-user) authentication.
- **Human-in-the-loop confirmation** — a required manual approval step before an AI agent can execute a sensitive action, rather than the agent acting fully autonomously.
- **Directional metrics** — numbers reported as order-of-magnitude indicators of value/usage rather than rigorously measured, audited figures — an important distinction the source itself flags.
