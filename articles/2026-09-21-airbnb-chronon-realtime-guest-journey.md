---
id: airbnb-chronon-realtime-guest-journey
title: "The Guest Journey, Updated in Real Time: Extending Airbnb's Sequence Recommender with Chronon"
source: "Airbnb Tech Blog"
url: "https://medium.com/airbnb-engineering/the-guest-journey-updated-in-real-time-extending-airbnbs-sequence-recommender-with-chronon-8f1582578553"
published: "2026-09"
added: "2026-09-21"
category: personalization-recsys
tags: [sequence-modeling, feature-store, real-time-features, transformer, chronon, feature-freshness]
novelty: 3
sourced_via: "web search"
---

# The Guest Journey, Updated in Real Time: Extending Airbnb's Sequence Recommender with Chronon

**Source:** [Airbnb Tech Blog](https://medium.com/airbnb-engineering/the-guest-journey-updated-in-real-time-extending-airbnbs-sequence-recommender-with-chronon-8f1582578553) · Published 2026-09 · Added 2026-09-21
**Category:** Personalization & Recommender Systems · **Tags:** `sequence-modeling`, `feature-store`, `real-time-features`, `transformer`, `chronon`, `feature-freshness`

## TL;DR

Airbnb's guest-journey sequence recommender used to learn what a guest wanted from a nightly batch snapshot of their activity, so a listing viewed five minutes ago wouldn't shape search results until the next day. The team added two capabilities — Near-real-time Model Transform and Push Mode — to Chronon, Airbnb's open-source feature platform, so a guest's transformer-encoded profile refreshes the moment they view a listing or search, without putting the expensive multi-layer transformer back on the search-time critical path.

## 1. Business context

Airbnb's search ranking already leans on a sequence recommender (previously described in Airbnb's JourneyFormer work) that encodes a guest's recent activity — searches, listing views, wishlists — into an embedding the ranking model conditions on. The problem the post addresses is staleness: the sequence encoder was run as a nightly batch job, so a guest's profile embedding reflected only activity through the previous day. A guest actively shopping — viewing several listings, refining a search, coming back an hour later — wouldn't have any of that session's signal available to the next search until the following day's batch run caught up. For a marketplace where guests often browse in short, intent-dense bursts, that lag means the ranking model is working from a slightly outdated picture of what the guest actually wants right now, at exactly the moment when fresh signal would matter most.

## 2. Technical details

The original design kept the sequence encoder — a multi-layer transformer, too expensive to run inline on every search request — off the serving-time critical path with a two-stage split: offline, a scheduled nightly batch job encoded the previous day's guest activity into an embedding and wrote it to a low-latency store; online, search just read that precomputed embedding cheaply. That kept latency low but tied freshness to the batch cadence.

The extension adds two capabilities to **Chronon**, Airbnb's feature engineering platform (open source, with these additions contributed back to the public repo):

- **Push Mode** — lets a feature respond to an event (a guest viewing a listing or issuing a search) as it happens, rather than only on a fixed batch schedule.
- **Near-real-time Model Transform** — when a triggering event fires, Chronon combines the new signal with the guest's existing stored history and re-runs the same sequence-recommender model to produce a refreshed embedding, asynchronously on the event path rather than inline on the search path.

The net effect is that the heavy transformer computation still never blocks a search request — it's triggered by guest activity events in the background — but the guest's profile embedding is refreshed close to real time instead of waiting for the next nightly batch. By the time the guest's next search happens, the stored embedding already reflects what they did moments ago.

## 3. Impact — potential & realized

**Realized:** Airbnb's guest-journey sequence recommender no longer depends on a full day-old snapshot of guest behavior; recent within-session activity (a listing view, a refined search) can now shape the very next search's ranking. The capabilities have been contributed back to the open-source Chronon project, making near-real-time feature refresh available to any team already using Chronon for feature engineering. Specific online experiment metrics (e.g., a booking or engagement lift) were not included in the search-surfaced summaries available for this write-up and are omitted here rather than guessed.

**Potential:** the pattern generalizes beyond Airbnb's guest journey — any sequence-model-based recommender built on a feature platform with an event bus can, in principle, adopt the same event-triggered "recompute and cache" pattern to close the gap between batch feature freshness and real-time relevance, without paying transformer inference cost on the serving path itself.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a well-executed, production-first take on a known pattern

Event-triggered incremental feature recomputation (keep the expensive model off the request path, refresh cached state asynchronously as events arrive) is an established technique in large-scale recsys — near-real-time feature stores exist at several companies. What's genuinely useful here is the specific, concrete application: extending Chronon with first-class primitives (Push Mode, Near-real-time Model Transform) for re-running a *sequence transformer* on an event trigger, and open-sourcing that capability rather than keeping it as internal plumbing. That's solid engineering, not a new idea.

### Similar / related work

- [**JourneyFormer: Encoding Airbnb Guest Journey with Sequence Modeling**](2026-09-06-airbnb-journeyformer-guest-sequence-search-ranking.md) (in this bank) — the underlying sequence-recommender model this post extends with real-time feature updates; JourneyFormer describes the modeling approach, this post describes making its inputs fresh.
- [**Personalizing Airbnb search by learning from the guest journey**](https://medium.com/airbnb-engineering/personalizing-airbnb-search-by-learning-from-the-guest-journey-bcefd1915624) — an earlier Airbnb Tech Blog post on using guest-journey signals for search personalization, providing context for why journey freshness matters.
- General real-time / streaming feature store literature (e.g., feature platforms that support event-driven feature computation) — left unlinked as a broad area rather than one specific paper.

### Jargon buster

- **Chronon** — Airbnb's open-source feature engineering platform, used to define, compute, and serve features consistently for both offline training and online inference.
- **Sequence recommender** — a recommendation model that encodes a user's ordered history of actions (searches, views, clicks) with a sequence model (often a transformer) to capture evolving intent, rather than treating each interaction independently.
- **Push Mode** — a feature-computation mode where a feature updates in response to an incoming event, instead of waiting for the next scheduled batch run.
- **Feature freshness** — how up-to-date a machine-learned feature is relative to real-world events; batch-computed features are only as fresh as the last batch run, while event-triggered features can be near real time.
