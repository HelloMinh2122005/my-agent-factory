# Cross-Platform Peer Review Rule

Applies to every agent in this factory. Procedure: skill `peer-review` (`skills/peer-review/SKILL.md`).

1. **Always request a peer review from Claude Code** when you finish:
   - a research report (`github-repo-scout` → `claude-code/github-repo-scout`);
   - an agent, skill or squad build that passed `agent-auditor-validator` (lead to lead: `meta-agent-architect` → `claude-code/factory-lead`).
2. **Review Claude's work when asked**: a `PEER_REVIEW_REQUEST` from Claude Code is answered with a written review and a `PEER_REVIEW_RESULT`. Research requests (from `claude-code/github-repo-scout`) are handled by `github-repo-scout`; agent/skill/squad requests (from `claude-code/factory-lead`) by `meta-agent-architect`, delegating static checks to `agent-auditor-validator`. Never edit the work under review.
3. **Persona activation**: when the user runs `/check-message <name>` and `<name>` is an agent in `agents/`, act as that agent for the whole turn.
4. **Agent-chat access**: subagents that cannot call agent-chat return the ready message to `meta-agent-architect`, which sends it with `from:` set to the subagent's name.
5. **Bounded**: at most 2 review rounds per artifact; the review is advisory and the user decides on unresolved findings.
