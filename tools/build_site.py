#!/usr/bin/env python3
"""Render the SW Buffet pack as a static, crawlable HTML site.

Single source of truth stays in pack/, core/ and evals/ - this script only
renders them. GitHub blocks crawlers from /*/tree/ URLs (see
https://github.com/robots.txt), so pack content is unreachable to search
engines on github.com; this site is the indexable surface.

Usage: python tools/build_site.py [output_dir]   (default: _site)
"""
from __future__ import annotations

import html
import posixpath
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"
BASE_URL = "https://rr26-7.github.io/sw-buffet"
SITE_ROOT = "/sw-buffet"
REPO_URL = "https://github.com/rr26-7/sw-buffet"
BLOB = REPO_URL + "/blob/main"

INDEX_TITLE = "SW Buffet - decision-governance pack for AI-assisted development"

MD_EXT = ["tables", "fenced_code", "sane_lists", "toc", "attr_list"]


def sources() -> list[tuple[Path, str, str]]:
    """(markdown path, output html path relative to site root, group)."""
    items: list[tuple[Path, str, str]] = [
        (ROOT / "README.md", "index.html", "Start"),
        (ROOT / "core" / "MINIMAL-CORE.md", "core/MINIMAL-CORE.html", "Start"),
    ]
    for p in sorted((ROOT / "pack").glob("*.md")):
        items.append((p, f"pack/{p.stem}.html", "Pack pages"))
    evals = ROOT / "evals"
    if (evals / "README.md").is_file():
        items.append((evals / "README.md", "evals/index.html", "Evals"))
    for p in sorted(evals.glob("eval-*.md")):
        items.append((p, f"evals/{p.stem}.html", "Evals"))
    return items


