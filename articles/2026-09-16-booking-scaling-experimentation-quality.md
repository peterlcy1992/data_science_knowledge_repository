---
id: booking-scaling-experimentation-quality
title: "Scaling Experimentation Quality at Booking.com"
source: "Booking.com ML & DS Blog"
url: "https://booking.ai/scaling-experimentation-quality-at-booking-com-726152ee4ef0"
published: "2026-03"
added: "2026-09-16"
category: experimentation-causal
tags: [experimentation-platform, ab-testing, organizational-scaling, quality-metrics]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Scaling Experimentation Quality at Booking.com

**Source:** [Booking.com ML & DS Blog](https://booking.ai/scaling-experimentation-quality-at-booking-com-726152ee4ef0) · Published 2026-03 · Added 2026-09-16
**Category:** Experimentation & Causal Inference · **Tags:** `experimentation-platform`, `ab-testing`, `organizational-scaling`, `quality-metrics`

## TL;DR

Booking.com describes how it scaled experiment *quality* alongside experiment *volume* by choosing education over enforcement: rather than gatekeeping experiments through a central team, it built a shared-responsibility model across product teams, a central experimentation team, and "experiment ambassadors," backed by a quality metric surfaced directly in their experimentation platform — an approach that surfaced, among other things, that 80% of experiments initially lacked a power calculation.

## 1. Business context

Running thousands of A/B tests only creates value if the results are trustworthy; a high-volume, low-quality experimentation culture just produces confident-sounding but wrong conclusions faster. As Booking.com's experimentation volume grew, the central team faced a familiar organizational choice: enforce strict methodological controls (a bottleneck as volume scales) or invest in educating experimenters so quality holds up without a central gate. They chose education, betting that experimenters who understand *why* a practice matters will apply it correctly and challenge bad methodology themselves, rather than experimenters who are just following a checklist imposed on them.

## 2. Technical details

The organizational model splits responsibility three ways: **product teams** run and own their own experiments; a **central experimentation team** builds and maintains the platform, tooling, and quality standards; and **experiment ambassadors** — embedded points of contact within product teams — help spread methodological practice without centralizing every decision through one team.

The technical backbone is an **experimentation quality metric** integrated directly into Booking.com's internal experimentation platform ("ET"), rather than living in a separate audit process. The central team built a dashboard on top of this metric to make experiment quality visible and monitorable across the organization in something close to real time, rather than discoverable only after the fact via post-hoc review.

Early data surfaced by this instrumentation was blunt: 80% of experiments did not have a power calculation performed before launch — meaning a large majority of tests were being run without a principled basis for whether the sample size could actually detect the effect size the team cared about. Making that gap visible, rather than assuming it away, appears to have been the practical starting point for the rest of the initiative.

## 3. Impact — potential & realized

**Realized:** Booking.com reports successfully scaling experiment quality alongside experiment volume using the shared-responsibility model, with the quality dashboard providing ongoing visibility rather than a one-time audit.

**Potential:** The general pattern — invest in a central platform, then push methodological autonomy and ownership out to product teams with a shared quality metric as the common visible standard — is a transferable organizational template for any company scaling experimentation beyond what a single gatekeeping team can review by hand.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — A useful organizational case study, not a new method

There's no new statistical technique here — this is a process and culture piece about how to scale experimentation governance, not how to run better individual experiments. The value is in the concrete organizational template (education-over-enforcement, ambassadors, an embedded quality metric) and the honest data point (80% of experiments lacking a power calculation) rather than any methodological innovation. Useful for a team facing the same scaling problem, but incremental relative to established experimentation-platform practice.

### Similar / related work

- [**Why Spotify Is Not Using Bayesian A/B Testing**](2026-09-16-spotify-bayesian-ab-testing-critique.md) (in this bank) — a sharper contrast in kind: Spotify's piece is a rigorous statistical-methodology argument, while Booking.com's is an organizational-scaling case study; together they cover the two very different meanings of "experimentation quality" (statistical rigor vs. organizational process).
- [**Harnessing the Power of Geo-Experimentation: How Mercado Libre Measures the Effectiveness of Its Third-Party Media Strategies Using GeoLift**](2026-09-13-mercadolibre-geo-experimentation-geolift.md) (in this bank) — another applied experimentation write-up from the same broader coverage window, focused on a specific measurement technique rather than organizational scaling.
- **Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments*** — the standard reference on running experimentation programs at scale, including statistical power and organizational practice; no single URL specified.

### Jargon buster

- **Statistical power / power calculation** — A pre-experiment calculation of whether a planned sample size is large enough to reliably detect an effect of the size you actually care about; skipping it risks running an experiment that could never have found a real effect even if one existed.
- **Experiment ambassador** — A person embedded within a product team (rather than the central experimentation team) who helps that team apply good experimentation practice locally, spreading expertise without centralizing every review.
- **Shared-responsibility model** — An organizational structure where ownership of an outcome (here, experiment quality) is distributed across multiple groups — product teams, a central platform team, and embedded ambassadors — rather than concentrated in one gatekeeping team.
