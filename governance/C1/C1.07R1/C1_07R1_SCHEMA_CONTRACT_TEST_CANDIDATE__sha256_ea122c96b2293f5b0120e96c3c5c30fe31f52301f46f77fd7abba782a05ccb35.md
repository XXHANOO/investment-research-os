# C1.07R1 — Canonical Parent Invariants & Successor-Graph Integrity Repair Candidate

Generated: 2026-08-23T19:13:56Z

Status: `CANDIDATE_FOR_C1_07R1_INDEPENDENT_REGRESSION_RECHECK`

Production implementation: `NOT AUTHORIZED`

## Exact parent

The executable parent is the exact C1.06R5 integrated machine schema:

```text
C1_06R5_MACHINE_SCHEMA_CANDIDATE__sha256_027878d3eaf9f52806d9667847c1ba196cd53f1a21ea12cbf2fd0dbb12fc15b9.json
SHA-256 027878d3eaf9f52806d9667847c1ba196cd53f1a21ea12cbf2fd0dbb12fc15b9
```

The governing red-team audit is:

```text
C1_07_INDEPENDENT_RED_TEAM_AUDIT_REPORT.md
SHA-256 af7d0783aa931984b8408fc1546d69dcec83574cb9fb7a6dd6ef55031663dd25
```

## C1RT-B01 — successor-graph distinct endpoints

R1 materializes an explicit C1 semantic validator:

`C1.SEM.SUCCESSOR_DISTINCT_ENDPOINTS`

For `PREDECESSOR_OF` / `ADD_SUCCESSOR_RELATION`:

```text
target canonical ref != related_target canonical ref
```

A self-loop returns:

`PREDECESSOR_SUCCESSOR_SELF_LOOP_FORBIDDEN`

This is a semantic comparison because JSON Schema cannot compare arbitrary sibling canonical-ref values.

## C1RT-B02 — Contract parent DERIVATIVE_PRODUCT

R1 materializes:

`C1.SEM.CONTRACT_PARENT_DERIVATIVE_PRODUCT`

Validation requires:

```text
ContractRecord.parent_instrument_ref == parent InstrumentRecord.ref
AND
parent InstrumentRecord.instrument_kind == DERIVATIVE_PRODUCT
```

Reference mismatch returns `CONTRACT_PARENT_INSTRUMENT_REFERENCE_MISMATCH`.

Non-derivative parent kind returns `CONTRACT_PARENT_INSTRUMENT_KIND_MISMATCH`.

This stays inside C1 identity semantics and does not import C11 persistence.

## C1RT-B03 — canonical parent immutability

R1 materializes:

- `C1.SEM.CONTRACT_PARENT_IMMUTABLE`
- `C1.SEM.LISTING_PARENT_IMMUTABLE`
- `C1.SEM.CANONICAL_REPLACEMENT_PACKAGE`

For the same stable canonical ID, the Instrument parent cannot change.

A genuine replacement uses distinct old/new canonical IDs plus:
- `TERMINATE_IDENTITY` on old;
- `CREATE_IDENTITY` on new;
- `PREDECESSOR_OF` old -> new.

## Carried hardening

R1 also materializes the two previously non-blocking C1.07 hardenings without changing ownership boundaries:

- CURRENT `PIT_SAFE` is not historical evidence absent C4 reconstruction equivalence.
- duplicate active ContractVenueAdmission endpoint tuples are invalid within the active set supplied by C4; C11 persistence remains external.

## Regression

Exact R5 schema vectors remain 112/112 passing during construction.

C1-338..C1-545 acceptance rows are preserved exactly.

New obligations are C1-546..C1-570 and are 25/25 decision-mapped.

Inherited authority covers C1-001..C1-545 gaplessly.

## Gate

The three C1.07 blockers are **addressed, not closed** by construction.

`C1.OPEN-010` remains CLOSED.

C1 remains not freeze-eligible until an independent C1.07R1 regression re-check passes.

Next exact gate:

`C1.07R1 Independent Regression Re-Check`
