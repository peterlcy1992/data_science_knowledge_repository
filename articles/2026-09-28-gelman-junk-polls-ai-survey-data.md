---
id: gelman-junk-polls-ai-survey-data
title: "It's Fine to Use Computer-Generated Survey Responses — If You Don't Care About the Data Anyway"
source: "Statistical Modeling, Causal Inference, and Social Science (Andrew Gelman)"
url: "https://statmodeling.stat.columbia.edu/2026/09/24/junk-polls-and-junk-survey-research-they-go-together-so-well/"
published: "2026-09"
added: "2026-09-28"
category: statistical-modeling
tags: [survey-methodology, llm-generated-data, synthetic-respondents, research-quality, polling]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# It's Fine to Use Computer-Generated Survey Responses — If You Don't Care About the Data Anyway

**Source:** [Statistical Modeling, Causal Inference, and Social Science (Andrew Gelman)](https://statmodeling.stat.columbia.edu/2026/09/24/junk-polls-and-junk-survey-research-they-go-together-so-well/) · Published 2026-09 · Added 2026-09-28
**Category:** Statistical Modeling · **Tags:** `survey-methodology`, `llm-generated-data`, `synthetic-respondents`, `research-quality`, `polling`

## TL;DR

Andrew Gelman argues that substituting LLM-generated ("computer-generated") respondents for real survey data isn't a new problem — it's the same old problem of low-quality, unaccountable survey and polling practice, just with a new tool for cutting the same corners. Pollsters and researchers who were already comfortable adjusting, herding toward, or effectively fabricating numbers to match expectations will find synthetic respondents a convenient upgrade, not a new failure mode.

## 1. Business context

A wave of vendors and researchers now offer LLM-simulated ("synthetic") survey respondents as a fast, cheap substitute for fielding real human panels — useful in principle for early-stage product or message testing where speed matters more than precision. The pitch is that a model can stand in for a demographic segment's likely opinions without the cost and latency of a real fielded survey. Gelman's post responds to this trend by asking a pointed question: for organizations that are already willing to publish numbers with a thin evidentiary basis — low response-rate polls papered over with heavy post-hoc adjustment, "herding" toward other pollsters' published numbers, or survey designs flexible enough to produce whatever result was wanted — does swapping in an LLM to generate the raw responses actually change anything, or does it just remove even the pretense of empirical grounding?

## 2. Technical details

The post's argument is not a technical critique of any specific LLM-simulation method; it's a methodology-and-incentives argument. Gelman's point is that traditional survey research already has well-documented soft spots — low response rates requiring substantial statistical adjustment to be usable, "herding" behavior where pollsters nudge their numbers toward the consensus of other published polls rather than reporting what they actually measured, and enough researcher-degrees-of-freedom in exclusion rules and weighting choices to steer a result toward a desired conclusion. His claim is that an organization willing to exploit that flexibility to produce a number it likes doesn't need real respondents at all — it could "cut out the middleman" and just make up a number, so long as there's a plausible-looking data paper trail. Feeding a prompt to an LLM and treating its output as if it were real human survey responses is, in his framing, simply a more sophisticated version of that same paper trail: it looks more like real data collection than an outright fabricated number would, without actually solving the underlying accountability problem, because the LLM's outputs reflect its training and prompting, not any accountable sampling process from the population the survey claims to represent.

## 3. Impact — potential & realized

This is an opinion/critique piece rather than an empirical study, so there's no reported metric to cite — the "impact" is on how practitioners and consumers of survey research should read claims based on LLM-generated respondents. The implication for teams considering synthetic-respondent tools is a sharpened version of an old due-diligence question: the risk isn't really "is the LLM's simulation accurate," it's "does this organization's overall research process have the accountability and transparency to make any data source — human or synthetic — trustworthy." Gelman's broader point (echoed elsewhere in the literature on synthetic survey panels) is that junk methodology produces junk conclusions regardless of what technology fills in the individual answers, so the fix isn't better LLM calibration, it's the same rigor (transparent sampling, pre-registered analysis, accountable reporting) that good survey research always required.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — A sharp framing, but a restatement of long-standing methodological skepticism

The underlying critique — that flexible, unaccountable survey practices can produce whatever result is wanted — is not new; Gelman and others have made versions of this argument for years about traditional polling (herding, researcher degrees of freedom, weighting flexibility). Applying it to LLM-generated respondents is a natural and well-aimed extension rather than a new insight. It's a useful, quotable framing for practitioners evaluating synthetic-respondent vendors, but it doesn't introduce new evidence or a new methodological tool — hence the low novelty score despite being directionally correct and worth keeping in mind.

### Similar / related work

- [**This Is How We Do Modern Frequentist Statistics: Using Fake-Data Simulation to Understand What Can Happen in a Study**](2026-09-25-gelman-fake-data-simulation-frequentist.md) (in this bank) — a constructive counterpart from the same author: simulation used honestly, to understand a *proposed* study design, rather than as a substitute for real data collection.
- **"Synthetic Replacements for Human Survey Data? The Perils of Large Language Models"** (Political Analysis) — an academic companion finding that LLM-simulated respondents are highly sensitive to prompt wording and model version, and can inflate or invent between-segment differences that don't exist in real human data, giving empirical teeth to Gelman's more polemical argument here.
- **Herding in political polling** (general survey-methodology literature) — the documented practice of pollsters nudging published estimates toward the consensus of other polls, which Gelman references as the pre-existing failure mode that synthetic respondents don't fix.

### Jargon buster

- **Herding (in polling)** — when pollsters' published numbers cluster suspiciously close to each other or to a consensus forecast, suggesting adjustment toward expected results rather than independent measurement.
- **Researcher degrees of freedom** — the many small, seemingly reasonable choices in data cleaning, exclusion rules, and analysis (which respondents to drop, how to weight, which model to report) that, taken together, give a researcher enough flexibility to steer a result toward a desired conclusion without any single choice looking like outright misconduct.
- **Synthetic / LLM-generated respondents** — survey "answers" produced by prompting a large language model to simulate how a person (or demographic segment) might respond, used as a stand-in for fielding a real human panel.
