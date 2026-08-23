# Investment Research OS — Governance Archive

This repository is the version-controlled governance archive for the Investment Research OS project.

## Governance model

- `C0` is frozen.
- C1 work is developed through gated candidate construction, independent review, narrow repair, and regression re-check stages.
- Production implementation remains prohibited unless a later explicit governance gate authorizes it.
- Content-addressed SHA-256 identities are preserved in filenames/manifests where available.

## Repository layout

- `governance/C0/` — canonical Frozen C0 and freeze seal.
- `archive/` — exact project files physically available in the active project runtime, preserving their source-relative paths.
- `manifests/` — archive hashes and externally referenced content-addressed dependencies that are not physically available in the active runtime.

## Current gate

At repository bootstrap, C1.06R3 independent regression re-check failed with three load-bearing blockers. The exact next stage is C1.06R4 — Integrated Mapping Governance & Executable-Test Repair.

This repository is governance/archive infrastructure only; it is not production implementation authorization.
