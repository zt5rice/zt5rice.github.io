# Portfolio QA

The QA tools are intentionally kept outside the website dependency tree.

## Playwright smoke test

```bash
PLAYWRIGHT_MODULE=/Users/zhaotang/projects/person_website/.node-envs/qa/node_modules/playwright/index.mjs \
CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
BASE_URL=http://127.0.0.1:4321 \
node qa/smoke.mjs
```

The test expects a static server serving `dist/` at `BASE_URL`.

It writes:

- `qa/results.json`
- `qa/screenshots/home-1440.png`
- `qa/screenshots/home-768.png`
- `qa/screenshots/home-390.png`

Screenshots use reduced-motion mode so the complete layout is stable and
reviewable; motion behavior is verified separately by the script.

## Lighthouse

```bash
CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  /Users/zhaotang/projects/person_website/.node-envs/qa/node_modules/.bin/lighthouse http://127.0.0.1:4321/ \
  --quiet \
  --chrome-flags="--headless --no-sandbox --disable-gpu" \
  --only-categories=performance,accessibility,best-practices,seo \
  --output=json \
  --output-path=qa/lighthouse/mobile.json

CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  /Users/zhaotang/projects/person_website/.node-envs/qa/node_modules/.bin/lighthouse http://127.0.0.1:4321/ \
  --quiet \
  --preset=desktop \
  --chrome-flags="--headless --no-sandbox --disable-gpu" \
  --only-categories=performance,accessibility,best-practices,seo \
  --output=json \
  --output-path=qa/lighthouse/desktop.json
```

The full report and known issues are in `qa/REPORT.md`.
