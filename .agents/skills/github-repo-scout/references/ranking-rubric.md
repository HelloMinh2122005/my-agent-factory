# Repository Ranking Rubric (0–100)

Score every candidate on all six criteria. Record the evidence for each score. Rank by total; ties → higher **Fit**, then higher **Maintenance**.

## Hard filters (excluded, listed under "Rejected")
- Archived, or a fork with no commits of its own.
- Unrelated to the need after reading the README.
- Known malicious behaviour (obfuscated code, credential exfiltration, `curl … | sh` installers pulling unpinned remote code).

## Criteria

| # | Criterion | Max | Scoring anchors |
| :-- | :--- | :-- | :--- |
| 1 | **Fit** to the need | 30 | 30 solves the need directly · 20 solves most, small gaps · 10 partial / needs real adaptation · 0 tangential |
| 2 | **Platform fit** | 15 | 15 native format for the target platform (Claude Code skill/agent/plugin, or Antigravity `.agents/` skill/agent) · 12 portable Agent Skills (`SKILL.md`) · 5 needs porting · 0 different ecosystem |
| 3 | **Adoption** (stars) | 15 | 15 ≥10k · 12 ≥1k · 8 ≥200 · 4 ≥50 · 1 <50 |
| 4 | **Maintenance** (last push) | 15 | 15 ≤30 days · 12 ≤90 · 8 ≤180 · 4 ≤365 · 0 older |
| 5 | **License** | 10 | 10 MIT / Apache-2.0 / BSD · 7 other OSI · 3 custom with reuse allowed · 0 none (code cannot be reused; ideas only) |
| 6 | **Safety & cost** | 15 | 15 instruction-only (Markdown) · 10 scripts read and benign · 5 session-wide context injection (e.g. SessionStart hooks) or heavy always-on token cost · 0 network/credential access or unpinned remote installs |

## Reuse recommendation (per candidate)
- **install** — total ≥ 75, Fit ≥ 20, Safety ≥ 10, License ≥ 7
- **adapt** — Fit ≥ 20 but platform/format or small gaps need changes (keep LICENSE + source)
- **reference** — useful pattern or ideas, not reusable as-is (incl. License = 0)
- **reject** — Fit < 10 or Safety = 0

## Reporting
Per candidate: `owner/repo @ sha`, stars, last push date, license, what it contains, the six scores with one line of evidence each, total, recommendation.
