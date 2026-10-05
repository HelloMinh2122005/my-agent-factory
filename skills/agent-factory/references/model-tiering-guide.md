# Subscription-Aware Model Tiering & Allocation Guide

This guide establishes the rules for selecting and allocating Google Gemini model tiers (`pro` vs `flash`) when designing AI subagents in the Google Antigravity ecosystem.

---

## 1. Foundational Policy: Ask First, Default Intelligently

1. **Mandatory User Inquiry**: When designing a new agent or squad, always ask the user if they have specific model tier preferences for each role.
2. **Subscription-Aware Default Fallback**: If the user does not specify a model or defers to the system, the squad must automatically apply the optimal model based on the user's active **Antigravity Subscription Tier**.

---

## 2. Subscription Tier Strategies

### A. Antigravity Pro Subscription Optimization (Default Production Profile)
> **Default to Gemini 3.8 Flash for execution agents to maximize throughput, minimize latency, and conserve rate limits, while reserving Gemini Pro for heavy reasoning, architectural planning, and deep static auditing.**
- **Gemini 3.8 Flash**: UI developers, E2E testers, task workers, scrapers, documentation writers, skill scaffolders.
- **Gemini Pro**: Meta-architects, tech leads, deep compliance auditors, complex state-machine designers.

### B. Antigravity Free / Rate-Limited Profiles
For users operating on free tiers or tight RPM/TPM quotas:
> **Default to Gemini 3.8 Flash across ALL roles (including Architect & Auditor).**
- Flash ensures uninterrupted multi-agent execution loops without triggering fatal `429 RESOURCE_EXHAUSTED` errors.
- Elevate to `pro` only if the user explicitly confirms available quota.

### C. Enterprise / Ultra Profiles
For enterprise teams with elevated token limits:
- Use `pro` across all strategic design and architectural evaluation roles.
- Retain `flash` for high-frequency execution tasks (e.g. running parallel unit tests) purely for speed and minimal latency.

---

## 3. Persona-to-Model Tiering Matrix

| Persona Role | Recommended Model | Primary Justification |
| :--- | :--- | :--- |
| **Lead Tech Architect / Meta-Architect** | `pro` | Requires multi-hop strategic reasoning, domain decomposition, and deep dependency mapping. |
| **Static Code Quality / Compliance Auditor** | `pro` | Requires exhaustive edge-case detection, strict rubric adherence, and anti-hallucination rigor. |
| **Product Owner / Business Analyst** | `pro` | Synthesizes complex market research, competitor benchmarks, and ambiguous business specs. |
| **Core Logic & State Developer** | `pro` or `flash` | `pro` for complex algorithms / state machines; `flash` for standard CRUD, API callers, and Zod schemas. |
| **UI & Design System Developer** | `flash` | High-speed component templating, Tailwind token mapping, and visual CSS styling. |
| **E2E Tester / QA Executor** | `flash` | Rapid execution of test scripts, browser automation steps, and DOM assertions. |
| **Skill & Workflow Designer** | `flash` | Fast generation of Markdown templates, runbooks, and configuration manifests. |

---

## 4. Antigravity YAML Frontmatter Representation

Every subagent manifest must explicitly declare its model in the YAML frontmatter:

```yaml
---
name: my-specialized-agent
description: Detailed role description and invocation triggers.
model: flash  # or 'pro' based on the tiering matrix above
subagent: true
tools:
  - view_file
  - write_to_file
---
```

### Prohibited Practices:
- **Never omit the `model` key**: Antigravity requires explicit model attribution to avoid falling back to unpredictable defaults.
- **Never assign `pro` indiscriminately**: Overusing `pro` for simple, repetitive execution roles causes unnecessary latency and rapid quota exhaustion.
