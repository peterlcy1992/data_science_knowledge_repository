---
id: pinterest-metric-movements-root-cause-analysis
title: "The Quest to Understand Metric Movements"
source: "Pinterest Engineering Blog"
url: "https://medium.com/pinterest-engineering/the-quest-to-understand-metric-movements-8ab12ae97cda"
published: "2025-02"
added: "2026-08-31"
category: data-engineering
tags: [root-cause-analysis, observability, metrics, anomaly-detection, segment-analysis]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# The Quest to Understand Metric Movements

**Source:** [Pinterest Engineering Blog](https://medium.com/pinterest-engineering/the-quest-to-understand-metric-movements-8ab12ae97cda) · Published 2025-02 · Added 2026-08-31
**Category:** Data Engineering · **Tags:** `root-cause-analysis`, `observability`, `metrics`, `anomaly-detection`

## TL;DR

Pinterest built a **root-cause-analysis (RCA) platform** that narrows down why
a key metric moved, using three complementary, pragmatic approaches — segment
drilling, cross-metric similarity search, and experiment-effect attribution —
rather than one unified causal model.

## 1. Business context

"Why did this metric move?" is one of the most common but hardest questions
for a platform Pinterest's size to answer: candidate causes range from
infrastructure issues (OS upgrades, logging errors) to traffic shifts to
recent code or experiment changes, spread across many teams and systems.
Answering it manually, ad hoc, every time a metric moves is slow and
inconsistent, so Pinterest built a dedicated platform to systematize the
investigation.

## 2. Technical details

- **Segment drilling.** The platform slices a metric along a **tree structure
  of dimensions**, letting an investigator (or the tool) choose an order of
  dimensions to drill through, narrowing down which specific segment of
  traffic or users is responsible for the movement. This approach has found
  particular success diagnosing **video metric regressions**.
- **Cross-metric similarity ("general similarity").** The platform scans
  other metrics for ones that moved **similarly** over the same window —
  either in the same direction (positive association) or the opposite
  direction (negative association) — surfacing correlated signals as clues to
  a shared underlying cause.
- **Experiment-effect attribution.** A third approach checks whether the
  metric movement is explained by a live **experiment** rather than an
  organic or infrastructure cause.
- **Feedback loop as a stated gap.** The team notes that RCA suggestions are
  often just that — suggestions a user may not know how to interpret or tune
  — and calls out wanting a feedback mechanism where users label results as
  helpful or not, feeding back into the algorithm.
- **Future direction: causal discovery.** The post flags interest in using
  **causal discovery** to learn actual causal relationships between metrics,
  aiming for richer, less noisy statistical evidence than the current
  general-similarity approach provides.

## 3. Impact — potential & realized

- **Realized:** A production RCA platform combining three named,
  complementary techniques (segment drilling, cross-metric similarity,
  experiment attribution) used across Pinterest's metrics, with a specific
  win cited in diagnosing video metric regressions.
- **Potential:** The team's own stated next step — moving from correlational
  general-similarity matching toward genuine causal discovery between metrics
  — points to a broader opportunity for less noisy, more trustworthy
  automated RCA if that direction pans out.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — practical engineering with an honest account of its own limits

None of the three techniques is individually novel — segment slicing,
correlation scanning, and experiment-effect checks are all standard
observability moves — but combining them into one platform at Pinterest's
scale, and being candid that the current "general similarity" approach is
correlational (not causal) and that a feedback loop is still missing, makes
this a useful, grounded engineering account rather than a breakthrough.

### Similar / related work

- **Autonomous Observability at Pinterest** — a related, more automated
  Pinterest effort following clues across logs, metrics, traces, and change
  events for root-cause analysis.
- **Handling Online-Offline Discrepancy in Pinterest Ads Ranking System** — a
  narrower, model-specific instance of root-cause diagnosis (why offline and
  online metrics disagree) using a similar layered-hypothesis approach.
- General metric-tree / root-cause-analysis tooling used across the industry
  (e.g. segment-based drill-down dashboards) — this platform formalizes a
  similar pattern with an added cross-metric similarity layer.

### Jargon buster

- **Root-cause analysis (RCA)** — the process of identifying the underlying
  reason a metric or system behavior changed, as opposed to just observing
  that it changed.
- **Segment drilling** — narrowing down a metric movement by successively
  slicing the data along dimensions (e.g. platform, country, content type)
  to find which specific slice is responsible.
- **General similarity** — Pinterest's term for finding other metrics whose
  time series moved in a correlated (similar or inverse) pattern, used as a
  clue rather than proof of causation.
- **Causal discovery** — a family of statistical methods that attempt to
  infer cause-and-effect structure between variables from observational data,
  rather than just correlation.
