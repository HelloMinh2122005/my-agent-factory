# Project Learnings & Anti-Patterns (Continuous Evolution Log)

## [2026-10-05] Cross-Workspace Plugin Generation & Java AI Backend Setup
- **Context**: Generating the Occupify backend plugin from within `my-agent-factory` targeting `/home/phandinhminh/Downloads/Occupify/.agents/plugins/backend`.
- **Root Cause (Sandbox Policy)**: Antigravity IDE file inspection tools (`view_file`, `write_to_file`, `list_dir`) enforce strict sandbox boundaries to the active workspace URI (`my-agent-factory`). Attempting direct file tool calls against external paths triggers `Permission denied ... Matches default system policy`.
- **Conflict Check**: Verified non-conflicting with `human-alignment-and-research.md` and `verification.md`.
- **Mandatory Directives**:
  1. **Cross-Workspace Deployment**: When deploying plugins to external workspaces, use deterministic shell automation scripts via `run_command` (with `Cwd` set to the active workspace) or switch the active workspace in the IDE.
  2. **Model Tiering & Effort Codification**: For Gemini 3.8 Flash squads, declare `model: flash` in YAML frontmatter and embed explicit `Reasoning Effort Profile` directives (HIGH, MEDIUM, BALANCED-FAST) in each persona prompt.
  3. **No In-Memory H2 for PgVector**: When testing Spring AI or LangChain4j vector search, in-memory H2 cannot execute pgvector HNSW operations. Always mandate Testcontainers with `pgvector/pgvector:pg16`.
