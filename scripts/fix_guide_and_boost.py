# -*- coding: utf-8 -*-
"""Clean guide page, boost any still-thin blogs, refresh sitemap + seo-setup."""
from pathlib import Path
import re
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
TODAY = date.today().isoformat()

GUIDE_PROSE = r'''
        <h2 id="what-anti-cheat">What Anti-Cheat Does Meccha Chameleon Use?</h2>
        <p>Short answer: Meccha Chameleon does not ship a dedicated commercial anti-cheat stack. There is no Easy Anti-Cheat, no BattlEye, and no Valve Anti-Cheat (VAC) scanning listed for the PC client the way you see on many competitive shooters.</p>
        <p>Online lobbies use <strong>Epic Online Services (EOS)</strong> for matchmaking and account infrastructure. EOS is networking and session glue — it is not the same thing as a kernel anti-cheat driver that scans processes at boot.</p>
        <p>That distinction matters for anyone comparing Meccha Chameleon cheat software to tools built for games with Ricochet, ACE, EAC, or Vanguard. The risk model here is different: social reports and developer action matter more than signature waves.</p>
        <p>If you only remember one sentence: <strong>no kernel AC ≠ no consequences</strong>. Public lobbies still punish obvious play.</p>

        <h2 id="kernel-level">Is Meccha Chameleon Using Kernel-Level Anti-Cheat?</h2>
        <p>No. Community and product research for the current PC build points to <strong>no kernel-level anti-cheat</strong>. There is no ring-0 driver from Meccha Chameleon continuously scanning for injected overlays the way EAC or BattlEye does in other titles.</p>
        <h3>What “no kernel AC” does not mean</h3>
        <p>It does not mean “no bans.” Developers can still remove accounts after reports, clips, and repeated complaints. Hosts can kick. Friends can refuse to queue with you. Stream audiences can pile on. Software silence is not the same as social invisibility.</p>
        <h3>How this changes tool design priorities</h3>
        <p>On kernel-heavy titles, delivery architecture dominates the conversation. On Meccha Chameleon, delivery still matters (loader stability, CLOUD-DMA option on AWS, Windows requirements), but <strong>behavior and stream leaks</strong> are the everyday risk surfaces. That is why stream-proof overlay mode is a first-class feature on the buy page.</p>

        <h2 id="how-it-works">How Enforcement Actually Works</h2>
        <p>Enforcement in Meccha Chameleon is primarily <strong>report-driven</strong>:</p>
        <ul>
          <li>Players notice Instant Tag snaps, wall-perfect Heat Vision plays, or impossible camouflage breaks</li>
          <li>They record clips and file reports</li>
          <li>Developers or moderators can act on that evidence</li>
          <li>Lobby hosts can remove disruptors immediately</li>
        </ul>
        <p>There is no confirmed automated wave-ban signature system comparable to large competitive shooters. Your behavior in lobby is the main risk surface — especially on Meccha Chameleon multiplayer public queues.</p>
        <h3>Practical takeaway for tool users</h3>
        <p>Subtle presets matter more here than empty “undetected forever” slogans. Use Heat Vision / ESP and Instant Tag at a human pace in public matches if you care about reports. Save loud Match Timer Freeze and Full-Map Reveal patterns for private sessions when you want maximum control.</p>
        <h3>Patch cadence still matters</h3>
        <p>Even without kernel AC, game updates can break loaders and overlays. Our target window is <strong>2–4 hours</strong> after Meccha Chameleon patches so access is not stuck for days. Free leaks usually lose that race.</p>

        <h2 id="eos">What Epic Online Services Does (and Does Not Do)</h2>
        <p>EOS handles lobby creation, matchmaking, and online session identity for Meccha Chameleon online play. It is why Steam players can enter shared lobbies quickly.</p>
        <p>EOS does <strong>not</strong> automatically equal a full anti-cheat product. Treat it as account and networking infrastructure — not as proof that a kernel scanner is watching every overlay.</p>
        <p>For lobby behavior guides, continue to <a href="blog-meccha-chameleon-online.html">online lobbies</a> and <a href="blog-meccha-chameleon-multiplayer.html">multiplayer formats</a>. This page stays focused on enforcement architecture.</p>

        <h2 id="dma-detection">Can Meccha Chameleon Detect DMA / Cloud DMA?</h2>
        <p>Without a dedicated kernel anti-cheat layer, classic DMA hardware detection is not the primary enforcement story for Meccha Chameleon. The bigger risks remain malware from free leaks, account reports, and broken loaders after patches.</p>
        <p>Our suite offers optional <strong>CLOUD-DMA on AWS</strong> as a delivery method inside the same product — not a second unrelated cheat. Processing runs on AWS cloud infrastructure for players who want an external path alongside the standard loader workflow. Read the full breakdown in <a href="blog-cloud-dma-aws.html">How Cloud DMA on AWS Works</a>.</p>
        <h3>Hosting clarity</h3>
        <p>CLOUD-DMA option and AWS option are the same delivery story: cloud-hosted DMA path on AWS, inside one suite, with the same feature list as Monthly and Lifetime plans.</p>

        <h2 id="safer-habits">Safer Setup Habits</h2>
        <p>If you run Meccha Chameleon cheats for PC, keep the stack consistent with the <a href="meccha-chameleon-cheats.html#features">buy-page feature list</a>:</p>
        <ol>
          <li>Enable HVCI, Core Isolation, TPM, and Secure Boot before first load</li>
          <li>Use stream-proof overlay mode when you stream Meccha Chameleon gameplay</li>
          <li>Prefer maintained builds with 2–4 hour patch updates over random free downloads</li>
          <li>Enable CLOUD-DMA (AWS) when you want the cloud delivery option</li>
          <li>Learn hider and seeker modules separately so you are not toggling every loud tool by accident</li>
        </ol>
        <p>For role-specific settings, start with the <a href="blog-hider-setup-guide.html">hider setup guide</a> and the <a href="blog-seeker-esp-setup-guide.html">seeker ESP setup guide</a>. For commercial decision-making, use the <a href="blog-cheat-comparison-2026.html">2026 comparison</a>.</p>
        <h3>Windows requirements (locked)</h3>
        <ul>
          <li>HVCI ON</li>
          <li>Core Isolation ON</li>
          <li>TPM ON</li>
          <li>Secure Boot ON</li>
          <li>Windows 10 or Windows 11</li>
          <li>CLOUD-DMA / AWS — option</li>
        </ul>

        <h2 id="feature-truth">Feature truth (never contradict the buy page)</h2>
        <ul>
          <li>Pixel-Perfect Blend camo for hider rounds</li>
          <li>Auto-Chameleon Paint with environment color match</li>
          <li>Auto-Pose Snapping for frozen disguise poses</li>
          <li>Perfect Disguise — lock camouflage until tagged</li>
          <li>Freeze Pose Timer to hold your stealth stance</li>
          <li>Infinite Stamina for hiders and seekers</li>
          <li>Heat Vision / ESP — see hiders through walls (seeker)</li>
          <li>Hider positions on minimap (seeker role)</li>
          <li>Instant Tag and one-hit tag through obstacles</li>
          <li>Super Speed (1–5×) for seeker closes</li>
          <li>Reveal All Hiders and freeze hider in place</li>
          <li>Match timer freeze and full-map reveal</li>
          <li>Free camera / noclip for scouting hiding spots</li>
          <li>Stream-proof overlay mode</li>
          <li>CLOUD-DMA option · AWS option</li>
        </ul>

        <h2 id="faq">FAQ</h2>
        <div class="faq-list" style="margin-top:1rem">
          <details class="faq-item" open>
            <summary>Does Meccha Chameleon have anti-cheat?</summary>
            <div class="faq-body">It does not have a dedicated kernel anti-cheat like EAC, BattlEye, or VAC. Online play uses Epic Online Services for matchmaking. Bans and removals are mainly report-based.</div>
          </details>
          <details class="faq-item">
            <summary>Can I still get banned?</summary>
            <div class="faq-body">Yes. Obvious cheating gets clipped and reported. Developer action can still remove accounts even without automated signature scanning.</div>
          </details>
          <details class="faq-item">
            <summary>Is Cloud DMA a separate product?</summary>
            <div class="faq-body">No. CLOUD-DMA on AWS is an optional delivery path inside the same suite with the same feature list.</div>
          </details>
          <details class="faq-item">
            <summary>Where do I buy the full tool suite?</summary>
            <div class="faq-body">See plans and the complete feature list on the <a href="meccha-chameleon-cheats.html">Meccha Chameleon cheats buy page</a>. Monthly is $35; Lifetime is $150 with permanent access and future updates.</div>
          </details>
          <details class="faq-item">
            <summary>Where is the resource hub?</summary>
            <div class="faq-body">Use <a href="resources.html">mecchahacks.com/resources</a> as the clean citation page for communities and creators.</div>
          </details>
        </div>
'''


