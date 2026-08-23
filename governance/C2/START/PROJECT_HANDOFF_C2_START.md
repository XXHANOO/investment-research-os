# Investment Research OS — New Chat Handoff for C2

Generated: 2026-08-23T21:18:15Z

## 1. Authoritative starting state

```text
C0 = FROZEN
C1 = FROZEN

C1 Freeze Seal:
438274542570f7398af8622fdb511b85d69fc4c403b246b93a8a593b5d8070a5

C2 = NOT STARTED

Production implementation = NOT AUTHORIZED
```

The new chat must treat the bundled C0 and C1 bytes/hashes as parent authority. It must not redesign or weaken C0/C1.

## 2. C2 responsibility frozen by C0

C0 assigns C2:

**Provider / Source Router / Provider Certification**

C2 owns:
- provider capabilities;
- routing;
- certification;
- credentials boundary;
- typed provider outcomes.

C2 does **not** own:
- C1 canonical identity;
- C3 cache/quota/freshness/coalescing/LKG;
- C4 exact PIT/revision/available_from;
- C5 evidence/source-fitness/verification/conflict;
- C11 persistence.

Cross-contract seams must remain explicit rather than absorbed into C2.

## 3. Mandatory C0 provider semantics

At minimum C2 must preserve:
- `C0-008`: HTTP/server/auth/network failures are typed failures, never genuine NO_DATA.
- `C0-009`: exhausted 429/rate-limit retry is typed failure.
- `C0-010`: provider-established genuine absence may be NO_DATA.
- `C0-011`: operation status and data outcome are orthogonal.
- `C0-014`: provider-native payload cannot bypass canonical normalization.
- `C0-049/050`: secure raw-ingress precedes immutable permitted-raw storage; admitted raw content is immutable by identity.
- `C0-051`: claim/source fitness belongs to C5, not C2.
- `C0-052`: domain/application cannot directly import provider infrastructure.
- `C0-057`: untrusted provider/web/tool content cannot originate side-effect intent.
- `C0-060`: load-bearing repository evidence must be exact-path/blob pinned and role/scope constrained.

C0 forbidden provider-relevant patterns include F-04, F-06, F-13, F-19, F-20, F-25, and F-33.

## 4. Frozen C1.05 ↔ C2 interface

The exact passed C1.05R1 provider-normalization interface is bundled.

Non-negotiable downstream requirements on C2:
1. load-bearing semantic/capability/completeness references are snapshot-stable;
2. replay-critical lineage is mandatory for materialized normalized output;
3. material fallback/degradation provenance cannot be erased;
4. FAILED/CANCELLED implies normalization NOT_RUN;
5. SUCCESS+NO_DATA does not by itself prove C1 NO_MATCH;
6. SUCCESS+PARTIAL cannot prove missing-candidate absence or uniqueness;
7. load-bearing exact absence/uniqueness needs certified completeness/coverage;
8. provider/data/normalization/resolution/PIT/verification axes stay orthogonal;
9. positive exact mapping does not automatically require universe-wide enumeration.

C2 must define its own provider capability/certification/completeness records without redefining C1 identity semantics.

## 5. Proposed C2 governance sequence

The package contains `C2_PROPOSED_STAGE_PLAN.yaml`.

This sequence is **PROPOSED, NOT C0/C1-FROZEN AUTHORITY**. The new chat must say so.

Recommended first construction gate:

```text
C2.00 — Scope / Authority / Vocabulary Candidate
```

Suggested later stages:
C2.01 capability/endpoint semantics;
C2.02 typed operation/data outcomes;
C2.03 routing/fallback/degradation;
C2.04 credentials/secure ingress;
C2.05 certification/completeness/coverage;
C2.06 C1/C3/C4/C5 interfaces;
C2.07 schema/tests;
C2.08 whole-C2 red-team;
C2.09 freeze candidate/review.

## 6. C2.00 rules

C2.00 should:
- define C2 scope, authority and vocabulary only;
- create an ownership/boundary matrix;
- enumerate inherited C0/C1 constraints with exact parent hashes;
- define unresolved questions without silently choosing implementation vendors;
- create an acceptance catalog/decision ledger appropriate to the stage;
- remain content-addressed;
- stop for independent C2.00 review.

C2.00 must **not**:
- write production provider adapters;
- select Alpaca/Tushare/AKShare/etc as canonical semantics;
- define C3 freshness/cache policy;
- define C4 temporal visibility;
- define C5 source fitness;
- weaken C1.05;
- authorize LIVE/PAPER/external side effects;
- self-approve or self-freeze.

## 7. Required workflow

Use the same governance discipline as C1:

```text
candidate construction
→ independent review
→ narrow repair if blocked
→ independent regression re-check
→ only then next stage
```

Passed/frozen parent artifacts remain immutable.

When a blocker is found, stop and issue the narrowest repair stage. Do not silently redesign parents.

## 8. New-chat first action

Before constructing C2.00:
1. verify the package manifest;
2. rehash exact C0 root/core authority and C1 freeze seal;
3. verify C1.05R1 hashes;
4. state that the proposed C2 stage plan is not yet frozen;
5. then construct **C2.00 only** if the user authorizes/adopts the proposed plan.

Production implementation remains NOT AUTHORIZED.
