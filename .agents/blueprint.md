# Architectural Blueprint: Occupify Frontend UI Support & Anti-Slop Dev (`react-ui-refiner`)

- **Target Workspace**: `/home/phandinhminh/Downloads/Occupify`
- **Plugin Directory**: `/home/phandinhminh/Downloads/Occupify/.agents/plugins/frontend`
- **Architecture Complexity Score (ACS)**: 4/10 (Specialist Agent Addition with Anti-Slop Filter Directives)
- **Approved by User**: Option A Gate Approved (`react-ui-refiner` on Gemini 3.8 Flash)
- **Model Selection**: Gemini 3.8 Flash (`model: flash`)

---

## 1. Executive Summary & Prior Art Synthesis

The addition of **`react-ui-refiner`** to the Occupify frontend multi-agent squad resolves visual regressions, layout defects, and AI-generated design slop. It draws directly from the open-source **[Anti-Slop](https://github.com/miqdadbadjuber/anti-slop)** framework (`miqdadbadjuber/anti-slop`).

### Foundational Prior Art
- **Anti-Slop AI UI Filter (R-01 to R-38)**: Enforces strict aesthetic discipline without prescribing rigid style guides. Stops generic landing-page and dashboard templates, invented metrics/deltas (`12,483`, `+12% this week`), fabricated filler data (`John Doe`, fake testimonials), and ungrounded decorative charts.
- **Motion & Visual Restraint**: Ban perpetual pulsing loops, endless bouncing badges, and excessive glassmorphism (`backdrop-blur`). Enforces user-triggered, purposeful micro-interactions and `prefers-reduced-motion` compliance.
- **Actionable States Over Bare Placeholders (R-27)**: Ban generic "No data" screens and bare spinners. Mandates cause-and-action empty states, geometrically matching loading skeletons, and recoverable error boundaries.
- **Collaborative Squad Specialization**:
  - `react-ui-dev`: Primitives & compound component authoring (greenfield development).
  - `react-ui-refiner`: UI support, de-slopping, layout repair, and surgical bug-fixing (remediation & polish).
  - `react-tech-lead`: Orchestrator and task delegator.
  - `react-e2e-tester`: Dynamic test execution and visual breakage detection.
  - `react-static-auditor`: Static code hygiene and zero deprecations.

---

## 2. Squad Composition & Subscription-Aware Model Tiering

| Agent Name | Role & Responsibility | Model Tier | Tools Granted |
| :--- | :--- | :--- | :--- |
| **`react-tech-lead`** | Frontend Architect & Squad Orchestrator. Decomposes tasks into Core, UI, and Remediation streams. | `pro` | `view_file`, `write_to_file`, `replace_file_content`, `multi_replace_file_content`, `run_command`, `grep_search`, `list_dir` |
| **`react-core-dev`** | Core Data & State Specialist. Pure TypeScript types, Zod schemas, TanStack Query hooks, Zustand stores. | `pro` | `view_file`, `write_to_file`, `replace_file_content`, `multi_replace_file_content`, `grep_search`, `list_dir` |
| **`react-ui-dev`** | Design System & Component Presentation Specialist. Primitives, compound components, semantic Tailwind tokens. | `flash` | `view_file`, `write_to_file`, `replace_file_content`, `multi_replace_file_content`, `grep_search`, `list_dir` |
| **`react-ui-refiner`** *(New)* | UI Support, Bug-Fixing & Anti-Slop Specialist. Audits layout bugs, cleanses AI slop/fake metrics, polishes interaction states, fixes responsive overflow. | `flash` | `view_file`, `write_to_file`, `replace_file_content`, `multi_replace_file_content`, `grep_search`, `list_dir` |
| **`react-e2e-tester`** | Dynamic QA & Accessibility Tester. Vitest, Playwright, browser interaction validation, keyboard a11y. | `flash` | `browser_subagent`, `run_command`, `view_file`, `write_to_file`, `replace_file_content`, `list_dir` |
| **`react-static-auditor`** | Independent Code Quality & Antipattern Auditor. Read-only inspection of types, tokens, and zero-deprecation policies. | `pro` | `view_file`, `grep_search`, `run_command`, `list_dir` |

---

## 3. Directory Layout & Artifacts

```text
/home/phandinhminh/Downloads/Occupify/.agents/plugins/frontend/
├── plugin.json
├── agents/
│   ├── react-tech-lead.md       # Orchestrates core, UI, and remediation
│   ├── react-core-dev.md        # Headless data & state
│   ├── react-ui-dev.md          # Component authoring & primitives
│   ├── react-ui-refiner.md      # UI bug remediation & anti-slop enforcement
│   ├── react-e2e-tester.md      # Dynamic browser tests
│   └── react-static-auditor.md  # Static quality auditor
├── skills/
│   ├── react/                   # React 19 / Tailwind v4 patterns
│   ├── deprecation-audit/       # Zero-deprecation scanner
│   ├── antislop/                # Core filter, usage modes, dials, Delivery Gate
│   ├── antislop-ui/             # UI tells, whys, and fixes
│   ├── antislop-layoutmobile/   # Viewport reflow & touch targets
│   ├── antislop-human/          # A11y, focus rings, contrast-check.py
│   ├── antislop-copywriting/    # Honest copy & anti-buzzword filter
│   └── antislop-code/           # Clean code comments
└── rules/
    ├── antislop.md              # Global antislop activation hook
    ├── antislop-reference.md    # Canonical 38-rule reference manual (R-01..R-38)
    └── ui-remediation.md        # Surgical editing, tokens, and layout resilience
```
