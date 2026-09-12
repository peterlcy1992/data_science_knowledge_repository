---
id: uber-agent-identity-crisis-trust-platform
title: "Solving the Identity Crisis for AI Agents"
source: "Uber Engineering Blog"
url: "https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/"
published: "2026-05"
added: "2026-09-12"
category: ml-infra-serving
tags: [agent-identity, security, spiffe-spire, mcp, delegation, policy-enforcement, uber]
novelty: 4
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Solving the Identity Crisis for AI Agents

**Source:** [Uber Engineering Blog](https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/) · Published 2026-05 · Added 2026-09-12
**Category:** ML Infrastructure & Serving · **Tags:** `agent-identity`, `security`, `spiffe-spire`, `mcp`, `delegation`, `policy-enforcement`, `uber`

## TL;DR

Uber built a cryptographic identity system for AI agents that preserves the full delegation chain — which human triggered which agent, which then called which other agent — as short-lived tokens exchanged at every hop, so downstream systems can enforce policy on complete provenance instead of just the immediate caller, at a reported sub-40ms p99 token-exchange latency.

## 1. Business context

Traditional identity models draw a hard line between humans and workloads, but AI agents don't fit either bucket cleanly — an agent "acts for or in the place of another," which existing identity systems have no first-class way to express. Uber's concrete failure case: an on-call Investigation Agent modifies a monitoring configuration, but when something goes wrong downstream, nobody can trace that action back to the human engineer who was ultimately responsible, because the chain of "user asked → on-call agent decided → investigation agent acted" isn't preserved anywhere. As agent-to-agent delegation multiplies across systems, that lost provenance breaks both audit trails and any security policy that depends on knowing who is really behind an action.

## 2. Technical details

Uber's architecture layers several components:

- **Agent Registry** — a source-of-truth mapping agents to the underlying workloads that run them.
- **SPIRE integration** — uses SPIFFE/SPIRE, an established open-source standard for cryptographic workload identity, as the trust foundation each agent identity is anchored to.
- **Security Token Service (STS)** — issues short-lived, single-hop JWTs that carry the *full actor chain* rather than just the immediate caller, e.g. an embedded chain like `[user1, oncall-agent, investigation-agent]`.
- **Token minting pattern** — described as "OAuth 2.0 Token Exchange–inspired": at each hop, an agent exchanges its current credential for a new one scoped to the next hop, rather than reusing one long-lived credential across an entire delegation chain — which limits the blast radius of any single compromised token.
- **MCP Gateway** — the policy enforcement point that checks these tokens before allowing a tool invocation, letting policy decisions reference the complete lineage instead of only the last caller.
- **AI Agent Mesh** — the data plane where agents actually communicate, secured by the identity and token layers above.

Uber frames this as the first of three planned layers: (1) Identity & Trust Foundation — what this article describes — followed by (2) Dynamic Access Control and (3) a Unified Enforcement Plane, aimed at letting humans and agents "collaborate at machine speed" without losing security guarantees.

## 3. Impact — potential & realized

**Realized:** p99 latency for STS token exchange stays consistently below 40ms (with typical values under 10ms) at Uber's current production scale, across a reported "thousands" of internal agents already using the system.

**Potential:** the full-actor-chain token design is the reusable idea — any organization running multi-hop agent delegation (agent calls agent calls agent) faces the same lost-provenance problem, and embedding the complete chain in every token rather than just the last hop is a general fix, not one specific to Uber's stack. The three-layer roadmap (identity → dynamic access control → unified enforcement) also sketches where this class of system needs to go next.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A well-timed, genuinely new take on an old primitive for a new problem

OAuth token exchange and cryptographic workload identity (SPIFFE/SPIRE) are both established technology; what's new is applying full-chain delegation tracking specifically to *agent-to-agent* action provenance, a problem that barely existed at this scale before 2026. As agentic systems proliferate inside large companies, "who is really behind this action" is going to become a standard security requirement rather than a nice-to-have, and Uber's embedded-actor-chain JWT is a clean, concrete answer other companies building internal agent platforms will likely converge on or copy. The sub-40ms p99 number is a meaningful existence proof that this doesn't have to come at a serious latency cost.

### Similar / related work

- [**Uber's Agent Platform / Ranking Engineer Agent lineage**](2026-09-10-meta-ranking-engineer-agent-rea-ads.md) (in this bank) — Meta's REA is a different concern (autonomous ranking-model engineering) but shares the broader 2026 theme of production companies building serious governance infrastructure around autonomous agents rather than treating them as toys.
- [**AWS DevOps Agent and AgentCore Evaluations**](2026-09-12-aws-devops-agent-agentcore-evaluations-monitoring.md) (in this bank) — AWS's article notes that a revoked IAM permission causes silent agent failure; Uber's identity/token system is one architectural answer to exactly that class of problem (agents acting with unclear or stale authorization).
- **SPIFFE/SPIRE (open standard)** — the underlying open-source workload-identity project (spiffe.io) Uber builds this system's trust foundation on; well-established outside the agent context, applied here to a new use case.

### Jargon buster

- **SPIFFE/SPIRE** — an open standard (and its reference implementation) for issuing short-lived cryptographic identities to software workloads, so services can prove who they are to each other without shared long-lived secrets.
- **Actor chain / delegation chain** — the ordered record of every human and agent involved in producing an action, e.g. "user asked the on-call agent, which asked the investigation agent, which made the change" — as opposed to only recording the last, most immediate caller.
- **OAuth 2.0 Token Exchange** — a standard OAuth extension that lets one party trade a token it holds for a new, differently-scoped token, which is the pattern Uber adapts so each hop in a delegation chain gets its own narrowly-scoped credential.
- **MCP (Model Context Protocol)** — a standard protocol for connecting AI agents to external tools and data sources; here, the "MCP Gateway" is where policy decisions actually get enforced before a tool call is allowed through.
