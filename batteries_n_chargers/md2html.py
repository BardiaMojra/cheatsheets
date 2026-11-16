#!/usr/bin/env python3
"""Render one markdown file to a styled, self-contained HTML page for PDF printing.

Used by build_pdfs.sh; also usable alone:
    python3 md2html.py cards/00_safety_card.md build/00_safety_card.html card
The third arg picks the body class ("guide" or "card"), which selects the page
size and type scale in style/cheatsheet.css. Images stay local file:// paths.
"""
import os
import re
import sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
CSS = os.path.join(HERE, "style", "cheatsheet.css")

HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<link rel="stylesheet" href="file://{css}">
</head>
<body class="{cls}">
<main>
{body}
</main>
</body>
</html>
"""


IMG_RE = re.compile(r'<img\s[^>]*src="([^"]+)"[^>]*>')


def fill_missing_images(html):
    """Swap any <img> whose file is not on disk for a labelled placeholder slot.

    Photos are downloaded separately into img/; until one lands, its figure
    prints as a hatched box naming the file that belongs there, so the layout
    is final and dropping the photo in needs no edit to the markdown.
    """

    def sub(m):
        src = m.group(1)
        if src.startswith(("http:", "https:", "data:", "file:")):
            return m.group(0)
        abspath = os.path.join(HERE, src)
        if not os.path.exists(abspath):
            # the fetcher names files by their real extension; match the slot anyway
            stem = os.path.splitext(abspath)[0]
            for alt in (".jpg", ".jpeg", ".png"):
                if os.path.exists(stem + alt):
                    abspath = stem + alt
                    break
        if os.path.exists(abspath):
            # the HTML is rendered into build/, so relative paths must be absolutised.
            # src is the path as written in the markdown -- substitute on that, not on
            # the resolved name, or the replace silently matches nothing.
            return m.group(0).replace(f'src="{src}"', f'src="file://{abspath}"')
        return f'<div class="slot">photo slot<br>{os.path.basename(src)}</div>'

    return IMG_RE.sub(sub, html)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    cls = sys.argv[3] if len(sys.argv) > 3 else "guide"
    text = open(src, encoding="utf-8").read()
    md = markdown.Markdown(
        extensions=["tables", "attr_list", "fenced_code", "admonition", "toc", "md_in_html"],
        extension_configs={"toc": {"permalink": False}},
    )
    body = fill_missing_images(md.convert(text))
    title = os.path.splitext(os.path.basename(src))[0].replace("_", " ")
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write(HTML.format(title=title, css=CSS, cls=cls, body=body))
    print(f"  html  {os.path.relpath(dst, HERE)}")


if __name__ == "__main__":
    main()
