---
id: arxiv-benchmark-checks-llm-simulations-zero-reference
title: "What Does Matching a Human Intervention Effect Establish? Benchmark Checks for LLM Simulations"
source: "Waseda / Anglia Ruskin / Cambridge Silicon Age Centre (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.27186"
published: "2026-11"
added: "2026-11-23"
category: experimentation-causal
tags: [llm-simulation, synthetic-respondents, equivalence-testing, tost, validation, zero-reference, preregistration, survey-experiments]
novelty: 4
sourced_via: "full-text fetch"
---

# What Does Matching a Human Intervention Effect Establish? Benchmark Checks for LLM Simulations

**Source:** [Waseda / Anglia Ruskin / Cambridge Silicon Age Centre (arXiv stat.ME)](https://arxiv.org/abs/2611.27186) · Published 2026-11 · Added 2026-11-23
**Category:** Experimentation & Causal Inference · **Tags:** `llm-simulation`, `synthetic-respondents`, `equivalence-testing`, `tost`, `validation`, `zero-reference`, `preregistration`, `survey-experiments`

## TL;DR

LLM simulations of experiments are often validated by showing the simulated effect is "equivalent" to the human effect within a margin. The paper shows that a reference that predicts zero effect, ignoring treatment, passes that test whenever the human estimate's 90% interval sits inside the margin. You can tell this from the human benchmark alone, before running any model. In a 70-experiment reanalysis, 72% of GPT-4's ±0.20 SD equivalence passes were also zero-reference passes. The authors propose reporting the zero-reference threshold beside every equivalence decision.

## 1. Business context

Teams increasingly use LLM "silicon participants" to screen interventions, plan human sample sizes or simulate group behaviour. These simulations are validated against human experiments. A common criterion is equivalence via two one-sided tests (TOST): the 90% interval of (simulated − human) effect lies within ±δ. If the human effect is small and precisely estimated, a simulator that does not respond to treatment at all can pass. Agreement then says nothing about whether the model actually responds to the intervention.

## 2. Technical details

- **Zero-reference threshold.** A fixed zero prediction passes TOST at margin δ exactly when the human estimate's 90% interval lies inside ±δ. This is the minimum supported margin (after Hartman & Hidalgo) applied to a zero prediction, and it is computable from the benchmark's estimate, SE and margin alone.
- **Dominance result.** In an independent comparison where the true human effect is inside the margin, the zero reference passes at least as often as any nonresponsive simulation, averaged over human and simulated samples.
- **Separation.** A simulation *separates* when it passes and the zero reference fails. With planned precision, the paper defines P₀, the probability that a nonresponsive simulation separates, and δ.05, the margin up to which separation is a 5% test of response. It also defines a *precision floor*: the smallest margin an independent comparison can attain.
- **Five-step protocol, with code.** It pairs each validation claim (average effect, treatment-effect gradient, related outcome, planning input) with the response or measurement evidence that claim requires. The same zero reference is the baseline for margin-free scores (significance agreement, MSE skill).
- **Contrast with PPI.** Prediction-powered inference uses unit-level predictions, while this check uses only the benchmark's estimate, SE and margin.

## 3. Impact — potential & realized

**Measured:**
- *Archive reanalysis* (exploratory; 70 survey experiments, 156 contrasts, from Ashokkumar et al.'s released archive). GPT-4's predicted and observed effects correlate at r = .81. At ±0.20 SD, unscaled predictions pass on 58 contrasts versus 61.4 expected from a nonresponsive noise reference. Of the 58 passes, 42 (72%) are zero-reference passes, against about half for an oracle reference. GPT-4 separates on 16 contrasts versus 1.58 expected without response.
- *Study 1* (preregistered audit of two randomized social-norm experiments, Andre et al. and Geiger et al.). The human benchmarks alone show zero-reference passes on all four registered intention targets. Claude Sonnet 5.5 passed three of them, all zero-reference passes, plus the registered belief-gradient control, which the zero reference fails. Its norm-belief change was 0.065 SD against the human 0.351. The zero-reference check was added after unblinding. Registered tests detected no overestimation, and average-effect intervals excluded overestimation above 0.08 SD.
- *Study 2* (hidden-profile group-discussion experiment with an LLM facilitator). The benchmark's SE fixes a 1.33-fact precision floor against a 2.9-fact human effect. A coding audit shows measurement checks must assess error in the arm *contrast*, not pooled agreement.

**Potential:** A cheap pre-registration step for anyone using LLM personas to pre-screen A/B tests or plan samples: compute what a do-nothing simulator would "achieve" before reporting agreement.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A one-line diagnostic that deflates many "LLMs replicate experiments" claims

The math is elementary (TOST plus a zero reference), but that is the point. The argument is clear, and the 72% figure is striking. The paper is careful about what was preregistered and what was added after unblinding, which strengthens rather than weakens it. For product teams experimenting with persona-based simulators, the takeaway is direct: an equivalence pass on a near-null benchmark is not evidence the simulator is responsive.

The writing is dense, and the group-discussion study is less transferable to product contexts.

### Similar / related work

- [**Augmented Hypothesis Testing with Persona-Based LLM Simulations**](2026-09-25-amazon-ppi-persona-llm-ab-testing.md) (in this bank) — uses LLM personas inside A/B testing via PPI; this paper's check is the sanity test such pipelines should report.
- [**Partial pooling beats synthetic respondents as estimators, not as covariates: a preregistered small-sample tournament**](2026-11-13-arxiv-partial-pooling-vs-synthetic-respondents-small-area.md) (in this bank) — another preregistered test of how far synthetic respondents can be trusted.
- [**Prediction-Powered Inference**](https://arxiv.org/abs/2301.09633) — Angelopoulos et al.; the unit-level alternative the authors contrast with.

### Jargon buster

- **TOST (two one-sided tests)** — an equivalence test: declare "same within ±δ" if the 90% CI of the difference lies inside the margin.
- **Zero reference** — a fake simulator that always predicts no effect; the paper's null benchmark for validation.
- **Separation** — the simulation passes where the zero reference fails, which is the only kind of pass that shows response to treatment.
- **Precision floor** — the tightest margin the human benchmark's own noise allows any comparison to reach.
