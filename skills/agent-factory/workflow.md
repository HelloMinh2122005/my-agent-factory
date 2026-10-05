# Meta-Agent Factory Execution Workflow (SOP)

This document specifies the standard operating procedure (SOP) governing the lifecycle of agent, skill, and plugin creation within the Agent Factory.

---

## The 6-Phase Factory Pipeline

```text
[User Request / New Domain Need]
                 │
                 ▼
Phase 1: USER ALIGNMENT & COMPLEXITY GATE (ask_question)
├── Dissect business problem & target domain
├── Anthropic Rule #1: Single Rule vs Single Skill vs Multi-Agent Squad
└── Clarify ambiguities & constraints before proposing designs
                 │
                 ▼
Phase 2: OPEN-SOURCE PRIOR ART RESEARCH
├── Search authoritative sources & open-source repos
├── Extract proven patterns (MetaGPT, Anthropic, ROMA, LangGraph)
└── Document reusable benchmarks (Do NOT reinvent the wheel)
                 │
                 ▼
Phase 3: ARCHITECTURAL BLUEPRINT & CO-PILOT GATE (Option A via ask_question)
├── Formulate role breakdown & single responsibilities
├── Map model tiering (Pro vs Flash, subscription-aware)
├── Establish tool permission matrix (Least Privilege)
└── Present interactive modal & AWAIT EXPLICIT APPROVAL
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
├── Remediation Circuit Breaker: Max 2 cycles (Halt on failure)
└── Deliver clean, tested plugin package to user
                 │ (Sprint Completed or Friction Encountered)
                 ▼
Phase 6: RETROSPECTIVE & CONTINUOUS SELF-EVOLUTION
├── Reflexion Post-Mortem: Extract friction, remediation causes, and anti-patterns
├── Tier 1: Ingest negative constraints into .agents/rules/project-learnings.md
├── Tier 2: Package novel procedural solutions into .agents/skills/<new-skill>/
└── Tier 3: Persona mutation (Strict Option A user approval via ask_question)
```

---

## Detailed Phase Breakdown

### Phase 1: User Alignment & Complexity Gate
*Mandatory Reference*: [Open-Source Prior Art & Foundations](./references/open-source-prior-art.md)
1. **Analyze User Goal**: Understand what capability the user wants to introduce.
2. **Apply Complexity Gate (Anthropic "Start Simple" Principle)**:
   - *Low Complexity*: Recommend a single Antigravity **Rule** (`rules/*.md`) or standalone **Skill** (`skills/<name>/SKILL.md`).
   - *Medium Complexity*: Recommend **1 Specialist Agent + 1 Tester**.
   - *High Complexity*: Architect a full **Multi-Agent Squad** (3-5 specialized personas).
3. **Formulate Clarification Questions**: If requirements are ambiguous, prompt the user via `ask_question`.
*Exit Criteria*: Clear understanding of scope and confirmation of whether a full squad or single skill is needed.

### Phase 2: Open-Source Prior Art Research
*Mandatory Reference*: [Open-Source Prior Art & Foundations](./references/open-source-prior-art.md)
1. **Search Repositories & Research Papers**: Use `search_web` to review how leading open-source projects solve this domain.
2. **Benchmark SOPs & Workflows**: Check MetaGPT, Anthropic patterns, LangGraph state-machine patterns, or LLM-as-a-judge rubric strategies.
3. **Synthesize Findings**: Identify 2-3 standard practices to adopt and document them in the architectural dossier.
*Exit Criteria*: Established set of reusable open-source benchmarks; zero duplicate wheel-reinvention.

### Phase 3: Architectural Blueprint & Co-Pilot Gate (Option A)
*Mandatory Reference*: [Subscription-Aware Model Tiering Guide](./references/model-tiering-guide.md)
1. **Compose Blueprint**:
   - Agent Personas (Name, Role, Responsibilities).
   - Model Tiering: Default to Gemini 3.8 Flash for execution agents on Antigravity Pro; reserve Pro for reasoning roles.
   - Tool Matrix: Minimum required tools per persona (strictly zero destructive tools for validators).
   - Folder Structure: Exact path layout within `plugins/<plugin-name>/`.
2. **Present to User**: Trigger interactive modal using `ask_question`.
3. **AWAIT USER APPROVAL**: **Strict Gate**: Do not invoke authoring subagents or write files until the user explicitly confirms the architecture.
*Exit Criteria*: Explicit user approval of the blueprint via interactive modal or chat confirmation.

### Phase 4: Parallel Codification & Generation
*Mandatory Reference*: [Antigravity Specification Guide](./references/antigravity-spec-guide.md)
1. **Delegate Personas**: `prompt-persona-engineer` authors `agents/*.md` with valid YAML frontmatter, mental models, inviolable directives, and output contracts.
2. **Delegate Skills & Workflows**: `skill-workflow-designer` authors `SKILL.md`, `workflow.md`, and modular documentation in `references/`.
3. **Package Manifests**: Generate `plugin.json` and contextual `rules/`.
*Exit Criteria*: All files generated and conforming to Antigravity file conventions.

### Phase 5: Independent QA Audit & Delivery
*Mandatory Reference*: [Agent Evaluation & Rubrics](./references/evaluation-rubric.md)
1. **Independent Inspection**: `agent-auditor-validator` (equipped strictly with read-only tools: `view_file`, `grep_search`, `list_dir`) inspects:
   - YAML frontmatter correctness (`name`, `description`, `model`, `subagent: true`, `tools`).
   - JSON syntax and schema compliance in `plugin.json`.
   - Tool permissions compliance (no excess tools, reviewers strictly read-only).
   - Relative path integrity across all Markdown links.
2. **Remediation Circuit Breaker (Max 2 Cycles)**:
   - *Cycle 1*: Authoring agents remediate reported deficiencies.
   - *Cycle 2*: Validator re-inspects. If checks still fail, **HALT immediately**. Do not continue looping. Escalate unresolved issues to the user via `ask_question`.
3. **Final Delivery Dossier**: Present the verified plugin tree and usage instructions to the user.
*Exit Criteria*: Unanimous PASS from `agent-auditor-validator` or user override upon Circuit Breaker halt.

### Phase 6: Retrospective & Continuous Self-Evolution
*Mandatory Reference*: [Retrospective & Continuous Self-Evolution Guide](./references/retrospective-and-self-evolution.md)
1. **Reflexion Post-Mortem**:
   - Analyze any remediation loops, tool execution errors, or ambiguities that occurred during the session.
   - Formulate root-cause explanations and permanent preventive measures.
2. **Tier 1 Self-Evolution (Rule Ingestion)**:
   - Append concise negative constraints and lessons to `.agents/rules/project-learnings.md` (keep file < 100 lines).
3. **Tier 2 Self-Evolution (Skill Accumulation)**:
   - If a novel, reusable procedural workflow was engineered, delegate to `skill-workflow-designer` to scaffold a permanent runbook under `.agents/skills/<new-skill>/`.
4. **Tier 3 Self-Evolution (Prompt Mutation Guard)**:
   - If a subagent persona prompt in `agents/*.md` requires refinement, present the proposed diff and seek explicit user approval via `ask_question`. Never mutate system prompts silently.
*Exit Criteria*: Institutional lessons committed to Git; workspace intelligence baseline permanently elevated.
