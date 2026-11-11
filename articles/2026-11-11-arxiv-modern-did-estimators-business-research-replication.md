---
id: arxiv-modern-did-estimators-business-research-replication
title: "Do Modern Difference-in-Differences Estimators Change Published Findings in Business Research?"
source: "arXiv econ.EM (Davide Proserpio, USC Marshall)"
url: "https://arxiv.org/abs/2611.11003"
published: "2026-11"
added: "2026-11-11"
category: experimentation-causal
tags: [difference-in-differences, staggered-adoption, TWFE, Callaway-SantAnna, imputation-estimator, replication, LLM-agents]
novelty: 4
sourced_via: "full-text fetch"
---

# Do Modern Difference-in-Differences Estimators Change Published Findings in Business Research?

**Source:** [arXiv econ.EM (Davide Proserpio, USC Marshall)](https://arxiv.org/abs/2611.11003) · Published 2026-11 · Added 2026-11-11
**Category:** experimentation-causal · **Tags:** `difference-in-differences`, `staggered-adoption`, `TWFE`, `Callaway-SantAnna`, `imputation-estimator`, `replication`, `LLM-agents`

## TL;DR

Re-estimating 355 staggered-adoption DiD specifications from 40 Management Science and Marketing Science papers with Callaway–Sant'Anna and Borusyak–Jaravel–Spiess estimators, TWFE and modern estimates correlate only 0.61–0.70 and flip sign in 18–25% of comparisons — more often than in economics. Disagreement concentrates in unbalanced panels and designs without never-treated units. LLM agents did the screening and replication under a logged protocol.

## 1. Business context

Staggered rollouts — platform entry, feature launches, policy and regulatory changes arriving in different markets at different times — are exactly what product and marketing analysts evaluate with DiD. The standard two-way fixed effects (TWFE) regression can place negative weights on heterogeneous treatment effects and so produce an estimand outside the range of the underlying effects, even of the wrong sign. Hull (2026) found that in economics this rarely changes conclusions (correlation ~0.9; significant wrong-sign TWFE estimates in only 0.6–2.1% of cases by a hierarchical model). No comparable check existed for marketing or management.

The paper argues business settings could differ: short panels with few cohorts, high-frequency outcomes like sales, reviews or engagement, and plausibly more cohort heterogeneity (early adopters of a feature differ from late ones) — though large never-treated groups cut the other way.

## 2. Technical details

Sample: Management Science (from 2019, its Code and Data Disclosure Policy) and Marketing Science (from 2013); LLM agents (the author discloses Anthropic Claude) screened 1,331 articles from these and JMR, plus 498 from four other INFORMS journals without archives, using full-text term search, OpenAlex citation links to eleven key DiD methods papers, and abstract flags. The agents replicated the published TWFE estimate and re-estimated each specification with the DiD-averaging estimator of Callaway & Sant'Anna (2021) and the imputation estimator of Borusyak et al. (2024), following Hull's protocol, with every judgment call logged in a public repo.

Comparisons use Hull's leverage screen (neither estimate rests on a few clusters): 283 DiD-averaging and 306 imputation comparisons from 28 and 29 papers. Significance of the difference uses analytic SEs plus the bootstrap covariance between estimators; a hierarchical model separates estimand variation from estimation noise.

Extension: time-varying controls, which Hull's protocol excludes, were the most common reason a design failed to qualify, so 12 such papers were also re-estimated with their published controls.

## 3. Impact — potential & realized

Realized: correlations 0.61 (DiD-averaging) and 0.70 (imputation); sign changes in 25.1% and 18.0% of comparisons (19.9% and 16.4% weighting papers equally), versus 14.5% and 10.8% in Hull's economics sample; significant opposite-sign differences in 10.2% and 7.2%. Modern SEs average 1.61× and 1.30× TWFE's (medians 1.36× and 1.11×). The hierarchical model gives estimand correlations of 0.62 and 0.61 and a prior sign-reversal probability of 28.0%; with ~30 papers, leave-one-paper-out estimand correlations range 0.55–0.71 and 0.48–0.92. Disagreement concentrates in unbalanced panels, in designs without never-treated units, and in a few papers; absence of never-treated units is the clearest predictor of reversals for imputation, and no feature predicts reversals for DiD-averaging. With controls, imputation tracks TWFE closely (correlation 0.99, 3.0% reversals over 100 comparisons) while DiD-averaging diverges more (0.80, 28.9%), partly because it conditions on pre-treatment values of the controls.

Also: 18 of 92 papers with an eligible design ship synthetic or disguised data. Potential: a template for LLM-agent-assisted replication audits, and a concrete checklist for which staggered designs warrant heterogeneity-robust estimators.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — An important reality check for anyone who reads or runs staggered-rollout DiD in marketing/product settings, with an unusually transparent LLM-agent replication pipeline.

For industry analysts the takeaway is not 'TWFE is always wrong' but 'know when it matters': unbalanced panels (units churn in and out — common with user or merchant panels), no never-treated group, and outcomes that encode whether a unit is still active. Those are the default conditions of many product rollouts. Run Callaway–Sant'Anna or imputation alongside TWFE and accept the precision cost (SEs ~1.1–1.6× larger). The paper is a preliminary draft, the sample is ~30 papers so single papers move the numbers, and 'disagree' is not the same as 'TWFE was wrong' — the estimands differ.

### Similar / related work

- [**Causal inference in staggered adoption panels: The correct comparison set depends on your intervention**](2026-10-30-arxiv-staggered-adoption-comparison-set-momentary-vs-longitudinal.md) — in this bank: why different staggered estimators target different estimands
- [**Valid Inference After Control Selection in Difference-in-Differences**](2026-10-22-arxiv-valid-inference-did-control-selection.md) — in this bank: the control-variable issue this paper finds blocks many replications
- [**When Covariates Mask Pre-Trends**](2026-11-06-arxiv-when-covariates-mask-pre-trends-honest-did.md) — in this bank: another robustness check on published-style DiD practice

### Jargon buster

- **Staggered adoption** — Units receive treatment at different times rather than all at once.
- **TWFE** — Two-way fixed effects: a regression with unit and time fixed effects and one treatment dummy, the classic DiD implementation.
- **Negative weights** — Under heterogeneous effects, TWFE can implicitly subtract some units' effects, using already-treated units as controls.
- **Never-treated units** — Units that never receive treatment during the panel, a clean comparison group.
