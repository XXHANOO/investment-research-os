# C1.07 — Independent C1 Red-Team Audit Report

Generated: 2026-08-23T19:04:28Z

## Final Verdict

```text
C1.07 — Independent C1 Red-Team Audit:
FAIL_WITH_THREE_LOAD_BEARING_BLOCKERS

Selected R5 targets:
8 / 8 PASS

C1.07 handoff package manifest:
32 / 32 PASS

Exact R4 parent bindings:
6 / 6 PASS

JSON Schema Draft 2020-12:
PASS

Declared R5 schema vectors:
112 / 112 PASS

Inherited regression authority:
C1-001..C1-534
534 / 534
0 gaps
0 overlaps

R5 additions:
C1-535..C1-545
11 contiguous
11 / 11 mapped

C1RT-B01 OPEN
C1RT-B02 OPEN
C1RT-B03 OPEN

C1.06 historical local gate:
PASS — unchanged

C1.OPEN-010:
CLOSED — not reopened

C1 overall freeze eligibility:
NO

C1.08 / downstream:
NOT AUTHORIZED

Production implementation:
NOT AUTHORIZED

NEXT EXACT STAGE:
C1.07R1 — Canonical Parent Invariants & Successor-Graph Integrity Repair
```

This was a read-only whole-C1 audit. No selected R5 artifact or passed parent artifact was edited.

---

## 1. Authority reconstruction

The selected C1.06R5 target set is internally intact and exactly matches Candidate Selection.

The C1.07 handoff package manifest verifies all bundled files. The six exact R4 parent artifacts pinned by R5 also rehash correctly.

The R5 schema passes JSON Schema Draft 2020-12 meta-validation, and all 112 declared schema vectors independently execute to their declared outcomes.

The inherited authority manifest reconstructs C1-001..C1-534 gaplessly and without overlap. C1-535..C1-545 are contiguous and decision-mapped.

Important limitation: the earliest passed parent acceptance artifacts are represented in the R5 authority chain as exact external content-addressed dependencies. This audit does not falsely claim that every early parent byte stream was freshly rehashed from the local C1.07 ZIP.

Integrity therefore passes. The failure below is semantic integration failure found only by whole-C1 cross-stage red-team attacks.

---

## 2. What survived the whole-C1 audit

The audit did not find a regression in the recently repaired C1.06 surfaces.

Independent current-schema smoke attacks remain fail-closed for:
- discriminator/payload mismatch;
- uncertified exact-resolution eligibility;
- provider `SUCCESS + NO_DATA + observations` inconsistency;
- registered-identifier target-family mismatch;
- CURRENT_ONLY expected-target mismatch;
- TEMPORAL expected-target mismatch.

The previous C1SCHEMA-B01..B07 repairs therefore remain closed.

The C1.04 temporal split remains coherent:
- C4 owns time/revision/effectivity;
- CURRENT anchors do not become `available_from`;
- a CURRENT anchor is not by itself historical PIT evidence;
- historical consumers require HISTORICAL reconstruction unless C4 proves equivalence.

The C1.05 provider boundary also remains fail-closed in the current declared schema suite.

---

# 3. C1RT-B01 — Predecessor/successor self-loop invariant dropped

Inherited C1 acceptance contains the graph-integrity rule:

```text
predecessor/successor relation
must not create a self-loop
unless the relation type explicitly permits one
```

The final integrated R5 `SuccessorEffect` enforces:
- same endpoint kind;
- fixed PREDECESSOR/SUCCESSOR roles;
- fixed `PREDECESSOR_OF`;
- fixed direction.

It does **not** require the two canonical refs to be different.

Independent attack:

```text
target:
  ENTITY A

related_target:
  ENTITY A

effect_type:
  ADD_SUCCESSOR_RELATION

relation_type:
  PREDECESSOR_OF
```

Results:

```text
SuccessorEffect:
SCHEMA VALID

IdentityEffectAssertion:
SCHEMA VALID

explicit self-loop semantic validator/vector in R5:
NOT FOUND
```

The distinct-endpoint control also validates, so this is not a malformed-fixture artifact.

### Impact

A canonical object can become its own predecessor/successor while satisfying the integrated C1 contract. That breaks identity-graph acyclicity/integrity assumptions and contradicts inherited C1-028.

### Required repair

```text
ADD_SUCCESSOR_RELATION / PREDECESSOR_OF
→ target canonical ref != related_target canonical ref
```

If JSON Schema cannot compare the two refs, R1 must add an explicit named semantic validator contract and executable negative self-loop vector.

```text
C1RT-B01:
OPEN
```

---

# 4. C1RT-B02 — Contract parent kind is not bound to DERIVATIVE_PRODUCT

Passed C1.01R1 requires:

```text
ContractID
→ exactly one parent InstrumentID
→ parent Instrument kind = DERIVATIVE_PRODUCT
```

The integrated R5 `ContractRecord` only validates that `parent_instrument_ref` is syntactically an `InstrumentRef`.

