---
id: stripe-harbor-ai-assisted-prototyping
title: "Harbor: Stripe's AI-Assisted Prototyping Tool"
source: "Stripe Dot Dev Blog"
url: "https://stripe.dev/blog/harbor-stripes-ai-assisted-prototyping-tool"
published: "2026-09"
added: "2026-09-18"
category: llm-genai
tags: [ai-agents, prototyping, mcp, design-tools, developer-productivity, in-browser-compilation]
novelty: 3
sourced_via: "full-text fetch"
---

# Harbor: Stripe's AI-Assisted Prototyping Tool

**Source:** [Stripe Dot Dev Blog](https://stripe.dev/blog/harbor-stripes-ai-assisted-prototyping-tool) · Published 2026-09 · Added 2026-09-18
**Category:** LLMs & Generative AI · **Tags:** `ai-agents`, `prototyping`, `mcp`, `design-tools`, `developer-productivity`, `in-browser-compilation`

## TL;DR

Stripe built Harbor, an internal browser-based tool that lets designers and other non-engineers turn a static design idea into an interactive, shareable prototype using an AI agent — no server-side build step, no code required. Since May 2026 it has been used by over 3,000 employees to create 12,000 prototypes, with adoption spreading well beyond the design org.

## 1. Business context

Evaluating a new product-design concept for stripe.com traditionally required a full engineering prototype before anyone could click through it, talk to it, or share it for feedback — an expensive way to validate an idea that might get thrown away. Stripe wanted designers (and eventually non-technical staff generally) to be able to go from an idea to an interactive, realistic prototype without waiting on engineering resources or learning to code.

## 2. Technical details

Harbor's core trick is that an AI agent writes a multi-file source tree, and the resulting page **compiles and renders in the browser** rather than being built and served from a backend — each viewer's browser compiles its own fresh copy on load, removing server infrastructure from the critical path entirely. The rendering engine behind this, called Drydock, and Harbor's broader toolset are exposed internally over Stripe's Model Context Protocol (MCP) server, so other internal AI tools can create and manipulate prototypes programmatically rather than only through Harbor's own UI.

The agent doesn't just generate code blind — it runs an inspection loop: it can read the rendered page, inspect DOM elements, simulate user interactions (clicks, typing, scrolling), switch between viewport sizes, and take screenshots, then iterate based on what it observes, closer to how a human developer would sanity-check their own work in a browser. To keep human feedback usable across iterations, Harbor also implements a comment-anchoring system: each comment captures a semantic label, a stable identifier, surrounding text evidence, and structural context, so that when the agent rewrites the page, comments can be re-resolved as "attached," "needs review," or "orphaned" instead of silently disappearing or jumping to the wrong element. Stripe seeded the tool with the company's real design system and realistic mock data so prototypes look and feel production-accurate rather than like generic scaffolding.

## 3. Impact — potential & realized

**Realized:** since a May 2026 rollout, over 3,000 Stripe employees (about 25% of staff) have created roughly 12,000 prototypes. At least one early Harbor prototype's animated hero elements shipped to production nearly unchanged. Adoption has spread past the design org — finance teams have used it to build business reviews, risk analysts for dashboards, and account executives for pricing calculators.

**Potential:** because Harbor's rendering and tooling are exposed via MCP, any internal AI system at Stripe can drive prototype creation programmatically, not just through the Harbor UI — pointing toward prototyping-as-a-capability that other internal agents (support tools, sales tools, data tools) can call into rather than a single standalone app.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-engineered production take on agentic prototyping, not a new idea

"An LLM agent that writes and iterates on a UI" is now a familiar pattern (v0, Claude Artifacts, and similar tools all do versions of this). What's genuinely well-executed here is the production-engineering layer that makes it durable inside a large company: browser-only compilation to avoid server sprawl, a self-inspection loop so the agent checks its own visual output before handing it back, and — the most distinctive piece — comment anchoring that survives page rewrites instead of quietly breaking, which is exactly the kind of detail that determines whether a tool like this actually gets adopted at scale versus abandoned after the demo.

### Similar / related work

- [**Coding Had a Concurrency Problem: How Mux Helped Solve It**](2026-09-11-coinbase-mux-multi-agent-coding-tool.md) (in this bank) — another internal developer-productivity tool built around orchestrating coding agents, at Coinbase rather than Stripe.
- [**Building an MCP Ecosystem at Pinterest**](2026-09-10-pinterest-mcp-ecosystem-ai-agents.md) (in this bank) — a parallel example of a company exposing internal tooling to AI agents via MCP as a general integration pattern.

### Jargon buster

- **Model Context Protocol (MCP)** — an open protocol that lets AI agents discover and call external tools and data sources through a standard interface, rather than each integration being bespoke.
- **In-browser compilation** — building and rendering a web page's code directly in the visitor's browser at load time, instead of compiling it once on a server and serving static output.
