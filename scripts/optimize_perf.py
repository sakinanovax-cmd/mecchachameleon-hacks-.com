# -*- coding: utf-8 -*-
"""Performance assets: compress images, local logo, self-host Inter fonts."""
from __future__ import annotations

import re
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def compress_hero() -> None:
    src = Image.open(ROOT / "images" / "hero-source.jpg").convert("RGB")
    # Re-apply similar grade lightly from existing hero-bg if source is ungraded
    # Use current hero-bg.jpg as base for fidelity to what's on site
    base = Image.open(ROOT / "images" / "hero-bg.jpg").convert("RGB")
    base = base.resize((1600, 844), Image.Resampling.LANCZOS)
    out = ROOT / "images"
    base.save(out / "hero-bg.webp", "WEBP", quality=68, method=6)
    base.save(out / "hero-bg.jpg", "JPEG", quality=72, optimize=True)
    # Mobile LCP variant
    mobile = base.resize((960, 506), Image.Resampling.LANCZOS)
    mobile.save(out / "hero-bg-mobile.webp", "WEBP", quality=62, method=6)
    print("hero", (out / "hero-bg.webp").stat().st_size // 1024, "KB")


def compress_ign() -> None:
    ign = ROOT / "images" / "ign"
    webp_dir = ROOT / "images" / "ign-webp"
    webp_dir.mkdir(exist_ok=True)
    for path in sorted(ign.glob("*.jpg")):
        im = Image.open(path).convert("RGB")
        # card/strip size
        im.thumbnail((960, 960), Image.Resampling.LANCZOS)
        dest = webp_dir / (path.stem + ".webp")
        im.save(dest, "WEBP", quality=70, method=6)
        # also overwrite jpg smaller for fallback
        im.save(path, "JPEG", quality=75, optimize=True)
        print(path.name, dest.stat().st_size // 1024, "KB webp")


def download_logo() -> None:
    url = "https://zadeyo.com/_next/image?url=%2Frt-removebg-preview.png&w=128&q=75"
    data = fetch(url)
    dest = ROOT / "images" / "logo.png"
    dest.write_bytes(data)
    # also make a tiny favicon-ish copy
    try:
        im = Image.open(dest).convert("RGBA")
        im.resize((64, 64), Image.Resampling.LANCZOS).save(ROOT / "images" / "logo-64.png")
    except Exception as e:
        print("logo resize skip", e)
    print("logo", dest.stat().st_size)


def download_fonts() -> None:
    fonts_dir = ROOT / "fonts"
    fonts_dir.mkdir(exist_ok=True)
    css_url = (
        "https://fonts.googleapis.com/css2?"
        "family=Inter:wght@400;600;700;800&display=swap"
    )
    req = urllib.request.Request(
        css_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/css,*/*;q=0.1",
        },
    )
    css = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "ignore")
    weight_files = {
        m.group(1): m.group(2)
        for m in re.finditer(
            r"font-weight:\s*(\d+);\s*font-display:\s*swap;\s*src:\s*url\((https://fonts\.gstatic\.com/[^)]+)\)",
            css,
        )
    }
    if not weight_files:
        # fallback looser parse
        weight_files = {
            m.group(1): m.group(2)
            for m in re.finditer(
                r"font-weight:\s*(\d+);[\s\S]{0,200}?url\((https://fonts\.gstatic\.com/[^)]+\.woff2)\)",
                css,
            )
        }
    mapping = {
        "400": "inter-400.woff2",
        "600": "inter-600.woff2",
        "700": "inter-700.woff2",
        "800": "inter-800.woff2",
    }
    faces = []
    for weight, name in mapping.items():
        url = weight_files.get(weight)
        if not url:
            print("missing weight", weight)
            continue
        data = fetch(url)
        (fonts_dir / name).write_bytes(data)
        faces.append(
            f'@font-face{{font-family:"Inter";font-style:normal;font-weight:{weight};font-display:swap;src:url("../fonts/{name}") format("woff2")}}'
        )
        print("font", weight, len(data) // 1024, "KB")
    if not faces:
        raise RuntimeError("No fonts downloaded:\n" + css[:500])
    (ROOT / "css" / "fonts.css").write_text("\n".join(faces) + "\n", encoding="utf-8")
    print("fonts.css written")


def main() -> None:
    compress_hero()
    compress_ign()
    download_logo()
    download_fonts()


if __name__ == "__main__":
    main()
