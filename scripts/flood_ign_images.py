# -*- coding: utf-8 -*-
"""Put IGN Meccha Chameleon screenshots throughout every blog and key pages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
IMGS = [
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
CREDIT = (
    '<p class="article-img-credit">Screenshots via '
    '<a href="https://za.ign.com/meccha-chameleon/235012/meccha-chameleon-steam-screenshots" '
    'rel="noopener noreferrer">IGN Meccha Chameleon gallery</a> '
    "(courtesy of lemorion_1224).</p>"
)


def figure(src: str, alt: str, caption: str = "Meccha Chameleon — IGN screenshot") -> str:
    return (
        f'<figure class="inline-shot">'
        f'<img src="{src}" width="1280" height="720" alt="{alt}" loading="lazy">'
        f"<figcaption>{caption}</figcaption>"
        f"</figure>\n"
    )


def gallery(start: int) -> str:
    picks = [IMGS[(start + i) % len(IMGS)] for i in range(4)]
    tiles = "\n".join(
        f'          <img src="{src}" alt="Meccha Chameleon IGN screenshot {i+1}" loading="lazy">'
        for i, src in enumerate(picks)
    )
    return (
        '<div class="article-gallery">\n'
        "        <h2>More Meccha Chameleon Screenshots</h2>\n"
        f"        {CREDIT}\n"
        '        <div class="article-gallery-grid">\n'
        f"{tiles}\n"
        "        </div>\n"
        "      </div>\n"
    )


def enrich_prose(prose_inner: str, seed: int, title: str) -> str:
    # Remove previously injected inline shots / galleries to allow re-run
    prose_inner = re.sub(r"<figure class=\"inline-shot\">[\s\S]*?</figure>\s*", "", prose_inner)
    parts = re.split(r"(<h2[\s\S]*?</h2>)", prose_inner)
    out = []
    img_i = seed
    h2_count = 0
    for part in parts:
        out.append(part)
        if part.startswith("<h2"):
            h2_count += 1
            # After 1st, 2nd, 3rd+ H2 blocks place an image before next content
            # Actually place image AFTER the h2 heading content that follows - we append after h2 tag
            if h2_count >= 1:
                src = IMGS[img_i % len(IMGS)]
                img_i += 1
                out.append(
                    figure(
                        src,
                        f"{title} — Meccha Chameleon screenshot",
                        "Meccha Chameleon gameplay (IGN / lemorion_1224)",
                    )
                )
    # If fewer than 2 images injected, force mid-content images after paragraphs
    text = "".join(out)
    if text.count("inline-shot") < 2:
        paras = list(re.finditer(r"</p>", text))
        insert_at = []
        if len(paras) >= 2:
            insert_at.append(paras[min(1, len(paras) - 1)].end())
        if len(paras) >= 4:
            insert_at.append(paras[min(3, len(paras) - 1)].end())
        offset = 0
        for idx, pos in enumerate(insert_at):
            src = IMGS[(seed + idx + 3) % len(IMGS)]
            chunk = "\n" + figure(src, f"{title} — Meccha Chameleon", "Meccha Chameleon (IGN)")
            pos2 = pos + offset
            text = text[:pos2] + chunk + text[pos2:]
            offset += len(chunk)
    return text


def ensure_hero(html: str, seed: int, title: str) -> str:
    hero = IMGS[seed % len(IMGS)]
    if 'class="article-hero-img"' not in html:
        credit = (
            f'      <img class="article-hero-img" src="{hero}" width="1280" height="720" '
            f'alt="{title} — Meccha Chameleon screenshot" loading="lazy">\n'
            f"      {CREDIT}\n"
        )
        html = re.sub(
            r'(<p class="article-lead">[\s\S]*?</p>\s*)',
            r"\1" + credit,
            html,
            count=1,
        )
    else:
        html = re.sub(
            r'(<img class="article-hero-img" src=")[^"]+(")',
            rf"\1{hero}\2",
            html,
            count=1,
        )
    # og:image absolute-ish local path
    if 'property="og:image"' in html:
        html = re.sub(
            r'(property="og:image" content=")[^"]+(")',
            rf"\1https://mecchahacks.com/{hero}\2",
            html,
            count=1,
        )
    else:
        html = html.replace(
            "</title>",
            f'</title>\n  <meta property="og:image" content="https://mecchahacks.com/{hero}">',
            1,
        )
    return html


def process_article(path: Path, seed: int) -> None:
    html = path.read_text(encoding="utf-8")
    title_m = re.search(r"<h1>(.*?)</h1>", html, re.S)
    title = re.sub(r"<[^>]+>", "", title_m.group(1)).strip() if title_m else "Meccha Chameleon"
    html = ensure_hero(html, seed, title)

    # enrich prose
    m = re.search(r'(<div class="prose">)([\s\S]*?)(</div>\s*<div class="article-cta">)', html)
    if not m:
        m = re.search(r'(<div class="prose">)([\s\S]*?)(</div>\s*<div class="related-links">)', html)
    if m:
        inner = enrich_prose(m.group(2), seed, title)
        html = html[: m.start()] + m.group(1) + inner + m.group(3) + html[m.end() :]

    # gallery before CTA / related
    html = re.sub(r'<div class="article-gallery">[\s\S]*?</div>\s*', "", html)
    gal = gallery(seed + 2)
    if 'class="article-cta"' in html:
        html = html.replace('<div class="article-cta">', gal + '      <div class="article-cta">', 1)
    elif 'class="related-links"' in html:
        html = html.replace('<div class="related-links">', gal + '      <div class="related-links">', 1)
    else:
        html = html.replace("</article>", gal + "    </article>", 1)

    path.write_text(html, encoding="utf-8")
    print("enriched", path.name)


def enrich_home_buy() -> None:
    # Home: add image strip section if missing
    home = ROOT / "index.html"
    h = home.read_text(encoding="utf-8")
    if "ign-photo-strip" not in h:
        strip = """
    <section class="section" id="screens">
      <div class="container">
        <div class="section-head">
          <span class="section-label">Screenshots</span>
          <h2>Meccha Chameleon In-Game Shots</h2>
          <p>Official-style Steam screenshots featured via the IGN gallery.</p>
        </div>
        <div class="ign-photo-strip">
