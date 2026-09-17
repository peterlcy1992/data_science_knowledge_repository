---
id: yelp-video-review-moderation
title: "Moderating Inappropriate Video Content at Yelp"
source: "Yelp Engineering Blog"
url: "https://engineeringblog.yelp.com/2024/03/moderating-inappropriate-video-content-at-yelp.html"
published: "2024-03"
added: "2026-09-17"
category: cv-multimodal
tags: [content-moderation, video-classification, trust-and-safety, frame-sampling, deep-learning]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Moderating Inappropriate Video Content at Yelp

**Source:** [Yelp Engineering Blog](https://engineeringblog.yelp.com/2024/03/moderating-inappropriate-video-content-at-yelp.html) · Published 2024-03 · Added 2026-09-17
**Category:** Computer Vision & Multimodal · **Tags:** `content-moderation`, `video-classification`, `trust-and-safety`, `frame-sampling`, `deep-learning`

## TL;DR

After adding video uploads to reviews, Yelp built a moderation pipeline that pre-filters incoming videos against a database of previously-removed content via similarity hashing, then runs unmatched videos through a multi-label deep learning classifier — extending its existing photo-moderation model — using selective frame sampling instead of full-video processing to keep inference cost manageable, with flagged content routed to human reviewers rather than auto-removed.

## 1. Business context

Yelp introduced video uploads alongside written reviews in April 2023, and video submissions grew significantly afterward. Video brings the same trust-and-safety exposure as photos — nudity, violence, extremist content — but at substantially higher moderation cost: a video is effectively many frames' worth of content to check rather than one image, and processing every frame of every uploaded video would be far more expensive than photo moderation at Yelp's scale. The team needed a moderation pipeline that caught the same categories of harmful content as their existing photo system without that cost blowing up, while still protecting the recall/false-positive balance that keeps trust-and-safety enforcement from frustrating legitimate users.

## 2. Technical details

The pipeline runs in parallel with video ingestion and has two stages:

1. **Similarity-hash pre-filter.** Incoming videos are checked against a database of hashes of previously-removed content. A match auto-blocks the video immediately, without invoking the more expensive classification model — this catches repeat offenders re-uploading known-bad content cheaply.
2. **Deep learning multi-label classification.** Videos that pass the hash check go to a neural network classifier built on top of Yelp's existing photo-moderation model, extended to handle video. Rather than scoring every frame, the system uses **selective frame sampling** — processing a subset of frames rather than the full video — trading some theoretical accuracy for tractable inference cost, then combines the individual sampled-frame scores into one final video-level determination.

Videos whose combined classification score exceeds the category-specific threshold are hidden proactively and routed to Yelp's User Operations team for human review, rather than being auto-removed outright — reflecting the same recall/false-positive tradeoff Yelp's photo-moderation system manages: catching truly harmful content matters, but incorrectly removing legitimate content discourages genuine participation. The team also uses account-level signals to pre-emptively flag suspicious uploaders, reducing the volume of video that needs to reach the expensive classification stage at all.

## 3. Impact — potential & realized

**Realized:** The pipeline is described as Yelp's production video-moderation system, built by extending the company's existing photo-moderation infrastructure rather than building a video model from scratch. No specific accuracy, precision/recall, or cost figures are disclosed in the source post.

**Potential:** The general pattern — cheap similarity-based pre-filtering before an expensive classifier, plus selective sampling to make video-scale inference tractable — generalizes to any platform adding video moderation on top of an existing photo-moderation stack, and the account-level pre-flagging idea extends naturally to reducing load on any per-item trust-and-safety pipeline.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — Sound, pragmatic engineering; no new modeling idea

Similarity hashing for known-bad content and frame sampling to control video-inference cost are both standard trust-and-safety techniques; the value here is in the pragmatic system design — reusing the existing photo-moderation model as the backbone for video rather than building separately, and layering pre-filters to keep the expensive path small — rather than any novel architecture or algorithm.

### Similar / related work

- **Standard image/video content-moderation classifiers used industry-wide (e.g. at Meta, Google, TikTok)** — the broader body of practice this design draws on; no specific comparable post from this bank covers video-specific trust-and-safety moderation yet, making this a useful first entry in the `cv-multimodal` category for that topic.
- [**Beyond the Model: Engineering AI Infra with Scientific Judgement**](2026-09-17-airbnb-insight-miner-agent-harness-scientific-judgement.md) (in this bank) — a different trust-and-safety-adjacent investigation workflow (customer-service edge cases rather than content moderation), useful contrast in how "safety-critical unstructured content review" gets tackled with very different tooling.

### Jargon buster

- **Similarity hashing** — Generating a compact fingerprint of a piece of content so that near-duplicate or previously-seen content can be matched cheaply, without re-running a full classifier on it.
- **Multi-label classification** — A model that can assign more than one category to a single input at once (e.g. a video could be flagged for both "violence" and "hate speech" simultaneously), as opposed to picking a single label.
- **Frame sampling** — Processing only a selected subset of a video's frames (rather than every frame) to reduce compute cost, then combining the sampled frames' results into one overall judgment.
