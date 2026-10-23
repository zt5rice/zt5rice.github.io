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

Deployment remains on the existing GitHub Pages configuration until `ZHA-197`.
Do not switch Pages to the new build before visual QA and explicit release
approval.
