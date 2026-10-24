---
name: github-repo-scout
description: Search GitHub for repositories that already solve a need (skills, agents, plugins, squads, libraries) and rank them with a fixed, evidence-based rubric. Use when a task needs prior art, "is there an existing repo/skill/plugin for X", or a ranked shortlist of GitHub repositories. Platform-neutral — shared by the Antigravity and Claude Code github-repo-scout agents.
---

# GitHub Repo Scout

One job: **find GitHub repositories for a need and rank them.** Do not design, install or build anything — the output is a ranked, evidenced shortlist that others act on.

- Ranking rubric (mandatory): [references/ranking-rubric.md](./references/ranking-rubric.md)
- Report template: [templates/repo-ranking.md](./templates/repo-ranking.md)
- After the report: request a peer review with the `peer-review` skill.

## Procedure

1. **Frame the need** in one sentence plus 3–6 keywords and the target platform(s) (Claude Code, Antigravity, any).
2. **Search wide** — at least 4 queries mixing synonyms and platform words (`claude code skill`, `SKILL.md`, `antigravity`, `agent skills`, `subagent`, `plugin marketplace`):
   ```bash
   gh search repos "<query>" --sort stars --limit 25 \
     --json fullName,description,stargazersCount,forksCount,pushedAt,license,isArchived,isFork,url
   gh search repos --topic claude-skills "<keyword>" --limit 25 --json fullName,stargazersCount,pushedAt,url   # one --topic per call (several = AND); repeat for agent-skills, claude-code, antigravity
   gh search code "<keyword>" --filename SKILL.md --limit 30 --json repository,path
   ```
   Also check curated lists and the local mirror if present (`~/.agent-factory/vendor/`: `skills_index.json`, `CATALOG.md`, awesome-list READMEs). No `gh`? Use web search plus `https://api.github.com/repos/<owner>/<repo>` (unauthenticated: 60 requests/hour).
3. **Filter**: drop archived repos, forks with no own commits, and anything unrelated after reading the README. Keep 8–15 candidates.
4. **Inspect each candidate** (read-only, never run its code):
   ```bash
   gh api repos/<owner>/<repo> --jq '{stars:.stargazers_count,forks:.forks_count,pushed:.pushed_at,license:.license.spdx_id,archived:.archived,topics:.topics}'
   gh api repos/<owner>/<repo>/git/trees/HEAD?recursive=1 --jq '.tree[].path' | grep -E 'SKILL.md|agents/|hooks|plugin.json|marketplace.json|\.sh$|\.py$|package.json' | head -50
   gh api repos/<owner>/<repo>/commits/HEAD --jq .sha
   ```
   Read the README and the files that would actually be reused (SKILL.md, agent files, hooks, scripts) to score **fit** and **safety**.
5. **Score** every candidate with the rubric; show the per-criterion breakdown and the evidence behind it.
6. **Write the report** from the template to `.research/<YYYYMMDD>-<slug>/repos-<platform>.md` (`<platform>` = `claude` or `antigravity`).
7. **Request peer review** of the report from the other platform's `github-repo-scout` (skill `peer-review`).

## Rules

- Evidence over memory: every number (stars, last push, license) comes from a command run today; cite the commit sha you inspected.
- Never clone into the workspace, run install scripts, or execute repo code. Read-only.
- Rank honestly: a famous repo that doesn't fit scores low on fit. If nothing fits, say so and list what was searched.
