// Popular Alaska POI coordinates for itinerary geocoding.
// Keyed by lowercase normalized name. Covers top attractions at launch destinations.
// Used by generate-itinerary.ts to resolve activity coordinates without Geocoding API calls.

export const LANDMARK_COORDS: Record<string, { lat: number; lng: number }> = {
  // ── Anchorage ──
  'tony knowles coastal trail': { lat: 61.2022, lng: -149.9384 },
  'flattop mountain': { lat: 61.0988, lng: -149.6826 },
  'alaska wildlife conservation center': { lat: 60.8233, lng: -148.9867 },
  'anchorage museum': { lat: 61.2167, lng: -149.8867 },
  'alaska native heritage center': { lat: 61.2328, lng: -149.7706 },
  'ship creek': { lat: 61.2267, lng: -149.8833 },

  // ── Fairbanks ──
  'chena hot springs': { lat: 65.0528, lng: -146.0558 },
  'museum of the north': { lat: 64.8583, lng: -147.8422 },
  'gold dredge no. 8': { lat: 64.9106, lng: -147.8000 },
  'pioneer park': { lat: 64.8386, lng: -147.7758 },
  'trans-alaska pipeline viewpoint': { lat: 64.8500, lng: -147.7500 },

  // ── Juneau ──
  'mendenhall glacier': { lat: 58.4189, lng: -134.5517 },
  'mount roberts tramway': { lat: 58.3000, lng: -134.4167 },
  'tracy arm fjord': { lat: 57.8833, lng: -133.6167 },
  'alaska state museum': { lat: 58.3014, lng: -134.4164 },

  // ── Denali National Park ──
  'denali visitor center': { lat: 63.7300, lng: -148.9100 },
  'eielson visitor center': { lat: 63.4300, lng: -150.3000 },
  'wonder lake': { lat: 63.4533, lng: -150.8667 },
  'savage river': { lat: 63.7147, lng: -149.2400 },

  // ── Glacier Bay ──
  'bartlett cove': { lat: 58.4550, lng: -135.8883 },
  'margerie glacier': { lat: 58.9667, lng: -136.9167 },

  // ── Kenai Fjords ──
  'exit glacier': { lat: 60.1833, lng: -149.6333 },
  'harding icefield trail': { lat: 60.1833, lng: -149.6500 },

  // ── Sitka ──
  'sitka national historical park': { lat: 57.0467, lng: -135.3133 },
  'castle hill': { lat: 57.0522, lng: -135.3408 },
  'alaska raptor center': { lat: 57.0589, lng: -135.3467 },

  // ── Ketchikan ──
  'creek street': { lat: 55.3414, lng: -131.6389 },
  'totem heritage center': { lat: 55.3367, lng: -131.6250 },
  'misty fjords': { lat: 55.6167, lng: -130.7167 },

  // ── Skagway ──
  'white pass railroad depot': { lat: 59.4583, lng: -135.3139 },
  'chilkoot trail': { lat: 59.5167, lng: -135.2833 },

  // ── Homer ──
  'homer spit': { lat: 59.6017, lng: -151.4100 },
  'kachemak bay': { lat: 59.6000, lng: -151.3000 },

  // ── Kodiak ──
  'baranov museum': { lat: 57.7894, lng: -152.4058 },
  'fort abercrombie': { lat: 57.8250, lng: -152.3250 },

  // ── Valdez ──
  'columbia glacier': { lat: 61.1500, lng: -147.0833 },
  'keystone canyon': { lat: 61.1167, lng: -145.9833 },
  'worthington glacier': { lat: 61.1694, lng: -145.7500 },
};
