# -*- coding: utf-8 -*-
"""Generate 30 SEO/backlink Meccha Chameleon blog posts with IGN images."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

IGN = [
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

BUY = "https://mecchahacks.com/meccha-chameleon-cheats"
HOME = "https://mecchahacks.com/"
GUIDE = "https://mecchahacks.com/guide"
BLOG = "https://mecchahacks.com/blog"
PURCHASE = "https://zadeyo.com/go/SAKINA?to=%2Fproducts%2Fmeccha-chameleon-cheats"
SUPPORT = "https://zadeyo.com/support"
LOGO = "https://zadeyo.com/_next/image?url=%2Frt-removebg-preview.png&w=64&q=75"
IGN_SLIDES = "https://za.ign.com/meccha-chameleon/235012/meccha-chameleon-steam-screenshots"

POSTS = [
    {
        "slug": "blog-what-is-meccha-chameleon",
        "cat": "guides",
        "date": "2026-06-15",
        "label": "Jun 15, 2026",
        "title": "What Is Meccha Chameleon? The Hide and Seek Paint Game Explained",
        "meta_title": "What Is Meccha Chameleon? Game Explained",
        "meta_desc": "Meccha Chameleon is a Steam hide-and-seek painting game. Learn how hiders, seekers, and camouflage work — plus where to get tools.",
        "h1": "What Is Meccha Chameleon? The Hide and Seek Paint Game Explained",
        "lead": "If you keep seeing Meccha Chameleon clips and wonder what the fuss is, here is the simple version. It is a multiplayer hide-and-seek game where you paint your body to disappear into the map.",
        "kw": "Meccha Chameleon game",
        "body": """
        <h2>The basic loop</h2>
        <p>You join a lobby. Half the players hide. Half seek. Hiders start as plain white figures, then paint themselves to match walls, floors, props, and weird Workshop maps. Seekers hunt before the timer runs out.</p>
        <p>That paint twist is why people call it a Meccha Chameleon painting game instead of a normal prop hunt clone. Spotting someone is half art critique, half shotgun chase.</p>
        <h2>Who made it</h2>
        <p>It comes from Japanese indie creators Lemorion_1224 and Haganeiro. Small team. Fast build. Huge Steam numbers. No big marketing push — just shareable Meccha Chameleon gameplay.</p>
        <h2>Where players go next</h2>
        <p>Most people start on Steam, then look up Meccha Chameleon tips once public lobbies get sweaty. If you want the full tool suite for both roles, check the <a href="{BUY}">Meccha Chameleon cheats buy page</a> on mecchahacks.com. For how online enforcement works, read the <a href="{GUIDE}">anti-cheat guide</a>.</p>
        <h2>Quick takeaway</h2>
        <p>Meccha Chameleon online is social camouflage. Hide with paint. Seek with eyes. Laugh when someone blends into a fridge for four minutes straight.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-online",
        "cat": "guides",
        "date": "2026-06-18",
        "label": "Jun 18, 2026",
        "title": "How Meccha Chameleon Online Lobbies Actually Work",
        "meta_title": "Meccha Chameleon Online Lobbies Guide",
        "meta_desc": "How Meccha Chameleon online matchmaking works, what to expect in public lobbies, and how to play smarter with friends.",
        "h1": "How Meccha Chameleon Online Lobbies Actually Work",
        "lead": "Meccha Chameleon online is where the game lives. There is no deep single-player campaign — the fun is other people failing to see you, or tagging you mid-paint.",
        "kw": "Meccha Chameleon online",
        "body": """
        <h2>Public vs private</h2>
        <p>Public lobbies are loud, chaotic, and full of Workshop maps. Private lobbies are better for friends and cleaner Meccha Chameleon multiplayer nights. If a public room feels broken, leave and requeue.</p>
        <h2>Matchmaking note</h2>
        <p>Online sessions lean on Epic Online Services for lobbies. That is account and matchmaking glue — not a heavy kernel anti-cheat. We break that down on the <a href="{GUIDE}">Meccha Chameleon guide</a>.</p>
        <h2>Staying useful in public queues</h2>
        <p>Learn map flow. Do not stand in the open while painting. If you use tools, keep presets subtle — see <a href="blog-hider-setup-guide.html">hider setup</a> and <a href="blog-seeker-esp-setup-guide.html">seeker ESP setup</a>.</p>
        <h2>Want full lobby tools?</h2>
        <p>Role presets, Heat Vision ESP, and Instant Tag are listed on <a href="{BUY}">mecchahacks.com Meccha Chameleon cheats</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-download",
        "cat": "guides",
        "date": "2026-06-20",
        "label": "Jun 20, 2026",
        "title": "Meccha Chameleon Download Guide — Steam Install Made Simple",
        "meta_title": "Meccha Chameleon Download — Steam Install",
        "meta_desc": "How to download Meccha Chameleon on PC through Steam, what you need, and what to avoid when searching for free files.",
        "h1": "Meccha Chameleon Download Guide — Steam Install Made Simple",
        "lead": "Searching “Meccha Chameleon download” usually means one thing: you want it on PC fast. The clean path is Steam. Random free installers are where people get burned.",
        "kw": "Meccha Chameleon download",
        "body": """
        <h2>Official download steps</h2>
        <ol>
          <li>Open Steam and create or log into an account</li>
          <li>Search for Meccha Chameleon</li>
          <li>Buy or claim the game listing</li>
          <li>Hit Install and wait for the download</li>
          <li>Launch and join a lobby</li>
        </ol>
        <h2>System basics</h2>
        <p>It is a Windows-first multiplayer title. Keep GPU drivers current if paint and Workshop maps stutter. Windows 10 and 11 both run it fine for most players.</p>
        <h2>About “free download” sites</h2>
        <p>Third-party Meccha Chameleon free download pages often package malware. Stick to Steam for the game client. If you want maintained lobby tools later, use a known suite from <a href="{HOME}">mecchahacks.com</a> instead of mystery EXEs.</p>
        <h2>After install</h2>
        <p>Jump into a private lobby first. Learn paint controls. Then read our <a href="blog-meccha-chameleon-tips.html">Meccha Chameleon tips</a> before diving into ranked-feeling public chaos.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-gameplay",
        "cat": "guides",
        "date": "2026-06-22",
        "label": "Jun 22, 2026",
        "title": "Meccha Chameleon Gameplay — What a Real Match Feels Like",
        "meta_title": "Meccha Chameleon Gameplay Explained",
        "meta_desc": "A plain-English look at Meccha Chameleon gameplay for hiders and seekers, from first paint stroke to final tag.",
        "h1": "Meccha Chameleon Gameplay — What a Real Match Feels Like",
        "lead": "Meccha Chameleon gameplay is simple to start and hard to master. One round you are art. The next round you are a panicked seeker checking every pillow.",
        "kw": "Meccha Chameleon gameplay",
        "body": """
        <h2>Hider side</h2>
        <p>Pick a spot. Paint. Pose. Freeze. Good hiders think about light, silhouette, and how long a seeker will stare. Bad hiders paint for five seconds and hope.</p>
        <h2>Seeker side</h2>
        <p>Walk rooms with purpose. Check odd corners. Listen for movement. Tag when you are sure. Rushing every shadow wastes the timer.</p>
        <h2>Why it clips so well</h2>
        <p>Paint mistakes are funny. Perfect blends are scary. That mix is why Meccha Chameleon gameplay spreads on streams even without a huge marketing budget.</p>
        <h2>Tools some players use</h2>
        <p>If you want camo assists or seeker vision tools, the feature list on <a href="{BUY}">Meccha Chameleon cheats</a> covers Pixel-Perfect Blend, Heat Vision ESP, Instant Tag, and more. Start with the explainers on our <a href="{BLOG}">blog</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-hide-and-seek",
        "cat": "guides",
        "date": "2026-06-24",
        "label": "Jun 24, 2026",
        "title": "Meccha Chameleon Hide and Seek — Why the Twist Works",
        "meta_title": "Meccha Chameleon Hide and Seek Guide",
        "meta_desc": "Why Meccha Chameleon hide and seek feels different from classic playground rounds — paint, poses, and pressure.",
        "h1": "Meccha Chameleon Hide and Seek — Why the Twist Works",
        "lead": "Classic hide and seek is about location. Meccha Chameleon hide and seek is about location plus paint. That one extra skill check changes everything.",
        "kw": "Meccha Chameleon hide and seek",
        "body": """
        <h2>Paint is the twist</h2>
        <p>You are not grabbing a barrel prop. You are becoming the wall. If your colors are off, seekers clock you. If your pose is wrong, they clock you. If both are right, they walk past.</p>
        <h2>Timer pressure</h2>
        <p>Seekers cannot search forever. Hiders cannot fidget forever. That clock keeps Meccha Chameleon hide and seek online matches tense even when the lobby is joking around.</p>
        <h2>Skill ceiling</h2>
        <p>New players hide behind couches. Better players vanish into patterned floors. The best ones use Workshop maps as blank canvases. For practical Meccha Chameleon hider tips, open <a href="blog-meccha-chameleon-hider-tips.html">this guide</a>.</p>
        <h2>Extra edge</h2>
        <p>Players who want camo locks and seeker assists usually land on <a href="{BUY}">mecchahacks.com</a> after learning the base loop.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-multiplayer",
        "cat": "guides",
        "date": "2026-06-26",
        "label": "Jun 26, 2026",
        "title": "Meccha Chameleon Multiplayer — Best Ways to Play With Friends",
        "meta_title": "Meccha Chameleon Multiplayer Tips",
        "meta_desc": "Best Meccha Chameleon multiplayer setups for friends, public lobbies, and longer sessions without the chaos getting annoying.",
        "h1": "Meccha Chameleon Multiplayer — Best Ways to Play With Friends",
        "lead": "Meccha Chameleon multiplayer is the whole product. Solo practice helps a little. Real laughs start when your friends fail to see you sitting in the wallpaper.",
        "kw": "Meccha Chameleon multiplayer",
        "body": """
        <h2>Friend lobby checklist</h2>
        <ul>
          <li>Use a private room when you can</li>
          <li>Agree on map rules before loading ten Workshop stages</li>
          <li>Rotate hider and seeker so nobody gets stuck hunting all night</li>
          <li>Mute toxic public voice if you hop into open queues</li>
        </ul>
        <h2>Public multiplayer reality</h2>
        <p>Public Meccha Chameleon multiplayer can be amazing or messy. Hosts matter. Map choice matters. If a lobby feels broken, leave early.</p>
        <h2>Longer sessions</h2>
        <p>Take short breaks between maps. Paint fatigue is real. Keep a couple “serious” rounds and a couple “meme paint” rounds so the night stays fun.</p>
        <h2>Tools for both roles</h2>
        <p>Saved hider and seeker configs from the <a href="{BUY}">Meccha Chameleon cheats page</a> help if your group wants consistent presets. Support is linked from <a href="{HOME}">mecchahacks.com</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-steam",
        "cat": "guides",
        "date": "2026-06-28",
        "label": "Jun 28, 2026",
        "title": "Meccha Chameleon Steam — Pages, Workshop, and What to Check",
        "meta_title": "Meccha Chameleon Steam Guide",
        "meta_desc": "Everything to know about Meccha Chameleon on Steam — store page, Workshop maps, reviews, and PC setup tips.",
        "h1": "Meccha Chameleon Steam — Pages, Workshop, and What to Check",
        "lead": "Meccha Chameleon Steam is how almost everyone finds the game. The store page, reviews, and Workshop tabs tell you if a lobby night will be chill or cursed.",
        "kw": "Meccha Chameleon Steam",
        "body": """
        <h2>What to read on the store page</h2>
        <p>Check system notes, recent reviews, and tags. Hide-and-seek plus paint is the pitch. Workshop support is the long-term fuel.</p>
        <h2>Workshop caution</h2>
        <p>Workshop maps make Meccha Chameleon Steam lobbies endless — and sometimes risky. Only subscribe to maps from lobbies you trust. Skip random Discord map links.</p>
        <h2>PC tips</h2>
        <p>Close heavy background apps. Verify game files if paint brushes stutter. Update GPU drivers after big Steam client updates.</p>
        <h2>After you own it</h2>
        <p>Learn the base game first. Then, if you want role tools, browse <a href="{BLOG}">our Meccha Chameleon blog</a> and the <a href="{BUY}">cheats pricing page</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-free",
        "cat": "guides",
        "date": "2026-07-01",
        "label": "Jul 1, 2026",
        "title": "Is Meccha Chameleon Free? Price, Sales, and Fake Free Sites",
        "meta_title": "Is Meccha Chameleon Free? Price Guide",
        "meta_desc": "Is Meccha Chameleon free? Learn the real Steam price situation and why fake free downloads are a bad idea.",
        "h1": "Is Meccha Chameleon Free? Price, Sales, and Fake Free Sites",
        "lead": "People type Meccha Chameleon free every day. Short answer: it is a paid Steam game that often sits at a low price — not a permanent free-to-play title.",
        "kw": "Meccha Chameleon free",
        "body": """
        <h2>Real price situation</h2>
        <p>Buy it on Steam when it is listed. Watch for regional sales. Do not trust “100% free full version” mirror sites.</p>
        <h2>Why fake free pages exist</h2>
        <p>Popular indie hits attract malware SEO. A Meccha Chameleon free crack page is usually a trap. Your account and PC are not worth it.</p>
        <h2>Free vs paid tools</h2>
        <p>Same story for cheat files. Free leaks break and get people infected. A maintained suite with clear features is listed on <a href="{BUY}">mecchahacks.com</a>. We also compared options in the <a href="blog-cheat-comparison-2026.html">2026 cheat comparison</a>.</p>
        <h2>Bottom line</h2>
        <p>Pay for the game on Steam. Skip shady free installers. Keep your Workshop habits clean.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-review",
        "cat": "guides",
        "date": "2026-07-03",
        "label": "Jul 3, 2026",
        "title": "Meccha Chameleon Review — Who Will Love It (and Who Won’t)",
        "meta_title": "Meccha Chameleon Review 2026",
        "meta_desc": "Honest Meccha Chameleon review for PC players: fun camouflage multiplayer, rough edges, and who should buy it.",
        "h1": "Meccha Chameleon Review — Who Will Love It (and Who Won’t)",
        "lead": "This Meccha Chameleon review keeps it plain. The idea is excellent. The menus can feel rough. With friends, it still earns the hype.",
        "kw": "Meccha Chameleon review",
        "body": """
        <h2>What works</h2>
        <ul>
          <li>Paint camouflage is a fresh hide-and-seek hook</li>
          <li>Matches create instant stories and clips</li>
          <li>Workshop maps keep nights from getting stale</li>
          <li>Cheap entry for how long groups play it</li>
        </ul>
        <h2>What frustrates</h2>
        <p>UI and lobby friction show. Public servers vary. Some maps have jank corners. If you need polished ranked competitive structure, this is not that game.</p>
        <h2>Who should buy</h2>
        <p>Friend groups. Streamers. Anyone who likes party chaos with a creative skill check. Solo players who hate multiplayer friction may bounce.</p>
        <h2>After you buy</h2>
        <p>Learn painting first. Then browse tips on <a href="{HOME}">mecchahacks.com</a>. Screenshot gallery vibes from IGN’s Steam set match what lobbies look like in practice.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-tips",
        "cat": "guides",
        "date": "2026-07-05",
        "label": "Jul 5, 2026",
        "title": "Meccha Chameleon Tips That Actually Help New Players",
        "meta_title": "Meccha Chameleon Tips for Beginners",
        "meta_desc": "Practical Meccha Chameleon tips for new hiders and seekers — paint faster, hide smarter, search cleaner.",
        "h1": "Meccha Chameleon Tips That Actually Help New Players",
        "lead": "You do not need twenty “pro secrets.” A few Meccha Chameleon tips fix most early losses.",
        "kw": "Meccha Chameleon tips",
        "body": """
        <h2>Hider tips</h2>
        <ul>
          <li>Pick the spot before you paint</li>
          <li>Match big color blocks first, details second</li>
          <li>Freeze your pose — fidgeting is free detection</li>
          <li>Avoid the first place every seeker checks</li>
        </ul>
        <h2>Seeker tips</h2>
        <ul>
          <li>Clear rooms in a loop, not random zigzags</li>
          <li>Look for edges that do not belong</li>
          <li>Tag after a short confirm, not panic spam</li>
          <li>Watch the timer and leave dead zones sooner</li>
        </ul>
        <h2>Go deeper</h2>
        <p>Need more role detail? Read <a href="blog-meccha-chameleon-hider-tips.html">hider tips</a> and <a href="blog-meccha-chameleon-seeker-strategy.html">seeker strategy</a>. Want tool presets? See <a href="{BUY}">Meccha Chameleon cheats</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-painting-game",
        "cat": "guides",
        "date": "2026-07-07",
        "label": "Jul 7, 2026",
        "title": "Meccha Chameleon Painting Game — Why Art Skill Matters",
        "meta_title": "Meccha Chameleon Painting Game Guide",
        "meta_desc": "How Meccha Chameleon turns hide and seek into a painting game — and how to improve your camouflage fast.",
        "h1": "Meccha Chameleon Painting Game — Why Art Skill Matters",
        "lead": "Calling Meccha Chameleon a painting game sounds cute until a seeker stares at your bad brushwork for two seconds and tags you.",
        "kw": "Meccha Chameleon painting game",
        "body": """
        <h2>Paint is the win condition</h2>
        <p>Hiding spots matter. Paint decides if the spot works. That is why Meccha Chameleon painting techniques separate new players from annoying veterans.</p>
        <h2>Fast improvement loop</h2>
        <ol>
          <li>Copy big shapes from the wall</li>
          <li>Soften edges so you do not look stamped on</li>
          <li>Pose like an object, not a person</li>
          <li>Stop painting early enough to freeze</li>
        </ol>
        <h2>When people use auto paint tools</h2>
        <p>Some players want environment color match without slow brushing. Auto-Chameleon Paint and Pixel-Perfect Blend are covered on <a href="{BUY}">the cheats page</a> and in <a href="blog-auto-chameleon-paint.html">this explainer</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-camouflage",
        "cat": "guides",
        "date": "2026-07-08",
        "label": "Jul 8, 2026",
        "title": "Meccha Chameleon Camouflage — How to Blend Without Looking Fake",
        "meta_title": "Meccha Chameleon Camouflage Tips",
        "meta_desc": "Learn Meccha Chameleon camouflage basics: color matching, pose, light, and why “almost painted” gets you tagged.",
        "h1": "Meccha Chameleon Camouflage — How to Blend Without Looking Fake",
        "lead": "Good Meccha Chameleon camouflage is boring on purpose. If seekers glance once and keep walking, you did it right.",
        "kw": "Meccha Chameleon camouflage",
        "body": """
        <h2>Color first</h2>
        <p>Match the dominant color before tiny details. A perfect logo on the wrong wall still fails.</p>
        <h2>Pose second</h2>
        <p>People shapes scream “player.” Object shapes pass. Auto-Pose Snapping helps if you use the suite — see <a href="blog-hider-setup-guide.html">hider setup</a>.</p>
        <h2>Light and edges</h2>
        <p>Bright rooms punish bad edges. Soften the outline. Sit where light already breaks the wall pattern.</p>
        <h2>Camouflage game mindset</h2>
        <p>Think like a chameleon, not a sprinter. For full module names, open <a href="{BUY}">Meccha Chameleon cheats features</a> on mecchahacks.com.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-strategy",
        "cat": "guides",
        "date": "2026-07-09",
        "label": "Jul 9, 2026",
        "title": "Meccha Chameleon Strategy — Simple Plans for Both Roles",
        "meta_title": "Meccha Chameleon Strategy Guide",
        "meta_desc": "Simple Meccha Chameleon strategy for hiders and seekers — map choice, timing, and pressure without overcomplicating it.",
        "h1": "Meccha Chameleon Strategy — Simple Plans for Both Roles",
        "lead": "You do not need a binder of Meccha Chameleon strategy notes. You need a plan for the first thirty seconds of each role.",
        "kw": "Meccha Chameleon strategy",
        "body": """
        <h2>Hider plan</h2>
        <p>Commit to a zone. Paint. Lock. Stay. Mid-round relocates are how people get spotted. Save moves for when a seeker is glued to your wall.</p>
        <h2>Seeker plan</h2>
        <p>Split the map into chunks. Clear one chunk fully. Then rotate. Random sprinting feels active and achieves nothing.</p>
        <h2>Lobby strategy</h2>
        <p>Agree on map types. Some Workshop stages reward parkour nonsense more than camouflage skill. Pick stages that match the night’s mood.</p>
        <h2>Tool-assisted strategy</h2>
        <p>Heat Vision ESP and Instant Tag change seeker routes. Camo locks change hider routes. Browse <a href="{BLOG}">mecchahacks.com/blog</a> for module guides, then the <a href="{BUY}">buy page</a> for the full list.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-indie-game",
        "cat": "guides",
        "date": "2026-07-10",
        "label": "Jul 10, 2026",
        "title": "Meccha Chameleon Indie Game Success — Small Team, Huge Steam Hit",
        "meta_title": "Meccha Chameleon Indie Game Story",
        "meta_desc": "How Meccha Chameleon became a huge indie game hit on Steam with a tiny team and a sharp hide-and-seek idea.",
        "h1": "Meccha Chameleon Indie Game Success — Small Team, Huge Steam Hit",
        "lead": "Meccha Chameleon is the kind of indie game story Steam loves: small team, clear hook, giant player spike.",
        "kw": "Meccha Chameleon indie game",
        "body": """
        <h2>Why it broke out</h2>
        <p>The pitch fits in one sentence. Paint yourself. Hide. Seek. Clips do the marketing. That is efficient for a Meccha Chameleon Japanese indie game with little ad spend.</p>
        <h2>What indie polish looks like here</h2>
        <p>Core fantasy is strong. Systems around it can feel unfinished. Players accept that when the round-to-round fun is high.</p>
        <h2>What that means for you</h2>
        <p>Buy it for the concept. Expect Workshop chaos. Expect patches. Expect public lobbies that need patience.</p>
        <h2>Community tooling</h2>
        <p>As the player base grew, so did demand for role tools. Our hub at <a href="{HOME}">mecchahacks.com</a> covers Meccha Chameleon cheats, guides, and setup notes without fluff.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-japanese-game",
        "cat": "guides",
        "date": "2026-07-11",
        "label": "Jul 11, 2026",
        "title": "Meccha Chameleon Japanese Game Roots — Why the Vibe Feels Different",
        "meta_title": "Meccha Chameleon Japanese Game Guide",
        "meta_desc": "Meccha Chameleon as a Japanese indie multiplayer game — creators, tone, and why the humor lands worldwide.",
        "h1": "Meccha Chameleon Japanese Game Roots — Why the Vibe Feels Different",
        "lead": "Part of the charm is that Meccha Chameleon feels like a Japanese party experiment that escaped onto Steam and refused to stay small.",
        "kw": "Meccha Chameleon Japanese game",
        "body": """
        <h2>Tone</h2>
        <p>Cute presentation. Mean shotgun tags. Silly Workshop maps. That mix is very “party game that got too popular.”</p>
        <h2>Creators</h2>
        <p>Credit goes to Lemorion_1224 and Haganeiro. Small teams ship weird ideas faster. Weird ideas clip better.</p>
        <h2>Language and menus</h2>
        <p>Expect some friction if your lobby hops languages. Set options carefully before a friend night so nobody spends ten minutes in the wrong menu.</p>
        <h2>Keep learning</h2>
        <p>For English guides and tool explainers, stay on <a href="{BLOG}">the mecchahacks blog</a>. For purchase and features, use <a href="{BUY}">Meccha Chameleon cheats</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-lemorion",
        "cat": "guides",
        "date": "2026-07-12",
        "label": "Jul 12, 2026",
        "title": "Lemorion_1224 and Meccha Chameleon — The Creator Behind the Hit",
        "meta_title": "Lemorion_1224 Meccha Chameleon Creator",
        "meta_desc": "Who is Lemorion_1224? A short look at the Meccha Chameleon creator story and why the game exploded.",
        "h1": "Lemorion_1224 and Meccha Chameleon — The Creator Behind the Hit",
        "lead": "When people search Meccha Chameleon Lemorion_1224, they want the human story: who built the paint-hide monster on Steam.",
        "kw": "Meccha Chameleon Lemorion_1224",
        "body": """
        <h2>Small credit, big result</h2>
        <p>Lemorion_1224 is tied to the Meccha Chameleon development credit alongside Haganeiro. The build time was short. The player response was not.</p>
        <h2>Why creator searches matter</h2>
        <p>Players want to know if the game will keep updating, if Workshop stays central, and if the tone stays light. Follow official channels for patch notes — not random Discord mirrors.</p>
        <h2>Player tools vs official game</h2>
        <p>Third-party tools are separate from the developers. Our pages on <a href="{HOME}">mecchahacks.com</a> talk about lobby tools and safety context only. They are not an official Lemorion product.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-haganeiro",
        "cat": "guides",
        "date": "2026-07-13",
        "label": "Jul 13, 2026",
        "title": "Haganeiro and Meccha Chameleon — Co-Creator Context for Players",
        "meta_title": "Haganeiro Meccha Chameleon Co-Creator",
        "meta_desc": "Haganeiro’s role in Meccha Chameleon and what players should know about this Japanese indie co-creation.",
        "h1": "Haganeiro and Meccha Chameleon — Co-Creator Context for Players",
        "lead": "Meccha Chameleon Haganeiro searches usually sit next to Lemorion questions. People want the co-creator picture, not a lore dump.",
        "kw": "Meccha Chameleon Haganeiro",
        "body": """
        <h2>Co-created hit</h2>
        <p>Haganeiro is part of the small team story behind Meccha Chameleon. That matters because the game feels handmade — for better and for rougher edges.</p>
        <h2>What players should expect</h2>
        <p>Updates can be practical instead of flashy. Community maps fill gaps. Public lobbies evolve faster than official content drops.</p>
        <h2>Where we fit</h2>
        <p>If you need setup guides or the <a href="{BUY}">Meccha Chameleon cheats feature list</a>, use mecchahacks.com. For game news, trust official creator posts and Steam notes.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-ranking-system",
        "cat": "guides",
        "date": "2026-07-14",
        "label": "Jul 14, 2026",
        "title": "Meccha Chameleon Ranking System — What Players Mean by “Ranked”",
        "meta_title": "Meccha Chameleon Ranking System Explained",
        "meta_desc": "Does Meccha Chameleon have a ranking system? What players mean by ranked lobbies and how to climb skill without stress.",
        "h1": "Meccha Chameleon Ranking System — What Players Mean by “Ranked”",
        "lead": "Search “Meccha Chameleon ranking system” and you will find confusion. Some players mean formal ranks. Others just mean sweaty public lobbies.",
        "kw": "Meccha Chameleon ranking system",
        "body": """
        <h2>Formal vs informal rank</h2>
        <p>Treat most “rank” talk as skill reputation inside lobbies and friend groups. The game’s party DNA matters more than a polished competitive ladder.</p>
        <h2>How to “climb” anyway</h2>
        <ul>
          <li>Track your own paint quality over a week</li>
          <li>Learn common Workshop maps</li>
          <li>Practice seeker room loops</li>
          <li>Watch one replay of yourself getting found</li>
        </ul>
        <h2>Tools and ranking pressure</h2>
        <p>When lobbies get sweaty, some players add Heat Vision ESP or camo assists. Features and pricing are on <a href="{BUY}">mecchahacks.com/meccha-chameleon-cheats</a>. Play subtle in public if you care about reports — see the <a href="{GUIDE}">guide</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-prop-hunt",
        "cat": "guides",
        "date": "2026-07-15",
        "label": "Jul 15, 2026",
        "title": "Meccha Chameleon Prop Hunt Vibes — Similar, But Not the Same",
        "meta_title": "Meccha Chameleon Prop Hunt Comparison",
        "meta_desc": "Is Meccha Chameleon just prop hunt? Compare the paint camouflage twist to classic prop hunt games.",
        "h1": "Meccha Chameleon Prop Hunt Vibes — Similar, But Not the Same",
        "lead": "People say Meccha Chameleon prop hunt because the social fantasy matches. The mechanic does not.",
        "kw": "Meccha Chameleon prop hunt",
        "body": """
        <h2>Prop hunt in one line</h2>
        <p>Classic prop hunt: become an object from a list. Meccha Chameleon: paint your body until you look like the room.</p>
        <h2>Why the difference matters</h2>
        <p>Prop lists limit creativity. Paint expands it. That is also why Meccha Chameleon vs prop hunt debates never end — fans argue which skill is “more fair.”</p>
        <h2>Which should you play</h2>
        <p>Want instant object jokes? Prop hunt. Want artistic camouflage stress? Meccha Chameleon. Many groups play both in one night.</p>
        <h2>More comparison</h2>
        <p>Read <a href="blog-meccha-chameleon-vs-prop-hunt.html">Meccha Chameleon vs prop hunt</a> next, then browse tools on <a href="{HOME}">mecchahacks.com</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-hider-tips",
        "cat": "guides",
        "date": "2026-07-16",
        "label": "Jul 16, 2026",
        "title": "Meccha Chameleon Hider Tips — Survive Longer Without Looking Sus",
        "meta_title": "Meccha Chameleon Hider Tips",
        "meta_desc": "Meccha Chameleon hider tips for better camouflage, smarter spots, and fewer early tags in public lobbies.",
        "h1": "Meccha Chameleon Hider Tips — Survive Longer Without Looking Sus",
        "lead": "These Meccha Chameleon hider tips are the ones that stick after a dozen lost rounds.",
        "kw": "Meccha Chameleon hider tips",
        "body": """
        <h2>Spot selection</h2>
        <p>Busy visual noise beats empty white walls. Patterned floors and cluttered shelves hide paint errors.</p>
        <h2>Paint timing</h2>
        <p>Finish early enough to freeze. A half-painted player mid-brush is free elo for seekers.</p>
        <h2>Stillness</h2>
        <p>If you breathe with the mouse, you die with the mouse. Lock pose. Look away from your own body if it makes you twitch.</p>
        <h2>Optional assists</h2>
        <p>Pixel-Perfect Blend, Perfect Disguise, and Freeze Pose Timer are explained in our <a href="blog-hider-setup-guide.html">hider setup guide</a>. Full access is on the <a href="{BUY}">buy page</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-painting-techniques",
        "cat": "guides",
        "date": "2026-07-17",
        "label": "Jul 17, 2026",
        "title": "Meccha Chameleon Painting Techniques for Cleaner Blends",
        "meta_title": "Meccha Chameleon Painting Techniques",
        "meta_desc": "Easy Meccha Chameleon painting techniques: block colors, edges, patterns, and when to stop brushing.",
        "h1": "Meccha Chameleon Painting Techniques for Cleaner Blends",
        "lead": "You do not need art school. You need a few Meccha Chameleon painting techniques you can repeat under timer stress.",
        "kw": "Meccha Chameleon painting techniques",
        "body": """
        <h2>Block in first</h2>
        <p>Lay the biggest color. Ignore tiny marks until the silhouette disappears.</p>
        <h2>Break the human outline</h2>
        <p>Shoulders and head shapes sell you out. Paint across those edges using nearby prop colors.</p>
        <h2>Copy nearby noise</h2>
        <p>If the wall has stripes, fake stripes. If it has dirt, fake dirt. Blank paint on noisy walls looks wrong.</p>
        <h2>Stop early</h2>
        <p>Perfect is late. Good-and-frozen beats perfect-and-tagged. For auto color match help, see <a href="blog-auto-chameleon-paint.html">Auto-Chameleon Paint</a> and <a href="{BUY}">mecchahacks.com cheats</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-best-hiding-spots",
        "cat": "guides",
        "date": "2026-07-18",
        "label": "Jul 18, 2026",
        "title": "Meccha Chameleon Best Hiding Spots — How to Pick Them",
        "meta_title": "Meccha Chameleon Best Hiding Spots",
        "meta_desc": "How to choose Meccha Chameleon best hiding spots on default and Workshop maps without camping the same fridge every round.",
        "h1": "Meccha Chameleon Best Hiding Spots — How to Pick Them",
        "lead": "There is no permanent list of Meccha Chameleon best hiding spots. Maps change. Seekers learn. Your method should stay sharper than any one couch.",
        "kw": "Meccha Chameleon best hiding spots",
        "body": """
        <h2>Rules for good spots</h2>
        <ul>
          <li>High visual noise</li>
          <li>Natural object poses available</li>
          <li>Not the first choke seekers enter</li>
          <li>Escape path if someone camps you</li>
        </ul>
        <h2>Default maps vs Workshop</h2>
        <p>Default stages teach fundamentals. Workshop stages invent nonsense geometry. Scout with Free Camera in private practice if you use match tools from the <a href="{BUY}">cheats suite</a>.</p>
        <h2>Rotate your habits</h2>
        <p>If a clip of your spot goes around the lobby Discord, retire it for a night. Fresh spots beat famous spots.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-seeker-strategy",
        "cat": "guides",
        "date": "2026-07-19",
        "label": "Jul 19, 2026",
        "title": "Meccha Chameleon Seeker Strategy — Find People Without Panic",
        "meta_title": "Meccha Chameleon Seeker Strategy",
        "meta_desc": "Meccha Chameleon seeker strategy for cleaner clears, better tags, and less wasted timer.",
        "h1": "Meccha Chameleon Seeker Strategy — Find People Without Panic",
        "lead": "Bad seeker rounds feel busy. Good Meccha Chameleon seeker strategy feels calm and mean.",
        "kw": "Meccha Chameleon seeker strategy",
        "body": """
        <h2>Clear with a path</h2>
        <p>Enter a room the same way each time until it is empty in your head. Then mark it done and move.</p>
        <h2>Read paint errors</h2>
        <p>Wrong hue. Wrong pose. Shiny edges. Those mistakes are louder than footsteps.</p>
        <h2>Tag discipline</h2>
        <p>Whiffed tags warn hiders. Confirm, then commit. Instant Tag tools exist in the suite — details in <a href="blog-instant-tag.html">Instant Tag explained</a>.</p>
        <h2>ESP presets</h2>
        <p>Heat Vision / ESP setup lives in the <a href="blog-seeker-esp-setup-guide.html">seeker guide</a>. Pricing and modules: <a href="{BUY}">Meccha Chameleon cheats</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-character-customization",
        "cat": "guides",
        "date": "2026-07-20",
        "label": "Jul 20, 2026",
        "title": "Meccha Chameleon Character Customization — What You Can Change",
        "meta_title": "Meccha Chameleon Character Customization",
        "meta_desc": "Meccha Chameleon character customization basics: what matters for identity vs what matters for camouflage rounds.",
        "h1": "Meccha Chameleon Character Customization — What You Can Change",
        "lead": "Meccha Chameleon character customization is lighter than a fashion MMO. In this game, paint during the round matters more than lobby drip.",
        "kw": "Meccha Chameleon character customization",
        "body": """
        <h2>Lobby look vs round paint</h2>
        <p>Your menu cosmetics are fun. Your round paint is survival. Do not confuse the two.</p>
        <h2>What actually helps</h2>
        <p>Practice brush control. Learn poses. Save configs if you use tools. That beats chasing rare lobby skins.</p>
        <h2>Want deeper control</h2>
        <p>Camouflage modules and saved presets are listed on <a href="{BUY}">mecchahacks.com</a>. New players should still learn manual paint first.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-maps-download",
        "cat": "guides",
        "date": "2026-07-21",
        "label": "Jul 21, 2026",
        "title": "Meccha Chameleon Maps Download — Safe Workshop Habits",
        "meta_title": "Meccha Chameleon Maps Download Safety",
        "meta_desc": "How to handle Meccha Chameleon maps download requests through Steam Workshop without grabbing shady files.",
        "h1": "Meccha Chameleon Maps Download — Safe Workshop Habits",
        "lead": "“Meccha Chameleon maps download” should mean Steam Workshop subscribe — not a ZIP from a stranger.",
        "kw": "Meccha Chameleon maps download",
        "body": """
        <h2>Safe path</h2>
        <ol>
          <li>Join a lobby using a Workshop map</li>
          <li>Accept Steam’s Workshop prompt</li>
          <li>Let Steam download the map</li>
          <li>Launch when it finishes</li>
        </ol>
        <h2>Unsafe path</h2>
        <p>Manual archive downloads from random links. That is how malware stories start around popular Steam hits.</p>
        <h2>Map quality tips</h2>
        <p>Read comments. Avoid brand-new zero-review maps in public play. Keep a short favorites list for friend nights.</p>
        <h2>More reading</h2>
        <p>See <a href="blog-meccha-chameleon-workshop-mods.html">Workshop mods</a> and general safety notes on <a href="{GUIDE}">the guide page</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-workshop-mods",
        "cat": "guides",
        "date": "2026-07-22",
        "label": "Jul 22, 2026",
        "title": "Meccha Chameleon Workshop Mods — Fun Maps Without the Headache",
        "meta_title": "Meccha Chameleon Workshop Mods Guide",
        "meta_desc": "How to use Meccha Chameleon Workshop mods and maps for better lobbies while staying safe.",
        "h1": "Meccha Chameleon Workshop Mods — Fun Maps Without the Headache",
        "lead": "Meccha Chameleon Workshop mods are why the game still feels fresh after the tenth friend night.",
        "kw": "Meccha Chameleon workshop mods",
        "body": """
        <h2>What Workshop is good for</h2>
        <p>New stages. Joke maps. Recreated spaces. Infinite hide-and-seek variety.</p>
        <h2>What to watch</h2>
        <p>Broken collisions. Unfair void hides. Suspicious files. If staff or Steam warn about a map, drop it.</p>
        <h2>Host etiquette</h2>
        <p>Tell the lobby before you load a heavy mod list. Nobody likes a twenty-minute subscribe stall.</p>
        <h2>Practice tools</h2>
        <p>Free Camera / Noclip in the <a href="{BUY}">cheats suite</a> helps scout new Workshop stages in private sessions. Pair with <a href="blog-super-speed-match-tools.html">match tools notes</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-crossplay",
        "cat": "guides",
        "date": "2026-07-23",
        "label": "Jul 23, 2026",
        "title": "Meccha Chameleon Crossplay — Can You Play Across Platforms?",
        "meta_title": "Meccha Chameleon Crossplay Status",
        "meta_desc": "Does Meccha Chameleon have crossplay? What PC Steam players should know about platforms and lobbies.",
        "h1": "Meccha Chameleon Crossplay — Can You Play Across Platforms?",
        "lead": "Meccha Chameleon crossplay questions come up because friends sit on different devices. Treat the Steam PC build as the main multiplayer home.",
        "kw": "Meccha Chameleon crossplay",
        "body": """
        <h2>Practical answer</h2>
        <p>Plan around the Windows Steam version. Do not assume console or mobile lobbies will magically sync with your PC party.</p>
        <h2>If your group is split</h2>
        <p>Pick one platform and meet there. Cloud PC options exist for some players, but native Windows is simpler for Meccha Chameleon online nights.</p>
        <h2>PC tool stack</h2>
        <p>Our guides and <a href="{BUY}">Meccha Chameleon cheats</a> target the PC client with Windows security requirements listed on the buy page.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-mobile-version",
        "cat": "guides",
        "date": "2026-07-24",
        "label": "Jul 24, 2026",
        "title": "Meccha Chameleon Mobile Version — What Exists (and What Doesn’t)",
        "meta_title": "Meccha Chameleon Mobile Version?",
        "meta_desc": "Is there a Meccha Chameleon mobile version? What to know before downloading random phone ports.",
        "h1": "Meccha Chameleon Mobile Version — What Exists (and What Doesn’t)",
        "lead": "Searches for a Meccha Chameleon mobile version usually mean someone wants paint-hide chaos on a phone. Be careful what you install.",
        "kw": "Meccha Chameleon mobile version",
        "body": """
        <h2>The safe expectation</h2>
        <p>The hit experience people clip is the PC Steam multiplayer game. Random “mobile port” APKs are often junk or worse.</p>
        <h2>If you only have a phone</h2>
        <p>Watch streams. Join friends on PC later. Do not sideload mystery packages named after Meccha Chameleon.</p>
        <h2>PC remains the hub</h2>
        <p>Guides, Workshop talk, and tools on <a href="{HOME}">mecchahacks.com</a> are built around the Windows version. Start at the <a href="blog-meccha-chameleon-download.html">download guide</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-vs-prop-hunt",
        "cat": "comparison",
        "date": "2026-07-25",
        "label": "Jul 25, 2026",
        "title": "Meccha Chameleon vs Prop Hunt — Which Should Your Group Play?",
        "meta_title": "Meccha Chameleon vs Prop Hunt",
        "meta_desc": "Meccha Chameleon vs prop hunt compared: paint skill, object props, lobby vibes, and which fits your friends.",
        "h1": "Meccha Chameleon vs Prop Hunt — Which Should Your Group Play?",
        "lead": "Meccha Chameleon vs prop hunt is the comparison everyone makes after the first viral clip. Both hide. Only one asks you to paint.",
        "kw": "Meccha Chameleon vs prop hunt",
        "body": """
        <h2>Side-by-side</h2>
        <div class="table-wrap"><table>
          <thead><tr><th>Factor</th><th>Meccha Chameleon</th><th>Classic Prop Hunt</th></tr></thead>
          <tbody>
            <tr><td>Hide method</td><td>Paint camouflage</td><td>Become a prop</td></tr>
            <tr><td>Skill feel</td><td>Artistic + stillness</td><td>Prop choice + movement tricks</td></tr>
            <tr><td>Clip energy</td><td>Very high</td><td>High</td></tr>
            <tr><td>Workshop chaos</td><td>Huge on Steam</td><td>Depends on game</td></tr>
          </tbody>
        </table></div>
        <h2>Pick Meccha Chameleon if…</h2>
        <p>Your friends like creative challenge and do not mind rough edges.</p>
        <h2>Pick prop hunt if…</h2>
        <p>You want instant object comedy with less brush work.</p>
        <h2>Playing both</h2>
        <p>Best answer for most groups. When you main Meccha Chameleon, keep tips bookmarked on <a href="{BLOG}">mecchahacks.com/blog</a>.</p>
        """,
    },
    {
        "slug": "blog-meccha-chameleon-camouflage-game",
        "cat": "guides",
        "date": "2026-07-27",
        "label": "Jul 27, 2026",
        "title": "Meccha Chameleon Camouflage Game Guide for New Steam Players",
        "meta_title": "Meccha Chameleon Camouflage Game Guide",
        "meta_desc": "A clear Meccha Chameleon camouflage game guide covering paint, poses, seekers, and where to find PC tools.",
        "h1": "Meccha Chameleon Camouflage Game Guide for New Steam Players",
        "lead": "If you came here for a Meccha Chameleon camouflage game overview, you are in the right place. Paint. Pose. Vanish. Or get tagged and laugh.",
        "kw": "Meccha Chameleon camouflage game",
        "body": """
        <h2>Core fantasy</h2>
        <p>You are not a soldier. You are a walking canvas. The camouflage game fantasy only works if you commit to stillness after the paint dries.</p>
        <h2>Learn path</h2>
        <ol>
          <li><a href="blog-what-is-meccha-chameleon.html">What is Meccha Chameleon?</a></li>
          <li><a href="blog-meccha-chameleon-tips.html">Beginner tips</a></li>
          <li><a href="blog-meccha-chameleon-painting-techniques.html">Painting techniques</a></li>
          <li><a href="blog-meccha-chameleon-seeker-strategy.html">Seeker strategy</a></li>
        </ol>
        <h2>Tools hub</h2>
        <p>When you want hider camo assists, seeker Heat Vision ESP, Instant Tag, Stream-Proof overlay, or Cloud DMA on AWS, go to <a href="{BUY}">https://mecchahacks.com/meccha-chameleon-cheats</a>. That page is the source of truth for features and pricing.</p>
        """,
    },
]


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_body(raw: str) -> str:
    return raw.format(BUY=BUY, HOME=HOME, GUIDE=GUIDE, BLOG=BLOG)


NAV = """  <header class="navbar">
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
  </header>"""

FOOTER = """  <footer class="footer">
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
            <a href="{SUPPORT}" rel="noopener noreferrer">Support Channel</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer">Disclaimer: This site provides information about third-party game software tools. Use is at your own risk and subject to the game’s terms of service. Not affiliated with Meccha Chameleon, Steam, IGN, or the game developers. Screenshots credited to their sources.</p>
        <p>© 2026 mecchahacks.com</p>
      </div>
    </div>
  </footer>"""


def related_links(i: int) -> str:
    others = [POSTS[(i + k) % len(POSTS)] for k in (1, 2, 5)]
    items = "\n".join(
        f'          <li><a href="{p["slug"]}.html">{esc(p["title"])}</a></li>' for p in others
    )
    return f"""      <div class="related-links">
        <h2>Keep Reading</h2>
        <ul>
{items}
          <li><a href="{BUY}">Meccha Chameleon cheats — pricing &amp; features</a></li>
          <li><a href="{GUIDE}">Meccha Chameleon anti-cheat guide</a></li>
        </ul>
      </div>"""


def render_post(i: int, post: dict) -> str:
    img = IGN[i % len(IGN)]
    body = render_body(post["body"])
    nav = NAV.format(
        PURCHASE=PURCHASE,
        LOGO=LOGO,
    )
    footer = FOOTER.format(PURCHASE=PURCHASE, SUPPORT=SUPPORT, LOGO=LOGO)
    pill = "pill-comparison" if post["cat"] == "comparison" else "pill-guides"
    label = "Comparison" if post["cat"] == "comparison" else "Guides"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(post["meta_title"])}</title>
  <meta name="description" content="{esc(post["meta_desc"])}">
  <link rel="canonical" href="https://mecchahacks.com/{post["slug"]}">
  <meta name="robots" content="index, follow">
  <meta property="og:title" content="{esc(post["meta_title"])}">
  <meta property="og:description" content="{esc(post["meta_desc"])}">
  <meta property="og:image" content="{img}">
  <meta property="og:url" content="https://mecchahacks.com/{post["slug"]}">
  <link rel="icon" href="{LOGO}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/global.css">
  <link rel="stylesheet" href="css/blog.css">
</head>
<body>
{nav}
  <main>
    <article class="container article-wrap">
      <div class="article-meta">
        <span class="pill {pill}">{label}</span>
        <time datetime="{post["date"]}">{post["label"]}</time>
      </div>
      <h1>{esc(post["h1"])}</h1>
      <p class="article-lead">{esc(post["lead"])}</p>
      <img class="article-hero-img" src="{img}" width="1280" height="720" alt="{esc(post["kw"])} — Meccha Chameleon screenshot" loading="lazy">
      <p class="article-img-credit">Screenshot via <a href="{IGN_SLIDES}" rel="noopener noreferrer">IGN Meccha Chameleon gallery</a> (image courtesy of lemorion_1224).</p>
      <div class="prose">
{body}
      </div>
      <div class="article-cta">
        <h2>Play with the full tool suite</h2>
        <p>Hider camo, Heat Vision ESP, Instant Tag, Stream-Proof, Cloud DMA — listed on mecchahacks.com.</p>
        <a class="btn btn-primary" href="{PURCHASE}" rel="noopener noreferrer">Buy Meccha Chameleon Cheats</a>
        <p class="redirect-note">You may be redirected to complete checkout.</p>
        <p class="mt-2"><a href="{BUY}">View features &amp; pricing on mecchahacks.com</a></p>
      </div>
{related_links(i)}
    </article>
  </main>
{footer}
  <script src="js/main.js" defer></script>
</body>
</html>
"""


