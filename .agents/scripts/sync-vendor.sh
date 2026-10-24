#!/usr/bin/env bash
# Mirror the community repos listed in vendor-manifest.json into ~/.agent-factory/vendor
# (shallow clones, read-only use). Never runs code from the cloned repos.
set -euo pipefail

here=$(cd "$(dirname "$0")" && pwd)
vendor=${AGENT_FACTORY_VENDOR:-$HOME/.agent-factory/vendor}
mkdir -p "$vendor"

python3 -I -c 'import json,sys; [print(r["repo"]) for r in json.load(open(sys.argv[1]))["repos"]]' "$here/vendor-manifest.json" |
while read -r repo; do
  dir="$vendor/${repo/\//__}"
  if [[ -d "$dir/.git" ]]; then
    git -C "$dir" -c core.hooksPath=/dev/null pull -q --depth 1 --ff-only 2>/dev/null || echo "warn: could not update $repo" >&2
  else
    git -c core.hooksPath=/dev/null clone -q --depth 1 "https://github.com/$repo.git" "$dir" || { echo "warn: could not clone $repo" >&2; continue; }
  fi
  printf '%-45s %s\n' "$repo" "$(git -C "$dir" log -1 --format='%h %cs')"
done
