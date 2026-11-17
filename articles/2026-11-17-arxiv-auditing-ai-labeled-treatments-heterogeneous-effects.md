---
id: arxiv-auditing-ai-labeled-treatments-heterogeneous-effects
title: "Who Is the Regression About? Auditing AI-Labeled Treatments When Effects Differ"
source: "Yahoo researcher (arXiv stat.AP / econ.EM)"
url: "https://arxiv.org/abs/2611.21207"
published: "2026-11"
added: "2026-11-17"
category: statistical-modeling
tags: [misclassification, llm-labels, heterogeneous-treatment-effects, att-atu, ols-weights, prediction-powered-inference, two-phase-sampling, audit-design, measurement-error]
novelty: 4
sourced_via: "full-text fetch"
---

# Who Is the Regression About? Auditing AI-Labeled Treatments When Effects Differ

**Source:** [Yahoo researcher (arXiv stat.AP / econ.EM)](https://arxiv.org/abs/2611.21207) · Published 2026-11 · Added 2026-11-17
**Category:** Statistical Modeling · **Tags:** `misclassification`, `llm-labels`, `heterogeneous-treatment-effects`, `att-atu`, `ols-weights`, `prediction-powered-inference`, `two-phase-sampling`, `audit-design`, `measurement-error`

## TL;DR

When an LLM-labelled binary treatment enters an OLS regression and effects differ across units, the coefficient is a weighted mix of the ATT and ATU tilted toward the smaller group — and the label's misses hit that minority hardest. In 35,618 LinkedIn job postings labelled for remote work by a 7B LLM, a precision check passes yet the remote pay gap is understated by nearly 40%, a bias more data cannot remove. A stratified, blind audit of both labelled groups, used in a cell-by-cell prediction-powered correction, recovers both effects.

## 1. Business context

LLMs make it cheap to turn text into variables — remote status from postings, technology mentions from filings — which then enter regressions estimated on the full labelled sample. The usual validation reads a sample of flagged records and reports precision. The paper argues this looks in the wrong place: under effect heterogeneity, OLS (per Słoczyński 2022) weights the ATT and ATU *against* group sizes (13% remote postings → 81% weight on the remote effect), so the regression is about the minority; misclassification (Aigner 1973) attenuates effects, most where the treatment is rare; and because errors are a property of the label, bias does not shrink with n while standard errors do — the naive 95% interval covered the true β in none of 200 resampled samples at full size.

## 2. Technical details

- **Decomposition.** The bias of OLS on a label splits exactly into an *effects channel* (each group's effect replaced by its attenuated version) and a *weights channel* (misses shrink the apparent minority, so OLS leans harder on the damaged effect). Attenuation carries an extra *selective* term when the label's errors correlate with the outcome — plausible for an LLM reading the same text that describes the job.
- **When misses dominate (Proposition 2).** With random errors and a rare treatment, false positives carry the bias (the classical result); once missed units differ from caught ones in the outcome by about half the effect, misses take over, even at one or two misses per false positive.
- **Procedure: audit, correct the cells, choose the estimand.** Cells are bins of the label's propensity score given controls. A blind audit (outcome hidden, two readers, written rule) samples records from every cell and from *both* flagged and unflagged columns. Each cell's labelled moments are replaced by the full-sample label average plus the audit's estimate of the gap to the truth — a prediction-powered difference estimator applied cell by cell, valid even when errors depend on the outcome because it uses audited differences rather than estimated error rates. Report ATT, ATU and β with Słoczyński's weights.
- **Extras.** Estimator properties, a budget rule for audit size, and open-source tools (blind audit sheets, a labelling tool, a protocol for an LLM as one of the two readers). Contrasted with Battaglia et al. (2024) and Christensen et al. (2026), which need only error rates but assume a common coefficient, errors uncorrelated with the regression error, and (for the latter) calibration implying equal false positives and misses.

## 3. Impact — potential & realized

**Measured (LinkedIn postings, 7B LLM labels):**
- Naive β = 0.086 log points vs a corrected 0.14 — nearly 40% too low; ATT and ATU understated by about the same proportion. Corrected: weight on the treated 0.84; remote-posting gap 0.12–0.13 vs 0.20–0.21 for postings that are not remote.
- False-positive rate below 1% in every cell, and 86% of apparent false positives are remote by their own text (the benchmark field is wrong) — a precision check would pass. But the label misses 55% of remote postings, and misses within a cell pay 8 log points more than caught ones (the model catches remote status stated at the top of short postings and misses it stated once in long ones; long postings are better-paid jobs).
- Keeping each cell's number of misses but choosing them at random recovers two-thirds of the bias; removing misses removes it entirely; removing false positives leaves it intact. The zero-shot LLM made ~300 false positives and ~2,600 misses against the employer field, versus ~2,700 and ~2,500 for the DistilBERT classifier used in prior work.
- Audit design matters: uncertainty is dominated by the largest unflagged stratum (one reading can stand for 300 records); a reader with salary visible coded remote status in a way that tracked pay about three times as steeply as blind reading (suggestive, not conclusive); masking pay sentences deleted the treatment cue in 6–12% of postings.

**Potential:** any analytics team that uses LLM labels as regressors (intent, topic, policy-violation flags) gets a concrete validation protocol: audit misses in the big unflagged column, stratify by propensity, correct cells, and state which estimand you report.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — "Precision passed" is not validation

The estimator is borrowed (PPI / two-phase sampling, as the author says plainly); the contribution is the structure — combining Słoczyński's weights with selective misclassification and showing, on real data, that a 99%-precise label yields a 40% bias. It's the most actionable LLM-labelling caveat I've seen for applied regression work: check the unflagged column, and decide whether you want the ATT, ATU or the OLS mix before you correct. Single-dataset evidence, but Proposition 2 tells you when to expect the same.

### Similar / related work

- [**Covariance-Calibrated Prediction-Powered Inference**](2026-10-16-arxiv-covariance-calibrated-prediction-powered-inference.md) (in this bank) — the PPI family whose validation-sample correction is applied here cell by cell.
- [**Who Counts as Exposed? Measurement Choices in an Open, Re-estimable Index of Occupational AI Exposure**](2026-11-16-mit-who-counts-as-exposed-occupational-ai-exposure-index.md) (in this bank) — LLM labels treated as measurements whose validity must be argued.
- [**Prediction-Powered Inference**](https://arxiv.org/abs/2301.09633) (Angelopoulos et al.) — the difference estimator underlying the correction.

### Jargon buster

- **ATT / ATU** — the average effect on units that actually got the treatment vs on those that didn't.
- **Słoczyński weights** — the weights OLS implicitly puts on ATT and ATU; the smaller group's effect gets the larger weight.
- **Selective misclassification** — label errors that are correlated with the outcome (here, missed remote jobs pay more), which classical attenuation formulas ignore.
- **Two-phase sampling** — label everything cheaply, then measure the truth on a designed subsample and use it to correct the full-sample estimate.
