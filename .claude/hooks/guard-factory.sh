#!/usr/bin/env bash
# PreToolUse guard (Write|Edit) for the Claude factory squad, registered in .claude/settings.json
# and by the /factory-lead skill (which passes "factory-lead" as $1, because an inline lead
# session has no agent_type). Only the four squad roles are restricted; everything else passes.

input=$(cat)
file=$(jq -r '.tool_input.file_path // .tool_input.notebook_path // empty' <<<"$input")
agent=$(jq -r '.agent_type // empty' <<<"$input"); agent=${agent:-$1}
[[ -z "$file" ]] && exit 0
abs=$(realpath -m -- "$file")

block() {
  echo "Blocked by guard-factory: $agent may not write '$abs'. $1" >&2
  exit 2
}

case "$agent" in
  *github-repo-scout)
    [[ "$abs" == */.research/* || "$abs" == */.peer-review/* ]] || block "The scout writes only .research/ and .peer-review/ files."
    ;;
  *peer-reviewer)
    [[ "$abs" =~ /\.peer-review/[^/]+/review-by-claude\.md$ ]] || block "The reviewer writes only .peer-review/<id>/review-by-claude.md."
    ;;
  *factory-lead)
    [[ "$abs" == */.factory/* || "$abs" == */.peer-review/* || "$abs" == */.claude/factory-learnings.md ]] || block "The lead writes only .factory/, .peer-review/ requests and .claude/factory-learnings.md; agents and skills are built by claude-squad-engineer."
    [[ "$abs" =~ /review-by-[^/]+\.md$ ]] && block "Review files belong to the reviewer."
    ;;
  *claude-squad-engineer)
    [[ "$abs" == */.agents/* ]] && block "The .agents/ tree belongs to the Antigravity factory."
    [[ "$abs" == */.research/* || "$abs" == */.peer-review/* ]] && block "Research and review files belong to the scout and reviewers."
    if [[ "$abs" == */.factory/* ]]; then
      [[ "$abs" =~ /\.factory/[^/]+/build-report-claude\.md$ ]] || block "In .factory/ the engineer writes only build-report-claude.md."
    fi
    ;;
esac
exit 0
