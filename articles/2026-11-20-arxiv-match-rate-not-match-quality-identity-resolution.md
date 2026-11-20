---
id: arxiv-match-rate-not-match-quality-identity-resolution
title: "Match Rate Is Not Match Quality: An Empirical Assessment of Third-Party Identity Resolution Using Random Device Engagement Polling and a National Voter File"
source: "Konitzer (GrowthLoop) & Rothschild (arXiv econ.EM)"
url: "https://arxiv.org/abs/2611.23851"
published: "2026-11"
added: "2026-11-20"
category: product-analytics
tags: [identity-resolution, match-rate, metric-design, measurement-validity, advertising, audience-activation, mixture-model]
novelty: 3
sourced_via: "full-text fetch"
---

# Match Rate Is Not Match Quality: An Empirical Assessment of Third-Party Identity Resolution Using Random Device Engagement Polling and a National Voter File

**Source:** [Konitzer (GrowthLoop) & Rothschild (arXiv econ.EM)](https://arxiv.org/abs/2611.23851) · Published 2026-11 · Added 2026-11-20
**Category:** Product Analytics & Metrics · **Tags:** `identity-resolution`, `match-rate`, `metric-design`, `measurement-validity`, `advertising`, `audience-activation`, `mixture-model`

## TL;DR

Identity-resolution vendors sell on match rate, the share of submitted records linked to ad identifiers. Using 2019–20 data, the authors compare voter-file age and gender with survey self-reports from the linked mobile devices for two leading vendors. Age bracket and gender agree in only 23.6% of pairs one vendor labels 'individual-level' and 21.8% of the other's audited links, against roughly 10% by chance. Under a mixture model, that implies identity-level precision of about 15% and 13%. Match rate alone can't tell you whether you reached the intended people.

## 1. Business context

Advertisers send CRM lists to vendors, who onboard them to ad platforms. The headline KPI is match rate, which vendors are incentivized to maximize even at the cost of quality, through household-level, probabilistic or single-touchpoint links. Advertisers usually can't audit quality, because platforms don't return individual identifiers. A stylized example: a 90% match rate with 15% precision reaches 13,500 intended customers, while 40% with 90% precision reaches 36,000. The relevant quantity is match rate × quality.

## 2. Technical details

- **Data.** The now-defunct survey firm PredictWise linked voter-file records and mobile ad IDs (MAIDs) through two vendors. The paper names Vendor A as LiveRamp (voter file → MAIDs) and Vendor B as Kochava (MAIDs → voter records). PredictWise then surveyed the linked devices in-app for self-reported age and gender. The authors were associated with PredictWise.
- **Link ambiguity.** Vendor A returns an average of 3.4 device IDs per match, and Vendor B 7.9 voter records per match. Vendor B's match rate on a random 6,765 frequently surveyed MAIDs was 17.38%.
- **Agreement.** Vendor A's 119 audited links: gender agrees 61.3%, age bracket 32.8%, both 21.8% (95% interval 15–30%). Vendor B's individual-level pairs: both agree 23.6%. Uniform chance over the 5×2 grid is 10%; the empirical baseline is 9.1–9.4%.
- **Mixture model.** Agreement = π·(1−e) + (1−π)·b, where π is precision, b is wrong-person agreement and e is measurement error. The authors give sensitivity curves over b and e and no interval for Vendor B. Precision hits zero if b = 23.6%, i.e. if wrong-person links (e.g. household members) agree more than chance.

## 3. Impact — potential & realized

**Measured:**
- Implied identity-level precision is about 15% (Vendor B individual-level pairs) and about 13% (Vendor A). At the empirical b = 9.4%, Vendor A is 13.7%.
- The authors stress that these are 2019–20 data and don't establish the performance of today's products, and that demographic disagreement is a diagnostic, not direct verification.

**Potential:** A general metric-design lesson: a volume KPI (match rate, coverage, recall) needs a paired quality KPI (precision) and an independent audit design. A survey-plus-ground-truth triangulation like this is reusable for evaluating any entity-resolution or lookalike pipeline.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sharp metric-validity cautionary tale for anyone buying data or audiences

The contribution is the measurement design and the m × q framing more than any statistical novelty. Product and marketing analysts constantly accept vendor KPIs that measure quantity, not correctness, and this paper is the clean counterexample to cite.

Weaknesses: old data, small audit samples (119 links), authors associated with the data source, and precision estimates that depend heavily on the assumed wrong-person agreement rate (household members can push it above or below chance). Treat the 13–15% as illustrative, as the authors do.

### Similar / related work

- [**Not All Matches Are Equally Valuable: An Online Experiment of Retention-Focused Recommendation in a Job-Matching Platform**](2026-09-04-wantedly-retention-focused-recommendation-job-matching.md) (in this bank) — another case where the volume metric (matches) diverges from the quality outcome you care about.
- **Ansolabehere & Hersh (2012), validation with voter files** — the political-science tradition of using voter files as a validation source, which the paper builds on.

### Jargon buster

- **Identity resolution** — linking records about the same person across systems (CRM emails, device IDs, voter files) so they can be targeted or measured together.
- **Match rate vs match quality** — the share of records a vendor links to *something*, vs the share linked to the *right person*.
- **MAID** — Mobile Advertising ID, a resettable device identifier (IDFA on iOS, AAID on Android).
- **Mixture model for agreement** — observed agreement is a blend of correct links (which almost always agree) and wrong links (which agree by chance); solving for the blend weight estimates precision.