Independent attack:

```text
Instrument A:
  instrument_kind = EQUITY_SHARE_CLASS
  schema = VALID

Contract C:
  parent_instrument_ref = Instrument A
  schema = VALID
```

A DERIVATIVE_PRODUCT control is also valid, which shows the issue is not that valid parents are rejected; the issue is that non-derivative parents are not rejected.

Search of the R5 semantic-vector surface found no explicit Contract-parent-kind validator that resolves the parent reference and requires `DERIVATIVE_PRODUCT`.

### Impact

The integrated contract can serialize a Contract under:
- EQUITY_SHARE_CLASS;
- FUND_SHARE_CLASS;
- DEBT_SECURITY;
- DEPOSITARY_RECEIPT;
- INDEX_REFERENCE;

despite the passed C1.01R1 identity model.

This is a canonical-parent violation, not a C11 storage concern.

### Required repair

Add a cross-record C1 semantic rule:

```text
ContractRecord.parent_instrument_ref
→ resolve exact InstrumentRecord
→ instrument_kind MUST equal DERIVATIVE_PRODUCT
```

Add one valid derivative-parent vector and negative vectors for every supported non-derivative Instrument kind.

```text
C1RT-B02:
OPEN
```

---

# 5. C1RT-B03 — Listing/Contract parent reassignment guard is not materialized

Passed C1.01R1 also requires:

```text
same ContractID
→ cannot change parent InstrumentID

same ListingID
→ cannot change parent InstrumentID
```

A genuine replacement must use explicit termination/create/successor semantics rather than rewriting the canonical object's parent.

The R5 error vocabulary contains:

```text
CONTRACT_INSTRUMENT_REPARENT_FORBIDDEN
LISTING_REPARENT_FORBIDDEN
```

but the audit found no executable semantic contract/vector that enforces those errors across versions.

Independent two-snapshot attack:

```text
Snapshot 1:
Contract C → Instrument A
VALID

Snapshot 2:
same Contract C → Instrument B
VALID
```

and independently:

```text
Snapshot 1:
Listing L → Instrument A
VALID

Snapshot 2:
same Listing L → Instrument B
VALID
```

All four records are individually schema-valid. No R5 semantic vector contains a reparenting validator.

### Impact

An implementation conforming only to the integrated R5 machine/semantic contract could silently mutate canonical lineage and still claim C1 conformance.

The presence of an error-code enum is not equivalent to an invariant.

### Required repair

Add cross-version semantic validators:

```text
same ContractID:
parent_instrument_ref immutable

same ListingID:
instrument_ref immutable
```

If a true replacement occurs:

```text
terminate old canonical object
+ create/reference new canonical object
+ explicit successor/replacement semantics
```

Add negative two-snapshot tests for both Listing and Contract.

```text
C1RT-B03:
OPEN
```

---

## 6. Non-blocking hardenings

### C1RT-H01 — CURRENT `PIT_SAFE` wording

The integrated schema can represent a CURRENT result as `PIT_SAFE` when its load-bearing temporal dependencies are PIT-safe. That is compatible with the passed weakest-dependency rule.

Before C1 freeze, wording should make the distinction unmistakable:

```text
CURRENT result reconstructability=PIT_SAFE
!=
CURRENT anchor is historical PIT evidence
```

The already-passed requirement remains:

```text
historical reuse
→ HISTORICAL reconstruction
or explicit C4 proof of reconstruction equivalence
```

This is not a blocker.

### C1RT-H02 — ContractVenueAdmission temporal uniqueness

The earlier C1.01R1 independent review already classified active-state admission uniqueness/idempotency formalization as hardening.

Before final freeze, C1 should make duplicate active Contract→Listing admission semantics executable at a C4-defined state while leaving:
- temporal computation to C4;
- persistence/idempotent coalescing to C11.

This audit does not promote that prior hardening to a blocker.

---

## 7. Governance decision

The C1.06R5 independent re-check remains historically valid for the local C1.06 gate it reviewed.

C1.07 is deliberately broader. It found three inherited identity invariants that were content-addressed in the parent acceptance chain but were not fully materialized in the final integrated schema/semantic test surface.

Therefore:

```text
C1.06:
HISTORICAL LOCAL PASS — NOT REVOKED

C1.OPEN-010:
CLOSED — NOT REOPENED

C1.07:
FAIL_WITH_THREE_LOAD_BEARING_BLOCKERS

C1 overall:
NOT FREEZE-ELIGIBLE

C1.08:
NOT AUTHORIZED

PRODUCTION IMPLEMENTATION:
NOT AUTHORIZED
```

Only the following next stage is authorized:

```text
C1.07R1 — Canonical Parent Invariants & Successor-Graph Integrity Repair
```

R1 must repair the final integrated C1 schema/semantic-test materialization only. It must not redesign or reopen the passed C1.01R1–C1.05R1 parent contracts.

After R1 construction, stop at:

```text
C1.07R1 Independent Regression Re-Check
```
