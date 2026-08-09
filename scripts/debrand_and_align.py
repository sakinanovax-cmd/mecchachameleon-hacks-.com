# -*- coding: utf-8 -*-
"""Remove site brand names from visible/meta copy; restore logo URL; keep buy/support redirects."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGO = "https://zadeyo.com/_next/image?url=%2Frt-removebg-preview.png&w=64&q=75"
LOGO_ESC = LOGO.replace("&", "&amp;")
DOMAIN = "https://mecchahacks.com"
TODAY = date.today().isoformat()

# Visible/meta brand replacements — never print store name
REPLACEMENTS = [
    ("Meccha Hacks", "Meccha Chameleon Cheats"),
    ("meccha hacks", "meccha chameleon cheats"),
]


def scrub_text(text: str) -> str:
    for a, b in REPLACEMENTS:
        text = text.replace(a, b)
    return text


def set_logo_srcs(text: str) -> str:
    # navbar/footer/favicon/apple to required remote logo
    text = re.sub(
        r'(src=")images/logo(?:-64)?\.png(")',
        rf"\1{LOGO_ESC}\2",
        text,
    )
    text = re.sub(
        r'(href=")images/logo(?:-64)?\.png(")',
        rf"\1{LOGO_ESC}\2",
        text,
    )
    # schema logo absolute
    text = re.sub(
        r'("logo":\s*")[^"]*(")',
        rf'\1{LOGO}\2',
        text,
    )
    text = re.sub(
        r'("url":\s*")https://mecchahacks\.com/images/logo\.png(")',
        rf'\1{LOGO}\2',
        text,
    )
    # ImageObject logo in schemas
    text = text.replace(
        '"url": "https://mecchahacks.com/images/logo.png"',
        f'"url": "{LOGO}"',
    )
    return text


def scrub_author_meta(text: str) -> str:
    text = re.sub(
        r'<meta name="author" content="[^"]*">',
        '<meta name="author" content="Meccha Chameleon Cheats">',
        text,
    )
    text = re.sub(
        r'<meta property="og:site_name" content="[^"]*">',
        '<meta property="og:site_name" content="Meccha Chameleon Cheats">',
        text,
    )
    return text


def fix_footer_brand(text: str) -> str:
    # footer brand text node after img
    text = re.sub(
        r'(class="footer-brand">[\s\S]*?</img>\s*)Meccha Chameleon Cheats',
        r"\1Meccha Chameleon Cheats",
        text,
    )
    # Support Channel -> Support
    text = text.replace(">Support Channel<", ">Support<")
    return text


def process_html(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    original = text
    text = scrub_text(text)
    text = set_logo_srcs(text)
    text = scrub_author_meta(text)
    text = fix_footer_brand(text)
    # Ensure no bare word Zadeyo/ZADEYO in visible content (URLs allowed)
    # Remove any accidental brand words in titles/text outside hrefs
    if re.search(r"(?i)zadeyo", text):
        # only flag if appears outside URLs
        stripped = re.sub(r"https?://[^\s\"'<>]+", "", text)
        stripped = re.sub(r"href=\"[^\"]+\"", "", stripped)
        stripped = re.sub(r"src=\"[^\"]+\"", "", stripped)
        if re.search(r"(?i)zadeyo", stripped):
            print("WARN visible zadeyo", path.name)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print("updated", path.name)


def update_manifest() -> None:
    path = ROOT / "site.webmanifest"
    data = {
        "name": "Meccha Chameleon Cheats",
        "short_name": "Meccha Cheats",
        "description": "Meccha Chameleon cheats, guides, and lobby tools.",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#0B0914",
        "theme_color": "#0B0914",
        "lang": "en",
        "icons": [
            {
                "src": LOGO,
                "sizes": "64x64",
                "type": "image/png",
                "purpose": "any",
            }
        ],
    }
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_seo_harden_defaults() -> None:
    p = ROOT / "scripts" / "seo_harden.py"
    if not p.exists():
        return
    t = p.read_text(encoding="utf-8")
    t = t.replace("Meccha Hacks", "Meccha Chameleon Cheats")
    t = t.replace(
        'LOGO = "https://zadeyo.com/_next/image?url=%2Frt-removebg-preview.png&w=64&q=75"',
        f'LOGO = "{LOGO}"',
    )
    # ensure author content uses product name
    t = t.replace(
        '<meta name="author" content="Meccha Chameleon Cheats">',
        '<meta name="author" content="Meccha Chameleon Cheats">',
    )
    p.write_text(t, encoding="utf-8")


def main() -> None:
    for path in sorted(ROOT.glob("*.html")):
        process_html(path)
    update_manifest()
    update_seo_harden_defaults()
    # generators
    for name in ("generate_seo_blogs.py", "rebuild_blog_index.py"):
        p = ROOT / "scripts" / name
        if p.exists():
            t = scrub_text(p.read_text(encoding="utf-8"))
            t = t.replace("images/logo.png", LOGO_ESC)
            # keep logo constant if present
            t = re.sub(
                r'LOGO = "[^"]+"',
                f'LOGO = "{LOGO}"',
                t,
            )
            p.write_text(t, encoding="utf-8")
            print("script", name)
    print("done")


if __name__ == "__main__":
    main()
