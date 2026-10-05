# Retrospective & Continuous Self-Evolution Guide (The Learning Flywheel)

This reference outlines the architecture, protocols, and safety guardrails that empower Antigravity agent squads to learn from operational experience, conduct retrospectives, and continuously improve their own configurations in `.agents/`.

---

## 1. Theoretical Foundations: The Continuous Learning Flywheel

A static agent squad repeats the same mistakes across sessions. A self-evolving agent squad accumulates institutional knowledge into the codebase using proven research patterns:

```text
       ┌────────────────────────────────────────────────────────┐
       │             TASK EXECUTION & QA VERDICT                │
       └────────────────────────┬───────────────────────────────┘
                                │
                                ▼
       ┌────────────────────────────────────────────────────────┐
       │   PHASE 6: RETROSPECTIVE HARVESTING (Reflexion)        │
       │   Analyze friction, remediation loops, and edge cases │
       └────────┬───────────────────────┬───────────────────────┘
                │                       │
                ▼                       ▼
    [Tier 1: Rule Ingestion]    [Tier 2: Skill Accumulation]
    Append to rules/*.md        Scaffold new skills/*/
                │                       │
                └───────────┬───────────┘
                            │
                            ▼
       ┌────────────────────────────────────────────────────────┐
       │   PERSISTENT SYSTEM EVOLUTION (.agents/ in Git)         │
       │   Next session loads higher-intelligence baseline      │
       └────────────────────────────────────────────────────────┘
```

1. **Reflexion (Shinn et al., NeurIPS 2023)**:
   - Verbal reinforcement learning without gradient updates. Agents convert trajectory feedback, linter failures, and auditor critiques into persistent natural language reflections.
2. **Voyager (Wang et al., 2023)**:
   - Lifelong learning through an iteratively expanding skill library. Complex operational solutions are modularized and committed to disk as reusable runbooks.
3. **Antigravity Native Metacognition**:
   - Everything in Antigravity is **Agent-as-Code** (markdown and JSON in `.agents/`). By writing back to `.agents/rules/` and `skills/`, agents permanently upgrade the workspace's collective intelligence.

---

## 2. The 3 Tiers of Agent Self-Evolution

### Tier 1: Workspace Rule Ingestion (Reflexion Pattern — Safe & Rapid)
- **Scope**: Anti-patterns, code-style quirks, library-specific gotchas, and common developer misconceptions.
- **Target File**: `.agents/rules/project-learnings.md` or scoped domain rules (e.g. `.agents/rules/frontend-learnings.md`).
- **Mechanism**:
  - When an auditor flags a recurring mistake (e.g. "Dev used arbitrary Tailwind pixel values instead of tokens"), the squad extracts the root cause and appends a single, high-density negative constraint to the rule file.
  - On the next prompt, Antigravity automatically loads this rule into context.

### Tier 2: Skill Accumulation (Voyager Pattern — Procedural Knowledge)
- **Scope**: Reusable recipes, migration guides, and multi-step deployment runbooks.
- **Target Directory**: `.agents/skills/<new-skill-name>/`
- **Mechanism**:
  - When a squad successfully solves a novel, multi-step problem (e.g. setting up Mock Service Worker with Vitest in Vite 6), `skill-workflow-designer` scaffolds a new skill directory with `SKILL.md` and reference manuals.
  - Future developer turns can invoke `@skill-name` directly.

### Tier 3: Persona & Prompt Mutation (High Impact — Strict Human Gate Required)
- **Scope**: Refactoring agent roles, updating toolsets, clarifying responsibilities, or optimizing prompt directives.
- **Target File**: `.agents/plugins/<plugin>/agents/<agent-name>.md`
- **Mechanism**:
  - Used only when an agent persona is demonstrably misaligned with its domain duties.
  - **MANDATORY**: Must generate a clear Git diff and solicit explicit approval from the user via `ask_question` before applying changes.

---

## 3. The Phase 6 Retrospective Protocol

At the conclusion of an engineering sprint, feature implementation, or after surviving a Remediation Loop (Cycle 1 or 2), the squad activates Phase 6:

### The 4 Retrospective Questions (Post-Mortem Inquiry):
1. **What unexpected friction or remediation loops occurred?**
   *(e.g. "The auditor rejected the code twice due to missing Zod response validation.")*
2. **Which directive was missing, ambiguous, or violated?**
   *(e.g. "The core developer agent prompt did not explicitly mandate Zod schemas for 200 OK responses.")*
3. **What is the minimal, permanent fix?**
   - *Option A*: Append a 1-line directive to `.agents/rules/project-learnings.md`.
   - *Option B*: Package the working solution into a new skill runbook.
   - *Option C*: Patch the subagent's prompt in `agents/*.md`.
4. **Is human confirmation required?**
   - Rule/Skill additions: Log summary to chat.
   - Persona mutations: **Halt and request user confirmation via `ask_question`**.

---

## 4. Inviolable Safety Guardrails for Self-Modifying Agents

Self-modifying systems without guardrails suffer from **Prompt Drift**, **Rule Bloat**, and **Security Degradation**. All agents must obey four non-negotiable laws:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ GUARDRAIL 1: AUDIT RUBRIC IMMUTABILITY                                      │
│ Agents are strictly forbidden from modifying evaluation-rubric.md to        │
│ artificially lower quality bars or pass failed audits.                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ GUARDRAIL 2: MANDATORY HUMAN GATE FOR PROMPT MUTATIONS                      │
│ Any modification to agents/*.md system prompts requires explicit Option A   │
│ approval via ask_question with a side-by-side markdown diff.                │
├─────────────────────────────────────────────────────────────────────────────┤
│ GUARDRAIL 3: ATOMIC GIT VERSIONING                                          │
│ Every self-evolution edit must be committed to Git with a clear message     │
│ (e.g. "learn(rules): record MSW setup gotcha from sprint retro").          │
├─────────────────────────────────────────────────────────────────────────────┤
│ GUARDRAIL 4: RULE COMPACTNESS & ANTI-BLOAT POLICY                           │
│ Learning rule files must never exceed 100 lines. When reaching capacity,     │
│ the Architect must consolidate, deduplicate, and prune obsolete entries.   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Schema for `.agents/rules/project-learnings.md`

When appending learned lessons, follow this high-density format:

```markdown
# Project Learnings & Anti-Patterns (Continuous Evolution Log)

## [YYYY-MM-DD] Feature / Incident Name
- **Context**: Brief description of the problem solved or friction encountered.
- **Root Cause**: Why the agent or developer initially made a mistake.
- **Mandatory Directive**: Inviolable instruction for all future agent invocations (e.g. "NEVER use mock data in components/; always import from api/").
```
