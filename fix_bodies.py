#!/usr/bin/env python3
"""Fix missing AEO ledes and immersive breaks for files that were skipped."""
import re, os

BASE = "C:/Users/scott/Documents/discover-alaska/src/content/destinations"

# Files that need AEO + immersive break added - these were skipped by add_body.py
# because text matched accidentally or the first para had encoding issue
targets = {
    "juneau": {
        "aeo": "Juneau is Alaska's capital city — accessible only by air or sea, surrounded by the Tongass rainforest and Juneau Icefield, with whale watching, Mendenhall Glacier, and helicopter glacier treks, budget $105-260/day, best May through September.",
        "video_title": "The Capital You Cannot Drive To",
        "video_text": "No road connects Juneau to the rest of Alaska — the state capital exists between the Tongass rainforest and the Juneau Icefield, accessible only by air and sea.",
        "gradient": "linear-gradient(135deg, #0f766e, #1d4ed8, #334155)",
        "old_body_start": "Juneau is the only state capital in America you cannot drive to."
    },
}

for slug, data in targets.items():
    filepath = f"{BASE}/{slug}.md"
    content = open(filepath, 'r', encoding='utf-8').read()

    if "immersive-break-inline" in content:
        print(f"SKIP {slug} — already has immersive break")
        continue

    old = data['old_body_start']
    if old not in content:
        print(f"WARN {slug} — old body start not found")
        continue

    video_block = (
        '<div class="immersive-break-inline">\n'
        '  <video autoplay muted loop playsinline preload="metadata">\n'
        f'    <source src="/videos/destinations/{slug}-hero.mp4" type="video/mp4" />\n'
        '  </video>\n'
        f'  <div class="ib-gradient" style="background: {data["gradient"]};"></div>\n'
        '  <div class="ib-content">\n'
        f'    <div class="ib-title">{data["video_title"]}</div>\n'
        f'    <p class="ib-text">{data["video_text"]}</p>\n'
        '  </div>\n'
        '</div>\n'
    )

    replacement = f'{data["aeo"]}\n\n{video_block}\n{old}'
    content = content.replace(old, replacement, 1)

    open(filepath, 'w', encoding='utf-8').write(content)
    print(f"Done {slug}")

print("Fix complete")
