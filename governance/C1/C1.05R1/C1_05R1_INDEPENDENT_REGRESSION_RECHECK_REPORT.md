# C1.05R1 — Independent Regression Re-Check Report

Generated: 2026-08-19T13:02:47Z

Verdict: `PASS_CANDIDATE_FOR_C1_06`

## 1. Scope and Review Discipline

This is a read-only independent regression re-check of the exact content-addressed C1.05R1 repair targets.

The C1.05 stage report was treated as context only, not proof. Exact target hashes were recomputed from bytes. The failed C1.05 base artifacts were compared directly against the R1 artifacts. No implementation code was created or authorized.

Review objective:

```text
C1PN-B01 — floating C2 semantic dependency / determinism defect
C1PN-B02 — replay-lineage normative-strength defect
```

Gate rule:

```text
PASS → close C1PN-B01 and C1PN-B02
     → authorize C1.06 Schema & Contract-Test Candidate Design
     → implementation remains NOT AUTHORIZED
```

## 2. Exact Target Integrity

All six C1.05R1 independent-review targets recomputed to their selected SHA-256 values:

```text
candidate        71d472e63044b9a7be2c6cc831705ed80dc6a06ccd0ef03e71a0618794bdef63
registry         422010036a00ad0d1fbfa4176ae27f107fec4761a92c0f0ad5b7db29eed2379b
ledger           47315933c5369aa1aa3a9719874dee31348335efa1a2120677747ab7c9a47031
acceptance       bbf23c97dbab72844956fd6a751c63ba13eba2857fcf4bb62faa875709bc5b83
repair diffs     036fa6f62630b6c1e60eef7171eae5c5db8b0700064557d6d069a7b4f0056810
selection        b6c97bef49e6a0f21000167097f6eae202014051ae0fd760e22afaeb4deb2482
```

Result:

```text
6 / 6 exact target hashes PASS
```

Direct local parent rehashes also PASS for Frozen C0, the C0 freeze seal, the exact C1.04R1 temporal/PIT candidate, and the C1.04R1 independent re-check report.

Older C1.01R1/C1.02R1/C1.03R1 parents are not falsely represented as newly byte-rehashed from this R1 package. Their exact content-addressed hashes remain pinned through the previously verified parent chain.

## 3. C1PN-B01 Independent Re-Check

### Required stable dependencies

PASS.

The R1 contract now requires any load-bearing C2-owned semantic, capability, or completeness reference affecting normalization meaning, exactness, absence/uniqueness, or replay to resolve to an immutable/version-addressed/content-addressed or equivalent snapshot-stable C2 semantic state.

The explicit minimum load-bearing set includes:

```text
provider_profile_ref
provider_field_semantic_refs[]
provider_capability_ref
c2_completeness_refs[]
```

### Floating/latest references

PASS.

A floating `latest`, mutable provider-profile handle, or mutable coverage/capability reference cannot satisfy deterministic/audit-safe materialization. A floating completeness reference also cannot support exact `NO_MATCH` or uniqueness when the conclusion depends on that mutable state.

### Stable positive path

PASS.

The contract does not overcorrect by requiring one specific foreign-ID mechanism. C2 may use a version, immutable snapshot ID, content address, or equivalent mechanism, provided replay resolves the same semantic state.

### Ownership

PASS.

C1 owns only the referential-stability requirement. C2 continues to own its record schema, capability taxonomy, routing, certification algorithm, and completeness methodology.

### Blocker decision

```text
C1PN-B01: CLOSED
```

## 4. C1PN-B02 Independent Re-Check

### Normative strength

PASS.

Replay-critical lineage is now `MUST`, not `SHOULD`.

### Required lineage

PASS.

Every replay-safe materialized normalized candidate/result must retain enough immutable or snapshot-stable lineage to identify:

```text
validated input or immutable validated-input ref
source_record_ref / source_group_ref
exact normalization_profile_ref
exact parent C1 contract refs
provider_operation_ref
load-bearing provider semantic/capability refs
load-bearing c2_completeness_refs[]
load-bearing C4 temporal refs
load-bearing C5 evidence/provenance refs
item/batch outcome context needed to explain partiality
degradation/fallback refs when materially relevant
```

Missing replay-critical lineage makes the result ineligible for replay-safe materialization.

### Partial materialization

PASS.

Partial normalization cannot discard the item/batch outcome context needed to explain which inputs succeeded, failed, or remained partial.

