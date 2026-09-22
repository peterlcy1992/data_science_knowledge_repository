---
id: expedia-lodging-ranking-objective-functions
title: "How Expedia Ranks Lodging: Objective Functions, Signals, and a Three-Stage Experimentation Funnel"
source: "Expedia Group Technology"
url: "https://medium.com/expedia-group-tech/interleaving-for-accelerated-testing-75adc644027b"
published: "2026-03"
added: "2026-09-22"
category: search-ranking
tags: [learning-to-rank, personalization, interleaving, ab-testing, candidate-generation, lodging]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# How Expedia Ranks Lodging: Objective Functions, Signals, and a Three-Stage Experimentation Funnel

**Source:** [Expedia Group Technology](https://medium.com/expedia-group-tech/interleaving-for-accelerated-testing-75adc644027b) · Published 2026-03 · Added 2026-09-22
**Category:** Search & Ranking · **Tags:** `learning-to-rank`, `personalization`, `interleaving`, `ab-testing`, `candidate-generation`, `lodging`

## TL;DR

Across a series of Expedia Group Technology posts, the lodging-search team describes their full ranking pipeline end to end: an ML or heuristic candidate-generation stage that narrows the property pool, a personalized ranking model balancing traveler experience against business metrics, and — the newest piece — an interleaving layer inserted between offline backtesting and full A/B tests, which is 10x–100x more statistically sensitive than a standard A/B test and lets the team prune weak ranking ideas cheaply before committing traffic to them.

## 1. Business context

Ranking which lodging properties to show, and in what order, is one of the highest-leverage surfaces in a travel marketplace: it directly shapes both how easily a traveler finds something they'll book and which properties get discovered at all. Getting the objective wrong in either direction is costly — optimize purely for traveler experience (e.g., favoring highly-rated, well-reviewed properties) and business metrics like revenue or supplier diversity can suffer; optimize purely for revenue and traveler trust erodes over time. Layered on top of that is a testing-throughput problem: with a large and continuous stream of candidate ranking improvements to evaluate, running every idea through a full-scale A/B test is slow and statistically expensive, so the team needed a way to filter out weak ideas cheaply before spending real A/B testing budget on them.

## 2. Technical details

**Candidate generation.** Before ranking can run, the pool of properties under consideration has to be narrowed to a manageable size. Expedia's approach supports both an ML-based candidate generator — preferred when historical shopping-log data is available — and a heuristic-based fallback for situations (e.g., new markets or properties) where that history doesn't yet exist, including specific strategies for the cold-start case.

**Personalized ranking model.** The ranking layer (illustrated in earlier work by the Egencia/Expedia team on a "Smart Mix" lodging model) combines search-context signals — destination, check-in/check-out dates, party composition (rooms, adults, children), point of sale, device — with property-side signals — price, review score, star rating, amenities — and personalized user features, trained with models spanning linear methods and factorization machines through to the deep learning architectures used in production today. The explicit objective balances **shopping efficiency** metrics (e.g., the proportion of bookings made within the top-ranked results, and overall search-to-booking conversion rate) against broader business considerations, rather than optimizing a single metric in isolation. In an earlier personalized version of this ranking model, the team reported a **7.4% increase in bookings within the top-1 displayed rank**, a **1.3% increase in search conversion** (p < 10⁻¹⁰), and a **1.3% increase in the proportion of bookings completed within 5 minutes** of search, relative to a prior non-personalized baseline.

**The experimentation funnel.** Sitting on top of the modeling work is a three-stage pipeline for deciding which ranking ideas actually ship: **backtesting** (offline replay against historical logs, typically optimizing NDCG or revenue-oriented proxies) identifies promising variants; those variants then go through **interleaving** tests, where two ranking treatments are blended into a single result list shown to the same user and preference is inferred from which treatment's results get more engagement; only variants that clear the interleaving bar proceed to full **A/B tests** with real traffic. The key property exploited here is that interleaving tests are reported to be **10x to 100x more statistically sensitive** than standard A/B tests at detecting a real difference between two ranking treatments — because both treatments are shown to the same user in the same session, the comparison isn't diluted by between-user variance the way a between-subjects A/B test is. That sensitivity means the team can distinguish "clearly weak" ideas from "worth a full A/B test" ideas using much less traffic and time than jumping straight to A/B testing every candidate.

## 3. Impact — potential & realized

**Realized:** the personalized ranking work reports measurable gains in top-rank bookings, search conversion, and booking speed versus a non-personalized baseline (see numbers above). The interleaving layer is reported to meaningfully increase the team's sensitivity to detect real ranking differences relative to jumping straight to A/B tests, letting them prune weak candidates before spending full A/B testing budget on them.

**Potential:** the three-stage funnel (backtest → interleave → A/B) is a general-purpose pattern for any ranking or recommendation team facing a high volume of candidate improvements relative to available A/B testing capacity — it doesn't require anything Expedia-specific and several other marketplaces (Airbnb, Netflix) have published similar interleaving-based accelerated-testing approaches, suggesting this is becoming a standard tool in the search/ranking experimentation toolkit rather than a one-off.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — solid, well-synthesized production practice rather than a new idea

Personalized learning-to-rank for travel/lodging search, multi-objective ranking balancing user and business metrics, and interleaving as a cheaper-than-A/B-testing pruning step are all well-established techniques independently — Netflix and Airbnb have published closely analogous interleaving work, and personalized ranking for marketplaces is a mature area. The value of this synthesis is in seeing the full pipeline (candidate generation → personalized ranking → backtest/interleave/A-B funnel) laid out end to end as one coherent system, which is useful as a reference architecture even though no individual stage is novel on its own.

### Similar / related work

- [**Learning to Rank for Maps at Airbnb**](2026-08-30-airbnb-learning-to-rank-for-maps.md) (in this bank) — a close analog in both problem shape (personalized ranking for a travel marketplace) and experimentation approach (interleaving-based accelerated testing).
- [**Elevating Travel Experiences with AI**](2026-09-05-expedia-generative-and-traditional-ai.md) (in this bank) — another Expedia AI initiative, but focused on generative trip-planning features layered on top of the core search/ranking stack described here rather than the ranking pipeline itself.
- Netflix's interleaving-based accelerated testing work (published as "Innovating Faster on Personalization Algorithms at Netflix Using Interleaving," Netflix TechBlog) — a close industry parallel applying the same interleaving-for-sensitivity idea to a different recommendation surface; left unlinked as it sits outside this bank's indexed entries, but is directly relevant prior art.

### Jargon buster

- **Interleaving test** — an experimentation technique that blends the results of two ranking treatments into one list shown to the same user, then infers which treatment users prefer from which treatment's items they engage with more — far more statistically sensitive per unit of traffic than a standard between-user A/B test.
- **NDCG (Normalized Discounted Cumulative Gain)** — a standard ranking-quality metric that rewards placing more relevant items higher in a result list, discounting the value of relevant items that appear further down; commonly used as the offline optimization target in backtesting.
- **Cold start (in ranking)** — the problem of ranking or recommending items (or serving users) with little to no historical interaction data to learn from, typically handled with heuristic rules or content-based signals until enough behavioral data accumulates.
- **Backtesting (in ranking)** — evaluating a candidate ranking model or policy offline by replaying it against historical logged data, rather than exposing live users to it, used as a cheap first filter before more expensive online testing.
