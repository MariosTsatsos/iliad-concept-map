#!/usr/bin/env bash
# Puts the built page (site/dist) on the 'gh-pages' branch of the given remote.
# Usage: bash scripts/publish.sh <remote-url>      (run 'python scripts/build.py' first)
# The branch holds one commit with index.html and graph.json; each run replaces it.
set -euo pipefail
remote="$1"
root="$(cd "$(dirname "$0")/.." && pwd)"
test -s "$root/site/dist/index.html" || { echo "site/dist/index.html is missing: run scripts/build.py first"; exit 1; }
work="$(mktemp -d)"
cp "$root/site/dist/index.html" "$root/site/dist/graph.json" "$work/"
touch "$work/.nojekyll"          # tells GitHub Pages to serve the files as they are
cd "$work"
git init -q -b gh-pages
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add -A
git commit -q -m "Publish map from ${GITHUB_SHA:-a local build}"
git push -q -f "$remote" gh-pages
echo "published $(wc -c < index.html) bytes of index.html to gh-pages"