### Degradation/fallback provenance

PASS.

A materially degraded/fallback/stale/last-known-good path must preserve the applicable opaque degradation/fallback provenance and cannot be materialized as clean primary-source provenance.

### Ownership

PASS.

The R1 contract does not prescribe internal C2/C4/C5 schema or storage layout.

### Blocker decision

```text
C1PN-B02: CLOSED
```

## 5. Regression Preservation

Programmatic comparison against the exact failed C1.05 base shows:

```text
C1-257..C1-330 legacy rows       74 / 74 byte-for-byte row-equivalent
new acceptance IDs               C1-331..C1-337 only

C1.DEC-107..C1.DEC-138           32 / 32 structured blocks unchanged
new decision IDs                 C1.DEC-139..C1.DEC-141 only

combined acceptance range        C1-257..C1-337
acceptance obligations           81
mapped                           81 / 81
unmapped                         0
duplicate decision IDs           0
```

The new decision/test mapping is narrow:

```text
C1.DEC-139 → C1-331, C1-332, C1-333
C1.DEC-140 → C1-334, C1-335, C1-336
C1.DEC-141 → C1-337
```

No unrelated legacy acceptance row or legacy decision block was changed.

## 6. Regression Attack Surface

The re-check actively attacked previously passing C1.05 semantics. No regression was found in the following load-bearing areas:

```text
raw provider payload cannot become canonical truth
provider-native ID/symbol cannot become internal canonical ID
C2 routing/auth/retry/certification remains external
C1.02 scheme/context/grouping exactness remains intact
C1.01 Listing/Instrument/ContractVenueAdmission identity model remains intact
C1.03 event-classification != identity-effect semantics remain intact
PROJECTED effects cannot activate canonical identity
C1.04 T knowledge cutoff / S state-point separation remains intact
available_from remains C4 visibility authority
provider failure != NO_DATA
NO_DATA/PARTIAL/search emptiness cannot prove absence by convenience
absence-based exactness requires matching completeness evidence when load-bearing
completeness cannot override C4 PIT constraints
provider confidence/ranking cannot become C5 verification
ambiguity remains distinct from conflict
batch/item failures remain explicit
unknown provider fields cannot silently pollute canonical schema
downstream canonical-domain logic consumes normalized C1 types, not raw provider objects
```

## 7. Active Search for New Blockers

The reviewer specifically tested whether the repair itself introduced new authority or determinism defects.

Examined and rejected as blockers:

1. `provider_operation_ref` is replay lineage but is not promoted into C1-owned provider semantics; stable validated input/source plus pinned load-bearing semantic state remains the semantic replay basis.
2. C1 does not mandate a particular C2 snapshot-ID encoding, so referential stability does not become a C2 schema takeover.
3. Positive exact mapping remains possible without universe-wide enumeration when exactness does not rely on absence; completeness is load-bearing only when absence/uniqueness depends on missing alternatives.
4. `materially relevant` degradation provenance does not authorize silent omission when fallback/stale/LKG changes source/provenance semantics; C1-337 explicitly guards this boundary.
5. New typed error families do not freeze wire serialization; exact error/result serialization remains C1.06-owned.
6. Legacy C1-312 remains compatible with the repair because floating load-bearing semantic references are now ineligible; eligible replay inputs resolve pinned foreign semantic states.

New load-bearing blockers found:

```text
NONE
```

## 8. Final Independent Decision

```text
C0 weakening:                                   NONE FOUND
C1.01R1–C1.04R1 regression:                    NONE FOUND
C1/C2 ownership collision:                      NONE FOUND
C1/C4 ownership collision:                      NONE FOUND
C1/C5 ownership collision:                      NONE FOUND

C1PN-B01:                                       CLOSED
C1PN-B02:                                       CLOSED
NEW LOAD-BEARING BLOCKERS:                      NONE

C1.05R1 Independent Regression Re-Check:        PASS_CANDIDATE_FOR_C1_06
C1.06 Schema & Contract-Test Candidate Design:  AUTHORIZED
IMPLEMENTATION:                                 NOT AUTHORIZED
```

## 9. Exact Next Stage

```text
C1.06 — Schema & Contract-Test Candidate Design
```

C1.06 may now design the typed schema/serialization and executable contract-test candidate needed to encode the already-approved C1 semantics, including closure of `C1.OPEN-010`, but it must not silently redesign C1.01R1–C1.05R1 semantics and must not begin production implementation without a separate gate.
