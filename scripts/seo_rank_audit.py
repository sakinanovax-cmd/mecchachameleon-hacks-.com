from pathlib import Path
import re
from collections import Counter

files = sorted(Path(".").glob("blog*.html"))
rows = []
for p in files:
    t = p.read_text(encoding="utf-8")
    t2 = re.sub(r"<script[^>]*>.*?</script>", "", t, flags=re.S | re.I)
    t2 = re.sub(r"<style[^>]*>.*?</style>", "", t2, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", t2)
    words = len(re.findall(r"[A-Za-z0-9']+", text))
    title = re.search(r"<title>(.*?)</title>", t, re.I | re.S)
    desc = re.search(r'name="description" content="(.*?)"', t)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.I | re.S)
    canon = re.search(r'rel="canonical" href="(.*?)"', t)
    schema = '"@type": "Article"' in t or '"@type":"Article"' in t
    rows.append(
        (
            words,
            p.name,
            bool(title and h1 and canon and desc),
            schema,
            len(desc.group(1)) if desc else 0,
            re.sub("<[^>]+>", "", title.group(1)).strip() if title else "",
        )
    )

rows.sort()
print(f"blog pages: {len(rows)}")
print(f"thin <350 words: {sum(1 for r in rows if r[0] < 350)}")
print(f"350-700: {sum(1 for r in rows if 350 <= r[0] < 700)}")
print(f"700+: {sum(1 for r in rows if r[0] >= 700)}")
print(f"missing basic SEO tags: {sum(1 for r in rows if not r[2])}")
print(f"missing Article schema: {sum(1 for r in rows if not r[3])}")
print("\nThinnest 10:")
for r in rows[:10]:
    print(f"  {r[0]:4d} | {r[1]}")
print("\nThickest 5:")
for r in rows[-5:]:
    print(f"  {r[0]:4d} | {r[1]}")

titles = [r[5] for r in rows]
dups = [k for k, v in Counter(titles).items() if v > 1]
print("dup titles:", dups or "none")

# core pages
for name in ["index.html", "meccha-chameleon-cheats.html", "guide.html", "blog.html"]:
    t = Path(name).read_text(encoding="utf-8")
    ok = all(
        x in t
        for x in [
            'rel="canonical"',
            'name="description"',
            "<title>",
            'name="robots" content="index, follow',
        ]
    )
    print(f"{name}: seo_ok={ok}")

sm = Path("sitemap.xml").read_text(encoding="utf-8")
print("sitemap urls:", sm.count("<loc>"))
print("qa in sitemap:", "qa-checklist" in sm)
print("robots has qa disallow:", "qa-checklist" in Path("robots.txt").read_text(encoding="utf-8"))
