# Portfolio v2 QA Report

Date: 2026-10-24; publication-copy follow-up: 2026-10-26

Preview URL: `http://127.0.0.1:4321`

Verdict: **PASS**. No release-blocking defects found.

## Build and static checks

- `npm run check`: 0 errors, 0 warnings, 0 hints.
- `npm run build`: passed.
- Static routes generated: 6.
- Homepage and four case-study routes have:
  - one `h1`
  - a unique title
  - a canonical URL
  - image alt attributes
- All local `href`, `src`, `poster`, and `srcset` files resolve.
- The sitemap includes the homepage and all four case-study routes.
- Initial inline JavaScript: approximately 892 bytes gzip per page.
- No phone number, legacy email, placeholder domain, or credential markers found.

## Playwright

Results file: `qa/results.json`

- 6 routes tested at 3 viewports:
  - 1440 x 900
  - 768 x 1024
  - 390 x 844
- Route-viewport checks: 18.
- Failures: 0.
- Console errors: 0.
- Internal links checked: 6 unique URLs; all returned HTTP 200.
- Media assets checked: 16 unique resources; all returned HTTP 200.
- Responsive page overflow: none.
- Hero name renders `Dr. Zhao Tang` on one line at 390 px, 768 px, and 1440 px;
  narrower viewports retain a natural wrapped fallback.
- AVIF sources selected in Chromium with WebP fallbacks available.
- GraphAtlas videos:
  - 3 players
  - native controls
  - `preload="none"`
  - no autoplay
  - poster images present
- Mobile menu opens and closes with Escape.
- Keyboard focus order begins with `Skip to content`, followed by header links.
- All tested controls show a 2 px solid focus outline.
- Reduced motion:
  - browser media query active
  - hero animation disabled
  - reveal opacity remains 1
  - reveal transform remains none

## Visual regression baselines

- [1440 px](screenshots/home-1440.png)
- [768 px](screenshots/home-768.png)
- [390 px](screenshots/home-390.png)

All three rendered pages were inspected. Project cards, case-study imagery,
Experience, About, Research, Contact, and Footer are present with no clipping.

## Lighthouse

Raw results:

- [Mobile JSON](lighthouse/mobile.json)
- [Desktop JSON](lighthouse/desktop.json)

| Category | Mobile | Desktop | Target |
| --- | ---: | ---: | ---: |
| Performance | 97 | 100 | >= 95 |
| Accessibility | 100 | 100 | >= 95 |
| Best Practices | 100 | 100 | >= 95 |
| SEO | 100 | 100 | >= 95 |

Mobile metrics:

- FCP: 2.1 s
- LCP: 2.2 s
- TBT: 0 ms
- CLS: 0
- Speed Index: 2.1 s

Desktop metrics:

- FCP: 0.4 s
- LCP: 0.5 s
- TBT: 0 ms
- CLS: 0
- Speed Index: 0.4 s

## Manual content review

- Positioning is consistently `Software Engineer · Data & AI Systems`.
- The homepage presents `6` under `Peer-reviewed publications` only. Research
  copy explicitly notes that posters and presentations are separate and excluded
  from that count.
- Public resume is the sanitized two-page Data & AI Systems version.
- Clickstream, GraphAtlas, and NL2SQLAgent remain clearly identified as
  portfolio systems rather than production traffic.
- GraphAtlas evidence links resolve to public benchmark documentation.
- Research links point to the approved Google Scholar profile.
- Phone number is not published.

## Known issues and boundaries

- The publication-count clarification awaits review and deployment; production
  continues to show the previous wording until that release completes.
- The independent nanotrack README publication correction remains tracked in
  `ZHA-198` and is not part of this website PR.
- No custom domain is in scope.
- Visual regression is currently baseline-based; pixel-diff automation is a
  future enhancement rather than a release blocker.

## Release checklist

- [x] Type check and production build
- [x] Route navigation and responsive layouts
- [x] Internal link and media asset checks
- [x] Mobile navigation and keyboard focus
- [x] Reduced-motion behavior
- [x] Video loading policy
- [x] SEO, canonical, sitemap, favicon, and social metadata
- [x] Privacy and publication-fact review
- [x] Lighthouse targets
- [ ] Zhao Tang reviews the preview
- [x] Platform ticket `ZHA-196` is complete
- [x] Production release in `ZHA-197` is approved and deployed
- [ ] Publication-count clarification is reviewed and deployed
