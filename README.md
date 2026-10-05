# my-agent-factory — Meta-Agent Engineering & Squad Factory for Google Antigravity

[![Antigravity Compatible](https://img.shields.io/badge/Google%20Antigravity-Ready-4285F4.svg)](https://antigravity.google)
[![Architecture](https://img.shields.io/badge/Architecture-Meta--Agent%20Squad-0F9D58.svg)](#)
[![Model Optimization](https://img.shields.io/badge/Default%20Model-Gemini%203.8%20Flash-F4B400.svg)](#)
[![Philosophy](https://img.shields.io/badge/Philosophy-Standing%20on%20Giants'%20Shoulders-DB4437.svg)](#)

`my-agent-factory` is a specialized **AI Meta-Agent Engineering System & Squad Factory** designed specifically for **Google Antigravity**. It automates the research, architectural decomposition, persona prompt drafting, skill codification, and QA validation required to produce enterprise-grade Antigravity agent squads and plugins.

---

## 1. Core Operating Philosophy

Instead of manually drafting prompts and guessing directory structures, the Agent Factory operates on seven non-negotiable engineering principles:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. DEEP USER UNDERSTANDING & COMPLEXITY GATE (Step 1)                       │
│    Comprehend domain constraints. Apply Anthropic Rule #1 ("Start Simple"): │
│    Single Rule vs Single Skill vs Multi-Agent Squad before authoring code.  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. STAND ON THE SHOULDERS OF GIANTS (Step 2 - Never Reinvent the Wheel)     │
│    Synthesize battle-tested open-source architectures (MetaGPT SOPs,        │
│    Anthropic Patterns, ROMA, LangGraph State Machines, G-Eval Rubrics).     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. INTERACTIVE CO-PILOT APPROVAL GATE (Option A via ask_question)           │
│    Propose Architectural Blueprint (Roles, Models, Tools, Directory Tree)   │
│    via interactive modal and await explicit user confirmation.              │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. SUBSCRIPTION-AWARE MODEL SELECTION                                       │
│    Proactively ask user; default to Gemini 3.8 Flash for execution agents   │
│    to optimize throughput, latency, and rate limits on Antigravity Pro.     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. PRINCIPLE OF LEAST PRIVILEGE                                             │
│    Enforce strict tool boundary isolation: Auditors have ZERO write or shell│
│    tools; Architects focus on pure planning and research orchestration.     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 6. REMEDIATION CIRCUIT BREAKER (Max 2 Cycles)                               │
│    Strictly halt automated audit ping-pong after 2 cycles to prevent         │
│    context bloat and infinite loops; escalate unresolved items to user.     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 7. CONTINUOUS SELF-EVOLUTION & RETROSPECTIVES (The Learning Flywheel)       │
│    Reflexion harvesting: Ingest post-mortem insights into .agents/rules/    │
│    and scaffold reusable skills to continuously upgrade squad intelligence. │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The Agent Factory Squad

The system is powered by four specialized meta-agent personas:

| Agent Persona | Role & Responsibilities | Model Tier | Tool Permissions |
| :--- | :--- | :--- | :--- |
| **`@meta-agent-architect`** | **Lead Meta-Architect & Orchestrator**: Ingests user domain needs, assesses quantitative complexity, conducts open-source research, decomposes domain into single-responsibility roles, determines model tiering, writes the Blueprint and session state to the Blackboard, leads Phase 6 retrospectives, and manages the interactive Co-Pilot approval gate. | `pro` | Interactive UI (`ask_question`), Web Search, Inspection, Blueprint & State Authoring *(Strictly zero application code-write)* |
| **`@prompt-persona-engineer`** | **Persona & Behavior Specialist**: Drafts high-density system prompts, mental models, inviolable directives, edge-case mitigation protocols, and deterministic output contracts. | `pro` | Code & Filesystem Authoring Tools |
| **`@skill-workflow-designer`** | **Skill & Workflow Specialist**: Packages domain knowledge into Antigravity `skills/` using progressive disclosure (`SKILL.md` + modular `references/`), authors SOP `workflow.md`, scaffolds harvested skills from retrospectives, and configures internal manifests. | `flash` *(Pro default)* | Code & Filesystem Authoring Tools |
| **`@agent-auditor-validator`** | **Independent QA & Compliance Inspector**: Validates YAML frontmatter, checks JSON schemas, verifies tool least-privilege, and checks relative link integrity. Strictly read-only to prevent cognitive bias. | `pro` | Inspection Only (`view_file`, `grep_search`, `list_dir`) *(Strictly zero write/bash)* |

---

## 3. The 6-Phase Factory Pipeline

```text
[User Domain Request / High-Level Need]
                    │
                    ▼
Phase 1: USER ALIGNMENT & QUANTITATIVE COMPLEXITY GATE (ask_question)
├── Dissect business objectives & operational constraints
└── Anthropic Rule #1 & ACS Score: Rule vs Skill vs Specialist vs Squad
                    │
                    ▼
Phase 2: OPEN-SOURCE PRIOR ART RESEARCH
├── Search authoritative sources & GitHub repos
├── Benchmark proven patterns (MetaGPT SOPs, Anthropic, ROMA)
└── Document reusable benchmarks (No wheel-reinvention)
                    │
                    ▼
Phase 3: ARCHITECTURAL BLUEPRINT, CO-PILOT GATE & BLACKBOARD PERSISTENCE
├── Formulate role breakdown & single responsibilities
├── Map model tiering (Gemini 3.8 Flash default for Pro workers)
├── Establish tool permission matrix (Least Privilege)
├── Present interactive modal (Option A via ask_question) & AWAIT APPROVAL
└── Persist .agents/blueprint.md & initialize .agents/.factory-state.json
                    │ (User Approval)
                    ▼
Phase 4: PARALLEL GENERATION & CODIFICATION
├── prompt-persona-engineer -> System prompts, YAML frontmatter, mental models
└── skill-workflow-designer -> SKILL.md, progressive disclosure, references/
                    │
                    ▼
Phase 5: INDEPENDENT QUALITY AUDIT & DELIVERY
├── agent-auditor-validator (Strictly read-only inspection)
├── Validate schemas, paths, permissions, and token economy
├── Remediation Circuit Breaker: Max 2 cycles tracked in state
└── Deliver clean, tested plugin package to user
                    │ (Sprint Complete or Friction Encountered)
                    ▼
Phase 6: RETROSPECTIVE & CONTINUOUS SELF-EVOLUTION
├── Reflexion Post-Mortem: Extract friction, remediation causes, and anti-patterns
├── Anti-Poisoning & Conflict Check: Verify validity & non-contradiction
├── Tier 1: Ingest negative constraints into .agents/rules/project-learnings.md (<100 lines)
├── Tier 2: Package novel procedural solutions into .agents/skills/<new-skill>/
└── Tier 3: Persona mutation (Strict Option A user approval via ask_question)
```

---

## 4. Directory Structure

```text
my-agent-factory/
├── plugin.json                    # Antigravity Plugin Manifest
├── hooks.json                     # Antigravity Lifecycle Hooks (PreToolUse rubric protection)
├── README.md                      # System manual & developer onboarding (this file)
│
├── scripts/                       # Native execution & safety hook scripts
│   └── protect-rubric.sh          # Hard blocking of unauthorized rubric modifications
│
├── rules/                         # Workspace-wide rules
│   ├── verification.md            # Zero-guess policy & path integrity
│   └── human-alignment-and-research.md # Alignment, ACS scoring, model tiering & retro
│
├── agents/                        # Specialized Meta-Agent Personas
│   ├── meta-agent-architect.md    # Lead Architect (ask_question + state persistence + retro)
│   ├── prompt-persona-engineer.md # Prompt & Persona Author
│   ├── skill-workflow-designer.md # Skill & Progressive Disclosure Designer
│   └── agent-auditor-validator.md # Independent QA Inspector (pure read-only)
│
├── skills/                        # Packaged Meta-Skills
│   └── agent-factory/
│       ├── SKILL.md               # Progressive disclosure entry point
│       ├── config.json            # Internal factory policy manifest (subagent data contract)
│       ├── workflow.md            # 6-phase SOP lifecycle with circuit breaker & retro
│       ├── system_prompt.md       # Operational directives & mental models
│       └── references/            # Deep architectural references (phase-gated)
│           ├── open-source-prior-art.md   # MetaGPT, Anthropic, ROMA, LangGraph
│           ├── model-tiering-guide.md     # Multi-tier subscription-aware model selection
│           ├── antigravity-spec-guide.md  # Complete Antigravity specs
│           ├── evaluation-rubric.md       # G-Eval style rubrics & compliance matrix
│           └── retrospective-and-self-evolution.md # The Continuous Learning Flywheel
│
└── templates/                     # Production-ready starter boilerplates
    ├── agent-template.md          # Starter agent manifest with frontmatter
    ├── rule-template/
    │   └── project-learnings.md   # Starter template for continuous learning logs
    ├── skill-template/
    │   └── SKILL.md               # Starter SKILL.md with progressive disclosure
    └── plugin-template/
        └── plugin.json            # Starter plugin.json manifest
```

---

## 5. How to Use

### A. Invoke in Antigravity Chat
You can trigger the squad directly in your IDE chat:

```text
@meta-agent-architect: I need a new Antigravity capability for DevOps & CI/CD Kubernetes.
Please follow the 6-phase factory pipeline:
1. Assess complexity (Does this need a single skill or full squad?).
2. Research existing open-source DevOps agent frameworks.
3. Present the Architectural Blueprint (Option A via ask_question) for my approval.
4. Default to Gemini 3.8 Flash for execution workers.
5. Conduct Phase 6 retrospective to ingest any setup gotchas into .agents/rules/.
```

### B. Installing as a Plugin in Any Project
To use this factory in any project workspace:
1. Clone or copy `my-agent-factory` into your workspace customization root:
   ```bash
   git clone https://github.com/HelloMinh2122005/my-agent-factory.git .agents/plugins/agent-factory
   ```
2. Antigravity will automatically detect `plugin.json` and ingest the squad and skill into your pair-programming environment.

---

## 6. Built on Modern Research

This repository synthesizes foundational principles from:
* **MetaGPT** (*Hong et al., ICLR 2024*): Standard Operating Procedures ("Code = SOP(Team)").
* **Anthropic Research**: *Building Effective Agents* (Complexity Gate, Router, Orchestrator-Workers, Evaluator-Optimizer).
* **Reflexion** (*Shinn et al., NeurIPS 2023*): Verbal self-reflection & episodic memory harvesting into persistent rules.
* **Voyager** (*Wang et al., 2023*): Lifelong self-expanding procedural skill libraries.
* **ROMA** (*Sentient AGI*): Recursive Open Meta-Agent hierarchical decomposition.
* **LangGraph** (*LangChain*): Cyclic stateful agent architectures & human-in-the-loop checkpointing.
* **G-Eval & Trajectory Evaluation** (*Liu et al.*): 4-part deterministic rubrics with chain-of-thought verification.
