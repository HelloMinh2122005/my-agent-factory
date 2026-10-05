# my-agent-factory — Meta-Agent Engineering & Squad Factory for Google Antigravity

[![Antigravity Compatible](https://img.shields.io/badge/Google%20Antigravity-Ready-4285F4.svg)](https://antigravity.google)
[![Architecture](https://img.shields.io/badge/Architecture-Meta--Agent%20Squad-0F9D58.svg)](#)
[![Model Optimization](https://img.shields.io/badge/Default%20Model-Gemini%203.8%20Flash-F4B400.svg)](#)
[![Philosophy](https://img.shields.io/badge/Philosophy-Standing%20on%20Giants'%20Shoulders-DB4437.svg)](#)

`my-agent-factory` is a specialized **AI Meta-Agent Engineering System & Squad Factory** designed specifically for **Google Antigravity**. It automates the research, architectural decomposition, persona prompt drafting, skill codification, and QA validation required to produce enterprise-grade Antigravity agent squads and plugins.

---

## 1. Core Operating Philosophy

Instead of manually drafting prompts and guessing directory structures, the Agent Factory operates on five non-negotiable engineering principles:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. DEEP USER UNDERSTANDING (Step 1)                                         │
│    Comprehend real operational domain constraints before designing.         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. STAND ON THE SHOULDERS OF GIANTS (Step 2 - Never Reinvent the Wheel)     │
│    Synthesize battle-tested open-source architectures (MetaGPT SOPs,        │
│    Anthropic Agent Patterns, ROMA, LangGraph State Machines, DSPy Evals).   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. INTERACTIVE CO-PILOT APPROVAL GATE (Option A)                            │
│    Always propose the complete Architectural Blueprint (Roles, Models,      │
│    Tools, Hierarchy) to the user and await explicit confirmation.           │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. SUBSCRIPTION-AWARE MODEL SELECTION                                       │
│    Proactively ask user; default to Gemini 3.8 Flash for execution agents   │
│    to optimize throughput, latency, and rate limits on Antigravity Pro.     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. INDEPENDENT DUAL QA AUDIT                                                │
│    Enforce read-only validator inspection for YAML frontmatter, JSON        │
│    schemas, least-privilege tool security, and path integrity.              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The Agent Factory Squad

The system is powered by four specialized meta-agent personas:

| Agent Persona | Role & Responsibilities | Model Tier | Tool Permissions |
| :--- | :--- | :--- | :--- |
| **`@meta-agent-architect`** | **Lead Meta-Architect & Orchestrator**: Ingests user domain needs, conducts open-source research, decomposes domain into single-responsibility roles, determines model tiering, enforces tool least-privilege, and manages the Option A Co-Pilot approval gate. | `pro` | Web Search, Inspection, Code Tools |
| **`@prompt-persona-engineer`** | **Persona & Behavior Specialist**: Drafts high-density system prompts, mental models, inviolable directives, edge-case mitigation protocols, and deterministic output contracts. | `pro` | Code & Filesystem Tools |
| **`@skill-workflow-designer`** | **Skill & Workflow Specialist**: Packages domain knowledge into Antigravity `skills/` using progressive disclosure (`SKILL.md` + modular `references/`), authors SOP `workflow.md`, and configures `config.json`. | `flash` *(Pro-tier default)* | Code & Filesystem Tools |
| **`@agent-auditor-validator`** | **Independent QA & Compliance Inspector**: Validates YAML frontmatter, checks JSON schemas (`plugin.json`, `config.json`), enforces least-privilege tool security, and verifies relative link integrity. Strictly read-only to prevent cognitive bias. | `pro` | Read-Only Inspection Tools |

---

## 3. The 5-Phase Factory Pipeline

```text
[User Domain Request / High-Level Need]
                    │
                    ▼
Phase 1: USER ALIGNMENT & INTENT EXTRACTION
├── Dissect business objectives & end-user personas
└── Clarify boundaries & ambiguous constraints
                    │
                    ▼
Phase 2: OPEN-SOURCE PRIOR ART RESEARCH
├── Search authoritative sources & GitHub repos
├── Benchmark proven patterns (MetaGPT SOPs, Anthropic, ROMA)
└── Document reusable benchmarks (No wheel-reinvention)
                    │
                    ▼
Phase 3: ARCHITECTURAL BLUEPRINT & CO-PILOT GATE (Option A)
├── Formulate role breakdown & single responsibilities
├── Map model tiering (Gemini 3.8 Flash default for Pro users)
├── Establish tool permission matrix (Least Privilege)
└── Present to user & AWAIT EXPLICIT APPROVAL
                    │ (User Approval)
                    ▼
Phase 4: PARALLEL GENERATION & CODIFICATION
├── prompt-persona-engineer -> System prompts, YAML frontmatter, mental models
└── skill-workflow-designer -> SKILL.md, config.json, progressive disclosure
                    │
                    ▼
Phase 5: INDEPENDENT QUALITY AUDIT & DELIVERY
├── agent-auditor-validator (Read-only inspection)
├── Validate schemas, paths, permissions, and token economy
└── Deliver clean, tested plugin package to user
```

---

## 4. Directory Structure

```text
my-agent-factory/
├── plugin.json                    # Antigravity Plugin Manifest
├── README.md                      # System manual & developer onboarding (this file)
│
├── rules/                         # Workspace-wide rules
│   ├── verification.md            # Zero-guess policy & path integrity
│   └── human-alignment-and-research.md # Alignment, research-first & model tiering
│
├── agents/                        # Specialized Meta-Agent Personas
│   ├── meta-agent-architect.md    # Lead Architect & Orchestrator
│   ├── prompt-persona-engineer.md # Prompt & Persona Author
│   ├── skill-workflow-designer.md # Skill & Progressive Disclosure Designer
│   └── agent-auditor-validator.md # Independent QA & Compliance Inspector
│
├── skills/                        # Packaged Meta-Skills
│   └── agent-factory/
│       ├── SKILL.md               # Progressive disclosure entry point
│       ├── config.json            # Triggers, schemas, policies
│       ├── workflow.md            # 5-phase SOP lifecycle
│       ├── system_prompt.md       # Operational directives & mental models
│       └── references/            # Deep architectural references
│           ├── open-source-prior-art.md   # MetaGPT, Anthropic, ROMA, LangGraph
│           ├── model-tiering-guide.md     # Subscription-aware model selection
│           ├── antigravity-spec-guide.md  # Complete Antigravity specs
│           └── evaluation-rubric.md       # LLM judge rubrics & compliance matrix
│
└── templates/                     # Production-ready starter boilerplates
    ├── agent-template.md          # Starter agent manifest with frontmatter
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
@meta-agent-architect: I need a new Antigravity squad for DevOps & CI/CD Kubernetes.
Please follow the 5-phase factory pipeline:
1. Research existing open-source DevOps agent frameworks.
2. Present the Architectural Blueprint (Option A) for my approval.
3. Default to Gemini 3.8 Flash for execution workers.
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
* **Anthropic Research**: *Building Effective Agents* (Router, Orchestrator-Workers, Evaluator-Optimizer).
* **ROMA** (*Sentient AGI*): Recursive Open Meta-Agent hierarchical decomposition.
* **LangGraph** (*LangChain*): Cyclic stateful agent architectures & human-in-the-loop checkpointing.
* **DSPy** (*Stanford NLP*): Trajectory evaluation and programmatic rubric grading.
