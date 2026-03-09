#!/usr/bin/env python3
import re, os

BASE = "C:/Users/scott/Documents/discover-alaska/src/content/destinations"

body_additions = {
    "glacier-bay": {
        "aeo": "Glacier Bay National Park is a remote Southeast Alaska wilderness where seven tidewater glaciers actively calve into a 65-mile fjord — budget $80-300/day, accessible by a 30-minute flight from Juneau, and best visited June through August for glacier calving and humpback whales.",
        "video_title": "Ice and Silence",
        "video_text": "Seven tidewater glaciers actively calve into a 65-mile fjord — one of the last places on Earth where you can watch geology happen in real time.",
        "gradient": "linear-gradient(135deg, #155e75, #93c5fd, #ffffff)",
    },
    "haines": {
        "aeo": "Haines is a small Southeast Alaska town accessible by road or ferry, famous for the world's largest bald eagle gathering in November and a genuine working-town character — budget $95-200/day, best May through August or October-November for eagles.",
        "video_title": "Valley of the Eagles",
        "video_text": "The Chilkat Valley hosts the world's largest gathering of bald eagles each fall — thousands of birds feeding on a late salmon run against snow-capped peaks.",
        "gradient": "linear-gradient(135deg, #1a4731, #d97706, #1e3a5f)",
    },
    "homer": {
        "aeo": "Homer is the halibut fishing capital of Alaska on Kachemak Bay at the end of the Kenai Peninsula road — vibrant arts scene, sea kayaking, and bear viewing across the bay, budget $100-220/day, best May through September.",
        "video_title": "End of the Road",
        "video_text": "The 4.5-mile Homer Spit juts into Kachemak Bay with fishing charters, galleries, and one of Alaska's most iconic small-town waterfronts.",
        "gradient": "linear-gradient(135deg, #0c4a6e, #065f46, #92400e)",
    },
    "katmai-national-park": {
        "aeo": "Katmai National Park is a remote Alaska peninsula preserve where brown bears catch sockeye salmon at Brooks Falls — accessible only by floatplane, budget $200-500+/day, best July through September for the bear-salmon spectacle.",
        "video_title": "Brooks Falls",
        "video_text": "Sockeye salmon leap into the jaws of waiting brown bears at Brooks Falls — one of the most concentrated wildlife spectacles anywhere on Earth.",
        "gradient": "linear-gradient(135deg, #7f1d1d, #92400e, #1a4731)",
    },
    "kenai-fjords": {
        "aeo": "Kenai Fjords National Park is a dramatic coastal Alaska wilderness south of Seward — glacier-carved fjords, tidewater glaciers, and marine wildlife including orcas and puffins, budget $80-220/day, best May through September.",
        "video_title": "Glacier to Sea",
        "video_text": "The Harding Icefield sends its glaciers cascading to the sea, creating one of Alaska's most dramatic coastal wildernesses with world-class marine wildlife.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #0891b2, #064e3b)",
    },
    "ketchikan": {
        "aeo": "Ketchikan is Southeast Alaska's first Inside Passage port — a colorful fishing town built on pilings over a salmon creek, home to the world's largest standing totem pole collection, budget $95-200/day, best May through September.",
        "video_title": "Creek Street",
        "video_text": "Ketchikan's historic buildings line the creek on pilings — where salmon run each fall beneath the town's most charming neighborhood.",
        "gradient": "linear-gradient(135deg, #7c2d12, #15803d, #1e40af)",
    },
    "kodiak": {
        "aeo": "Kodiak is Alaska's second largest island — home of the world's largest brown bears, a major commercial fishing fleet, and genuine frontier wilderness, budget $100-250/day, accessible by Alaska Airlines from Anchorage.",
        "video_title": "Island of Giants",
        "video_text": "Kodiak Island is home to the world's largest brown bears and one of Alaska's busiest fishing ports — where wilderness and working Alaska overlap completely.",
        "gradient": "linear-gradient(135deg, #3b0764, #166534, #7c2d12)",
    },
    "nome": {
        "aeo": "Nome is a remote Arctic Alaska gold rush town on the Bering Sea — the Iditarod finish line, surrounded by extraordinary tundra wildlife including musk oxen, budget $100-220/day, best March for the Iditarod or June through August for wildlife.",
        "video_title": "End of the Iditarod",
        "video_text": "Nome's Front Street burlab arch marks the finish of the world's most grueling sled dog race — 1,000 miles across Alaska's most remote wilderness.",
        "gradient": "linear-gradient(135deg, #1c1917, #92400e, #1a4731)",
    },
    "petersburg": {
        "aeo": "Petersburg is Southeast Alaska's Little Norway — a proudly Norwegian-heritage fishing town with LeConte Glacier iceberg viewing and minimal cruise ship crowds, budget $90-200/day, best May through September.",
        "video_title": "Little Norway",
        "video_text": "Petersburg's Norwegian fishing heritage shows in the Sons of Norway Hall and rosemaling decorations — a working town the cruise ships bypass.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #dc2626, #ffffff)",
    },
    "seward": {
        "aeo": "Seward is a small port town at the entrance to Kenai Fjords National Park — 127 miles from Anchorage via one of Alaska's most scenic highways, the base for glacier and wildlife boat tours, budget $80-200/day, best May through September.",
        "video_title": "Gateway to Kenai Fjords",
        "video_text": "Seward sits where the Kenai Mountains meet Resurrection Bay — the starting point for the state's best glacier and wildlife cruises.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #0f766e, #334155)",
    },
    "sitka": {
        "aeo": "Sitka is Southeast Alaska's most culturally rich town — former capital of Russian America and historic Tlingit homeland, with world-class bald eagle viewing and dramatic volcanic island scenery, budget $100-250/day, best May through September.",
        "video_title": "Russian Alaska",
        "video_text": "The onion dome of St. Michael's Cathedral watches over Sitka's harbor — where Tlingit culture and Russian colonial history intersect at the edge of the Pacific.",
        "gradient": "linear-gradient(135deg, #7c2d12, #1d4ed8, #14532d)",
    },
    "skagway": {
        "aeo": "Skagway is a living gold rush museum — a perfectly preserved 1898 boomtown at the head of the Lynn Canal, gateway to the Chilkoot Trail and White Pass Railway, budget $90-200/day, best May through September.",
        "video_title": "Gold Rush Town",
        "video_text": "Skagway's entire downtown is a National Historic Landmark — the 1898 boomtown where 100,000 prospectors launched their Klondike journeys.",
        "gradient": "linear-gradient(135deg, #92400e, #1c1917, #854d0e)",
    },
    "talkeetna": {
        "aeo": "Talkeetna is a tiny quirky Alaska town — the base for Denali climbing expeditions and flightseeing over the Alaska Range, with a bohemian character unlike anywhere else in the state, budget $80-200/day, best May through September.",
        "video_title": "Denali Basecamp",
        "video_text": "Talkeetna launches climbers toward Denali each spring — the same Main Street bars serve mountaineers and tourists in equal measure.",
        "gradient": "linear-gradient(135deg, #1c1917, #0c4a6e, #166534)",
    },
    "utqiagvik": {
        "aeo": "Utqiagvik is America's northernmost city — 330 miles above the Arctic Circle on the Arctic Ocean coast, with Inupiaq culture, polar bear viewing, and 82 days of midnight sun, budget $150-300/day, accessible only by air.",
        "video_title": "Top of the World",
        "video_text": "Utqiagvik sits at 71 degrees north — the sun does not set for 82 days each summer, and polar bears roam the frozen sea just outside town.",
        "gradient": "linear-gradient(135deg, #0c4a6e, #e2e8f0, #1e3a5f)",
    },
    "valdez": {
        "aeo": "Valdez is a small Prince William Sound port surrounded by dramatic fjord scenery — the Trans-Alaska Pipeline terminus and base for Columbia Glacier tours, budget $90-220/day, best May through September.",
        "video_title": "Prince William Sound",
        "video_text": "Valdez sits deep in a fjord encircled by 5,000-foot peaks — the head of Prince William Sound and terminus of the Trans-Alaska Pipeline.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #0c4a6e, #334155)",
    },
    "whittier": {
        "aeo": "Whittier is an unusual Alaska town accessible only by road-rail tunnel — the primary Prince William Sound access for kayaking, glacier tours, and whale watching, budget $80-200/day, best May through September.",
        "video_title": "One Tunnel Town",
        "video_text": "Whittier is reached through a single shared road-rail tunnel — 250 people, mostly in one building, surrounded by glaciers and Prince William Sound.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #134e4a, #1c1917)",
    },
    "wrangell-st-elias": {
        "aeo": "Wrangell-St. Elias is the largest national park in America — bigger than Switzerland — a remote Alaska wilderness of glaciers, volcanoes, and the Kennicott copper ghost town, budget $80-300/day, best June through August.",
        "video_title": "America's Largest Park",
        "video_text": "Wrangell-St. Elias is six times the size of Yellowstone — active volcanoes, the largest non-polar glacier system in the world, and the Kennicott ghost town frozen in 1938.",
        "gradient": "linear-gradient(135deg, #14532d, #7c2d12, #0c4a6e)",
    },
}

