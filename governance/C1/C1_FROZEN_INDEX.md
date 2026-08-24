# C1 Frozen Authority Index

Status: **DERIVED NAVIGATION INDEX — NON-AUTHORITATIVE**

This file exists only to make the frozen C1 authority easy to locate in the repository.
It is **not** a new C1 freeze artifact, is **not** part of the original C1 freeze seal,
and MUST NOT be treated as a second root of trust or as a replacement for the exact
content-addressed C1 freeze bundle.

## Frozen C1 state

C1 is frozen by the independently passed C1.08R1 freeze-review chain.

Authoritative final freeze record:

`governance/C1/C1.08R1/C1_FINAL_FREEZE_RECORD.md`

Authoritative C1 freeze seal:

`governance/C1/C1.08R1/C1_FREEZE_SEAL__sha256_438274542570f7398af8622fdb511b85d69fc4c403b246b93a8a593b5d8070a5.yaml`

Freeze Seal SHA-256:

`438274542570f7398af8622fdb511b85d69fc4c403b246b93a8a593b5d8070a5`

Frozen candidate selected by that seal:

`governance/C1/C1.08/C1_08_FREEZE_CANDIDATE__sha256_e9f7446fad39a3fbe4c204129a95e9255353addeb7893e76465c93f9c7be4db9.md`

Freeze-candidate SHA-256:

`e9f7446fad39a3fbe4c204129a95e9255353addeb7893e76465c93f9c7be4db9`

Approval-ready freeze manifest:

`governance/C1/C1.08/C1_08_APPROVAL_READY_FREEZE_MANIFEST__sha256_74a169c75d52125edfe6f5a9d125186530bac332ba66a942db44ec779242faf7.yaml`

Acceptance authority:

`governance/C1/C1.08/C1_08_FREEZE_ACCEPTANCE_AUTHORITY__sha256_82991dbf5da9c1ef200ff8c801067edd128dfd0733c69c9f99e615ee5f39907c.yaml`

Final machine schema pinned by the freeze seal:

`C1_07R2_MACHINE_SCHEMA_CANDIDATE__sha256_927f1916d3b4b0c0600c1988d6cff0c91dfaaf840b676ce8b6f6f86cb61e52d4.json`

Final machine-schema SHA-256:

`927f1916d3b4b0c0600c1988d6cff0c91dfaaf840b676ce8b6f6f86cb61e52d4`

## Why there is no authoritative `C1_FROZEN.md`

C1 was frozen as a content-addressed multi-artifact bundle rather than by rewriting the
entire accepted C1 surface into a new monolithic `C1_FROZEN.md`. The C1 freeze seal pins
the exact accepted candidate, manifest, machine schema, acceptance authority, and recheck
evidence. Creating a new post-freeze monolithic document and treating it as authoritative
would create an unsealed competing authority surface.

Therefore this index is intentionally navigation-only.

## Authority rule

If this index ever conflicts with the content-addressed artifacts above, this index loses.
The freeze seal and the artifacts it pins remain authoritative.

Production implementation remains **NOT AUTHORIZED** by this index.
