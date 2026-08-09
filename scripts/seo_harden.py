# -*- coding: utf-8 -*-
"""Make all pages SEO-complete: social meta, schemas, sitemap, robots helpers."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "https://mecchahacks.com"
TODAY = date.today().isoformat()
DEFAULT_OG = f"{DOMAIN}/images/hero-bg.jpg"
LOGO = "https://zadeyo.com/_next/image?url=%2Frt-removebg-preview.png&w=64&q=75"


def text_between(html: str, start: str, end: str) -> str:
    m = re.search(re.escape(start) + r"(.*?)" + re.escape(end), html, re.S | re.I)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    return (
        s.replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
        .strip()
    )


def get_meta(html: str, name: str) -> str:
    m = re.search(
        rf'<meta[^>]+(?:name|property)=["\']{re.escape(name)}["\'][^>]+content=["\']([^"\']+)["\']',
        html,
        re.I,
    )
    if m:
        return m.group(1)
    m = re.search(
        rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:name|property)=["\']{re.escape(name)}["\']',
        html,
        re.I,
    )
    return m.group(1) if m else ""


def get_canonical(html: str) -> str:
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', html, re.I)
    if m:
        return m.group(1)
    m = re.search(r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']', html, re.I)
    return m.group(1) if m else ""


def get_title(html: str) -> str:
    return strip_tags(text_between(html, "<title>", "</title>"))


def get_h1(html: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    return strip_tags(m.group(1)) if m else ""


def get_og_image(html: str, slug_hint: str = "") -> str:
    img = get_meta(html, "og:image")
    if img:
        if img.startswith("http"):
            return img
        return f"{DOMAIN}/{img.lstrip('/')}"
    m = re.search(r'class="article-hero-img"[^>]+src=["\']([^"\']+)["\']', html)
    if m:
        src = m.group(1)
        return src if src.startswith("http") else f"{DOMAIN}/{src.lstrip('/')}"
    m = re.search(r'src=["\'](images/ign/[^"\']+)["\']', html)
    if m:
        return f"{DOMAIN}/{m.group(1)}"
    return DEFAULT_OG


def remove_blocks(html: str) -> str:
    # Remove prior injected SEO bundles to allow reruns
    html = re.sub(
        r"\n?\s*<!-- SEO-HARDEN:START -->[\s\S]*?<!-- SEO-HARDEN:END -->\s*",
        "\n",
        html,
    )
    return html


def page_kind(path: Path) -> str:
    name = path.name
    if name == "index.html":
        return "home"
    if name == "meccha-chameleon-cheats.html":
        return "product"
    if name == "blog.html":
        return "blogindex"
    if name == "guide.html":
        return "guide"
    if name.startswith("blog-"):
        return "article"
    return "page"


def breadcrumb(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": url,
            }
            for i, (name, url) in enumerate(items)
        ],
    }


def schemas_for(path: Path, html: str) -> list[dict]:
    kind = page_kind(path)
    title = get_title(html) or "Meccha Chameleon Cheats"
    desc = get_meta(html, "description") or title
    canonical = get_canonical(html) or f"{DOMAIN}/"
    og_image = get_og_image(html)
    h1 = get_h1(html) or title
    schemas: list[dict] = []

    if kind == "home":
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": "Meccha Chameleon Cheats",
                "alternateName": "Meccha Chameleon Cheats",
                "url": f"{DOMAIN}/",
                "description": desc,
                "inLanguage": "en",
            }
        )
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "Organization",
                "name": "Meccha Chameleon Cheats",
                "url": f"{DOMAIN}/",
                "logo": LOGO,
                "description": "Meccha Chameleon cheats, guides, and lobby tools for PC players.",
                "sameAs": [],
            }
        )
        schemas.append(
            breadcrumb([("Home", f"{DOMAIN}/")])
        )

    if kind == "product":
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "Product",
                "name": "Meccha Chameleon Cheats",
                "description": desc,
                "image": [og_image, f"{DOMAIN}/images/hero-bg.jpg"],
                "brand": {"@type": "Brand", "name": "Meccha Chameleon Cheats"},
                "category": "PC Game Software",
                "offers": [
                    {
                        "@type": "Offer",
                        "name": "Monthly",
                        "price": "35.00",
                        "priceCurrency": "USD",
                        "availability": "https://schema.org/InStock",
                        "url": canonical,
                        "priceValidUntil": f"{date.today().year}-12-31",
                    },
                    {
                        "@type": "Offer",
                        "name": "Lifetime",
                        "price": "150.00",
                        "priceCurrency": "USD",
                        "availability": "https://schema.org/InStock",
                        "url": canonical,
                        "priceValidUntil": f"{date.today().year}-12-31",
                    },
                ],
            }
        )
        schemas.append(
            breadcrumb(
                [
                    ("Home", f"{DOMAIN}/"),
                    ("Meccha Chameleon Cheats", canonical),
                ]
            )
        )

    if kind == "blogindex":
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "Blog",
                "name": "Meccha Chameleon Blog",
                "url": canonical,
                "description": desc,
                "publisher": {"@type": "Organization", "name": "Meccha Chameleon Cheats", "logo": {"@type": "ImageObject", "url": LOGO}},
            }
        )
        schemas.append(
            breadcrumb([("Home", f"{DOMAIN}/"), ("Blog", canonical)])
        )

    if kind == "guide":
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "TechArticle",
                "headline": h1,
                "description": desc,
                "image": [og_image],
                "author": {"@type": "Organization", "name": "Meccha Chameleon Cheats"},
                "publisher": {
                    "@type": "Organization",
                    "name": "Meccha Chameleon Cheats",
                    "logo": {"@type": "ImageObject", "url": LOGO},
                },
                "mainEntityOfPage": canonical,
                "datePublished": "2026-08-05",
                "dateModified": TODAY,
                "inLanguage": "en",
            }
        )
        schemas.append(
            breadcrumb([("Home", f"{DOMAIN}/"), ("Guide", canonical)])
        )

    if kind == "article":
        # try date from <time datetime="">
        dm = re.search(r'<time[^>]+datetime=["\']([^"\']+)["\']', html, re.I)
        published = dm.group(1) if dm else "2026-07-01"
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": h1[:110],
                "description": desc,
                "image": [og_image],
                "author": {"@type": "Organization", "name": "Meccha Chameleon Cheats"},
                "publisher": {
                    "@type": "Organization",
                    "name": "Meccha Chameleon Cheats",
                    "logo": {"@type": "ImageObject", "url": LOGO},
                },
                "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
                "datePublished": published,
                "dateModified": TODAY,
                "inLanguage": "en",
                "articleSection": "Meccha Chameleon",
                "keywords": [
                    "Meccha Chameleon",
                    "Meccha Chameleon cheats",
                    "Meccha Chameleon tips",
                    "Meccha Chameleon Steam",
                ],
            }
        )
        schemas.append(
            breadcrumb(
                [
                    ("Home", f"{DOMAIN}/"),
                    ("Blog", f"{DOMAIN}/blog"),
                    (h1[:60], canonical),
                ]
            )
        )

    return schemas


def social_and_tech_tags(path: Path, html: str) -> str:
    title = get_title(html)
    desc = get_meta(html, "description") or title
    canonical = get_canonical(html) or f"{DOMAIN}/"
    og_image = get_og_image(html)
    kind = page_kind(path)
    og_type = "article" if kind in {"article", "guide"} else "website"

    tags = f"""<!-- SEO-HARDEN:START -->
  <meta name="theme-color" content="#0B0914">
  <meta name="author" content="Meccha Chameleon Cheats">
  <meta name="keywords" content="Meccha Chameleon cheats, Meccha Chameleon hack, Meccha Chameleon ESP, Meccha Chameleon tips, Meccha Chameleon Steam, Meccha Chameleon camouflage, mecchahacks">
  <meta name="googlebot" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="bingbot" content="index, follow">
  <link rel="alternate" hreflang="en" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{canonical}">
  <meta property="og:site_name" content="Meccha Chameleon Cheats">
  <meta property="og:locale" content="en_US">
  <meta property="og:type" content="{og_type}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:alt" content="{title}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og_image}">
  <link rel="apple-touch-icon" href="{LOGO}">
  <link rel="manifest" href="/site.webmanifest">
