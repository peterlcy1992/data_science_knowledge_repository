---
id: statsig-multiple-comparisons-more-problems
title: "Multiple comparisons: More comparisons, more problems"
source: "Statsig Blog (Matthew Rogers)"
url: "https://www.statsig.com/blog/more-comparisons-more-problems"
published: "2026-09"
added: "2026-10-01"
category: experimentation-causal
tags: [multiple-comparisons, bonferroni, benjamini-hochberg, false-discovery-rate, ab-testing]
novelty: 2
sourced_via: "web search"
---

# Multiple comparisons: More comparisons, more problems

**Source:** [Statsig Blog (Matthew Rogers)](https://www.statsig.com/blog/more-comparisons-more-problems) · Published 2026-09 · Added 2026-10-01
**Category:** experimentation-causal · **Tags:** `multiple-comparisons`, `bonferroni`, `benjamini-hochberg`, `false-discovery-rate`, `ab-testing`

## TL;DR

Statsig explains why testing many metrics or variants inflates false positives (about 40% cumulative risk for ten independent tests at 5%) and when to apply Bonferroni versus Benjamini-Hochberg corrections, including options that protect primary metrics and guardrails.

## 1. Business context

Experiment dashboards routinely show many metrics and variant comparisons per test. Treating any significant result as real turns noise into launch decisions and erodes trust in the experimentation programme.

## 2. Technical details

Cumulative false-positive probability is 1-(1-α)^n; with α=5% and ten independent comparisons it is roughly 40%. Bonferroni controls the family-wise error rate by dividing α by the number of comparisons (0.05/10 = 0.005) and is the most conservative; Statsig offers a 'Preferential Bonferroni' that gives primary KPIs a larger share of α. Benjamini-Hochberg controls the false discovery rate by ranking p-values and applying a graduated threshold (rank/total × target FDR), catching more real effects; Statsig lets it apply to primary metrics only so guardrail sensitivity is kept. The post recommends choosing the correction before looking at results.

## 3. Impact — potential & realized

This is an explainer, so no experiment outcomes are reported. The practical benefit is fewer spurious launches and a pre-registered rule for how to read many-metric scorecards; the cost is lower power, most severe under Bonferroni.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — Textbook content, but a useful practitioner checklist.

Nothing new statistically; its value is how the correction is wired into a platform (primary vs guardrail metrics). Note the independence assumption behind the 40% figure; correlated metrics inflate less, which the post's formula does not capture.

### Similar / related work

- [**Our Take on AI for Experimentation**](2026-09-29-statsig-our-take-on-ai-for-experimentation.md) — same vendor's view on experimentation practice (in this bank)
- [**Why is it OK to run a z-test on a non-normal distribution for A/B tests?**](2026-09-30-statsig-z-test-non-normal-ab-tests.md) — companion statistical explainer (in this bank)

### Jargon buster

- **Family-wise error rate (FWER)** — Probability of at least one false positive across a family of tests.
- **False discovery rate (FDR)** — Expected share of declared discoveries that are false.
- **Guardrail metric** — A metric you monitor to make sure a change doesn't cause harm, not the one you are trying to move.
