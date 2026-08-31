---
id: <kebab-case-unique-id>
title: "<Article title>"
source: "<Publisher, e.g. Netflix Tech Blog>"
url: "<canonical article or paper URL>"
published: "<YYYY-MM or YYYY-MM-DD>"
added: "<YYYY-MM-DD>"           # date this entry was written
category: <slug from taxonomy.md>
tags: [<tag>, <tag>]
novelty: <1-5>                   # Claude's score; mirrors the Claude's Take section
sourced_via: "<full-text fetch | web search>"
---

# <Article title>

**Source:** [<Publisher>](<url>) · Published <published> · Added <added>
**Category:** <Name> · **Tags:** `<tag>`, `<tag>`

## TL;DR

<Two or three sentences a busy reader can absorb in 15 seconds.>

## 1. Business context

<What problem is being solved and why it matters commercially. What was the
prior state, what was painful or expensive, what the bet is.>

## 2. Technical details

<Architecture, models, data, training, and serving. Name the concrete
techniques and give numbers where the source provides them. Prefer specifics
over generalities.>

## 3. Impact — potential & realized

<Reported metrics (realized) and the broader capabilities the approach unlocks
(potential). Separate what the source measured from what it enables.>

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: <n>/5 — <one-line verdict>

<Why this score. What is genuinely new vs. a production-first take on an
existing idea. Who is likely to copy it.>

### Similar / related work

Link every reference that points at a reachable material. For another entry already
in this bank, link its title to the sibling file, e.g.
`[**Title**](YYYY-MM-DD-id.md) (in this bank)`. For an external paper with an arXiv
id, link the title to `https://arxiv.org/abs/<id>`. Leave a reference unlinked only
when no specific URL is known (a vague body of work, "general X literature") — never
invent a URL.

- [**<Article or paper>**](<sibling-file.md or source URL>) — <one line on the connection>
- [**<Article or paper>**](<sibling-file.md or source URL>) — <one line on the connection>

### Jargon buster

- **<Term>** — <plain-language explainer, 1-2 sentences>
- **<Term>** — <plain-language explainer, 1-2 sentences>
