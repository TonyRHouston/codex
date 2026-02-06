---
name: unity-asset-recovery-5eacb9
description: 'Recover high-fidelity Unity assets and scenes from legacy projects.
  Use when extracting assets, rebuilding scenes, or validating Unity recovery work.

  Keywords: unity,asset-recovery,assetripper,unitypy,scene-rebuild'
---

# Unity Asset Recovery

## When to use
- Recovering Unity assets from APKs or legacy bundles
- Rebuilding scenes with correct materials, lighting, and VFX

## Core workflow
1. Discover asset bundles and streaming assets
2. Review prior artifacts to avoid duplicate work
3. Run raw extraction (AssetRipper/UnityPy)
4. Reconstruct scenes and prefabs in Unity editor
5. Validate rendering, UI, audio, and VFX
6. Document issues, fixes, and deviations

## Anti-patterns (NEVER)
- Change behavior without documenting deviations
- Discard shader variants or texture provenance
- Skip validation scenes after reconstruction

## Output expectations
- Inventory of assets and sources
- Reconstruction status by scene
- Validation results and remaining gaps

## References
- Read references/asset-recovery-plan.md and references/reconstruction-checklist.md
