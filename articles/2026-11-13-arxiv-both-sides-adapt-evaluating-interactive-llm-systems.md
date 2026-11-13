---
id: arxiv-both-sides-adapt-evaluating-interactive-llm-systems
title: "When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems"
source: "arXiv stat.ME (Hannah Li)"
url: "https://arxiv.org/abs/2611.17239"
published: "2026-11"
added: "2026-11-13"
category: experimentation-causal
tags: [llm-evaluation, offline-vs-online, estimands, endogenous-prompts, ranking-reversal, novelty-effects, variance-inflation, reward-hacking]
novelty: 4
sourced_via: "full-text fetch"
---

# When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems

**Source:** [arXiv stat.ME (Hannah Li)](https://arxiv.org/abs/2611.17239) · Published 2026-11 · Added 2026-11-13
**Category:** experimentation-causal · **Tags:** `llm-evaluation`, `offline-vs-online`, `estimands`, `endogenous-prompts`, `ranking-reversal`, `novelty-effects`, `variance-inflation`, `reward-hacking`

## TL;DR

Users change what they ask an LLM after seeing its answers, so a model partly chooses the prompts it is judged on. The paper shows that an offline benchmark and a live A/B test therefore estimate *different* quantities — a "common-distribution effect" versus an "induced-distribution effect" — which can rank two models in opposite orders. It gives a sufficient condition, checkable from offline and historical data, under which the two rankings must agree, and shows in a stylized linear model that user adaptivity increases estimator variance.

## 1. Business context

Platforms choosing whether to ship a new LLM use two kinds of evidence: offline benchmark evaluation (both models answer the same prompts, including replays of historical user prompts) and live A/B tests (users are randomized to models and outcomes are measured on their subsequent interactions). General-purpose LLMs have a "jagged frontier" of capability across a huge task space, and users are free to move around that space — changing task type, difficulty and prompting strategy after seeing responses. The paper asks (1) whether offline benchmarks and live A/B tests estimate the same quantity, and (2) if not, whether the difference can change which model looks better.

The motivating example: 100 users per model start with a routine email-writing request. An unusable answer ends the session; a usable-but-generic answer leads to another routine request; a usable-and-excellent answer leads the user to try a difficult request. Both models are 90% usable on routine tasks, and the new model M1 is *better* on difficult ones (70% vs 30% usable) and gives far more excellent routine answers (0.8 vs 0.1). In turn 2, M0 therefore gets about 80 routine and 10 difficult requests while M1 gets about 10 routine and 80 difficult. Turn-2 success is 83.3% for M0 vs 72.2% for M1, and the two-turn average is 86.65% vs 81.1%. A benchmark on any fixed prompt mix with some difficult prompts prefers M1; the A/B test prefers M0 — because M1's strength pushed its users toward harder tasks.

## 2. Technical details

**Framework.** A stochastic model of user–model interaction in which each prompt and response can depend on the preceding interaction, so each model induces its own distribution over conversation paths and prompts. Main results assume a Markov, single-turn dependence: the next prompt depends only on the last model response (a "user response kernel"), and the response depends only on the current prompt. Conversations across users are assumed independent (the paper notes peer learning or cross-user model memory would add spillovers).

**Two estimands.**
- *Common-distribution effect* τ^common(π): difference in a metric between models on the same prompt distribution π.
- *Induced-distribution effect* τ^induced: difference when each model is evaluated on the prompt distribution its own users generate (finite-horizon version over turns 1..T, and a long-run limit).

**Proposition 1.** The difference-in-means estimator from an offline benchmark (or any replay of a fixed historical prompt set) converges to τ^common(π_bench); the estimator from a live A/B test — and from user *simulation* — converges to τ^induced. Even with infinite samples, the two can disagree.

**Decomposition and reversal condition.** τ^induced = τ^common(π(M0)) [a *performance effect*: the new model on the status-quo model's prompt mix] + a *composition effect* (the shift in prompt mix from π(M0) to π(M1), weighted by M1's performance on each cell of a partition of the prompt space where performance is constant). Lemma 2: rankings reverse iff the composition effect has the opposite sign to the performance effect and at least its magnitude.

**Sufficient condition for agreement (Proposition 3).** If |τ^common(π(M0))| ≥ TV(π(M1), π(M0)) × (max − min of M1's cell-level performance), the offline comparison on the status-quo prompt mix and the A/B test have the same sign. All three quantities can be estimated or approximated from offline and historical deployment data without deploying M1, giving a **pre-experiment screening rule**: if the inequality plausibly holds, the benchmark ranking is guaranteed to match the A/B ranking; if not, run the live test. The paper cautions that a coarse prompt partition (e.g. lumping routine and difficult writing into "Writing") understates the total-variation distance, so the rule should come with sensitivity analysis over partitions.

**Interpretation hazards.**
- *Reward hacking via the prompt distribution:* a model can improve an aggregate metric not by doing better on any prompt but by steering users toward prompts it handles well.
- *Novelty effects and user discovery:* if users have learned that the old model fails on some prompt type S, they stop sending S, so a new model that improves only on S shows ≈0 effect on the status-quo prompt mix and may show none in a short A/B test unless users rediscover S. Longer horizons, capability announcements or peer information may be needed; changes in what users ask can themselves be implicit feedback.
- *Burn-in:* dropping early turns (the standard novelty-effect fix) removes the turns where prompt mixes still coincide; that helps if the goal is long-run performance but biases a same-prompt comparison. The paper says the platform should fix its estimand before deciding.

**Variance (Section 4, stylized linear model).** With γ_P = sensitivity of the prompt to the previous response and γ_M = sensitivity of the response to the prompt, the within-user process is AR(1) with feedback strength γ_Pγ_M. Proposition 5: user adaptivity increases the variance of the within-user time average; for 0 < γ_Pγ_M < 1 variance still falls as 1/T but with a larger constant, at γ_Pγ_M = 1 it grows linearly in T, and above 1 it grows exponentially (the paper notes bounded metrics would not diverge, and presents the linear model as illustrative, not high-fidelity). Implication: A/B tests on adaptive users need more users for the same power, and a longer test both reveals long-run behaviour and may add variance.

## 3. Impact — potential & realized

**Realized.** This is a theory paper: there is no empirical LLM study; results are propositions plus the worked email example. Its concrete deliverables are the two estimands, the decomposition, the TV-based agreement condition and the screening procedure built on it.

**Potential.** It gives experimentation teams vocabulary for a disagreement many have seen — "the model won the evals but lost the A/B test" — and an explicit check for when offline evaluation can stand in for a live test. The paper's stated takeaway is that evaluating an interactive system requires measuring not just how the model responds to users but how users respond to the model: track changes in prompt mix as an outcome in its own right.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Cleanly names why LLM evals and A/B tests disagree, and turns it into a checkable pre-experiment rule.

The core idea is familiar from recsys feedback loops and performative prediction, but this is the clearest statement I've seen of it for LLM evaluation, and the performance-vs-composition decomposition is immediately usable: it is the same shape as an Oaxaca–Blinder or mix-shift decomposition that analysts already run on funnel metrics. The TV × performance-range bound is crude (it's a worst-case bound, and the partition is doing a lot of work), so expect it to be inconclusive often; its value is in forcing teams to estimate how much a new model will shift the prompt mix before trusting a benchmark. Practical moves I'd take from it: log task-type mix as a first-class A/B metric, report the performance and composition terms separately, and decide burn-in policy from the estimand rather than habit. Caveats: single-turn Markov dependence, no cross-user learning, and no empirical validation yet.

### Similar / related work

- [**When Can You Ship on Evals Alone? Trial-Level Surrogacy for Offline Evaluation of LLM Systems**](2026-11-02-arxiv-trial-level-surrogacy-ship-on-evals-alone.md) — in this bank: attacks the same offline-vs-online question empirically, by validating evals as surrogates across many past trials
- [**From More to Better: Causal Inference and Digital Experimentation in the Age of AI**](2026-11-13-arxiv-cider-causal-inference-digital-experimentation-age-of-ai.md) — in this bank: a practitioner roundtable (Li is a co-author) whose section on evaluating AI products as their uses change makes the same point informally
- [**Knowing When to Intervene: Causal Evaluation of AI Agents**](2026-11-10-arxiv-knowing-when-to-intervene-causal-evaluation-ai-agents.md) — in this bank: another causal framing of agent evaluation
- [**UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents**](2026-10-23-arxiv-userarena-user-simulation-shopping-agents.md) — in this bank: user simulators, which Proposition 1 says target the induced-distribution effect, like A/B tests

### Jargon buster

- **Common-distribution effect** — The difference between two models when both answer the same set of prompts (what a benchmark measures).
- **Induced-distribution effect** — The difference when each model is scored on the prompts its own users end up sending (what an A/B test measures).
- **Composition effect** — The part of an A/B difference caused by the change in prompt mix rather than by better answers to any given prompt.
- **Total variation (TV) distance** — Half the summed absolute difference between two distributions' probabilities; here, how much the prompt mix shifts between models.
- **Novelty effect** — A treatment effect that changes over time as users get used to (or discover) a new experience.
