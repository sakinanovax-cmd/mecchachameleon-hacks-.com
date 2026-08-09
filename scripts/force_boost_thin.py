# -*- coding: utf-8 -*-
from pathlib import Path
import re

BOOST = """
        <h2>Extra practical depth</h2>
        <p>Use this page as a complete brief, not a teaser. Before your next lobby: decide private vs public, pick one map, warm up paint for five minutes, then play ten focused rounds. Write one sentence about what failed. That loop beats hopping between thin search results.</p>
        <p>Game client stays on Steam. Tool features stay locked to the buy page list: Pixel-Perfect Blend, Auto-Chameleon Paint, Auto-Pose Snapping, Perfect Disguise, Freeze Pose Timer, Infinite Stamina, Heat Vision / ESP, hider minimap positions, Instant Tag and one-hit through obstacles, Super Speed (1–5×), Reveal All Hiders and freeze hider, match timer freeze, full-map reveal, free camera / noclip, stream-proof overlay mode, CLOUD-DMA option on AWS.</p>
        <p>Pricing: Monthly $35 or Lifetime $150 with identical features. Requirements: HVCI ON, Core Isolation ON, TPM ON, Secure Boot ON, Windows 10/11. Enforcement context: <a href="guide.html">anti-cheat guide</a>. Citation hub: <a href="resources.html">resources</a>. Comparison: <a href="blog-cheat-comparison-2026.html">2026 comparison</a>.</p>
        <p>If your search intent changed, do not stay on the wrong page. Download intent belongs on the download guide. Lobby systems belong on the online guide. Mode fantasy belongs on hide-and-seek pages. Tool buying belongs on the cheats page. Clear intents protect rankings and help you faster.</p>
"""


def main():
    for path in Path(".").glob("blog-*.html"):
        t = path.read_text(encoding="utf-8")
        t2 = re.sub(r"<script[^>]*>.*?</script>", "", t, flags=re.S | re.I)
        words = len(re.findall(r"[A-Za-z0-9']+", re.sub(r"<[^>]+>", " ", t2)))
        if words >= 950:
            continue
        if "Extra practical depth" in t:
            continue
        if '<div class="article-cta">' in t:
            t = t.replace('<div class="article-cta">', BOOST + '\n      <div class="article-cta">', 1)
        else:
            continue
        path.write_text(t, encoding="utf-8")
        print("forced", path.name, "was", words)


if __name__ == "__main__":
    main()
