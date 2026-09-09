---
id: nova-verification-aware-agent-harness-recsys
title: "NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems"
source: "arXiv"
url: "https://arxiv.org/abs/2606.27243"
published: "2026-06"
added: "2026-09-09"
category: personalization-recsys
tags: [ai-agents, agentic-harness, recommender-systems, architecture-search, production-audit, ads-ranking]
novelty: 4
sourced_via: "web search"
---

# NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems

**Source:** [arXiv](https://arxiv.org/abs/2606.27243) · Published 2026-06 · Added 2026-09-09
**Category:** Personalization & Recommender Systems · **Tags:** `ai-agents`, `agentic-harness`, `recommender-systems`, `architecture-search`, `production-audit`, `ads-ranking`

## TL;DR

NOVA is a "verification-aware agent harness" that automates architecture evolution for an industrial advertising recommender: it generates candidate architecture modifications, rejects ones that violate recommender-specific semantic constraints (not just code syntax), ranks survivors for offline evaluation, and maintains a trajectory memory of past outcomes to guide future search. A production A/B test on 5% of traffic in a billion-user system delivered GMV gains of +1.25% to +2.02% across pCVR objectives, with pCVR bias reduced by 37–67%.

## 1. Business context

Industrial advertising recommenders continually evolve — new feature interactions, new interaction modules, new model topologies — but every production modification has to satisfy strict interface, resource, and serving constraints on top of improving the underlying metric. Doing this by hand means engineers coordinating changes to model topology, feature configuration, and interaction modules while manually verifying each candidate respects production limits, which caps how many architecture ideas a team can actually test. Existing AutoML tooling doesn't fully solve this either, since it's typically limited to a predefined search space rather than open-ended architectural exploration informed by prior experiment outcomes.

## 2. Technical details

NOVA frames architecture modification as a multi-round search process with several cooperating pieces:

- **Candidate generation:** the harness proposes multiple architecture modifications per round, respecting declared production constraints (interface compatibility, resource budgets, serving limits) rather than searching an unconstrained space.
- **Semantic verification:** candidates are rejected not just for syntax errors but for *semantic* violations specific to recommender systems — e.g., a change that would break a serving invariant or an interaction pattern the system depends on, which a generic code-correctness check wouldn't catch.
- **Ranking and offline evaluation:** valid candidates are ranked and passed to offline evaluation before any candidate is considered for online testing.
- **Trajectory memory:** the system maintains a memory of past search trajectories — what was tried, what happened, and why — which both guides future candidate generation toward more promising regions of the search space and helps identify forbidden patterns to avoid re-proposing failed ideas.

## 3. Impact — potential & realized

**Realized:** NOVA achieves a 53.3% effective pass rate on ScaleUp tasks and 51.7% on Literature-to-Production tasks within a fixed evaluation budget — i.e., roughly half of generated candidates that reach evaluation turn out to be genuinely valid, constraint-respecting proposals worth testing further. In a production A/B test on 5% of traffic within a billion-user advertising system, NOVA-discovered architecture changes produced GMV (gross merchandise value) gains of +1.25% to +2.02% across different pCVR (predicted conversion rate) objectives, alongside a 37–67% relative reduction in pCVR bias.

**Potential:** the semantic-verification layer — rejecting recommender-specific invalid changes before they ever reach costly GPU training or online testing — is the piece most transferable to other industrial recsys teams building similar agentic architecture-search tools, since it directly targets the main source of wasted evaluation budget: technically-valid-but-semantically-broken candidates.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — One of the more rigorous entries in a fast-growing genre

Agent-driven architecture and iteration for production recommenders is now a genre with several entries in this bank (AutoLR, AgentX, and NOVA itself), and NOVA's core idea — search over architecture modifications with constraint-aware filtering — sits within that broader trend rather than inventing a new category. What earns it a 4 is the specificity of the semantic-verification step (explicitly recommender-aware, not just generic code correctness) and a genuine production A/B result on real ad traffic in a billion-user system, with concrete GMV and bias numbers rather than only offline pass rates. It's a notable, well-evidenced entry in this space rather than a field-shifting one.

### Similar / related work

- [**AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems**](2026-09-09-agentx-agent-driven-self-iteration-recsys.md) (in this bank) — a closely related self-iterating agent loop for recommenders (brainstorm → develop → evaluate → harness-evolution), useful to compare against NOVA's search-and-verify framing.
- [**AutoLR: Automating the Path from Research to Launch Review in Industrial Recommender Systems**](2026-09-08-netease-autolr-agentic-recsys-launch-review.md) (in this bank) — NetEase's parallel system, which explicitly cites NOVA as related work; AutoLR's deterministic-controller/LLM-proposal split addresses a similar trust problem to NOVA's semantic verification, from a different architectural angle.
- [**TGR: Advancing Industrial Recommendation from Generative-Paradigm Ranking toward Unified Generation and Reasoning**](2026-09-09-tencent-tgr-unified-generation-reasoning-recsys.md) (in this bank) — a different axis of "industrializing" recsys (model architecture and generation paradigm rather than the iteration process itself), useful contrast on where effort is concentrated across the industry this year.

### Jargon buster

- **pCVR (predicted conversion rate)** — a model's estimate of how likely a shown ad is to lead to a conversion (purchase, signup, etc.); a common ranking objective in ads systems, and the metric NOVA's production test measured bias reduction against.
- **GMV (gross merchandise value)** — the total dollar value of transactions flowing through a platform; a top-line business metric that ads and recommendation changes are often measured against in e-commerce/advertising contexts.
- **Effective pass rate** — the fraction of agent-generated candidates that survive both semantic verification and offline evaluation as genuinely valid, worthwhile proposals, within a fixed evaluation budget.
- **ScaleUp / Literature-to-Production tasks** — the paper's internal benchmark task categories for evaluating NOVA: ScaleUp tasks scale an existing approach up, while Literature-to-Production tasks adapt an idea from published research into a production-constrained implementation.