"""
    if path.name == "index.html":
        tags += f"""  <link rel="preload" as="image" href="images/hero-bg.webp" type="image/webp">
  <!-- After deploy: paste Google Search Console code below
  <meta name="google-site-verification" content="PASTE_VERIFICATION_CODE">
  -->
  <!-- After deploy: replace G-XXXXXXXXXX with your GA4 Measurement ID
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XXXXXXXXXX');</script>
  -->
"""
    # schemas
    for schema in schemas_for(path, html):
        # skip duplicate FAQ on product (already present)
        if schema.get("@type") == "FAQPage":
            continue
        if path.name == "meccha-chameleon-cheats.html" and schema.get("@type") == "FAQPage":
            continue
        payload = json.dumps(schema, ensure_ascii=True, indent=2)
        tags += f'  <script type="application/ld+json">\n{payload}\n  </script>\n'

    # Product page already has FAQ — keep it; we add Product + Breadcrumb above
    tags += "  <!-- SEO-HARDEN:END -->\n"
    return tags


def upsert_head(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    html = remove_blocks(html)

    # Ensure robots index follow
    if 'name="robots"' not in html:
        html = html.replace(
            "<head>",
            '<head>\n  <meta name="robots" content="index, follow, max-image-preview:large">',
            1,
        )
    else:
        html = re.sub(
            r'<meta name="robots" content="[^"]*">',
            '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">',
            html,
            count=1,
        )

    # Normalize og:image to absolute if relative
    def abs_og(m):
        val = m.group(1)
        if val.startswith("http"):
            return m.group(0)
        return m.group(0).replace(val, f"{DOMAIN}/{val.lstrip('/')}")

    html = re.sub(r'(property="og:image" content=")([^"]+)(")', abs_og, html)

    # Remove duplicate weak twitter:card summary if we inject large image
    # Insert SEO bundle before </head>
    bundle = social_and_tech_tags(path, html)
    # Avoid duplicating identical og tags too heavily: strip old og/twitter that will be replaced
    # Keep original title/description/canonical — remove old og:* and twitter:* lines outside harden block
    html = re.sub(r'\n\s*<meta property="og:[^"]+" content="[^"]*">', "", html)
    html = re.sub(r'\n\s*<meta name="twitter:[^"]+" content="[^"]*">', "", html)

    html = html.replace("</head>", bundle + "</head>", 1)
    path.write_text(html, encoding="utf-8")
    print("seo", path.name)


def write_sitemap() -> None:
    pages = [
        ("/", "1.0", "daily"),
        ("/meccha-chameleon-cheats", "0.95", "weekly"),
        ("/blog", "0.9", "daily"),
        ("/guide", "0.85", "weekly"),
    ]
    blogs = sorted(p.stem for p in ROOT.glob("blog-*.html"))
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, pri, freq in pages:
        lines += [
            "  <url>",
            f"    <loc>{DOMAIN}{loc if loc != '/' else '/'}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{pri}</priority>",
            "  </url>",
        ]
    for slug in blogs:
        lines += [
            "  <url>",
            f"    <loc>{DOMAIN}/{slug}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            "    <changefreq>weekly</changefreq>",
            "    <priority>0.75</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("sitemap", 4 + len(blogs))


def write_robots() -> None:
    (ROOT / "robots.txt").write_text(
        f"""User-agent: *
