# -*- coding: utf-8 -*-
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
fragment = (root / "scripts" / "seo_blog_cards.htmlfragment").read_text(encoding="utf-8")
slugs = json.loads((root / "scripts" / "seo_blog_cards.json").read_text(encoding="utf-8"))["slugs"]

def card(cat, pill, pill_label, href, title, desc, date, label, img):
    return f"""
          <article class="blog-card" data-category="{cat}">
            <img class="blog-card-thumb" src="{img}" width="640" height="360" alt="Meccha Chameleon" loading="lazy">
            <div class="blog-card-body">
              <span class="pill {pill}">{pill_label}</span>
              <h2><a href="{href}">{title}</a></h2>
              <p>{desc}</p>
              <div class="blog-card-meta">
                <time datetime="{date}">{label}</time>
                <a href="{href}">Read Article →</a>
              </div>
            </div>
          </article>
"""

imgs = [
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

existing = "".join(
    [
        card("hider", "pill-hider", "Hider", "blog-pixel-perfect-blend.html", "Pixel-Perfect Blend in Meccha Chameleon Cheats Explained", "How Pixel-Perfect Blend locks hider camouflage to stage colors so seekers walk past painted props.", "2026-07-12", "Jul 12, 2026", imgs[0]),
        card("hider", "pill-hider", "Hider", "blog-auto-chameleon-paint.html", "Auto-Chameleon Paint Explained — Environment Color Match", "Automatic environment color matching for faster Meccha Chameleon camouflage setups every round.", "2026-07-14", "Jul 14, 2026", imgs[1]),
        card("esp", "pill-esp", "ESP", "blog-heat-vision-esp.html", "Heat Vision / ESP in Meccha Chameleon Cheats Explained", "Seeker wall vision and hider minimap tracking — the core ESP stack for Meccha Chameleon hunts.", "2026-07-16", "Jul 16, 2026", imgs[2]),
        card("combat", "pill-combat", "Combat", "blog-instant-tag.html", "Instant Tag &amp; One-Hit Tag Through Obstacles Explained", "How Instant Tag and one-hit tag through obstacles help seekers close Meccha Chameleon rounds.", "2026-07-18", "Jul 18, 2026", imgs[3]),
        card("combat", "pill-combat", "Combat", "blog-super-speed-match-tools.html", "Super Speed, Timer Freeze &amp; Free Camera Match Tools", "Super Speed (1–5×), Match Timer Freeze, Full-Map Reveal, and Free Camera / Noclip explained.", "2026-07-20", "Jul 20, 2026", imgs[4]),
        card("safety", "pill-safety", "Safety", "blog-stream-proof-overlay.html", "Stream-Proof Overlay for Meccha Chameleon Cheats", "Keep menus invisible to OBS and Discord while you stream Meccha Chameleon hide and seek.", "2026-07-22", "Jul 22, 2026", imgs[5]),
        card("safety", "pill-safety", "Safety", "blog-cloud-dma-aws.html", "How Cloud DMA on AWS Works for Meccha Chameleon", "Cloud DMA hosted on AWS — what it is, how it fits the suite, and when players enable it.", "2026-07-24", "Jul 24, 2026", imgs[6]),
        card("hider", "pill-hider", "Hider", "blog-hider-setup-guide.html", "Hider Setup Guide — Camo, Pose Lock &amp; Stamina", "Practical Meccha Chameleon hider settings for Pixel-Perfect Blend, Perfect Disguise, and pose tools.", "2026-07-26", "Jul 26, 2026", imgs[7]),
        card("esp", "pill-esp", "ESP", "blog-seeker-esp-setup-guide.html", "Seeker ESP Setup Guide — Heat Vision, Minimap &amp; Tag", "Configure Heat Vision / ESP, minimap tracking, and Instant Tag for cleaner seeker rounds.", "2026-07-28", "Jul 28, 2026", imgs[8]),
        card("comparison", "pill-comparison", "Comparison", "blog-cheat-comparison-2026.html", "Best Meccha Chameleon Cheat Review &amp; Comparison 2026", "Paid suite vs free leaks — update speed, feature depth, stream-proof, support, and price.", "2026-08-01", "Aug 1, 2026", imgs[9]),
    ]
)


html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meccha Chameleon Cheat Blog — Guides, ESP &amp; Tips</title>
  <meta name="description" content="40+ Meccha Chameleon guides and cheat explainers — gameplay tips, Steam help, camouflage, ESP, and links to mecchahacks.com tools.">
  <link rel="canonical" href="https://mecchahacks.com/blog">
  <meta name="robots" content="index, follow">
  <meta property="og:title" content="Meccha Chameleon Cheat Blog — Guides, ESP &amp; Tips">
  <meta property="og:description" content="Guides and comparisons for Meccha Chameleon — gameplay, camouflage, ESP, and safety.">
  <meta property="og:url" content="https://mecchahacks.com/blog">
  <link rel="icon" href="https://zadeyo.com/_next/image?url=%2Frt-removebg-preview.png&amp;w=64&amp;q=75" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/global.css">
  <link rel="stylesheet" href="css/blog.css">
</head>
<body>
  <header class="navbar">
    <div class="container nav-inner">
      <a class="brand" href="index.html">
        <img src="https://zadeyo.com/_next/image?url=%2Frt-removebg-preview.png&amp;w=64&amp;q=75" width="36" height="36" alt="Meccha Chameleon Cheats">
        <span>Meccha Chameleon Cheats</span>
      </a>
      <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav-links" aria-label="Primary">
        <a href="index.html">Home</a>
        <a href="meccha-chameleon-cheats.html">Buy</a>
        <a href="blog.html" class="active">Blog</a>
        <a href="guide.html">Guide</a>
        <a class="nav-cta" href="https://zadeyo.com/go/SAKINA?to=%2Fproducts%2Fmeccha-chameleon-cheats" rel="noopener noreferrer">Buy Cheats</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="page-hero">
      <div class="container">
        <h1>Meccha Chameleon Blog — Guides, Tips &amp; Cheat Explainers</h1>
        <p>Easy guides for Meccha Chameleon gameplay, Steam, camouflage, and tools. Keyword pages that link back to <a href="https://mecchahacks.com/">mecchahacks.com</a>.</p>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="container">
        <div class="blog-filters" role="toolbar" aria-label="Filter articles">
          <button type="button" class="filter-btn active" data-filter="all" aria-pressed="true">All</button>
          <button type="button" class="filter-btn" data-filter="guides" aria-pressed="false">Guides</button>
          <button type="button" class="filter-btn" data-filter="comparison" aria-pressed="false">Comparison</button>
          <button type="button" class="filter-btn" data-filter="esp" aria-pressed="false">ESP</button>
          <button type="button" class="filter-btn" data-filter="combat" aria-pressed="false">Combat</button>
          <button type="button" class="filter-btn" data-filter="hider" aria-pressed="false">Hider</button>
          <button type="button" class="filter-btn" data-filter="safety" aria-pressed="false">Safety</button>
        </div>

        <div class="blog-grid">
{fragment}
{existing}
        </div>

        <div class="cta-banner mt-3">
          <h2>Ready to Use These Tools In-Game?</h2>
          <p>Full feature access on Monthly ($35) and Lifetime ($150) plans.</p>
          <a class="btn btn-primary btn-lg" href="https://zadeyo.com/go/SAKINA?to=%2Fproducts%2Fmeccha-chameleon-cheats" rel="noopener noreferrer">Buy Meccha Chameleon Cheats</a>
          <p class="redirect-note">You may be redirected to complete checkout.</p>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">
            <img src="https://zadeyo.com/_next/image?url=%2Frt-removebg-preview.png&amp;w=64&amp;q=75" width="32" height="32" alt="Meccha Chameleon Cheats">
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
            <a href="https://zadeyo.com/go/SAKINA?to=%2Fproducts%2Fmeccha-chameleon-cheats" rel="noopener noreferrer">Purchase</a>
            <a href="meccha-chameleon-cheats.html#pricing">Pricing</a>
            <a href="meccha-chameleon-cheats.html#features">Features</a>
          </div>
        </div>
        <div>
          <h4>Support</h4>
          <div class="footer-links">
            <a href="https://zadeyo.com/support" rel="noopener noreferrer">Support Channel</a>
            <a href="blog-hider-setup-guide.html">Hider Setup</a>
            <a href="blog-seeker-esp-setup-guide.html">Seeker Setup</a>
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

(root / "blog.html").write_text(html, encoding="utf-8")

core = [
    ("https://mecchahacks.com/", "weekly", "1.0"),
    ("https://mecchahacks.com/meccha-chameleon-cheats", "weekly", "0.95"),
    ("https://mecchahacks.com/blog", "weekly", "0.9"),
    ("https://mecchahacks.com/guide", "monthly", "0.85"),
]
product = [
    "blog-pixel-perfect-blend",
    "blog-auto-chameleon-paint",
    "blog-heat-vision-esp",
    "blog-instant-tag",
    "blog-super-speed-match-tools",
    "blog-stream-proof-overlay",
    "blog-cloud-dma-aws",
    "blog-hider-setup-guide",
    "blog-seeker-esp-setup-guide",
    "blog-cheat-comparison-2026",
]
urls = (
    core
    + [(f"https://mecchahacks.com/{s}", "monthly", "0.75") for s in slugs]
    + [(f"https://mecchahacks.com/{s}", "monthly", "0.7") for s in product]
)
parts = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
]
for loc, freq, pri in urls:
    parts.extend(
        [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{pri}</priority>",
            "  </url>",
        ]
    )
parts.append("</urlset>")
(root / "sitemap.xml").write_text("\n".join(parts) + "\n", encoding="utf-8")
print("ok", "seo", len(slugs), "sitemap", len(urls))
