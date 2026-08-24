# C2.03 — Stage Report

Generated: 2026-08-24T10:49:00Z

## Stage

`C2.03 — Routing / Fallback / Degradation Semantics`

## Construction verdict

`COMPLETE_AS_CANDIDATE_NOT_INDEPENDENTLY_REVIEWED`

## Constructed semantic surface

- hard semantic-compatibility route eligibility inherited from C2.01R1;
- deterministic candidate ordering without concrete vendor priorities;
- typed route continuation classes and closed route-action domain;
- explicit handling for PRESENT / genuine NO_DATA / PARTIAL / FAILED / CANCELLED;
- same-route reattempt versus next-route fallback semantics;
- exact semantic ownership seam: C2 logical route nomination vs C3 quota/backoff admission vs C7 orchestration/budget;
- mandatory FallbackEvent lineage;
- equivalent fallback versus explicit requirement downgrade;
- closed provider/route degradation kinds without absorbing C3 stale/cache/LKG;
- orthogonal route terminal dispositions;
- route exhaustion and zero-candidate states that cannot masquerade as provider NO_DATA/C1 NO_MATCH;
- replay-lineage and trusted-intent constraints.

## Candidate open-question disposition

```text
C2.OPEN-006 = CANDIDATE_CLOSED_PENDING_INDEPENDENT_ROUTING_REVIEW
C2.OPEN-007 = CANDIDATE_CLOSED_AT_C2_03_SEMANTIC_LEVEL_PENDING_INDEPENDENT_ROUTING_REVIEW_AND_C2_06_WIRE_BINDING
C2.OPEN-008..015 = OPEN_UNCHANGED
```

## Governance counts

```text
Decisions: C2.DEC-130..C2.DEC-179 = 50
Acceptance obligations: C2-181..C2-230 = 50
Concrete provider instances = 0
Production adapters = 0
```

## Required independent review attacks

The Independent Routing Review must specifically attack:

1. whether route eligibility can ever weaken C2.01 compatibility;
2. route-order total determinism and hidden provider priority;
3. FAILED/NO_DATA/PARTIAL/CANCELLED continuation correctness;
4. whether retry nomination accidentally absorbs C3 backoff/quota authority;
5. whether C7 budgets/cancellation are accidentally absorbed;
6. equivalent fallback versus silent requirement degradation;
7. whether successful fallback can erase material failed/partial/no-data lineage;
8. route exhaustion versus provider NO_DATA/C1 NO_MATCH;
9. C2 degradation versus C3 stale/cache/LKG degradation;
10. untrusted provider content modifying routing, policy, or side-effect intent;
11. replay sufficiency and C1.05R1 lineage continuity;
12. C2.OPEN-007 semantic closure versus still-open C2.06 wire binding.

## Stop condition

C2.04 is not started or authorized by this construction. The next gate is **C2.03 Independent Routing Review**.
