---
id: razorpay-bumblebee-multiagent-fraud-detection
title: "Bumblebee: The Multi-Agent AI That Changed Fraud Detection at Razorpay"
source: "Razorpay Engineering"
url: "https://engineering.razorpay.com/meet-bumblebee-the-multi-agent-ai-architecture-that-changed-fraud-detection-at-razorpay-c2b6d5704f51"
published: "2026"
added: "2026-09-14"
category: data-engineering
tags: [multi-agent, fraud-detection, merchant-risk, orchestration, llm-agents, caching, razorpay]
novelty: 4
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Bumblebee: The Multi-Agent AI That Changed Fraud Detection at Razorpay

**Source:** [Razorpay Engineering](https://engineering.razorpay.com/meet-bumblebee-the-multi-agent-ai-architecture-that-changed-fraud-detection-at-razorpay-c2b6d5704f51) · Published 2026 · Added 2026-09-14
**Category:** Data Engineering · **Tags:** `multi-agent`, `fraud-detection`, `merchant-risk`, `orchestration`, `llm-agents`

## TL;DR

Razorpay's risk team was manually reviewing 10,000–12,000 merchant websites a month for fraud signals — ~700–800 human-hours, with inconsistent judgment calls between reviewers and a costly third-party screening service that had under 10% precision. Bumblebee replaces that with a three-tier multi-agent system (planner, parallel data-fetcher agents, analyzer) that cuts review latency from 35 seconds to 8–12 seconds per merchant and raises success rate from 88% to 99%+, largely eliminating the manual review load.

## 1. Business context

Before a merchant can process payments through Razorpay, someone has to assess whether their website and business represent fraud risk — a generic privacy policy, a suspicious pricing pattern, a domain registered days ago. Razorpay's risk team was doing this manually: roughly 10,000–12,000 reviews a month, each taking about 4 minutes, totaling 700–800 human-hours of work every month. Beyond the raw cost, manual review at that volume is inconsistent by nature — the article's own example is blunt: "one agent might flag a merchant for having a generic privacy policy while another considers the same policy acceptable." Razorpay had also been paying for a third-party content-screening service to supplement this, but that service delivered under 10% precision on its alerts, meaning the team was spending money to generate mostly-noise signals that still needed human triage. The business needed something that was both faster and more *consistent* than either the manual process or the vendor tool — not just faster.

## 2. Technical details

Bumblebee is structured as a three-tier agent pipeline rather than a single end-to-end model call:

- **Planner Agent.** Receives an incoming merchant case, inspects which tools and data sources are available (checking system health and API quotas along the way), and produces a structured execution plan — assigning priorities, timeouts, and token budgets to each downstream step, and specifying the expected output schema. Some business rules are enforced deterministically at this stage rather than left to the LLM's judgment — for example, skipping GST (tax ID) validation entirely for merchants outside India, where that check doesn't apply.
- **Data Fetcher Agents (parallel).** A set of specialized agents run concurrently, each responsible for one data source: website content review, WHOIS/domain lookups, fraud-database queries, social media metrics, pricing comparisons, and policy verification. Each fetcher performs local data pruning before returning its result — extracting only the relevant sections with a confidence score, rather than handing back a raw 50KB HTML dump for the next stage to wade through. This matters directly for cost and latency: passing dense, pre-filtered JSON instead of raw page content keeps the downstream context small.
- **Analyzer Agent.** Consumes the structured, pre-pruned outputs from all the fetchers and produces the final risk assessment. It runs deterministic rules first — hard thresholds, blacklist checks — and only invokes the LLM for genuinely interpretive work, like generating a human-readable summary of the findings. If a fetcher fails, the Analyzer proceeds with whatever data is available and explicitly flags what's missing, rather than blocking the whole review.

Supporting infrastructure choices: Celery orchestrates the parallel fetcher jobs and triggers the Analyzer once they complete (an event-driven rather than polling design); WHOIS and domain-reputation lookups are cached with appropriate TTLs to avoid redundant external calls; and each agent's LLM temperature is tuned to its role — low for deterministic scoring, medium for planning, higher for narrative/summary generation. Structured logging with trace IDs across the whole pipeline enables case replay and audit trails, which matters for a system making risk decisions that may need to be explained or contested later.

## 3. Impact — potential & realized

**Realized:**
- Per-review latency: **35 seconds → 8–12 seconds**.
- Token usage: **60% reduction** (attributable largely to the fetcher-level pruning before data reaches the Analyzer).
- Review success/accuracy rate: **88% → 99%+**.
- Per-review time overall: **75% reduction**.
- Manual review load: **700–800 hours/month → minimal**.
- Third-party screening alerts (previously ~50/month at under 10% precision): **eliminated**.

**Potential:** The architecture — deterministic gatekeeping at the planning stage, parallel specialized fetchers that pre-compress their own findings, and an analyzer that only spends LLM budget on genuinely interpretive steps — is a directly reusable blueprint for any high-volume, multi-source review workflow (KYC, content moderation, vendor onboarding) where the bottleneck is synthesizing many heterogeneous signals into one judgment call under a tight latency budget.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A well-instrumented production multi-agent system with unusually complete before/after numbers

The planner/parallel-fetchers/analyzer pattern isn't architecturally new — it's a fairly standard orchestrator-plus-specialist-agents design. What earns this a high score is the execution discipline: deterministic rules kept out of the LLM's hands wherever possible, aggressive context pruning at the source rather than downstream, and a genuinely complete set of before/after metrics (latency, tokens, accuracy, hours saved, vendor cost eliminated) rather than a single headline number. That level of instrumentation is rarer than the multi-agent pattern itself, and it's what makes the ROI story credible rather than anecdotal.

### Similar / related work

- [**Building an Agentic SOC on a Stream**](2026-09-12-confluent-agentic-soc-streaming-investigation.md) (in this bank) — a similar multi-agent triage pattern applied to security alert investigation instead of merchant fraud risk.
- [**Monitoring Production Agent Lifecycle with AWS DevOps Agent and AgentCore Evaluations**](2026-09-12-aws-devops-agent-agentcore-evaluations-monitoring.md) (in this bank) — a complementary concern: how to observe and evaluate a multi-agent system like Bumblebee once it's in production, rather than how to build it.
- [**Harnessing the Power of Geo-Experimentation**](2026-09-13-mercadolibre-geo-experimentation-geolift.md) (in this bank) — unrelated domain, but a useful contrast in a different Latin-American/emerging-market fintech-adjacent company solving a measurement problem with similarly pragmatic, metrics-first engineering.

### Jargon buster

- **Orchestrator / planner agent** — The component in a multi-agent system responsible for deciding what work needs to happen and delegating it to specialized sub-agents, rather than one model trying to do everything in a single pass.
- **Context pruning** — Reducing the amount of text/data passed to a downstream LLM call (e.g., extracting relevant snippets instead of a full raw webpage) to cut both cost and the risk of the model getting distracted by irrelevant content.
- **WHOIS lookup** — A query against public domain-registration records (registrant, registration date, etc.), commonly used as a fraud signal since newly-registered or anonymized domains are higher risk.
