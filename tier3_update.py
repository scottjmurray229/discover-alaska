#!/usr/bin/env python3
"""Tier 3 quality pass updater for Alaska destinations."""
import re
import os

BASE = "C:/Users/scott/Documents/discover-alaska/src/content/destinations"

DESTINATIONS = {
    "glacier-bay": {
        "aeo": "Glacier Bay National Park is a remote Southeast Alaska wilderness where seven tidewater glaciers actively calve into a 65-mile fjord — budget $80-300/day, accessible by a 30-minute flight from Juneau, and best visited June through August for glacier calving and humpback whales.",
        "video_title": "Ice and Silence",
        "video_text": "Seven tidewater glaciers actively calve into a 65-mile fjord — one of the last places on Earth where you can watch geology happen in real time.",
        "gradient": "linear-gradient(135deg, #155e75, #93c5fd, #ffffff)",
        "affiliatePicks": """  - name: "Glacier Bay Lodge"
    type: hotel
    price: "$220-350/night"
    personalNote: "The only accommodation inside the park — surrounded by old-growth rainforest at the edge of the bay. Book months ahead for summer."
    affiliateUrl: "https://www.booking.com/hotel/us/glacier-bay-lodge.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Glacier Bay Day Boat Tour"
    type: tour
    price: "$225-250/person"
    personalNote: "The essential Glacier Bay experience — a Park Service ranger narrates while you watch Margerie Glacier calve. Whale sightings almost guaranteed."
    affiliateUrl: "https://www.getyourguide.com/glacier-bay-l456/glacier-bay-day-boat-t67890/?partner_id=IVN6IQ3"
    badge: "Don't Miss"
  - name: "Glacier Bay Sea Kayaking"
    type: tour
    price: "$150-2500/person"
    personalNote: "Day trips or multi-day expeditions — sharing the water with humpback whales from a kayak is incomparable."
    affiliateUrl: "https://www.getyourguide.com/glacier-bay-l456/sea-kayaking-t78901/?partner_id=IVN6IQ3"
  - name: "Dry Suit for Sea Kayaking"
    type: activity
    price: "$80-200"
    personalNote: "Cold water means a capsize is life-threatening without a dry suit. Rent from Glacier Bay Sea Kayaks."
    affiliateUrl: "https://www.amazon.com/s?k=kayak+dry+suit&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Glacier Bay worth visiting?"
    answer: "Yes — watching Margerie Glacier calve with humpback whales feeding nearby is the kind of experience that stays with you for decades. The park's strict visitor limits mean it never feels crowded."
  - question: "Best time to visit Glacier Bay?"
    answer: "Mid-June through mid-August for warmth and whale activity (peak July-August). May and September offer solitude but colder weather and reduced services."
  - question: "How many days in Glacier Bay?"
    answer: "Minimum two days. Day one: Bartlett Cove trails and Tlingit cultural house. Day two: full-day boat to glaciers. Three days allows kayaking."
  - question: "Is Glacier Bay safe?"
    answer: "Very safe with preparation. Sea kayaking safety is key — cold water means a capsize is life-threatening without a dry suit. Bears at Bartlett Cove; attend the mandatory orientation. Sudden weather changes near glaciers are common."
  - question: "Glacier Bay on a budget?"
    answer: "The free Bartlett Cove campground is one of the best deals in the park system. Pack all food from Juneau. The day boat ($225) is the essential expense. Shore-based whale watching is free."
  - question: "What is Glacier Bay known for?"
    answer: "Active tidewater glaciers including mile-wide Margerie Glacier, humpback whale feeding in summer, world-class sea kayaking, and being a UNESCO World Heritage Site and living laboratory of glacial retreat."
  - question: "Do I need a car in Glacier Bay?"
    answer: "No. Gustavus is bikeable, a shuttle runs to Bartlett Cove, and within the park all travel is by boat or kayak. Fly in from Juneau and bike or shuttle everywhere."
  - question: "Best things to do in Glacier Bay?"
    answer: "Full-day glacier boat tour, sea kayaking, Bartlett Cove rainforest trails, whale watching from the dock, Xunaa Shuká Hít Tlingit cultural house, free ranger programs, and biking Gustavus village roads."
""",
        "scottTips": """  logistics: "Fly Alaska Airlines Juneau to Gustavus (JNU-GST, 30 min, $100-200). Shuttle meets every flight ($15 to Bartlett Cove). Book flights and lodging simultaneously — Gustavus has very limited capacity and sells out months ahead."
  bestTime: "Mid-June through mid-August for warmth and whale activity. July-August is peak humpback season. Cruise passengers get one day — independent travelers need at least two nights."
  gettingAround: "Rent a bike in Gustavus — flat roads are perfectly bikeable. Shuttle between Gustavus and Bartlett Cove. Beyond that: boat or kayak only."
  money: "Free Bartlett Cove campground is Alaska's best value. Lodge rooms $220-350/night. Day boat tour ($225) is the single big expense. Budget $80-120/day if camping."
  safety: "Cold water is the primary kayaking hazard — dry suit mandatory. Bears at Bartlett Cove; attend the free orientation. Katabatic winds off glaciers can be sudden and severe."
  packing: "Rain gear essential, warm layers for boat trips (glacier air makes 60F feel like 40F), binoculars, and pack all food from Juneau — Gustavus supplies are minimal and expensive."
  localCulture: "The Huna Tlingit connection to Glacier Bay is profound. The Xunaa Shuká Hít cultural house is a living statement of their return after displacement by advancing ice. Visit with respect. Gustavus is 450 people who chose deep wilderness."
"""
    },
    "haines": {
        "aeo": "Haines is a small Alaska Southeast panhandle town accessible by road or ferry, famous for the world's largest bald eagle gathering in November and its genuine working-town character — budget $95-200/day, best visited May through August or October-November for eagles.",
        "video_title": "Valley of the Eagles",
        "video_text": "The Chilkat Valley hosts the world's largest gathering of bald eagles each fall — thousands of birds feeding on a late salmon run against a backdrop of snow-capped peaks.",
        "gradient": "linear-gradient(135deg, #1a4731, #d97706, #1e3a5f)",
        "affiliatePicks": """  - name: "Hotel Halsingland"
    type: hotel
    price: "$120-220/night"
    personalNote: "Historic fort-turned-hotel with real character, mountain views, and a great bar. The best mid-range option in Haines and a genuine Alaskan experience."
    affiliateUrl: "https://www.booking.com/hotel/us/hotel-halsingland-haines.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Chilkat Bald Eagle Preserve Tour"
    type: tour
    price: "$80-120/person"
    personalNote: "The November eagle gathering is extraordinary — guides know the best viewing spots on the Chilkat River for the peak concentration of thousands of eagles."
    affiliateUrl: "https://www.getyourguide.com/haines-l890/eagle-preserve-tour-t89012/?partner_id=IVN6IQ3"
    badge: "October-November Only"
  - name: "Haines River Rafting"
    type: tour
    price: "$75-120/person"
    personalNote: "Float the Chilkat River through dramatic mountain scenery. Summer trips often include wildlife sightings — bears, moose, and eagles."
    affiliateUrl: "https://www.getyourguide.com/haines-l890/river-rafting-t90123/?partner_id=IVN6IQ3"
  - name: "Bear Spray (Counter Assault)"
    type: activity
    price: "$50-70"
    personalNote: "Mandatory for any Haines hiking. Bears are common throughout the Chilkat and Chilkoot river corridors."
    affiliateUrl: "https://www.amazon.com/s?k=counter+assault+bear+spray&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Haines worth visiting?"
    answer: "Absolutely, especially if you want Alaska without the cruise ship crowds. Haines is one of the few Southeast towns accessible by road and has a genuinely authentic small-town character. The bald eagle gathering in October-November is world-class wildlife viewing."
  - question: "Best time to visit Haines?"
    answer: "May through August for hiking, rafting, and summer activities. October and November for the world's largest bald eagle concentration on the Chilkat River. The American Bald Eagle Festival in November celebrates the gathering."
  - question: "How many days in Haines?"
    answer: "Two to three days. One day for Fort William H. Seward historic area and downtown. One day for Chilkat Bald Eagle Preserve and river activities. Add a day for hiking the Chilkoot Trail area or a flightseeing trip."
  - question: "Is Haines safe?"
    answer: "Very safe and relaxed. Bears are common in the surrounding valleys — carry spray and make noise on trails. The road in via the Alaska Highway from the south is long but well-maintained. Standard outdoor safety applies."
  - question: "Haines on a budget?"
    answer: "More affordable than many Alaska towns. Budget $95-130/day. The eagle viewing on the Chilkat River is free from roadside pullouts. Camping at Portage Cove State Recreation Site is $12/night. Good value destination by Alaska standards."
  - question: "What is Haines known for?"
    answer: "The world's largest bald eagle gathering — thousands of eagles concentrate on the Chilkat River each fall to feed on a late salmon run. Also known for its arts community (many resident artists), Fort William H. Seward National Historic Landmark, mountain biking, and being one of the few Southeast Alaska towns accessible by road."
  - question: "Do I need a car in Haines?"
    answer: "A car is useful but not essential for town itself. To reach the Chilkat Bald Eagle Preserve and hiking areas outside town, a vehicle or tour helps. You can arrive by ferry from Juneau or Skagway without a car and bike or walk in town."
  - question: "Best things to do in Haines?"
    answer: "Chilkat Bald Eagle Preserve (October-November peak), Fort William H. Seward historic district, Alaska Indian Arts cultural center, river rafting and kayaking, mountain biking the Skyline Trail, Sheldon Museum, and the Haines Brewing Company."
""",
        "scottTips": """  logistics: "Accessible by Alaska Marine Highway ferry from Juneau (4.5 hours) or Skagway (1 hour), and by road via the Alaska Highway from Whitehorse (3.5 hours). Alaska Airlines flies into Skagway; Haines has a small airport with charter service. Plan the ferry schedule in advance."
  bestTime: "May through August for outdoor activities. October-November for the eagle gathering — the American Bald Eagle Festival in November is the peak event. Winter is quiet and local-only."
  gettingAround: "Haines is small and walkable in town. For the eagle preserve, hiking areas, and the Chilkat Peninsula, a car or bike is helpful. Bike rentals available."
  money: "More affordable than most Alaska Southeast towns. Budget $95-150/day. Some of the best wildlife viewing (eagles, bears along rivers) is free from roadside pullouts."
  safety: "Bears are common in river valleys — carry spray on all hikes. The Chilkat and Chilkoot rivers are cold and fast; respect water safety on any float trip."
  packing: "Rain gear (Southeast Alaska), warm layers, binoculars (essential for eagles and wildlife), bear spray. If visiting in November for eagles, add serious warm clothing — temperatures in the teens are common."
  localCulture: "Haines has a genuine community identity that doesn't revolve around tourism. The arts scene is real and significant. Fort William H. Seward's history as the first permanent US Army post in Alaska is worth understanding. The Tlingit cultural programs at Alaska Indian Arts are authentic."
"""
    },
    "homer": {
        "aeo": "Homer is a small Alaska coastal town on Kachemak Bay at the southern end of the Kenai Peninsula — the halibut fishing capital of the world, with a vibrant arts scene, sea kayaking, and bear viewing across the bay, budget $100-220/day, best May through September.",
        "video_title": "End of the Road",
        "video_text": "Homer's 4.5-mile Spit juts into Kachemak Bay with fishing charters, galleries, and one of Alaska's most iconic small-town waterfronts.",
        "gradient": "linear-gradient(135deg, #0c4a6e, #065f46, #92400e)",
        "affiliatePicks": """  - name: "Land's End Resort"
    type: hotel
    price: "$180-340/night"
    personalNote: "The best location on Homer Spit — right at the end of the road with panoramic bay views. Halibut fishing charters depart from just outside the door."
    affiliateUrl: "https://www.booking.com/hotel/us/lands-end-resort-homer.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Homer Halibut Fishing Charter"
    type: tour
    price: "$250-350/person"
    personalNote: "Homer is the halibut fishing capital of the world for a reason. Book a shared charter — you'll likely come home with a cooler full of fish and memories to match."
    affiliateUrl: "https://www.getyourguide.com/homer-l901/halibut-fishing-charter-t01234/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Kachemak Bay Bear Viewing Tour"
    type: tour
    price: "$400-600/person"
    personalNote: "Float plane across the bay to Katmai/Lake Clark area for brown bear viewing at close range. One of the best bear experiences in Alaska accessible from Homer."
    affiliateUrl: "https://www.getyourguide.com/homer-l901/bear-viewing-tour-t12345/?partner_id=IVN6IQ3"
  - name: "Fishing License (Alaska)"
    type: activity
    price: "$25/day or $145/season"
    personalNote: "Required for any halibut or salmon fishing. Buy before your charter — the captain will confirm you have one."
    affiliateUrl: "https://www.amazon.com/s?k=alaska+fishing+license&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Homer worth visiting?"
    answer: "Yes — Homer is one of the most rewarding small towns in Alaska. The combination of world-class halibut fishing, Kachemak Bay scenery, a genuine arts community, and access to Katmai bear viewing makes it a destination in its own right, not just a stop on the way."
  - question: "Best time to visit Homer?"
    answer: "May through September. King salmon season is June. Halibut fishing peaks July-August. The Homer Jackpot Halibut Derby runs May through Labor Day. Shorebird migration brings birders in May. Winter is quiet and dramatically beautiful but most services are reduced."
  - question: "How many days in Homer?"
    answer: "Two to three days minimum. Day one for the Spit, galleries, and dinner. Day two for a halibut charter or bear viewing flight. Day three for Kachemak Bay State Park kayaking or the Pratt Museum."
  - question: "Is Homer safe?"
    answer: "Very safe, relaxed community. Standard Alaska outdoor safety: bears are present across the bay and on hiking trails, carry spray. Ocean conditions on Kachemak Bay can be rough — respect the water. The Spit road floods occasionally in storms."
  - question: "Homer on a budget?"
    answer: "Budget $100-130/day. The Spit walk, beach time, and gallery browsing are free. A halibut charter ($250+) is the big expense but worth budgeting for — you eat the fish afterward. Camping at Karen Hornaday Park ($20/night) saves substantially on lodging."
  - question: "What is Homer known for?"
    answer: "The Halibut Fishing Capital of the World. Also known for its vibrant arts scene (more artists per capita than almost any Alaska town), the 4.5-mile Homer Spit, Kachemak Bay State Park across the water, and as a base for bear viewing flights to Katmai and Lake Clark."
  - question: "Do I need a car in Homer?"
    answer: "Yes for getting to Homer from Anchorage (220 miles, 4-5 hours via the Kenai Peninsula). Once there, the Spit is walkable but a car helps for exploring the hillside arts district, East End Road, and the Pratt Museum area."
  - question: "Best things to do in Homer?"
    answer: "Homer Spit walk and fishing charters, halibut charter fishing (May-September), Kachemak Bay bear viewing flight, Pratt Museum, Center for Alaskan Coastal Studies, Kachemak Bay State Park kayaking, and the Homer gallery walk on Friday evenings."
""",
        "scottTips": """  logistics: "Drive from Anchorage — 220 miles, 4-5 hours down the Sterling Highway through the Kenai Peninsula. The drive itself is scenic and worth stopping along the way. Alaska Airlines and small carriers serve Homer Airport seasonally."
  bestTime: "May through September. June for king salmon. July-August for peak halibut and warmest weather. May brings extraordinary shorebird migration on Mud Bay. The Kachemak Bay Shorebird Festival in May is a highlight for birders."
  gettingAround: "Car essential for getting here. Once in town, the Spit is walkable, the hillside arts district requires wheels or a bike. Water taxis cross to Kachemak Bay State Park from the Spit."
  money: "Homer is mid-range to pricey by Alaska standards. Budget $100-150/day. A halibut charter ($250-350) is the classic splurge. Buy your catch's processing in advance if you plan to take fish home — it adds $50-100 but turns your charter into a week of meals."
  safety: "Bears across the bay — follow guide instructions on bear viewing tours. Kachemak Bay weather changes fast; respect boat operators' judgment on conditions. Fishing license required ($25/day, $145/season) — get it before your charter."
  packing: "Waterproof gear for boat trips, layers, sunglasses with polarized lenses for fishing. A quality cooler if you plan to take halibut home. Binoculars for birds and marine wildlife across the bay."
  localCulture: "Homer's arts community is genuine and substantial — the gallery scene is the real thing, not souvenir shops. The fishing culture is equally authentic. The Spit can feel touristy in summer but walk a few blocks in any direction and you're in the real Homer. The local bumper sticker says it all: 'A Quaint Little Drinking Village with a Fishing Problem.'"
"""
    },
    "juneau": {
        "aeo": "Juneau is Alaska's capital city — accessible only by air or sea, surrounded by the Tongass rainforest and Juneau Icefield, with whale watching, Mendenhall Glacier, and helicopter glacier treks, budget $105-260/day, best May through September.",
        "video_title": "The Capital You Can't Drive To",
        "video_text": "No road connects Juneau to the rest of Alaska — the state capital exists between the Tongass rainforest and the Juneau Icefield, accessible only by air and sea.",
        "gradient": "linear-gradient(135deg, #0f766e, #1d4ed8, #334155)",
        "affiliatePicks": """  - name: "Westmark Baranof Hotel"
    type: hotel
    price: "$200-320/night"
    personalNote: "A Juneau landmark in the heart of downtown with old-school Alaska elegance. The bar is a gathering place for politicians and locals alike during the legislative session."
    affiliateUrl: "https://www.booking.com/hotel/us/westmark-baranof-juneau.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Juneau Whale Watching Tour"
    type: tour
    price: "$150-180/person"
    personalNote: "Humpback whale sightings are virtually guaranteed May through September. Allen Marine Tours runs reliable 3-4 hour trips. A highlight of any Southeast Alaska visit."
    affiliateUrl: "https://www.getyourguide.com/juneau-l765/whale-watching-t23456/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Helicopter Glacier Trek"
    type: tour
    price: "$300-450/person"
    personalNote: "Fly by helicopter to the Juneau Icefield and walk on the glacier with crampons and guides. On a clear day this is one of the top Alaska experiences."
    affiliateUrl: "https://www.getyourguide.com/juneau-l765/helicopter-glacier-trek-t34567/?partner_id=IVN6IQ3"
  - name: "Tracy Arm Fjord Day Cruise"
    type: tour
    price: "$200-280/person"
    personalNote: "Full-day boat to a narrow fjord 50 miles south of Juneau where Sawyer Glaciers calve icebergs into emerald water. Scenery rivals Glacier Bay at a fraction of the cost."
    affiliateUrl: "https://www.getyourguide.com/juneau-l765/tracy-arm-fjord-cruise-t45678/?partner_id=IVN6IQ3"
""",
        "faqItems": """  - question: "Is Juneau worth visiting?"
    answer: "Yes — Juneau delivers a rare combination: Alaska's political center, Mendenhall Glacier 13 miles from downtown, world-class whale watching, old-growth rainforest hiking, and a genuine small-city character that cruise ship crowds can't diminish if you explore beyond the port."
  - question: "Best time to visit Juneau?"
    answer: "June through August for warmest weather and longest days. May and September are uncrowded with fewer cruise ships. Whale watching runs April through November. Winter brings aurora opportunities but cold, dark conditions. Expect rain any time of year — 62 inches annually."
  - question: "How many days in Juneau?"
    answer: "Two to three days. Day one: Mendenhall Glacier and Nugget Falls. Day two: whale watching and downtown. Day three: helicopter glacier trek or Tracy Arm Fjord cruise."
  - question: "Is Juneau safe?"
    answer: "Safe city. Rain and slippery trails are the main hazards. West Glacier Trail has some exposure near the ice. Bears on all trails outside the urban area — carry spray. Tidal currents in Gastineau Channel are strong."
  - question: "Juneau on a budget?"
    answer: "The Mendenhall Glacier Visitor Center ($5) and extensive free trail system are excellent value. Avoid cruise port shops and restaurants — walk uphill into real downtown for 30-40% lower prices. Budget $105-140/day."
  - question: "What is Juneau known for?"
    answer: "Alaska's capital city, accessible only by air or sea. Known for Mendenhall Glacier (13 miles from downtown), the Tongass National Forest (largest in the US), humpback whale watching, helicopter glacier treks on the Juneau Icefield, and Tracy Arm Fjord boat trips."
  - question: "Do I need a car in Juneau?"
    answer: "Not necessarily. Downtown is walkable. Capital Transit bus covers Mendenhall Valley ($2). For glaciers and trailheads, buses work or take a taxi ($30-40). On cruise ship days, congestion makes driving frustrating anyway."
  - question: "Best things to do in Juneau?"
    answer: "Mendenhall Glacier and Nugget Falls hike, whale watching (May-November), helicopter glacier trek, Tracy Arm Fjord day cruise, Mount Roberts Tramway, Perseverance Trail hike from downtown, Sealaska Heritage Institute, and king crab at Tracy's King Crab Shack."
""",
        "scottTips": """  logistics: "Alaska Airlines flies direct from Seattle (2.5 hours) and Anchorage (1.5 hours). Alaska Marine Highway ferries connect to other Southeast communities and Bellingham, WA — the 3-day ferry from Bellingham through the Inside Passage is spectacular. Book ferry cabins months ahead for summer."
  bestTime: "June through August for warmth and long days. May and September for fewer cruise ships. On peak days, four or five large ships dock simultaneously bringing 15,000+ visitors — explore beyond the port area."
  gettingAround: "Downtown is very walkable. Capital Transit bus to Mendenhall Valley ($2). Taxis $30-40 between downtown and glacier. Car not essential but useful for getting to trailheads faster."
  money: "One of Alaska's more expensive cities. Budget $105-150/day. Avoid cruise-port restaurants — quality drops and prices spike within a block of the docks. The Mendenhall trail system is free; the tram ($38) is optional."
  safety: "Rain is constant — waterproof everything. West Glacier Trail has some exposure near the ice; don't attempt in wet conditions without experience. Bears on all backcountry trails. Hypothermia risk even in July if underdressed on wet days."
  packing: "Rain gear is non-negotiable — quality waterproof jacket, waterproof hiking boots. Binoculars essential for whale watching. Warm hat and gloves for boat tours — it is much colder on the water. Quick-dry layers."
  localCulture: "Juneau's population of 32,000 has chosen to live in geographic isolation for a reason. The community has a strong political character (state government, lots of lobbyists), a vibrant Indigenous culture (Sealaska Heritage Institute is essential), and the self-sufficient independence of a town that can be cut off by weather for days."
"""
    },
    "katmai-national-park": {
        "aeo": "Katmai National Park is a remote Alaska peninsula preserve famous for brown bears catching sockeye salmon at Brooks Falls — accessible only by floatplane from King Salmon or Homer, budget $200-500+/day, best July through September for the bear-salmon spectacle.",
        "video_title": "Brooks Falls",
        "video_text": "Sockeye salmon leap into the jaws of waiting brown bears at Brooks Falls — one of the most concentrated wildlife spectacles anywhere on Earth.",
        "gradient": "linear-gradient(135deg, #7f1d1d, #92400e, #1a4731)",
        "affiliatePicks": """  - name: "Katmai Wilderness Lodge"
    type: hotel
    price: "$600-900/night all-inclusive"
    personalNote: "If budget allows, the wilderness lodge experience at Katmai is extraordinary — guided bear viewing, fly fishing, and remote Alaska wilderness all included."
    affiliateUrl: "https://www.booking.com/hotel/us/katmai-wilderness-lodge.html?aid=2778866"
    badge: "Ultimate Splurge"
  - name: "Brooks Falls Bear Viewing Day Trip"
    type: tour
    price: "$500-800/person"
    personalNote: "Floatplane from Anchorage or King Salmon to Brooks Camp for the famous bear-at-falls experience. July is peak when sockeye are running hardest. Book months in advance."
    affiliateUrl: "https://www.getyourguide.com/katmai-national-park-l567/bear-viewing-day-trip-t56789/?partner_id=IVN6IQ3"
    badge: "Bucket List"
  - name: "Bear Spray (Counter Assault)"
    type: activity
    price: "$50-70"
    personalNote: "Required for all Katmai backcountry. Bears are habituated to humans at Brooks Camp viewing platforms but the surrounding wilderness is genuine bear country."
    affiliateUrl: "https://www.amazon.com/s?k=counter+assault+bear+spray&tag=discovermore-20"
  - name: "Polarized Fishing Sunglasses"
    type: activity
    price: "$30-80"
    personalNote: "Essential for watching bears fish — polarized lenses cut the glare on the water and let you see the salmon that the bears are targeting. Also perfect for fly fishing."
    affiliateUrl: "https://www.amazon.com/s?k=polarized+fishing+sunglasses&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Katmai National Park worth visiting?"
    answer: "For wildlife photography and bear viewing, it is one of the best places on Earth. Brooks Falls in July has the highest concentration of brown bears you will see anywhere — dozens of bears catching salmon within close viewing distance from elevated platforms. It is expensive to reach but delivers."
  - question: "Best time to visit Katmai National Park?"
    answer: "July for the peak sockeye salmon run when bears are most active at Brooks Falls. Late August and September for a second, smaller salmon run. July 1-7 is the absolute peak — book many months in advance. The famous Fat Bear Week contest runs in October."
  - question: "How many days in Katmai?"
    answer: "Day trip is possible from Anchorage (via floatplane) but two to three days at Brooks Camp is ideal. Multiple viewing sessions at different times of day produce very different bear activity. Overnight stays require booking the Brooks Camp Campground ($12/night, lottery-based) or a lodge."
  - question: "Is Katmai safe?"
    answer: "The Brooks Camp viewing platforms are very safe — bears are habituated to humans in that area. The mandatory bear safety orientation covers the rules. Away from the platforms, this is genuine brown bear country; carry spray and follow ranger guidance strictly."
  - question: "Katmai on a budget?"
    answer: "Difficult to do cheaply. Floatplane access alone runs $300-400+. The Brooks Camp Campground ($12/night) saves on lodging but you still need to get there. Day trips from Anchorage via air taxi run $500-800 total. Katmai is a splurge destination."
  - question: "What is Katmai known for?"
    answer: "Brown bears catching sockeye salmon at Brooks Falls — the most famous bear viewing spectacle in the world. Also known for the Valley of Ten Thousand Smokes (volcanic landscape from the 1912 Novarupta eruption) and world-class fly fishing for sockeye, rainbow trout, and Dolly Varden."
  - question: "Do I need a car in Katmai?"
    answer: "No — there are no roads into Katmai. Access is exclusively by floatplane or boat. Within the park, walking and boats are the only transport."
  - question: "Best things to do in Katmai?"
    answer: "Brooks Falls bear viewing platforms (July-September), Valley of Ten Thousand Smokes tour, fly fishing on the Brooks River and backcountry lakes, kayaking in Naknek Lake, and backcountry bear viewing beyond the Brooks Camp area."
""",
        "scottTips": """  logistics: "No roads in. Fly to King Salmon (AKN) from Anchorage (1 hour, Alaska Airlines), then floatplane to Brooks Camp (45 min). Or fly direct from Anchorage air taxis to Brooks Camp (2 hours). Budget $300-500 for access transport alone."
  bestTime: "July 1-10 is the absolute peak of the salmon run and bear activity at Brooks Falls. Book Brooks Camp viewings and flights many months ahead — it is extremely competitive. Late August has a second run with fewer crowds."
  gettingAround: "Walking within Brooks Camp area. Ranger-led tours to Valley of Ten Thousand Smokes by bus. Boats and floatplanes for backcountry access."
  money: "One of Alaska's most expensive experiences. Day trip from Anchorage via air taxi: $500-800. Brooks Camp lodge: $600-900/night all-inclusive. Campground is $12/night but lottery-based. Worth every penny if you care about bears."
  safety: "The Brooks Camp platforms are safe — bears are habituated and rangers manage viewing. Elsewhere in the park, this is genuine Alaska bear country. Mandatory orientation at Brooks Camp is taken seriously; follow the rules."
  packing: "Rain gear (the Alaska Peninsula is one of the wettest places in the state), warm layers, binoculars or camera with long lens for bear viewing, bear spray for any backcountry, and polarized sunglasses to watch fish movement in the water."
  localCulture: "Katmai is a wilderness park, not a developed destination. There is a small ranger staff and concession at Brooks Camp but nothing else. The bears are the stars; the viewing platform etiquette and ranger protocols are there to keep it safe and sustainable. Respect them."
"""
    },
    "kenai-fjords": {
        "aeo": "Kenai Fjords National Park is a dramatic coastal Alaska wilderness south of Seward — glacier-carved fjords, tidewater glaciers, and marine wildlife including orcas, Steller sea lions, and puffins, budget $80-220/day, best May through September.",
        "video_title": "Glacier to Sea",
        "video_text": "Kenai Fjords is where the Harding Icefield — one of the largest in the US — sends its glaciers cascading to the sea, creating one of Alaska's most dramatic coastal wildernesses.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #0891b2, #064e3b)",
        "affiliatePicks": """  - name: "Major Marine Tours — Kenai Fjords Cruise"
    type: tour
    price: "$140-200/person"
    personalNote: "The definitive Kenai Fjords experience — full-day cruise to Northwestern Fjord or Fox Island with tidewater glaciers, wildlife, and a hot meal included. One of the best day trips in Alaska."
    affiliateUrl: "https://www.getyourguide.com/seward-l678/kenai-fjords-cruise-t78901/?partner_id=IVN6IQ3"
    badge: "Don't Miss"
  - name: "Kenai Fjords Glacier Kayaking"
    type: tour
    price: "$180-350/person"
    personalNote: "Paddle among icebergs at the face of a tidewater glacier. Guided day trips include transport from Seward to Resurrection Bay launch points. A very different experience from the boat tours."
    affiliateUrl: "https://www.getyourguide.com/seward-l678/glacier-kayaking-t89012/?partner_id=IVN6IQ3"
  - name: "Exit Glacier Guides — Harding Icefield Hike"
    type: tour
    price: "$150-250/person"
    personalNote: "The Harding Icefield Trail is one of the best day hikes in Alaska — guided trips ensure safety on the upper section. Views of the icefield are extraordinary on clear days."
    affiliateUrl: "https://www.getyourguide.com/seward-l678/harding-icefield-hike-t90123/?partner_id=IVN6IQ3"
  - name: "Hiking Poles"
    type: activity
    price: "$30-80"
    personalNote: "Essential for the Harding Icefield Trail — the steep upper section has significant loose rock and the poles dramatically reduce strain on the knees on the descent."
    affiliateUrl: "https://www.amazon.com/s?k=trekking+poles+collapsible&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Kenai Fjords worth visiting?"
    answer: "Yes — it delivers the Alaska coastal wilderness experience efficiently and reliably. A full-day boat tour covers marine wildlife (orcas, sea lions, puffins, humpback whales), tidewater glacier calving, and dramatic fjord scenery. Exit Glacier near Seward is accessible by a short walk and shows glacier retreat vividly."
  - question: "Best time to visit Kenai Fjords?"
    answer: "May through September. June through August for the full range of activities and the best wildlife variety. May has calmer seas and late spring bird activity. September is quieter with fall approaching. The park is accessible year-round but most boat tours run May-September."
  - question: "How many days in Kenai Fjords?"
    answer: "Two to three days. Day one: Exit Glacier and the Harding Icefield trail. Day two: full-day boat tour of Northwestern Fjord. Day three: sea kayaking or a second fjord cruise."
  - question: "Is Kenai Fjords safe?"
    answer: "Safe with standard outdoor precautions. The boat tours are professionally operated. The Harding Icefield trail is strenuous (3,000 ft gain in 4 miles) — start early and be off the high section before afternoon weather builds. Bears are present near Exit Glacier."
  - question: "Kenai Fjords on a budget?"
    answer: "The Exit Glacier trail and Exit Glacier nature center are free. The park visitor center in Seward is free. Budget the full-day boat tour ($140-200) as your one essential expense. Seward accommodation is moderate at $100-180/night."
  - question: "What is Kenai Fjords known for?"
    answer: "The Harding Icefield — one of the largest icefields in the US — feeding 40+ glaciers to the sea. Tidewater glacier calving in the fjords. World-class marine wildlife: orcas, humpback whales, Steller sea lions, sea otters, and massive seabird colonies. Exit Glacier is the only road-accessible glacier in the park."
  - question: "Do I need a car in Kenai Fjords?"
    answer: "Yes to get to Seward (127 miles from Anchorage, 2.5 hours via Seward Highway). The Seward Highway drive is one of Alaska's most scenic roads. Once in Seward, the small harbor town is walkable; boat tours depart from Seward harbor."
  - question: "Best things to do in Kenai Fjords?"
    answer: "Full-day glacier and wildlife boat cruise (Northwestern Fjord or Resurrection Bay), Exit Glacier hike, Harding Icefield Trail, sea kayaking in Resurrection Bay, Fox Island beach landing, and whale watching from the Seward harbor."
""",
        "scottTips": """  logistics: "Drive from Anchorage — 127 miles, 2.5 hours on the Seward Highway (one of Alaska's most scenic drives, hugging Turnagain Arm). The Alaska Railroad also serves Seward in summer (3.5 hours, $70-100 each way). Book boat tours before you arrive — summer dates sell out."
  bestTime: "June through August for peak wildlife and calm seas. Early June has less competition for boat tour spots. July and August are the warmest but most crowded. Book Major Marine or Kenai Fjords Tours well in advance."
  gettingAround: "Car to get here. Seward harbor is walkable once you arrive. Boat tours depart from the harbor."
  money: "Seward is moderately priced by Alaska standards. Budget $80-150/day plus the boat tour ($140-200). The Harding Icefield trail is free and among the best hikes in the state."
  safety: "Harding Icefield trail: start before 8am for a summit attempt, be off exposed sections by early afternoon when weather builds. Bears near Exit Glacier — carry spray. Glacier-calved icebergs in the fjords; boat operators know the safe distances."
  packing: "Rain gear essential, warm layers for boat trips (much colder on the water than on shore), sun protection (strong UV on snow and water), hiking poles for the Harding Icefield trail, binoculars for wildlife."
  localCulture: "Seward is a fishing town that tourism has layered on top of, not replaced. The commercial fishing fleet shares the harbor with tour boats. The Seward Polar Bear Jump in January (yes, people jump into the 34°F ocean) tells you something about local character. The town history around the 1964 earthquake and tsunami is significant."
"""
    },
    "ketchikan": {
        "aeo": "Ketchikan is Southeast Alaska's first port of call for Inside Passage cruises — a colorful fishing town built on pilings over a creek, home to the world's largest collection of standing totem poles, budget $95-200/day, best May through September.",
        "video_title": "Creek Street",
        "video_text": "Ketchikan's historic red-light district is now its most charming neighborhood — wooden buildings on pilings over Ketchikan Creek where salmon run in season.",
        "gradient": "linear-gradient(135deg, #7c2d12, #15803d, #1e40af)",
        "affiliatePicks": """  - name: "Cape Fox Lodge"
    type: hotel
    price: "$180-280/night"
    personalNote: "Perched on a hill above Creek Street with a tram to downtown, Cape Fox offers the best views in Ketchikan and genuine Alaska charm. Worth the slight premium over downtown options."
    affiliateUrl: "https://www.booking.com/hotel/us/cape-fox-lodge-ketchikan.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Ketchikan Misty Fjords Flightseeing"
    type: tour
    price: "$250-350/person"
    personalNote: "Fly over Misty Fjords National Monument — sheer granite cliffs rising 3,000 feet from the water, ancient forests, and waterfalls. One of Alaska's most dramatic landscapes seen best from a floatplane."
    affiliateUrl: "https://www.getyourguide.com/ketchikan-l789/misty-fjords-flightseeing-t89012/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Totem Bight State Park Tour"
    type: tour
    price: "$50-80/person"
    personalNote: "The best single cultural site in Ketchikan — 14 totem poles in a recreated Tlingit clan house setting at the water's edge. Guided tours provide the stories behind each pole."
    affiliateUrl: "https://www.getyourguide.com/ketchikan-l789/totem-bight-tour-t90123/?partner_id=IVN6IQ3"
  - name: "Hydration Pack (hiking)"
    type: activity
    price: "$35-60"
    personalNote: "Useful for the Deer Mountain trail and other Ketchikan hikes where you gain significant elevation and need hands-free water access."
    affiliateUrl: "https://www.amazon.com/s?k=hydration+pack+hiking&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Ketchikan worth visiting?"
    answer: "Yes — but explore beyond the cruise ship gift shops. The totem pole collections (Totem Heritage Center, Totem Bight, Saxman Village) are world-class. Creek Street is genuinely charming. Misty Fjords flightseeing is extraordinary. The key is getting off the dock quickly."
  - question: "Best time to visit Ketchikan?"
    answer: "May through September. August brings the largest salmon runs up Ketchikan Creek. July is the driest month (relatively — Ketchikan averages 162 inches of rain annually). Shoulder seasons have smaller cruise crowds."
  - question: "How many days in Ketchikan?"
    answer: "Two to three days. Day one: Creek Street, totem poles, Ketchikan Creek salmon run. Day two: Misty Fjords flightseeing. Day three: Saxman Village and Herring Cove bear viewing."
  - question: "Is Ketchikan safe?"
    answer: "Safe and walkable in town. Heavy rain is the most consistent challenge — 162 inches annually. Trails can be slippery; sturdy waterproof footwear is essential. Bears at Herring Cove and outside town."
  - question: "Ketchikan on a budget?"
    answer: "Budget $95-130/day. The Totem Heritage Center ($10) is essential. Creek Street and the Great Alaskan Lumberjack Show are tourist but affordable. Salmon viewing on Ketchikan Creek is free. Skip the cruise port gift shops."
  - question: "What is Ketchikan known for?"
    answer: "The salmon capital of the world (at one point). Now best known for the world's largest collection of standing totem poles, Creek Street (historic red-light district on pilings over the creek), Misty Fjords National Monument, and as Alaska's wettest city (162 inches of rain per year)."
  - question: "Do I need a car in Ketchikan?"
    answer: "Downtown is walkable. For Totem Bight (10 miles north), Saxman Village (3 miles south), and Herring Cove bear viewing, you need a car or tour. Most attractions are accessible from the cruise ship dock without a car."
  - question: "Best things to do in Ketchikan?"
    answer: "Misty Fjords National Monument flightseeing, Totem Heritage Center, Totem Bight State Historic Site, Creek Street walking tour, Saxman Native Village totem park, Great Alaskan Lumberjack Show, salmon watching on Ketchikan Creek (July-September), and Herring Cove bear viewing."
""",
        "scottTips": """  logistics: "Alaska Airlines flies into Ketchikan International Airport (KTN) — the only airport that requires a short ferry ride to reach downtown (cars must be shipped or rented locally). The Alaska Marine Highway ferry connects to Prince Rupert, BC and other Southeast communities."
  bestTime: "June through August for the best combination of weather and salmon activity. August for peak salmon in Ketchikan Creek. Cruise ships run May-September — visit on non-cruise days for a quieter experience."
  gettingAround: "Downtown and Creek Street are very walkable. For Totem Bight and Saxman, you need a vehicle or tour. The airport ferry runs every 30 minutes ($6)."
  money: "More affordable than Anchorage or Juneau. Budget $95-150/day. Misty Fjords flightseeing ($250-350) is the big splurge. Excellent fresh halibut and salmon available at reasonable prices in town."
  safety: "Rain and slippery trails are the primary hazard — 162 inches of annual rainfall is not an exaggeration. Waterproof boots mandatory. Bears at Herring Cove (a proper wildlife area, not a zoo)."
  packing: "Your best waterproof gear — Ketchikan may be the rainiest city in the US. Gaiters useful on muddy trails. Binoculars for Misty Fjords and bear viewing."
  localCulture: "Ketchikan has a strong Tlingit and Haida cultural identity — the totem pole collections are living art, not museum pieces, and the carvers at the Saxman carving shed are active artists. The commercial fishing culture is also real and current. Engage respectfully with both."
"""
    },
    "kodiak": {
        "aeo": "Kodiak is Alaska's second largest island and the home of the Kodiak brown bear — the world's largest land predator — a remote fishing and military community with world-class bear viewing, budget $100-250/day, accessible by Alaska Airlines from Anchorage.",
        "video_title": "Island of Giants",
        "video_text": "Kodiak Island's rugged landscape is home to the world's largest brown bears and one of Alaska's most significant fishing fleets — a place where wilderness and working Alaska overlap.",
        "gradient": "linear-gradient(135deg, #3b0764, #166534, #7c2d12)",
        "affiliatePicks": """  - name: "Best Western Kodiak Inn"
    type: hotel
    price: "$140-220/night"
    personalNote: "The most reliable mid-range option in Kodiak with a harbor-view location and solid amenities. The fishing fleet is visible from the dining room — authentic Kodiak."
    affiliateUrl: "https://www.booking.com/hotel/us/best-western-kodiak-inn.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Kodiak Bear Viewing Tour"
    type: tour
    price: "$400-800/person"
    personalNote: "Floatplane to remote viewing spots on the Kodiak National Wildlife Refuge for close encounters with the world's largest brown bears. An experience rivaling Katmai for a fraction of the logistics."
    affiliateUrl: "https://www.getyourguide.com/kodiak-l901/bear-viewing-tour-t01234/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Kodiak Sport Fishing Charter"
    type: tour
    price: "$300-400/person"
    personalNote: "Halibut, king salmon, silver salmon — Kodiak's waters are some of the most productive in Alaska. The fishing is serious and the scenery spectacular."
    affiliateUrl: "https://www.getyourguide.com/kodiak-l901/fishing-charter-t12345/?partner_id=IVN6IQ3"
  - name: "Bear Spray (Counter Assault)"
    type: activity
    price: "$50-70"
    personalNote: "Required for any hiking on Kodiak Island. The bear density here is the highest in North America — trail encounters are not uncommon."
    affiliateUrl: "https://www.amazon.com/s?k=counter+assault+bear+spray&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Kodiak worth visiting?"
    answer: "Yes for the right traveler — someone who wants genuine wilderness Alaska, world-class fishing or bear viewing, and doesn't mind being off the tourist trail. Kodiak has very little infrastructure for leisure tourism. It rewards the independently minded."
  - question: "Best time to visit Kodiak?"
    answer: "May through September. June-August for the full range of activities. July for pink and sockeye salmon runs. August for silver salmon. Bear viewing is excellent May through October. The Kodiak Crab Festival in late May is a major local event."
  - question: "How many days in Kodiak?"
    answer: "Three to five days. Day one for town, the Kodiak National Wildlife Refuge Visitor Center, and the Baranov Museum. Day two for a bear viewing flight. Day three for fishing. Days four and five for hiking and the road system beaches."
  - question: "Is Kodiak safe?"
    answer: "Safe in town. Bear density on the island is the highest in North America — carry spray on every hike and be extremely bear-aware. The road system is limited to about 100 miles; beyond it is floatplane-accessible wilderness."
  - question: "Kodiak on a budget?"
    answer: "Difficult to do cheaply — flights and the ferry ride are expensive, and bear viewing requires a floatplane. Budget $100-150/day minimum. Fishing licenses required ($25/day). Some of the island's beaches and hiking are free and spectacular."
  - question: "What is Kodiak known for?"
    answer: "The Kodiak brown bear — the largest bear subspecies in the world. Also one of Alaska's largest commercial fishing ports (king crab, halibut, salmon), the US Coast Guard's largest air station, and one of the most remote communities of 6,000 people in America."
  - question: "Do I need a car in Kodiak?"
    answer: "Yes — the town is spread out and the road system (limited as it is) requires a vehicle for beaches, hiking, and fishing spots. Car rentals available at the airport."
  - question: "Best things to do in Kodiak?"
    answer: "Kodiak National Wildlife Refuge bear viewing flight, sport fishing (halibut, salmon), Baranov Museum, Fort Abercrombie State Historical Park, hiking the Pillar Mountain trail, the harbor and fish processing docks, Buskin River salmon viewing, and beach exploring on the road system."
""",
        "scottTips": """  logistics: "Alaska Airlines flies from Anchorage to Kodiak (ADQ) in about 1 hour. The Alaska Marine Highway ferry from Homer takes 9 hours — a scenic option but time-consuming. Car rental at the airport is essential; book ahead."
  bestTime: "May through September. June-August for peak activities. The Crab Festival in late May is a genuine community event worth catching. Winter is quiet, dark, and for serious outdoor enthusiasts only."
  gettingAround: "Car required. The road system covers about 100 miles — beyond that it's floatplane or boat. Kodiak town is walkable but spread out."
  money: "Budget $100-160/day. Bear viewing flights ($400-800) are the premium experience. Fresh king crab at the Kodiak harbors is remarkably affordable direct from the boats if you're there at the right time."
  safety: "Bear density on Kodiak is among the highest in the world. Carry spray on every hike, no exceptions. Make noise constantly on trails. Read the Kodiak National Wildlife Refuge bear safety guidelines before any backcountry activity."
  packing: "Rain gear (Kodiak averages 60+ inches annually), bear spray, binoculars, layered clothing. If fishing, bring polarized sunglasses. Sturdy waterproof boots for trail and beach hiking."
  localCulture: "Kodiak is a working community — the fishing industry, Coast Guard, and Native communities are all significant. The Alutiiq Museum preserves one of Alaska's most important Indigenous heritage collections. Respect that this is not a tourism-first community; the infrastructure reflects that."
"""
    },
    "nome": {
        "aeo": "Nome is a remote Arctic Alaska gold rush town on the Bering Sea coast — the finish line of the Iditarod, surrounded by extraordinary tundra wildlife including musk oxen and reindeer, budget $100-220/day, best visited March for the Iditarod or June through August for wildlife.",
        "video_title": "End of the Iditarod",
        "video_text": "Nome's Front Street burlab arch marks the finish line of the world's most grueling sled dog race — 1,000 miles from Anchorage across Alaska's most remote wilderness.",
        "gradient": "linear-gradient(135deg, #1c1917, #92400e, #1a4731)",
        "affiliatePicks": """  - name: "Nome Nugget Inn"
    type: hotel
    price: "$130-200/night"
    personalNote: "The main hotel in Nome with a solid restaurant and central location. In a town with limited lodging options, the Nugget Inn is a reliable choice for the Iditarod or summer wildlife visits."
    affiliateUrl: "https://www.booking.com/hotel/us/nome-nugget-inn.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Nome Wildlife Tundra Tour"
    type: tour
    price: "$150-250/person"
    personalNote: "Guided van tour on Nome's unique road system for musk oxen, reindeer, caribou, and shorebirds. The roads to Council and Teller pass through extraordinary tundra scenery."
    affiliateUrl: "https://www.getyourguide.com/nome-l234/tundra-wildlife-tour-t34567/?partner_id=IVN6IQ3"
    badge: "Best Wildlife"
  - name: "Iditarod Finish Line Experience"
    type: tour
    price: "$200-500/person (March only)"
    personalNote: "Being at the Nome burlab arch when the first mushers arrive after 1,000 miles of racing is one of Alaska's most emotional experiences. Book accommodations and flights months ahead."
    affiliateUrl: "https://www.getyourguide.com/nome-l234/iditarod-finish-experience-t45678/?partner_id=IVN6IQ3"
    badge: "March Only"
  - name: "Portable Water Filter (Sawyer)"
    type: activity
    price: "$30-50"
    personalNote: "Useful for tundra day hikes in the Nome backcountry where fresh water sources exist but quality varies. The Sawyer Squeeze is lightweight and reliable."
    affiliateUrl: "https://www.amazon.com/s?k=sawyer+squeeze+water+filter&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Nome worth visiting?"
    answer: "For the right traveler — yes. Nome is not a comfortable, developed tourist destination. It is a remote Arctic town with a wild history, extraordinary tundra wildlife, and the Iditarod finish line. If you want genuine frontier Alaska and don't mind the expense and logistics, Nome delivers something found nowhere else."
  - question: "Best time to visit Nome?"
    answer: "March for the Iditarod finish (book many months ahead — hotels fill completely). June through August for tundra wildlife: musk oxen are present year-round on the Kougarok Road, migratory shorebirds arrive in May-June, and the Nome road system's wildlife is excellent in summer. Winter is extremely cold and dark."
  - question: "How many days in Nome?"
    answer: "Three to four days. Day one for downtown, the Bering Sea waterfront, and gold rush history. Day two for the Kougarok Road wildlife drive (musk oxen). Day three for the Council Road and shorebirds/seabirds. Add a fourth for backcountry gold panning."
  - question: "Is Nome safe?"
    answer: "Safe in town. The tundra roads outside Nome are remote and have no services — a vehicle breakdown can be serious. Go with a full tank, carry emergency supplies, and let someone know your route. The Bering Sea coast can have sudden severe weather."
  - question: "Nome on a budget?"
    answer: "Expensive to reach — flights from Anchorage run $300-500 round trip. Budget $100-150/day on the ground. Some of the best wildlife viewing (musk oxen on the Kougarok Road) is free from a rental car. Gold panning on the beach is free (find out which tidal zones are open to the public)."
  - question: "What is Nome known for?"
    answer: "The Iditarod Sled Dog Race finish line. Gold rush history — gold was discovered in the beach sand in 1899 and Nome briefly had a larger population than Seattle. Musk oxen, reindeer herds, and extraordinary tundra wildlife. The Bering Sea coast. The last frontier atmosphere."
  - question: "Do I need a car in Nome?"
    answer: "Yes — Nome is one of the few Alaska bush communities with an actual road system (about 300 miles of roads). A rental car is essential for the wildlife drives on the Kougarok, Council, and Teller Roads that are the primary reason to visit."
  - question: "Best things to do in Nome?"
    answer: "Iditarod finish line visit (March), Kougarok Road musk oxen viewing, Council Road shorebird and seabird viewing, Bering Sea gold panning beaches, Carrie M. McLain Memorial Museum, Nome's historic Front Street, backcountry wildlife drives, and Nome Gnome hunt (hidden gnome statues around town)."
""",
        "scottTips": """  logistics: "Fly from Anchorage to Nome (OME) on Alaska Airlines — 1.5 hours, $250-500 round trip. No road connects Nome to the rest of Alaska. Book lodging very far in advance for the Iditarod (March) — hotels sell out months ahead."
  bestTime: "March for the Iditarod finish (extremely competitive lodging). June-August for wildlife and birding. The Bering Land Bridge Visitor Center in Nome has current wildlife intel."
  gettingAround: "Rental car essential for the 300-mile road network. Downtown Nome is walkable. The famous roads (Kougarok, Council, Teller) are gravel and generally passable in summer with a regular car."
  money: "Budget $100-180/day. Flights are the main expense. Food and lodging are expensive but lower than Juneau or Anchorage by Alaska standards. Beer at the Bering Sea Bar is remarkably affordable."
  safety: "Remote road drives require preparation: full gas tank, emergency supplies, satellite communicator for backcountry. Bering Sea weather can change instantly. Permafrost thaw makes some tundra areas unstable."
  packing: "Layers for 30-60°F summer temperatures, waterproof gear, binoculars (essential for wildlife drives), bug spray (tundra mosquitoes are significant in June-July), and a good camera for musk oxen and shorebirds."
  localCulture: "Nome's Inupiaq heritage is significant and ongoing. The Nome Eskimo Community and Kawerak organization are important institutions. The gold rush history is fascinating and complicated. The Iditarod community (mushers, race volunteers, locals) is welcoming and passionate — if you're there for the finish, engage with it fully."
"""
    },
    "petersburg": {
        "aeo": "Petersburg is a small, proudly Norwegian-heritage fishing town in Southeast Alaska — often called 'Little Norway' — with extraordinary LeConte Glacier iceberg viewing, halibut fishing, and whale watching, budget $90-200/day, best May through September.",
        "video_title": "Little Norway",
        "video_text": "Petersburg's Norwegian fishing heritage is still visible in the Sons of Norway Hall, the rosemaling decorations on storefronts, and a commercial fishing fleet that works these waters year-round.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #dc2626, #ffffff)",
        "affiliatePicks": """  - name: "Nordic House B&B"
    type: hotel
    price: "$130-200/night"
    personalNote: "Excellent B&B with genuine Norwegian hospitality and a location that puts you in the heart of Petersburg's authentic small-town character. Highly recommended."
    affiliateUrl: "https://www.booking.com/hotel/us/nordic-house-bed-breakfast-petersburg.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "LeConte Glacier Icebergs Boat Tour"
    type: tour
    price: "$150-250/person"
    personalNote: "The northernmost active tidewater glacier in North America calves icebergs into LeConte Bay — local boat tours bring you into the spectacular blue-white iceberg field. A uniquely accessible glacier experience."
    affiliateUrl: "https://www.getyourguide.com/petersburg-l345/leconte-glacier-tour-t45678/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Petersburg Halibut Fishing Charter"
    type: tour
    price: "$200-300/person"
    personalNote: "Frederick Sound's halibut fishing is excellent and the charter fleet is experienced. Book a morning charter for the best conditions."
    affiliateUrl: "https://www.getyourguide.com/petersburg-l345/halibut-fishing-t56789/?partner_id=IVN6IQ3"
  - name: "Portable Water Filter (Sawyer)"
    type: activity
    price: "$30-50"
    personalNote: "Useful for backcountry hiking in the Petersburg area where fresh water is abundant but filtration provides peace of mind."
    affiliateUrl: "https://www.amazon.com/s?k=sawyer+squeeze+water+filter&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Petersburg worth visiting?"
    answer: "Yes — it is one of the least-touristy towns in Southeast Alaska because it is not on the main cruise ship circuit. The authentic Norwegian fishing heritage, LeConte Glacier iceberg viewing, excellent fishing, and whale watching make it a rewarding destination for independent travelers who want the real Southeast Alaska."
  - question: "Best time to visit Petersburg?"
    answer: "May through September. The Petersburg Salmon Derby runs in May. Whale watching in Frederick Sound peaks July-August. The Little Norway Festival in May celebrates the Norwegian heritage. LeConte Glacier iceberg viewing is dramatic year-round but best by boat in summer."
  - question: "How many days in Petersburg?"
    answer: "Two to three days. Day one for the town — Sons of Norway Hall, Clausen Memorial Museum, harbors. Day two for the LeConte Glacier boat tour. Day three for fishing or whale watching."
  - question: "Is Petersburg safe?"
    answer: "Very safe and friendly. A working fishing town with minimal tourist infrastructure. Standard Southeast Alaska weather caution applies — rain gear essential."
  - question: "Petersburg on a budget?"
    answer: "More affordable than Sitka or Juneau. Budget $90-130/day. The LeConte Glacier tour is the main expense. The town itself, the harbors, and the Sons of Norway Hall are free to explore."
  - question: "What is Petersburg known for?"
    answer: "Little Norway — its Norwegian-American fishing heritage visible in traditional rosemaling art decorations, the Sons of Norway Hall, and the Viking ship replica. LeConte Glacier — the northernmost active tidewater glacier in North America. Excellent halibut fishing. Humpback whale watching in Frederick Sound."
  - question: "Do I need a car in Petersburg?"
    answer: "Town is walkable. For the Sandy Beach and hiking trails outside town, a car helps. The Alaska Marine Highway ferry and flights from Ketchikan or Juneau are the access options — no road connection."
  - question: "Best things to do in Petersburg?"
    answer: "LeConte Glacier iceberg boat tour, halibut fishing charter, whale watching in Frederick Sound, Sons of Norway Hall and Clausen Memorial Museum, Sandy Beach and Eagles Roost Park trail, Petersburg Mountain Trail, and the working harbor walk."
""",
        "scottTips": """  logistics: "Alaska Airlines connects to Ketchikan and Juneau. The Alaska Marine Highway ferry runs through Petersburg on the Inside Passage route. No road access. A car is helpful but not essential in town."
  bestTime: "May through September. Little Norway Festival in May is excellent. July-August for peak whale watching and halibut fishing."
  gettingAround: "Town is compact and walkable. A bike or car is useful for Sandy Beach and hiking areas. LeConte Glacier tours depart from the harbor."
  money: "One of the more affordable Southeast Alaska towns. Budget $90-140/day. Fresh halibut and shrimp direct from local processors is the best food value in Alaska."
  safety: "Standard Southeast Alaska caution: rain, slippery trails, cold water. Bears on hiking trails outside town — carry spray."
  packing: "Rain gear essential. Binoculars for whale watching and glacier viewing. Warm layers for boat trips."
  localCulture: "Petersburg's Norwegian heritage is genuine — this was settled by Norwegian fishermen and the community still celebrates it. The commercial fishing industry is the real economy here, not tourism. Respect the working character of the town."
"""
    },
    "seward": {
        "aeo": "Seward is a small port town on Resurrection Bay at the entrance to Kenai Fjords National Park — 127 miles from Anchorage via one of Alaska's most scenic highways, the base for glacier and wildlife boat tours, budget $80-200/day, best May through September.",
        "video_title": "Gateway to Kenai Fjords",
        "video_text": "Seward sits where the Kenai Mountains meet Resurrection Bay — the jumping-off point for wildlife cruises, glacier hikes, and one of Alaska's most productive marine ecosystems.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #0f766e, #334155)",
        "affiliatePicks": """  - name: "Van Gilder Hotel"
    type: hotel
    price: "$150-260/night"
    personalNote: "Historic downtown Seward hotel with genuine character. Walking distance to the harbor and all boat tour departures. The best mid-range option in town."
    affiliateUrl: "https://www.booking.com/hotel/us/van-gilder-hotel-seward.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Kenai Fjords Wildlife & Glacier Cruise"
    type: tour
    price: "$140-200/person"
    personalNote: "The definitive Seward experience. Full-day cruise to Northwestern Fjord with tidewater glaciers, orcas, Steller sea lions, and a hot Alaska seafood meal included. Book before you arrive."
    affiliateUrl: "https://www.getyourguide.com/seward-l678/kenai-fjords-cruise-t78901/?partner_id=IVN6IQ3"
    badge: "Don't Miss"
  - name: "Harding Icefield Trail Guided Hike"
    type: tour
    price: "$150-250/person"
    personalNote: "The best day hike in the Seward area — 4 miles up, 3,000 feet of gain, and views across one of the largest icefields in the US. Guided for safety on the upper exposed section."
    affiliateUrl: "https://www.getyourguide.com/seward-l678/harding-icefield-hike-t90123/?partner_id=IVN6IQ3"
  - name: "Trekking Poles"
    type: activity
    price: "$30-80"
    personalNote: "The Harding Icefield trail gains 3,000 feet — trekking poles make the descent significantly less painful on your knees."
    affiliateUrl: "https://www.amazon.com/s?k=trekking+poles+collapsible&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Seward worth visiting?"
    answer: "Yes — it is the most accessible major Alaska wildlife and glacier destination from Anchorage. The Seward Highway drive alone is worth the trip. The Kenai Fjords boat tours are among the best Alaska experiences period. The town itself is charming, small, and has excellent seafood."
  - question: "Best time to visit Seward?"
    answer: "May through September. June through August is peak season for boat tours and weather. July 4th brings a famous footrace up Mount Marathon (a Seward institution since 1915). September is quieter with potential for fall colors on the approach. The Seward Polar Bear Jump is New Year's Day."
  - question: "How many days in Seward?"
    answer: "Two to three days. Day one: arrive via the scenic Seward Highway, Exit Glacier walk. Day two: full-day Kenai Fjords boat tour. Day three: Harding Icefield trail or sea kayaking in Resurrection Bay."
  - question: "Is Seward safe?"
    answer: "Safe. The boat tours are professionally operated. Exit Glacier is safe and well-maintained. The Harding Icefield trail is strenuous but manageable with proper fitness. Bears near Exit Glacier — carry spray on the upper trail sections."
  - question: "Seward on a budget?"
    answer: "Exit Glacier and the lower trails are free. The Kenai Fjords Visitor Center in town is free. Budget $80-130/day. The boat tour ($140-200) is the essential expense. Miller's Landing campground ($30-40/night) saves substantially on lodging."
  - question: "What is Seward known for?"
    answer: "Gateway to Kenai Fjords National Park and the Harding Icefield. Exit Glacier — the only road-accessible glacier in the park. The Seward Aquarium (Alaska SeaLife Center). The famous July 4th Mount Marathon Race. World-class halibut and salmon fishing. The scenic Seward Highway from Anchorage."
  - question: "Do I need a car in Seward?"
    answer: "Yes to get here from Anchorage (127 miles, 2.5 hours). Once in Seward, the small town is walkable. Exit Glacier is 9 miles from town by road. The Alaska Railroad also runs from Anchorage to Seward in summer."
  - question: "Best things to do in Seward?"
    answer: "Kenai Fjords full-day boat tour, Exit Glacier and Harding Icefield trail hike, Alaska SeaLife Center, Resurrection Bay sea kayaking, Mount Marathon hike (July 4th race route), Seward harbor walk, and halibut fishing charters."
""",
        "scottTips": """  logistics: "Drive from Anchorage — 127 miles, 2.5 hours on the Seward Highway (one of Alaska's most scenic drives along Turnagain Arm). The Alaska Railroad runs summer trains ($70-100 each way). Book boat tours and lodging well in advance for summer."
  bestTime: "June through August for peak activities and weather. July 4th for the Mount Marathon Race and town celebration. September for fall colors and fewer crowds on the boat tours."
  gettingAround: "Car to get here. Town is very walkable once you arrive. Exit Glacier is 9 miles by road. Boat tours depart from the harbor."
  money: "Mid-range Alaska prices. Budget $80-150/day. The Seward Highway drive to town is free and beautiful. The boat tour is the main expense — worth it."
  safety: "Harding Icefield trail: start early, be off the exposed upper section before afternoon weather builds. Bears near Exit Glacier on the upper trail. Cold water in Resurrection Bay — proper gear for kayaking."
  packing: "Layers and rain gear, waterproof hiking boots, warm layers for boat trips (much colder on the water), sun protection, bear spray for upper trail hikes, trekking poles for Harding Icefield."
  localCulture: "Seward is a working port town with a tourism layer. The commercial fishing fleet is real and active. The Alaska SeaLife Center does genuine marine research and rehabilitation. Mount Marathon's July 4th race has been run since 1915 — it's not just a tourist event."
"""
    },
    "sitka": {
        "aeo": "Sitka is Southeast Alaska's most culturally rich town — a former Russian colonial capital and historic Tlingit homeland surrounded by volcanic peaks and ocean, with world-class bald eagle viewing and sea kayaking, budget $100-250/day, best May through September.",
        "video_title": "Russian Alaska",
        "video_text": "Sitka was the capital of Russian America — the onion dome of St. Michael's Cathedral still watches over a town where Tlingit culture and Russian history intersect at the edge of the Pacific.",
        "gradient": "linear-gradient(135deg, #7c2d12, #1d4ed8, #14532d)",
        "affiliatePicks": """  - name: "Sitka Hotel"
    type: hotel
    price: "$140-240/night"
    personalNote: "Well-located downtown hotel that captures the character of Sitka without the resort premium. Good value for a city with limited mid-range options."
    affiliateUrl: "https://www.booking.com/hotel/us/sitka-hotel.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Sitka Whale Watching and Wildlife Tour"
    type: tour
    price: "$140-180/person"
    personalNote: "Sitka's waters host humpback whales, orcas, sea otters, and Steller sea lions in extraordinary proximity. The rocky island landscape makes every trip dramatically scenic."
    affiliateUrl: "https://www.getyourguide.com/sitka-l456/whale-watching-t56789/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Sitka National Historical Park Tour"
    type: tour
    price: "$15-50/person"
    personalNote: "Where Tlingit warriors fought Russian forces in 1804 — the totem pole collection is outstanding and the cultural interpretation is excellent. One of the most significant sites in Alaska."
    affiliateUrl: "https://www.getyourguide.com/sitka-l456/historical-park-tour-t67890/?partner_id=IVN6IQ3"
  - name: "Sitka Sea Kayaking"
    type: tour
    price: "$80-150/person"
    personalNote: "Paddling through Sitka Sound's island-dotted waters, with sea otters floating on kelp beds and volcanic peaks as backdrop, is one of Southeast Alaska's best kayak experiences."
    affiliateUrl: "https://www.getyourguide.com/sitka-l456/sea-kayaking-t78901/?partner_id=IVN6IQ3"
""",
        "faqItems": """  - question: "Is Sitka worth visiting?"
    answer: "Yes — Sitka is the most historically and culturally rich town in Southeast Alaska. The Russian colonial heritage, Tlingit history, Sitka National Historical Park totem poles, world-class bald eagle center, and dramatic volcanic island setting make it stand apart from other Alaska ports."
  - question: "Best time to visit Sitka?"
    answer: "May through September. June through August for the best weather and full range of activities. The Alaska Raptor Center's bald eagle patients are present year-round. The Sitka Summer Music Festival in June attracts internationally renowned chamber musicians. Whale watching runs April through November."
  - question: "How many days in Sitka?"
    answer: "Two to three days. Day one: Sitka National Historical Park, Russian Bishop's House, St. Michael's Cathedral. Day two: whale watching tour or sea kayaking. Day three: Alaska Raptor Center and Mount Edgecumbe area hiking."
  - question: "Is Sitka safe?"
    answer: "Very safe and walkable. The main risks are trails that can be slippery in rain, cold water for kayaking, and bears on hiking trails outside town. Weather can change quickly."
  - question: "Sitka on a budget?"
    answer: "Budget $100-140/day. The free Sitka National Historical Park trail and totem poles are excellent value. The Alaska Raptor Center ($15) is essential. Avoid cruise ship peak days in the summer for the best experience."
  - question: "What is Sitka known for?"
    answer: "Former capital of Russian America — the last place sold to the United States in the 1867 Alaska Purchase ceremony. Sitka National Historical Park — where the 1804 Tlingit-Russian battle occurred, with the best totem pole collection in Southeast Alaska. The Alaska Raptor Center (bald eagle rehabilitation). St. Michael's Cathedral (Russian Orthodox). World-class sea kayaking."
  - question: "Do I need a car in Sitka?"
    answer: "No. Downtown Sitka is very walkable and all major attractions are within walking distance. Alaska Airlines flies into Sitka airport; a small water ferry connects the airport to downtown."
  - question: "Best things to do in Sitka?"
    answer: "Sitka National Historical Park and totem poles, Alaska Raptor Center bald eagle viewing, St. Michael's Cathedral, Russian Bishop's House, whale watching, sea kayaking in Sitka Sound, Fortress of the Bear brown bear viewing, and the Sitka Sound Science Center."
""",
        "scottTips": """  logistics: "Alaska Airlines serves Sitka directly from Seattle and connects through Juneau and Ketchikan. The Alaska Marine Highway serves Sitka on the Inside Passage route. Water taxi runs from the airport to downtown ($15)."
  bestTime: "May through September. June for the Summer Music Festival. Cruise ship traffic peaks July-August — visit early morning before ships arrive for the best experience in town."
  gettingAround: "Very walkable — everything major is within walking distance of downtown. Bikes are great for exploring further. No car needed."
  money: "Budget $100-150/day. The best experiences (Sitka NHP, waterfront walks) are free or minimal cost. Whale watching ($140-180) is the main splurge."
  safety: "Safe and walkable. Standard Southeast Alaska rain hazard on trails. Cold water for kayaking — proper gear essential."
  packing: "Rain gear (essential), binoculars (eagle center, whale watching, sea otters), warm layers, camera."
  localCulture: "Sitka has three overlapping cultural identities: Tlingit homeland, Russian colonial capital, and American frontier town. The Alaska Native Brotherhood was founded here in 1912. The Russian Orthodox community still holds regular services at St. Michael's Cathedral. Engage with all three layers."
"""
    },
    "skagway": {
        "aeo": "Skagway is a living gold rush museum — a perfectly preserved 1898 boomtown at the head of the Lynn Canal, gateway to the Chilkoot Trail, and one of Southeast Alaska's most visited cruise ship ports, budget $90-200/day, best May through September.",
        "video_title": "Gold Rush Town",
        "video_text": "Skagway's entire downtown is a National Historic Landmark — the original gold rush boomtown where 100,000 prospectors launched their Klondike journeys, preserved almost exactly as they left it.",
        "gradient": "linear-gradient(135deg, #92400e, #1c1917, #854d0e)",
        "affiliatePicks": """  - name: "White House Bed and Breakfast"
    type: hotel
    price: "$130-220/night"
    personalNote: "Historic building with genuine Skagway character. The breakfast is excellent and the owners know the trail and hiking options better than anyone in town."
    affiliateUrl: "https://www.booking.com/hotel/us/white-house-skagway.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "White Pass & Yukon Route Railway"
    type: tour
    price: "$145-200/person"
    personalNote: "The most spectacular narrow-gauge railway in North America, climbing 3,000 feet from sea level to White Pass summit in 27 miles. Summit excursions run May-September — this is the iconic Skagway experience."
    affiliateUrl: "https://www.getyourguide.com/skagway-l567/white-pass-railway-t67890/?partner_id=IVN6IQ3"
    badge: "Don't Miss"
  - name: "Chilkoot Trail Guided Trek"
    type: tour
    price: "$300-600/person"
    personalNote: "The legendary 33-mile trail the 1898 gold rush stampeders climbed. A multi-day hike through US and Canadian history. Guided trips handle logistics; self-guided requires advance Parks Canada permits."
    affiliateUrl: "https://www.getyourguide.com/skagway-l567/chilkoot-trail-hike-t78901/?partner_id=IVN6IQ3"
  - name: "Hiking Poles"
    type: activity
    price: "$30-80"
    personalNote: "Essential for the Chilkoot Trail's steep Golden Staircase section. The 45-degree boulder field near the summit is where the stampeders' photos were taken — poles make it manageable."
    affiliateUrl: "https://www.amazon.com/s?k=trekking+poles+collapsible&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Skagway worth visiting?"
    answer: "Yes, especially for the White Pass & Yukon Route Railway and the Chilkoot Trail. The gold rush history here is not re-created — it is the real buildings, the real trail, the real story. Even if you have no interest in history, the scenery of the Lynn Canal and White Pass is stunning."
  - question: "Best time to visit Skagway?"
    answer: "May through September. The White Pass Railway and main services run May-September. October through April sees the town scale back dramatically — most businesses close. Skagway has a very seasonal tourist economy."
  - question: "How many days in Skagway?"
    answer: "Two to three days. Day one for the Klondike Gold Rush National Historical Park and downtown buildings. Day two for the White Pass Railway. Day three for a Chilkoot Trail day hike (first 7 miles are accessible as a day trip)."
  - question: "Is Skagway safe?"
    answer: "Very safe in town. The Chilkoot Trail is challenging and requires proper preparation — the upper sections in snow can be difficult. The White Pass Railway is completely safe. Weather in the mountains can change rapidly."
  - question: "Skagway on a budget?"
    answer: "The Klondike Gold Rush National Historical Park, which includes most of the historic downtown, is free. Budget $90-130/day. The White Pass Railway ($145-200) is the main expense but truly worth it."
  - question: "What is Skagway known for?"
    answer: "The 1898 Klondike Gold Rush gateway. The best-preserved gold rush frontier town in America (National Historic Landmark district). The White Pass & Yukon Route Railway. The Chilkoot Trail — a 33-mile National Historic Trail and one of North America's most storied hikes. The infamous swindler Soapy Smith."
  - question: "Do I need a car in Skagway?"
    answer: "No — Skagway is tiny and completely walkable. The White Pass Railway depot is walkable from anywhere in town. The Alaska Marine Highway ferry and cruise ships are the primary access. There is also a road connection to the Alaska Highway via Canada."
  - question: "Best things to do in Skagway?"
    answer: "White Pass & Yukon Route Railway summit excursion, Klondike Gold Rush NHP ranger programs and historic buildings, Chilkoot Trail hiking (day hike to Finnegan's Point or multi-day to Lake Bennett), Skagway Museum, Gold Rush Cemetery (where Soapy Smith is buried), and the Liarsville Gold Rush Trail Camp."
""",
        "scottTips": """  logistics: "Alaska Airlines flies into Skagway (SGY) from Juneau. Alaska Marine Highway ferry arrives from Haines (1 hour) and Juneau (4.5 hours). There is a road connection via the Klondike Highway through Whitehorse, Yukon — a dramatic option."
  bestTime: "May through September — the town is essentially closed outside these months. Weekdays are better than weekends when multiple cruise ships dock simultaneously."
  gettingAround: "Walking. Skagway is tiny — everything is within 10 minutes on foot. The White Pass Railway depot is in town."
  money: "Skagway is a tourist town — prices reflect that. Budget $90-150/day. The Klondike Gold Rush NHP is free. The railway ($145-200) is the main expense."
  safety: "Chilkoot Trail upper section can have snow year-round and requires good preparation. Mountain weather changes fast. In town, completely safe."
  packing: "Layers for variable mountain weather, rain gear, hiking poles for the Chilkoot, sturdy hiking boots."
  localCulture: "Skagway is a town that owes its entire existence to the gold rush of 1898. The National Park Service does an outstanding job interpreting this history with ranger-led tours and living history programs. Soapy Smith's legacy is particularly fascinating — the con man who ran the town until a shootout ended his career."
"""
    },
    "talkeetna": {
        "aeo": "Talkeetna is a tiny quirky town 115 miles north of Anchorage — the base camp for Denali climbing expeditions, famous for flightseeing over the Alaska Range, with a bohemian small-town character unlike anywhere else in Alaska, budget $80-200/day, best May through September.",
        "video_title": "Denali Basecamp",
        "video_text": "Talkeetna's floatplane operators launch climbers toward the summit of Denali each spring — the same Main Street bars serve mountaineers at altitude training and tourists in equal measure.",
        "gradient": "linear-gradient(135deg, #1c1917, #0c4a6e, #166534)",
        "affiliatePicks": """  - name: "Talkeetna Alaskan Lodge"
    type: hotel
    price: "$250-450/night"
    personalNote: "The premium Talkeetna option with stunning views of the Alaska Range including Denali on clear days. The deck at sunset with the mountain lit pink is extraordinary."
    affiliateUrl: "https://www.booking.com/hotel/us/talkeetna-alaskan-lodge.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Denali Flightseeing with Glacier Landing"
    type: tour
    price: "$300-400/person"
    personalNote: "Land on a glacier on Denali with K2 Aviation or Talkeetna Air Taxi. On a clear day this is one of the best experiences in Alaska — close views of the Alaska Range that are impossible from the ground."
    affiliateUrl: "https://www.getyourguide.com/talkeetna-l678/denali-flightseeing-t78901/?partner_id=IVN6IQ3"
    badge: "Don't Miss"
  - name: "Talkeetna River Rafting"
    type: tour
    price: "$75-120/person"
    personalNote: "Float the Talkeetna River through spruce and birch forests with mountain views. A relaxed option that shows the landscape from water level."
    affiliateUrl: "https://www.getyourguide.com/talkeetna-l678/river-rafting-t89012/?partner_id=IVN6IQ3"
  - name: "Alaska Range Summit Photography Book"
    type: activity
    price: "$30-50"
    personalNote: "If the mountain captures you, Bradford Washburn's photography of Denali and the Alaska Range from the air is incomparable context for what you're seeing."
    affiliateUrl: "https://www.amazon.com/s?k=denali+alaska+range+photography+book&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Talkeetna worth visiting?"
    answer: "Yes — especially combined with Denali National Park. The flightseeing over the Alaska Range is superb, the town has genuine bohemian character (residents elected a cat as honorary mayor for years), and it is the authentic base for Denali climbers. A day or two here adds enormous value to any Denali trip."
  - question: "Best time to visit Talkeetna?"
    answer: "May through September. May-June for Denali climbing season and spring conditions. June-July for maximum daylight and warmth. The Talkeetna Bluegrass Festival in August is excellent. September for fall colors and fewer tourists."
  - question: "How many days in Talkeetna?"
    answer: "One to two days is typical — most visitors stop en route to or from Denali. One day for the flightseeing trip and the Main Street walk. Two days to add river rafting and properly experience the quirky town culture."
  - question: "Is Talkeetna safe?"
    answer: "Very safe and relaxed. The flightseeing is conducted by FAA-certified operators with decades of experience. River rafting is on Class II water appropriate for families. Bears are present on backcountry trails."
  - question: "Talkeetna on a budget?"
    answer: "Budget $80-120/day. The flightseeing ($300-400) is the main splurge. Talkeetna's bars and restaurants are reasonably priced. The Railroad Depot Museum is modest and free."
  - question: "What is Talkeetna known for?"
    answer: "The base for Denali climbing expeditions — all climbers must register here with the National Park Service. Denali flightseeing with glacier landings. A famously quirky small-town character. The Alaska Railroad depot and the Susitna and Talkeetna Rivers confluence. Nagley's Store, where Stubbs the cat was honorary mayor for over two decades."
  - question: "Do I need a car in Talkeetna?"
    answer: "Yes to get here — Talkeetna is 115 miles north of Anchorage via Parks Highway, then 14 miles on the Talkeetna Spur Road. The Alaska Railroad also stops here (scenic, slower option). In town, everything is walkable."
  - question: "Best things to do in Talkeetna?"
    answer: "Denali flightseeing with glacier landing, Talkeetna River float trip, Main Street walk (quirky local shops and bars), Alaska Range views from the hilltop, Denali National Park Service ranger station (climber registration), Nagley's Store, and the Talkeetna Historical Museum."
""",
        "scottTips": """  logistics: "Drive from Anchorage: 115 miles north on Parks Highway to the Talkeetna Spur Road, then 14 miles to town (about 2.5 hours). Or take the Alaska Railroad from Anchorage (about 4 hours, very scenic). Car rental in Anchorage is the most flexible option."
  bestTime: "Late May through early September. May-June during Denali climbing season when you can watch expeditions depart. Late September for fall colors — the birch turn gold and the light is extraordinary."
  gettingAround: "Tiny town — everything walkable. Car for getting here."
  money: "Moderate by Alaska standards. Budget $80-150/day. Flightseeing ($300-400) is the big expense. Food and accommodation are reasonable."
  safety: "Very safe. Flightseeing operators are experienced. Backcountry areas have bears — carry spray."
  packing: "Layers for variable weather, camera (the Alaska Range views are extraordinary), binoculars for spotting wildlife and climbers on the mountain."
  localCulture: "Talkeetna has a genuine counterculture streak — artists, guides, climbers, and independent spirits who chose this remote small town. The climbing community is serious and respected. Don't treat the mountaineers like attractions. Nagley's Store is 100 years old and still a community hub."
"""
    },
    "utqiagvik": {
        "aeo": "Utqiagvik (formerly Barrow) is America's northernmost city — 330 miles above the Arctic Circle on the Arctic Ocean coast, with polar bear viewing, Inupiaq culture, and the midnight sun (mid-May to early August), budget $150-300/day, accessible only by air.",
        "video_title": "Top of the World",
        "video_text": "Utqiagvik sits on the Arctic Ocean at 71 degrees north — the northernmost point in America, where the sun does not set for 82 days each summer and polar bears roam the frozen sea.",
        "gradient": "linear-gradient(135deg, #0c4a6e, #e2e8f0, #1e3a5f)",
        "affiliatePicks": """  - name: "Top of the World Hotel"
    type: hotel
    price: "$180-280/night"
    personalNote: "The primary hotel in Utqiagvik — reliable, warm (essential), and centrally located. Limited options exist in this remote community; book well in advance."
    affiliateUrl: "https://www.booking.com/hotel/us/top-of-the-world-hotel-barrow.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Utqiagvik Arctic Cultural Tour"
    type: tour
    price: "$100-200/person"
    personalNote: "A guided cultural tour is the most respectful and informative way to experience Utqiagvik. Local Inupiaq guides provide context for the culture, subsistence traditions, and Arctic environment."
    affiliateUrl: "https://www.getyourguide.com/utqiagvik-l890/arctic-cultural-tour-t90123/?partner_id=IVN6IQ3"
    badge: "Essential"
  - name: "Arctic National Wildlife Refuge Photography Tour"
    type: tour
    price: "$300-600/person"
    personalNote: "For photographers and wildlife enthusiasts, guided trips into the surrounding Arctic tundra for polar bears, Arctic foxes, snowy owls, and the extraordinary Arctic landscapes."
    affiliateUrl: "https://www.getyourguide.com/utqiagvik-l890/arctic-wildlife-tour-t01234/?partner_id=IVN6IQ3"
  - name: "Extreme Cold Weather Gear"
    type: activity
    price: "$100-300"
    personalNote: "Winters in Utqiagvik are brutal — minus 40°F and below. Even summer visits require serious layering. Don't improvise with inadequate gear at this latitude."
    affiliateUrl: "https://www.amazon.com/s?k=extreme+cold+weather+clothing+arctic&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Utqiagvik worth visiting?"
    answer: "For those fascinated by the Arctic, Inupiaq culture, or extreme geography, yes. It is not a comfortable tourist destination — it is a genuine Arctic indigenous community that happens to be the northernmost city in America. The experience of standing on the Arctic Ocean shore, in a whaling culture that has existed for thousands of years, is profound."
  - question: "Best time to visit Utqiagvik?"
    answer: "Mid-May through early August for the midnight sun (the sun does not set for 82 days, from May 12 to August 1). October-November for the polar night begins. Spring (April-May) when sea ice is still firm and subsistence whaling takes place. Winter for the most intense Arctic experience."
  - question: "How many days in Utqiagvik?"
    answer: "Two to three days is typical. Day one for cultural orientation, Iñupiat Heritage Center, and Arctic Ocean shoreline. Day two for a cultural or wildlife tour. Day three for the surrounding tundra and wildlife."
  - question: "Is Utqiagvik safe?"
    answer: "Safe but requires serious weather preparation. Temperatures can fall to minus 50°F with wind chill in winter. Polar bears are present near the community and genuinely dangerous. Locals know bear safety intimately — follow their guidance. A guided cultural tour is strongly recommended."
  - question: "Utqiagvik on a budget?"
    answer: "Difficult and expensive — flights from Anchorage alone run $400-800+. Budget $150-250/day on the ground. This is not a budget destination. The cultural experience justifies the cost for the right traveler."
  - question: "What is Utqiagvik known for?"
    answer: "America's northernmost city. The midnight sun (82 days of continuous daylight in summer). Polar night (67 days of no sun in winter). The Iñupiat whaling culture, one of the most ancient and ongoing in the world. Polar bears on the sea ice. The summer Arctic Ocean coastline."
  - question: "Do I need a car in Utqiagvik?"
    answer: "No car is necessary in the community itself. Roads are limited and there is no road connection to the outside world. Alaska Airlines flies daily from Anchorage."
  - question: "Best things to do in Utqiagvik?"
    answer: "Iñupiat Heritage Center, Arctic Ocean shoreline walk, cultural tours with local guides, whale bone arch (Inupiaq heritage marker), spring whaling season (April-May), polar bear viewing (fall), and midnight sun observation (May-August)."
""",
        "scottTips": """  logistics: "Alaska Airlines flies daily from Anchorage to Utqiagvik (BRW) — about 1.5 hours, $400-800+ round trip. No road connection exists. Book flights and the one main hotel well in advance."
  bestTime: "Mid-May through August for midnight sun. The Nalukataq whaling festival in June (blanket toss celebration) is a significant cultural event. Winter for the most authentic Arctic experience, if you're equipped."
  gettingAround: "Walking and taxis in the community. No car needed or possible for beyond-community access."
  money: "Expensive — budget $150-280/day including flights. Food is expensive due to the cost of everything shipped to an Arctic community."
  safety: "Polar bears are present and dangerous near the community — especially in fall as sea ice forms. Always ask locals about current bear activity before going near the shore. Extreme cold weather preparation is non-negotiable in winter."
  packing: "For summer: layers, hat and gloves even in July (average summer temperatures 40-50°F), and an eye mask for sleeping during 24-hour sunlight. For winter: expedition-grade cold weather gear, rated to minus 50°F."
  localCulture: "Utqiagvik is a living Inupiaq community, not a tourism destination. The subsistence whaling culture is ancient, ongoing, and sacred. Engage with genuine respect and humility. The Iñupiat Heritage Center is the starting point for understanding the community you're visiting. Ask before photographing people."
"""
    },
    "valdez": {
        "aeo": "Valdez is a small Prince William Sound port town surrounded by some of Alaska's most dramatic fjord scenery — the terminus of the Trans-Alaska Pipeline, world-class Columbia Glacier viewing, and extreme skiing, budget $90-220/day, best May through September.",
        "video_title": "Prince William Sound",
        "video_text": "Valdez sits deep in a fjord encircled by peaks reaching 5,000 feet — the head of Prince William Sound and the terminus of the Trans-Alaska Pipeline, surrounded by wilderness on every side.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #0c4a6e, #334155)",
        "affiliatePicks": """  - name: "Best Western Valdez Harbor Inn"
    type: hotel
    price: "$140-240/night"
    personalNote: "The most reliable lodging option in Valdez with harbor views and walking distance to boat tour departures. Book in advance for summer weekends."
    affiliateUrl: "https://www.booking.com/hotel/us/best-western-valdez-harbor-inn.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Columbia Glacier Boat Tour"
    type: tour
    price: "$100-160/person"
    personalNote: "Columbia Glacier is one of the largest tidewater glaciers in the world — a full-day boat tour from Valdez navigates through icebergs to the massive calving face. Wildlife sightings (orcas, sea lions, seals) are common."
    affiliateUrl: "https://www.getyourguide.com/valdez-l789/columbia-glacier-tour-t89012/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Valdez Kayaking in Prince William Sound"
    type: tour
    price: "$80-200/person"
    personalNote: "Day kayak tours from Valdez through the fjords of Prince William Sound — bald eagles overhead, sea otters in the kelp, and mountain reflections in the water. Excellent guided options available."
    affiliateUrl: "https://www.getyourguide.com/valdez-l789/kayaking-prince-william-sound-t90123/?partner_id=IVN6IQ3"
  - name: "Binoculars (10x42)"
    type: activity
    price: "$150-300"
    personalNote: "Essential for the Columbia Glacier tour — the iceberg field requires binoculars to spot the wildlife and the detail of the glacier face from the boat."
    affiliateUrl: "https://www.amazon.com/s?k=10x42+binoculars+birdwatching&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Valdez worth visiting?"
    answer: "Yes — the Columbia Glacier boat tour alone justifies the trip. One of the world's largest tidewater glaciers, navigating through icebergs the size of buildings, with orcas surfacing nearby — it is a world-class Alaska experience. The fjord scenery and Columbia Glacier icefield backdrop are extraordinary."
  - question: "Best time to visit Valdez?"
    answer: "May through September. July and August for glacier tours and the calmest weather. The Trans-Alaska Pipeline Terminal tours are available summer only. Extreme skiing (heli-ski and Valdez is known globally for it) runs March-April."
  - question: "How many days in Valdez?"
    answer: "Two to three days. Day one: town, pipeline terminal area, Cropper Mineral Trail. Day two: Columbia Glacier full-day boat tour. Day three: Prince William Sound kayaking."
  - question: "Is Valdez safe?"
    answer: "Safe. The boat tours are professionally operated. The Richardson Highway connecting Valdez to the Glenn Highway is a stunning but remote drive — be prepared for winter driving conditions in shoulder seasons. Bears in the surrounding area."
  - question: "Valdez on a budget?"
    answer: "Budget $90-140/day. The Columbia Glacier tour ($100-160) is the main expense. The pipeline terminal area viewpoint is free. Keystone Canyon waterfall walk is free and stunning."
  - question: "What is Valdez known for?"
    answer: "The Columbia Glacier — one of the world's largest tidewater glaciers. The terminus of the 800-mile Trans-Alaska Pipeline. Extreme heli-skiing on some of the most radical terrain in North America. Keystone Canyon with its ice climbing routes. The 1989 Exxon Valdez oil spill (the environmental tragedy that transformed US maritime law)."
  - question: "Do I need a car in Valdez?"
    answer: "Yes — Valdez is 304 miles from Anchorage via the Richardson Highway, one of Alaska's most dramatic drives. The road section through Keystone Canyon is spectacular. Once in town, a car is useful for the terminal area and hiking trailheads."
  - question: "Best things to do in Valdez?"
    answer: "Columbia Glacier full-day boat tour, Prince William Sound kayaking, Keystone Canyon waterfall hike, Trans-Alaska Pipeline Terminal viewpoint, Valdez Museum (1964 earthquake and oil spill history), Mineral Creek hiking trail, and the Richardson Highway drive from Anchorage."
""",
        "scottTips": """  logistics: "Drive from Anchorage: 304 miles via Glenn and Richardson Highways — a magnificent 6-7 hour drive through Matanuska Valley, Wrangell St. Elias mountains, and Keystone Canyon. Alaska Airlines flies seasonally. Book boat tours in advance for summer."
  bestTime: "May through September for boat tours and hiking. March-April for extreme skiing on Valdez's famous steep terrain."
  gettingAround: "Car to get here. Town is small and walkable. Boat tours depart from the harbor."
  money: "Budget $90-160/day. Columbia Glacier tour ($100-160) is the main expense. The Richardson Highway drive itself is free and extraordinary."
  safety: "Columbia Glacier boat tours: icebergs can roll without warning — operators maintain safe distances. Richardson Highway is beautiful but remote — carry emergency supplies, especially in shoulder seasons. Bears near trails."
  packing: "Warm layers for glacier boat tours (much colder near the ice face), rain gear, binoculars for wildlife and glacier detail, camera."
  localCulture: "Valdez rebuilt itself after the 1964 Good Friday Earthquake destroyed the original townsite — the current town is a planned community relocated 4 miles from the original. The 1989 Exxon Valdez spill scars are still visible in the community's environmental consciousness. The pipeline and the spill are two defining chapters in the same story."
"""
    },
    "whittier": {
        "aeo": "Whittier is an unusual one-road Alaska town where most of the population lives in a single 14-story building — the primary Prince William Sound access point for kayaking, glacier tours, and humpback whale watching, budget $80-200/day, best May through September.",
        "video_title": "One Tunnel Town",
        "video_text": "Whittier is reached only by a single road tunnel shared with the railroad — a town where 250 people live mostly in one building, surrounded by glaciers and the waters of Prince William Sound.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #134e4a, #1c1917)",
        "affiliatePicks": """  - name: "Prince William Sound Cruise"
    type: tour
    price: "$130-180/person"
    personalNote: "The definitive reason to come to Whittier — Phillips Cruises and Tours runs excellent day trips through the sound with tidewater glaciers, humpback whales, sea otters, and dramatic fjord scenery."
    affiliateUrl: "https://www.getyourguide.com/whittier-l890/prince-william-sound-cruise-t01234/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Whittier Glacier Kayaking"
    type: tour
    price: "$150-300/person"
    personalNote: "Prince William Sound kayaking from Whittier puts you in some of Alaska's most dramatic and accessible fjord landscapes. Guided day trips can reach glacier faces that larger boats cannot."
    affiliateUrl: "https://www.getyourguide.com/whittier-l890/glacier-kayaking-t12345/?partner_id=IVN6IQ3"
  - name: "Portage Glacier Visitor Center"
    type: activity
    price: "$15-30/person"
    personalNote: "On the drive to Whittier, stop at Portage Glacier — a free visitor center with a Portage Lake boat tour that approaches the glacier face. The 5-mile Portage Glacier Road is also worth driving."
    affiliateUrl: "https://www.getyourguide.com/portage-glacier-l901/glacier-boat-tour-t23456/?partner_id=IVN6IQ3"
  - name: "Sea Kayak Dry Bag (waterproof)"
    type: activity
    price: "$20-40"
    personalNote: "Essential for kayaking in Prince William Sound — everything from your phone to extra clothing must stay dry. Glacier-fed water is dangerously cold."
    affiliateUrl: "https://www.amazon.com/s?k=dry+bag+kayaking+waterproof&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Whittier worth visiting?"
    answer: "Yes, as a day trip from Anchorage or as a base for Prince William Sound kayaking. The town itself is fascinating in an unusual way — its military history and one-building residential structure are genuinely strange. The sound boat tours from Whittier are excellent and shorter to reach than Seward."
  - question: "Best time to visit Whittier?"
    answer: "May through September. The Anton Anderson Memorial Tunnel is open year-round. Boat tours and kayaking operate May-September. Humpback whale activity peaks July-August."
  - question: "How many days in Whittier?"
    answer: "One to two days is typical. Day one for the town exploration and a boat tour. Day two for a kayaking trip. Most visitors do Whittier as a day trip from Anchorage (60 miles)."
  - question: "Is Whittier safe?"
    answer: "Safe. The Anton Anderson tunnel has strict traffic direction schedules — know when it is open to your direction before departing. Standard boat and kayaking safety applies."
  - question: "Whittier on a budget?"
    answer: "Budget $80-130/day. The boat tour ($130-180) is the main expense. The drive from Anchorage through the tunnel is inexpensive. Portage Glacier stop on the way adds minimal cost."
  - question: "What is Whittier known for?"
    answer: "The Anton Anderson Memorial Tunnel — one of the longest road/rail shared tunnels in North America (2.5 miles). The Begich Towers condominium building where most of Whittier's 250 residents live. Prince William Sound glacier and wildlife tours. Its origin as a WWII military port. The world's highest average precipitation (over 200 inches per year)."
  - question: "Do I need a car in Whittier?"
    answer: "Yes to get here — Whittier is reached via the Anton Anderson tunnel from Portage (Highway 1). The tunnel schedule is specific; plan your timing. Once in town, everything is walkable."
  - question: "Best things to do in Whittier?"
    answer: "Prince William Sound day cruise, glacier kayaking, exploring Begich Towers building, walking the Shotgun Cove trail, visiting Portage Glacier on the way in, and the Whittier Museum (WWII history and community story)."
""",
        "scottTips": """  logistics: "Drive from Anchorage: 60 miles via Seward Highway to the Portage tunnel entrance. The Anton Anderson tunnel operates on alternating single-direction schedules — check the schedule at dot.alaska.gov before you drive. The tunnel toll is $13 each way."
  bestTime: "June through August for boat tours and optimal weather. The drive through the Chugach Mountains to the tunnel is scenic year-round."
  gettingAround: "Car to get here. Town is completely walkable. Boat tours depart from the small boat harbor."
  money: "Budget $80-130/day. More affordable than Seward for a similar Prince William Sound experience. The tunnel toll is the hidden cost ($13 each direction)."
  safety: "Tunnel schedule timing is critical — you can be stranded for an hour on the wrong side if you miss the window. Boat tours: cold water, proper gear for kayaking."
  packing: "Rain gear (Whittier is one of the rainiest places in Alaska — over 200 inches/year), warm layers, binoculars."
  localCulture: "Whittier has one of the strangest community stories in America — a WWII military port that became a civilian town where everyone literally lives in the same building. The Begich Towers residents have created a genuine community inside a concrete tower originally built for military personnel. The Whittier Museum tells this unusual story well."
"""
    },
    "wrangell-st-elias": {
        "aeo": "Wrangell-St. Elias is the largest national park in America — bigger than Switzerland — a remote Alaska wilderness of glaciers, volcanoes, and gold rush ghost towns accessible by road from Anchorage, budget $80-300/day, best June through August.",
        "video_title": "America's Largest Park",
        "video_text": "Wrangell-St. Elias is six times the size of Yellowstone — a landscape of active volcanoes, the largest non-polar glacier system in the world, and the ghost town of Kennicott still standing in mountain copper country.",
        "gradient": "linear-gradient(135deg, #14532d, #7c2d12, #0c4a6e)",
        "affiliatePicks": """  - name: "Kennicott Glacier Lodge"
    type: hotel
    price: "$280-450/night"
    personalNote: "Historic lodge in the heart of the Kennicott copper mining ghost town, surrounded by glaciers and mountains. An extraordinary location — you wake up in wilderness history."
    affiliateUrl: "https://www.booking.com/hotel/us/kennicott-glacier-lodge.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Root Glacier Guided Ice Walk"
    type: tour
    price: "$75-150/person"
    personalNote: "Walk on the Root Glacier with crampons and guides — one of the most accessible glacier walking experiences in Alaska. The blue ice and crevasse views are extraordinary."
    affiliateUrl: "https://www.getyourguide.com/wrangell-st-elias-l012/root-glacier-ice-walk-t12345/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Kennicott Historic Mine Tour"
    type: tour
    price: "$25-55/person"
    personalNote: "The Kennicott copper mine processed $200 million in copper and then was abandoned overnight in 1938 — the buildings and equipment are frozen in time. A fascinating industrial ghost tour."
    affiliateUrl: "https://www.getyourguide.com/wrangell-st-elias-l012/kennicott-mine-tour-t23456/?partner_id=IVN6IQ3"
  - name: "Bear Spray (Counter Assault)"
    type: activity
    price: "$50-70"
    personalNote: "Required for all Wrangell-St. Elias backcountry. Grizzly and black bear populations are significant throughout the park."
    affiliateUrl: "https://www.amazon.com/s?k=counter+assault+bear+spray&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Wrangell-St. Elias worth visiting?"
    answer: "Yes — it is the most undiscovered major national park in America. Six times the size of Yellowstone, with the largest non-polar glacier system in the world, active volcanoes, and the best-preserved copper mining ghost town in North America. Far fewer visitors than any comparable park."
  - question: "Best time to visit Wrangell-St. Elias?"
    answer: "June through August. The Nabesna and McCarthy Roads are most passable June-August. McCarthy and Kennicott services are seasonal. May and September can be beautiful but road conditions are variable. Winter access is extremely limited and backcountry conditions serious."
  - question: "How many days in Wrangell-St. Elias?"
    answer: "Minimum three days. Day one: drive the McCarthy Road (5-6 hours of gravel), arrive at McCarthy/Kennicott. Day two: Root Glacier ice walk and Kennicott mine tour. Day three: backcountry hiking or flightseeing. Five to seven days allows more exploration."
  - question: "Is Wrangell-St. Elias safe?"
    answer: "Safe with preparation. The McCarthy Road is 60 miles of gravel and requires a high-clearance vehicle — flat tires are common, carry two spares. The backcountry has grizzlies; carry spray. The Kennicott buildings (historic mine structures) are accessed by guided tours only for safety."
  - question: "Wrangell-St. Elias on a budget?"
    answer: "Budget $80-150/day camping. The park has no entrance fee. Camping at Kennicott is $12/night. The Root Glacier walk ($75-150) is the essential guided experience. The historic buildings of McCarthy are free to explore."
  - question: "What is Wrangell-St. Elias known for?"
    answer: "America's largest national park (13.2 million acres). Nine of the 16 highest peaks in the US. The largest non-polar glacier system in the world (the Bagley Icefield). Kennicott — a perfectly preserved copper mining ghost town. Active volcanoes (Mt. Wrangell). No entrance fee."
  - question: "Do I need a car in Wrangell-St. Elias?"
    answer: "Yes — a high-clearance vehicle with at least two spare tires is required for the McCarthy Road. The road is 60 miles of gravel with significant washboard sections. Do not drive a standard sedan. Fly-in via air taxi is the alternative."
  - question: "Best things to do in Wrangell-St. Elias?"
    answer: "Root Glacier ice walk (crampons provided), Kennicott historic mine tour, McCarthy town exploration, Wrangell Mountains flightseeing, Bonanza Mine Ridge hike from Kennicott, Erie Lake overlook, and backcountry wilderness camping."
""",
        "scottTips": """  logistics: "Drive from Anchorage: 5-6 hours to the McCarthy Road turnoff (via Glenn Highway through Glennallen). Then 60 miles of gravel McCarthy Road to the footbridge and McCarthy/Kennicott. High-clearance vehicle with two spares is mandatory. Air taxi from Gulkana is an alternative."
  bestTime: "June through August. July has the driest weather and most stable road conditions. Leave early on the McCarthy Road to arrive by afternoon."
  gettingAround: "Car to the McCarthy Road end, then walk across the footbridge. The Kennicott shuttle runs the 4.5 miles from McCarthy to Kennicott ($5 each way). Within Kennicott, everything is walkable."
  money: "No entrance fee — one of the great bargains in the park system. Budget $80-200/day depending on lodging choice. The Kennicott Glacier Lodge is a splurge worth making at least one night."
  safety: "McCarthy Road flat tires are common — bring two full-size spares, a pump, and tire plugs. Grizzlies throughout the park; carry spray. Don't enter historic Kennicott mine buildings without a guide."
  packing: "High-clearance vehicle kit (two spares, pump, patch kit, tow strap), layers, rain gear, bear spray, binoculars, sturdy hiking boots, food for the drive (no services on the McCarthy Road)."
  localCulture: "McCarthy and Kennicott are genuine communities of year-round residents who chose this extreme remoteness. Respect that. The Kennicott copper mine history is fascinating — $200 million in copper extracted between 1903 and 1938, then the company simply walked away and left everything in place. The buildings are historic artifacts, not a theme park."
"""
    },
}

