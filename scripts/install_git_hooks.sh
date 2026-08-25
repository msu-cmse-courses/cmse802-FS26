#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

git config core.hooksPath .githooks
chmod +x .githooks/pre-push

echo "Installed local git hooks using core.hooksPath=.githooks"
echo "Pre-push schedule check is now active."
echo "Override make target if needed: SCHEDULE_MAKE_TARGET=schedule-spring git push"
