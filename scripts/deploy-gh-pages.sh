#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PAGES_BRANCH="${PAGES_BRANCH:-gh-pages}"
SOURCE_REMOTE="${SOURCE_REMOTE:-origin}"
MODE="dry-run"

usage() {
  cat <<'EOF'
Build and publish the static portfolio to a GitHub Pages branch.

Usage:
  bash scripts/deploy-gh-pages.sh [--dry-run|--publish]

Options:
  --dry-run   Validate the production artifact without pushing (default).
  --publish   Force-push the validated artifact to the Pages branch.

Environment:
  PAGES_BRANCH    Deployment branch name (default: gh-pages).
  SOURCE_REMOTE   Repository remote used to resolve the push URL (default: origin).
  PAGES_GIT_URL   Optional explicit push URL, useful for SSH deployments.
EOF
}

for arg in "$@"; do
  case "$arg" in
    --dry-run)
      MODE="dry-run"
      ;;
    --publish)
      MODE="publish"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      usage >&2
      exit 2
      ;;
  esac
done

cd "$ROOT_DIR"

if [[ ! -f package-lock.json ]]; then
  echo "package-lock.json is required for a reproducible deployment." >&2
  exit 1
fi

echo "Running static checks and production build..."
npm run check
npm run build

if [[ ! -d dist ]]; then
  echo "Build output directory is missing: $ROOT_DIR/dist" >&2
  exit 1
fi

DEPLOY_DIR="$(mktemp -d "${TMPDIR:-/tmp}/zt5rice-gh-pages.XXXXXX")"
cleanup() {
  rm -rf "$DEPLOY_DIR"
}
trap cleanup EXIT

cp -R dist/. "$DEPLOY_DIR/"
find "$DEPLOY_DIR" -name .DS_Store -delete
touch "$DEPLOY_DIR/.nojekyll"

required_files=(
  ".nojekyll"
  "index.html"
  "404.html"
  "robots.txt"
  "sitemap-index.xml"
  "sitemap-0.xml"
  "favicon.svg"
  "site.webmanifest"
  "og/og-portfolio.png"
  "resume/Zhao_Tang_Resume_DataAI_2026-10-21.pdf"
  "work/clickstream/index.html"
  "work/graphatlas/index.html"
  "work/nl2sqlagent/index.html"
  "work/nanotrack/index.html"
)

for path in "${required_files[@]}"; do
  if [[ ! -f "$DEPLOY_DIR/$path" ]]; then
    echo "Missing required deployment artifact: $path" >&2
    exit 1
  fi
done

if grep -RIlE \
  'zt5rice@gmail\.com|example\.com|12 publications|I build softwares' \
  --include='*.html' --include='*.xml' --include='*.txt' \
  "$DEPLOY_DIR" >/dev/null; then
  echo "Deployment artifact contains legacy or placeholder content." >&2
  exit 1
fi

SOURCE_COMMIT="$(git rev-parse HEAD)"
SOURCE_SUBJECT="$(git log -1 --pretty=%s)"

cd "$DEPLOY_DIR"
git init -q
git config user.name "ZHA-197 deployment"
git config user.email "ztangintuit@gmail.com"
git checkout -q -b "$PAGES_BRANCH"
git add -A
git commit -q -m "Deploy portfolio v2 from ${SOURCE_COMMIT:0:12} (ZHA-197)"

DEPLOY_COMMIT="$(git rev-parse HEAD)"
FILES_COUNT="$(git ls-files | wc -l | tr -d ' ')"

cat <<EOF
Deployment artifact validated.
  Source commit:  ${SOURCE_COMMIT:0:12} (${SOURCE_SUBJECT})
  Artifact commit: ${DEPLOY_COMMIT:0:12}
  Branch:          ${PAGES_BRANCH}
  Files:           ${FILES_COUNT}
  Mode:            ${MODE}
EOF

if [[ "$MODE" == "dry-run" ]]; then
  echo "Dry run complete. No remote branch was changed."
  exit 0
fi

if [[ -n "${PAGES_GIT_URL:-}" ]]; then
  PUSH_URL="$PAGES_GIT_URL"
else
  PUSH_URL="$(git -C "$ROOT_DIR" remote get-url "$SOURCE_REMOTE")"
fi

echo "Publishing ${PAGES_BRANCH}..."
git push --force "$PUSH_URL" "HEAD:refs/heads/${PAGES_BRANCH}"

echo "Published ${PAGES_BRANCH} at ${DEPLOY_COMMIT:0:12}."
