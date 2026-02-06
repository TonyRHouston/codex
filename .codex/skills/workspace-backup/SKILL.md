---
name: workspace-backup-3e96e9
description: 'Backup large workspaces to Google Drive via gcloud ADC + Drive API.
  Use when creating archives, choosing backup profiles, or uploading to Drive.

  Keywords: backup,gdrive,gcloud,archive'
---

# Workspace Backup

## When to use
- Backing up large workspaces to Google Drive
- Choosing backup profiles or troubleshooting Drive uploads

## Core workflow
1. Choose a backup profile (minimal, standard, full)
2. Authenticate with gcloud ADC using Drive scopes
3. Set quota project and enable Drive API
4. Create archive via workspace backup script
5. Upload archives with the Drive uploader
6. Record folder ID and uploaded artifacts

## Anti-patterns (NEVER)
- Upload secrets or tokens without encryption
- Skip quota project setup (causes 403 errors)
- Upload caches or build artifacts without justification

## Output expectations
- Selected profile and commands used
- Archive list and Drive folder ID
- Any warnings or exclusions

## References
- Read references/runbook.md before executing
