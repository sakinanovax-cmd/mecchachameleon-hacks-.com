# -*- coding: utf-8 -*-
"""Add the 4 long-tail keyword blogs missing from the approved list."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
LOGO = "https://zadeyo.com/_next/image?url=%2Frt-removebg-preview.png&w=64&q=75"
BUY = "https://mecchahacks.com/meccha-chameleon-cheats"
PURCHASE = "https://zadeyo.com/go/SAKINA?to=%2Fproducts%2Fmeccha-chameleon-cheats"
SUPPORT = "https://zadeyo.com/support"
IGN = [
    "images/ign-webp/hero.webp",
    "images/ign-webp/shot-02.webp",
    "images/ign-webp/shot-03.webp",
    "images/ign-webp/shot-04.webp",
    "images/ign-webp/shot-05.webp",
    "images/ign-webp/shot-06.webp",
    "images/ign-webp/shot-07.webp",
    "images/ign-webp/shot-08.webp",
    "images/ign-webp/shot-09.webp",
    "images/ign-webp/shot-10.webp",
]

POSTS = [
    {
        "slug": "blog-meccha-chameleon-painting-multiplayer",
        "title": "Meccha Chameleon Painting Multiplayer — Friend Night Rules That Work",
        "meta_title": "Meccha Chameleon Painting Multiplayer",
        "meta_desc": "Host cleaner Meccha Chameleon painting multiplayer nights with simple map rules, role swaps, and paint-focused rounds.",
        "h1": "Meccha Chameleon Painting Multiplayer — Friend Night Rules That Work",
        "lead": "Meccha Chameleon painting multiplayer is peak fun when the lobby has light rules. Without them, everyone argues about Workshop downloads.",
        "kw": "Meccha Chameleon painting multiplayer",
        "date": "2026-07-31",
        "label": "Jul 31, 2026",
        "body": """
        <h2>House rules that keep paint nights fun</h2>
        <ul>
          <li>Two default maps, then one Workshop map</li>
          <li>Swap hider and seeker every round</li>
          <li>No void-hide maps unless everyone votes yes</li>
          <li>Short break after a heated round</li>
        </ul>
        <h2>Host checklist</h2>
        <p>Share the map list in chat. Wait for Workshop subscribes. Start when the last friend finishes download.</p>
        <h2>Optional tool presets</h2>
        <p>If your group uses tools, save separate hider and seeker configs. Feature names stay consistent on the <a href="{BUY}">Meccha Chameleon cheats page</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-hide-and-seek-online",
        "title": "Meccha Chameleon Hide and Seek Online — Public Lobby Survival",
        "meta_title": "Meccha Chameleon Hide and Seek Online",
        "meta_desc": "Survive Meccha Chameleon hide and seek online with cleaner habits, safer Workshop use, and smarter public lobby play.",
        "h1": "Meccha Chameleon Hide and Seek Online — Public Lobby Survival",
        "lead": "Meccha Chameleon hide and seek online is messy in the best and worst ways. Here is how to enjoy public queues without rage-quitting every third map.",
        "kw": "Meccha Chameleon hide and seek online",
        "date": "2026-07-29",
        "label": "Jul 29, 2026",
        "body": """
        <h2>Public lobby rules of thumb</h2>
        <ul>
          <li>Leave toxic hosts fast</li>
          <li>Do not trust unknown Workshop packs blindly</li>
          <li>Mute early if voice chat is useless</li>
          <li>Finish paint before you freeze — half-painted players get tagged first</li>
        </ul>
        <h2>Skill vs tools</h2>
        <p>Manual skill still matters. Tools change the ceiling. Compare options in our <a href="blog-cheat-comparison-2026.html">2026 comparison</a>, then open <a href="{BUY}">Meccha Chameleon cheats</a> for the full suite.</p>
        <h2>Safety note</h2>
        <p>No kernel anti-cheat does not mean zero risk. Reports still happen. Read the <a href="guide.html">anti-cheat guide</a> before long public sessions.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-artistic-skill-game",
        "title": "Meccha Chameleon Artistic Skill Game — Do You Need to Draw Well?",
        "meta_title": "Meccha Chameleon Artistic Skill Game",
        "meta_desc": "Is Meccha Chameleon an artistic skill game? How much drawing talent you need and how to win without being a painter.",
        "h1": "Meccha Chameleon Artistic Skill Game — Do You Need to Draw Well?",
        "lead": "People call Meccha Chameleon an artistic skill game. True — but you do not need museum talent to survive a lobby.",
        "kw": "Meccha Chameleon artistic skill game",
        "date": "2026-07-30",
        "label": "Jul 30, 2026",
        "body": """
        <h2>What “artistic” means here</h2>
        <p>It means color judgment and shape breaking under pressure. Not oil painting. Not anatomy class.</p>
        <h2>If you are bad at art</h2>
        <p>Use bigger props. Copy chunky colors. Freeze sooner. Pick noisier walls. Technique beats talent for most rounds.</p>
        <h2>Assists for consistency</h2>
        <p>Auto-Chameleon Paint and Pixel-Perfect Blend help consistency. See <a href="blog-pixel-perfect-blend.html">Pixel-Perfect Blend</a> and the <a href="{BUY}">cheats feature list</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-chameleon-painting-simulator",
        "title": "Meccha Chameleon Painting Simulator Feel — Practice Without Wasting Lobbies",
        "meta_title": "Meccha Chameleon Painting Simulator Tips",
        "meta_desc": "Treat Meccha Chameleon like a chameleon painting simulator in private lobbies to practice blends before public queues.",
        "h1": "Meccha Chameleon Painting Simulator Feel — Practice Without Wasting Lobbies",
        "lead": "Think of private rounds as a Meccha Chameleon chameleon painting simulator. No audience. No ego. Just reps.",
        "kw": "Meccha Chameleon chameleon painting simulator",
        "date": "2026-08-02",
        "label": "Aug 2, 2026",
        "body": """
        <h2>Private practice routine</h2>
        <ol>
          <li>Load a quiet map with a friend</li>
          <li>Paint three spots in five minutes</li>
          <li>Have a friend seek for two minutes</li>
          <li>Note which blends failed and why</li>
        </ol>
        <h2>What to measure</h2>
        <p>Time to freeze. Edge quality. Whether your pose looks human. That feedback loop beats random public deaths.</p>
        <h2>When to add tools</h2>
        <p>After you understand manual paint, try assists from <a href="{BUY}">mecchahacks.com/meccha-chameleon-cheats</a>. Setup walkthroughs are on the <a href="blog-hider-setup-guide.html">hider guide</a>.</p>
        """,
    },
]


