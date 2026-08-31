---
id: netflix-video-annotator-active-learning-vlm
title: "Video Annotator: A Framework for Efficiently Building Video Classifiers Using Vision-Language Models and Active Learning"
source: "Netflix Tech Blog"
url: "https://netflixtechblog.com/video-annotator-building-video-classifiers-using-vision-language-models-and-active-learning-8ebdda0b2db4"
published: "2024-06"
added: "2026-08-31"
category: cv-multimodal
tags: [active-learning, vision-language-models, video-classification, human-in-the-loop, annotation]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Video Annotator: A Framework for Efficiently Building Video Classifiers Using Vision-Language Models and Active Learning

**Source:** [Netflix Tech Blog](https://netflixtechblog.com/video-annotator-building-video-classifiers-using-vision-language-models-and-active-learning-8ebdda0b2db4) · Published 2024-06 · Added 2026-08-31
**Category:** Computer Vision & Multimodal · **Tags:** `active-learning`, `vision-language-models`, `video-classification`, `human-in-the-loop`

## TL;DR

Netflix built **Video Annotator (VA)**, a self-service framework that combines
zero-shot vision-language model (VLM) embeddings with an active-learning loop
so domain experts — not ML engineers — can bootstrap and iterate on video
classifiers cheaply. Across 56 labels and 500,000 shots it beat the strongest
baseline by a median 8.3 points of Average Precision.

## 1. Business context

Netflix needs many narrow video classifiers — one for each specific
content-understanding task a creative or product team needs (identifying a
particular visual style, scene type, or content attribute) — but training a
custom classifier per task the conventional way requires ML engineering
resources and large hand-labeled datasets for every new label. That doesn't
scale to the long tail of ad hoc classification needs across Netflix's media
teams. The bet behind Video Annotator was to let domain experts (video
editors, not ML engineers) build classifiers themselves, cheaply, using a
human-in-the-loop tool built on top of VLM embeddings.

## 2. Technical details

- **Bootstrapping via text-to-video search.** Users start by finding an
  initial set of relevant examples in a large, diverse video corpus using
  **text-to-video search**, powered by the video and text encoders of a
  vision-language model to extract shared embeddings — no labeled data
  required to get started.
- **Active learning loop.** VA then trains a **lightweight binary classifier**
  directly on the VLM's video embeddings, scores all clips in the corpus with
  it, and surfaces the most informative unlabeled examples back to the
  annotator for labeling — the classic active-learning cycle of
  train-score-select-label, repeated with direct domain-expert involvement.
- **Human-in-the-loop by design.** The whole pipeline is built for iteration
  by non-ML-engineer domain experts (video editors), who both bootstrap the
  seed set and drive the active-learning labeling loop.
- **Released dataset.** The team released a dataset of **153k labels across
  56 video-understanding tasks**, annotated by three professional video
  editors using VA itself.

## 3. Impact — potential & realized

- **Realized:** Across experiments spanning **56 labels and 500,000 shots**,
  VA achieved a **median 8.3-point improvement in Average Precision** versus
  the strongest competing baseline.
- **Potential:** A general recipe — VLM embeddings plus active learning plus
  a self-service UI — for letting non-ML domain experts build narrow,
  high-quality video classifiers on demand, reducing dependence on
  ML-engineering bandwidth for the long tail of content-understanding needs.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid, well-executed combination of established techniques

Zero-shot VLM embeddings and active learning are each well-established; the
contribution here is packaging them into a self-service tool that domain
experts can drive without ML engineers, validated at real scale (56 tasks,
500k shots, a released dataset). It's a strong production engineering story
rather than a new method, which is why it lands at 3 rather than higher.

### Similar / related work

- **MediaFM: The Multimodal AI Foundation for Media Understanding at Netflix**
  — a related, more recent Netflix effort building shared multimodal
  foundations for media understanding tasks.
- **MAPS: Multimedia Asset Personalization via Multimodal Embeddings at
  Netflix** (in this bank) — another Netflix system built on multimodal
  embeddings, applied to asset personalization rather than classifier
  bootstrapping.
- General active-learning-for-annotation literature — VA is a concrete,
  VLM-embedding-based instance of the classic pool-based active-learning
  paradigm.

### Jargon buster

- **Vision-language model (VLM)** — a model trained jointly on images/video
  and text so that both modalities land in a shared embedding space,
  enabling text-to-video search and zero-shot classification.
- **Active learning** — a training strategy where the model itself selects
  which unlabeled examples would be most informative to label next, rather
  than labeling data randomly.
- **Zero-shot** — using a model on a task it wasn't specifically trained for,
  with no task-specific labeled examples.
- **Average Precision (AP)** — a standard metric summarizing a classifier's
  precision-recall trade-off across thresholds into a single score.
