---
id: airbnb-travel-destination-recommendations-explore
title: "Recommending Travel Destinations to Help Users Explore"
source: "Airbnb Tech Blog"
url: "https://airbnb.tech/ai-ml/recommending-travel-destinations-to-help-users-explore/"
published: "2026-06"
added: "2026-09-14"
category: personalization-recsys
tags: [destination-recommendation, sequence-modeling, transformer, multi-task-learning, geolocation, cold-start, airbnb]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Recommending Travel Destinations to Help Users Explore

**Source:** [Airbnb Tech Blog](https://airbnb.tech/ai-ml/recommending-travel-destinations-to-help-users-explore/) · Published 2026-06 · Added 2026-09-14
**Category:** Personalization & Recommender Systems · **Tags:** `destination-recommendation`, `sequence-modeling`, `transformer`, `multi-task-learning`, `geolocation`

## TL;DR

A large slice of Airbnb's traffic is users who don't yet know where they want to go — they're exploring, not searching for a specific listing. Airbnb built a transformer-style sequence model over booking, view, and search history that predicts likely destination regions and cities to nudge these undecided users toward a concrete next step, deployed in both search autosuggest and abandoned-search emails.

## 1. Business context

Airbnb identified a meaningful user segment stuck in the "exploration" stage of trip planning: no fixed destination, no fixed dates, no clear preferences yet. These users visit less frequently than intent-driven searchers and rarely book soon after a session — but they're not lost causes, they're an audience the product can actively help move forward. The bet is that surfacing well-chosen destination suggestions can spark inspiration, reduce the decision friction that keeps exploratory users from converting, and drive broader engagement, rather than leaving them to either bounce or arrive at a destination decision entirely on their own.

## 2. Technical details

The model borrows directly from language modeling: user actions are treated as tokens in a sequence, drawn from three behavioral sources — booking history, view history, and search history. Each action's embedding combines the city/region visited with the temporal distance from the prediction point, and contextual signals like the current time of year capture seasonality (predicting winter destinations differently than summer ones).

Two design choices stand out:

- **Multi-task, multi-granularity geolocation heads.** Rather than predicting only a city or only a region, the model adds separate prediction heads for region-level and city-level destinations trained jointly, letting the model exploit Airbnb's geolocation hierarchy (e.g., recognizing San Francisco and San Jose both belong to the Bay Area) to learn richer, more transferable location representations than either granularity alone would produce.
- **Stratified training data for active vs. dormant users.** The training set is built differently depending on how "active" a user's trip-planning signal is: for users 1–7 days before a booking, the model uses the full behavioral signal (booking, view, and search history); for users 8–365 days out, it uses only booking data, to simulate the sparse-signal reality of someone very early in planning. This dual strategy generates 14 training examples per booking event, explicitly designed so the model doesn't only learn to predict destinations for users who already show strong intent signals.

## 3. Impact — potential & realized

**Realized:** An A/B test of the resulting autosuggest feature showed "significant booking gains in regions where English is not the primary language" — a notable result suggesting the model helps most where text search is a weaker signal of intent. Airbnb also reports the approach benefits users beyond the destination-uncertain segment, including those looking for more affordable neighboring alternatives to a destination they already have in mind. The source does not publish an aggregate booking or engagement lift number.

**Potential:** The model powers two concrete product surfaces — city autosuggest when a user first opens the search bar, and destination-based re-engagement emails for users who abandoned a search — and the same sequence-plus-geo-hierarchy approach could extend to other coarse-to-fine recommendation problems (e.g., suggesting a neighborhood before a specific listing).

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid, well-engineered application of known techniques to a real cold-start problem

Sequence-to-embedding modeling for user intent is well established, and the multi-task region/city heads are a sensible but incremental design choice. What makes this a good production case study rather than a routine one is the explicit stratified-data strategy for handling users at wildly different stages of intent formation — that's the kind of unglamorous data-construction detail that often matters more than model architecture, and it's rare for companies to describe it this concretely.

### Similar / related work

- [**JourneyFormer: Encoding Airbnb Guest Journey with Sequence Modeling**](2026-09-06-airbnb-journeyformer-guest-sequence-search-ranking.md) (in this bank) — another Airbnb sequence model over guest behavior, applied to search ranking rather than destination suggestion; likely shares underlying behavioral-sequence infrastructure with this work.
- [**Scaling Conditional Learned Retrieval for Pinterest Home Feed**](2026-09-14-pinterest-scaling-conditional-learned-retrieval-home-feed.md) (in this bank) — a different company's answer to the same underlying challenge of representing a user who holds multiple, unresolved intents at once.
- [**How Instacart Uses Machine Learning to Suggest Replacements for Out-of-Stock Products**](2026-09-11-instacart-ml-replacement-recommendations.md) (in this bank) — a different flavor of the same "help an undecided or blocked user take a next step" recommendation problem.

### Jargon buster

- **Cold-start (exploration-stage) user** — A user who hasn't yet formed a specific, searchable intent, making standard search or item-based recommendation weak because there's little concrete signal to match against.
- **Multi-task learning** — Training one model with several prediction heads (here, region and city) simultaneously, so shared representations benefit from signal that any single task alone wouldn't fully capture.
- **Stratified training data** — Deliberately constructing different training examples for different user segments (here, "active" vs. "dormant" planners) so the model doesn't overfit to the segment with the richest signal.
