#!/usr/bin/env python3
"""Create an UNPUBLISHED (draft) episode on RSS.com for "Data Science in the Wild".

Built against the RSS.com Core API v4 (OpenAPI 3.1). It uploads an episode as a
**draft** so the owner can review it and press publish; it never publishes on its
own.

An episode is "unpublished" precisely when it has **no `schedule_datetime`** —
the API then reports `status: "draft"`. Setting `schedule_datetime` is what
schedules/publishes, so this script simply never sends it.

Flow (RSS.com Core API v4):
  1. Auth with the account API key via the `X-Api-Key` header.
  2. GET /v4/podcasts -> find the podcast id for "Data Science in the Wild".
  3. POST /v4/podcasts/{id}/assets/presigned-uploads (asset_type=audio) -> {id,url};
     PUT the local .m4a bytes to that presigned url. Same for the cover image.
  4. POST /v4/podcasts/{id}/episodes with title, description, itunes_season,
     itunes_episode, itunes_episode_type=full, audio_upload_id, cover_upload_id
     and NO schedule_datetime  -> episode created as a draft.
  5. Record the episode id + status back into podcasts/episodes.json.

Requirements:
  - An RSS.com **Network plan** (the API is gated to it).
  - `RSS_API_KEY` in the environment (never commit it).
  - Outbound egress to api.rss.com and to the presigned storage host. This
    repo's automation environments block those by policy — run this locally, or
    in an environment whose network policy allows them.

Usage:
  export RSS_API_KEY=...                              # from RSS.com settings
  python3 automation/rss_upload.py --list-podcasts    # discover the podcast id
  python3 automation/rss_upload.py --episode 1        # dry-run (default)
  python3 automation/rss_upload.py --episode 1 --yes  # actually create the draft
  python3 automation/rss_upload.py --all --yes        # create drafts for all
                                                       # not-yet-uploaded episodes

Optional env:
  RSS_PODCAST_TITLE   override the show title to match on (default below)
  RSS_PODCAST_ID      skip title lookup and use this podcast id directly
  RSS_API_BASE        override the API base (default https://api.rss.com)
"""
import argparse
import json
import mimetypes
import os
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MANIFEST = REPO / "podcasts" / "episodes.json"
PODCAST_TITLE = os.environ.get("RSS_PODCAST_TITLE", "Data Science in the Wild")
BASE = os.environ.get("RSS_API_BASE", "https://api.rss.com")

AUDIO_MIME = {".m4a": "audio/mp4", ".mp3": "audio/mpeg", ".wav": "audio/wav"}
IMAGE_MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}


def _ctx():
    ctx = ssl.create_default_context()
    ca = os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt"
    if os.path.exists(ca):
        try:
            ctx.load_verify_locations(ca)
        except Exception:
            pass
    return ctx


def _opener():
    handlers = [urllib.request.HTTPSHandler(context=_ctx())]
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if proxy:
        handlers.append(urllib.request.ProxyHandler({"https": proxy, "http": proxy}))
    return urllib.request.build_opener(*handlers)


def api(method, path, api_key, body=None):
    """A JSON call to the RSS.com API (adds X-Api-Key)."""
    url = BASE + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("X-Api-Key", api_key)
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with _opener().open(req, timeout=120) as resp:
            raw = resp.read().decode()
            return resp.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        print(f"  ! HTTP {e.code} {method} {url}\n    {e.read().decode(errors='replace')}",
              file=sys.stderr)
        raise
    except urllib.error.URLError as e:
        print(f"  ! network error {method} {url}: {e.reason}\n"
              "    (api.rss.com is egress-blocked in this repo's automation "
              "environments — run this locally.)", file=sys.stderr)
        raise


def put_file(presigned_url, file_path, content_type):
    """Upload a local file to a presigned (PUT) URL — no API key, storage host."""
    data = Path(file_path).read_bytes()
    req = urllib.request.Request(presigned_url, data=data, method="PUT")
    req.add_header("Content-Type", content_type)
    with _opener().open(req, timeout=600) as resp:
        return resp.status


def load_manifest():
    return json.loads(MANIFEST.read_text())


def save_manifest(m):
    MANIFEST.write_text(json.dumps(m, indent=2) + "\n")


def find_episode(manifest, number):
    for ep in manifest.get("episodes", []):
        if ep.get("episode") == number:
            return ep
    return None


def known_podcast_id(manifest):
    return os.environ.get("RSS_PODCAST_ID") or manifest.get("rss_show_id")


def resolve_podcast_id(api_key, manifest):
    known = known_podcast_id(manifest)
    if known:
        return known
    _, podcasts = api("GET", "/v4/podcasts", api_key)
    items = podcasts if isinstance(podcasts, list) else podcasts.get("data", [])
    for p in items:
        if str(p.get("title", "")).strip().lower() == PODCAST_TITLE.lower():
            return p.get("id")
    raise SystemExit(f"Podcast {PODCAST_TITLE!r} not found. Seen: "
                     + ", ".join(f"{p.get('title')} (id={p.get('id')})" for p in items))