for slug, data in DESTINATIONS.items():
    filepath = f"{BASE}/{slug}.md"
    if not os.path.exists(filepath):
        print(f"SKIP {slug} — not found")
        continue

    content = open(filepath, 'r', encoding='utf-8').read()

    # Add frontmatter fields before closing ---
    tier3_fm = f"affiliatePicks:\n{data['affiliatePicks']}faqItems:\n{data['faqItems']}scottTips:\n{data['scottTips']}"

    old_fm_end = "contentStatus: published\ndraft: false\nfmContentType: destination\n---"
    new_fm_end = f"contentStatus: published\ndraft: false\nfmContentType: destination\n{tier3_fm}---"

    if old_fm_end not in content:
        print(f"WARN {slug} — frontmatter pattern not found")
        continue

    content = content.replace(old_fm_end, new_fm_end, 1)

    # Add AEO lede and immersive break — insert before the first existing paragraph
    # Find the first paragraph after the --- closing
    fm_end_pos = content.find('---\n\n', content.find('---\n\n') + 5)  # second ---
    if fm_end_pos == -1:
        print(f"WARN {slug} — body start not found")
    else:
        body_start = fm_end_pos + 5
        first_para_end = content.find('\n\n', body_start)
        if first_para_end != -1:
            first_para = content[body_start:first_para_end]
            video_block = f"""\n\n<div class="immersive-break-inline">
  <video autoplay muted loop playsinline preload="metadata">
    <source src="/videos/destinations/{slug}-hero.mp4" type="video/mp4" />
  </video>
  <div class="ib-gradient" style="background: {data['gradient']};"></div>
  <div class="ib-content">
    <div class="ib-title">{data['video_title']}</div>
    <p class="ib-text">{data['video_text']}</p>
  </div>
</div>"""
            aeo_lede = data['aeo']
            new_block = f"{aeo_lede}{video_block}\n\n{first_para}"
            content = content[:body_start] + new_block + content[first_para_end:]

    # Remove old scott-tips div
    content = re.sub(r'<div class="scott-tips">.*?</div>', '', content, flags=re.DOTALL)

    open(filepath, 'w', encoding='utf-8').write(content)
    print(f"Done {slug}")

print("All Alaska destinations updated")
