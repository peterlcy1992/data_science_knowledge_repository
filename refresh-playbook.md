# Daily refresh playbook

This is the exact procedure the daily Claude Code Routine follows. The Routine
fires a fresh session each morning with a short standalone prompt that points
here, so this file is the real spec. Keep it self-contained.

## Goal each run

1. Discover articles **published or surfaced in roughly the last 7 days** from
   [`sources.md`](sources.md) that are not already in [`index.json`](index.json).
2. Write a full entry (per [`TEMPLATE.md`](TEMPLATE.md)) for each genuinely new,
   high-signal article. Quality over quantity — 0 to ~5 per day is normal.
3. Update [`index.json`](index.json).
4. Compose and archive a digest, and email it to the owner via the Routine's
   completion notification.

## Step 1 — Set up

- Work on branch `main` (create from the
  latest default branch if it does not exist locally).
- Read `index.json` to know what is already captured (match on `url` and on
  `id`; also treat near-duplicate titles as already-captured).

## Step 2 — Discover

- For each source area, run web searches such as:
  - `<company> engineering blog machine learning <current month year>`
  - `Netflix | Uber | DoorDash | Spotify | Databricks new ML LLM recsys post <month year>`
  - `arxiv cs.IR OR cs.LG recent generative recommendation | retrieval | feature store`
- Web search is the primary channel because the egress proxy blocks many blog
  domains. Attempt a direct `WebFetch` only when the domain is reachable; if it
  returns `EGRESS_BLOCKED`, fall back to search-surfaced summaries and set
  `sourced_via: "web search"`.
- Dedupe against `index.json`. Skip anything already present.

## Two-tier storage

- **Full entries** — deep-dive write-ups in `articles/`, registered in `index.json`.
- **Backlog stubs** — `catalog.json` holds lightweight leads (company, title,
  category, one-line hook, best-effort url) for articles discovered but not yet
  written up — mostly recovered from the *Snacks Weekly on Data Science*
  episodes. Each run should both **add** newly discovered leads here and
  **deepen** a few of them into full entries (Step 4b).

## Step 3 — Write entries

- Copy `TEMPLATE.md`. Fill every section with **specific** content: name the
  models, techniques, and numbers. Keep business/technical/impact factual and
  attributed to the source.
- Put all opinion under **Claude's Take**: score novelty `/5` (see
  `taxonomy.md`), list 2-3 similar articles/papers, and explain the jargon.
- Choose one `category` slug from `taxonomy.md`.
- File name: `articles/<YYYY-MM-DD>-<id>.md` where `<YYYY-MM-DD>` is today.

## Step 4 — Update the index

Append one object per new article to `index.json` `articles` (newest first),
and bump the top-level `updated` date. Each object:

```json
{
  "id": "…", "title": "…", "source": "…", "url": "…",
  "published": "YYYY-MM", "added": "YYYY-MM-DD",
  "category": "…", "tags": ["…"], "novelty": 4,
  "file": "articles/YYYY-MM-DD-….md",
  "deep_dived_on": null,
  "sourced_via": "web search"
}
```

`deep_dived_on` tracks whether the article has already been the email deep dive
(null until it has). Never rewrite history for existing entries except to set
`deep_dived_on`.

## Step 4b — Deepen backlog stubs

Convert a few `catalog.json` stubs into full entries each run (aim for 2-5,
budget permitting):

1. Pick the highest-signal stubs (favor variety across companies/categories).
2. For each, locate the underlying company article (web search first; the stub's
   `url` if present is a lead, often just the podcast episode, not the source).
   Research it enough to write a genuine summary — do not fabricate.
3. Write a full entry per Step 3/4 (into `articles/` + `index.json`), setting
   `discovered_via: "Snacks Weekly on Data Science podcast"` where applicable.
4. **Remove** the deepened stub from `catalog.json` and bump its `updated`.
5. Mirror the new full entries into `index.html`'s `ARTICLES` array and drop the
   corresponding objects from its `CATALOG` array (Step 6b).

Also enumerate more episodes when you can (the full podcast feed/list is
egress-blocked, so use web search: `"Snacks Weekly on Data Science" episode
<company/topic>`) and append any genuinely new leads to `catalog.json`, deduping
against both `catalog.json` and `index.json`.

## Step 5 — Pick the deep-dive article

Choose the article to feature in today's email:

1. Prefer entries with `deep_dived_on == null`.
2. Among those, prefer the **most recently `added`** (newest first).
3. Break ties by highest `novelty`.
4. If everything has been deep-dived, pick the highest-novelty entry whose
   `deep_dived_on` is oldest (re-feature).

Set that entry's `deep_dived_on` to today's date in `index.json`.

## Step 6 — Compose the digest

Write `digests/<YYYY-MM-DD>.md` with two parts:

1. **Deep dive** — a rich, readable walk through the chosen article: the three
   substance sections plus Claude's Take, written to stand alone in an email.
2. **Newly added today** — a bulleted list of the entries created this run
   (title, source, category, one-line hook, novelty). If none were added, say
   so and note what was scanned.