def page(post: dict, i: int) -> str:
    img = IGN[i % len(IGN)]
    body = post["body"].format(BUY=BUY)
    gal = "".join(
        f'<img src="{IGN[(i + n) % len(IGN)]}" alt="Meccha Chameleon screenshot" loading="lazy" width="640" height="400">'
        for n in range(4)
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{post["meta_title"]}</title>
  <meta name="description" content="{post["meta_desc"]}">
  <link rel="canonical" href="https://mecchahacks.com/{post["slug"]}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="icon" href="{LOGO}" type="image/png">
  <link rel="preload" href="fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/inter-700.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="css/fonts.css">
  <link rel="stylesheet" href="css/global.css">
  <link rel="stylesheet" href="css/blog.css">
  <meta name="author" content="Meccha Chameleon Cheats">
  <meta property="og:site_name" content="Meccha Chameleon Cheats">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{post["meta_title"]}">
  <meta property="og:description" content="{post["meta_desc"]}">
  <meta property="og:url" content="https://mecchahacks.com/{post["slug"]}">
  <meta property="og:image" content="https://mecchahacks.com/{img}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{post["meta_title"]}">
  <meta name="twitter:description" content="{post["meta_desc"]}">
  <meta name="twitter:image" content="https://mecchahacks.com/{img}">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{post["h1"]}",
    "description": "{post["meta_desc"]}",
    "image": ["https://mecchahacks.com/{img}"],
    "author": {{"@type": "Organization", "name": "Meccha Chameleon Cheats"}},
    "publisher": {{"@type": "Organization", "name": "Meccha Chameleon Cheats", "logo": {{"@type": "ImageObject", "url": "{LOGO}"}}}},
    "datePublished": "{post["date"]}",
    "dateModified": "{post["date"]}",
    "mainEntityOfPage": "https://mecchahacks.com/{post["slug"]}"
  }}
  </script>
