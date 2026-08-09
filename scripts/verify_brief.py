from pathlib import Path
import re

files = list(Path(".").glob("*.html"))
mh = [p.name for p in files if "Meccha Hacks" in p.read_text(encoding="utf-8")]
print("Meccha Hacks files:", mh or "none")

vis = []
for p in files:
    t = p.read_text(encoding="utf-8")
    s = re.sub(r"https?://[^\s\"'<>]+", "", t)
    s = re.sub(r'(href|src)="[^"]+"', "", s)
    if re.search(r"zadeyo", s, re.I):
        vis.append(p.name)
print("visible zadeyo files:", vis or "none")

idx = Path("index.html").read_text(encoding="utf-8")
print("logo remote:", "zadeyo.com/_next/image" in idx)
print("nav product name:", "Meccha Chameleon Cheats" in idx)
print(
    "missing blogs exist:",
    Path("blog-meccha-chameleon-painting-multiplayer.html").exists(),
    Path("blog-meccha-chameleon-hide-and-seek-online.html").exists(),
    Path("blog-meccha-chameleon-artistic-skill-game.html").exists(),
    Path("blog-meccha-chameleon-chameleon-painting-simulator.html").exists(),
)
blog = Path("blog.html").read_text(encoding="utf-8")
print("spoofing filter:", 'data-filter="spoofing"' in blog)
print("painting multiplayer card:", "painting-multiplayer" in blog)
print("keyword blog count:", len(list(Path(".").glob("blog-meccha-chameleon-*.html"))))
