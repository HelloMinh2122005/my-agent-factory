# Open-Source Prior Art & Multi-Agent Architectural Foundations

This reference synthesizes the state of the art in open-source multi-agent engineering. Agents in the Agent Factory must consult and build upon these battle-tested foundations rather than reinventing ad-hoc patterns.

---

## 1. MetaGPT: Standard Operating Procedures (SOPs)

### Core Philosophy: "Code = SOP(Team)"
MetaGPT (Hong et al., ICLR 2024) models complex software engineering as an assembly line of specialized agents coordinated by human-like Standard Operating Procedures.

### Key Takeaways for Antigravity Agent Design:
1. **Strict Intermediate Artifacts**:
   - Never pass vague conversational context between agents.
   - Require structured contracts: The output of Agent A (e.g. PRD with Gherkin criteria) must serve as the exact input specification for Agent B (e.g. Architecture decomposition).
2. **Role Specialization over Monoliths**:
   - Rather than asking a single generalist model to write requirements, architecture, code, and tests, decompose the work into specialized personas (PM $\rightarrow$ Architect $\rightarrow$ Engineer $\rightarrow$ QA).
3. **Structured Communication Protocols**:
   - SOPs act as guardrails that prevent cascading hallucinations by keeping each agent strictly within its professional domain.

---

## 2. Anthropic: Building Effective Agents

### Core Philosophy: Simple, Composable Patterns
Anthropic's research emphasizes that the most robust agentic systems use simple, transparent building blocks rather than opaque, overly complex frameworks.

### The 5 Architectural Patterns:

```text
1. ROUTER:
   Incoming Request ──> [Router / Classifier] ──> Specialized Handler A | B | C

2. ORCHESTRATOR-SUBAGENT (Workers):
   Task ──> [Lead Orchestrator] ──┬──> [Worker 1 (Data)]
                                  ├──> [Worker 2 (UI)]
                                  └──> [Worker 3 (Test)]
                                  └──> Synthesis / Aggregation

3. PROMPT CHAINING:
   Step 1 Output ──> Step 2 Input ──> Step 3 Input ──> Final Deliverable

4. PARALLELIZATION (Fan-Out / Fan-In):
   Task ──┬──> Subtask A (Core) ──┐
          └──> Subtask B (Visual) ┴──> Merged Output

5. EVALUATOR-OPTIMIZER (Iterative Refinement):
   [Generator] ──> Draft ──> [Evaluator / Judge] ──> Feedback ──> Loop until PASS
```

### Key Rules from Anthropic:
- **Workflows vs Agents**: Use deterministic workflows (code-directed) for predictable sequential pipelines; use autonomous agents (LLM-directed tool use) only when dynamic decision-making is necessary.
- **Start Simple**: Always benchmark a single well-prompted model call before adding multi-agent complexity. Only introduce subagents when demonstrable benefits emerge.

---

## 3. ROMA & LangGraph: Recursive Decomposition & Stateful Graphs

### ROMA (Recursive Open Meta-Agent)
- Demonstrates hierarchical, tree-based decomposition: a parent meta-agent breaks a broad objective into sub-goals, delegates them to leaf executors, and aggregates the results.
- Essential for long-horizon tasks that exceed the context capacity of a single execution turn.

### LangGraph & State Machines
- Treats multi-agent workflows as stateful cyclic graphs.
- **Human-in-the-Loop Checkpoints**: Formalizes gates where execution pauses and requests human validation before state transitions occur (directly inspiring our **Option A Co-Pilot Gate**).

---

## 4. DSPy & LLM-as-a-Judge: Trajectory Evaluation

### The 4-Part Evaluation Rubric:
When auditing agents, avoid subjective, binary assessments ("good" or "bad"). Implement a rigorous 4-part evaluation rubric:
1. **Criterion Definition**: Define the exact metric (e.g. "Schema Validity", "Tool Least-Privilege", "Link Integrity").
2. **Explicit Reasoning Structure**: Require Chain-of-Thought analysis before scoring.
3. **Deterministic Scoring Rule**: Map findings directly to scores (e.g. 1 broken link = automatic FAIL).
4. **Edge Case Clause**: Explicitly handle corner cases (e.g. empty tool output, missing documentation).

### Trajectory Evaluation:
Grade the complete trajectory of the agent:
- Did it choose the right tool?
- Did it respect directory boundaries?
- Did it hallucinate non-existent files?
- Is the output deterministic and consumable downstream?
