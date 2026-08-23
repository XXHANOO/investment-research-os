# C1.07R2 — Independent Regression Re-Check Report

Generated: 2026-08-23T19:52:54Z

## Final Verdict

```text
C1.07R2 Independent Regression Re-Check:
PASS

Selected R2 targets:
9 / 9 PASS

Exact R1 parent bindings:
8 / 8 PASS

Governing R1 re-check bindings:
3 / 3 PASS

Independent package manifest:
27 / 27 PASS

JSON Schema Draft 2020-12:
PASS

Inherited machine vectors:
112 / 112 PASS

Executable C1.07R1 + R2 semantic vectors:
30 / 30 PASS

C1RT-B01 CLOSED
C1RT-B02 CLOSED
C1RT-B03 CLOSED
C1RT-B04 CLOSED

New load-bearing blockers:
NONE

C1.OPEN-010:
CLOSED — unchanged

C1.07:
PASS_AFTER_C1_07R2

C1 freeze-candidate eligibility:
YES

C1.08:
AUTHORIZED

Production implementation:
NOT AUTHORIZED

NEXT EXACT STAGE:
C1.08 — Freeze Candidate & Independent Freeze Review
```

This review was read-only with respect to every selected C1.07R2 artifact.

## 1. Integrity and regression

All nine selected R2 targets rehash to Candidate Selection.

All eight exact C1.07R1 parent bindings and all three governing R1 independent-recheck artifacts rehash correctly.

The independent package manifest verifies every bundled file.

The full R2 machine schema passes Draft 2020-12 meta-validation.

All 112 inherited machine vectors pass. All 30 executable semantic vectors from C1.07R1 and C1.07R2 were independently re-evaluated using a separately implemented validator.

C1-338..C1-570 are preserved from the exact R1 acceptance artifact. C1-571..C1-585 are contiguous and 15/15 decision-mapped.

Inherited authority reconstructs C1-001..C1-570 exactly once.

## 2. C1RT-B04 — CLOSED

The direct cross-version Listing attacks now behave correctly:

```text
same ListingID + same InstrumentID + same VenueID
→ PASS

same ListingID + same InstrumentID + changed VenueID
→ LISTING_VENUE_REPARENT_FORBIDDEN

same ListingID + changed InstrumentID
→ LISTING_REPARENT_FORBIDDEN
```

The cross-canonical-Venue transfer package also behaves correctly:

```text
same InstrumentID
distinct old/new VenueIDs
distinct old/new ListingIDs
TERMINATE old
CREATE new
PREDECESSOR_OF old → new
→ PASS
```

Negative attacks reject reuse of the old ListingID, InstrumentID changes, a same-Venue fake transfer, and a reversed/misdirected successor package.

The same-canonical-Venue continuity control passes when ListingID, InstrumentID and VenueID remain unchanged while only non-identity tier/segment/display-label metadata changes.

## 3. Prior closure regression

C1RT-B01/B02/B03 remain closed. Targeted C1.06 smoke vectors remain passing for discriminator/payload binding, exactness certification, provider outcome consistency, mapping target-kind governance, and CURRENT_ONLY/TEMPORAL expected-target mismatch cases.

The integrated semantic surface also still carries explicit inherited hooks for ContractVenueAdmission same-parent-Instrument consistency, PROJECTED/REALIZED separation, projected non-activation, active-vs-visible graph separation, SchemeDefinition/result target compatibility, and exact source-query binding.

No new whole-C1 load-bearing contradiction was found.

## 4. Gate

The complete C1.07 red-team blocker sequence is now closed:

```text
C1RT-B01 CLOSED
C1RT-B02 CLOSED
C1RT-B03 CLOSED
C1RT-B04 CLOSED
```

Therefore:

```text
C1.07:
PASS_AFTER_C1_07R2

C1:
ELIGIBLE TO ENTER FREEZE-CANDIDATE STAGE
NOT YET FROZEN

C1.08:
AUTHORIZED
```

C1.08 must construct a content-addressed freeze candidate and then undergo an independent freeze review.

Production implementation remains NOT AUTHORIZED.
