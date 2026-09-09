---
id: aws-agentcore-memory-lifecycle-policies
title: "Designing Lifecycle Policies for AgentCore Memory"
source: "AWS Machine Learning Blog"
url: "https://aws.amazon.com/blogs/machine-learning/designing-lifecycle-policies-for-agentcore-memory/"
published: "2026-09"
added: "2026-09-09"
category: ml-infra-serving
tags: [ai-agents, agent-memory, aws-bedrock-agentcore, step-functions, memory-management, gdpr]
novelty: 3
sourced_via: "full-text fetch"
---

# Designing Lifecycle Policies for AgentCore Memory

**Source:** [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/designing-lifecycle-policies-for-agentcore-memory/) · Published 2026-09 · Added 2026-09-09
**Category:** ML Infrastructure & Serving · **Tags:** `ai-agents`, `agent-memory`, `aws-bedrock-agentcore`, `step-functions`, `memory-management`, `gdpr`

## TL;DR

AWS walks through a nightly, AWS Step Functions-orchestrated pipeline for pruning and consolidating long-running agents' memory on Amazon Bedrock AgentCore, combining TTL-based expiration, a weighted relevance-decay scoring formula, and LLM-based (Claude Sonnet 4.5) consolidation of low-scoring memories before deletion — motivated by real production failures where stale memories caused agents to give outdated or already-resolved answers.

## 1. Business context

Long-running AI agents accumulate memory over time — conversation history, learned facts, task procedures — and AgentCore Memory has no built-in auto-delete. Left unmanaged, that accumulation degrades response quality and creates real operational and compliance risk. The post opens with two concrete production failures that motivate the whole design: a support agent incorrectly referenced a billing dispute that had already been resolved months earlier, and another agent repeated deployment guidance from a runbook that had since been superseded. Both failures share a root cause — the agent had no mechanism to recognize that a memory it was holding was stale — which is the specific gap this post's lifecycle-policy design closes.

## 2. Technical details

The solution is three complementary policies, executed nightly via an AWS Step Functions state machine triggered by an EventBridge rule:

- **TTL-based expiration.** Since AgentCore memory has no native auto-delete, the pipeline calls `ListMemoryRecords` with `BEFORE` filters on the `x-amz-agentcore-memory-createdAt` timestamp to find and delete records older than a configured threshold (default 90 days).
- **Relevance-decay scoring.** A weighted three-term formula combines creation recency, last-access recency, and access frequency: `score = W_RECENCY * exp(-decay_rate * days_since_creation) + W_ACCESS * exp(-decay_rate * days_since_last_access) + W_FREQUENCY * min(access_count / MAX_ACCESS_BASELINE, 1.0)`. Access data is derived from CloudTrail by analyzing `GetMemoryRecord` events (a byproduct of an audit log, repurposed as usage telemetry). Memories scoring below a threshold are flagged for consolidation or pruning.
- **LLM-based consolidation.** Before deletion, low-scoring memories are merged using Amazon Bedrock's Claude Sonnet 4.5, which summarizes related episodic memories into a compact semantic entry with an attached confidence score, then the originals are deleted — so information isn't simply lost, it's compressed into a denser, still-useful form.

The design also defines a **memory-type taxonomy** with different implied retention needs: **episodic** memories (timestamped conversation records) get the shortest retention, **semantic** memories (facts decoupled from any specific session) get medium retention, and **procedural** memories (learned workflows and tool-use patterns) get the longest retention. The full nightly pipeline chains: TTL expiration → relevance scoring → conditional consolidation → metrics emission → output writing. Decay rates are configurable per agent archetype in the post's examples — a support bot uses a 7-day `pruneDays`, a sales agent 21 days, and a compliance advisor 180 days — reflecting how differently "stale" should be defined depending on what the agent is for.

## 3. Impact — potential & realized

The post reports design outcomes rather than large-scale production metrics: memory accumulation becomes controlled without manual intervention; retention policy is tunable per agent archetype via the `pruneDays` parameter; quality is protected by a regression test suite (using AgentCore Evaluations) that measures the score delta between an agent's baseline responses and its post-lifecycle-operation responses, catching cases where pruning or consolidation degraded answer quality; compliance needs (e.g., GDPR right-to-erasure requests) are handled via dedicated deletion handlers with a CloudTrail audit trail; and the whole nightly run is reported to cost roughly $0.01–$0.02 per run for a moderate workload — a genuinely small operating cost for what it prevents.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-reasoned reference pattern for a problem every long-running agent will eventually hit

Memory management for long-running agents — deciding what to forget, what to compress, and what to keep — is a problem every team shipping a persistent agent will eventually run into, and this post is a genuinely useful, concrete reference architecture for it: the relevance-decay formula, the CloudTrail-as-usage-telemetry trick, and the regression-test-gated rollout are all directly reusable ideas. It's not higher than 3 because none of the individual techniques (TTL expiration, weighted recency/frequency scoring, LLM-based summarization for compression) are new in isolation — this is competent applied engineering assembling known primitives into a coherent, AgentCore-specific pipeline, not a new memory-management paradigm.

### Similar / related work

- [**How Intuit Built an Agentic Disaster Recovery Assistant with Amazon Bedrock**](2026-09-05-intuit-ewok-agentic-disaster-recovery.md) (in this bank) — another AWS Bedrock-based production agent writeup, useful for comparing how different teams handle agent state and reliability on the same underlying platform.
- [**Databricks — How We Eliminated $1M/Year of Wasted AI Agent Spend in One Hour**](2026-09-02-databricks-agent-cost-tracing-mcp.md) (in this bank) — a different resource-management concern (spend rather than memory) for long-running production agents, from the same general "keep autonomous agents operationally sane" problem space.
- [**How Fast Do Agents Rot? An Empirical Study of Long-Horizon Degradation in LLM Agents for Production Decision-Making**](2026-09-09-how-fast-do-agents-rot-long-horizon-degradation.md) (in this bank) — relevant context: stale or bloated memory is one plausible contributor to long-horizon agent degradation, making this lifecycle-policy pattern a candidate partial mitigation worth testing against that paper's findings.

### Jargon buster

- **AgentCore Memory** — Amazon Bedrock AgentCore's managed store for an agent's persistent memory (conversation history, facts, learned procedures) across sessions.
- **TTL (time-to-live)** — a fixed expiration window after which a stored record is automatically eligible for deletion, regardless of whether it's still being accessed.
- **Episodic / semantic / procedural memory** — a common cognitive-science-derived taxonomy applied to agent memory: episodic is "what happened when" (a specific conversation), semantic is "facts learned," and procedural is "how to do something" (a learned workflow or tool-use pattern).
- **CloudTrail** — an AWS service that logs API calls made against AWS resources; repurposed here as a source of access-frequency data for the relevance-decay formula, since AgentCore Memory itself doesn't natively track access counts.