Allow: /
Disallow: /scripts/
Disallow: /seo-setup.html

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
Host: {DOMAIN.replace('https://', '')}
""",
        encoding="utf-8",
    )


def write_htaccess() -> None:
    (ROOT / ".htaccess").write_text(
        """RewriteEngine On
RewriteBase /

# Force HTTPS
RewriteCond %{HTTPS} !=on
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Force non-www
RewriteCond %{HTTP_HOST} ^www\\.(.+)$ [NC]
RewriteRule ^ https://%1%{REQUEST_URI} [L,R=301]

# Remove trailing slash (except root)
RewriteCond %{REQUEST_URI} ^(.+)/$
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.+)/$ /$1 [L,R=301]

# Redirect .html to clean URL
RewriteCond %{THE_REQUEST} \\s/+(.+?)\\.html[\\s?] [NC]
RewriteRule ^ /%1 [R=301,L]

# Serve extensionless HTML
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.+?)/?$ $1.html [L]

# Security / SEO headers
<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
  Header set X-Frame-Options "SAMEORIGIN"
  Header set Permissions-Policy "geolocation=(), microphone=(), camera=()"
</IfModule>

# Cache static assets
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/jpeg "access plus 30 days"
  ExpiresByType image/webp "access plus 30 days"
  ExpiresByType image/png "access plus 30 days"
  ExpiresByType text/css "access plus 7 days"
  ExpiresByType application/javascript "access plus 7 days"
