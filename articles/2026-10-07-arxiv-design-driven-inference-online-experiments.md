---
id: arxiv-design-driven-inference-online-experiments
title: "Design-Driven Inference for Online Experiments"
source: "arXiv (Jun Yu, Wenbiao Zhao, Lixing Zhu et al.)"
url: "https://arxiv.org/abs/2610.07831"
published: "2026-10"
added: "2026-10-07"
category: experimentation-causal
tags: [multifactorial-experiments, e-values, anytime-valid, sequential-testing, optimal-design]
novelty: 3
sourced_via: "web search"
---

# Design-Driven Inference for Online Experiments

**Source:** [arXiv (Jun Yu, Wenbiao Zhao, Lixing Zhu et al.)](https://arxiv.org/abs/2610.07831) · Published 2026-10 · Added 2026-10-07
**Category:** experimentation-causal · **Tags:** `multifactorial-experiments`, `e-values`, `anytime-valid`, `sequential-testing`, `optimal-design`

## TL;DR

A framework that treats treatment allocation as evidence collection: block-orthogonal designs with isotropic allocation and batchwise replication give an anytime-valid e-process, so multifactorial online experiments can stop early when effects are negligible while keeping estimation precise.

## 1. Business context

Online experiments increasingly test many factors at once (the abstract cites LLM-prompting tasks as an example). Teams want to stop early when nothing is happening, but standard sequential testing and standard estimation-oriented designs pull in different directions: designs good for testing are not necessarily good for estimating effects.

## 2. Technical details

Per the abstract, the paper has three pieces: (1) block-orthogonal designs that remove bias from nuisance block effects and treatment interactions, described as a complete class for worst-case evidence growth; (2) isotropic allocation paired with an explicit radial e-value, which achieves minimax-rate optimality against unknown directional alternatives; (3) batchwise replication, which yields an anytime-valid e-process. The allocation is claimed to be simultaneously A-, D- and E-optimal for estimation while remaining optimal for testing ("double optimality"). Full paper not read.

## 3. Impact — potential & realized

Realized: validated in simulations and in experiments on LLM prompting tasks, per the abstract; no production numbers reported in the material seen. Potential: one design that supports both early stopping and precise effect estimates, relevant to multi-arm / factorial prompt and feature testing.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A theory-heavy paper that tackles a real tension (optimal-for-testing vs.

A theory-heavy paper that tackles a real tension (optimal-for-testing vs. optimal-for-estimation designs) and uses e-values, which are becoming the standard route to anytime-valid inference. Evidence seen is simulation plus LLM-prompt experiments; adoption by platforms depends on how simple the allocation is to implement.

### Similar / related work

- [**Ensuring Trustworthy Online A/B Testing: Addressing Five Key Questions on CUPED**](2026-10-02-arxiv-cuped-five-questions-bytedance.md) (in this bank) — complementary lever: variance reduction on top of a fixed design
- [**Sequentially-Rerandomized Switchback Experiments**](2026-10-05-arxiv-sequentially-rerandomized-switchback.md) (in this bank) — another design-level approach to improving experiment efficiency
- [**Always Valid Inference: Continuous Monitoring of A/B Tests**](https://arxiv.org/abs/1512.04922) — foundational anytime-valid testing paper (Johari et al.)

### Jargon buster

- **E-value** — A nonnegative statistic whose expected value is at most 1 under the null; large values are evidence against it, and they stay valid under optional stopping.
- **Anytime-valid** — An inference guarantee that holds no matter when you peek or stop the experiment.
- **A-/D-/E-optimality** — Classic design criteria that minimize average, volume-based or worst-direction variance of the effect estimates.
- **Block-orthogonal design** — A design where treatment factors are uncorrelated with block (nuisance) effects, so blocks do not bias effect estimates.
