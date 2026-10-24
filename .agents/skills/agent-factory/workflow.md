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
Phase 2: INHERIT THE WORLD'S KNOWLEDGE (PRIOR ART)
├── Search GitHub, marketplaces & community libraries for ready-made skills/agents/plugins
├── Read & risk-check candidates; decide install → adapt → reference → author
├── Extract proven patterns (MetaGPT, Anthropic, ROMA, LangGraph)
└── Document the reuse plan with sources (Do NOT reinvent the wheel)
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
Phase 5: INDEPENDENT QUALITY AUDIT, PEER REVIEW & DELIVERY
├── agent-auditor-validator (Strictly read-only inspection)
├── Cross-platform peer review by Claude Code via agent-chat (≤2 rounds)
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

### Phase 1: User Alignment & Quantitative Complexity Gate
*Mandatory Reference*: [Open-Source Prior Art & Foundations](./references/open-source-prior-art.md)
1. **Analyze User Goal**: Understand what capability the user wants to introduce.
2. **Compute Architecture Complexity Score (ACS)**:
   - *Single linear task or file-scoped rule*: +1 pt
   - *Multi-step procedure with tools or runbooks*: +2 pts
   - *Decoupled domain boundaries (Data vs UI vs Testing)*: +3 pts
   - *Asynchronous / Long-horizon lifecycle or dual sign-off QA*: +4 pts
3. **Apply Gate Thresholds**:
   - *Score 1 (Low)*: Recommend a single Antigravity **Rule** (`rules/*.md`).
   - *Score 2–3 (Low-Medium)*: Recommend a standalone Antigravity **Skill** (`skills/<name>/`).
   - *Score 4–5 (Medium)*: Recommend **1 Specialist Agent + 1 Tester**.
   - *Score 6+ (High)*: Architect a full **Multi-Agent Squad** (3-5 specialized personas).
4. **Formulate Clarification Questions**: If requirements are ambiguous, prompt the user via `ask_question`.
*Exit Criteria*: Confirmed ACS score, clear scope, and consensus on architectural tier.

### Phase 2: Inherit the World's Knowledge (Prior Art)
*Mandatory Reference*: [Open-Source Prior Art & Foundations](./references/open-source-prior-art.md) (§5 lists the community libraries)
1. **Search for Existing Artifacts**: Delegate to `github-repo-scout` (skill `github-repo-scout`), which searches and ranks GitHub repositories with the shared rubric and writes `.research/<YYYYMMDD>-<slug>/repos-antigravity.md`. Supplement with `search_web` / `read_url_content` on GitHub, plugin marketplaces and the community libraries (local mirror: `scripts/sync-vendor.sh` → `~/.agent-factory/vendor/`) for skills, agents and plugins that already solve each need.
2. **Read & Risk-Check**: Read every candidate file. Flag session-wide context injection, bundled scripts, network calls, credential access and instruction-override language; note license, last update and always-on token cost.
3. **Decide per Need (Reuse Ladder)**: install as-is → adapt a copy (keep LICENSE + `SOURCE.txt` with URL and commit) → reference the pattern → author new only with a written reason.
4. **Benchmark SOPs & Workflows**: Check MetaGPT, Anthropic patterns, LangGraph state-machine patterns, or LLM-as-a-judge rubric strategies.
5. **Write the Reuse Plan**: List every installed, adapted, referenced and authored item with its source in the architectural dossier.
6. **Peer Review the Research**: `github-repo-scout` requests a review of its ranking from `claude-code/github-repo-scout` (skill `peer-review`); fold accepted findings into the reuse plan before Phase 3.
*Exit Criteria*: Every need maps to a reuse decision with a source, or to "author new" with a reason; zero duplicate wheel-reinvention.

### Phase 3: Architectural Blueprint, Co-Pilot Gate (Option A) & Blackboard State Persistence
*Mandatory Reference*: [Subscription-Aware Model Tiering Guide](./references/model-tiering-guide.md)
1. **Compose Blueprint**:
   - Agent Personas (Name, Role, Responsibilities).
   - Model Tiering: Default to Gemini 3.8 Flash for execution agents on Antigravity Pro; reserve Pro for reasoning roles.
   - Tool Matrix: Minimum required tools per persona (strictly zero destructive tools for validators).
   - Folder Structure: Exact path layout within `plugins/<plugin-name>/`.
