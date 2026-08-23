# PROJECT HANDOFF — C1.07 FAIL → C1.07R1

Generated: 2026-08-23T19:04:28Z

## Authoritative state

```text
C0 FROZEN

C1.01R1 PASS
C1.02R1 PASS
C1.03R1 PASS
C1.04R1 PASS
C1.05R1 PASS

C1.06R5 Independent Regression Re-Check:
PASS

C1.OPEN-010:
CLOSED

C1.07 Independent C1 Red-Team Audit:
FAIL_WITH_THREE_LOAD_BEARING_BLOCKERS

C1RT-B01:
OPEN — predecessor/successor self-loop invariant not materialized

C1RT-B02:
OPEN — Contract parent DERIVATIVE_PRODUCT binding not materialized

C1RT-B03:
OPEN — Listing/Contract parent reassignment guards not materialized

C1 overall freeze:
NOT ELIGIBLE

Production implementation:
NOT AUTHORIZED
```

## Exact next stage

```text
C1.07R1 — Canonical Parent Invariants & Successor-Graph Integrity Repair
```

This is a narrow construction stage.

### R1 must repair only

1. `SuccessorEffect` / `PREDECESSOR_OF` semantic distinct-endpoint rule:
   - target canonical ref != related target canonical ref;
   - add positive distinct-endpoint and negative self-loop vectors.

2. `ContractRecord` parent-kind rule:
   - `parent_instrument_ref` resolves to exact InstrumentRecord;
   - `instrument_kind == DERIVATIVE_PRODUCT`;
   - add valid derivative and negative non-derivative parent vectors.

3. Parent immutability:
   - same ContractID cannot change parent InstrumentID;
   - same ListingID cannot change parent InstrumentID;
   - genuine replacement must use terminate/create/successor semantics;
   - add two-snapshot reparent negative vectors.

4. Preserve every already-closed C1SCHEMA-B01..B07 repair.

5. Preserve C1.OPEN-010 CLOSED.

6. Preserve Frozen C0 and all passed C1.01R1–C1.05R1 semantics.

7. Do not absorb C4/C5/C11/C12 internal schemas.

8. Do not begin production implementation.

### R1 should carry forward as hardening, not blocker repair

- clarify CURRENT `PIT_SAFE` vs historical evidence;
- make active-state ContractVenueAdmission duplicate semantics explicit without importing C4/C11 internals.

### Stop condition

After content-addressed R1 construction, stop at:

```text
C1.07R1 Independent Regression Re-Check
```
