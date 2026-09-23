---
id: doordash-feature-flag-cleanup-multi-agent-llm
title: "Automating Feature-Flag Cleanup at Scale with a Multi-Agent LLM System"
source: "DoorDash Engineering Blog"
url: "https://careersatdoordash.com/blog/automating-feature-flag-cleanup-at-scale-with-a-multi-agent-llm-system/"
published: "2026-09"
added: "2026-09-23"
category: llm-genai
tags: [agents, dev-tooling, feature-flags, multi-agent, mcp, code-generation]
novelty: 3
sourced_via: "web search"
---

# Automating Feature-Flag Cleanup at Scale with a Multi-Agent LLM System

**Source:** [DoorDash Engineering Blog](https://careersatdoordash.com/blog/automating-feature-flag-cleanup-at-scale-with-a-multi-agent-llm-system/) · Published 2026-09 · Added 2026-09-23
**Category:** LLMs & Generative AI · **Tags:** `agents`, `dev-tooling`, `feature-flags`, `multi-agent`, `mcp`, `code-generation`

## TL;DR

DoorDash built a two-phase multi-agent LLM system that finds stale feature flags, proposes a resolution, and opens an engineer-reviewed pull request to remove the flag's dead code — cutting a 1-2 hour manual chore to about 14 minutes for under $5. Also documented as an ICSME 2026 industry-track paper.

## 1. Business context

DoorDash's experimentation platform carries over 60,000 feature flags spread across roughly 623 repositories, with about 2,300 new flags created every month. Manually retiring a single flag — confirming its rollout state, finding every code reference, and cleanly removing the dead branches — takes an engineer one to two hours, so the backlog of stale flags grows faster than teams can work through it. The bet was that an agentic system could absorb the toil of investigation and first-draft code changes while keeping a human as the approver of record before any code merges.

## 2. Technical details

The system runs in two phases, built on Google's Agent Development Kit:

- **Phase 1 — Orchestrator (Claude Sonnet).** Pulls stale-flag tickets from Jira via the Atlassian CLI, queries DoorDash's experimentation platform over Model Context Protocol (MCP) for the flag's metadata (UUID, rollout percentage, target value), searches the relevant repositories for code references, and produces a structured report proposing a target value and listing every affected file. An engineer reviews this report and confirms the target value before any code changes begin.
- **Phase 2 — Worker agents (Claude Opus).** Once confirmed, cleanup agents run inside isolated Git worktrees so parallel jobs don't collide with each other or with ongoing developer work. Each worker edits the code to bake in the flag's resolved value, removes the now-dead branch, runs tests and coverage, applies linting, and opens a pull request for a human to merge.

The orchestrator/worker split mirrors a pattern seen elsewhere in the bank (Meta's KernelEvolve, DoorDash's own Vera data agent): a cheaper or more deliberative model handles investigation and planning, while a stronger coding model executes the mechanical edit under test-and-lint guardrails.

## 3. Impact — potential & realized

In an evaluation of 50 stale flags, 45 (90%) produced a usable, engineer-approved pull request, averaging 13.8 minutes and $4.79 per cleanup. Results scaled with flag complexity: simple flags hit a 100% single-pass cleanup rate, medium-complexity flags 94%, and complex flags 85%. Against a 1-2 hour manual baseline across a 60,000-flag backlog growing by ~2,300/month, this is the difference between a chore nobody gets to and a queue an existing platform team can plausibly keep drained — provided review capacity for the resulting PRs keeps pace.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid production engineering, not a new idea

The orchestrator-then-parallel-workers-in-isolated-worktrees pattern is now a familiar shape for "agents that touch real code" systems; what's new here is DoorDash's willingness to publish hard numbers (cost, time, success rate by complexity tier) and the ICSME 2026 industry-track validation, which is rarer for this kind of internal tooling write-up. Likely to be copied less for the architecture and more for the evaluation discipline — running a 50-flag graded eval before declaring victory.

### Similar / related work

- [**Inside Vera, DoorDash's Data Agent**](2026-09-18-doordash-vera-data-agent.md) (in this bank) — another DoorDash agent that turns investigation work (here: data questions) into a structured, human-reviewed output.
- [**Delegating Engineering Work to Cloud-Based Agents (Flux)**](2026-08-31-doordash-flux-cloud-agents-engineering.md) (in this bank) — DoorDash's broader push to hand routine engineering tasks to cloud-based coding agents.
- [**KernelEvolve: How Meta's Ranking Engineer Agent Optimizes AI Infrastructure**](2026-09-18-meta-kernelevolve-ranking-engineer-agent-infra.md) (in this bank) — same orchestrator-plus-executor agent shape, applied to kernel optimization instead of dead-code removal.

### Jargon buster

- **Feature flag** — a runtime switch that lets a team turn a code path on or off (or ramp it gradually) without a new deploy; useful for experiments, but each one left un-cleaned becomes permanent conditional-branch debt.
- **Git worktree** — a way to check out multiple working copies of the same repository at once, so parallel automated jobs can each edit code in isolation without stepping on each other.
- **MCP (Model Context Protocol)** — a standard interface that lets an LLM agent call out to external tools and data sources (here, DoorDash's experimentation platform) in a structured way instead of screen-scraping or hand-written API glue per agent.
