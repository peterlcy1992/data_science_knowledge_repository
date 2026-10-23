#!/usr/bin/env python3
"""Pick and add the NotebookLM source for the daily deep-dive podcast.

The hosts should read the paper or post itself, not our summary of it: our
summaries are often written from the abstract alone, and their "Claude's
Take" / related-work notes are opinion that the hosts would treat as fact.

  python3 automation/podcast_source.py add articles/<id>.md <notebook_id>
      Add exactly ONE source to the notebook and print a JSON result:
        {"podcast_source": "full_text" | "summary", "method": ..., "note": ...}
      Attempts, in order, keeping the first that loads real text (>= 8000
      chars, so an error page or abstract page doesn't count):
        1. pdf_upload  download the PDF here and upload it as a file
                       (works only if this environment can reach the host)
        2. url         let NotebookLM fetch each full-text URL on Google's side
        3. brief       facts-only brief of our entry (the fallback)
      Every notebooklm call names the notebook with -n, so it never depends on
      `notebooklm use` context. Each attempt's outcome is in "attempts" so a
      fallback always says why.

  python3 automation/podcast_source.py urls articles/<id>.md
      Print candidate full-text URLs, best first. arXiv papers map to the
      full-text HTML and PDF renderings (the /abs page is abstract-only).

  python3 automation/podcast_source.py brief articles/<id>.md <out.md>
      Write the facts-only brief: front-matter facts, TL;DR and sections 1-3,
      without Claude's Take, novelty score, related work or jargon notes. If
      the entry was not built from the full text, the brief says so, so the
      hosts report gaps instead of filling them.
"""
import json
import os
import re
import ssl
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

MIN_CHARS = 8000


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            k, sep, v = line.partition(":")
            if sep:
                fm[k.strip()] = v.split("#", 1)[0].strip().strip('"')
    return fm, text[m.end():] if m else text


def arxiv_id(url):
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5})", url or "")
    return m.group(1) if m else None


def urls(path):
    fm, _ = front_matter(Path(path).read_text())
    url = fm.get("url", "")
    aid = arxiv_id(url)
    if aid:
        return [f"https://arxiv.org/html/{aid}", f"https://arxiv.org/pdf/{aid}"]
    return [url] if url else []


def pdf_url(path):
    fm, _ = front_matter(Path(path).read_text())
    url = fm.get("url", "")
    aid = arxiv_id(url)
    if aid:
        return f"https://arxiv.org/pdf/{aid}"
    return url if url.lower().endswith(".pdf") else None


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


# ---- adding the source -------------------------------------------------------

def nlm(*args, timeout=600):
    """Run a notebooklm CLI command; return (returncode, stdout, stderr)."""
    try:
        p = subprocess.run(["notebooklm", *args], capture_output=True, text=True,
                           timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return 124, "", f"timed out after {timeout}s"
    except FileNotFoundError:
        return 127, "", "notebooklm CLI not found"


def tail(s, n=300):
    s = " ".join((s or "").split())
    return s[-n:]


def download_pdf(url, dest):
    """Fetch a PDF through the environment's proxy; True if it looks like one."""
    ctx = ssl.create_default_context()
    ca = os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt"
    if os.path.exists(ca):
        ctx.load_verify_locations(ca)
    handlers = [urllib.request.HTTPSHandler(context=ctx)]
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if proxy:
        handlers.append(urllib.request.ProxyHandler({"https": proxy, "http": proxy}))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (podcast source fetch)"})
    with urllib.request.build_opener(*handlers).open(req, timeout=60) as r:
        data = r.read()
    if not data.startswith(b"%PDF") or len(data) < 30000:
        raise ValueError(f"not a full PDF ({len(data)} bytes)")
    Path(dest).write_bytes(data)


def add_and_check(nb, content, title=None):
    """Add one source; keep it only if it becomes ready with >= MIN_CHARS text.
    Returns (ok, source_id, detail)."""
    args = ["source", "add", content, "-n", nb, "--json", "--request-timeout", "120"]
    if title:
        args += ["--title", title]
    if content.startswith("http"):
        args += ["--type", "url"]
    rc, out, err = nlm(*args)
    try:
        sid = json.loads(out)["source"]["id"]
    except Exception:
        return False, None, f"add failed (rc={rc}): {tail(err or out)}"
    rc, out, err = nlm("source", "wait", sid, "-n", nb, "--timeout", "300")
    if rc != 0:
        nlm("source", "delete", sid, "-n", nb, "-y")
        return False, sid, f"did not become ready (rc={rc}): {tail(err or out)}"
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
        txt = f.name
    rc, out, err = nlm("source", "fulltext", sid, "-n", nb, "-o", txt, "--force")
    chars = len(Path(txt).read_text(errors="replace")) if rc == 0 and os.path.exists(txt) else 0
    if chars < MIN_CHARS:
        nlm("source", "delete", sid, "-n", nb, "-y")
        why = f"only {chars} chars of text" if rc == 0 else f"fulltext failed (rc={rc}): {tail(err or out)}"
        return False, sid, why
    return True, sid, f"{chars} chars"


def add(path, nb):
    fm, _ = front_matter(Path(path).read_text())
    title = fm.get("title") or Path(path).stem
    attempts = []

    pdf = pdf_url(path)
    if pdf:
        dest = os.path.join(tempfile.mkdtemp(), "paper.pdf")
        try:
            download_pdf(pdf, dest)
            ok, sid, detail = add_and_check(nb, dest, title)
            attempts.append({"method": "pdf_upload", "target": pdf, "ok": ok, "detail": detail})
            if ok:
                return {"podcast_source": "full_text", "method": "pdf_upload", "source_id": sid,
                        "note": f"uploaded {pdf}", "attempts": attempts}
        except Exception as e:
            attempts.append({"method": "pdf_upload", "target": pdf, "ok": False,
                             "detail": f"download failed: {tail(str(e))}"})

    for u in urls(path):
        ok, sid, detail = add_and_check(nb, u)
        attempts.append({"method": "url", "target": u, "ok": ok, "detail": detail})
        if ok:
            return {"podcast_source": "full_text", "method": "url", "source_id": sid,
                    "note": f"NotebookLM fetched {u}", "attempts": attempts}

    out = os.path.join(tempfile.mkdtemp(), "podcast_source.md")
    brief(path, out)
    rc, o, err = nlm("source", "add", out, "-n", nb, "--json", "--title", title)
    try:
        sid = json.loads(o)["source"]["id"]
    except Exception:
        raise SystemExit(f"Could not add even the fallback brief (rc={rc}): {tail(err or o)}")
    why = "; ".join(f"{a['method']} {a['target']}: {a['detail']}" for a in attempts) or "no full-text URL"
    return {"podcast_source": "summary", "method": "brief", "source_id": sid,
            "note": f"full text unavailable ({why})", "attempts": attempts}


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) == 3 and a[0] == "add":
        print(json.dumps(add(a[1], a[2]), indent=2))
    elif len(a) == 2 and a[0] == "urls":
        print("\n".join(urls(a[1])))
    elif len(a) == 3 and a[0] == "brief":
        brief(a[1], a[2])
    else:
        sys.exit(__doc__)
