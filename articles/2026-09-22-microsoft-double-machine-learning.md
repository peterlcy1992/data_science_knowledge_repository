---
id: microsoft-double-machine-learning
title: "Introduction to Causal Inference Using Double Machine Learning"
source: "Data Science + AI at Microsoft"
url: "https://medium.com/data-science-at-microsoft/introduction-to-causal-inference-using-double-machine-learning-5daa642321f3"
published: "2025-01"
added: "2026-09-22"
category: experimentation-causal
tags: [causal-inference, double-machine-learning, econml, observational-data, treatment-effects]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Introduction to Causal Inference Using Double Machine Learning

**Source:** [Data Science + AI at Microsoft](https://medium.com/data-science-at-microsoft/introduction-to-causal-inference-using-double-machine-learning-5daa642321f3) · Published 2025-01 · Added 2026-09-22
**Category:** Experimentation & Causal Inference · **Tags:** `causal-inference`, `double-machine-learning`, `econml`, `observational-data`, `treatment-effects`

## TL;DR

Microsoft's Data Science + AI team walks through Double Machine Learning (DML) as a way to estimate a causal treatment effect from observational data when a clean A/B test genuinely isn't an option — using flexible ML models to strip out confounding via orthogonalization and cross-fitting, implemented in practice through Microsoft's open-source EconML package.

## 1. Business context

A/B testing is the gold standard for measuring causal impact, but it isn't always available: some interventions can't ethically or practically be randomized (you can't randomly assign some customers to slower delivery just to measure the effect on lifetime value), some questions are about a change that already shipped to everyone, and some decisions need an answer faster than a properly powered experiment can deliver. In those situations, teams are stuck trying to answer causal questions — "what effect did X actually have on Y?" — from purely observational data, where naive correlation-based analysis is unreliable because it can't distinguish a real causal effect from confounding (some third factor driving both the "treatment" and the outcome). Double Machine Learning is offered as a principled middle path: a way to get defensible causal effect estimates from observational data without needing a randomized experiment.

## 2. Technical details

DML addresses a specific failure mode of naively plugging flexible ML models into a causal estimation problem: when you use a high-capacity model to predict an outcome from a treatment plus confounders, and another to predict the treatment from confounders, the *regularization bias* introduced by the ML models themselves (to control overfitting) can leak into and distort the final causal effect estimate, and using the same data to fit and evaluate the models can compound that into *overfitting bias*. DML corrects both:

1. **Orthogonalization (double robustness).** Rather than directly regressing the outcome on treatment and confounders, DML first uses ML models to predict the outcome from confounders alone, and separately predicts the treatment from confounders alone. The *residuals* from both predictions — the parts of outcome and treatment that confounders don't explain — are what's actually used to estimate the causal effect. This "partials out" the confounders' influence in a way that's more robust to the nuisance models' own regularization bias than a naive approach.
2. **Cross-fitting.** To avoid overfitting bias from using the same data to both fit the nuisance models (the outcome and treatment predictors) and estimate the final effect, DML splits the data into folds, fits nuisance models on one fold, and estimates the effect on a held-out fold, rotating across folds — analogous to cross-validation but applied to keep the causal estimation step statistically well-behaved.

The two "nuisance" models (predicting outcome from confounders, and predicting treatment from confounders) can be any flexible ML model — gradient boosting, random forests, neural networks — which is the appeal: DML lets you bring modern, high-capacity ML methods to bear on confounder-adjustment without those methods' own biases contaminating the final causal estimate, as long as the orthogonalization and cross-fitting steps are applied correctly. In practice, Microsoft implements this through **EconML**, its open-source Python library for estimating heterogeneous treatment effects (i.e., how the effect varies across different segments, not just a single average effect) via double machine learning and related methods.

## 3. Impact — potential & realized

**Realized:** the post is explanatory/educational rather than a single deployed case study, aimed at giving Microsoft's data science practitioners (and readers generally) a correct mental model and practical entry point — via EconML — for applying DML rather than reporting a specific production result.

**Potential:** DML generalizes to any setting where a team needs a causal (not merely correlational) answer but can't run a clean randomized experiment — pricing changes already rolled out to everyone, policy changes that can't ethically be withheld from a control group, or retrospective analysis of a launched feature's impact. Because it composes with arbitrary ML models for the nuisance-prediction steps, it also scales to settings with many, complex confounders where simpler adjustment methods (e.g., basic regression or propensity score matching) would struggle.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — a well-established method, valuable mainly as a clear practitioner explainer

Double Machine Learning itself is not new — it's a well-established technique in the causal inference literature (formalized by Chernozhukov et al.), and EconML has existed as Microsoft's implementation of it for some time. This piece's value is pedagogical: making the orthogonalization/cross-fitting mechanics concrete and approachable for practitioners who need to reach for DML when a clean experiment isn't available, rather than introducing new causal-inference theory. It's a useful addition to the bank as a reference explainer alongside the growing set of applied causal-inference case studies already indexed, even though it doesn't score high on novelty.

### Similar / related work

- [**Harnessing the Power of Geo-Experimentation: How Mercado Libre Measures the Effectiveness of Its Third-Party Media Strategies Using GeoLift**](2026-09-13-mercadolibre-geo-experimentation-geolift.md) (in this bank) — another causal-inference method for settings where individual-level randomization isn't possible, using geographic rather than model-based confounder adjustment.
- [**Decoding Causal Incrementality in E-Commerce: Leveraging Bayesian Structural Time Series Model with a Real-World Example**](2026-09-19-walmart-bayesian-structural-time-series.md) (in this bank) — a different causal-estimation tool (Bayesian structural time series) aimed at the same broader problem class of measuring impact without a clean randomized test.
- [**Ladder of Evidence in Understanding Effectiveness of New Products**](2026-09-01-meta-ladder-of-evidence.md) (in this bank) — a complementary framework for reasoning about which level of causal rigor (from correlational signals up to randomized experiments) is appropriate for a given business question, which is the broader decision DML is one specific answer to.

### Jargon buster

- **Confounder** — a variable that influences both the "treatment" (the thing whose effect you're trying to measure) and the outcome, creating a spurious correlation between them that isn't causal; the central obstacle any causal inference method has to control for.
- **Orthogonalization (in DML)** — the technique of "partialing out" the predictable-from-confounders parts of both treatment and outcome (via residuals) before estimating the causal effect, making the estimate more robust to bias from the ML models used to adjust for confounders.
- **Cross-fitting** — splitting data into folds and estimating nuisance models on different folds than the one used for the final effect estimate, to prevent the same overfitting-driven bias that plagues naively reusing the same data for both model fitting and evaluation.
- **EconML** — Microsoft's open-source Python library implementing Double Machine Learning and related methods for estimating treatment effects, including how those effects vary across different subgroups (heterogeneous treatment effects), from observational data.