def first_heading(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def description(text: str) -> str:
    body = re.sub(r"^#.*$", "", text, count=1, flags=re.M)
    for para in body.split("\n\n"):
        para = " ".join(para.split())
        if not para or para.startswith(("#", "-", "*", "|", "```", ">")):
            continue
        para = re.sub(r"\*\*|__|`|\*|_", "", para)
        para = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", para)
        if len(para) <= 155:
            return para
        cut = para[:155].rsplit(" ", 1)[0]
        return cut.rstrip(",;:-") + "..."
    return ""


def rewrite_links(body: str, src_rel: Path, pages: dict[str, str]) -> str:
    def repl(m: re.Match[str]) -> str:
        href = m.group(1)
        if href.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        target, _, frag = href.partition("#")
        resolved = posixpath.normpath((src_rel.parent / target).as_posix())
        out = pages.get(resolved)
        if out:
            url = f"{SITE_ROOT}/{out}"
        elif (ROOT / resolved).exists():
            # not a rendered page (scripts, dirs): send readers to the source
            url = f"{BLOB}/{resolved}"
        else:
            return m.group(0)
        return f'href="{url}{"#" + frag if frag else ""}"'

    return re.sub(r'href="([^"]+)"', repl, body)


def nav(items: list[tuple[Path, str, str]], current: str) -> str:
    out = ['<nav class="sidebar" aria-label="Pack contents">']
    group = None
    for md, rel, grp in items:
        if grp != group:
            if group is not None:
                out.append("</ul>")
            out.append(f"<h2>{html.escape(grp)}</h2><ul>")
            group = grp
        title = first_heading(md.read_text(encoding="utf-8-sig"), md.stem)
        title = INDEX_TITLE if rel == "index.html" else title
        label = html.escape(title.replace("SW Pack - ", ""))
        href = f"{SITE_ROOT}/" if rel == "index.html" else f"{SITE_ROOT}/{rel}"
        cls = ' class="current"' if rel == current else ""
        out.append(f'<li{cls}><a href="{href}">{label}</a></li>')
    out.append("</ul></nav>")
    return "".join(out)


CSS = """
:root{color-scheme:light dark;--fg:#1f2328;--bg:#fff;--muted:#59636e;--line:#d1d9e0;--link:#0969da}
@media(prefers-color-scheme:dark){:root{--fg:#e6edf3;--bg:#0d1117;--muted:#9198a1;--line:#30363d;--link:#4493f8}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
a{color:var(--link)}
.wrap{max-width:1180px;margin:0 auto;padding:24px;display:grid;grid-template-columns:280px minmax(0,1fr);gap:40px}
.sidebar{font-size:14px;border-right:1px solid var(--line);padding-right:16px}
.sidebar h2{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);margin:20px 0 6px}
.sidebar ul{list-style:none;margin:0;padding:0}
.sidebar li{margin:3px 0}
.sidebar li.current>a{font-weight:600}
main{min-width:0}
main h1{font-size:32px;line-height:1.25;margin-top:0;border-bottom:1px solid var(--line);padding-bottom:.3em}
main h2{margin-top:2em;border-bottom:1px solid var(--line);padding-bottom:.3em}
code,pre{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13.6px}
pre{background:rgba(129,139,152,.12);padding:16px;border-radius:6px;overflow:auto}
code{background:rgba(129,139,152,.12);padding:.2em .4em;border-radius:6px}
pre code{background:none;padding:0}
table{border-collapse:collapse;display:block;overflow:auto}
th,td{border:1px solid var(--line);padding:6px 13px}
blockquote{border-left:3px solid var(--line);margin:0;padding-left:1em;color:var(--muted)}
.src{font-size:14px;color:var(--muted);margin-bottom:24px}
footer{grid-column:1/-1;border-top:1px solid var(--line);margin-top:48px;padding-top:16px;font-size:14px;color:var(--muted)}
@media(max-width:800px){.wrap{grid-template-columns:1fr}.sidebar{border-right:0;border-bottom:1px solid var(--line);padding:0 0 12px}}
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="google-site-verification" content="lMvwrmrSELT6W16PIAL0xyTgNqap5ct33aVf-eLYr78">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<style>{css}</style>
</head>
<body>
<div class="wrap">
{nav}
<main>
<p class="src"><a href="{source}">Source on GitHub</a> &middot; <a href="{repo}">rr26-7/sw-buffet</a></p>
{body}
</main>
<footer>SW Buffet &middot; MIT licensed &middot; <a href="{repo}">github.com/rr26-7/sw-buffet</a></footer>
</div>
</body>
</html>
"""


def main() -> int:
    items = sources()
    pages = {str(md.relative_to(ROOT).as_posix()): rel for md, rel, _ in items}
    OUT.mkdir(parents=True, exist_ok=True)
    urls: list[str] = []

    for md_path, rel, _ in items:
        text = md_path.read_text(encoding="utf-8-sig")
        src_rel = md_path.relative_to(ROOT)
        title = INDEX_TITLE if rel == "index.html" else \
            first_heading(text, md_path.stem) + " - SW Buffet"
        canonical = f"{BASE_URL}/" if rel == "index.html" else f"{BASE_URL}/{rel}"
        body = markdown.markdown(text, extensions=MD_EXT)
        body = rewrite_links(body, src_rel, pages)
        if rel == "index.html":
            body += contents_block(items)
        out_file = OUT / rel
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(
            PAGE.format(
                title=html.escape(title),
                desc=html.escape(description(text)),
                canonical=canonical,
                css=CSS,
                nav=nav(items, rel),
                body=body,
                source=f"{BLOB}/{src_rel.as_posix()}",
                repo=REPO_URL,
            ),
            encoding="utf-8",
        )
        urls.append(canonical)

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sitemap.append(f"  <url><loc>{html.escape(u)}</loc></url>")
    sitemap.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    # Verbatim passthrough: search-engine verification files and anything else
    # that must be served exactly as committed.
    static = ROOT / "static"
    copied = 0
    if static.is_dir():
        for f in static.rglob("*"):
            if f.is_file():
                dest = OUT / f.relative_to(static)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(f.read_bytes())
                copied += 1
        print(f"copied {copied} static file(s)")

    print(f"built {len(urls)} pages into {OUT}")
    return 0


def contents_block(items: list[tuple[Path, str, str]]) -> str:
    out = ['<h2 id="all-pages">All pages</h2>']
    group = None
    for md, rel, grp in items:
        if rel == "index.html":
            continue
        if grp != group:
            if group is not None:
                out.append("</ul>")
            out.append(f"<h3>{html.escape(grp)}</h3><ul>")
            group = grp
        text = md.read_text(encoding="utf-8-sig")
        title = html.escape(first_heading(text, md.stem).replace("SW Pack - ", ""))
        desc = html.escape(description(text))
        out.append(f'<li><a href="{SITE_ROOT}/{rel}">{title}</a> - {desc}</li>')
    out.append("</ul>")
    return "".join(out)


if __name__ == "__main__":
    sys.exit(main())