## Step 6b — Update the browsable reader

`index.html` is a single-file, standalone HTML reader (served publicly via
GitHub Pages) whose article data lives in the `ARTICLES` array near the bottom
of the file. If new entries were added, mirror them into that array (same fields
used by existing entries) and bump `UPDATED`. The backlog lives in a parallel
`CATALOG` array in the same file: add new stubs there, and when a stub is
deepened, remove it from `CATALOG` and add the full object to `ARTICLES`. Keep
`index.html` and `catalog.json` in sync.

Each `related` item is a string that the reader auto-links: a bare `arXiv <id>`
becomes a link, an in-bank title listed in the `REL_LINKS` map links to its source,
and explicit `[text](url)` markdown is honoured. So write related items as plain
`Title — note` (or `[Title](url) — note` for anything not in `REL_LINKS`), and when
you add a new in-bank article that others cite, add its title → source-URL to the
`REL_LINKS` object near the top of the script. In the `articles/*.md` entries, link
related work per `TEMPLATE.md` (sibling `.md` for in-bank, `arxiv.org/abs/<id>` for
papers).

`index.html` is published by **GitHub Pages** straight from `main` — no Artifact
step. Just committing the updated `index.html` in Step 7 redeploys the public
page automatically; do not call the `Artifact` tool. Do not add `<!doctype>`,
`<html>`, `<head>`, or `<body>` tags beyond the ones already in the file, and
keep it a single self-contained document (inline CSS/JS; only the Google Fonts
`<link>` is external).

## Step 6c — Generate the deep-dive podcast (best-effort)

Turn today's deep-dive article (the one chosen in Step 5) into a NotebookLM
**deep-dive audio podcast**, using [`notebooklm-py`](https://github.com/teng-lin/notebooklm-py)
and the steering prompt in [`automation/podcast_prompt.md`](automation/podcast_prompt.md).

This step is **best-effort**: it needs NotebookLM to be installed and
authenticated in the run environment (see Prerequisites). If it is not, **skip
silently** and add one line to the digest — `🎙️ Podcast: skipped (NotebookLM not
configured in this environment)` — then carry on. Never let this step fail the run.

Precondition check first:

```sh
command -v notebooklm >/dev/null 2>&1 && notebooklm auth status >/dev/null 2>&1
```

(If `auth status` is not a valid subcommand in the installed version, treat a
successful `notebooklm create --help` plus an existing stored login as the gate.)
If the check fails, skip per above.

When available, run — substituting the chosen article's file and today's date:

```sh
# 1. New notebook for today's deep dive
notebooklm create "DS Deep Dive <YYYY-MM-DD> — <article title>"
# 2. Add the article itself as the single source (Markdown is supported)
notebooklm source add "articles/<YYYY-MM-DD>-<id>.md"
# 3. Generate a deep-dive podcast at the DEFAULT length, steered by the prompt file.
#    Confirm the exact format/length flag names with `notebooklm generate audio --help`
#    (the format is "deep-dive"; do NOT pass a length flag — default length is wanted).
notebooklm generate audio --prompt-file automation/podcast_prompt.md --wait
# 4. Download the audio into the repo
notebooklm download audio "podcasts/<YYYY-MM-DD>-<id>.m4a"
```

Then:
- Add a **Podcast** line to today's digest and to the deep-dive section:
  `🎙️ Deep-dive podcast: podcasts/<YYYY-MM-DD>-<id>.m4a` (once committed it is
  also reachable on the Pages site at
  `https://peterlcy1992.github.io/data_science_knowledge_repository/podcasts/<YYYY-MM-DD>-<id>.m4a`).
- Commit the `.m4a` with everything else in Step 7. (Audio is large — if repo
  size becomes a concern, switch to keeping only the latest file, e.g.
  `podcasts/latest.m4a`, instead of a dated archive.)

**Prerequisites (one-time, in the Routine's environment — not doable from a
normal run):** install the tool (`uv tool install "notebooklm-py[browser]"`),
and create a **persisted, non-interactive login** with a master token
(`notebooklm login --master-token --account <you@example.com>`) so fresh CI-style
sessions can authenticate without a browser. The environment also needs outbound
network access to Google/NotebookLM. Until these are in place, the step no-ops by
design and the digest notes the skip.

## Step 7 — Deliver & persist

- Commit everything on the branch (articles, `index.json`, `catalog.json`,
  `index.html`, the digest, and today's `podcasts/*.m4a` if one was produced)
  with a message like `refresh <YYYY-MM-DD> (+N articles)` and push with
  `git push -u origin main` (retry on
  network errors with exponential backoff).
- End the session with the digest as the final message so it becomes the
  owner-notification email body. Lead with the deep-dive article title and the
  count of newly added articles; if a podcast was produced, mention it.

## Guardrails

- Do **not** add email/SMS/push-sending code to the product. Delivery is only
  ever the Routine's own owner notification.
- Do not fabricate metrics or article content. If a detail is not in the
  source or search results, omit it or mark it as unclear.
- Keep opinions fenced under **Claude's Take**; never present them as the
  source's claims.
