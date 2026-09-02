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

Bootstrap + precondition — run this first; if the final check is non-zero, skip
per above (missing secret, no tool, or no egress):

```sh
# 1. Materialize the master token from the environment secret, if present.
if [ -n "$NOTEBOOKLM_MASTER_TOKEN_JSON" ]; then
  umask 077; mkdir -p ~/.notebooklm/profiles/default
  printf '%s' "$NOTEBOOKLM_MASTER_TOKEN_JSON" > ~/.notebooklm/profiles/default/master_token.json
  chmod 600 ~/.notebooklm/profiles/default/master_token.json
fi
# 2. Install the CLI if absent (headless extra — pure Python, no browser).
command -v notebooklm >/dev/null 2>&1 || pip install "notebooklm-py[headless]" >/dev/null 2>&1
# 3. Gate: only proceed if the tool is present AND auth refreshes (needs the
#    secret + egress to Google). A non-zero exit here means skip.
command -v notebooklm >/dev/null 2>&1 && notebooklm auth refresh --quiet >/dev/null 2>&1
```

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

**Prerequisites (one-time, environment-level — cannot be done from inside a run).**
Use the **master-token** auth: durable, self-refreshing, pure-Python (no browser).

1. On a normal machine, with a **dedicated/throwaway Google account**:
   `pip install "notebooklm-py[headless]"` then
   `notebooklm login --master-token --account <you@gmail.com>`. This writes
   `~/.notebooklm/profiles/default/master_token.json`.
2. Add that file's JSON to the Routine's environment as a **secret** named
   `NOTEBOOKLM_MASTER_TOKEN_JSON` (env `env_01Kyo6JpRMFq4tGL5wUee1Ln`). Never
   commit the token — it grants full account access, hence the throwaway account.
3. Ensure the environment's **network policy allows outbound access to Google /
   NotebookLM**.

At run time, Step 6c (or the environment setup script) materializes it before use:

```sh
umask 077; mkdir -p ~/.notebooklm/profiles/default
printf '%s' "$NOTEBOOKLM_MASTER_TOKEN_JSON" > ~/.notebooklm/profiles/default/master_token.json
chmod 600 ~/.notebooklm/profiles/default/master_token.json
command -v notebooklm >/dev/null 2>&1 || pip install "notebooklm-py[headless]" >/dev/null 2>&1
notebooklm auth refresh --quiet   # mints fresh web cookies from the master token
```

Until the secret + egress are in place, Step 6c no-ops by design and the digest
notes the skip.

## Step 6d — Episode metadata, cover art & RSS.com draft (best-effort)

Run this **only when Step 6c actually produced an `.m4a`**. Every part is
best-effort — never fail the run over it. The audio lives in the podcast show
**Data Science in the Wild** (see [`podcasts/SHOW.md`](podcasts/SHOW.md)).

1. **Episode notes.** Write `podcasts/<YYYY-MM-DD>-<id>.md` — the episode title
   and a one-paragraph description built from the article's substance. Title:
   `"<Company> — <short hook>"`. End the description with a
   `Source article: "<article title>" — <source>, <url> (published <YYYY-MM>).`
   line taken from the article's front matter. Do **not** reference the internal
   knowledge bank — the podcast audience can't see it.

2. **Manifest.** Append an entry to [`podcasts/episodes.json`](podcasts/episodes.json)
   (the manifest `automation/rss_upload.py` reads). Use `next_episode` for the
   `episode` number, then increment `next_episode`. Fields:
   `{ "episode": N, "season": 1, "date": "<YYYY-MM-DD>", "title": "...",
   "description": "...", "audio": "podcasts/<YYYY-MM-DD>-<id>.m4a",
   "cover": "podcasts/<YYYY-MM-DD>-<id>.cover.png", "rss_status": "not_uploaded" }`.
   Keep `title`/`description` identical to the sidecar `.md`.

3. **Cover art.** Generate a mono-color episode tile with the source company's
   stylized wordmark (an attribution treatment — never a reproduction of a
   trademarked logo). Derive the company from the article's `source`/front
   matter, then:

   ```sh
   NODE_PATH=/opt/node22/lib/node_modules node automation/podcast_cover.js \
     --company "<Company>" \
     --title "<short display title>" \
     --overline "<category or theme>" \
     --subtitle "<one short line>" \
     --episode <N> \
     --out "podcasts/<YYYY-MM-DD>-<id>.cover.png"
   ```

   Optional `--motif signal|sequence|loop` (default `signal`); palette + monogram
   are auto-derived from the company when not overridden with `--ink/--accent-ink/--mono`.
   Needs Node + Playwright + Chromium (present in this environment; set
   `CHROMIUM_PATH` only if auto-detect fails). If it errors, skip and leave the
   `cover` field null.

4. **RSS.com draft (best-effort).** Create an **unpublished draft** episode on
   RSS.com:

   ```sh
   python3 automation/rss_upload.py --episode <N> --yes
   ```

   It needs `RSS_API_KEY` and egress to `api.rss.com`; if either is missing it
   exits cleanly — then skip and leave `rss_status` `"not_uploaded"`, noting in
   the digest that the episode is ready for a manual/local upload. **NEVER
   publish** — the script only ever creates a draft; the owner publishes from the
   RSS.com dashboard. On success it records `rss_status`/`rss_episode_id` back
   into `episodes.json`.

Add a short line to the digest reflecting what happened, e.g.
`🎙️ Episode S1E<N> — cover ✓, RSS draft ✓` (or `RSS: not configured — ready for
local upload`).

## Step 7 — Deliver & persist

- Commit everything on the branch (articles, `index.json`, `catalog.json`,
  `index.html`, the digest, and — if a podcast was produced in Step 6c/6d —
  today's `podcasts/<YYYY-MM-DD>-<id>.m4a`, its `.md` sidecar and `.cover.png`,
  and the updated `podcasts/episodes.json`) with a message like
  `refresh <YYYY-MM-DD> (+N articles)` and push with `git push -u origin main`
  (retry on network errors with exponential backoff).
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
- RSS.com uploads (Step 6d) only ever create an **unpublished draft** — never
  publish or schedule an episode. The owner reviews and publishes each draft.
- Never commit secrets (`RSS_API_KEY`, the NotebookLM token). They come from the
  environment; the repo only reads them.
- Company wordmarks on covers are stylized attribution treatments — never
  reproduce a company's actual trademarked logo.
