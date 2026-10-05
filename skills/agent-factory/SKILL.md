---
name: agent-factory
description: Meta-Agent engineering and squad generation skill for Google Antigravity. Use when architecting new AI subagents, designing multi-agent squads, writing Antigravity plugins, authoring SKILL.md runbooks, configuring tool permissions, and validating agent manifests.
---

# Agent Factory (Meta-Agent Engineering Skill)

This skill provides comprehensive architecture guidelines, prior art benchmarks, and operational procedures for designing, authoring, and validating production-grade AI agents, skills, and plugins in Google Antigravity.

---

## 1. Skill Specifications & Manifests

- **Configuration & Triggers**: [config.json](./config.json)  
  Defines triggers, agent roles (`meta-agent-architect`, `prompt-persona-engineer`, `skill-workflow-designer`, `agent-auditor-validator`), model selection rules, and quality policies.
- **Operational Directives**: [system_prompt.md](./system_prompt.md)  
  Specifies the foundational principles (Human Alignment First, Prior Art Research First, Option A Approval Gate).
- **Execution Protocol**: [workflow.md](./workflow.md)  
  The 5-phase SOP: Alignment $\rightarrow$ Research $\rightarrow$ Co-Pilot Gate $\rightarrow$ Parallel Generation $\rightarrow$ Independent Audit.

---

## 2. Progressive Knowledge References

Deep architectural reference manuals are located in `references/`:

- **[Open-Source Prior Art & Foundations](./references/open-source-prior-art.md)**: Synthesis of battle-tested multi-agent frameworks: MetaGPT's Standard Operating Procedures ("Code = SOP(Team)"), Anthropic's *Building Effective Agents* (Router, Orchestrator-Subagent, Evaluator-Optimizer), ROMA's recursive decomposition, and LangGraph state machines.
- **[Subscription-Aware Model Tiering Guide](./references/model-tiering-guide.md)**: Strategy for selecting between `pro` and `flash` models, subscription-aware defaults (Gemini 3.8 Flash for Antigravity Pro users), and rate-limit/latency optimization.
- **[Antigravity Specification Guide](./references/antigravity-spec-guide.md)**: Complete specification for `.agents/` workspace customization roots, `plugin.json` manifests, YAML frontmatter, progressive disclosure in `skills/`, contextual `rules/`, lifecycle `hooks.json`, and `mcp_config.json`.
- **[Agent Evaluation & Rubrics](./references/evaluation-rubric.md)**: LLM-as-a-judge rubrics, trajectory testing, tool least-privilege matrix, and static schema validation standards.

---

## 3. Quick Execution Summary

1. **Step 1 — Understand User**: Clarify requirements, operational context, and role boundaries before writing any code.
2. **Step 2 — Research Prior Art**: Search open-source projects and industry standards to reuse proven patterns rather than reinventing the wheel.
3. **Step 3 — Option A Approval Gate**: Propose the architectural blueprint (Roles, Models, Tools, File Tree) and obtain user sign-off.
4. **Step 4 — Parallel Authoring**: Generate agent `.md` files, `SKILL.md` runbooks, reference docs, and `plugin.json` manifests.
5. **Step 5 — Independent QA Audit**: Verify schemas, links, and permissions via `agent-auditor-validator` before delivery.
