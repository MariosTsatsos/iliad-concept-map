#!/usr/bin/env bash
# Puts the built page (site/dist) and the course material (materials/) on the 'gh-pages' branch of the given remote.
# Usage: bash scripts/publish.sh <remote-url>      (run 'python scripts/build.py' first)
# The branch holds one commit; each run replaces it. The commit is made from this repository's own objects,
# so the material, which the remote already has on 'main', is not uploaded again.
set -euo pipefail
remote="$1"
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
test -s site/dist/index.html || { echo "site/dist/index.html is missing: run scripts/build.py first"; exit 1; }
GIT_INDEX_FILE="$(mktemp -u)"
export GIT_INDEX_FILE
trap 'rm -f "$GIT_INDEX_FILE"' EXIT
git read-tree --empty
(cd site/dist && find . -type f ! -name fragment.html | sed 's|^\./||') | while IFS= read -r f; do
  git update-index --add --cacheinfo "100644,$(git hash-object -w "site/dist/$f"),$f"
done
git update-index --add --cacheinfo "100644,$(git hash-object -w --stdin </dev/null),.nojekyll"   # serve the files as they are
if git cat-file -e HEAD:materials 2>/dev/null; then
  git read-tree --prefix=materials/ HEAD:materials
fi
tree="$(git write-tree)"
export GIT_AUTHOR_NAME="github-actions[bot]" GIT_AUTHOR_EMAIL="41898282+github-actions[bot]@users.noreply.github.com"
export GIT_COMMITTER_NAME="$GIT_AUTHOR_NAME" GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"
commit="$(git commit-tree "$tree" -m "Publish map from ${GITHUB_SHA:-a local build}")"
git push -q -f "$remote" "$commit:refs/heads/gh-pages"
echo "published $(git ls-tree -r "$tree" | wc -l | tr -d ' ') files to gh-pages"