def fix_guide():
    path = ROOT / "guide.html"
    html = path.read_text(encoding="utf-8")
    html = re.sub(r"<figure class=\"inline-shot\">.*?</figure>", "", html, flags=re.S)
    html = re.sub(r'<div class="article-gallery">.*?</div>\s*', "", html, flags=re.S)
    html = re.sub(
        r'(<div class="prose">)(.*?)(</div>\s*<div class="article-cta">)',
        r"\1" + GUIDE_PROSE + r"\3",
        html,
        count=1,
        flags=re.S,
    )
    # toc add feature truth + resources
    if 'href="#feature-truth"' not in html:
        html = html.replace(
            '<li><a href="#faq">FAQ</a></li>',
            '<li><a href="#safer-habits">Safer setup habits</a></li>\n          <li><a href="#feature-truth">Feature truth</a></li>\n          <li><a href="#faq">FAQ</a></li>',
        )
    if "site-config.js" not in html:
        html = html.replace(
            '<script src="js/main.js" defer></script>',
            '<script src="js/site-config.js"></script>\n  <script src="js/analytics.js" defer></script>\n  <script src="js/main.js" defer></script>',
        )
    # related add resources
    if "resources.html" not in html:
        html = html.replace(
            '<li><a href="meccha-chameleon-cheats.html">Pricing &amp; full feature list</a></li>',
            '<li><a href="meccha-chameleon-cheats.html">Pricing &amp; full feature list</a></li>\n          <li><a href="resources.html">Resources hub</a></li>',
        )
    path.write_text(html, encoding="utf-8")
    print("guide fixed")


