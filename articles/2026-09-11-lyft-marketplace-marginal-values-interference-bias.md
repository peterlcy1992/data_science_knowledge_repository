---
id: lyft-interference-bias-mmv
title: "Using Marketplace Marginal Values to Address Interference Bias"
source: "Lyft Engineering Blog"
url: "https://eng.lyft.com/using-marketplace-marginal-values-to-address-interference-bias-a11aff6e670f"
published: "2025-01"
added: "2026-09-11"
category: experimentation-causal
tags: [experimentation, causal-inference, interference-bias, two-sided-marketplace, ab-testing, lyft]
novelty: 4
discovered_via: "Snacks Weekly on Data Science podcast"
sourced_via: "web search"
---

# Using Marketplace Marginal Values to Address Interference Bias

**Source:** [Lyft Engineering Blog](https://eng.lyft.com/using-marketplace-marginal-values-to-address-interference-bias-a11aff6e670f) · Published 2025-01 · Added 2026-09-11
**Category:** Experimentation & Causal Inference · **Tags:** `experimentation`, `causal-inference`, `interference-bias`, `two-sided-marketplace`, `ab-testing`, `lyft`

## TL;DR

Lyft corrects a systematic bias in ride-marketplace A/B tests — where treatment and control riders and drivers compete for the same limited pool of matches, contaminating each other's measured outcomes — by computing "Marketplace Marginal Values" from the dispatch optimization's shadow prices and using them to attribute each ride's value correctly between treatment and control.

## 1. Business context

In a two-sided marketplace like Lyft, a rider in the treatment group and a rider in the control group of the same experiment can end up competing for the same driver. When that happens, a ride "won" by the treatment group is effectively a ride "lost" by control — the two groups aren't independent, they're interfering with each other. This violates the core assumption behind standard A/B testing (that treatment and control outcomes are independent), and in match-based marketplaces (ride-hailing, food delivery) it systematically biases measured treatment effects, typically inflating them, because the experiment can't see that some of the treatment's apparent "wins" would have happened anyway to whichever rider got matched.

## 2. Technical details

Lyft addresses this using **Marketplace Marginal Values (MMVs)**: the shadow prices (dual values) that fall out of solving the marketplace's own matching optimization problem — the same dispatch graph optimization that decides which driver serves which rider is already implicitly computing, as a byproduct, how much marginal value each additional rider or driver contributes to the overall matching outcome. Lyft solves this dispatch optimization on an hourly basis and stores the resulting marginal values for every participant in a lookup table. When analyzing an experiment, instead of naively crediting a completed ride entirely to whichever arm (treatment or control) the rider happened to be in, Lyft splits the ride's contribution between the rider and the driver using their respective marginal values — correcting for the fact that a ride credited to one arm may have displaced a ride that would otherwise have gone to a participant in the other arm.

## 3. Impact — potential & realized

**Realized:** MMV-corrected metrics are now used in Lyft's A/B test analyses specifically to correct for interference-bias overestimation of treatment effects, changing which experiments are judged to have a genuine causal effect versus an artifact of marketplace contention.

**Potential:** the underlying technique — deriving correction values as a byproduct of a marketplace's own optimization/dispatch solver, rather than building a separate bias-correction model — is a reusable pattern for any two-sided, match-based marketplace (delivery, freelance labor, ad auctions) running experiments where treatment and control compete for the same limited supply.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — An elegant reuse of existing optimization output for a hard, well-known problem

Interference bias in marketplace experiments is a well-studied problem in the causal inference literature (switchback designs, cluster randomization, and synthetic control are all common responses), so the problem itself isn't new. What makes Lyft's approach a 4 is the elegance of the solution: rather than building a separate statistical correction model, they extract the correction directly from dual values the dispatch solver was already computing to run the marketplace — a genuinely clever "the answer was already inside the system" result rather than bolting on new machinery.

### Similar / related work

- [**Interference, Bias, and Variance in Two-Sided Marketplace Experimentation: Guidance for Platforms**](https://dl.acm.org/doi/10.1145/3485447.3512063) — the broader academic treatment of the same class of problem this post addresses in production.
- [**Price Experimentation and Interference**](https://arxiv.org/pdf/2310.17165) — a closely related paper specifically on interference bias in pricing experiments, a common special case of the marketplace-interference problem.
- [**Amazon — Price Experimentation**](2026-09-08-amazon-price-experimentation.md) (in this bank) — another company's production account of experimentation under marketplace/pricing dynamics, useful contrast on which correction strategy each company chose.

### Jargon buster

- **Interference bias (SUTVA violation)** — bias that arises when one experimental unit's treatment assignment affects another unit's outcome, violating the standard assumption that units don't interfere with each other — common in marketplaces where supply is shared and limited.
- **Shadow price / dual value** — in optimization, the marginal value of relaxing a constraint by one unit; here, roughly "how much better off the matching outcome would be with one more unit of this rider or driver available."
- **Two-sided marketplace** — a platform connecting two distinct groups of participants (riders and drivers, buyers and sellers) whose supply and demand interact, as opposed to a single-sided system like a content feed.
- **Dispatch graph optimization** — the algorithm that decides, at any given moment, which available driver gets matched to which waiting rider, typically solved as a matching or assignment optimization problem.