</head>
<body>
  <header class="navbar">
    <div class="container nav-inner">
      <a class="brand" href="index.html">
        <img src="{LOGO}" width="36" height="36" alt="Meccha Chameleon Cheats">
        <span>Meccha Chameleon Cheats</span>
      </a>
      <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
      <nav class="nav-links" aria-label="Primary">
        <a href="index.html">Home</a>
        <a href="meccha-chameleon-cheats.html">Buy</a>
        <a href="blog.html" class="active">Blog</a>
        <a href="guide.html">Guide</a>
        <a class="nav-cta" href="{PURCHASE}" rel="noopener noreferrer">Buy Cheats</a>
      </nav>
    </div>
  </header>
  <main>
    <article class="container article-wrap">
      <div class="article-meta">
        <span class="pill pill-guides">Guides</span>
        <time datetime="{post["date"]}">{post["label"]}</time>
      </div>
      <h1>{post["h1"]}</h1>
      <p class="article-lead">{post["lead"]}</p>
      <img class="article-hero-img" src="{img}" width="960" height="540" alt="{post["kw"]}" loading="lazy">
      <p class="article-img-credit">Screenshot via <a href="https://za.ign.com/meccha-chameleon/235012/meccha-chameleon-steam-screenshots" rel="noopener noreferrer">IGN Meccha Chameleon gallery</a> (courtesy of lemorion_1224).</p>
      <div class="prose">
{body}
        <figure class="inline-shot"><img src="{IGN[(i+2)%len(IGN)]}" alt="Meccha Chameleon gameplay" loading="lazy" width="960" height="540"><figcaption>Meccha Chameleon gameplay (IGN)</figcaption></figure>
      </div>
      <div class="article-gallery">
        <h2>More Meccha Chameleon Screenshots</h2>
        <div class="article-gallery-grid">{gal}</div>
      </div>
      <div class="article-cta">
        <h2>Get the full tool suite</h2>
        <p>Hider camo, Heat Vision ESP, Instant Tag, Stream-Proof, Cloud DMA on AWS.</p>
        <a class="btn btn-primary" href="{PURCHASE}" rel="noopener noreferrer">Buy Meccha Chameleon Cheats</a>
        <p class="redirect-note">You may be redirected to complete checkout.</p>
        <p class="mt-2"><a href="{BUY}">View features and pricing</a></p>
      </div>
      <div class="related-links">
        <h2>Keep Reading</h2>
        <ul>
          <li><a href="blog-meccha-chameleon-tips.html">Meccha Chameleon tips</a></li>
          <li><a href="blog-meccha-chameleon-painting-techniques.html">Painting techniques</a></li>
          <li><a href="{BUY}">Buy page</a></li>
          <li><a href="guide.html">Anti-cheat guide</a></li>
        </ul>
      </div>
    </article>
  </main>
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">
            <img src="{LOGO}" width="32" height="32" alt="Meccha Chameleon Cheats">
            Meccha Chameleon Cheats
          </div>
          <p>Premium Meccha Chameleon cheats for hider camouflage, seeker ESP, and match control.</p>
        </div>
        <div>
          <h4>Site</h4>
          <div class="footer-links">
            <a href="index.html">Home</a>
            <a href="meccha-chameleon-cheats.html">Buy</a>
            <a href="blog.html">Blog</a>
            <a href="guide.html">Guide</a>
          </div>
        </div>
        <div>
          <h4>Store</h4>
          <div class="footer-links">
            <a href="{PURCHASE}" rel="noopener noreferrer">Purchase</a>
            <a href="meccha-chameleon-cheats.html#pricing">Pricing</a>
          </div>
        </div>
        <div>
          <h4>Support</h4>
          <div class="footer-links">
            <a href="{SUPPORT}" rel="noopener noreferrer">Support</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer">Disclaimer: This site provides information about third-party game software tools. Use is at your own risk and subject to the game’s terms of service. Not affiliated with Meccha Chameleon, Steam, IGN, or the game developers.</p>
        <p>© 2026 mecchahacks.com</p>
      </div>
    </div>
  </footer>
  <script src="js/main.js" defer></script>