BOOST = """
        <h2>Depth notes for searchers who want more than a blurb</h2>
        <p>Thin pages lose to Steam, IGN, and malware spam farms for competitive head terms. This section exists to give you a complete, usable brief: what to do in the next lobby, what to ignore, and which sibling article to open if your intent shifted mid-search.</p>
        <p>Use a 20-minute practice block: five minutes private paint warm-up, ten minutes role focus (hide or seek), five minutes review. Write one sentence about what failed. That single habit beats reading twenty duplicate posts.</p>
        <h3>Checklist you can reuse tonight</h3>
        <ul>
          <li>Confirm you are on the Steam PC client</li>
          <li>Pick private vs public before launch</li>
          <li>Choose one map to master</li>
          <li>Decide unaided practice vs tool-assisted practice</li>
          <li>If streaming, enable stream-proof overlay mode first</li>
          <li>If buying tools, verify features against the buy page list only</li>
        </ul>
        <h3>Internal links with different intents</h3>
        <p>Overview: <a href="blog-what-is-meccha-chameleon.html">what is Meccha Chameleon</a>. Install safety: <a href="blog-meccha-chameleon-download.html">download guide</a>. Skill: <a href="blog-meccha-chameleon-tips.html">tips</a>. Enforcement: <a href="guide.html">anti-cheat guide</a>. Commerce: <a href="meccha-chameleon-cheats.html">pricing &amp; features</a>. Citation hub: <a href="resources.html">resources</a>.</p>
        <p>Pricing reminder for tool buyers: Monthly $35 (31 days) or Lifetime $150 (permanent access + future updates), full feature parity, Windows requirements listed on the buy page, CLOUD-DMA available as an AWS option.</p>
"""


