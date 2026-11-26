---
id: arxiv-monte-carlo-power-analysis-small-system-ab-newsletter
title: "Monte Carlo Power Analysis for Small-System A/B Trials: Detecting Differences in Newsletter Engagement"
source: "Drexel University / University of Minnesota / Gwendydd Research / Clemson University (arXiv cs.HC; RecSys '26)"
url: "https://arxiv.org/abs/2611.28018"
published: "2026-09"
added: "2026-11-26"
category: experimentation-causal
tags: [power-analysis, monte-carlo-simulation, sample-size, zero-inflated-models, bayesian-inference, news-recommendation, email-newsletters, small-samples]
novelty: 2
sourced_via: "full-text fetch"
discovered_via: "arXiv listing (backlog stub)"
---

# Monte Carlo Power Analysis for Small-System A/B Trials: Detecting Differences in Newsletter Engagement

**Source:** [Drexel University / University of Minnesota / Gwendydd Research / Clemson University (arXiv cs.HC; RecSys '26)](https://arxiv.org/abs/2611.28018) · Published 2026-09 · Added 2026-11-26
**Category:** Experimentation & Causal Inference · **Tags:** `power-analysis`, `monte-carlo-simulation`, `sample-size`, `zero-inflated-models`, `bayesian-inference`, `news-recommendation`, `email-newsletters`, `small-samples`

## TL;DR

The team behind POPROX, a research news-recommendation platform, describes how they estimate the power of A/B tests on its daily e-mail newsletter. They fit a zero-inflated Poisson model with a gamma-distributed per-user click rate to historical click logs. They then simulate experiments from it. A CAP odds ratio of 1.5 needs 300–400 users per condition, and 1.3 needs 750–800. The authors' key take-away: a reasonable, controllable model of user behaviour is a necessary precondition for accurate power analysis.

## 1. Business context

POPROX News (Ekstrand, Kluver, Higley, Knijnenburg) is a research platform that runs recommendation experiments on real subscribers. Its user base is small, so experiment capacity is limited. The authors want to prioritise experiments that are likely to produce measurable effects.

- Classical power analysis has closed-form solutions for simple designs, such as two means of a normal outcome. Tools like G*Power implement these.
- Their setting breaks those assumptions. Click outcomes are heavily skewed. There are many observations per user (nested sampling).
- They also want more than a yes/no on one experiment. They want to see how *baseline product improvements* would change experimental power. That needs model parameters and outcomes that map onto the product and subscriber experience.

The product is a daily newsletter, typically 5 sections of 3 articles (earlier versions had a single list of 10). Because of e-mail platform and content-licensing limits, the main feedback signal is which articles a subscriber clicks to read in full.

## 2. Technical details

- **Experiment and metrics.** A between-subjects A/B trial: two groups get newsletters from two recommendation pipelines. Two per-user metrics:
  - **Click-any probability (CAP):** the probability a user clicks at least one article in a newsletter.
  - **Article click-through rate (CTR):** the probability a user clicks any given article.
  - Treatments are compared on mean per-user CAP or CTR with a t-test.
- **Generative model.** The target is n_ℓ, the number of clicks on newsletter ℓ. It is right-skewed with many zeros.
  - ZINB fit better than ZIP when per-user effects were ignored (compared by ELPD-LOO and KL divergence).
  - They use the fact that a negative binomial is a Poisson with a gamma-distributed rate. So they pool Poisson rates by user: λ_u ~ Gamma(μ, σ) is the user's "clickiness". Then n_ℓ ~ Poisson(λ_u) with probability ψ, and n_ℓ = 0 with probability 1 − ψ.
  - Three parameters: μ (mean clickiness), σ² (variance of λ_u) and ψ (zero-inflation). Intuitively, ψ is the chance the user looks at the newsletter at all. λ_u is the expected clicks given that they look.
  - This avoids splitting users into "active" and "inactive" by an explicit, possibly arbitrary, rule.
- **Fitting.** MCMC with vague priors in PyMC 5.28.2 on an NVIDIA RTX 4090 GPU, summarised with ArviZ. 8 chains × 2.5K samples.
  - Posteriors: ψ = 0.55 (89% ETI 0.52–0.58), μ = 0.32 (0.25–0.40), σ² = 0.77 (0.46–1.21). All R̂ = 1.00.
  - The pooled model fits better than un-pooled ZINB: ELPD −4.4×10³ vs −6.3×10³.
  - A rootogram shows observed click counts sit within the posterior predictive bands.
  - A variant with per-user ψ_u mixed poorly (R̂ ≥ 1.02) and gave estimates with unusably high variance.
- **Simulating a treatment.** Run the model twice, with μ_A from the fit and μ_B = k·μ_A, then compute CAP and CTR from the simulated counts.
- **Translating to effect-size units.** μ is an expected click count, not CAP, and ψ also affects both. Standard effect sizes are log-odds of the observed quantity. They used SymPy to derive the μ–CAP relationship and solve for μ_B/μ_A given a target CAP odds ratio. With current parameters, μ_B/μ_A = 1.34 gives a CAP odds ratio of 1.5, the boundary between small and medium effects (Cohen; Chen et al. 2010).
- **Simulator.** 2,000 iterations per condition, fixed exposure (newsletters per user), with power curves for CTR and CAP across experiment sizes. Binary search finds the required users.
- Code is released on Zenodo (doi 10.5281/zenodo.21381743). The observed data is under a data-sharing agreement.

## 3. Impact — potential & realized

**Measured (simulation, not live experiments).**
- A 1.5 CAP odds ratio needs **300–400 users per condition**. A 1.3 odds ratio needs **750–800**.
- Per the power-curve figure, the current platform is not yet large enough to reliably detect a 1.5 effect. It can detect medium CAP changes of 2.0.
- The authors say the model has proved critically useful for first-pass estimates of power and test behaviour for their online recommender experiments.

**Not yet done (authors' stated future work).**
- Validating the power estimates against actual experimental results as more experiments run.
- Extending the model to within-subjects designs.

**Potential.** Any small platform with sparse, zero-heavy engagement data can reuse the recipe. Fit a generative model, pick a manipulable parameter, map it to a standard effect size, and simulate. Because the parameters have product meaning, teams can also ask how a baseline engagement lift (say, a higher ψ) would change the power of future tests.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — A tidy worked example of simulation-based power analysis, not a new method

This is a short note, and the authors frame it that way: an example and starting point for others. Monte Carlo power analysis is decades old (Muthén & Muthén 2002). The gamma-Poisson pooling with zero-inflation is a standard count model. The useful bits are practical. One is the SymPy step that turns a latent rate multiplier into a CAP odds ratio, so the result can be stated in units stakeholders know. Another is honest reporting of what did not work (per-user ψ). The headline numbers are a useful reality check for academic recommender field studies: a few hundred users per arm buys only small-to-medium effects.

Gaps I would flag. The analysis is a t-test on per-user means. A model-based test, or variance reduction using pre-period clickiness, might cut the required sample. The paper does not explore this. The simulation also assumes the treatment scales μ alone. A real recommender change may instead shift ψ (opens) or change the spread of clickiness. Those effects could have quite different power. Until validated against real experiments, the numbers are model-conditional.

### Similar / related work

- [**This Is How We Do Modern Frequentist Statistics: Using Fake-Data Simulation to Understand What Can Happen in a Study**](2026-09-25-gelman-fake-data-simulation-frequentist.md) (in this bank) — Gelman's blog argument for fake-data simulation over closed-form power formulas. This paper is a concrete instance of that workflow.
- [**Unlocking 66% Faster Experiments with Covariate Adjustment: Power Analysis for Clustered Data, Ratio Metrics, and OLS Regression**](2026-10-12-instacart-covariate-adjustment-power-analysis-clustered-data.md) (in this bank) — Instacart's power analysis for clustered data and ratio metrics with covariate adjustment. It is a lever this paper does not use.
- [**Why is it OK to run a z-test on a non-normal distribution for A/B tests?**](2026-09-30-statsig-z-test-non-normal-ab-tests.md) (in this bank) — the CLT argument for mean tests on skewed metrics. That argument weakens at the small samples POPROX faces, which is one reason to simulate.
- **How to Use a Monte Carlo Study to Decide on Sample Size and Determine Power** — Muthén & Muthén (Structural Equation Modeling, 2002). The classic reference for simulation-based power that the paper cites.

### Jargon buster

- **Power analysis** — estimating, before an experiment, how likely it is to detect an effect of a given size if the effect truly exists. 80% is the common target.
- **Monte Carlo power analysis** — simulate many fake experiments from an assumed data model, run the planned test on each, and count how often it is significant.
- **Zero-inflated Poisson (ZIP)** — a count model that mixes an extra "always zero" process with a Poisson. It suits data where most observations are zero.
- **Gamma-Poisson pooling** — give each user their own Poisson rate drawn from a shared gamma distribution. Marginally this gives a negative binomial, but keeps a per-user "clickiness".
- **ELPD-LOO** — expected log predictive density under leave-one-out cross-validation. Higher (less negative) means better out-of-sample fit.
- **R̂ (R-hat)** — an MCMC convergence check comparing chains. Values near 1.00 mean good mixing.
- **Rootogram** — a plot comparing observed and predicted count frequencies on a square-root scale, used to check count-model fit.
- **Odds ratio** — the ratio of the odds of an outcome (here, clicking anything) between treatment and control. 1.5 is about the small/medium boundary.
