# Meta-Agent Factory Execution Workflow (SOP)

This document specifies the standard operating procedure (SOP) governing the lifecycle of agent, skill, and plugin creation within the Agent Factory.

---

## The 5-Phase Factory Pipeline

```text
[User Request / New Domain Need]
                 │
                 ▼
Phase 1: USER ALIGNMENT & INTENT EXTRACTION
├── Dissect business problem & target domain
├── Identify end-user workflows & interactions
└── Clarify ambiguities before proposing designs
                 │
                 ▼
Phase 2: OPEN-SOURCE PRIOR ART RESEARCH
├── Search authoritative sources & open-source repos
├── Extract proven patterns (MetaGPT, Anthropic, ROMA, LangGraph)
└── Document reusable benchmarks (Do NOT reinvent the wheel)
                 │
                 ▼
Phase 3: ARCHITECTURAL BLUEPRINT & CO-PILOT GATE (Option A)
├── Formulate role breakdown & single responsibilities
├── Map model tiering (Pro vs Flash, default Gemini 3.8 Flash)
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

## Detailed Phase Breakdown

### Phase 1: User Alignment & Intent Extraction
1. **Analyze User Goal**: Understand what capability the user wants to introduce.
2. **Identify Scope Boundaries**: What is strictly in scope? What is explicitly out of scope?
3. **Formulate Clarification Questions**: If requirements are ambiguous, ask directly using structured options or clear bullet points.
*Exit Criteria*: Clear, unambiguous understanding of the desired domain capability.

### Phase 2: Open-Source Prior Art Research
1. **Search Repositories & Research Papers**: Use `search_web` to review how leading open-source projects solve this domain.
2. **Benchmark SOPs & Workflows**: Check MetaGPT, Anthropic patterns, LangGraph state-machine patterns, or DSPy prompt engineering strategies.
3. **Synthesize Findings**: Identify 2-3 standard practices to adopt and document them in the architectural dossier.
*Exit Criteria*: Established set of reusable open-source benchmarks; zero duplicate wheel-reinvention.

### Phase 3: Architectural Blueprint & Co-Pilot Gate (Option A)
1. **Compose Blueprint**:
   - Agent Personas (Name, Role, Responsibilities).
   - Model Tiering: Explicitly ask user or apply default (e.g. Gemini 3.8 Flash for Antigravity Pro subscribers).
   - Tool Matrix: Minimum required tools per persona.
   - Folder Structure: Exact path layout within `plugins/<plugin-name>/`.
2. **Present to User**: Deliver the blueprint clearly in chat.
3. **AWAIT USER APPROVAL**: **Strict Gate**: Do not invoke authoring subagents or write files until the user explicitly confirms the architecture.
*Exit Criteria*: Explicit user approval of the blueprint.

### Phase 4: Parallel Codification & Generation
1. **Delegate Personas**: `prompt-persona-engineer` authors `agents/*.md` with valid YAML frontmatter, mental models, inviolable directives, and output contracts.
2. **Delegate Skills & Workflows**: `skill-workflow-designer` authors `SKILL.md`, `config.json`, `workflow.md`, and modular documentation in `references/`.
3. **Package Manifests**: Generate `plugin.json` and contextual `rules/`.
*Exit Criteria*: All files generated and conforming to Antigravity file conventions.

### Phase 5: Independent QA Audit & Delivery
1. **Independent Inspection**: `agent-auditor-validator` (equipped strictly with read-only tools) inspects:
   - YAML frontmatter correctness (`name`, `description`, `model`, `subagent: true`, `tools`).
   - JSON syntax and schema compliance in `plugin.json` and `config.json`.
   - Tool permissions compliance (no excess tools).
   - Relative path integrity across all Markdown links.
2. **Remediation Loop (if needed)**: If any check fails, authoring agents correct the defect (max 2 cycles).
3. **Final Delivery Dossier**: Present the verified plugin tree and usage instructions to the user.
*Exit Criteria*: Unanimous PASS from `agent-auditor-validator`.