def presigned_upload(api_key, podcast_id, asset_type, file_path):
    """Request a presigned URL and PUT the file; returns the asset upload id."""
    p = Path(file_path)
    mime = (AUDIO_MIME if asset_type == "audio" else IMAGE_MIME).get(
        p.suffix.lower()) or mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    _, pre = api("POST", f"/v4/podcasts/{podcast_id}/assets/presigned-uploads", api_key,
                 {"asset_type": asset_type, "expected_mime": mime, "filename": p.name})
    upload_id, url = pre.get("id"), pre.get("url")
    if not upload_id or not url:
        raise SystemExit(f"Bad presigned response: {pre}")
    status = put_file(url, file_path, mime)
    print(f"  uploaded {asset_type}: {p.name} ({mime}) -> PUT {status}, id={upload_id}")
    return upload_id


def upload_one(ep, api_key, manifest, do_it):
    if ep.get("rss_status") in ("scheduled", "published"):
        print(f"Episode {ep['episode']} is already {ep['rss_status']} — skipping.")
        return
    season = ep.get("season", manifest.get("season", 1))
    audio_path = REPO / ep["audio"]
    if not audio_path.exists():
        raise SystemExit(f"Audio file missing: {audio_path}")
    cover_rel = ep.get("cover")
    cover_path = REPO / cover_rel if cover_rel else None
    has_cover = bool(cover_path and cover_path.exists())

    body = {
        "title": ep["title"],
        "description": ep["description"],
        "itunes_season": season,
        "itunes_episode": ep["episode"],
        "itunes_episode_type": "full",
        # NOTE: schedule_datetime is intentionally omitted -> episode stays a DRAFT.
    }

    print(f"Episode S{season}E{ep['episode']:02d} — {ep['title']!r}")
    print(f"  audio : {audio_path.relative_to(REPO)}")
    print(f"  cover : {cover_path.relative_to(REPO) if has_cover else '(none)'}")
    print(f"  create: POST {BASE}/v4/podcasts/<id>/episodes  "
          f"{json.dumps({**body, 'audio_upload_id': '<audio>', 'cover_upload_id': '<cover>'})}")
    print("  status will be: draft (no schedule_datetime sent)")

    if not do_it:
        print("  (dry-run — nothing uploaded. Re-run with --yes to create the draft.)")
        return

    podcast_id = resolve_podcast_id(api_key, manifest)
    print(f"  podcast_id: {podcast_id}")
    body["audio_upload_id"] = presigned_upload(api_key, podcast_id, "audio", audio_path)
    if has_cover:
        body["cover_upload_id"] = presigned_upload(api_key, podcast_id, "image", cover_path)

    _, created = api("POST", f"/v4/podcasts/{podcast_id}/episodes", api_key, body)
    status = created.get("status")
    print(f"  ✓ episode created: id={created.get('id')} status={status}")
    if status == "published":
        print("  ⚠️  WARNING: episode is published, not a draft — check the API/account "
              "default and unpublish in the RSS.com dashboard.", file=sys.stderr)

    ep["rss_status"] = status or "draft"
    ep["rss_episode_id"] = created.get("id")
    if not manifest.get("rss_show_id"):
        manifest["rss_show_id"] = podcast_id
    save_manifest(manifest)
    print(f"  updated {MANIFEST.relative_to(REPO)}. Review it on RSS.com and publish "
          "when ready.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--episode", type=int, help="episode number from episodes.json")
    ap.add_argument("--all", action="store_true",
                    help="process every episode whose rss_status is not_uploaded")
    ap.add_argument("--list-podcasts", action="store_true",
                    help="print your RSS.com podcasts (id + title) and exit")
    ap.add_argument("--yes", action="store_true",
                    help="actually upload + create the draft (default is dry-run)")
    args = ap.parse_args()

    api_key = os.environ.get("RSS_API_KEY")
    if not api_key:
        raise SystemExit("RSS_API_KEY is not set. Export your RSS.com API key first.")

    if args.list_podcasts:
        _, podcasts = api("GET", "/v4/podcasts", api_key)
        print(json.dumps(podcasts, indent=2))
        return

    manifest = load_manifest()

    if args.all:
        pending = [e for e in manifest.get("episodes", [])
                   if e.get("rss_status", "not_uploaded") not in ("draft", "scheduled", "published")]
        if not pending:
            print("No episodes with rss_status 'not_uploaded' — nothing to do.")
            return
        for ep in pending:
            upload_one(ep, api_key, manifest, args.yes)
        return

    if args.episode is None:
        raise SystemExit("Pass --episode N, --all, or --list-podcasts.")
    ep = find_episode(manifest, args.episode)
    if ep is None:
        raise SystemExit(f"Episode {args.episode} not found in {MANIFEST}.")
    upload_one(ep, api_key, manifest, args.yes)


if __name__ == "__main__":
    main()
