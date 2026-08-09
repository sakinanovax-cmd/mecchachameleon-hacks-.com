# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

GOOGLE_FONTS_BLOCK = re.compile(
    r'\s*<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*'
    r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*'
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter:[^"]+" rel="stylesheet">\s*',
    re.I,
)

# sometimes amp-encoded
GOOGLE_FONTS_BLOCK2 = re.compile(
    r'\s*<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*'
    r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*'
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter:[^\"]+" rel="stylesheet">\s*',
    re.I,
)

LOCAL_FONTS = """  <link rel="preload" href="fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/inter-700.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="css/fonts.css">
"""

LOGO_REMOTE = re.compile(
    r'https://zadeyo\.com/_next/image\?url=%2Frt-removebg-preview\.png(?:&amp;|&)w=\d+(?:&amp;|&)q=\d+'
)


def patch_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    original = text

    if "css/fonts.css" not in text:
        text2, n = GOOGLE_FONTS_BLOCK.subn(LOCAL_FONTS, text, count=1)
        if n == 0:
            # try line-by-line removal
            lines = text.splitlines(keepends=True)
            out = []
            skip_next_font = False
            i = 0
            inserted = False
            while i < len(lines):
                line = lines[i]
                if "fonts.googleapis.com" in line or "fonts.gstatic.com" in line:
                    i += 1
                    continue
                if not inserted and '<link rel="stylesheet" href="css/global.css">' in line:
                    out.append(LOCAL_FONTS)
                    inserted = True
                out.append(line)
                i += 1
            text = "".join(out)
            if not inserted and "css/fonts.css" not in text:
                text = text.replace(
                    '<link rel="stylesheet" href="css/global.css">',
                    LOCAL_FONTS + '  <link rel="stylesheet" href="css/global.css">',
                    1,
                )
        else:
            text = text2

    text = LOGO_REMOTE.sub("images/logo.png", text)
    # favicon local
    text = text.replace(
        'href="images/logo.png" type="image/png"',
        'href="images/logo-64.png" type="image/png"',
    )
    # apple touch
    text = re.sub(
        r'(<link rel="apple-touch-icon" href=")[^"]+(")',
        r"\1images/logo-64.png\2",
        text,
    )

    if path.name == "index.html":
        text = optimize_index(text)

    if text != original:
        path.write_text(text, encoding="utf-8")
        print("patched", path.name)


def optimize_index(text: str) -> str:
    # Hero: responsive webp only as LCP, no competing eager preview
    old_hero = re.search(
        r'<div class="hero-bg" aria-hidden="true">[\s\S]*?</div>\s*<div class="hero-bg-shade"></div>\s*</div>',
        text,
    )
    new_hero = """<div class="hero-bg" aria-hidden="true">
        <img
          src="images/hero-bg-mobile.webp"
          srcset="images/hero-bg-mobile.webp 960w, images/hero-bg.webp 1600w"
          sizes="100vw"
          width="1600"
          height="844"
          alt=""
          decoding="async"
          fetchpriority="high"
        >
        <div class="hero-bg-shade"></div>
      </div>"""
    if old_hero:
        text = text[: old_hero.start()] + new_hero + text[old_hero.end() :]

    # preload mobile+desktop hero, drop old preload
    text = re.sub(
        r'\s*<link rel="preload" as="image" href="images/hero-bg\.webp" type="image/webp">\s*',
        """
  <link rel="preload" as="image" href="images/hero-bg-mobile.webp" type="image/webp" imagesrcset="images/hero-bg-mobile.webp 960w, images/hero-bg.webp 1600w" imagesizes="100vw" fetchpriority="high">
""",
        text,
        count=1,
    )

    # preview photo lazy (not LCP)
    text = text.replace(
        'src="images/ign/hero.jpg" width="1280" height="720" alt="Meccha Chameleon gameplay screenshot from IGN" loading="eager"',
        'src="images/ign-webp/hero.webp" width="960" height="540" alt="Meccha Chameleon gameplay screenshot from IGN" loading="lazy" decoding="async"',
    )

    # preview tiles + strip -> webp
    for name in [
        "hero",
        "shot-02",
        "shot-03",
        "shot-04",
        "shot-05",
        "shot-06",
        "shot-07",
        "shot-08",
        "shot-09",
        "shot-10",
    ]:
        text = text.replace(f"images/ign/{name}.jpg", f"images/ign-webp/{name}.webp")

    # width/height on strip imgs missing
    text = re.sub(
        r'(<div class="preview-tile"><img src="images/ign-webp/[^"]+" alt="[^"]*" loading="lazy")(>)',
        r'\1 width="640" height="400" decoding="async"\2',
        text,
    )
    text = re.sub(
        r'(<div class="ign-photo-strip">[\s\S]*?</div>)',
        lambda m: m.group(1)
        .replace('loading="lazy"', 'loading="lazy" decoding="async" width="400" height="400"'),
        text,
        count=1,
    )
    return text


def main() -> None:
    for path in sorted(ROOT.glob("*.html")):
        if path.name == "seo-setup.html":
            continue
        patch_file(path)


if __name__ == "__main__":
    main()
