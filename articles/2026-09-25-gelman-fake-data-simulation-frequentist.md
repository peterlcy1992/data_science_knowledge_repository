---
id: gelman-fake-data-simulation-frequentist
title: "This Is How We Do Modern Frequentist Statistics: Using Fake-Data Simulation to Understand What Can Happen in a Study"
source: "Statistical Modeling, Causal Inference, and Social Science (Andrew Gelman)"
url: "https://statmodeling.stat.columbia.edu/2026/09/14/this-is-modern-frequentist-statistics-using-fake-data-simulation-to-understand/"
published: "2026-09"
added: "2026-09-25"
category: statistical-modeling
tags: [simulation, frequentist-statistics, power-analysis, study-design, bayesian-workflow]
novelty: 3
sourced_via: "web search"
---

# This Is How We Do Modern Frequentist Statistics: Using Fake-Data Simulation to Understand What Can Happen in a Study

**Source:** [Statistical Modeling, Causal Inference, and Social Science (Andrew Gelman)](https://statmodeling.stat.columbia.edu/2026/09/14/this-is-modern-frequentist-statistics-using-fake-data-simulation-to-understand/) · Published 2026-09 · Added 2026-09-25
**Category:** Statistical Modeling · **Tags:** `simulation`, `frequentist-statistics`, `power-analysis`, `study-design`, `bayesian-workflow`

## TL;DR

Andrew Gelman argues that the best way to understand what a proposed study design can and can't detect isn't a closed-form power formula — it's fake-data simulation: assume plausible parameter values, simulate many hypothetical datasets under the proposed design, and look directly at what estimates, p-values, and confidence intervals come out. He frames this as the real, practical content of "modern frequentist statistics," not a Bayesian add-on.

## 1. Business context

Anyone designing a study or experiment eventually has to answer "will this design actually be able to detect the effect I care about, and what will the results look like if it does (or doesn't)?" The traditional answer is a power analysis using a closed-form formula, which works cleanly for simple designs (a single two-arm comparison with a known variance) but breaks down or becomes opaque for anything more complex — multiple comparisons, hierarchical structure, non-standard outcome distributions, adaptive designs. Analysts then either force-fit the wrong formula, skip power analysis altogether, or intuit an answer without checking it — all of which can lead to underpowered studies that produce noisy, hard-to-interpret results, or overconfident interpretation of results that were never going to be reliable given the design.

## 2. Technical details

Gelman's proposed workflow is direct: pick plausible values for the unknown parameters (the true effect size, the noise level, the sample composition), simulate a large number of hypothetical datasets as if the study had actually been run under those assumed true values and the proposed design, and then apply the exact same estimation procedure and inferential tools (point estimates, standard errors, p-values, confidence intervals) to each simulated dataset that would be applied to the real data. Looking at how those outputs vary across simulated replications — how often a "significant" result appears, how noisy the point estimates are, how often the sign of the estimated effect flips — gives a direct, assumption-transparent answer to "what can this study design actually tell us," without needing a closed-form formula for the specific (possibly complex) design at hand. Gelman frames this as a formalization of the informal "folk theorem of statistical computing" (when something in your analysis pipeline seems broken or confusing, simulate fake data to check what your method actually does), positioning it as standard modern frequentist practice rather than something exclusive to Bayesian analysis — the simulation itself doesn't require a prior distribution, just plausible parameter guesses.

## 3. Impact — potential & realized

This is a methodological/workflow essay rather than a case study with reported production metrics, so the "impact" is about changing analyst practice: teams that adopt fake-data simulation as a default pre-registration step get a design-specific, assumption-explicit understanding of what their study can detect, catching underpowered or misspecified designs before data collection rather than discovering the problem only after running an inconclusive study. The broader potential is that this workflow generalizes cleanly to designs that don't have a tractable closed-form power formula at all (complex hierarchical experiments, sequential designs, multi-metric guardrail setups), which is an increasingly common situation for teams running sophisticated production experimentation.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Not a new method, but a well-argued, practically important workflow reminder from a leading voice in applied statistics

Simulation-based power analysis isn't new — it's standard advice in modern statistics education and Gelman himself has advocated this for years — so this doesn't introduce anything methodologically novel. It earns a solid (not higher) score because it's a genuinely useful, well-articulated nudge toward a practice that's still underused in industry: many teams still reach for a canned power-calculator formula even when their actual design (multiple guardrail metrics, sequential stopping, hierarchical randomization) doesn't match the formula's assumptions, and a fake-data simulation would catch that mismatch immediately.

### Similar / related work

- [**Decoding Causal Incrementality in E-Commerce: Leveraging Bayesian Structural Time Series Model with a Real-World Example**](2026-09-19-walmart-bayesian-structural-time-series.md) (in this bank) — a different application of simulation-adjacent Bayesian workflow to a production causal-inference problem.
- [**Beyond the A/B Test: Experiment Designs for Your Toughest Questions**](2026-09-25-statsig-beyond-ab-test-designs.md) (in this bank) — several of the nonstandard designs cataloged there (switchback, cluster randomization, response surface) are exactly the kind of design where a closed-form power formula is unavailable or misleading, making fake-data simulation the practical way to reason about their power.
- **"The Folk Theorem of Statistical Computing"** (Gelman's earlier writing, referenced in this post) — the informal principle this post formalizes into a concrete workflow for study design specifically.

### Jargon buster

- **Fake-data simulation** — generating many synthetic datasets under assumed-true parameter values and a proposed study design, then running the intended analysis on each simulated dataset to see what results the design would actually produce.
- **Power analysis** — an assessment of how likely a study design is to detect a real effect of a given size, traditionally computed via a closed-form formula but here computed empirically via simulation instead.
- **Folk theorem of statistical computing** — Gelman's informal principle that when a statistical result or computational pipeline seems confusing or wrong, simulating data with known true values and checking whether the method recovers them is the fastest way to find out what's actually happening.
