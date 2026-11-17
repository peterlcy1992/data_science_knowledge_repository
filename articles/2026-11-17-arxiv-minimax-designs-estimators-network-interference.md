---
id: arxiv-minimax-designs-estimators-network-interference
title: "Minimax designs and estimators for causal inference under network interference"
source: "Karwa (Temple) & Airoldi (arXiv math.ST)"
url: "https://arxiv.org/abs/2611.08560"
published: "2026-11"
added: "2026-11-17"
category: experimentation-causal
tags: [network-interference, minimax, design-based-inference, exposure-mapping, horvitz-thompson, price-of-unbiasedness, experimental-design, sampling-hypergraph]
novelty: 4
sourced_via: "full-text fetch"
discovered_via: "catalog backlog (arXiv math.ST scan)"
---

# Minimax designs and estimators for causal inference under network interference

**Source:** [Karwa (Temple) & Airoldi (arXiv math.ST)](https://arxiv.org/abs/2611.08560) · Published 2026-11 · Added 2026-11-17
**Category:** Experimentation & Causal Inference · **Tags:** `network-interference`, `minimax`, `design-based-inference`, `exposure-mapping`, `horvitz-thompson`, `price-of-unbiasedness`, `experimental-design`, `sampling-hypergraph`

## TL;DR

A design-based minimax theory for linear causal estimands under interference that answers *how low can the risk go* — with the design fixed, with the design chosen from a restricted class, or over all designs — for all estimators and for design-unbiased ones. Interference is recast as constrained sampling from an expanded population of potential outcomes, described by a weighted sampling hypergraph; lower bounds depend on probabilities (all estimators) or odds (unbiased estimators) that sets of potential outcomes are jointly missing.

## 1. Business context

Most interference work evaluates a specific strategy — e.g. a cluster design paired with a Horvitz–Thompson or Hájek estimator — and bounds its risk, sometimes optimizing the design for a fixed estimator. That shows how a strategy performs, not whether risk could be lowered by a different estimator under the same design, a different design within constraints (a treatment budget, an unknown graph), or any design at all. For marketplace and social-network experiments, the three problems map to analysis-stage, constrained design-stage and unconstrained design-stage choices, and comparing them tells you whether a large risk comes from the given design, a design restriction, or a limit of the experiment itself.

## 2. Technical details

- **Expanded population.** With a correctly specified exposure mapping (including the identity), unit *i* has d_i attainable exposure levels; the expanded finite population has Σ d_i potential-outcome cells. An assignment observes one cell per row; the interference graph, exposure mapping and assignment restrictions constrain which cells across rows can be observed together.
- **Sampling hypergraph.** Vertices are potential outcomes; hyperedges are maximal jointly observable sets O(z) for feasible assignments; a randomization design puts weights on hyperedges (the induced sampling design). Fixed-design minimax risk depends on the weighted hypergraph (the whole induced design, not just first-order inclusion probabilities); restricted-design risk on the attainable set of weighted hypergraphs; all-design risk only on the unweighted hypergraph.
- **Lower bounds via indistinguishability.** Two potential-outcome tables that differ only on cells that are all missing give identical data. With a packing of disjoint sets B_b, R_all(P) ≥ Σ c_b² ρ_P(B_b) and R_unb(P) ≥ Σ c_b² ρ_P(B_b)/(1−ρ_P(B_b)), where ρ_P(B_b) is the probability every cell in B_b is missing. All-design bounds use a "sampling rank" of an estimand arm, acting as an effective sample size.
- **Price of unbiasedness.** The ratio of minimax risk over unbiased estimators to that over all estimators.

## 3. Impact — potential & realized

**Results (theory):** examples span the ATE without interference; total, direct and complex-contagion effects under partial and neighbourhood interference; and bipartite dose–response contrasts, with matching upper and lower bounds in several settings. In the graph-unaware class, unbiasedness has no rate cost for the total effect or for direct effects at the extremes, but has a cost for intermediate treated-neighbour counts. For the graph families studied, unbiased and all estimators share the same rate, but a core–periphery family (a clique core with every periphery unit adjacent to it) shows unbiasedness can cost a *rate*. Conflict-graph and ordered-proposal designs attain order (d+1)/n on regular graphs. The paper positions itself against Kandiros, Harshaw & Sävje (2026), who studied the all-design problem under neighbourhood interference with the identity mapping for all estimators.

**Potential:** a benchmark for experiment designers — compute how far a proposed cluster or graph design is from the best achievable risk before running it — and a principled argument for when to give up unbiasedness (e.g. accept a biased estimator) on hub-heavy networks.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A unifying lens, heavy going

Recasting interference as sampling on a hypergraph of potential outcomes is a genuinely general frame that covers no-interference, partial, neighbourhood and bipartite settings in one theory, and the probability-vs-odds distinction gives a clean meaning to "the price of unbiasedness". It is a long, theory-first math.ST paper; practitioners will mostly use its conclusions (design limits, when HT-style unbiasedness is costly on core–periphery graphs) rather than its machinery. This entry is written from the abstract, introduction and selected result sections of a very long full text.

### Similar / related work

- [**Average versus Expected Causal Effects under Interference**](2026-11-10-arxiv-average-vs-expected-causal-effects-under-interference.md) (in this bank) — estimand choices under interference that this theory takes as given.
- [**Choosing Online Experiment Designs under Interference**](2026-10-13-arxiv-experiment-design-under-interference-robust-selector.md) (in this bank) — applied design selection that minimax bounds could benchmark.
- [**Estimating average causal effects under general interference**](https://arxiv.org/abs/1305.6156) (Aronow & Samii) — the exposure-mapping and Horvitz–Thompson framework this builds on.

### Jargon buster

- **Exposure mapping** — a rule summarizing which parts of everyone's treatment affect a unit (e.g. own treatment plus number of treated neighbours).
- **Design-based risk** — expected squared error over the randomization, with potential outcomes held fixed.
- **Minimax** — the smallest achievable worst-case risk over all allowed choices.
- **Price of unbiasedness** — how much worse the best unbiased estimator is than the best estimator of any kind.