""" + "\n".join(
            f'          <img src="{src}" alt="Meccha Chameleon screenshot" loading="lazy">'
            for src in IMGS
        ) + """
        </div>
        <p class="text-center mt-2" style="color:var(--text-dim);font-size:0.8rem">Via <a href="https://za.ign.com/meccha-chameleon/235012/meccha-chameleon-steam-screenshots" rel="noopener noreferrer">IGN Meccha Chameleon screenshots</a>.</p>
      </div>
    </section>
"""
        h = h.replace('<section class="section" id="why">', strip + '\n    <section class="section" id="why">', 1)
        home.write_text(h, encoding="utf-8")
        print("home strip added")

    buy = ROOT / "meccha-chameleon-cheats.html"
    b = buy.read_text(encoding="utf-8")
    if "ign-photo-strip" not in b:
        strip = """
        <div class="ign-photo-strip mt-3">
""" + "\n".join(
            f'          <img src="{src}" alt="Meccha Chameleon" loading="lazy">' for src in IMGS[:8]
        ) + """
        </div>
"""
        b = b.replace(
            '<section class="section" id="faq">',
            f'<section class="section section-alt" id="more-shots"><div class="container"><div class="section-head"><span class="section-label">Gallery</span><h2>More Meccha Chameleon Screenshots</h2></div>{strip}</div></section>\n\n    <section class="section" id="faq">',
            1,
        )
        buy.write_text(b, encoding="utf-8")
        print("buy gallery added")


def main():
    articles = sorted(ROOT.glob("blog-*.html"))
    if (ROOT / "guide.html").exists():
        articles.append(ROOT / "guide.html")
    for i, path in enumerate(articles):
        process_article(path, i)
    enrich_home_buy()
    print("total articles", len(articles))


if __name__ == "__main__":
    main()
