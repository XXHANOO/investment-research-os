# C1.06R5 — Independent Regression Re-Check Report

Generated: 2026-08-23T18:46:44Z

## Final Verdict

```text
C1.06R5 Independent Regression Re-Check:
PASS

Selected R5 targets:
8 / 8 PASS

Independent package manifest:
25 / 25 PASS

Exact R4 parent bindings:
6 / 6 PASS

JSON Schema Draft 2020-12:
PASS

All declared schema vectors:
112 / 112 PASS

Inherited R4 schema vectors:
104 / 104 PASS

R4 acceptance C1-338..C1-534:
PRESERVED

R5 additions C1-535..C1-545:
11 contiguous / 11 mapped

Inherited regression authority:
C1-001..C1-534
534 / 534
0 gaps
0 overlaps

C1SCHEMA-B01 CLOSED
C1SCHEMA-B02 CLOSED
C1SCHEMA-B03 CLOSED
C1SCHEMA-B04 CLOSED
C1SCHEMA-B05 CLOSED
C1SCHEMA-B06 CLOSED
C1SCHEMA-B07 CLOSED

New load-bearing blockers:
NONE

C1.OPEN-010:
CLOSED

C1.06 schema / contract-test gate:
PASS

NEXT AUTHORIZED STAGE:
C1.07 — Independent C1 Red-Team Audit

Production implementation:
NOT AUTHORIZED
```

This re-check was read-only with respect to the selected R5 candidate artifacts.

## 1. Integrity and regression

All eight selected R5 targets rehash to the exact hashes pinned by Candidate Selection.

The handoff package manifest verifies all entries, and the six exact R4 parent bindings in Candidate Selection independently rehash to their pinned values.

The full R5 schema passes JSON Schema Draft 2020-12 meta-validation.

All 112 declared schema vectors were independently executed and passed, including all inherited R4 vectors and the eight new direct B07 vectors.

C1-338..C1-534 are preserved from the exact R4 acceptance artifact. C1-535..C1-545 are contiguous and all eleven are decision-mapped.

Inherited regression authority reconstructs C1-001..C1-534 exactly once.

## 2. Prior blocker regression re-check

The independent adversarial suite re-attacked the load-bearing closures from B01 through B06.

Confirmed:
- discriminator/payload mismatches remain rejected;
- uncertified exact-resolution eligibility remains rejected;
- owner-specific foreign refs remain typed;
- RESOLVED/NO_MATCH cardinality remains correct;
- provider outcome/container consistency remains fail-closed;
- registered/symbol/provider target-family restrictions remain enforced.

No regression was found.

## 3. C1SCHEMA-B07 — CLOSED

R5 now enforces the result-side expected-target equality in both temporal modes.

Independent direct attacks:

```text
CURRENT_ONLY:
expected LISTING  + RESOLVED LISTING   PASS
expected LISTING  + RESOLVED CONTRACT  REJECT
expected CONTRACT + RESOLVED LISTING   REJECT
expected CONTRACT + RESOLVED CONTRACT  PASS

TEMPORAL:
expected LISTING  + RESOLVED LISTING   PASS
expected LISTING  + RESOLVED CONTRACT  REJECT
expected CONTRACT + RESOLVED LISTING   REJECT
expected CONTRACT + RESOLVED CONTRACT  PASS
```

The result-side machine rule operates on `ResolutionQueryBinding.expected_target_kind`.

The independent review also attacked the obvious cross-artifact bypass: omit `query_binding` from the result even though the source query supplied an expected target kind. That object can remain structurally valid in isolation, because the result schema cannot dereference the external source query by itself.

This does **not** remain an open blocker because R5 explicitly defines the cross-artifact authenticity rule in C1-543:

- the result binding references the exact source IdentifierResolutionQuery;
- if the source query supplied `expected_target_kind`, the binding must carry the same value;
- mismatch **or omission** is invalid.

This follows the established C1 contract pattern already used for other cross-artifact relations that JSON Schema cannot evaluate by itself: machine-enforce the local shape and state the external comparison as an explicit named semantic contract.

C1-545 also keeps SchemeDefinition target compatibility and query expected-target compatibility orthogonal. A producer must satisfy both; neither guard substitutes for the other.

```text
C1SCHEMA-B07: CLOSED
```

## 4. New adversarial search

The re-check specifically searched for:
- omitted query binding;
- forged expected kind;
- Listing/Contract cross-kind promotion;
- CURRENT_ONLY/TEMPORAL asymmetry;
- query guard replacing SchemeDefinition guard;
- regressions in B01-B06;
- acceptance/decision/authority discontinuity.

No additional load-bearing blocker was found.

## 5. C1.OPEN-010 and stage gate

The original C1 identity/mapping/schema closure question can now be closed at the C1.06 gate.

```text
C1.OPEN-010:
CLOSED

C1.06:
PASS
```

This does **not** freeze the entire C1 stage and does **not** authorize implementation. The roadmap's next independent gate is now authorized:

```text
C1.07 — Independent C1 Red-Team Audit
```

Production implementation remains:

```text
NOT AUTHORIZED
```