</IfModule>
""",
        encoding="utf-8",
    )


def write_netlify_redirects() -> None:
    # For Netlify/Cloudflare Pages style hosts
    (ROOT / "_redirects").write_text(
        """
https://www.mecchahacks.com/*  https://mecchahacks.com/:splat  301!
http://mecchahacks.com/*       https://mecchahacks.com/:splat  301!
http://www.mecchahacks.com/*   https://mecchahacks.com/:splat  301!

/*  /:splat.html  200!
""".strip()
        + "\n",
        encoding="utf-8",
    )
    (ROOT / "netlify.toml").write_text(
        """[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    X-Frame-Options = "SAMEORIGIN"

[[headers]]
  for = "/images/*"
  [headers.values]
    Cache-Control = "public, max-age=2592000"
""",
        encoding="utf-8",
    )


def write_manifest() -> None:
    (ROOT / "site.webmanifest").write_text(
        json.dumps(
            {
                "name": "Meccha Chameleon Cheats — Meccha Chameleon Cheats",
                "short_name": "Meccha Chameleon Cheats",
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
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def write_setup_page() -> None:
    blogs = sorted(p.stem for p in ROOT.glob("blog-*.html"))
    links = "\n".join(f'      <li><a href="/{s}">{s}</a></li>' for s in blogs[:12])
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SEO Launch Checklist — Meccha Chameleon Cheats</title>
  <meta name="robots" content="noindex, nofollow">
  <link rel="stylesheet" href="css/global.css">
</head>
<body>
  <main class="container article-wrap prose">
    <h1>SEO Launch Checklist (do after deploy)</h1>
    <p>This page is <strong>noindex</strong>. Use it once, then ignore it.</p>
    <h2>1. Deploy</h2>
    <ol>
      <li>Upload the full site folder to hosting</li>
      <li>Point <code>mecchahacks.com</code> DNS to the host</li>
      <li>Turn on HTTPS</li>
      <li>Confirm clean URLs work (no .html in address bar)</li>
    </ol>
    <h2>2. Google Search Console</h2>
    <ol>
      <li>Add property: <code>{DOMAIN}</code></li>
      <li>Paste verification meta into <code>index.html</code> (placeholder already marked)</li>
      <li>Submit sitemap: <a href="/sitemap.xml">{DOMAIN}/sitemap.xml</a></li>
      <li>Request indexing for Home, Buy, Blog, Guide, and top posts</li>
    </ol>
    <h2>3. Analytics</h2>
    <ol>
      <li>Create GA4 property</li>
      <li>Replace <code>G-XXXXXXXXXX</code> in <code>index.html</code></li>
      <li>Test Buy button click as a conversion event</li>
    </ol>
    <h2>4. Quick URL checks</h2>
    <ul>
      <li><a href="/">{DOMAIN}/</a></li>
      <li><a href="/meccha-chameleon-cheats">{DOMAIN}/meccha-chameleon-cheats</a></li>
      <li><a href="/blog">{DOMAIN}/blog</a></li>
      <li><a href="/guide">{DOMAIN}/guide</a></li>
{links}
    </ul>
    <h2>5. Ongoing</h2>
    <ul>
      <li>Publish 2–3 keyword posts weekly</li>
      <li>Update old posts monthly</li>
      <li>Earn natural backlinks (forums, social, guides)</li>
      <li>Watch Search Console coverage + queries every week</li>
    </ul>
    <p><a class="btn btn-primary" href="/">Back to Home</a></p>
  </main>
</body>
</html>
"""
    (ROOT / "seo-setup.html").write_text(html, encoding="utf-8")


def main() -> None:
    html_files = [p for p in ROOT.glob("*.html") if p.name != "seo-setup.html"]
    for path in sorted(html_files):
        upsert_head(path)
    write_sitemap()
    write_robots()
    write_htaccess()
    write_netlify_redirects()
    write_manifest()
    write_setup_page()
    print("done", len(html_files))


if __name__ == "__main__":
    main()
