#!/usr/bin/env python3
"""Download connector photos from Wikimedia Commons into img/.

Commons is used because every file carries an explicit licence, which this script
records in img/sources.md alongside the author and the file's description page.

    python3 fetch_images.py            # fetch only what is still missing
    python3 fetch_images.py --force    # re-fetch everything
    python3 fetch_images.py xt90 deans # only these slots

Commons rate-limits hard (HTTP 429), so requests are throttled and retried with
backoff. A download that fails, or that returns a file too small to be a usable
photo, is discarded rather than left behind as a broken slot.

Filenames match the slots in img/README.md, and the build matches a slot by name
regardless of extension, so a rebuild picks the photos up with no markdown edit:
    ./build_pdfs.sh
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "img")
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "uta-cse-cheatsheet-builder/1.0 (educational use; contact lab manager)"}

# Commons full-text search matches words, not parts: "Deans" returned a Navy machinist
# named Dean and a road junction in England. A candidate's file title must contain one of
# these before it is downloaded.
MUST_MATCH = {
    "xt30":     ["xt30", "xt 30"],
    "xt60":     ["xt60", "xt 60"],
    "xt90":     ["xt90", "xt 90"],
    "deans":    ["deans", "t-plug", "t plug"],
    "ec5":      ["ec5", "ec3"],
    "tamiya":   ["tamiya"],
    "anderson": ["powerpole", "anderson power"],
    "bullet":   ["bullet connector", "banana plug", "4mm plug", "bullet plug"],
    "jst":      ["jst", "balancer"],
    "jst_xh":   ["xh", "balancer"],
    "molex":    ["molex"],
    "usbc":     ["usb-c", "usb c", "type-c", "type c"],
}

PER_SLOT = 3            # candidates per connector, to pick from
THUMB_WIDTH = 1200      # wide enough for print at the size used in the documents
MIN_BYTES = 8 * 1024    # anything smaller is an icon or a sketch, not a usable photo
THROTTLE = 1.5          # seconds between requests, to stay under the rate limit

# slot prefix -> search terms, tried in order until the slot has enough candidates
QUERIES = {
    "xt30":     ["XT30 connector", "XT30 plug"],
    "xt60":     ["XT60 connector", "XT60 plug battery"],
    "xt90":     ["XT90 connector", "XT90 plug"],
    "deans":    ["Deans connector", "T-plug connector RC", "Ultra T plug"],
    "ec5":      ["EC5 connector", "EC3 connector battery"],
    "tamiya":   ["Tamiya connector battery"],
    "anderson": ["Anderson Powerpole"],
    "bullet":   ["bullet connector electrical", "banana plug 4mm RC"],
    "jst":      ["JST connector"],
    "jst_xh":   ["JST XH connector balance", "Balancer XH"],
    "molex":    ["Molex connector", "Molex KK connector"],
    "usbc":     ["USB-C connector", "USB Type-C plug"],
}


def get(url, tries=4):
    """Fetch a URL, backing off on 429/5xx."""
    for attempt in range(tries):
        try:
            time.sleep(THROTTLE)
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503) and attempt < tries - 1:
                wait = THROTTLE * (3 ** (attempt + 1))
                print(f"       rate limited ({exc.code}), waiting {wait:.0f}s")
                time.sleep(wait)
                continue
            raise
    raise RuntimeError("retries exhausted")


def search(query):
    url = API + "?" + urllib.parse.urlencode({
        "action": "query", "generator": "search", "gsrsearch": query,
        "gsrnamespace": "6", "gsrlimit": "8", "prop": "imageinfo",
        "iiprop": "url|extmetadata", "iiurlwidth": str(THUMB_WIDTH),
        "format": "json", "formatversion": "2"})
    return json.loads(get(url)).get("query", {}).get("pages", [])


def existing(slot, n):
    """Return the path of an already-downloaded candidate, whatever its extension."""
    for ext in (".jpg", ".png", ".jpeg"):
        path = os.path.join(OUT, f"{slot}_{n:02d}{ext}")
        if os.path.exists(path) and os.path.getsize(path) >= MIN_BYTES:
            return path
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    force = "--force" in sys.argv
    slots = {k: v for k, v in QUERIES.items() if not args or k in args}
    os.makedirs(OUT, exist_ok=True)
    rows, kept = [], 0

    for slot, queries in slots.items():
        n = 0
        seen = set()
        for query in queries:
            if n >= PER_SLOT:
                break
            try:
                pages = search(query)
            except Exception as exc:
                print(f"[fail] {slot} search '{query}': {exc}")
                continue
            for page in pages:
                if n >= PER_SLOT:
                    break
                info = (page.get("imageinfo") or [{}])[0]
                origin = info.get("url", "")
                ext = os.path.splitext(urllib.parse.urlparse(origin).path)[1].lower()
                if ext not in (".jpg", ".jpeg", ".png") or page["title"] in seen:
                    continue
                title = page["title"].lower()
                if not any(term in title for term in MUST_MATCH.get(slot, [slot])):
                    continue  # matched the words, not the part
                seen.add(page["title"])
                n += 1
                name = f"{slot}_{n:02d}{'.jpg' if ext in ('.jpg', '.jpeg') else '.png'}"
                dest = os.path.join(OUT, name)
                meta = info.get("extmetadata", {})
                licence = meta.get("LicenseShortName", {}).get("value", "?")
                author = re.sub("<[^>]+>", "", meta.get("Artist", {}).get("value", "?")).strip()

                have = existing(slot, n)
                if have and not force:
                    print(f"[skip] {os.path.basename(have)}")
                    rows.append((os.path.basename(have), page["title"], author, licence,
                                 info.get("descriptionurl", "")))
                    kept += 1
                    continue
                try:
                    data = get(info.get("thumburl") or origin)
                except Exception as exc:
                    print(f"[fail] {name}: {exc}")
                    n -= 1
                    seen.discard(page["title"])
                    continue
                if len(data) < MIN_BYTES:
                    print(f"[drop] {name}: only {len(data)} bytes, not a usable photo")
                    n -= 1
                    continue
                with open(dest, "wb") as fh:
                    fh.write(data)
                print(f"[ok]   {name}  {len(data)//1024} KB  ({licence})")
                rows.append((name, page["title"], author, licence, info.get("descriptionurl", "")))
                kept += 1
        if n == 0:
            print(f"[none] {slot}: no usable candidate found on Commons")

    # drop any zero-byte or junk file left by an earlier interrupted run
    for fn in sorted(os.listdir(OUT)):
        path = os.path.join(OUT, fn)
        if not fn.endswith((".jpg", ".jpeg", ".png")):
            continue
        size = os.path.getsize(path)
        if size < MIN_BYTES:
            os.remove(path)
            print(f"[rm]   {fn}: {size} bytes, unusable")

    with open(os.path.join(OUT, "sources.md"), "w", encoding="utf-8") as fh:
        fh.write("# Image sources\n\nGenerated by `fetch_images.py`. Every file is from "
                 "Wikimedia Commons; the licence column is what Commons reports. Keep this "
                 "file in step with `img/` — it is the attribution record.\n\n")
        fh.write("| File | Commons title | Author | Licence | Page |\n|---|---|---|---|---|\n")
        for name, title, author, licence, page in rows:
            fh.write(f"| `{name}` | {title} | {author} | {licence} | <{page}> |\n")

    print(f"\n{kept} candidates in img/, listed in img/sources.md")
    print("Pick one per connector, rename it to the slot name in img/README.md "
          "(extension does not matter), delete the rest, then run ./build_pdfs.sh")


if __name__ == "__main__":
    main()
