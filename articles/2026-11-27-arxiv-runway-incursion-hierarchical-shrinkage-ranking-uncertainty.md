---
id: arxiv-runway-incursion-hierarchical-shrinkage-ranking-uncertainty
title: "Airport-level runway-incursion rates normalized by movements: hierarchical shrinkage estimates, ranking uncertainty and severity for FAA-towered airports, FY2008–FY2024"
source: "FlightFinder / himaxym.com, Lisbon (arXiv physics.soc-ph)"
url: "https://arxiv.org/abs/2611.31544"
published: "2026-11"
added: "2026-11-27"
category: statistical-modeling
tags: [negative-binomial, hierarchical-model, empirical-bayes, shrinkage, exposure-offset, ranking-uncertainty, league-tables, ordinal-regression, aviation-safety, regression-to-the-mean]
novelty: 3
sourced_via: "full-text fetch"
---

# Airport-level runway-incursion rates normalized by movements: hierarchical shrinkage estimates, ranking uncertainty and severity for FAA-towered airports, FY2008–FY2024

**Source:** [FlightFinder / himaxym.com, Lisbon (arXiv physics.soc-ph)](https://arxiv.org/abs/2611.31544) · Published 2026-11 · Added 2026-11-27
**Category:** Statistical Modeling · **Tags:** `negative-binomial`, `hierarchical-model`, `empirical-bayes`, `shrinkage`, `exposure-offset`, `ranking-uncertainty`, `league-tables`, `ordinal-regression`, `aviation-safety`, `regression-to-the-mean`

## TL;DR

Kolomiiets builds a panel of 565 FAA-towered airports over FY2008–FY2024 (27,079 runway incursions, 919.7M operations). He fits a hierarchical negative-binomial model with log operations as an offset, which gives each airport a shrunken rate, an exceedance probability and a posterior rank interval. 199 airports exceed the national median with probability ≥ 0.9, but the 90% rank interval at the median airport spans 134 of 565 positions. Two findings stand out. The ranking is fragile to the choice of exposure: itinerant-only operations move 66 flags. And frequency says little about severity: the rank correlation is −0.08 (90% interval −0.14 to −0.02).

## 1. Business context

A runway incursion is the incorrect presence of an aircraft, vehicle or person on a runway's protected area. It is one of ICAO's five high-risk occurrence categories. Few end in collision, but a severe one can mean a high-energy collision between occupied aircraft. The extract analysed here holds 1,679 incursions in FY2024, nine of them in the most severe Categories A and B. (The FAA's official FY2024 figure is 1,758. The author attributes the gap to the vintage and scope of the file.)

The FAA publishes national rates per million operations. No exposure-normalized measure with uncertainty exists for individual airports, though that is where mitigation decisions are made, from taxiway reconfiguration to Runway Status Lights. The FAA's Runway Incursion Mitigation (RIM) programme flags a location with three or more incursions in a calendar year, or an average of one per year over a decade. The author calls such thresholds "the canonical case of selection on noise". Part of the decline later credited to mitigation is regression to the mean. A 2025 DOT Inspector General audit also found the FAA "lacks an integrated approach for analyzing runway incursion data".

Prior academic work treated operations as one covariate among several rather than as the exposure. It mostly used single cross-sections or short panels, and analysed severity and frequency in separate studies with different data windows. Road safety solved the same sparse-rate problem decades ago with empirical-Bayes (EB) shrinkage. The author says none of these tools had been applied to the FAA incursion record.

## 2. Technical details

- **Data.** Three sources are joined:
  - The FAA Runway Safety incursion file, taken from the author's FlightFinder database as an export said to be byte-identical to the FAA file (35,308 records, 27,242 in the window, pulled 2026-07-14).
  - Tower operations from the FAA Terminal Area Forecast (ATADS/OPSNET actuals). Only scenario = 0 rows are used; other rows are forecast variants that would multiply-count exposure.
  - Hub class and the tower flag from the TAF inventory.
- **Panel.** Unit = airport–fiscal year. Inclusion: towered, ≥ 5,000 operations that year. That gives 9,582 airport–years and 99.4% of in-window events. 163 events with no denominator are dropped. 40.8% of airport–years are zero, with mean 2.83 and variance 24.34 (index of dispersion 8.61). Crude national rate: 29.4 per million operations (95% interval 29.1–29.8).
- **Coding artefacts found in the data.**
  - Operational incidents are coded OE before FY2012 and OI after, so the two are pooled.
  - In FY2016–FY2017, 311 and 333 events carry uncoded types (OTH/UNK), against at most 53 in other years. The author says this makes part of that spike (rate peaking at 47.5 in FY2017) "a coding artefact".
- **Frequency model.** NB2: log μᵢₜ = log Eᵢₜ + α + uᵢ + γₜ + xᵢₜᵀβ.
  - uᵢ ~ N(0, σᵤ²) is the airport random effect and γₜ a fiscal-year random intercept.
  - Covariates: GA share of operations, local (pattern) share, and hub class.
  - Weakly informative priors, with α centred on the published national rate.
  - A variant frees the exposure exponent ρ by hub class (following Skaug 2026).
  - The model is also fitted separately for pilot deviations (PD), operational incidents (OI) and vehicle/pedestrian deviations (VPD).
- **EB benchmark.** The Hauer et al. estimator m̂ = wμ̂ + (1−w)y with w = 1/(1+μ̂/φ̂). The safety-performance function is fitted by maximum likelihood (`MASS::glm.nb`).
- **Ranking outputs.**
  - Exceedance probability πᵢ = Pr(λᵢ > median λ | y), with the median recomputed in each draw.
  - The posterior rank, summarized by its mean and a 90% interval, following Goldstein & Spiegelhalter.
  - Flag rule: πᵢ ≥ 0.90.
- **Severity model.** A cumulative-logit (proportional-odds) model on 23,165 categorized events, with airport and year random intercepts. Covariates are event type and the first aircraft's operating rule (part 91/121/129/135, vehicle, pedestrian, unknown), the only two predictors in the export. A binary A/B-vs-C/D logistic model is a check (233 A/B events). RQ3 is the draw-by-draw Spearman correlation between severity effects vᵢ and frequency effects from the two separately fitted models.
- **Estimation.** Stan via brms (R 4.6.1, brms 2.23.0), comparison with PSIS-LOO, and an analysis plan held in the code repository, not a registry. Several fits emitted low bulk-ESS warnings, including the free-exponent model, so the author says those intervals "should therefore be read as approximate".
- **Not done.** Planned geometry covariates (runway crossings, lagged hot-spot counts), surveillance and Runway Status Lights indicators were never obtained, so RQ4 is not estimated. Also unrun:
  - the latent-exposure treatment of non-towered fields;
  - leave-one-airport-out influence;
  - a GA-specific exposure;
  - prior variation on φ;
  - the joint bivariate random-effects model;
  - partial proportional odds.
- **Disclosure.** The sole author operates himaxym.com (FlightFinder), the platform the export comes from. Data and code are on Zenodo, including a script that rechecks the manuscript's numbers.

## 3. Impact — potential & realized

**Measured — frequency (RQ1).**
- Adjusted national mean: 14.30 per million (90% interval 11.38–18.17) for a non-hub at mean traffic mix.
- σᵤ = 1.05 (0.98–1.11), φ = 2.99. One SD above the mean is 2.84× the national rate.
- Coefficient of variation of crude rates: 0.94 raw, 0.89 after shrinkage.
- Rate ratios: GA share 3.58 per unit of share; local share 0.11; small, medium and large hubs vs non-hub about 1.56–1.57.
- Free exposure exponent: 0.80 (large hub), 0.83 (medium), 0.73 (small), 0.68 (non-hub). No interval contains 1. The author's reading: incursions scale sub-linearly with traffic, so a per-million rate "flatters busy airports and penalizes quiet ones".
- Model checks:
  - NB2 beats Poisson by ΔELPD +1509.5 (SE 250.5), which the author calls approximate (9 Pareto k̂ > 0.7).
  - Zero-inflated NB is indistinguishable (ΔELPD −2.0, SE 3.6). Hurdle NB is much worse (−2237.6).
  - The model reproduces zeros (38.6% replicated vs 40.8% observed) but under-predicts the maximum (90 replicated vs 171 observed).

**Measured — ranking (RQ2).**
- 199 airports have π ≥ 0.9, 209 have π ≤ 0.1, and 157 are indistinguishable from the median.
- All top 15 by exceedance are non-hub fields, led by Joplin at 186.0 per million (132.9–252.3). The author warns against reading this as "GA fields are most dangerous". The sub-linear exponent mechanically favours busy airports. And the GA covariate "prices" traffic mix rather than removing it.
- RIM comparison: all 77 RIM airports are in the panel. 59 (76.6%) are flagged by the shrinkage rule. 19 (24.7%) have a rank interval that includes the median rank. 140 of the 199 flagged airports have no RIM location.
- EB vs fully Bayesian: Spearman 0.999. At matched size (199 vs 199) the two sets share 190. The full posterior adds the uncertainty statement, not a different ordering.

**Measured — severity (RQ3).**
- Operational incident vs pilot deviation: odds ratio 8.93 for a more severe category. VPD: 2.36. Part 121 carrier: 1.29.
- In the A/B tail, OI stays dominant (4.77), but part 121 flips to 0.63 and VPD to 0.99.
- Airport severity SD σᵥ = 0.56, about half the frequency SD. In the A/B model it is 0.40 (0.11–0.61).
- Frequency–severity rank correlation: −0.08 (−0.14 to −0.02), Pr(ρ < 0) = 0.99. A 2×2 split is 155 / 170 / 99 / 86, "close to what independence would produce".
- The "operator unknown" odds ratio (0.020) is flagged by the author as a recording artefact. The unknown share moves with reporting era: 16%, then 41–57%, then about 2%.

**Measured — robustness.**
- σᵤ stays within 1.03–1.06 across variants.
- Flag changes: prior ×2 or ×0.5 changes 2 and 1; threshold 1,000 changes 2 and 20,000 changes 13; dropping FY2020–21 changes 17; dropping FY2024 changes 9; coded types only swaps 4 in and 4 out.
- Itinerant-only exposure moves 66 airports, about a third of the flagged set. The author's conclusion: the fragility "is not the count model, the priors or the shrinkage; it is the decision about what counts as exposure". Both flagged sets are published.
- Extending back to FY2002: σᵤ = 1.03, and the FY2008 definitional step is a rate ratio of 2.2 (1.8–2.6).

**Limitations stated.** Towered airports only. Detection and reporting intensity load on the airport effects. Operations are the exposure, while crossings would be the relevant one for crossing incursions. The latest year's severity may be incomplete. Geometry is unestimated. Reproducibility relies on the released export.

**Potential.** Per the author, exceedance probabilities and rank intervals could replace or supplement RIM count thresholds. Before–after evaluations of geometry fixes could use EB or hierarchical expected counts as the baseline, as road safety does. Frequency monitoring should be complemented by risk-based assessment.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Textbook league-table shrinkage, applied carefully and honestly to a new dataset; the exposure and severity findings are the real payload

The methods are off the shelf: an NB2 with an offset, Hauer EB, Goldstein–Spiegelhalter rank intervals, and the author says the ranking method follows them "without modification". What earns the 3 is execution and candour. The paper reports what was not run rather than filling gaps with proxies. It catches its own coding artefacts. It refuses the naive "GA fields are dangerous" headline. And it shows EB and full Bayes give nearly the same ordering, so the full posterior adds only the uncertainty statement. The two substantive results matter beyond aviation. First, the exposure exponent (0.68–0.83) and the itinerant-only variant show the denominator choice moves a third of the flags, while the priors barely move anything. Second, the frequency ranking is close to useless as a severity ranking. Caveats: a single author who also runs the data platform, an analysis plan that is a repository file rather than a registry entry, no geometry covariates, and approximate intervals on the free-exponent fit that carries the sub-linearity claim.

For DS practice (my extrapolation; the paper is about airports only): ranking stores by shrink rate, sellers by defect rate, or segments by conversion is the same problem. Three lessons transfer. Report exceedance probabilities and rank intervals rather than a league table, since a quarter of the table may be indistinguishable from the middle. Test whether events scale linearly with your denominator (orders, sessions, GMV) before dividing; a sub-linear relationship systematically makes small units look worse. And don't let a volume-type metric stand in for a severity-type one: the units with the most incidents per transaction may not be the ones with the costliest incidents. Raw-count alert rules ("≥ 3 complaints this month") will over-flag busy units and credit later improvement to the intervention when it is partly regression to the mean.

### Similar / related work

- [**Shrink Responsibly: Empirical Bayes in Economics**](2026-11-18-arxiv-shrink-responsibly-empirical-bayes-economics.md) (in this bank) — a review of EB for unit-level effects (teachers, schools, hospitals) and for top- or bottom-performer selection. It is the general theory behind this airport league table.
- [**Hierarchical Empirical-Bayes Forecasting of Sparse Counts with Exposure: An Application to Airline Demand and Premium-Cabin Capacity Sharing**](2026-11-16-arxiv-hierarchical-eb-sparse-counts-airline-demand.md) (in this bank) — the same Poisson–Gamma / negative-binomial partial pooling with exposure, used for forecasting thin airline markets rather than ranking sites. Its evaluation is synthetic only.
- [**Beyond empirical Bayes: A hierarchical Bayesian approach to crash rate estimation with missing traffic volume**](https://arxiv.org/abs/2605.27889) — Skaug (2026). The source of the free, class-varying exposure exponent and of the latent-exposure idea this paper specifies but does not run.
- **League tables and their limitations: Statistical issues in comparisons of institutional performance** — Goldstein & Spiegelhalter (JRSS A, 1996). The rank-interval methodology adopted here without modification.

### Jargon buster

- **Exposure offset** — log of the denominator (here operations) entered with a coefficient fixed at 1, so the model estimates a rate per unit of exposure, not a raw count.
- **Exposure exponent (ρ)** — the coefficient on log exposure when it is freed. ρ < 1 means events grow more slowly than traffic, so dividing by traffic flatters busy units.
- **Negative binomial (NB2)** — a count distribution whose variance (μ + μ²/φ) exceeds its mean. It handles the overdispersion that a Poisson cannot.
- **Empirical-Bayes shrinkage** — a site's estimate is a weighted mix of its own count and a model prediction. Low-volume sites lean on the prediction because their counts are mostly noise.
- **Exceedance probability** — the posterior probability that a unit's true rate is above a reference (here the national median). It is used as a flag instead of a raw threshold.
- **Posterior rank interval** — the range of league-table positions a unit plausibly occupies given the uncertainty. Wide intervals mean the point rank is not a finding.
- **Selection on noise / regression to the mean** — flagging units that had an unusually high count in one period. Their counts tend to fall back anyway, which can be mistaken for an effect of the intervention.
- **Proportional-odds (cumulative-logit) model** — an ordinal regression in which each covariate shifts the odds of being in a more severe category by the same factor at every cut point.
