import type { PackingItem, PackingConfig, GearRecommendation } from './packing-base';

export const ALASKA_ESSENTIALS: PackingItem[] = [
  { id: 'ak-bearspray', name: 'Bear Spray', category: 'destination', description: 'Not optional for any backcountry hiking. More effective than firearms at stopping a charge. Know how to use it before you go — watch a video, practice the draw. Carry clipped to your hip, not buried in your pack.', essential: true, amazonSearchFallback: 'bear+spray+counter+assault', affiliatePrice: '$40–55' },
  { id: 'ak-layers', name: 'Merino Wool Base Layers', category: 'destination', description: 'Alaska temperatures swing 30°F between morning and afternoon. Merino wool regulates temperature, resists odor, and stays warm when wet — unlike synthetic base layers.', essential: true, climate: ['cold', 'alpine'], amazonSearchFallback: 'merino+wool+base+layer+thermal', affiliatePrice: '$60–100' },
  { id: 'ak-waterproof', name: 'Waterproof Outer Shell (jacket + pants)', category: 'destination', description: 'Southeast Alaska (Juneau, Ketchikan, Sitka) gets 60–90 inches of rain annually. The Kenai Peninsula is wet. Rain gear isn\'t optional — it\'s daily.', essential: true, climate: ['cold'], amazonSearchFallback: 'waterproof+rain+jacket+pants+outdoor', affiliatePrice: '$80–150' },
  { id: 'ak-binoculars', name: 'Binoculars (8x42 minimum)', category: 'destination', description: 'Bears, moose, Dall sheep, bald eagles, orcas — wildlife is everywhere but rarely close. Quality binoculars transform wildlife viewing from "I think that\'s a bear" to "that\'s a sow with cubs."', essential: true, amazonSearchFallback: 'binoculars+8x42+wildlife+waterproof', affiliatePrice: '$80–200' },
  { id: 'ak-repellent', name: 'DEET Insect Repellent (40%+ strength)', category: 'destination', description: 'Alaskan mosquitoes are legendary — warm summer days bring clouds of them, especially in interior and coastal wetlands. 40% DEET minimum. 100% DEET is not overkill in the interior.', essential: true, amazonSearchFallback: 'deet+40+percent+insect+repellent+strong', affiliatePrice: '$10–18' },
];

export const ALASKA_GEAR_RECOMMENDATIONS: GearRecommendation[] = [
  { id: 'gr-ak-bearspray', name: 'Bear Spray', reason: 'More effective than firearms in a bear encounter. Required equipment for any backcountry Alaska hiking. Clip to your hip and practice the draw — you won\'t have time to dig it out.', amazonSearchFallback: 'bear+spray+counter+assault+hikers', affiliatePrice: '~$45' },
  { id: 'gr-ak-binoculars', name: 'Quality Binoculars (8x42)', reason: 'Alaska\'s wildlife is everywhere but never close enough without optics. Good binoculars turn a distant brown shape into a grizzly sow with cubs. Worth every dollar for any Alaska wildlife trip.', amazonSearchFallback: 'binoculars+8x42+wildlife+waterproof+fogproof', affiliatePrice: '~$150' },
  { id: 'gr-ak-jacket', name: 'Packable Down Jacket', reason: 'Alaska evenings drop fast, even in summer. A packable down jacket that compresses to nothing is the single most versatile layer for Alaska — from glacier viewing to dinner in Anchorage.', amazonSearchFallback: 'packable+down+jacket+lightweight+outdoor', affiliatePrice: '~$85' },
  { id: 'gr-ak-boots', name: 'Waterproof Hiking Boots', reason: 'Southeast Alaska gets 60–90 inches of rain annually. The trails are wet, the beaches are rocky, the boats splash. Waterproof boots are not a luxury — they\'re the difference between a fun day and a miserable one.', amazonSearchFallback: 'waterproof+hiking+boots+outdoor+ankle+support', affiliatePrice: '~$130' },
  { id: 'gr-ak-repellent', name: 'High-DEET Insect Repellent (40%+)', reason: 'Alaskan mosquitoes are legendary. Interior Alaska in June is cloud-of-insects territory. 40% DEET minimum — natural alternatives don\'t survive Alaska\'s humidity and density.', amazonSearchFallback: 'deet+40+percent+insect+repellent+strong', affiliatePrice: '~$12' },
];

export const ALASKA_CONFIG: PackingConfig = {
  sitePrefix: 'dak',
  destination: 'Alaska',
  climate: ['cold', 'alpine'],
  currency: 'USD',
  plugType: 'Type A/B',
  plugVoltage: '120V',
  affiliateTag: 'discoverphili-20',
  destinationEssentials: ALASKA_ESSENTIALS,
  gearRecommendations: ALASKA_GEAR_RECOMMENDATIONS,
};

export const SITE_CONFIG = ALASKA_CONFIG;

export const ALASKA_PACKING_FAQS = [
  { question: 'What should I pack for Alaska?', answer: 'Bear spray is non-negotiable for any backcountry hiking. Beyond that: merino wool base layers (30°F temperature swings are normal), a waterproof outer shell (Southeast Alaska gets 60–90 inches of rain annually), quality binoculars for wildlife, and 40%+ DEET repellent. Alaska is a gear-intensive destination — pack seriously or rent in Anchorage.' },
  { question: 'Do I really need bear spray in Alaska?', answer: 'Yes, for any backcountry or trail hiking. Bear spray is more effective than firearms in stopping a charge according to research. Carry it clipped to your hip — accessible in 2 seconds — not buried in your pack where you can\'t reach it in time. Practice the draw before your trip. Available to rent at outfitters in Anchorage, Juneau, and Fairbanks.' },
  { question: 'What power adapter do I need for Alaska?', answer: 'No adapter needed. Alaska uses US standard Type A/B outlets at 120V — the same as the lower 48 states.' },
  { question: 'Can I buy gear in Alaska?', answer: 'Yes — REI has stores in Anchorage. Alaska Mountaineering and Hiking in Anchorage is excellent for backcountry gear. Bear spray can be rented at many outfitters. However, specialty sizes, prescription items, and your preferred brands are better brought from home — selection in smaller towns is limited.' },
  { question: 'How many outfits should I pack for Alaska?', answer: 'Pack for 5–7 days with layering as the focus. Alaska laundry options are available in towns but limited in remote areas. Prioritize technical gear (waterproof, merino wool, packable layers) over quantity of outfits. A short Alaska trip may not require a laundry stop at all.' },
  { question: 'What should I NOT bring to Alaska?', answer: 'Cotton base layers (stays wet and cold — dangerous in Alaska conditions), light rain gear (Alaska rain is serious — bring proper waterproof shell), flip-flops as primary footwear for anything beyond a deck, and unprepared electronics (cold weather drains batteries fast — carry a power bank).' },
];