for slug, data in body_additions.items():
    filepath = f"{BASE}/{slug}.md"
    content = open(filepath, 'r', encoding='utf-8').read()

    # Skip if AEO already present
    if data['aeo'][:40] in content:
        print(f"SKIP {slug} — AEO already present")
        continue

    # Find body start using line-by-line approach
    lines = content.split('\n')
    fm_end = -1
    dash_count = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            dash_count += 1
            if dash_count == 2:
                fm_end = i
                break

    if fm_end == -1:
        print(f"WARN {slug} — could not find FM end")
        continue

    # Find first non-empty line after FM
    body_start = fm_end + 1
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1

    if body_start >= len(lines):
        print(f"WARN {slug} — no body content")
        continue

    # Find end of first paragraph
    para_end = body_start
    while para_end < len(lines) and lines[para_end].strip():
        para_end += 1

    first_para = '\n'.join(lines[body_start:para_end])

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
        '</div>'
    )

    # Build new content
    new_lines = lines[:fm_end+1]
    new_lines.append('')
    new_lines.append(data['aeo'])
    new_lines.append('')
    new_lines.extend(video_block.split('\n'))
    new_lines.append('')
    new_lines.append(first_para)
    new_lines.extend(lines[para_end:])

    new_content = '\n'.join(new_lines)

    # Remove old scott-tips div
    new_content = re.sub(r'<div class="scott-tips">.*?</div>', '', new_content, flags=re.DOTALL)

    open(filepath, 'w', encoding='utf-8').write(new_content)
    print(f"Done {slug}")

print("Body additions complete")
