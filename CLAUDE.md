# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Discover Alaska -- a travel guide website built with Astro 5, Tailwind CSS 4, and deployed to Cloudflare Pages. Content is markdown-based using Astro's content collections with Zod schemas.

## Commands

```bash
npm run dev       # Start dev server at localhost:4321
npm run build     # Production build to ./dist/
npm run preview   # Preview production build locally
```

No test runner is configured. No linter is configured.

## Branding

- Colors: Ocean Blue #0077B6 (primary), Sunset Coral #FF6B35 (accent)
- Deep Night #1A2332 (headings/dark backgrounds)
- Sand #F5F0E8 (light background), Sky #EFF8FF (alt background)
- Warm Gold #D4A574
- Fonts: Outfit (sans), DM Serif Display (serif)

## Regions

- southcentral
- interior
- southeast
- southwest
- arctic

## Architecture

### Content Collections (`src/content/`)

Two collections defined in `src/content/config.ts`:
- **destinations** -- Travel destination pages with typed schema (region enum: southcentral/interior/southeast/southwest/arctic, budgetPerDay in USD, highlights array, contentStatus workflow, gradientColors for per-destination theming)
- **blog** -- Articles with categories (destination, food, festival, practical, budget, culture)

Both collections use a `draft: true` default. Content status tracks: draft -> review -> published -> needs-update.

### Routing (`src/pages/`)

- `index.astro` -- Home page
- `destinations/[...slug].astro` -- Dynamic catch-all route
- `blog/[...slug].astro` -- Blog post pages
- `404.astro` -- Custom error page

### Layouts

- `BaseLayout.astro` -- Root layout with SEO meta, imports FloatingNav + Footer + global styles
- `DestinationLayout.astro` -- Wraps BaseLayout, adds hero with per-destination gradient

### Deployment

- Domain: discoveralaska.info
- D1 database: trip-planner-cache-ak (ID: b9ea8224-723a-41fe-ad28-dce76ffc99cd)
- Cloudflare Pages via `@astrojs/cloudflare` adapter

## Destinations (21)

Anchorage, Fairbanks, Juneau, Denali National Park, Glacier Bay, Kenai Fjords, Sitka, Ketchikan, Skagway, Seward, Homer, Kodiak, Valdez, Wrangell-St. Elias, Katmai National Park, Nome, Utqiagvik, Haines, Talkeetna, Whittier, Petersburg

## Content Voice

- First-person singular -- Scott's perspective as a visitor
- Prices in USD only
- Honest, opinionated, insider perspective
- **Names rule:** Only use "Scott" and "I" in content. Never include names of family members, children, or other companions.
- Cross-link every page to at least 2 other content pillars
- Question-based H2/H3 headings for GEO
- Answer-first paragraphs: lead with the answer, then supporting detail

### Required Pro Tips (Every Destination Page)

1. **Getting There** -- Directions, airport options, driving from major cities, ferry options
2. **Best Time to Visit** -- Summer midnight sun, aurora season, shoulder months
3. **Getting Around** -- Car rental, Alaska Railroad, bush planes, ferries
4. **Budget Tips** -- Camping, free hiking, shoulder season deals
5. **Safety** -- Bear safety, hypothermia, wildlife distances, tide awareness
6. **Packing** -- Layers, rain gear, bear spray, binoculars, insect repellent

Use `<div class="scott-tips">` block format.

## Affiliate Links

- Booking.com: aid=2778866, label=discoveralaska
- GetYourGuide: partner_id=IVN6IQ3
- Viator: pid=P00290009
- SafetyWing: referenceID=24858745
