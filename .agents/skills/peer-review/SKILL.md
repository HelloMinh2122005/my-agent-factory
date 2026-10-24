---
name: peer-review
description: Cross-platform peer review over agent-chat between Claude Code and Antigravity. Use right after finishing a research report (e.g. a GitHub repo ranking) or completing an agent, skill or squad build — to request a review from the other platform — and when a PEER_REVIEW_REQUEST or PEER_REVIEW_RESULT arrives.
---

# Peer Review (Claude Code ⇄ Antigravity)

A second model family reviews the work before it reaches the user. The review is **advisory**: the requester decides what to change and the user has the final say.

- Request template: [templates/request.md](./templates/request.md)
- Review template: [templates/review.md](./templates/review.md)

## 1. When to request (mandatory)

| Finished work | Request from (agent-chat address) |
| :--- | :--- |
| Research report by `github-repo-scout` | the other platform's `github-repo-scout` (`antigravity/github-repo-scout` ⇄ `claude-code/github-repo-scout`) |
| Agent / skill / squad built on Antigravity (factory Phase 5 passed) | lead to lead: `antigravity/meta-agent-architect` → `claude-code/factory-lead` |
| Agent / skill / squad built on Claude Code | lead to lead: `claude-code/factory-lead` → `antigravity/meta-agent-architect` |

The receiving lead does not review alone: Claude's `factory-lead` delegates to `peer-reviewer`; Antigravity's `meta-agent-architect` delegates the static checks to `agent-auditor-validator`.

Request only after your own checks pass (validators, auditor, tests). Do not request review of drafts.

## 2. How to request

1. Create `.peer-review/<YYYYMMDD>-<slug>/request.md` from the template: kind (`research` | `agent` | `skill` | `squad`), artifact paths, context, what to focus on, open questions.
2. Send one agent-chat message (≤ 2000 chars, files carry the content):
   ```
   [PEER_REVIEW_REQUEST] <YYYYMMDD-slug> · round <n>/2
   kind: research | agent | skill | squad
   dir: <absolute workspace path>/.peer-review/<YYYYMMDD-slug>/
   read: request.md, <artifact paths>
   focus: <1–3 lines>
   ```
   `chat(from: <your agent name>, to: <address from §1>, message: …)`. If you are a subagent without agent-chat access, return the message to your orchestrator, which sends it with `from:` set to your name.
3. Tell the user: "Peer review requested — run `/check-message <recipient name>` in <other IDE>."

## 3. How to review (when a PEER_REVIEW_REQUEST arrives)

- **Read-only on their work.** Never edit the requester's files; write only `review-by-<claude|antigravity>.md` in the request folder.
- **Research**: re-run 1–2 of the key searches independently, look for strong repositories they missed, re-check a sample of metrics (stars, last push, license) and re-score the top 3 with the shared rubric (`github-repo-scout` skill, `references/ranking-rubric.md`).
- **Agent / skill / squad**: check frontmatter validity, tool least privilege, model/effort choices, broken links, protocol consistency between platforms, loop caps and escalation paths (use `review-multi-agent-orchestration` when available; on Claude the review is done by `peer-reviewer`, on Antigravity the static checks by `agent-auditor-validator`).
- Findings: `F-nn · BLOCKER | MAJOR | MINOR · path:line — what / why / suggestion`. Verdict: **APPROVE** (no BLOCKER/MAJOR) · **CHANGES_SUGGESTED** · **REJECT** (fundamentally wrong approach).
- Reply:
  ```
  [PEER_REVIEW_RESULT] <YYYYMMDD-slug> · round <n>/2
  verdict: APPROVE | CHANGES_SUGGESTED | REJECT
  read: review-by-<platform>.md
  summary: <top findings, ≤5 lines>
  ```
  `chat(from: <your name>, to: <requester address>, message: …, reply_to: <request id>)`.

## 4. After the result (requester)

Address each BLOCKER/MAJOR finding or note why not in `request.md` ("Round n response"). At most **2 rounds**; then report to the user with the reviewer's verdict and any unresolved findings.

## Rules
No acknowledgement-only messages · one message per step · no secrets in files or messages · the reviewer never fixes the work itself.
