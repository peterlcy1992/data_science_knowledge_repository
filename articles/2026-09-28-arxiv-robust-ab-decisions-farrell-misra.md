---
id: arxiv-robust-ab-decisions-farrell-misra
title: "Robust A/B Decisions"
source: "arXiv (Farrell, Korganbekova, Misra)"
url: "https://arxiv.org/abs/2609.07633"
published: "2026-09"
added: "2026-09-28"
category: experimentation-causal
tags: [ab-testing, decision-theory, ambiguity-aversion, hypothesis-testing, deployment-rules, regret-minimization]
novelty: 4
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Robust A/B Decisions

**Source:** [arXiv (Farrell, Korganbekova, Misra)](https://arxiv.org/abs/2609.07633) · Published 2026-09 · Added 2026-09-28
**Category:** Experimentation & Causal Inference · **Tags:** `ab-testing`, `decision-theory`, `ambiguity-aversion`, `hypothesis-testing`, `deployment-rules`, `regret-minimization`

## TL;DR

Max Farrell, Malika Korganbekova, and Sanjog Misra argue that the standard workflow of running an A/B test and deploying the arm with a statistically significant t-test result answers the wrong question — firms actually need a decision rule optimized for real economic payoffs under real uncertainty, not just for whether a difference is detectable. They derive a simple, closed-form "ambiguity-averse" deployment rule that requires only standard experimental output plus one interpretable trust parameter, and show on 552 real digital-advertising experiments that it substantially reduces regret compared to conventional hypothesis-testing-based deployment.

## 1. Business context

Every company running A/B tests eventually faces the same procedural gap: the statistical test tells you whether treatment differs from control in the sample you happened to observe, but the actual business decision — which arm to ship to everyone, forever, going forward — is a different question with different stakes. A t-test's null-hypothesis framing wasn't designed to be a deployment policy; it was designed to control the rate of false claims of an effect. Yet in practice, "p < 0.05, ship it" (or its Bayesian "posterior probability of improvement > threshold" cousin) is exactly how a huge share of real deployment decisions get made, even though the resulting rule ignores how large and reliable the estimated payoff actually is and treats all forms of uncertainty about the future the same way — which can mean shipping a fragile winner that looked good in-sample but performs poorly once volatility or distributional drift moves the environment even slightly away from what the experiment measured.

## 2. Technical details

The authors formalize the deployment decision as a robust decision-theory problem rather than a hypothesis test. Each candidate arm is evaluated not just by its point estimate from the experiment, but by an "ambiguity-penalized value" computed over a neighborhood of distributions close to the experimentally observed outcome distribution — i.e., the rule explicitly asks "how good is this arm not just under the exact distribution I estimated, but under distributions that are plausibly close to it?" and penalizes arms whose apparent advantage is fragile to that kind of perturbation. The key technical move is applying the Donsker-Varadhan variational representation to this ambiguity-penalized value, which collapses what could have been an intractable optimization over a whole neighborhood of distributions into a simple closed-form expression. The resulting rule needs nothing beyond what a standard A/B test already produces (arm-level outcome data) plus a single interpretable "trust" parameter that controls how ambiguity-averse the decision-maker wants to be — at one extreme it recovers something close to naive best-arm selection, and at the other it becomes very conservative about deploying anything without a robust, uncertainty-adjusted edge. Critically, this keeps the implementation cost comparable to a standard t-test: no simulation, no complex Bayesian model-fitting, just a closed-form calculation on the same experimental output teams already have.

## 3. Impact — potential & realized

The paper validates the rule against 552 real digital-advertising experiments run on a major US online platform — a real-world dataset rather than only simulations. Deploying arms via the ambiguity-averse rule "substantially reduces regret relative to conventional hypothesis testing," meaning that across this large set of real experiments, following the new rule's deployment recommendations left less money on the table (or avoided more downside) than following the standard "deploy if statistically significant" convention. Because the rule slots into the same data pipeline as an ordinary t-test, the potential impact is direct and immediate for any team currently gating deployment decisions on p-values or Bayesian win-probability thresholds: swapping in this closed-form rule doesn't require new instrumentation, just a different (and, per this validation, better-calibrated-to-the-actual-decision) formula applied to data they already collect.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A genuinely new decision rule, not just another critique of p-value-driven shipping

The critique that "statistical significance is the wrong criterion for a deployment decision" is not new — it's a well-worn complaint in the experimentation community. What earns this a 4 rather than a 3 is that the paper doesn't stop at the critique: it produces a specific, closed-form, drop-in-replacement decision rule grounded in robust decision theory, and — unusually for a theory paper — validates it against 552 *real* experiments from a live ad platform rather than only simulated data. The combination of theoretical grounding (via the Donsker-Varadhan representation), practical simplicity (same inputs as a t-test, one extra parameter), and large-scale real-world validation is what makes this a candidate for actual adoption rather than just an academic argument.

### Similar / related work

- [**Beyond the A/B Test: Experiment Designs for Your Toughest Questions**](2026-09-25-statsig-beyond-ab-test-designs.md) (in this bank) — addresses the adjacent problem of choosing the right experiment *design*, whereas this paper addresses what to do with the *results* of a standard design once you have them.
- [**Why Spotify Is Not Using Bayesian A/B Testing**](2026-09-16-spotify-bayesian-ab-testing-critique.md) (in this bank) — a different, non-decision-theoretic argument about which statistical framework should drive experimentation decisions; useful contrast since this paper sidesteps the frequentist-vs-Bayesian debate entirely by reframing deployment as a robust decision problem.
- **Wald's statistical decision theory / minimax regret** (classical statistics literature) — the intellectual ancestor of the ambiguity-averse framing used here, where a decision rule is evaluated by its worst-case (or ambiguity-penalized) performance rather than only its average-case behavior under a single assumed distribution.

### Jargon buster

- **Ambiguity aversion** — a decision-making stance that penalizes options whose apparent advantage depends heavily on a single, precisely-assumed model of the world, preferring options that stay good across a range of plausible nearby models.
- **Donsker-Varadhan representation** — a variational (optimization-based) formula from large-deviations theory that rewrites certain worst-case-over-distributions quantities as a simple, tractable expression, which is what lets this paper's decision rule stay closed-form instead of requiring a hard numerical search.
- **Regret (in decision theory)** — the gap between the payoff actually achieved by a decision rule and the payoff that would have been achieved by making the best possible choice in hindsight; "reduces regret" means the rule's deployment choices come closer to the best-in-hindsight choice more often.