def boost_thin(min_words=900):
    for path in sorted(ROOT.glob("blog-*.html")):
        t = path.read_text(encoding="utf-8")
        t2 = re.sub(r"<script[^>]*>.*?</script>", "", t, flags=re.S | re.I)
        words = len(re.findall(r"[A-Za-z0-9']+", re.sub(r"<[^>]+>", " ", t2)))
        if words >= min_words:
            continue
        if "Depth notes for searchers" in t:
            continue
        if '<div class="prose">' not in t:
            continue
        t = t.replace(
            '<aside class="eeat-box"',
            BOOST + '\n    <aside class="eeat-box"',
            1,
        )
        # if eeat missing, inject before FAQ heading inside prose
        if "Depth notes for searchers" not in t:
            t = t.replace("<h2>FAQ</h2>", BOOST + "\n        <h2>FAQ</h2>", 1)
        path.write_text(t, encoding="utf-8")
        print(f"boosted {path.name} (was {words})")


def rebuild_sitemap():
    urls = [
        ("https://mecchahacks.com/", "1.0", "daily"),
        ("https://mecchahacks.com/meccha-chameleon-cheats", "0.95", "weekly"),
        ("https://mecchahacks.com/blog", "0.9", "daily"),
        ("https://mecchahacks.com/guide", "0.9", "weekly"),
        ("https://mecchahacks.com/resources", "0.9", "weekly"),
    ]
    for p in sorted(ROOT.glob("blog-*.html")):
        urls.append((f"https://mecchahacks.com/{p.stem}", "0.8", "weekly"))
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, pri, freq in urls:
        parts.append(
            f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>"
        )
    parts.append("</urlset>\n")
    (ROOT / "sitemap.xml").write_text("\n".join(parts), encoding="utf-8")
    print("sitemap urls", len(urls))


def patch_index_footer_resources():
    for name in ["index.html", "meccha-chameleon-cheats.html", "blog.html", "guide.html"]:
        path = ROOT / name
        html = path.read_text(encoding="utf-8")
        if "resources.html" not in html:
            html = html.replace(
                '<a href="guide.html">Guide</a>',
                '<a href="guide.html">Guide</a>\n            <a href="resources.html">Resources</a>',
                1,
            )
        if "site-config.js" not in html and 'script src="js/main.js"' in html:
            html = html.replace(
                '<script src="js/main.js" defer></script>',
                '<script src="js/site-config.js"></script>\n  <script src="js/analytics.js" defer></script>\n  <script src="js/main.js" defer></script>',
            )
        path.write_text(html, encoding="utf-8")


def update_seo_setup():
    path = ROOT / "seo-setup.html"
    path.write_text(
        """<!DOCTYPE html>
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
    <p>This page is <strong>noindex</strong>.</p>
    <h2>1. Deploy</h2>
    <ol>
      <li>Upload the full site folder</li>
      <li>Point <code>mecchahacks.com</code> DNS to the host</li>
      <li>Confirm HTTPS + clean URLs</li>
    </ol>
    <h2>2. Google Search Console + Analytics (one file)</h2>
    <ol>
      <li>Open <code>js/site-config.js</code></li>
      <li>Set <code>gscVerification</code> to your Search Console HTML-tag content value</li>
      <li>Set <code>ga4Id</code> to your GA4 ID like <code>G-XXXXXXXXXX</code></li>
      <li>Deploy that file</li>
      <li>Submit sitemap: <a href="/sitemap.xml">https://mecchahacks.com/sitemap.xml</a></li>
      <li>Request indexing for Home, Buy, Guide, Resources, and top posts</li>
    </ol>
    <h2>3. Domain authority (off-site)</h2>
    <p>Follow <a href="backlink-playbook.html">backlink-playbook.html</a> weekly. Share <a href="resources.html">/resources</a> as the citation URL.</p>
    <h2>4. QA</h2>
    <ul>
      <li><a href="qa-checklist.html">Feature consistency checklist</a></li>
      <li>Buy buttons fire <code>purchase_click</code> in dataLayer when GA is live</li>
    </ul>
    <p><a class="btn btn-primary" href="/">Back to Home</a></p>
  </main>
</body>
</html>
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    fix_guide()
    boost_thin(900)
    rebuild_sitemap()
    patch_index_footer_resources()
    update_seo_setup()
    print("done")
