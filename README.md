# zt5rice.github.io

Personal portfolio for Dr. Zhao Tang.

The production site is being rebuilt with Astro and TypeScript. The existing
GitHub Pages site remains in place until the deployment ticket switches Pages to
the new build.

## Local development

```bash
npm install
npm run dev
```

The development server runs at `http://localhost:4321`.

## Validation

```bash
npm run check
npm run build
npm run preview
```

## Media generation

```bash
python3 scripts/generate_responsive_images.py
python3 scripts/generate_og_image.py
```

The first command creates 640/1280 WebP and AVIF variants for static portfolio
images. The second creates the 1200x630 Open Graph image.

## Site structure

- `src/pages/`: routes
- `src/layouts/`: shared page shell and metadata
- `src/components/`: reusable interface components
- `src/content/work/`: project case-study content
- `src/data/site.ts`: canonical identity, contact, and navigation data
- `src/styles/global.css`: design tokens and global styles
- `public/`: static files copied into the build
- `docs/`: content, design, backup, and rollback documentation
- `design/`: reproducible high-fidelity mockups

## Deployment

Production is published from the generated `gh-pages` branch. The first switch
to that branch requires manual approval and a Settings change in GitHub Pages.
See [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md) for validation, release, and
rollback steps.

```bash
npm run deploy:pages -- --dry-run
```
