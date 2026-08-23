# C1.07R2 — Listing Venue Continuity & Transfer Invariant Repair Candidate

Generated: 2026-08-23T19:38:29Z

Status: `CANDIDATE_FOR_C1_07R2_INDEPENDENT_REGRESSION_RECHECK`

Production implementation: `NOT AUTHORIZED`

## Exact parent

R2 is constructed from the exact C1.07R1 full integrated schema:

```text
C1_07R1_MACHINE_SCHEMA_CANDIDATE__sha256_7e30026cfb60d08c4ad3ed162fa25768d17e7eb6e4a31c116efeff56db41b9c9.json
SHA-256 7e30026cfb60d08c4ad3ed162fa25768d17e7eb6e4a31c116efeff56db41b9c9
```

The governing independent R1 re-check is:

```text
C1_07R1_INDEPENDENT_REGRESSION_RECHECK_REPORT.md
SHA-256 0090118a79385babc3739c4a1c16be71ff4a00904d7b4c5cb9f35fe65b128195
```

## C1RT-B04 repair

For a stable ListingID:

```text
instrument_ref immutable
venue_ref immutable
```

A VenueID change under the same ListingID returns:

`LISTING_VENUE_REPARENT_FORBIDDEN`

## Cross-canonical-Venue transfer

R2 materializes `C1.SEM.LISTING_VENUE_TRANSFER_PACKAGE`.

Valid transfer requires:

```text
same InstrumentID
old VenueID != new VenueID
old ListingID != new ListingID
TERMINATE old ListingID
CREATE new ListingID
PREDECESSOR_OF old -> new
```

C4 continues to own effective timing/state. C11 continues to own persistence.

## Same-canonical-Venue continuity

R2 materializes `C1.SEM.SAME_VENUE_LISTING_CONTINUITY`.

Tier/segment/display-label-only metadata changes are not canonical ListingRecord identity fields and therefore do not force a new ListingID when InstrumentID and VenueID remain unchanged.

## Regression

- inherited machine vectors: 112/112 PASS
- inherited executable R1 semantic vectors: 20/20 PASS
- new executable R2 semantic vectors: 10/10 PASS
- inherited acceptance C1-338..570 preserved exactly
- inherited authority C1-001..570 gapless
- new C1-571..585 obligations: 15/15 mapped

## Gate

C1RT-B04 is addressed but remains open until independent C1.07R2 regression re-check.

C1RT-B01/B02/B03 remain CLOSED.

C1.OPEN-010 remains CLOSED.

C1.07 remains FAIL pending independent review; C1 is not freeze-eligible.

Next exact gate:

`C1.07R2 Independent Regression Re-Check`