def card_html(i: int, post: dict) -> str:
    img = IGN[i % len(IGN)]
    pill = "pill-comparison" if post["cat"] == "comparison" else "pill-guides"
    label = "Comparison" if post["cat"] == "comparison" else "Guides"
    return f"""          <article class="blog-card" data-category="{post["cat"]}">
            <img class="blog-card-thumb" src="{img}" width="640" height="360" alt="{esc(post["kw"])}" loading="lazy">
            <div class="blog-card-body">
              <span class="pill {pill}">{label}</span>
              <h2><a href="{post["slug"]}.html">{esc(post["title"])}</a></h2>
              <p>{esc(post["meta_desc"])}</p>
              <div class="blog-card-meta">
                <time datetime="{post["date"]}">{post["label"]}</time>
                <a href="{post["slug"]}.html">Read Article →</a>
              </div>
            </div>
          </article>
"""


def main():
    assert len(POSTS) == 30, len(POSTS)
    cards = []
    sitemap_urls = []
    for i, post in enumerate(POSTS):
        html = render_post(i, post)
        (ROOT / f"{post['slug']}.html").write_text(html, encoding="utf-8")
        cards.append(card_html(i, post))
        sitemap_urls.append(post["slug"])
        print("wrote", post["slug"])

    meta = {
        "cards": cards,
        "slugs": sitemap_urls,
        "count": len(POSTS),
    }
    (ROOT / "scripts" / "seo_blog_cards.json").write_text(
        json.dumps({"slugs": sitemap_urls}, indent=2), encoding="utf-8"
    )
    (ROOT / "scripts" / "seo_blog_cards.htmlfragment").write_text(
        "\n".join(cards), encoding="utf-8"
    )
    print("done", len(POSTS))


if __name__ == "__main__":
    main()
