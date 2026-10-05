---
name: agent-factory
description: Meta-Agent engineering and squad generation skill for Google Antigravity. Use when architecting new AI subagents, designing multi-agent squads, writing Antigravity plugins, authoring SKILL.md runbooks, configuring tool permissions, and validating agent manifests.
---

# Agent Factory (Meta-Agent Engineering Skill)

This skill provides comprehensive architecture guidelines, prior art benchmarks, and operational procedures for designing, authoring, and validating production-grade AI agents, skills, and plugins in Google Antigravity.

> **Antigravity Progressive Disclosure Note**: The Antigravity engine discovers skills via this file's frontmatter. To conserve context window tokens, do NOT load all reference manuals simultaneously. Agents should read specific reference files strictly according to their current execution phase.

---

## 1. Skill Specifications & Manifests

- **Internal Policy Manifest**: [config.json](./config.json)  
  User-space specification defining factory policies, role permissions, quantitative complexity triage, and circuit breaker settings (consumed dynamically by factory agents; not an Antigravity engine trigger hook).
- **Operational Directives**: [system_prompt.md](./system_prompt.md)  
  Specifies the foundational principles (Complexity Gate, Human Alignment First, Prior Art Research First, Option A Approval Gate via `ask_question`).
- **Execution Protocol**: [workflow.md](./workflow.md)  
  The 6-phase SOP: Alignment & Quantitative Complexity Gate $\rightarrow$ Research $\rightarrow$ Co-Pilot Gate & Blackboard Persistence $\rightarrow$ Parallel Generation $\rightarrow$ Independent Audit $\rightarrow$ Retrospective & Self-Evolution.

---

## 2. Phase-Gated Progressive Knowledge References

Read only the reference file mapped to your current workflow phase:

- **Phases 1 & 2 (Alignment & Research)**:  
  [Open-Source Prior Art & Foundations](./references/open-source-prior-art.md)  
  Synthesis of MetaGPT's Standard Operating Procedures ("Code = SOP(Team)"), Anthropic's *Building Effective Agents* (Complexity Gate, Router, Orchestrator-Subagent), ROMA's recursive decomposition, and LangGraph state machines.
- **Phase 3 (Architectural Blueprint)**:  
  [Subscription-Aware Model Tiering Guide](./references/model-tiering-guide.md)  
  Allocation rules between `pro` and `flash`, subscription-aware defaults (Gemini 3.8 Flash for execution agents on Pro; Free tier rate-limit resilience), and token economy.
- **Phase 4 (Codification & Manifests)**:  
  [Antigravity Specification Guide](./references/antigravity-spec-guide.md)  
  Official specifications for `.agents/` workspace customization roots, `plugin.json` manifests, YAML frontmatter, progressive disclosure in `skills/`, contextual `rules/`, and lifecycle `hooks.json`.
- **Phase 5 (Independent Audit & QA)**:  
  [Agent Evaluation & Rubrics](./references/evaluation-rubric.md)  
  LLM-as-a-judge rubrics (G-Eval style), tool least-privilege matrix, static schema validation, and Remediation Circuit Breaker (max 2 cycles).
- **Phase 6 (Retrospective & Continuous Self-Evolution)**:  
  [Retrospective & Continuous Self-Evolution Guide](./references/retrospective-and-self-evolution.md)  
  Metacognition and learning flywheel based on Reflexion (rule ingestion) and Voyager (skill accumulation), with strict human gates for prompt mutation.

---

## 3. Quick Execution Summary

1. **Step 1 — Understand User & Complexity Gate**: Triage whether the need requires a Single Rule, Single Skill, or Full Multi-Agent Squad before authoring code.
2. **Step 2 — Research Prior Art**: Search open-source projects and industry standards to reuse proven patterns rather than reinventing the wheel.
3. **Step 3 — Option A Approval Gate**: Propose the architectural blueprint (Roles, Models, Tools, File Tree) and obtain user confirmation via `ask_question`.
4. **Step 4 — Parallel Authoring**: Delegate persona generation to `prompt-persona-engineer` and skill runbooks to `skill-workflow-designer`.
5. **Step 5 — Independent QA Audit**: Verify schemas, links, and permissions via `agent-auditor-validator` (strictly read-only; max 2 remediation cycles).
6. **Step 6 — Retrospective & Self-Evolution**: Harvest lessons learned into `.agents/rules/` and scaffold reusable skills to prevent regression and continuously upgrade squad intelligence.
