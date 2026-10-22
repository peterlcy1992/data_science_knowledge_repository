#!/usr/bin/env python3
"""Pick the NotebookLM source for the daily deep-dive podcast.

The hosts should read the paper or post itself, not our summary of it: our
summaries are often written from the abstract alone, and their "Claude's
Take" / related-work notes are opinion that the hosts would treat as fact.

  python3 automation/podcast_source.py urls  articles/<id>.md
      Print candidate full-text URLs for the article, best first, one per
      line. arXiv papers map to the full-text HTML and PDF renderings (the
      /abs page is abstract-only); anything else is the article URL itself.
      NotebookLM fetches URLs on Google's side, so this works even when the
      run environment cannot reach the site.

  python3 automation/podcast_source.py brief articles/<id>.md <out.md>
      Fallback when no URL loads: write a facts-only brief -- front-matter
      facts, TL;DR and sections 1-3 -- dropping Claude's Take, novelty score,
      related work and jargon notes. If the entry was not built from the full
      text, the brief says so, so the hosts report gaps instead of filling them.
"""
import re
import sys
from pathlib import Path


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            k, sep, v = line.partition(":")
            if sep:
                fm[k.strip()] = v.split("#", 1)[0].strip().strip('"')
    return fm, text[m.end():] if m else text


def urls(path):
    fm, _ = front_matter(Path(path).read_text())
    url = fm.get("url", "")
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5})", url)
    if m:
        aid = m.group(1)
        return [f"https://arxiv.org/html/{aid}", f"https://arxiv.org/pdf/{aid}"]
    return [url] if url else []


def brief(path, out):
    fm, body = front_matter(Path(path).read_text())
    # Keep everything up to the rule that opens "Claude's Take".
    facts = re.split(r"\n---\s*\n\s*## Claude's Take", body, maxsplit=1)[0]
    facts = re.sub(r"^\*Sourced from.*\*\s*$", "", facts, flags=re.M).strip()
    lines = [f"Source: {fm.get('source', '')}",
             f"URL: {fm.get('url', '')}",
             f"Published: {fm.get('published', '')}", ""]
    if "full-text" not in fm.get("sourced_via", "") or re.search(
            r"abstract[- ]level|abstract only|full text not (read|reviewed)", body, re.I):
        lines += ["Note: this is a summary written from the paper's abstract, not its full "
                  "text. Anything not stated below is not reported here.", ""]
    Path(out).write_text("\n".join(lines) + "\n" + facts + "\n")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "urls":
        print("\n".join(urls(sys.argv[2])))
    elif len(sys.argv) == 4 and sys.argv[1] == "brief":
        brief(sys.argv[2], sys.argv[3])
    else:
        sys.exit(__doc__)
