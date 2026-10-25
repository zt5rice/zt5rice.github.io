# Production Deployment

## Current state

- Production URL: `https://zt5rice.github.io/`
- Pages source before the first switch: record the branch and folder in
  Settings before changing it; the legacy site is expected to use `master` at
  the repository root
- Legacy baseline commit: `97fdef9fbadd811947e92b586ca7427226537457`
- New static artifact branch: `gh-pages`
- Production changes require Zhao Tang's manual approval.

The new portfolio is built with Astro and published as static files. The
`gh-pages` branch contains only the generated artifact plus `.nojekyll`; source
files remain on `master`.

## Why this deployment model

The repository's Actions policy disallows marketplace actions that are not
owned by `zt5rice`. The Pages workflow therefore uses shell steps only:

- fetch through the scoped `GITHUB_TOKEN`;
- install Node and dependencies;
- run Astro checks and the production build;
- commit the artifact in a temporary Git repository;
- force-push that commit to `gh-pages`.

No third-party action is referenced.

## Pre-release validation

From the website repository:

```bash
npm ci
npm run check
npm run build
npm run deploy:pages -- --dry-run
```

The deployment script verifies the homepage, 404 page, four case-study routes,
resume PDF, sitemap, favicon, Open Graph image, and `.nojekyll`. It also rejects
known legacy content such as the old email address, `example.com`, the
12-publication statement, and the old hero copy.

## First production switch

1. Review and merge the ZHA-197 deployment PR.
2. Wait for the `Deploy Pages` workflow to create or update `gh-pages`.
3. In GitHub repository Settings, open **Pages**.
4. Record the current branch and folder for rollback.
5. Keep **Deploy from a branch** selected.
6. Set the branch to `gh-pages` and the folder to `/ (root)`.
7. Save, then wait for the Pages deployment status to become successful.

Do not switch the Pages source until the `gh-pages` branch exists and the PR has
been manually approved.

## Production verification

Verify these URLs after the switch:

- `https://zt5rice.github.io/`
- `https://zt5rice.github.io/work/clickstream/`
- `https://zt5rice.github.io/work/graphatlas/`
- `https://zt5rice.github.io/work/nl2sqlagent/`
- `https://zt5rice.github.io/work/nanotrack/`
- `https://zt5rice.github.io/resume/Zhao_Tang_Resume_DataAI_2026-10-21.pdf`
- `https://zt5rice.github.io/robots.txt`
- `https://zt5rice.github.io/sitemap-index.xml`
- `https://zt5rice.github.io/favicon.svg`
- `https://zt5rice.github.io/og/og-portfolio.png`

Confirm:

- every route returns HTTP 200;
- HTTPS is active and there is no mixed content;
- the resume downloads as the approved two-page PDF;
- the homepage contains 6 peer-reviewed publications;
- no phone number, legacy email, placeholder domain, or private data appears;
- the GitHub Profile README links to the live site and resume;
- the 404 page renders correctly.

## Rollback

The immediate rollback is to restore the previous GitHub Pages source:

1. Open repository Settings, then **Pages**.
2. Restore the branch and folder recorded before the first switch.
3. Save and wait for deployment.

The current `master` branch still contains the legacy root site, so
`master` / root is the expected rollback target. For a full restore, follow
`docs/ROLLBACK.md` and use the verified backup bundle and baseline commit.

Record the previous `gh-pages` SHA before every future deployment. To roll back
a later artifact, force-push that recorded SHA to `gh-pages` only after explicit
approval.
