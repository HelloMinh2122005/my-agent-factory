# Human Alignment & Research-First Engineering Rule

## Core Principle
Every agent, skill, and plugin design initiative must be grounded in two non-negotiable fundamentals:
1. **Deep User Understanding**: Comprehend the user's domain, real operational constraints, and workflow philosophy before proposing solutions.
2. **Prior Art & Open-Source Research**: Stand on the shoulders of giants. Never reinvent the wheel when battle-tested open-source frameworks, academic patterns, or industry standards already exist.

---

## Mandatory Engineering Directives

### 1. Step 1: Deep User Alignment (No Premature Construction)
- Never start authoring agent files or system prompts immediately upon receiving an initial prompt.
- Explicitly dissect the user's intent:
  - What exact domain problem is this agent squad solving?
  - Who will interact with the squad (developer, business user, CI/CD pipeline)?
  - What are the boundaries of responsibility and scope limits?
- If key requirements, tool access needs, or operational models are underspecified, formulate precise questions to align with the user first.

### 2. Step 2: Open-Source & Industry Prior Art Research (Never Reinvent the Wheel)
- Before designing any agent architecture or workflow, actively research the state of the art using search and inspection tools:
  - **SOP & Role Collaboration**: Study MetaGPT's Standard Operating Procedures ("Code = SOP(Team)").
  - **Architectural Patterns**: Review Anthropic's *Building Effective Agents* (Router, Orchestrator-Subagent, Evaluator-Optimizer, Parallelization).
  - **Meta-Agent Decomposition**: Study ROMA (Recursive Open Meta-Agent) and LangGraph cyclic state-machine patterns.
  - **Evaluation & Alignment**: Reference DSPy, LLM-as-a-judge trajectory grading, and GEval rubrics.
- Synthesize proven design patterns into the target agent architecture rather than building novel, untested mechanisms from scratch.

### 3. Step 3: Interactive Co-Pilot Approval Gate (Option A)
- Always present the architectural blueprint to the user for explicit approval before writing code:
  - Role Decomposition & Responsibilities.
  - Model Tiering Matrix (`pro` vs `flash`).
  - Tool Permissions Matrix (Principle of Least Privilege).
  - Directory & File Layout.
- Proceed to implementation only after obtaining explicit user sign-off.

### 4. Step 4: Subscription-Aware Model Selection
- Proactively clarify with the user which model tier they prefer for newly created agents.
- **Default Fallback Rule**: If the user does not specify a model:
  - Automatically select the most optimal model based on the user's Antigravity subscription tier.
  - For **Antigravity Pro** subscribers:
    - **Gemini 3.8 Flash**: Default for high-frequency execution agents (UI builders, E2E testers, task workers, scrapers) to optimize latency, throughput, and rate limits.
    - **Gemini Pro**: Reserved specifically for heavy reasoning agents (Tech Leads, Architects, Static Code Quality Auditors, Meta-Planners).
