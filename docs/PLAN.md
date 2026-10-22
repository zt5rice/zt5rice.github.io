# Portfolio v2 — Approved Plan

## Objective
Rebuild `zt5rice.github.io` and the GitHub profile around a consistent **Data & AI Systems** positioning. The site must quickly communicate identity, selected work, evidence, experience, and contact details to recruiters and engineering reviewers.

## Confirmed direction
- English-first.
- Primary positioning: `Software Engineer · Data & AI Systems`.
- Visual system: charcoal, bone, and signal orange, with restrained phosphor-green status accents.
- Professional portrait in a 4:5 hero treatment.
- Public email: `ztangintuit@gmail.com`.
- LinkedIn: `https://www.linkedin.com/in/tzhao7-sde/`.
- No public phone number.
- Keep the canonical site at `https://zt5rice.github.io/`.
- No blog, CMS, contact form, custom domain, or language switcher in the initial release.

## Site experience
1. Sticky navigation and accessible mobile menu.
2. Hero with portrait, positioning, and primary calls to action.
3. Proof strip with source-backed outcomes.
4. Four selected projects:
   - Clickstream — real-time data platform.
   - GraphAtlas — multi-engine GraphRAG platform.
   - NL2SQLAgent — governed natural-language analytics.
   - nanotrack — research data infrastructure and scientific computing.
5. Experience, About, Research, Contact, and public resume download.
6. Dedicated case-study pages with architecture, implementation, evidence, demo media, limitations, and repository links.
7. Custom 404 page.

## Technical direction
- Astro + TypeScript + native CSS variables.
- Astro Content Collections for project case studies.
- Minimal JavaScript; no React/Vue runtime for the static site.
- Self-hosted Space Grotesk and IBM Plex Mono.
- Responsive WebP/AVIF images and lazy-loaded video.
- Semantic HTML, WCAG AA contrast, keyboard support, and `prefers-reduced-motion`.
- Static deployment through GitHub Actions to GitHub Pages.

## Content and evidence rules
- Every metric must trace to a repository README, benchmark result, or verified local record.
- Portfolio/demo systems must be identified honestly and must not be presented as production traffic.
- The public resume must omit the phone number and use the approved email.
- No confidential employer data, credentials, `.env` files, IP addresses, or private identifiers may be published.

## Delivery workflow
- Each Linear ticket must have at least one dedicated PR linked in the issue.
- Every PR must include a substantive summary covering what changed, why, validation, media evidence, risk/rollback, and tracking.
- Zhao Tang must manually approve every PR before merge.
- No auto-merge, squash-merge, or direct push to `master` without explicit approval.

## Ticket map
- ZHA-185: backup and workspace initialization.
- ZHA-186: asset collection and sanitation.
- ZHA-187: content and fact sheet.
- ZHA-188: public resume.
- ZHA-189: visual system and mockups.
- ZHA-190: Astro scaffold and CI.
- ZHA-191: shell, hero, portrait, and proof strip.
- ZHA-192: project cards and case studies.
- ZHA-193: supporting sections, 404, and resume download.
- ZHA-194: motion, accessibility, SEO, and social assets.
- ZHA-195: end-to-end QA.
- ZHA-196: GitHub profile README and metadata.
- ZHA-197: deployment and rollback verification.

## Release gates
1. Backup is verified.
2. Visual direction is approved.
3. Local preview passes QA and user review.
4. Every PR is manually approved before merge.
5. Production deployment is verified and rollback remains available.
