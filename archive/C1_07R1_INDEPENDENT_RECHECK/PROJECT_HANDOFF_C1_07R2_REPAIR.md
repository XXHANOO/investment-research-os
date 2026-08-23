# PROJECT HANDOFF — C1.07R1 Failed Re-Check → C1.07R2

Generated: 2026-08-23T19:28:51Z

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

C1.07:
FAIL

C1RT-B01:
CLOSED

C1RT-B02:
CLOSED

C1RT-B03:
CLOSED

C1RT-B04:
OPEN — same ListingID can change canonical VenueID without terminate/create/successor semantics

C1 overall freeze:
NOT ELIGIBLE

Production implementation:
NOT AUTHORIZED
```

## Exact next stage

`C1.07R2 — Listing Venue Continuity & Transfer Invariant Repair`

## Narrow R2 repair

1. Preserve the exact R1 integrated schema/test/governance candidate as parent.
2. Extend the cross-version Listing invariant:
   - same ListingID → instrument_ref immutable;
   - same ListingID → venue_ref immutable.
3. Add `LISTING_VENUE_REPARENT_FORBIDDEN`.
4. Add explicit cross-canonical-Venue transfer semantic validation:
   - same InstrumentID;
   - old/new ListingIDs are distinct;
   - old/new VenueIDs are distinct;
   - terminate old ListingID;
   - create new ListingID;
   - predecessor/successor old→new.
5. Add a valid same-canonical-Venue continuity control so market-tier/segment/display-label changes do not automatically remint ListingID.
6. Preserve C1RT-B01/B02/B03 closures.
7. Preserve C1SCHEMA-B01..B07 closures.
8. Preserve C1.OPEN-010 CLOSED.
9. Preserve C4 ownership of effective time and C11 ownership of persistence.
10. Do not begin production implementation.
11. Add only narrow R2 decisions/acceptance/tests and extend inherited regression authority.
12. Stop at `C1.07R2 Independent Regression Re-Check`.

Do not redesign passed C1.01R1–C1.05R1 contracts.