2. **Present to User**: Trigger interactive modal using `ask_question`.
3. **AWAIT USER APPROVAL**: **Strict Gate**: Do not invoke authoring subagents or write files until the user explicitly confirms the architecture.
4. **Persist Blackboard & Initialize State**:
   - The Architect writes the approved blueprint to `.agents/blueprint.md` (or `.agents/blueprint.json`).
   - The Architect initializes the session state in `.agents/.factory-state.json`:
     ```json
     {
       "session_id": "auto",
       "current_phase": "PARALLEL_GENERATION",
       "complexity_score": 6,
       "remediation_cycle": 0,
       "max_remediation_cycles": 2,
       "blueprint_path": ".agents/blueprint.md",
       "audit_verdict": "PENDING"
     }
     ```
*Exit Criteria*: Explicit user approval of the blueprint via interactive modal and persistent state file initialized on disk.

### Phase 4: Parallel Codification & Generation
*Mandatory Reference*: [Antigravity Specification Guide](./references/antigravity-spec-guide.md)
1. **Read Blackboard**: Downstream agents read `.agents/blueprint.md` from disk as the single source of truth.
2. **Delegate Personas**: `prompt-persona-engineer` authors `agents/*.md` with valid YAML frontmatter, mental models, inviolable directives, and output contracts.
3. **Delegate Skills & Workflows**: `skill-workflow-designer` authors `SKILL.md`, `workflow.md`, and modular documentation in `references/`.
4. **Package Manifests**: Generate `plugin.json` and contextual `rules/`.
*Exit Criteria*: All files generated and conforming to Antigravity file conventions.

### Phase 5: Independent QA Audit & Delivery
*Mandatory Reference*: [Agent Evaluation & Rubrics](./references/evaluation-rubric.md)
1. **Independent Inspection**: `agent-auditor-validator` (equipped strictly with read-only tools: `view_file`, `grep_search`, `list_dir`) inspects:
   - YAML frontmatter correctness (`name`, `description`, `model`, `subagent: true`, `tools`).
   - JSON syntax and schema compliance in `plugin.json`.
   - Tool permissions compliance (no excess tools, reviewers strictly read-only).
   - Relative path integrity across all Markdown links.
   - Rubric immutability verification (ensuring `evaluation-rubric.md` is untouched).
2. **State-Tracked Remediation Circuit Breaker (Max 2 Cycles)**:
   - Read and increment `remediation_cycle` in `.agents/.factory-state.json`.
   - *Cycle 1*: Authoring agents remediate reported deficiencies.
   - *Cycle 2*: Validator re-inspects. If checks still fail (`remediation_cycle >= 2`), **HALT immediately** (`HALT_REMEDIATION`). Do not continue looping. Escalate unresolved issues to the user via `ask_question`.
3. **Cross-Platform Peer Review**: After the auditor PASS, send `PEER_REVIEW_REQUEST` lead to lead to `claude-code/factory-lead` (skill `peer-review`); address BLOCKER/MAJOR findings within ≤2 rounds.
4. **Final Delivery Dossier**: Present the verified plugin tree, usage instructions and the peer reviewer's verdict to the user.
*Exit Criteria*: Unanimous PASS from `agent-auditor-validator` or user override upon Circuit Breaker halt.

### Phase 6: Retrospective & Continuous Self-Evolution
*Mandatory Reference*: [Retrospective & Continuous Self-Evolution Guide](./references/retrospective-and-self-evolution.md)
1. **Reflexion Post-Mortem**:
   - Analyze any remediation loops, tool execution errors, or ambiguities that occurred during the session.
   - Formulate root-cause explanations and permanent preventive measures.
2. **Tier 1 Self-Evolution (Conflict-Checked Rule Ingestion)**:
   - Check proposed directive against existing rules in `.agents/rules/project-learnings.md` to prevent semantic contradictions.
   - Append concise negative constraint to `.agents/rules/project-learnings.md` (keep file < 100 lines; prune/consolidate if at capacity).
3. **Tier 2 Self-Evolution (Skill Accumulation)**:
   - If a novel, reusable procedural workflow was engineered, delegate to `skill-workflow-designer` to scaffold a permanent runbook under `.agents/skills/<new-skill>/`.
4. **Tier 3 Self-Evolution (Prompt Mutation Guard)**:
   - If a subagent persona prompt in `agents/*.md` requires refinement, present the proposed diff and seek explicit user approval via `ask_question`. Never mutate system prompts silently.
*Exit Criteria*: Institutional lessons committed to Git; workspace intelligence baseline permanently elevated.
