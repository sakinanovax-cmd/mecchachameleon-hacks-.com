# -*- coding: utf-8 -*-
"""Replace hotlinked IGN URLs with local images/ign copies across the site."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

REMOTE_TO_LOCAL = {
    "images/ign/hero.jpg": "images/ign/hero.jpg",
    "images/ign/shot-02.jpg": "images/ign/shot-02.jpg",
    "images/ign/shot-03.jpg": "images/ign/shot-03.jpg",
    "images/ign/shot-04.jpg": "images/ign/shot-04.jpg",
    "images/ign/shot-05.jpg": "images/ign/shot-05.jpg",
    "images/ign/shot-06.jpg": "images/ign/shot-06.jpg",
    "images/ign/shot-07.jpg": "images/ign/shot-07.jpg",
    "images/ign/shot-08.jpg": "images/ign/shot-08.jpg",
    "images/ign/shot-09.jpg": "images/ign/shot-09.jpg",
    "images/ign/shot-10.jpg": "images/ign/shot-10.jpg",
}

LOCAL = [
    "images/ign/hero.jpg",
    "images/ign/shot-02.jpg",
    "images/ign/shot-03.jpg",
    "images/ign/shot-04.jpg",
    "images/ign/shot-05.jpg",
    "images/ign/shot-06.jpg",
    "images/ign/shot-07.jpg",
    "images/ign/shot-08.jpg",
    "images/ign/shot-09.jpg",
    "images/ign/shot-10.jpg",
]


def swap_remotes(text: str) -> str:
    for remote, local in REMOTE_TO_LOCAL.items():
        text = text.replace(remote, local)
    return text


def inject_article_image(html: str, img: str) -> str:
    if 'class="article-hero-img"' in html or "article-hero-img" in html:
        return html
    # insert after article-lead paragraph
    credit = (
        f'      <img class="article-hero-img" src="{img}" width="1280" height="720" '
        f'alt="Meccha Chameleon gameplay screenshot" loading="lazy">\n'
        f'      <p class="article-img-credit">Screenshot via '
        f'<a href="https://za.ign.com/meccha-chameleon/235012/meccha-chameleon-steam-screenshots" '
        f'rel="noopener noreferrer">IGN Meccha Chameleon gallery</a> '
        f"(image courtesy of lemorion_1224).</p>\n"
    )
    pattern = r'(<p class="article-lead">[\s\S]*?</p>\s*)'
    new_html, n = re.subn(pattern, r"\1" + credit, html, count=1)
    return new_html if n else html


def main():
    # 1) Replace remotes in all html + generator fragment
    for path in list(ROOT.glob("*.html")) + list((ROOT / "scripts").glob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".html", ".htmlfragment", ".py", ".json"}:
            continue
        text = path.read_text(encoding="utf-8")
        if "sm.ign.com" not in text and "IGN =" not in text:
            continue
        updated = swap_remotes(text)
        # update generator list if present
        if path.name == "generate_seo_blogs.py":
            updated = updated.replace(
                "IGN = [\n"
                + "\n".join(f'    "{u}",' for u in REMOTE_TO_LOCAL.keys())
                + "\n]",
                "IGN = [\n" + "\n".join(f'    "{u}",' for u in LOCAL) + "\n]",
            )
            # simpler: rewrite IGN block entirely
            updated = re.sub(
                r"IGN = \[[\s\S]*?\]",
                "IGN = [\n" + "".join(f'    "{u}",\n' for u in LOCAL) + "]",
                updated,
                count=1,
            )
        path.write_text(updated, encoding="utf-8")
        print("updated urls", path.name)

    # 2) Add hero images to product blogs that lack them
    product_blogs = [
        "blog-pixel-perfect-blend.html",
        "blog-auto-chameleon-paint.html",
        "blog-heat-vision-esp.html",
        "blog-instant-tag.html",
        "blog-super-speed-match-tools.html",
        "blog-stream-proof-overlay.html",
        "blog-cloud-dma-aws.html",
        "blog-hider-setup-guide.html",
        "blog-seeker-esp-setup-guide.html",
        "blog-cheat-comparison-2026.html",
        "guide.html",
    ]
    for i, name in enumerate(product_blogs):
        path = ROOT / name
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        html2 = inject_article_image(html, LOCAL[i % len(LOCAL)])
        if html2 != html:
            path.write_text(html2, encoding="utf-8")
            print("injected image", name)

    print("done")


if __name__ == "__main__":
    main()
