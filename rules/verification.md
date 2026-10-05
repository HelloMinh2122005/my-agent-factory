# Information Verification and Zero-Guess Rule

## Core Principle
Never make assumptions or answer based on speculation. Always verify all information, file locations, directory hierarchies, and schema configurations using workspace tools before answering the user or modifying files.

## Mandatory Protocols

1. **Verify Existence Before Referencing**:
   - Always inspect the filesystem using `find`, `list_dir`, or `grep_search` to verify where a file actually resides before referencing, linking, importing, or configuring it.
   - Never assume a file is located at the project root or in a specific subfolder without confirming first.

2. **Accurate Path Resolution**:
   - When constructing relative paths (e.g. in Markdown links, configs, imports), calculate the exact directory depth between the source file and the target file.
   - Never use machine-local absolute paths (e.g. `file:///path/to/...`) in repository documentation, templates, or shared files. Always use dynamic repository-relative paths.

3. **Pre-Response Fact Checking**:
   - Check and verify all technical claims, schemas, and commands against the current workspace state before presenting answers or proposing edits to the user.
   - Strictly follow a zero-guess policy: if uncertain about any parameter, tool name, or API shape, inspect the relevant documentation or source code first.
