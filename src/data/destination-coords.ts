// Shared destination coordinates — single source of truth
// Used by plan page + companion app + generate-itinerary API.

export const DESTINATION_COORDS: Record<string, { lat: number; lng: number; label: string }> = {
  anchorage: { lat: 61.2181, lng: -149.9003, label: 'Anchorage' },
  fairbanks: { lat: 64.8378, lng: -147.7164, label: 'Fairbanks' },
  juneau: { lat: 58.3005, lng: -134.4197, label: 'Juneau' },
  'denali-national-park': { lat: 63.3333, lng: -150.5000, label: 'Denali National Park' },
  'glacier-bay': { lat: 58.5000, lng: -136.0000, label: 'Glacier Bay' },
  'kenai-fjords': { lat: 59.9167, lng: -149.6500, label: 'Kenai Fjords' },
  sitka: { lat: 57.0531, lng: -135.3300, label: 'Sitka' },
  ketchikan: { lat: 55.3422, lng: -131.6461, label: 'Ketchikan' },
  skagway: { lat: 59.4583, lng: -135.3139, label: 'Skagway' },
  seward: { lat: 60.1042, lng: -149.4422, label: 'Seward' },
  homer: { lat: 59.6425, lng: -151.5483, label: 'Homer' },
  kodiak: { lat: 57.7900, lng: -152.4072, label: 'Kodiak' },
  valdez: { lat: 61.1309, lng: -146.3483, label: 'Valdez' },
  'wrangell-st-elias': { lat: 61.7100, lng: -142.9857, label: 'Wrangell-St. Elias' },
  'katmai-national-park': { lat: 58.5000, lng: -155.0000, label: 'Katmai National Park' },
  nome: { lat: 64.5011, lng: -165.4064, label: 'Nome' },
  utqiagvik: { lat: 71.2906, lng: -156.7886, label: 'Utqiagvik' },
  haines: { lat: 59.2361, lng: -135.4456, label: 'Haines' },
  talkeetna: { lat: 62.3209, lng: -150.1064, label: 'Talkeetna' },
  whittier: { lat: 60.7733, lng: -148.6836, label: 'Whittier' },
  petersburg: { lat: 56.8125, lng: -132.9556, label: 'Petersburg' },
};