</body>
</html>
"""


def card(post: dict, i: int) -> str:
    img = IGN[i % len(IGN)]
    return f"""
          <article class="blog-card" data-category="guides">
            <img class="blog-card-thumb" src="{img}" width="640" height="360" alt="{post["kw"]}" loading="lazy">
            <div class="blog-card-body">
              <span class="pill pill-guides">Guides</span>
              <h2><a href="{post["slug"]}.html">{post["title"]}</a></h2>
              <p>{post["meta_desc"]}</p>
              <div class="blog-card-meta">
                <time datetime="{post["date"]}">{post["label"]}</time>
                <a href="{post["slug"]}.html">Read Article →</a>
              </div>
            </div>
          </article>
"""


def main() -> None:
    cards = []
    for i, post in enumerate(POSTS):
        (ROOT / f"{post['slug']}.html").write_text(page(post, i), encoding="utf-8")
        cards.append(card(post, i))
        print("wrote", post["slug"])

    blog = ROOT / "blog.html"
    html = blog.read_text(encoding="utf-8")
    # insert cards after opening blog-grid
    if "blog-meccha-chameleon-painting-multiplayer.html" not in html:
        html = html.replace(
            '<div class="blog-grid">',
            '<div class="blog-grid">\n' + "\n".join(cards),
            1,
        )
    # filters per brief
    html = re.sub(
        r'<div class="blog-filters"[\s\S]*?</div>',
        """<div class="blog-filters" role="toolbar" aria-label="Filter articles">
          <button type="button" class="filter-btn active" data-filter="all" aria-pressed="true">All</button>
          <button type="button" class="filter-btn" data-filter="comparison" aria-pressed="false">Comparison</button>
          <button type="button" class="filter-btn" data-filter="esp" aria-pressed="false">ESP</button>
          <button type="button" class="filter-btn" data-filter="combat" aria-pressed="false">Combat</button>
          <button type="button" class="filter-btn" data-filter="spoofing" aria-pressed="false">Spoofing</button>
          <button type="button" class="filter-btn" data-filter="safety" aria-pressed="false">Safety</button>
          <button type="button" class="filter-btn" data-filter="guides" aria-pressed="false">Guides</button>
          <button type="button" class="filter-btn" data-filter="hider" aria-pressed="false">Hider</button>
        </div>""",
        html,
        count=1,
    )
    # tag cloud dma as spoofing for filter
    html = html.replace(
        'data-category="safety">\n            <img class="blog-card-thumb" src="images/ign/shot-07.jpg"',
        'data-category="spoofing">\n            <img class="blog-card-thumb" src="images/ign-webp/shot-07.webp"',
    )
    # also match webp version cards for cloud dma
    html = re.sub(
        r'(href="blog-cloud-dma-aws\.html"[\s\S]{0,200}?data-category=")safety(")',
        r"\1spoofing\2",
        html,
        count=0,
    )
    # simpler: replace card category for cloud dma article block
    html = html.replace(
        '<article class="blog-card" data-category="safety">\n            <img class="blog-card-thumb" src="images/ign-webp/shot-07.webp"',
        '<article class="blog-card" data-category="spoofing">\n            <img class="blog-card-thumb" src="images/ign-webp/shot-07.webp"',
    )
    html = html.replace(
        '<article class="blog-card" data-category="safety">\n            <span class="pill pill-safety">Safety</span>\n            <h2><a href="blog-cloud-dma-aws.html">',
        '<article class="blog-card" data-category="spoofing">\n            <span class="pill pill-safety">Spoofing</span>\n            <h2><a href="blog-cloud-dma-aws.html">',
    )
    blog.write_text(html, encoding="utf-8")

    # sitemap append
    sm = ROOT / "sitemap.xml"
    s = sm.read_text(encoding="utf-8")
    for post in POSTS:
        loc = f"https://mecchahacks.com/{post['slug']}"
        if loc not in s:
            entry = f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{post["date"]}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.75</priority>
  </url>
"""
            s = s.replace("</urlset>", entry + "</urlset>")
    sm.write_text(s, encoding="utf-8")
    print("blog+sitemap updated")


if __name__ == "__main__":
    main()
