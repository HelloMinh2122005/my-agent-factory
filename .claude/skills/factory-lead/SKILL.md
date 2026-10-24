---
name: factory-lead
description: Call factory-lead, the lead of the Claude factory squad. "new <use case>" designs and builds agents/skills/squads (standalone by default, "paired" to let Antigravity build its side); no argument checks agent-chat for review requests and results; "status" lists factory sessions; anything else is a question for the lead.
argument-hint: "[new <use case> [paired] | status | <question>]"
disable-model-invocation: true
model: claude-opus-5-5
effort: xhigh
hooks:
  PreToolUse:
    - matcher: "Write|Edit|NotebookEdit"
      hooks:
        - type: command
          command: "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/guard-factory.sh factory-lead"
---

# /factory-lead — become factory-lead for this turn

1. Read `.claude/agents/factory-lead.md` in the my-agent-factory workspace (ignore its frontmatter) and act as that persona for the whole turn.
2. Delegate only to `github-repo-scout`, `claude-squad-engineer` and `peer-reviewer` (Agent tool).
3. Route the request:

| Request | Do |
| :--- | :--- |
| `new <use case…>` | Run the pipeline from phase 1 (standalone). If the request contains `paired`, use paired mode for the build. Stop at the approval gate and wait for the user. |
| *(empty)* | Follow the `check-message` skill with name `factory-lead`, then handle each NEW message per the persona's inbox table. |
| `status` | List `.factory/*/` sessions in the current workspace with their latest file (request / blueprint / build report / retro) and any pending peer reviews in `.peer-review/`. No writes. |
| anything else | Answer as the lead. |

Request: $ARGUMENTS
