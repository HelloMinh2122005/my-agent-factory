# Human Alignment & Research-First Engineering Rule

## Core Principle
Every agent, skill, and plugin design initiative must be grounded in two non-negotiable fundamentals:
1. **Deep User Understanding & Complexity Gate**: Comprehend the user's domain, real operational constraints, and workflow philosophy before proposing solutions. Always choose the simplest effective architecture.
2. **Prior Art & Open-Source Research**: Stand on the shoulders of giants. Never reinvent the wheel when battle-tested open-source frameworks, academic patterns, or industry standards already exist.

---

## Mandatory Engineering Directives

### 1. Step 1: Deep User Alignment & Quantitative Complexity Gate (Anthropic Rule #1)
- Never start authoring agent files or system prompts immediately upon receiving an initial prompt.
- **Compute Architecture Complexity Score (ACS)**:
  - *Single linear task or file-scoped rule*: +1 pt
  - *Multi-step procedure with tools or runbooks*: +2 pts
  - *Decoupled domain boundaries (Data vs UI vs Testing)*: +3 pts
  - *Asynchronous / Long-horizon lifecycle or dual sign-off QA*: +4 pts
- **Gate Thresholds**:
  - *Score 1 (Low)*: Recommend a single Antigravity **Rule** (`rules/*.md`).
  - *Score 2–3 (Low-Medium)*: Recommend a standalone Antigravity **Skill** (`skills/<name>/`).
  - *Score 4–5 (Medium)*: Recommend **1 Specialist Agent + 1 Tester**.
  - *Score 6+ (High)*: Architect a full **Multi-Agent Squad** (3-5 specialized personas).
- If requirements or boundaries are underspecified, formulate precise questions via `ask_question` to align with the user first.

### 2. Step 2: Open-Source & Industry Prior Art Research (Never Reinvent the Wheel)
- Before designing any agent architecture or workflow, actively research the state of the art using search and inspection tools:
  - **SOP & Role Collaboration**: Study MetaGPT's Standard Operating Procedures ("Code = SOP(Team)").
  - **Architectural Patterns**: Review Anthropic's *Building Effective Agents* (Router, Orchestrator-Subagent, Evaluator-Optimizer, Parallelization).
  - **Meta-Agent Decomposition**: Study ROMA (Recursive Open Meta-Agent) and LangGraph cyclic state-machine patterns.
  - **Evaluation & Alignment**: Reference G-Eval rubrics, LLM-as-a-judge trajectory grading, and DSPy metric compilation principles.
- Synthesize proven design patterns into the target agent architecture rather than building novel, untested mechanisms from scratch.

### 3. Step 3: Interactive Co-Pilot Approval Gate (Option A) & Blackboard State Persistence
- Always present the architectural blueprint to the user for explicit approval via `ask_question` before writing code:
  - Quantitative ACS score & justification.
  - Role Decomposition & Responsibilities.
  - Model Tiering Matrix (`pro` vs `flash`).
  - Tool Permissions Matrix (Principle of Least Privilege).
  - Directory & File Layout.
- **Filesystem Blackboard Persistence**: Upon user approval, the Architect must write `.agents/blueprint.md` and initialize `.agents/.factory-state.json` to ground subsequent worker subagents with deterministic state.

### 4. Step 4: Subscription-Aware Model Selection
- Proactively clarify with the user which model tier they prefer for newly created agents.
- **Default Fallback Rules**:
  - **Antigravity Pro**: Default to **Gemini 3.8 Flash** for execution agents (UI builders, E2E testers, task workers, scrapers) to optimize latency, throughput, and rate limits. Reserve **Gemini Pro** for heavy reasoning agents (Tech Leads, Architects, Static Code Quality Auditors).
  - **Antigravity Free / Rate-Limited**: Default to **Gemini 3.8 Flash** across all roles to avoid quota exhaustion.
  - **Enterprise**: Leverage **Gemini Pro** across architectural and critical analytical pathways.

### 5. Step 5: Remediation Circuit Breaker (Anti-Ping-Pong Guard)
- When coordinating quality audits between authoring agents and `agent-auditor-validator`, strictly enforce a **maximum of 2 remediation cycles**.
- Track `remediation_cycle` in `.agents/.factory-state.json`. If defects persist on cycle 2, halt execution immediately (`HALT_REMEDIATION`) and escalate unresolved findings to the user via `ask_question`. Autonomous infinite loops are strictly prohibited.

### 6. Step 6: Retrospective & Continuous Self-Evolution (The Learning Flywheel)
- Conclude sprints and friction episodes with an explicit post-mortem inquiry (Reflexion pattern).
- **Semantic Conflict & Anti-Poisoning Check**: Prior to appending lessons into `.agents/rules/project-learnings.md`, verify that the root cause is valid (not a transient external network failure) and ensure the new directive does not contradict existing directives.
- Keep `.agents/rules/project-learnings.md` under 100 lines; prune or consolidate when reaching capacity.
- Scaffold reusable procedural discoveries into `.agents/skills/<new-skill>/`.
- **Inviolable Mutation Guard**: Never mutate system prompts or evaluation rubrics without explicit user confirmation via `ask_question`. Protect `evaluation-rubric.md` via `hooks.json` lifecycle hook.
