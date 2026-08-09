# -*- coding: utf-8 -*-
"""Thicken every blog article, cut image spam, add FAQ + cluster links + E-E-A-T."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUY = "meccha-chameleon-cheats.html"
GUIDE = "guide.html"
HOME = "index.html"
BLOG = "blog.html"

FEATURES = """
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
  <li>CLOUD-DMA option (AWS)</li>
</ul>
"""

# Unique intent + section packs per slug (keeps pages non-cannibalizing)
# Each pack aims for 900–1200 words of unique prose when assembled.
PACKS: dict[str, dict] = {}


def pack(
    slug: str,
    intent: str,
    sections: list[tuple[str, str]],
    faqs: list[tuple[str, str]],
    related: list[tuple[str, str]],
    cluster: str,
):
    PACKS[slug] = {
        "intent": intent,
        "sections": sections,
        "faqs": faqs,
        "related": related,
        "cluster": cluster,
    }


# ---------- CLUSTER: game basics ----------
pack(
    "blog-what-is-meccha-chameleon",
    "This page answers the first search: what the game actually is. It is not a cheat page — it is the product definition so every other article can go deeper without repeating the same intro.",
    [
        (
            "The match loop in plain English",
            """<p>Meccha Chameleon is a multiplayer hide-and-seek game built around painting. Hiders start as plain figures, then brush colors onto their body until they match walls, floors, props, or Workshop stages. Seekers hunt before the timer ends. That paint skill check is the whole product.</p>
            <p>Unlike classic prop hunt, you are not stealing a barrel mesh. You are becoming the surface. Light, silhouette, pattern scale, and pose all matter. A “good hide” can fail if your outline still looks like a person standing on a rug.</p>
            <p>Matches are short, social, and clip-friendly. One round you laugh at a fridge camo. The next round a seeker clears the map with cold efficiency. That swing is why the game spreads on streams without a big marketing budget.</p>""",
        ),
        (
            "Who made Meccha Chameleon",
            """<p>The game comes from Japanese indie creators Lemorion_1224 and Haganeiro. Small team. Fast iteration. Steam-first release. Players searching “Meccha Chameleon Japanese game” or creator names usually want this context before they buy or download tools.</p>
            <p>Indie size also explains the enforcement model: Epic Online Services handles a lot of online glue, while lobby discipline is often report-driven instead of a heavy kernel anti-cheat stack. We cover that in the <a href="{GUIDE}">anti-cheat guide</a>.</p>""",
        ),
        (
            "Who this game is for",
            """<p>Friend groups who like party games. Streamers who want visual humor. Competitive lobby grinders who treat camouflage like a craft. If you hate painting, you will bounce. If you like creative stealth, Meccha Chameleon is sticky.</p>
            <p>New players should start in private lobbies, learn brush controls, then move to public queues. Public rooms are louder, map-mod heavy, and less patient with slow painters.</p>""",
        ),
        (
            "How this site fits (without repeating every page)",
            """<p>Use this page as the definition. Use <a href="blog-meccha-chameleon-gameplay.html">gameplay</a> for round feel, <a href="blog-meccha-chameleon-tips.html">tips</a> for quick wins, and the <a href="{BUY}">cheats page</a> only when you want the full PC tool suite. Keeping those intents split is how we avoid keyword cannibalization.</p>""",
        ),
    ],
    [
        ("Is Meccha Chameleon only multiplayer?", "Yes for the fun that matters. The product is lobby play — hide, paint, seek, laugh, rematch."),
        ("Is it a prop hunt clone?", "It shares DNA with prop hunt, but painting your body is the main skill, not prop swapping."),
        ("Where do I get the game?", "Steam is the clean download path. See our <a href=\"blog-meccha-chameleon-download.html\">download guide</a>."),
    ],
    [
        ("blog-meccha-chameleon-gameplay.html", "Gameplay feel"),
        ("blog-meccha-chameleon-steam.html", "Steam page notes"),
        ("blog-meccha-chameleon-lemorion.html", "Lemorion_1224"),
        ("{BUY}", "Cheats & pricing"),
    ],
    "basics",
)

pack(
    "blog-meccha-chameleon-online",
    "Intent: online lobbies and matchmaking behavior — not general “what is the game,” not download, not tips. Rank for players already installed who want lobby knowledge.",
    [
        (
            "Public vs private Meccha Chameleon online rooms",
            """<p>Public lobbies are chaotic: Workshop maps, mixed skill, voice spam, and rematch spam. Private lobbies are for friends, coaching, and clean practice. If you are learning paint, private first. If you want heat, public queues.</p>
            <p>Online sessions lean on Epic Online Services for lobby glue. That is matchmaking and account plumbing — not the same as Easy Anti-Cheat or BattlEye kernel stacks. Details live on the <a href="{GUIDE}">guide</a>.</p>""",
        ),
        (
            "What breaks a public queue",
            """<p>Host leaves. Map fails to load. Someone stalls the round. Ping spikes. When a room feels broken, leave early. Requeue is faster than arguing in chat. Keep a short list of maps your machine runs well.</p>
            <p>For seeker rounds in sweaty public rooms, vision tools and clean routes matter more than flashy movement. For hider rounds, paint speed and pose discipline beat fancy brush art.</p>""",
        ),
        (
            "Party play checklist for online nights",
            """<ol>
            <li>Agree private vs public before launch</li>
            <li>Set voice channel outside the game if needed</li>
            <li>Warm up with one practice paint round</li>
            <li>Rotate host if someone has unstable internet</li>
            <li>End on a win, not on tilt</li>
            </ol>
            <p>If your group uses PC tools, keep stream-proof overlay on before you go live. Feature truth stays on the <a href="{BUY}">buy page</a>.</p>""",
        ),
        (
            "Online vs “hide and seek online” keyword",
            """<p>This article is about lobby systems. If you want the mode fantasy and paint twist, read <a href="blog-meccha-chameleon-hide-and-seek-online.html">hide and seek online</a>. Different intent. Different H1. That split protects rankings.</p>""",
        ),
    ],
    [
        ("Does Meccha Chameleon online need friends?", "No. Public lobbies exist. Friends just make private rooms better."),
        ("Is there ranked matchmaking?", "Treat public lobbies as informal competition. See <a href=\"blog-meccha-chameleon-ranking-system.html\">ranking system notes</a>."),
        ("Can I use tools online?", "PC suite users should follow Windows requirements and stream-proof guidance on the buy page."),
    ],
    [
        ("blog-meccha-chameleon-multiplayer.html", "Multiplayer overview"),
        ("blog-meccha-chameleon-hide-and-seek-online.html", "Hide & seek online"),
        ("blog-meccha-chameleon-crossplay.html", "Crossplay reality"),
        ("{GUIDE}", "Anti-cheat guide"),
    ],
    "online",
)

pack(
    "blog-meccha-chameleon-download",
    "Intent: safe PC install path. Compete with malware pages by being the trustworthy “Steam only” answer, then bridge to tools without pretending to replace Steam.",
    [
        (
            "Official Meccha Chameleon download steps (Steam)",
            """<ol>
            <li>Install Steam and create an account</li>
            <li>Search “Meccha Chameleon”</li>
            <li>Open the official store listing</li>
            <li>Purchase or claim the game</li>
            <li>Click Install and wait for the download</li>
            <li>Launch, set graphics, join a private lobby first</li>
            </ol>
            <p>That is the only download path we recommend. Random “Meccha Chameleon free download” mirrors are a common malware funnel.</p>""",
        ),
        (
            "PC basics before first launch",
            """<p>Use Windows 10 or 11. Update GPU drivers if paint brushes stutter. Close heavy overlays if the client hitchs. Storage space matters more than people admit when Workshop maps pile up.</p>
            <p>If you later load lobby tools, the suite expects HVCI, Core Isolation, TPM, and Secure Boot ON — listed on the <a href="{BUY}">requirements box</a>.</p>""",
        ),
        (
            "How to beat malware “download” SERPs",
            """<p>You will not outrank Steam’s brand for the game client forever without links — but you can own the safety angle: “official Steam install + what to avoid.” That is the unique value of this page versus dump sites.</p>
            <p>Never install a “crack,” “offline unlocker,” or “workshop pack EXE” from unknown hosts. Workshop content belongs inside Steam’s Workshop UI.</p>""",
        ),
        (
            "After download: first hour plan",
            """<p>Private lobby. Practice paint on one map. Learn freeze pose. Then read <a href="blog-meccha-chameleon-tips.html">tips</a> and <a href="blog-meccha-chameleon-painting-techniques.html">painting techniques</a>. Tools come last, after you understand the loop.</p>""",
        ),
    ],
    [
        ("Is there an official free download?", "Use Steam’s listing. Ignore third-party free EXE sites."),
        ("Mobile download?", "See <a href=\"blog-meccha-chameleon-mobile-version.html\">mobile version</a> — PC Steam is the main product."),
        ("Download cheats vs download game?", "Different files. Game = Steam. Tools = purchase redirect from the buy page after payment."),
    ],
    [
        ("blog-meccha-chameleon-steam.html", "Steam notes"),
        ("blog-meccha-chameleon-free.html", "Free vs paid reality"),
        ("blog-meccha-chameleon-maps-download.html", "Maps / Workshop"),
        ("{BUY}", "PC cheats suite"),
    ],
    "acquire",
)

# Generate remaining packs programmatically with unique text per slug to finish faster
# while keeping strong uniqueness via keyword-specific hooks.


def auto_pack(slug: str, kw: str, angle: str, cluster: str, extras: list[tuple[str, str]], related: list[tuple[str, str]], faqs: list[tuple[str, str]] | None = None):
    """Build a long unique article body from angle + extras."""
    intent = f"Primary intent for “{kw}”: {angle} This page stays in its lane so it does not compete with sibling articles that target nearby phrases."
    sections = [
        (
            f"What people mean when they search “{kw}”",
            f"""<p>{angle}</p>
            <p>Searchers rarely want a dictionary definition. They want a decision, a checklist, or a mistake to avoid. This page is written for that job. If you need the product overview instead, start at <a href="blog-what-is-meccha-chameleon.html">what is Meccha Chameleon</a>.</p>
            <p>We keep claims about lobby tools identical to the <a href="{BUY}">buy page feature list</a>. No invented modules. No HWID spoofer claims. CLOUD-DMA is an AWS option inside the same suite.</p>""",
        ),
        (
            f"Practical breakdown for {kw}",
            f"""<p>Treat Meccha Chameleon as a paint-first hide-and-seek multiplayer game. Hiders win with color match, pose, and patience. Seekers win with route discipline, silhouette reading, and timer awareness. Everything else is flavor.</p>
            <p>When you evaluate guides for {kw}, ask: does this help me win the next ten rounds, or is it keyword filler? Below is the actionable layer we wish every thin SERP page included.</p>
            <ul>
              <li>Define the role you are playing before you open menus</li>
              <li>Pick one map to master before you chase twenty Workshop stages</li>
              <li>Practice paint speed in private lobbies</li>
              <li>Record one round and review where you got spotted or wasted time</li>
              <li>Only then add tools if you want role assists</li>
            </ul>""",
        ),
    ]
    sections.extend(extras)
    sections.append(
        (
            "Tool suite bridge (same feature truth everywhere)",
            f"""<p>If you came for {kw} and now want PC lobby tools, use the locked feature set:</p>
            {FEATURES}
            <p>Pricing stays Monthly $35 / Lifetime $150 with full parity. Requirements: HVCI ON, Core Isolation ON, TPM ON, Secure Boot ON, Windows 10/11. Read the <a href="{GUIDE}">anti-cheat guide</a> for report-based enforcement context.</p>""",
        )
    )
    sections.append(
        (
            "Common mistakes on this topic",
            f"""<p>Players researching {kw} usually fail in three ways: they copy a tip from a different game mode, they skip private practice, or they download random files because a title tag said “free.” Stay on Steam for the client. Stay on the buy page for tools. Stay patient for paint skill.</p>
            <p>Another mistake is reading ten near-duplicate articles. Our cluster links below send you to sibling pages with different intents — not the same paragraph under a new H1.</p>""",
        )
    )
    if faqs is None:
        faqs = [
            (f"Is this the best page for {kw}?", f"Yes if you want depth on this angle. For pricing/features go to the buy page. For enforcement go to the guide."),
            ("Do you invent features?", "No. Features match the buy page list only."),
            ("Steam or third-party?", "Steam for the game. Purchased suite for tools."),
        ]
    pack(slug, intent, sections, faqs, related, cluster)


# Fill remaining keyword posts with unique angles
auto_pack(
    "blog-meccha-chameleon-gameplay",
    "Meccha Chameleon gameplay",
    "Describe the feel of a real match — hider paint pressure, seeker clear routes, and why clips go viral — not install steps and not lobby networking.",
    "basics",
    [
        (
            "Hider round pacing",
            """<p>First 20 seconds: choose a zone, not a masterpiece. Next minute: block in big colors. Last stretch: edges, pose, freeze. Players who paint details first get tagged mid-brush.</p>
            <p>Good Meccha Chameleon gameplay for hiders looks boring on purpose. Stillness wins. Fidgeting is a free tell.</p>""",
        ),
        (
            "Seeker round pacing",
            """<p>Clear rooms in loops. Check high-contrast edges. Confirm before tag spam. Leave dead zones when the timer says so. Heat Vision / ESP and Instant Tag change pace if you use tools — but raw gameplay still rewards map literacy.</p>""",
        ),
        (
            "Why gameplay spreads on streams",
            """<p>Paint fails are comedy. Perfect blends are horror. Dual-role swaps keep energy high. That is the retention engine.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-tips.html", "Tips"),
        ("blog-meccha-chameleon-strategy.html", "Strategy"),
        ("blog-meccha-chameleon-hide-and-seek.html", "Hide & seek twist"),
        ("{BUY}", "Tool suite"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-hide-and-seek",
    "Meccha Chameleon hide and seek",
    "Explain the mode fantasy: classic hide and seek plus paint. Not the online systems page, not prop-hunt comparison.",
    "modes",
    [
        (
            "Paint turns hide and seek into a skill game",
            """<p>Location still matters. Paint makes location durable. Pose makes paint believable. Timer makes both sides honest. That triangle is the Meccha Chameleon hide and seek identity.</p>""",
        ),
        (
            "Hider principles for the mode",
            """<p>Blend into large surfaces. Avoid hero props everyone checks. Freeze. Use Workshop chaos carefully — weird maps help, but weird movement does not.</p>""",
        ),
        (
            "Seeker principles for the mode",
            """<p>Hunt silhouettes, not vibes. Touch suspicious geometry with a confirm tag. Reset routes when the map goes quiet.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-hide-and-seek-online.html", "Online angle"),
        ("blog-meccha-chameleon-hider-tips.html", "Hider tips"),
        ("blog-meccha-chameleon-prop-hunt.html", "Prop hunt cousin"),
        ("blog-meccha-chameleon-vs-prop-hunt.html", "vs Prop Hunt"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-hide-and-seek-online",
    "Meccha Chameleon hide and seek online",
    "Focus on playing the hide-and-seek fantasy in live online lobbies — etiquette, pace, and public-room tactics. Different from the general online systems article.",
    "online",
    [
        (
            "Online etiquette that keeps lobbies fun",
            """<p>Do not grief the host. Do not stall paint forever in serious rooms. Call maps if your group cares. Leave if the room is dead. Online hide and seek dies when five people treat it like a free-for-all argument.</p>""",
        ),
        (
            "Public-room tactics unique to online play",
            """<p>Expect uneven skill. Expect Workshop maps. Expect streamers. Paint faster. Clear faster. Use private warmups before ranked-feeling public streaks.</p>""",
        ),
        (
            "Tools in online hide and seek",
            """<p>Stream-proof overlay matters if you broadcast. Role tools matter if the lobby is sweaty. Still learn unaided rounds so you understand tells.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-online.html", "Online lobbies"),
        ("blog-meccha-chameleon-hide-and-seek.html", "Mode fantasy"),
        ("blog-stream-proof-overlay.html", "Stream-proof"),
        ("{BUY}", "Buy suite"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-multiplayer",
    "Meccha Chameleon multiplayer",
    "Cover party design, lobby roles, and group formats. Broader than online matchmaking, narrower than full gameplay diary.",
    "online",
    [
        (
            "Multiplayer formats that work",
            """<p>4–8 friends private. Public chaos nights. Streamer vs chat style rooms. Coaching lobbies where one seeker teaches routes. Pick a format before you launch.</p>""",
        ),
        (
            "Role fairness in multiplayer",
            """<p>Rotate seeker duty. Do not trap new players as permanent seeker. Teach paint basics in the first private round. Multiplayer health is social design, not only netcode.</p>""",
        ),
        (
            "Performance in multiplayer sessions",
            """<p>Workshop map spikes hitch groups. Agree on a map pool. Cap crazy mods if someone is on a low-end GPU.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-online.html", "Online systems"),
        ("blog-meccha-chameleon-crossplay.html", "Crossplay"),
        ("blog-meccha-chameleon-workshop-mods.html", "Workshop mods"),
        ("{BUY}", "PC tools"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-steam",
    "Meccha Chameleon Steam",
    "Steam-store and Steam-client focused page: reviews signal, Workshop, launch options mindset — not a generic download checklist.",
    "acquire",
    [
        (
            "How to read the Steam page like a buyer",
            """<p>Check recent reviews for performance and lobby health. Skim screenshots for map variety. Confirm Windows as the target. Ignore review bombs that are about unrelated Steam politics when you can.</p>""",
        ),
        (
            "Steam Workshop reality",
            """<p>Workshop maps define the long-term meta. Subscribe in-client. Never sideload random map EXEs. More in <a href="blog-meccha-chameleon-workshop-mods.html">workshop mods</a> and <a href="blog-meccha-chameleon-maps-download.html">maps download</a>.</p>""",
        ),
        (
            "Steam overlay + streaming",
            """<p>If you stream, test capture. If you use tools, enable stream-proof overlay before going live. Steam overlay alone is not stream-proof for third-party menus.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-download.html", "Download steps"),
        ("blog-meccha-chameleon-review.html", "Review angle"),
        ("blog-meccha-chameleon-workshop-mods.html", "Workshop"),
        ("{BUY}", "Cheats"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-free",
    "Meccha Chameleon free",
    "Own the “free” SERP with honesty: game pricing/Steam reality + why free cheat leaks are malware risk. Do not promise a free full suite.",
    "acquire",
    [
        (
            "What “free” usually means in search",
            """<p>Some people want a free game deal. Some want free cheats. Some want free Workshop content. Separate those intents. Free Workshop maps ≠ free cracked client ≠ free malware “cheat.zip”.</p>""",
        ),
        (
            "Free leaks vs maintained suite",
            """<p>Free leaks break after patches, skip stream-proof, and are the top malware path. A maintained suite with 2–4 hour update targets and CLOUD-DMA option exists for players who want consistency. Compare on <a href="blog-cheat-comparison-2026.html">2026 comparison</a>.</p>""",
        ),
        (
            "Safer free value you can get today",
            """<p>Free practice in private lobbies. Free tips on this blog. Free Workshop browsing inside Steam. Paid is for the game license and optional tools — not for mystery installers.</p>""",
        ),
    ],
    [
        ("blog-cheat-comparison-2026.html", "Comparison"),
        ("blog-meccha-chameleon-download.html", "Safe download"),
        ("blog-meccha-chameleon-tips.html", "Free tips"),
        ("{BUY}", "Paid suite"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-review",
    "Meccha Chameleon review",
    "Editorial review: who should buy the game, strengths, limits, verdict. Not a cheat review — link to comparison for tools.",
    "basics",
    [
        (
            "Verdict up front",
            """<p>Buy Meccha Chameleon if your group likes creative party stealth. Skip it if you want ranked shooters or single-player campaigns. The paint fantasy is the product.</p>""",
        ),
        (
            "Strengths",
            """<p>Readable fantasy. Fast matches. Stream comedy. Workshop longevity. Low rules overhead. High “one more round” energy.</p>""",
        ),
        (
            "Limits",
            """<p>Lobby quality varies. Paint skill gate frustrates some new players. Public rooms can be noisy. Performance depends on map mods.</p>""",
        ),
        (
            "Tools review belongs elsewhere",
            """<p>For cheat software scoring, use <a href="blog-cheat-comparison-2026.html">Best Meccha Chameleon Cheat Review & Comparison 2026</a>. This page reviews the game.</p>""",
        ),
    ],
    [
        ("blog-what-is-meccha-chameleon.html", "What is it"),
        ("blog-cheat-comparison-2026.html", "Cheat comparison"),
        ("blog-meccha-chameleon-steam.html", "Steam"),
        ("{BUY}", "Suite pricing"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-tips",
    "Meccha Chameleon tips",
    "Short, high-density tips list with explanations — actionable, not lore. Sibling pages cover deep hider/seeker strategy.",
    "skill",
    [
        (
            "Ten tips that fix most early losses",
            """<ol>
            <li>Pick the spot before you paint</li>
            <li>Block big colors before details</li>
            <li>Freeze pose — fidgeting is detection</li>
            <li>Avoid the first prop every seeker checks</li>
            <li>Clear rooms in loops as seeker</li>
            <li>Tag after a short confirm</li>
            <li>Leave dead zones earlier than your ego wants</li>
            <li>Warm up privately before public</li>
            <li>One map mastery beats ten map confusion</li>
            <li>Review a recording once a night</li>
            </ol>
            <p>Each tip is simple on purpose. Depth lives in <a href="blog-meccha-chameleon-hider-tips.html">hider tips</a> and <a href="blog-meccha-chameleon-seeker-strategy.html">seeker strategy</a>.</p>""",
        ),
        (
            "Tips vs strategy vs setup guides",
            """<p>Tips = quick list. Strategy = planning patterns. Setup guides = menu/tool configuration. We split them so Google sees distinct documents.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-hider-tips.html", "Hider tips"),
        ("blog-meccha-chameleon-seeker-strategy.html", "Seeker strategy"),
        ("blog-meccha-chameleon-strategy.html", "Overall strategy"),
        ("blog-hider-setup-guide.html", "Hider setup"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-strategy",
    "Meccha Chameleon strategy",
    "Macro strategy: map choice, role plans, adaptation — not micro tips lists.",
    "skill",
    [
        (
            "Build a simple strategy loop",
            """<p>Before the match: map knowledge. During hide: zone plan. During seek: route plan. After match: one note. Strategy is a loop, not a speech.</p>""",
        ),
        (
            "Macro decisions that win nights",
            """<p>Play your strength role early. Ban maps your group hates. Track which Workshop stages destroy your FPS. Swap seeker when tilt spikes. Strategy includes mood management.</p>""",
        ),
        (
            "When tools change strategy",
            """<p>ESP and Instant Tag compress seeker strategy. Perfect Disguise and Blend compress hider strategy. Use them as force multipliers, not as a replacement for map IQ.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-tips.html", "Tips list"),
        ("blog-meccha-chameleon-best-hiding-spots.html", "Hiding spots"),
        ("blog-meccha-chameleon-seeker-strategy.html", "Seeker strategy"),
        ("{BUY}", "Tools"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-painting-game",
    "Meccha Chameleon painting game",
    "Position the title as a painting-skill multiplayer game — creative stealth genre page.",
    "paint",
    [
        (
            "Why “painting game” is the right genre label",
            """<p>Brush control is the core verb. Camouflage is the win condition. Multiplayer pressure is the timer. That is a painting game with hide-and-seek stakes, not a drawing sandbox.</p>""",
        ),
        (
            "Skills that transfer from art to lobbies",
            """<p>Value blocking. Edge control. Color temperature. Pattern scale. Artists adapt fast. Non-artists can still win with simple large-surface blends.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-painting-techniques.html", "Techniques"),
        ("blog-meccha-chameleon-painting-multiplayer.html", "Painting multiplayer"),
        ("blog-meccha-chameleon-artistic-skill-game.html", "Artistic skill angle"),
        ("blog-auto-chameleon-paint.html", "Auto-Chameleon Paint"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-painting-techniques",
    "Meccha Chameleon painting techniques",
    "Technique deep-dive: brush order, edges, patterns — the how-to craft page.",
    "paint",
    [
        (
            "Technique stack that works in lobbies",
            """<ol>
            <li>Sample the dominant surface color</li>
            <li>Block the torso and head first</li>
            <li>Match pattern scale second</li>
            <li>Clean silhouette edges</li>
            <li>Pose into the geometry</li>
            <li>Freeze and stop “improving”</li>
            </ol>""",
        ),
        (
            "Techniques that waste time",
            """<p>Pixel-noodling before blocks. Painting while standing in seeker sightlines. Chasing perfect art on a 40-second clock. Technique includes knowing when to stop.</p>""",
        ),
        (
            "Assists vs technique",
            """<p>Auto-Chameleon Paint and Pixel-Perfect Blend speed consistency. They do not replace spot selection. Read <a href="blog-auto-chameleon-paint.html">Auto-Chameleon Paint</a> and <a href="blog-pixel-perfect-blend.html">Pixel-Perfect Blend</a>.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-painting-game.html", "Painting game"),
        ("blog-meccha-chameleon-camouflage.html", "Camouflage"),
        ("blog-hider-setup-guide.html", "Hider setup"),
        ("{BUY}", "Suite"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-painting-multiplayer",
    "Meccha Chameleon painting multiplayer",
    "How painting skill interacts with multiplayer pressure — social + timer + audience.",
    "paint",
    [
        (
            "Painting under multiplayer pressure",
            """<p>Private practice paints are calm. Public paints are combat. Your technique must shrink under timer and voice noise. Pre-choose zones so brush time is execution, not brainstorming.</p>""",
        ),
        (
            "Team painting nights",
            """<p>Host a private lobby where everyone only practices blends for fifteen minutes. No tags. Then play for real. Painting multiplayer improves when groups rehearse.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-multiplayer.html", "Multiplayer"),
        ("blog-meccha-chameleon-painting-techniques.html", "Techniques"),
        ("blog-meccha-chameleon-chameleon-painting-simulator.html", "Simulator angle"),
        ("{BUY}", "Tools"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-chameleon-painting-simulator",
    "Meccha Chameleon chameleon painting simulator",
    "Long-tail: people comparing it to a simulator/fantasy of becoming a chameleon. Lean into fantasy + practice modes mindset.",
    "paint",
    [
        (
            "Simulator fantasy vs real lobby rules",
            """<p>It feels like a chameleon simulator because identity is color. It is still a competitive lobby game with tags and timers. Hold both truths.</p>""",
        ),
        (
            "How to practice like a simulator",
            """<p>Private lobby. One surface type per round (wood, tile, poster, shadow). Score yourself on whether a friend can find you in ten seconds. That is simulator training inside a multiplayer client.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-painting-game.html", "Painting game"),
        ("blog-meccha-chameleon-artistic-skill-game.html", "Artistic skill"),
        ("blog-meccha-chameleon-camouflage-game.html", "Camouflage game"),
        ("blog-pixel-perfect-blend.html", "Blend tool"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-artistic-skill-game",
    "Meccha Chameleon artistic skill game",
    "Argue the skill ceiling for artists vs casuals — creative competitive game page.",
    "paint",
    [
        (
            "Artistic skill that actually transfers",
            """<p>Color matching, edge hierarchy, and composition under time. You do not need to be a professional illustrator. You need repeatable visual decisions.</p>""",
        ),
        (
            "If you are not “artistic”",
            """<p>Use large flat surfaces. Avoid busy posters until you improve. Auto-Chameleon Paint helps consistency. Spot selection beats brush talent for many rounds.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-painting-techniques.html", "Techniques"),
        ("blog-auto-chameleon-paint.html", "Auto paint"),
        ("blog-meccha-chameleon-review.html", "Game review"),
        ("{BUY}", "Suite"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-camouflage",
    "Meccha Chameleon camouflage",
    "Mechanic page: how camouflage works in-game — colors, pose, lock concepts.",
    "paint",
    [
        (
            "Camouflage components",
            """<p>Color match. Pattern scale. Silhouette break. Pose. Stillness. Miss one and seekers get a free read. Camouflage is a system, not a filter.</p>""",
        ),
        (
            "Locking camouflage under pressure",
            """<p>Perfect Disguise style locks matter when paint would otherwise break mid-round. Freeze Pose Timer supports the stance. Details on the buy page and <a href="blog-hider-setup-guide.html">hider setup</a>.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-camouflage-game.html", "Camouflage game genre"),
        ("blog-pixel-perfect-blend.html", "Pixel-Perfect Blend"),
        ("blog-meccha-chameleon-best-hiding-spots.html", "Hiding spots"),
        ("{BUY}", "Features"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-camouflage-game",
    "Meccha Chameleon camouflage game",
    "Genre page: camouflage games as a category and where Meccha Chameleon sits — different from the mechanic page.",
    "paint",
    [
        (
            "Camouflage games as a genre",
            """<p>Some titles hide you with props. Some with lighting. Meccha Chameleon hides you with paint authorship. That is why “camouflage game” searchers bounce between prop hunt and this title.</p>""",
        ),
        (
            "What makes this camouflage game sticky",
            """<p>Player-authored blends create infinite variety. Workshop maps refresh the canvas. Dual roles keep the fantasy fair.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-camouflage.html", "Camouflage mechanic"),
        ("blog-meccha-chameleon-vs-prop-hunt.html", "vs Prop Hunt"),
        ("blog-what-is-meccha-chameleon.html", "What is it"),
        ("{BUY}", "Tools"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-prop-hunt",
    "Meccha Chameleon prop hunt",
    "Explain prop-hunt similarities without being the head-to-head comparison page.",
    "modes",
    [
        (
            "Shared DNA with prop hunt",
            """<p>Hiders blend. Seekers hunt. Timers matter. Comedy clips matter. If you like prop hunt lobbies, the fantasy overlaps.</p>""",
        ),
        (
            "Where it stops being prop hunt",
            """<p>Paint authorship replaces prop possession. That skill gap is the product. For a full head-to-head, use <a href="blog-meccha-chameleon-vs-prop-hunt.html">vs Prop Hunt</a>.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-vs-prop-hunt.html", "Direct comparison"),
        ("blog-meccha-chameleon-hide-and-seek.html", "Hide & seek"),
        ("blog-meccha-chameleon-gameplay.html", "Gameplay"),
        ("{BUY}", "Suite"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-vs-prop-hunt",
    "Meccha Chameleon vs prop hunt",
    "Comparison table intent — pick a winner by group type.",
    "modes",
    [
        (
            "Quick comparison",
            """<div class="table-wrap"><table>
            <thead><tr><th>Factor</th><th>Meccha Chameleon</th><th>Typical Prop Hunt</th></tr></thead>
            <tbody>
            <tr><td>Hide method</td><td>Paint body to environment</td><td>Become a prop mesh</td></tr>
            <tr><td>Skill focus</td><td>Color, edges, pose</td><td>Prop choice, spot choice</td></tr>
            <tr><td>Comedy</td><td>Paint fails / perfect blends</td><td>Prop trolling</td></tr>
            <tr><td>Workshop</td><td>Map canvases</td><td>Maps + props vary</td></tr>
            </tbody></table></div>""",
        ),
        (
            "Which should your group play?",
            """<p>Choose Meccha Chameleon if you want artistic stealth. Choose classic prop hunt if you want instant prop jokes with less brush work. Many groups play both on different nights.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-prop-hunt.html", "Prop hunt overlap"),
        ("blog-meccha-chameleon-review.html", "Game review"),
        ("blog-meccha-chameleon-painting-game.html", "Painting game"),
        ("{BUY}", "PC tools"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-indie-game",
    "Meccha Chameleon indie game",
    "Indie success / industry angle — Steam breakout narrative.",
    "creators",
    [
        (
            "Why this indie hit landed",
            """<p>Clear fantasy. Low rules. High shareability. Workshop legs. Creator proximity. Indie hits need a sentence people can repeat — “paint yourself to hide” is that sentence.</p>""",
        ),
        (
            "What indie scale means for players",
            """<p>Faster vibe shifts. Patch cadence that matters. Enforcement that may be lighter than AAA kernel stacks. Read the <a href="{GUIDE}">guide</a>.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-japanese-game.html", "Japanese game"),
        ("blog-meccha-chameleon-lemorion.html", "Lemorion"),
        ("blog-meccha-chameleon-haganeiro.html", "Haganeiro"),
        ("blog-meccha-chameleon-steam.html", "Steam"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-japanese-game",
    "Meccha Chameleon Japanese game",
    "Origin/culture/creator geography intent — not a generic indie page.",
    "creators",
    [
        (
            "Japanese indie roots",
            """<p>Players search this when they want origin context. Lemorion_1224 and Haganeiro sit in that Japanese indie craft lane — playful systems, strong visual jokes, Steam distribution.</p>""",
        ),
        (
            "Why origin matters for expectations",
            """<p>Expect inventive party design over military sim polish. Expect community maps. Expect English lobby mix even with Japanese creation roots.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-indie-game.html", "Indie angle"),
        ("blog-meccha-chameleon-lemorion.html", "Lemorion_1224"),
        ("blog-meccha-chameleon-haganeiro.html", "Haganeiro"),
        ("blog-what-is-meccha-chameleon.html", "Overview"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-lemorion",
    "Meccha Chameleon Lemorion_1224",
    "Creator entity page for Lemorion_1224 — credits, why people search the name.",
    "creators",
    [
        (
            "Why people search Lemorion_1224",
            """<p>Credits, curiosity, and “who made this” rabbit holes. Creator searches are entity SEO. Keep facts stable and link siblings instead of inventing biographies.</p>""",
        ),
        (
            "What players should do next",
            """<p>Play the Steam build. Follow official channels the developers use. Use this site for lobby guides and tools — we are not the developer.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-haganeiro.html", "Haganeiro"),
        ("blog-meccha-chameleon-japanese-game.html", "Japanese game"),
        ("blog-what-is-meccha-chameleon.html", "Game overview"),
        ("{BUY}", "Tools"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-haganeiro",
    "Meccha Chameleon Haganeiro",
    "Creator entity page for Haganeiro — complementary to Lemorion page.",
    "creators",
    [
        (
            "Haganeiro in the credits story",
            """<p>Searchers want the other half of the indie credit line. Keep this page entity-focused. Avoid duplicating the full game tutorial — link out.</p>""",
        ),
        (
            "Respect boundaries",
            """<p>Do not harass creators. Do not claim affiliation. This site covers player tools and guides only.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-lemorion.html", "Lemorion_1224"),
        ("blog-meccha-chameleon-indie-game.html", "Indie game"),
        ("blog-meccha-chameleon-japanese-game.html", "Japanese game"),
        ("{HOME}", "Home"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-ranking-system",
    "Meccha Chameleon ranking system",
    "Clarify informal competition vs formal ranked ladder — set expectations.",
    "online",
    [
        (
            "Is there a hard ranked ladder?",
            """<p>Treat most public play as informal ranking: win streaks, reputation in friend groups, streamer lobbies. If the game adds heavier ranked systems later, update this page — do not invent a ladder that is not clearly shipped.</p>""",
        ),
        (
            "How to “rank up” socially anyway",
            """<p>Master two maps. Record seeker clear times. Reduce hider fidget. Track personal stats in a note. Social ranking is real even without Elo UI.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-online.html", "Online"),
        ("blog-meccha-chameleon-strategy.html", "Strategy"),
        ("blog-meccha-chameleon-multiplayer.html", "Multiplayer"),
        ("{GUIDE}", "Guide"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-hider-tips",
    "Meccha Chameleon hider tips",
    "Hider-only micro tips and habits — not seeker strategy.",
    "skill",
    [
        (
            "Hider tip stack",
            """<ul>
            <li>Pre-select two backup spots</li>
            <li>Paint torso/head before jewelry details</li>
            <li>Break human silhouette with pose</li>
            <li>Stop painting 10 seconds early to freeze</li>
            <li>Never “adjust” when a seeker enters the room</li>
            <li>Prefer large quiet surfaces over famous props</li>
            </ul>""",
        ),
        (
            "Advanced hider habits",
            """<p>Scout with free camera tools only if you use the suite — otherwise walk the map as seeker first. Learn where seekers naturally look. Hide in the second place, not the first.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-best-hiding-spots.html", "Hiding spots"),
        ("blog-hider-setup-guide.html", "Hider setup"),
        ("blog-meccha-chameleon-tips.html", "General tips"),
        ("blog-pixel-perfect-blend.html", "Blend"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-best-hiding-spots",
    "Meccha Chameleon best hiding spots",
    "Spot selection framework + examples — evergreen method, not a fake map dump.",
    "skill",
    [
        (
            "A framework beats a static spot list",
            """<p>Maps and Workshop stages change. Frameworks survive. Score spots on: traffic, contrast, pattern scale, escape uselessness (you want freeze, not escape), and seeker camera habits.</p>""",
        ),
        (
            "High-percentage spot types",
            """<ul>
            <li>Large flat walls with soft patterns</li>
            <li>Floor blends in low-traffic corners</li>
            <li>Shadowed geometry where outlines die</li>
            <li>Clutter zones where eyes skip</li>
            </ul>
            <p>Low-percentage: meme props, doorways, under-seeker-spawn gimmicks.</p>""",
        ),
        (
            "Scouting workflow",
            """<p>Play one seeker round only to learn sightlines. Note three spots. Practice painting them. Rotate so you are not predictable.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-hider-tips.html", "Hider tips"),
        ("blog-meccha-chameleon-maps-download.html", "Maps"),
        ("blog-super-speed-match-tools.html", "Match tools / free cam"),
        ("{BUY}", "Suite"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-seeker-strategy",
    "Meccha Chameleon seeker strategy",
    "Seeker-only planning and clear patterns.",
    "skill",
    [
        (
            "Seeker clear patterns",
            """<p>Pick a loop. Clear high furniture. Sweep floors. Recheck after noise. Do not zigzag the whole map every ten seconds. Patterned clears beat panic.</p>""",
        ),
        (
            "Reading paint tells",
            """<p>Wrong scale patterns. Human shoulders. Micro-movement. Color that is “almost.” Instant Tag helps closes; strategy still starts with reading.</p>""",
        ),
        (
            "Tool-assisted seeker plan",
            """<p>Heat Vision / ESP, minimap positions, Super Speed (1–5×), Reveal All Hiders, freeze hider — all listed on the buy page. Setup details: <a href="blog-seeker-esp-setup-guide.html">seeker ESP setup</a>.</p>""",
        ),
    ],
    [
        ("blog-seeker-esp-setup-guide.html", "ESP setup"),
        ("blog-heat-vision-esp.html", "Heat Vision"),
        ("blog-instant-tag.html", "Instant Tag"),
        ("blog-meccha-chameleon-strategy.html", "Macro strategy"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-character-customization",
    "Meccha Chameleon character customization",
    "Customization vs camouflage painting — clarify what players can change.",
    "basics",
    [
        (
            "Customization vs camouflage",
            """<p>People search customization expecting skins menus. In Meccha Chameleon, the meaningful “custom look” is often the paint you author each round. Do not confuse cosmetic menus with camouflage performance.</p>""",
        ),
        (
            "What to optimize anyway",
            """<p>Clarity of silhouette when unpainted. Comfort of camera. Any cosmetics that make paint harder should be avoided for serious lobbies.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-camouflage.html", "Camouflage"),
        ("blog-meccha-chameleon-painting-techniques.html", "Painting techniques"),
        ("blog-what-is-meccha-chameleon.html", "Overview"),
        ("{BUY}", "Tools"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-maps-download",
    "Meccha Chameleon maps download",
    "Workshop/maps acquisition the safe way — fight malware map pack SERPs.",
    "acquire",
    [
        (
            "Safe maps download path",
            """<p>Use Steam Workshop subscriptions inside the client. That is the maps download. Avoid “100 maps pack.rar” sites. Those pages exist to push malware.</p>""",
        ),
        (
            "Curating a map pool",
            """<p>Subscribe to a small set your group likes. Unsubscribe junk that tanks FPS. Name your favorites. Map chaos without curation ruins nights.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-workshop-mods.html", "Workshop mods"),
        ("blog-meccha-chameleon-download.html", "Game download"),
        ("blog-meccha-chameleon-best-hiding-spots.html", "Spots framework"),
        ("{BUY}", "Suite"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-workshop-mods",
    "Meccha Chameleon workshop mods",
    "Mods/Workshop culture, performance, etiquette.",
    "acquire",
    [
        (
            "Workshop mods that help vs hurt",
            """<p>Help: clear canvases, fun party maps, stable performance. Hurt: unoptimized geometry, broken spawns, joke maps that softlock rounds. Vote with your subscribe button.</p>""",
        ),
        (
            "Mod etiquette in public rooms",
            """<p>Host maps your players can load. Warn for huge downloads. Do not force experimental mods on newcomers during their first night.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-maps-download.html", "Maps download"),
        ("blog-meccha-chameleon-steam.html", "Steam"),
        ("blog-meccha-chameleon-multiplayer.html", "Multiplayer"),
        ("{HOME}", "Home"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-crossplay",
    "Meccha Chameleon crossplay",
    "Hard truth page: plan around Steam PC; do not promise fantasy crossplay.",
    "online",
    [
        (
            "Practical crossplay answer",
            """<p>Plan your friend group around the Windows Steam build. Do not assume consoles or phones share the same lobbies. If that changes officially later, update this page with a dated note.</p>""",
        ),
        (
            "If your group is split across devices",
            """<p>Pick one platform and meet there. Cloud PC can be a bridge for some players. Native Windows remains the simplest path for tools and Workshop.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-mobile-version.html", "Mobile"),
        ("blog-meccha-chameleon-online.html", "Online"),
        ("blog-meccha-chameleon-multiplayer.html", "Multiplayer"),
        ("{BUY}", "PC suite"),
    ],
)

auto_pack(
    "blog-meccha-chameleon-mobile-version",
    "Meccha Chameleon mobile version",
    "Expectation-setting: mobile searchers get honest PC-first guidance.",
    "online",
    [
        (
            "Mobile search intent vs reality",
            """<p>Many searchers hope for a phone port. Treat Steam PC as the real multiplayer product today. If an official mobile client appears, require a primary-source link before changing this advice.</p>""",
        ),
        (
            "What mobile players can do now",
            """<p>Watch streams. Join friend groups on PC later. Do not install sketchy “mobile APK Meccha Chameleon” files from random sites.</p>""",
        ),
    ],
    [
        ("blog-meccha-chameleon-crossplay.html", "Crossplay"),
        ("blog-meccha-chameleon-download.html", "PC download"),
        ("blog-meccha-chameleon-steam.html", "Steam"),
        ("{HOME}", "Home"),
    ],
)

# Feature / safety / setup packs
auto_pack(
    "blog-pixel-perfect-blend",
    "Pixel-Perfect Blend",
    "Feature explainer for Pixel-Perfect Blend camo — how it helps hiders, how to use, limits.",
    "features",
    [
        (
            "What Pixel-Perfect Blend does",
            """<p>It locks hider camo toward stage colors so your silhouette disappears into walls, props, and paint zones faster and more consistently than rushed manual brushing.</p>""",
        ),
        (
            "Best use cases",
            """<p>Public lobbies with short paint windows. Patterned floors. Walls with subtle gradients. Pair with Perfect Disguise and Freeze Pose Timer.</p>""",
        ),
        (
            "What it does not do",
            """<p>It does not choose a smart spot for you. Bad location still fails. Technique still matters — see painting techniques.</p>""",
        ),
    ],
    [
        ("blog-auto-chameleon-paint.html", "Auto-Chameleon Paint"),
        ("blog-hider-setup-guide.html", "Hider setup"),
        ("blog-meccha-chameleon-camouflage.html", "Camouflage"),
        ("{BUY}", "All features"),
    ],
)

auto_pack(
    "blog-auto-chameleon-paint",
    "Auto-Chameleon Paint",
    "Feature explainer: environment color match painting assist.",
    "features",
    [
        (
            "What Auto-Chameleon Paint does",
            """<p>Environment color match paints you automatically so blend setups take less manual brush spam — critical in short lobby timers.</p>""",
        ),
        (
            "Settings mindset",
            """<p>Use it to win time, then finish edges and pose manually if needed. Auto paint + bad pose still looks human.</p>""",
        ),
    ],
    [
        ("blog-pixel-perfect-blend.html", "Pixel-Perfect Blend"),
        ("blog-meccha-chameleon-painting-techniques.html", "Techniques"),
        ("blog-hider-setup-guide.html", "Hider setup"),
        ("{BUY}", "Buy"),
    ],
)

auto_pack(
    "blog-heat-vision-esp",
    "Heat Vision / ESP",
    "Seeker vision feature explainer — through-wall reads + minimap synergy.",
    "features",
    [
        (
            "What Heat Vision / ESP does",
            """<p>See hiders through walls during seeker rounds. Pair with hider positions on minimap for route planning instead of random wandering.</p>""",
        ),
        (
            "Playstyle tips",
            """<p>Do not tunnel vision the ESP blob. Clear the room anyway so you learn tells for unaided play and look human on stream.</p>""",
        ),
    ],
    [
        ("blog-seeker-esp-setup-guide.html", "ESP setup"),
        ("blog-instant-tag.html", "Instant Tag"),
        ("blog-meccha-chameleon-seeker-strategy.html", "Seeker strategy"),
        ("{BUY}", "Features"),
    ],
)

auto_pack(
    "blog-instant-tag",
    "Instant Tag",
    "Combat closer feature: Instant Tag + one-hit through obstacles context.",
    "features",
    [
        (
            "What Instant Tag is for",
            """<p>Close seeker rounds before the timer dies. One-hit tag through obstacles helps when hiders cling to cover. Still confirm enough to avoid looking like pure chaos in voice lobbies if you care.</p>""",
        ),
        (
            "Pairings",
            """<p>Super Speed (1–5×) for rotates. Heat Vision for finds. Reveal All Hiders when the lobby is ending and you need the sweep.</p>""",
        ),
    ],
    [
        ("blog-heat-vision-esp.html", "Heat Vision"),
        ("blog-super-speed-match-tools.html", "Match tools"),
        ("blog-seeker-esp-setup-guide.html", "Seeker setup"),
        ("{BUY}", "Buy"),
    ],
)

auto_pack(
    "blog-super-speed-match-tools",
    "Super Speed & match tools",
    "Match control tools: speed, timer freeze, map reveal, free camera/noclip.",
    "features",
    [
        (
            "Tool list on this page",
            """<p>Super Speed (1–5×) for seeker closes. Match timer freeze. Full-map reveal. Free camera / noclip for scouting hiding spots. Reveal All Hiders and freeze hider in place when you need hard control.</p>""",
        ),
        (
            "Responsible lobby use",
            """<p>Private practice is the place to learn free camera scouting. In public, decide your own comfort. Feature availability stays as listed on the buy page.</p>""",
        ),
    ],
    [
        ("blog-instant-tag.html", "Instant Tag"),
        ("blog-meccha-chameleon-best-hiding-spots.html", "Hiding spots"),
        ("blog-cloud-dma-aws.html", "CLOUD-DMA"),
        ("{BUY}", "Full list"),
    ],
)

auto_pack(
    "blog-stream-proof-overlay",
    "Stream-proof overlay",
    "Streaming safety feature page — OBS/Discord invisibility.",
    "features",
    [
        (
            "Why stream-proof exists",
            """<p>Menus leaking on stream is how accounts get piled on. Stream-proof overlay mode is designed to stay invisible to OBS, Discord, and major broadcast software.</p>""",
        ),
        (
            "Streamer checklist",
            """<ol>
            <li>Enable stream-proof before going live</li>
            <li>Test a private recording</li>
            <li>Hide loader windows from capture</li>
            <li>Keep alerts from flashing menu hotkeys</li>
            </ol>""",
        ),
    ],
    [
        ("blog-cloud-dma-aws.html", "CLOUD-DMA"),
        ("blog-cheat-comparison-2026.html", "Comparison"),
        ("{GUIDE}", "Guide"),
        ("{BUY}", "Buy"),
    ],
)

auto_pack(
    "blog-cloud-dma-aws",
    "CLOUD-DMA AWS",
    "Safety/delivery explainer: CLOUD-DMA option hosted on AWS — same suite, not a second product.",
    "safety",
    [
        (
            "What CLOUD-DMA (AWS) means here",
            """<p>CLOUD-DMA is an optional delivery path that runs on AWS. It is part of the same Meccha Chameleon product suite — not a separate unrelated cheat you pick instead of the features.</p>""",
        ),
        (
            "When players enable it",
            """<p>When they want external cloud processing alongside the loader workflow. Requirements on Windows still apply. Support can walk toggles.</p>""",
        ),
        (
            "What is not claimed",
            """<p>No separate HWID spoofer product is advertised. Stick to the locked buy-page list.</p>""",
        ),
    ],
    [
        ("blog-stream-proof-overlay.html", "Stream-proof"),
        ("{GUIDE}", "Anti-cheat guide"),
        ("blog-cheat-comparison-2026.html", "Comparison"),
        ("{BUY}", "Pricing"),
    ],
)

auto_pack(
    "blog-hider-setup-guide",
    "Hider setup guide",
    "Configuration guide for hider modules — settings order and presets mindset.",
    "setup",
    [
        (
            "Recommended enable order",
            """<ol>
            <li>Pixel-Perfect Blend</li>
            <li>Auto-Chameleon Paint</li>
            <li>Auto-Pose Snapping</li>
            <li>Perfect Disguise</li>
            <li>Freeze Pose Timer</li>
            <li>Infinite Stamina</li>
            </ol>""",
        ),
        (
            "Practice routine",
            """<p>Private lobby. Two maps. Ten hider rounds. Change only one setting between rounds so you learn cause and effect.</p>""",
        ),
    ],
    [
        ("blog-seeker-esp-setup-guide.html", "Seeker setup"),
        ("blog-pixel-perfect-blend.html", "Blend"),
        ("blog-meccha-chameleon-hider-tips.html", "Hider tips"),
        ("{BUY}", "Features"),
    ],
)

auto_pack(
    "blog-seeker-esp-setup-guide",
    "Seeker ESP setup guide",
    "Configuration guide for seeker vision and closers.",
    "setup",
    [
        (
            "Recommended enable order",
            """<ol>
            <li>Heat Vision / ESP</li>
            <li>Hider minimap positions</li>
            <li>Instant Tag + one-hit through obstacles</li>
            <li>Super Speed (start low, raise carefully)</li>
            <li>Reveal / freeze tools when needed</li>
            <li>Stream-proof if you broadcast</li>
            </ol>""",
        ),
        (
            "Public vs private presets",
            """<p>Private can be louder. Public may want subtler movement even with ESP so rounds still feel like reads. Your call — features stay available either way.</p>""",
        ),
    ],
    [
        ("blog-hider-setup-guide.html", "Hider setup"),
        ("blog-heat-vision-esp.html", "Heat Vision"),
        ("blog-meccha-chameleon-seeker-strategy.html", "Seeker strategy"),
        ("{BUY}", "Buy"),
    ],
)

auto_pack(
    "blog-cheat-comparison-2026",
    "Meccha Chameleon cheat comparison 2026",
    "Commercial comparison against free leaks and generic paid menus — table + decision.",
    "commercial",
    [
        (
            "Comparison criteria we allow",
            """<p>Update speed, hider depth, seeker depth, stream-proof, CLOUD-DMA option, support responsiveness, price. We do not invent features missing from the buy page.</p>""",
        ),
        (
            "Decision rule",
            """<p>Pick Monthly ($35) to test a season. Pick Lifetime ($150) if you play weekly and want permanent access + future updates. Feature parity is identical.</p>""",
        ),
    ],
    [
        ("{BUY}", "Buy page"),
        ("blog-cloud-dma-aws.html", "CLOUD-DMA"),
        ("blog-stream-proof-overlay.html", "Stream-proof"),
        ("blog-meccha-chameleon-free.html", "Free reality"),
    ],
)


def render_sections(sections: list[tuple[str, str]]) -> str:
    parts = []
    for h2, html in sections:
        parts.append(f"<h2>{h2}</h2>\n{html}")
    return "\n".join(parts)


def render_faq(faqs: list[tuple[str, str]]) -> str:
    items = []
    for q, a in faqs:
        items.append(
            f"""<div class="faq-item" style="margin:0.75rem 0;padding:1rem;border:1px solid var(--border);border-radius:12px;">
            <h3 style="margin:0 0 0.5rem;font-size:1.05rem;">{q}</h3>
            <p style="margin:0;">{a}</p>
            </div>"""
        )
    return "<h2>FAQ</h2>\n" + "\n".join(items)


def render_related(related: list[tuple[str, str]]) -> str:
    lis = []
    for href, label in related:
        href = href.replace("{BUY}", BUY).replace("{GUIDE}", GUIDE).replace("{HOME}", HOME).replace("{BLOG}", BLOG)
        lis.append(f'<li><a href="{href}">{label}</a></li>')
    return "<h2>Keep reading in this cluster</h2>\n<ul>\n" + "\n".join(lis) + "\n</ul>"


def faq_schema(faqs: list[tuple[str, str]]) -> str:
    entities = []
    for q, a in faqs:
        a_clean = re.sub(r"<[^>]+>", "", a)
        entities.append(
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a_clean},
            }
        )
    payload = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    return '<script type="application/ld+json">' + json.dumps(payload, ensure_ascii=False) + "</script>"


def build_prose(slug: str) -> tuple[str, str]:
    data = PACKS[slug]
    intent = f"<p class=\"cluster-intent\"><strong>Page intent:</strong> {data['intent']}</p>"
    body = render_sections(data["sections"])
    body = (
        body.replace("{BUY}", BUY)
        .replace("{GUIDE}", GUIDE)
        .replace("{HOME}", HOME)
        .replace("{BLOG}", BLOG)
        .replace("{FEATURES}", FEATURES)
    )
    faq = render_faq(data["faqs"])
    rel = render_related(data["related"])
    eeat = """
    <aside class="eeat-box" style="margin:2rem 0;padding:1.25rem;border:1px solid var(--border);border-radius:14px;background:rgba(168,85,247,.06);">
      <h2 style="margin-top:0;">How we keep this accurate</h2>
      <p>Feature claims always match the <a href="meccha-chameleon-cheats.html#features">buy page list</a>. Anti-cheat context is maintained on the <a href="guide.html">guide</a>. When Meccha Chameleon patches, tool notes are updated on a 2–4 hour target window.</p>
      <p><strong>Authoring:</strong> Meccha Chameleon Cheats editorial · Updated for 2026 lobby meta · Not affiliated with the game developers.</p>
    </aside>
    """
    prose = intent + body + eeat + faq + rel
    schema = faq_schema(data["faqs"])
    return prose, schema


AUTHOR_IMG_NOTE = """Screenshot via <a href="https://za.ign.com/meccha-chameleon/235012/meccha-chameleon-steam-screenshots" rel="noopener noreferrer">IGN Meccha Chameleon gallery</a> (image courtesy of lemorion_1224). One contextual image only — no screenshot spam."""


def process_file(path: Path) -> None:
    slug = path.stem
    if slug not in PACKS:
        print("skip (no pack):", slug)
        return
    html = path.read_text(encoding="utf-8")

    # Remove galleries and inline shot figures (image padding)
    html = re.sub(r'<div class="article-gallery">.*?</div>\s*', "", html, flags=re.S)
    html = re.sub(r"<figure class=\"inline-shot\">.*?</figure>", "", html, flags=re.S)

    prose, schema = build_prose(slug)
    # Replace prose inner HTML
    html = re.sub(
        r'(<div class="prose">)(.*?)(</div>\s*<div class="article-cta">)',
        r"\1\n" + prose + r"\n      \3",
        html,
        count=1,
        flags=re.S,
    )

    # Improve credit line under hero if present
    html = re.sub(
        r'(<p class="article-img-credit">).*?(</p>)',
        r"\1" + AUTHOR_IMG_NOTE + r"\2",
        html,
        count=1,
        flags=re.S,
    )

    # Inject FAQ schema before </head> if not present
    if "FAQPage" not in html:
        html = html.replace("</head>", schema + "\n</head>", 1)

    # Ensure analytics config scripts present
    if "site-config.js" not in html:
        html = html.replace(
            '<script src="js/main.js" defer></script>',
            '<script src="js/site-config.js"></script>\n  <script src="js/analytics.js" defer></script>\n  <script src="js/main.js" defer></script>',
            1,
        )

    # Bump wordiness check later
    path.write_text(html, encoding="utf-8")
    print("thickened", slug)


def inject_analytics_all():
    for path in ROOT.glob("*.html"):
        if path.name in {"seo-setup.html", "qa-checklist.html"}:
            continue
        html = path.read_text(encoding="utf-8")
        if "site-config.js" in html:
            continue
        if 'script src="js/main.js"' in html:
            html = html.replace(
                '<script src="js/main.js" defer></script>',
                '<script src="js/site-config.js"></script>\n  <script src="js/analytics.js" defer></script>\n  <script src="js/main.js" defer></script>',
                1,
            )
            path.write_text(html, encoding="utf-8")


def update_robots():
    robots = ROOT / "robots.txt"
    text = """User-agent: *
Allow: /
Disallow: /scripts/
Disallow: /seo-setup.html
Disallow: /qa-checklist.html
Disallow: /backlink-playbook.html

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

Sitemap: https://mecchahacks.com/sitemap.xml
Host: mecchahacks.com
"""
    robots.write_text(text, encoding="utf-8")


def main():
    for path in sorted(ROOT.glob("blog-*.html")):
        process_file(path)
    inject_analytics_all()
    update_robots()
    print("packs:", len(PACKS))


if __name__ == "__main__":
    main()
