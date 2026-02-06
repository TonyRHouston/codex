# Workspace Asset Index

Purpose
- Fast map of where key asset classes live in this repository.
- Codex should consult this index at session start and before broad filesystem scans.

## 1) Product Code
- `codex-rs/`: Primary Rust implementation (core, tui, protocol, app-server).
- `codex-cli/`: CLI/package-facing project assets.
- `sdk/`: SDK-related code/assets.
- `shell-tool-mcp/`: shell MCP server code.
- `thinkpdf/`: ThinkPDF project code and tooling.
- `third_party/`: vendored/external dependencies.

## 2) Build, Tooling, and Config
- `justfile`: workspace task runner entrypoint.
- `MODULE.bazel`, `BUILD.bazel`, `defs.bzl`, `rbe.bzl`: Bazel configuration.
- `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`: JS workspace config.
- `.github/`: CI/workflow definitions.
- `.githooks/`: repository git hooks.

## 3) Documentation and Notes
- `README.md`, `CHANGELOG.md`: top-level project docs.
- `docs/`: maintained product and engineering documentation.
- `reading-list/`: local reading/reference notes.

## 4) Codex Runtime/Automation (Repository-Scoped)
- `.codex/hooks/`: Codex runtime hooks.
- `.codex/scripts/`: codex automation scripts.
- `.codex/skill_index/`: generated skill registries and audits.
- `.codex/skills/`: local skill catalog (`SKILL.md` definitions).
- `.codex/memories/`: persistent local context snapshots.
- `.codex/workspace_index/`: this index and structured manifests.

## 5) Linked Source Trees (Symlinked)
- `partially-processed -> /home/web3tony/sys/sys/skills/partially-processed`
- `.curated -> /home/web3tony/sys/sys/skills/partially-processed/.curated`
- `tools -> /home/web3tony/sys/sys/skills/partially-processed/tools`
- `skills -> /home/web3tony/sys/sys/skills/partially-processed/skills`
- `claude-code -> /home/web3tony/sys/sys/skills/partially-processed/claude-code`

## 6) Local/Transient Artifacts (Do Not Treat as Canonical Source)
- `.local/`, `.triage-artifacts/`, `out/`, `node_modules/`
- `.codex/History/`, `.codex/logs/`, `.codex/sessions/`, browser/cache-style files in `.codex/`

## 7) Operational Guidance For Codex
1. Read this file first at session start.
2. Prefer paths in sections 1-4 for code and configuration changes.
3. Avoid broad scans across section 6 unless explicitly needed for diagnostics.
4. Treat section 5 symlinks as external source mirrors; do not reorganize without user request.
