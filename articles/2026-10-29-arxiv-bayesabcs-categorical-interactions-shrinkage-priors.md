---
id: arxiv-bayesabcs-categorical-interactions-shrinkage-priors
title: "Priors and parameterizations for Bayesian regression with categorical variables and interactions (BayesABCs)"
source: "arXiv stat.ME (Inkoo Lee et al.)"
url: "https://arxiv.org/abs/2610.36017"
published: "2026-10"
added: "2026-10-29"
category: statistical-modeling
tags: [bayesian-regression, categorical-interactions, shrinkage-priors, heterogeneous-effects, identifiability, ANOVA]
novelty: 3
sourced_via: "full-text fetch"
---

# Priors and parameterizations for Bayesian regression with categorical variables and interactions (BayesABCs)

**Source:** [arXiv stat.ME (Inkoo Lee et al.)](https://arxiv.org/abs/2610.36017) · Published 2026-10 · Added 2026-10-29
**Category:** Statistical Modeling · **Tags:** `bayesian-regression`, `categorical-interactions`, `shrinkage-priors`, `heterogeneous-effects`, `identifiability`, `ANOVA`

## TL;DR

Regression with categorical variables and their interactions is how analysts estimate group-specific effects, but the default of dummy coding with a dropped reference group plus shrinkage creates biases and asymmetries. BayesABCs pairs abundance-based identifiability constraints with tailored shrinkage priors, and has the property that the joint posterior of the main effects is (nearly) unchanged when interactions are added.

## 1. Business context

Heterogeneous effects by subgroup (device x region, speaker group x system, treatment x segment) are routine DS questions. The paper says interactions are noisy and weakly identified so they need shrinkage, but the standard recipe (dummy coding, a reference group, shrinkage) yields biases, asymmetries and parameters whose meaning changes from model to model.

## 2. Technical details

The 'cat-modified' linear model has an intercept, continuous main effects, categorical main effects, categorical-continuous interactions and categorical-categorical interactions. Identifiability is imposed through abundance-based constraints (ABCs): linear constraints weighted by the joint sample proportions of the categorical variables, so the intercept is the group-averaged mean and main effects are deviations from it, with no reference group. These are coupled with customised shrinkage priors for categorical effects and interactions. The headline result is posterior invariance: with these constraints the joint posterior of all main effects is (nearly) unchanged by adding categorical interactions; it is exact under conditions on the covariates (e.g. for continuous covariates, equal within-group variance of the covariate for the coefficient on x) and approximate otherwise. Constraints are enforced by conditioning, with a model representation that supports efficient posterior computation.

## 3. Impact — potential & realized

Realized: across three simulation studies (one-way ANOVA; multiple dependent categorical and continuous covariates with main-only vs cat-modified models; one in the appendix), the paper reports BayesABCs gives more accurate estimates and predictions, sharper inferences and robustness to extraneous interactions relative to competing parameterizations and priors. Application: error rates of automatic speech recognition systems, using the Koenecke et al. (2020) data, n = 8,817 recordings with the average word error rate across ASR systems from Google, IBM, Amazon, Microsoft and Apple as outcome, standardised speaker age and recording duration, and categorical speaker characteristics; main-effect inference was nearly unchanged by adding interactions. Potential: interpretable subgroup-disparity analyses where one wants to add interactions without disturbing the main-effect story.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A tidy, useful piece of Bayesian regression hygiene rather than a new paradigm. Most valuable where analysts add interactions to probe heterogeneity and then find the main effects have shifted meaning.

Novelty is modest because ABCs date back to classical ANOVA constraints; the contribution is making them work with shrinkage priors and proving when invariance holds. Directly applicable to subgroup disparity audits of models, including ML systems.

### Similar / related work

- [**BayesJudge: Bayesian meta-evaluation**](2026-10-09-arxiv-bayesjudge-bayesian-meta-evaluation.md) — another Bayesian shrinkage approach to comparing groups/systems
- [**Trustworthy method comparison with AI judges**](2026-10-07-arxiv-trustworthy-method-comparison-ai-judges.md) — statistical care when comparing systems across groups

### Jargon buster

- **Reference-group encoding (RGE)** — Dummy coding where one level is dropped and others are measured relative to it.
- **Abundance-based constraints** — Sum-to-zero style constraints weighted by group sizes, making effects deviations from a population-weighted mean.
- **Posterior invariance** — Adding model terms leaves the posterior of other parameters (almost) unchanged.
