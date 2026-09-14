---
id: uber-airport-driver-availability-forecasting
title: "Forecasting Models to Improve Driver Availability at Airports"
source: "Uber Engineering Blog"
url: "https://www.uber.com/us/en/blog/forecasting-models-to-improve-availability-at-airports/"
published: "2026"
added: "2026-09-14"
category: forecasting-timeseries
tags: [demand-forecasting, marketplace, transformer, gaussian-mixture-models, streaming, airports, uber]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Forecasting Models to Improve Driver Availability at Airports

**Source:** [Uber Engineering Blog](https://www.uber.com/us/en/blog/forecasting-models-to-improve-availability-at-airports/) · Published 2026 · Added 2026-09-14
**Category:** Forecasting & Time Series · **Tags:** `demand-forecasting`, `marketplace`, `transformer`, `gaussian-mixture-models`, `streaming`

## TL;DR

Airports are roughly 15% of Uber's global mobility gross bookings but behave like a distinct, FIFO-queue marketplace where flight delays and weather cause demand spikes that don't follow normal city patterns. Uber built three complementary forecasting models — queue wait time, earnings-per-hour, and short-horizon driver deficit — to help drivers decide whether to wait in the airport queue and to proactively summon more drivers before a shortage hits, lifting wait-time prediction precision by +30 percentage points for short waits.

## 1. Business context

Airport pickups don't work like a typical city ride request: drivers queue in a first-in-first-out (FIFO) holding lot and wait for their turn, rather than being matched to the nearest available rider. That structure creates two distinct failure modes. In **oversupply**, drivers face long, uncertain queue waits, which pushes some of them to "cherry-pick" — rejecting lower-value trips once they finally reach the front, since they've already sunk significant wait time and want the wait to pay off. In **undersupply**, riders face long pickup waits and higher cancellation rates, directly hurting reliability on a segment that represents a substantial share of Uber's mobility revenue. Making both sides of this marketplace work requires giving drivers enough information to make a good wait/don't-wait decision, and giving the platform enough foresight to correct imbalances before they show up as rider-facing pain — both of which are harder at airports than in the city because flight schedules, delays, and weather create irregular, poorly-forecastable demand surges.

## 2. Technical details

Uber built three purpose-specific forecasting systems rather than one general model:

- **ETR (Estimated Time to Request)** predicts how long a driver will wait in the queue before receiving a ride request. The upgraded version replaced an older heuristic that separately forecast demand and queue length and then combined them, with a single unified model trained directly against actual observed wait times as its target — a more direct supervision signal than composing two indirect forecasts.
- **Earnings Per Hour (EPH)** gives drivers a real-time comparison of expected earnings from staying in the airport queue versus repositioning to city trips, to inform that decision with data instead of guesswork. Rather than predicting a single expected value, EPH models the full earnings distribution using **Deep Gaussian Mixture Models**, explicitly capturing the heavy-tailed reality that some drivers, during low-demand windows, get very few trips — a single-point estimate would understate that risk.
- **Driver deficit forecasting** predicts marketplace imbalance in 5-minute intervals over a 30-minute forward horizon, feeding a system that proactively summons more drivers to the airport before a shortage materializes rather than reacting after riders start seeing long waits. This uses a **transformer-encoder-style architecture with 1D convolutional layers** adapted for time-series forecasting, chosen to handle the variable-length sequences that streaming marketplace data produces.

The data and serving pipeline behind all three: Apache Flink streaming jobs aggregate real-time queue length, demand, and flight-schedule data into feature vectors; Apache Spark batch jobs compute historical EPH patterns over 4-week lookback windows; and Apache Cassandra serves the resulting features for low-latency online inference. Predictions surface both to drivers directly (in-app) and to internal backend services that trigger proactive driver summoning.

## 3. Impact — potential & realized

**Realized:** The upgraded ETR model achieved a **+30 percentage point absolute** improvement in precision for correctly predicting short (0–15 minute) wait scenarios — a meaningful gain in the wait-time band that most affects whether a driver decides to enter the queue at all. Airports represent roughly **15% of Uber's global mobility gross bookings**, so improvements here have outsized platform-wide impact even though they're confined to a specific marketplace segment.

**Potential:** Uber describes EPH and the driver-summoning features built on deficit forecasting as still under active development, with "positive" early results but no finalized production impact numbers disclosed yet — meaning the fuller payoff (reduced cherry-picking, fewer rider cancellations from undersupply) is still ahead rather than fully realized at publication.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid, well-instrumented marketplace engineering rather than a new modeling idea

None of the individual techniques here — unified target training instead of composed heuristics, mixture-density modeling for skewed outcomes, transformer-style short-horizon forecasting — are novel in isolation. The value is in recognizing that a FIFO queue marketplace needs three distinct, purpose-built forecasts (wait time, earnings comparison, imbalance) rather than one general demand model, and building the streaming infrastructure to serve all three at the latency a driver decision actually needs.

### Similar / related work

- [**Real-Time Spatial Temporal Forecasting @ Lyft**](2026-09-13-lyft-realtime-spatial-temporal-forecasting.md) (in this bank) — a direct industry peer solving a related marketplace-forecasting problem, with an explicit discussion of when classical time-series methods beat deep learning.
- [**Using Marketplace Marginal Values to Address Interference Bias**](2026-09-11-lyft-marketplace-marginal-values-interference-bias.md) (in this bank) — tackles a related two-sided-marketplace measurement problem (interference bias in experiments) that would directly apply to evaluating changes like this ETR upgrade.
- [**DeepETT: Graph-Aware Traffic Forecasting**](2026-08-31-uber-deepett-graph-aware-traffic-forecasting.md) (in this bank) — another Uber forecasting system, applied to traffic rather than marketplace supply/demand, sharing the same broader forecasting-infrastructure lineage.

### Jargon buster

- **FIFO queue (airport marketplace)** — A first-in-first-out holding system where drivers wait their turn for the next ride request, structurally different from city dispatch where drivers are matched by proximity.
- **Deep Gaussian Mixture Model** — A neural network that outputs the parameters of a mixture of Gaussian distributions rather than a single predicted value, letting it represent multi-modal or heavy-tailed outcomes (e.g., "usually X, but sometimes much less").
- **Cherry-picking** — When a driver selectively accepts only higher-value trip requests and rejects lower-value ones, a behavior that long queue waits tend to encourage.
