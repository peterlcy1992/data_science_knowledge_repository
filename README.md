# Data Science Cutting-Edge Knowledge Bank

A self-refreshing repository of the most interesting applied data science, ML,
and AI-engineering articles from top industry engineering blogs and research
labs. Each entry is more than a link: it is a structured, opinionated deep
summary written to let you absorb the substance of an article in a few minutes.

## What's in an entry

Every article lives as one Markdown file in [`articles/`](articles/) and is
registered in [`index.json`](index.json). Each entry contains:

1. **Business context** — the problem, why it matters, what was at stake.
2. **Technical details** — architecture, models, data, training, serving, and
   the key techniques, with concrete numbers where the source gives them.
3. **Impact (potential & realized)** — metrics reported, and the broader
   ripple effects the approach enables.

Then a **Claude's Take** section adds:

- **Novelty assessment** — how new/important the idea is, scored `/5` with
  reasoning (this is an opinion, clearly labelled as such).
- **Similar / related work** — other articles and papers in the same space.
- **Jargon buster** — plain-language explainers of the technical terms used.

## How it stays fresh

A daily **Claude Code Routine** (see
[`refresh-playbook.md`](refresh-playbook.md)) wakes each morning, searches the
curated [`sources.md`](sources.md) list for newly published articles, writes new
entries, updates [`index.json`](index.json), and emails a digest containing:

1. A **deep dive** on one article (prioritising the most recently added ones
   that have not yet been featured), and
2. A **list of newly added articles** from that run.

The digest is delivered as a Claude Code owner notification — no
email-sending code ships into the Silvia product (per the repo's hard rule on
outbound user messaging).

## Layout

```
.
  README.md            — this file
  index.json           — machine-readable index of every full deep-dive entry
  catalog.json         — backlog of lightweight leads awaiting deep-dive write-ups
                         (mostly Snacks Weekly episodes), upgraded over time
  taxonomy.md          — category definitions
  sources.md           — curated source list (seed from the "Snacks Weekly on
                         Data Science" podcast, plus expansions)
  TEMPLATE.md          — the entry template new articles are written against
  refresh-playbook.md  — the exact steps the daily Routine follows
  articles/            — one Markdown file per article
  digests/             — archived copies of each day's email digest
```

## Two tiers: deep dives and the backlog

- **Deep dives** (`index.json` + `articles/`) are the full structured write-ups.
- **Backlog** (`catalog.json`) is a lightweight list of leads — mostly episodes
  of the *Snacks Weekly on Data Science* podcast — captured with a company,
  title, category, and one-line hook. The daily refresh upgrades backlog stubs
  into full deep dives over time. The podcast's full feed is egress-blocked
  here, so the backlog is a best-effort recovery via web search (~45 of 101
  episodes so far) and grows as the Routine runs.

## Reading the bank

- Browse by category: open [`index.json`](index.json) or
  [`taxonomy.md`](taxonomy.md).
- Newest first: entries are sorted by `added` date in `index.json`.
- Every entry links back to its original source; opinions are always fenced
  under **Claude's Take** and are not the source's claims.
