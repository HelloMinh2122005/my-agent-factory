# Agent Evaluation Rubrics & Compliance Testing Guide

This reference provides the formal evaluation criteria used by `agent-auditor-validator` and LLM judges to grade newly generated agents, skills, and plugins.

---

## 1. The 4-Part LLM-as-a-Judge Pattern

When evaluating an agent's definition, never rely on subjective impression. Execute a deterministic 4-part assessment:

1. **Criterion Definition**: Define the exact metric using domain terminology:
   - `YAML_COMPLIANCE`: Conformance to Antigravity frontmatter specification.
   - `LEAST_PRIVILEGE`: Strict alignment of tool permissions to role necessity.
   - `LINK_INTEGRITY`: 100% resolution of relative paths without dangling references.
   - `PROGRESSIVE_DISCLOSURE`: Context efficiency through separation of `SKILL.md` and `references/`.
   - `ZERO_GUESS_CLAUSE`: Inclusion of verification protocols and anti-hallucination constraints.
2. **Explicit Reasoning Structure (Chain-of-Thought)**:
   - Perform step-by-step verification of each criterion before producing a score.
3. **Deterministic Scoring Rule**:
   - Every criterion is graded **PASS** (1) or **FAIL** (0).
   - Any single **FAIL** results in an overall **REMEDIATION_REQUIRED** verdict.
4. **Edge Case Clause**:
   - Flag any undefined variables, missing subagent targets in `config.json`, or local machine-specific absolute paths (e.g. `file:///path/to/...`).

---

## 2. Comprehensive Compliance Checklist

| Category | Inspection Item | Pass Criteria | Severity if Failed |
| :--- | :--- | :--- | :--- |
| **Frontmatter** | `name` attribute | Lowercase kebab-case matching filename. | Blocker |
| **Frontmatter** | `description` attribute | Explains role and clear trigger conditions. | Major |
| **Frontmatter** | `model` attribute | Explicitly set to `pro` or `flash`. | Major |
| **Frontmatter** | `subagent` attribute | Must be boolean `true`. | Blocker |
| **Frontmatter** | `tools` list | Explicit array of valid Antigravity tools only. | Blocker |
| **Tool Security** | Least-Privilege Check | Auditor/Reviewer roles have NO write tools. | Blocker |
| **File Integrity** | Relative Paths | Every Markdown link points to a real file. | Blocker |
| **File Integrity** | No Absolute Paths | Zero `file:///path/to/...` or machine-local paths. | Major |
| **Token Economy**| Progressive Disclosure | `SKILL.md` < 150 lines; deep docs in `references/`. | Minor |
| **JSON Schemas** | Syntax & Structure | `plugin.json` and `config.json` parse without error. | Blocker |

---

## 3. Trajectory Evaluation for Multi-Agent SOPs

When testing a squad's execution trajectory:
1. **Contract Handoff**: Does Agent $A$'s output contract fulfill Agent $B$'s required input contract?
2. **Boundary Enforcement**: Did any worker attempt to execute tasks assigned to another specialist?
3. **Independent Gatekeeping**: Did the Tech Lead or Validator enforce a real gate, or did they rubber-stamp unverified deliverables?
4. **Remediation Loop**: When a defect was reported, did the author remediate specifically to green, or did it introduce regressions?
