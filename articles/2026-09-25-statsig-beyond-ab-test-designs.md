---
id: statsig-beyond-ab-test-designs
title: "Beyond the A/B Test: Experiment Designs for Your Toughest Questions"
source: "Statsig Blog"
url: "https://www.statsig.com/blog/beyond-the-a-b-test-blog-version"
published: "2026-09"
added: "2026-09-25"
category: experimentation-causal
tags: [ab-testing, experiment-design, switchback, synthetic-control, bandits, sequential-testing]
novelty: 3
sourced_via: "web search"
---

# Beyond the A/B Test: Experiment Designs for Your Toughest Questions

**Source:** [Statsig Blog](https://www.statsig.com/blog/beyond-the-a-b-test-blog-version) · Published 2026-09 · Added 2026-09-25
**Category:** Experimentation & Causal Inference · **Tags:** `ab-testing`, `experiment-design`, `switchback`, `synthetic-control`, `bandits`, `sequential-testing`

## TL;DR

Statsig's Pritul Patel walks through 12 experiment designs beyond the standard A/B/n test — from A/A tests and non-inferiority tests to switchback tests, geo/synthetic control, response surface methodology, and bandits — organized around two failure modes: violating a test's statistical assumptions, and rigorously answering the wrong question (a "Type III error").

## 1. Business context

Most teams default to the standard A/B/n test for every question, but many real business questions don't fit that mold cleanly: a B2B product where users on the same account influence each other, a marketplace change with network effects that contaminate a simple user-level split, a market-level campaign that can't be randomized at the individual level, or a decision that genuinely needs to optimize several variables at once rather than compare two fixed options. Forcing a standard A/B test onto these situations either breaks the test's statistical assumptions (producing an answer that looks confident but isn't valid) or answers a cleanly-defined but wrong question — getting a statistically solid result that doesn't actually inform the decision at hand.

## 2. Technical details

The post catalogs 12 designs and when to reach for each: the standard A/B/n test (default, for acquisition surfaces/product changes with independent users); the A/A test (validates that randomization and the measurement pipeline themselves are working, with no real treatment); the non-inferiority test (proves a change didn't meaningfully worsen an outcome, rather than proving it improved one); cluster randomization (randomizes at the account/group level for B2B products where members of the same account influence each other); holdout tests (measure the accumulated impact of an entire program over a quarter rather than one change); geo tests/synthetic control (evaluate market-level campaigns, like advertising, where individual-level randomization isn't possible); switchback tests (alternate treatment/control by time period on the same units to handle marketplace network effects); elasticity and response surface methodology (find an optimal level, or jointly optimize several continuous variables, rather than just compare two arms); SPRT-style sequential testing (stop as soon as evidence crosses a threshold rather than waiting for a fixed sample size); and multi-armed and contextual bandits (learn the best-performing variant, or personalize which variant a user sees, while minimizing exposure to worse options during learning). The two organizing failure modes are assumption violations — breaking independence, SUTVA (no spillover between treatment and control), or misaligning the unit of randomization with the unit of measurement, which typically requires a statistical fix like the delta method or cluster-robust standard errors — and "Type III errors," where a team answers a precisely-defined question with rigor, but it's the wrong question for the actual decision.

## 3. Impact — potential & realized

The piece grounds both failure modes in concrete, recognizable cases: a lead-gen form test where a five-field form beat a seven-field form on conversion rate, only for the team to discover months later that the shorter form's leads were lower quality — a textbook Type III error, since "conversion rate" wasn't actually the metric that mattered. A separate B2B example shows account admins adopting a feature and other users on the same account following suit automatically, violating the independence assumption a standard A/B test relies on and requiring cluster randomization to fix. The broader value is as a reference/checklist: a team facing an unusual measurement problem can match its situation to one of the 12 designs rather than defaulting to a standard A/B test and discovering the mismatch only after shipping a wrong decision.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Not new individually, but an unusually comprehensive and well-organized practitioner reference

None of these 12 designs is novel on its own — switchback tests, synthetic control, and bandits are all established techniques individually covered elsewhere in this bank and the broader literature. What earns this a solid score is the organizing framework: naming "Type III error" as a distinct failure mode from assumption violations is a genuinely useful mental model, since most experimentation post-mortems in practice are Type III errors (the test was statistically clean, but it answered the wrong question) rather than statistical mistakes. Worth bookmarking as a first-pass checklist before designing a nonstandard experiment.

### Similar / related work

- [**Harnessing the Power of Geo-Experimentation: How Mercado Libre Measures the Effectiveness of Its Third-Party Media Strategies Using GeoLift**](2026-09-13-mercadolibre-geo-experimentation-geolift.md) (in this bank) — a deep, single-company case study of exactly one of the 12 designs cataloged here (geo/synthetic control), useful as a worked example.
- [**Augmented Hypothesis Testing with Persona-Based LLM Simulations**](2026-09-25-amazon-ppi-persona-llm-ab-testing.md) (in this bank) — a different lever on experimentation cost: rather than choosing a different design, this reduces the sample size a standard test needs via prediction-powered inference.
- [**Why Spotify Is Not Using Bayesian A/B Testing**](2026-09-16-spotify-bayesian-ab-testing-critique.md) (in this bank) — a complementary piece on picking the right statistical *framework* (frequentist vs. Bayesian) rather than the right experimental *design*, for the standard A/B/n case this post treats as the default.

### Jargon buster

- **SUTVA (Stable Unit Treatment Value Assumption)** — the assumption that one unit's treatment assignment doesn't affect another unit's outcome (no spillover); switchback and cluster designs exist specifically to handle cases where this assumption is violated.
- **Type III error** — a term for correctly and rigorously answering a research question that turns out not to be the question that actually mattered for the decision at hand.
- **Response surface methodology** — an experimental design approach for finding the optimal combination of several continuous input variables simultaneously, rather than testing them one at a time or comparing fixed discrete arms.
