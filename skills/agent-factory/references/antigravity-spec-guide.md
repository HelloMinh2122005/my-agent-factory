# Google Antigravity Customization Architecture & Specification Guide

This reference document outlines the complete architectural specifications for creating plugins, agents, skills, rules, hooks, and MCP servers in Google Antigravity.

---

## 1. Customization Roots & Discovery

Antigravity traverses specific directories to discover customizations automatically:

1. **Workspace Customization Root (Project-Specific)**:
   - Location: `.agents/` at the root of the workspace.
   - Purpose: Checked into version control (VCS) to share agents, skills, and rules across the engineering team.
2. **Global Customization Root (Machine-Local)**:
   - Location: `~/.gemini/config/`
   - Purpose: Machine-wide defaults, developer-specific tooling, and global skills.

---

## 2. Plugins Architecture (`plugins/<name>/`)

Plugins are namespaced, shareable bundles packaging skills, agents, rules, hooks, and MCP configs into a single deployable unit.

```text
plugins/<plugin_name>/
├── plugin.json       # Required: Manifest file
├── mcp_config.json   # Optional: Model Context Protocol external servers
├── hooks.json        # Optional: Lifecycle event hooks
├── rules/            # Optional: Markdown rules applied when plugin is active
│   └── *.md
├── agents/           # Optional: Subagent persona definitions
│   └── *.md
└── skills/           # Optional: Domain skills exposed by the plugin
    └── <skill_name>/
        └── SKILL.md
```

### The Manifest (`plugin.json`):
```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Concise description of the plugin's purpose.",
  "author": {
    "name": "Author Name",
    "email": "email@example.com"
  },
  "keywords": ["tag1", "tag2"]
}
```

---

## 3. Subagents Architecture (`agents/<name>.md`)

Antigravity subagents are defined as Markdown files containing valid YAML frontmatter at the very top:

```markdown
---
name: specialized-agent-name
description: Clear, high-signal description of role and triggers.
model: pro  # or 'flash'
subagent: true
tools:
  - view_file
  - write_to_file
  - replace_file_content
  - run_command
  - grep_search
  - list_dir
---

# Agent Title

System prompt, mental models, inviolable directives, and output contracts.
```

### Valid Antigravity Tools Matrix:
- **Filesystem & Code**: `view_file`, `write_to_file`, `replace_file_content`, `multi_replace_file_content`, `grep_search`, `list_dir`.
- **System & Shell**: `run_command`, `manage_task`, `schedule`.
- **Research & Web**: `search_web`, `read_url_content`.
- **Browser Automation**: `browser_subagent`.
- **Interactive UI**: `ask_question`.
- **Multimodal Assets**: `generate_image`.

---

## 4. Skills & Progressive Disclosure (`skills/<name>/`)

Skills teach agents multi-step procedures, runbooks, and deep domain knowledge.

```text
skills/<skill_name>/
├── SKILL.md          # Progressive disclosure entry point
├── config.json       # Optional: Triggers, intent mapping, policies
├── workflow.md       # Optional: Step-by-step SOP lifecycle
├── system_prompt.md  # Optional: Domain operational directives
└── references/       # Modular reference manuals loaded on demand
    └── *.md
```

### The `SKILL.md` File:
```markdown
---
name: my-skill
description: Clear description of what the skill teaches and when to activate it.
---

# Skill Title
Progressive overview, checklist, and relative links to references/.
```

> **Progressive Disclosure Principle**: Only the `name` and `description` from the YAML frontmatter are injected into the model's system prompt by default. The full content of `SKILL.md` is loaded only when the skill is explicitly activated, and files in `references/` are read only when needed.

---

## 5. Lifecycle Hooks (`hooks.json`)

Hooks allow executing automated scripts or checks at specific agent lifecycle events:

```json
{
  "hooks": {
    "post_tool_call": [
      {
        "tool": "replace_file_content",
        "command": "pnpm lint --fix",
        "description": "Automatically run linter after code modifications"
      }
    ]
  }
}
```

---

## 6. MCP Server Configurations (`mcp_config.json`)

Connects Antigravity agents to external tool providers using the Model Context Protocol (e.g. Figma, PostgreSQL, GitHub, Jira):

```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-figma"],
      "env": {
        "FIGMA_ACCESS_TOKEN": "${FIGMA_ACCESS_TOKEN}"
      }
    }
  }
}
```
