# C2.03R1 Independent Routing Re-Check Report

Generated: 2026-08-24T11:54:40Z

Review type: `INDEPENDENT_ROUTING_RECHECK`

Candidate under review: `C2.03R1 Routing / Fallback / Degradation Semantics Scoped Repair Candidate`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

C2.04: `NOT_AUTHORIZED`

## 1. Exact successor-candidate pins re-checked

```text
C2.03R1 normative contract      18273aced9f962a863a71a82dd538707dd68f3e234d240d4a1f8cd7d75c77fe5
C2.03R1 logical model           620ad5a56130861c730b2c042d0cd9a79f9f738f433242553f97ce68528af082
C2.03R1 acceptance delta        e57370c527bbc0a01a5be71b0946a9acc61305d29ab6a17362367e9a4c181167
C2.03R1 decision ledger         4b010ebf02e0cdef28b60f5727781df4baaf0f0071febb78b1931d0ad7d32650
C2.03 original review report    4852c1109ab0175715a282d125871a2cd3215097eb27ba854e1616f4a48c2a3a
C2.03 original review result    d1a46f949f42612b963b742107ef9fd819b257821b5e4bbfa0d422d3f62618ba
```

Local SHA-256 re-hash matched the content-addressed successor filenames for the normative contract, logical model, acceptance delta, and decision ledger. The review did not use construction mechanical validation as approval evidence.

## 2. Review method

The re-check independently re-attacked all four original routing blockers and the repaired surfaces:

- C2.03-owned candidate-set and route-policy stable identity;
- route-policy permission and deterministic candidate ordering;
- exact `ContinuationRule` match-set construction and tie-breaking;
- external-admission block event provenance and consumed-state progression;
- `RouteStateKey = (route_candidate_ref, effective_requirement_identity)` semantics;
- same-candidate / new-requirement transitions;
- interaction between an authorized `R -> R'` transition and ordinary continuation under current `R`;
- replay reconstruction and C2/C3/C6/C7 ownership boundaries;
- the five original failed obligations `C2-204`, `C2-221`, `C2-226`, `C2-227`, `C2-228`;
- all R1 obligations `C2-231..C2-269`.

The review also used adversarial states not explicitly enumerated by the R1 acceptance delta, because an independent re-check must reject a candidate if a load-bearing deterministic-closure gap remains even when all stated repair vectors pass.

## 3. Original blocker re-check

### C2ROUTE-B01 — CLOSED

R1 now defines a C2.03-owned `C2RoutingStableRef` with the full tuple:

```text
(authority, ref_kind, logical_id, semantic_revision, content_sha256)
```

and closes routing ref kinds to `ROUTE_CANDIDATE_SET` and `ROUTE_POLICY_SNAPSHOT`. Content identity is `SHA-256(RFC8785_JCS(normative_body))`; wrong-kind, dangling, floating, or hash-mismatched refs fail closed.

`CandidateSetDefinition` now provides a content-addressed candidate inventory with unique `route_candidate_id`, deterministic body canonicalization, and a route-candidate ref scoped by the exact candidate-set ref.

`RoutePolicySnapshot` now binds the exact candidate set and closes permission to:

```text
ALL_IN_CANDIDATE_SET
ALLOWLIST
```

with exact allowlist validation. Thus the route-policy-eligible set is derivable from the pinned candidate set and pinned policy rather than from provider names, mutable defaults, or implementation-local policy.

**Verdict:** `C2ROUTE-B01 = CLOSED`.

### C2ROUTE-B02 — CLOSED

R1 now defines `matches(rule, A)` before tie-breaking:

- continuation class uses exact closed-enum equality;
- omitted qualifiers are wildcards;
- present qualifiers compare exactly;
- failure qualifiers are legal only for `FAILED`;
- `failure_code` requires `failure_family`;
- present qualifier + absent attempt value is non-matching;
- unknown/illegal state fails closed;
- only after exact match-set construction is `(rule_priority, rule_id)` applied.

The previous implementation-dependent interpretation of optional qualifiers is therefore removed.

**Verdict:** `C2ROUTE-B02 = CLOSED`.

### C2ROUTE-B03 — CLOSED at the C2.03 semantic-contract level

R1 now introduces immutable `ExternalAdmissionBlockRecord` lineage for a candidate that does not dispatch because required external admission is unresolved/non-positive. An external-admission fallback has an event-level `triggering_external_admission_block_ref`, and provider-attempt and external-block triggers are mutually distinguished.

The successor also defines:

```text
RouteStateKey = (route_candidate_ref, effective_requirement_identity)
```

and makes a key consumed for `NOMINATE_NEXT_ROUTE` after either a dispatched attempt or a fallback-consuming external block. `YIELD_FOR_EXTERNAL_ADMISSION` does not newly consume the key and keeps the same candidate pending. The prior A -> B -> A reselection loop caused by a non-dispatched blocked candidate is therefore removed.

The exact C3/C6/C7 wire types and canonical external-gate ref serialization remain correctly deferred to C2.06; that deferral no longer substitutes for missing C2.03 event semantics.

**Verdict:** `C2ROUTE-B03 = CLOSED`.

### C2ROUTE-B04 — OPEN_AFTER_R1_RECHECK

R1 successfully repairs the **same-candidate / new-requirement** contradiction that caused the original B04. It defines an explicit `AuthorizedRequirementTransitionInput`, requirement-keyed `RouteStateKey`, a dedicated `NOMINATE_CANDIDATE_UNDER_DOWNGRADED_REQUIREMENT` action, `RequirementTransitionEvent`, and mandatory `REQUIREMENT_DOWNGRADE` degradation lineage. Therefore `A@R` and `A@R'` are distinct route states and a candidate previously attempted under `R` may be selected under valid `R'` without misusing `NOMINATE_SAME_ROUTE_REATTEMPT`.

However, the successor still does **not** define the deterministic activation / precedence rule for an already-present valid `AuthorizedRequirementTransitionInput` relative to ordinary routing under the current requirement.

The same pinned decision state can contain all of the following:

```text
current effective requirement = R
prior attempt A@R = FAILED
pinned continuation rule for FAILED = NOMINATE_NEXT_ROUTE
eligible unconsumed candidate B@R exists
a valid trusted AuthorizedRequirementTransitionInput R -> R' is also present
eligible candidate(s) under R' exist
```

The contract states both that ordinary continuation rules choose the action for the current attempt and that the closed action for applying an already-authorized downgrade is `NOMINATE_CANDIDATE_UNDER_DOWNGRADED_REQUIREMENT`. It does not state whether:

1. the current-R continuation must run first and only after current-R routing is exhausted may the transition apply;
2. presence of a valid authorized transition immediately supersedes ordinary continuation;
3. a trusted upstream directive must explicitly choose between continuing R and applying R'; or
4. another deterministic precedence rule applies.

Consequently two implementations can consume the same exact `RouteDecisionInput`, policy, candidate set, prior lineage, and valid transition input and produce different next logical states while each follows a separately stated rule:

```text
Implementation A: continue to B@R
Implementation B: apply R -> R' and nominate first eligible candidate under R'
```

The same ambiguity exists if an authorized transition is present before any provider attempt: the successor does not state whether such a transition may be applied immediately or only after a defined current-requirement terminal condition. This also makes the phrase “same candidate as before / selected candidate also changes” under Section 12.3 under-defined when there is no prior selected/attempted candidate.

The `EXHAUSTED` definition reinforces the need for an explicit rule because it says exhaustion means no conforming action remains under the current pinned state and available authorizations, yet the contract does not specify at what point an available downgrade authorization participates in the action-selection order.

This is not a C3/C6/C7 wire-binding problem: the transition input is already assumed trusted and present. It is a C2.03 route-decision totality / precedence problem.

**Required R2 repair:** freeze an exact transition-application predicate and precedence relation relative to ordinary continuation/default/exhaustion. The repair must make `next_route_action(RouteDecisionInput, current_state)` single-valued when a valid authorized transition coexists with normal current-R actions. It may, for example, require downgrade application only after a precisely defined current-R exhaustion/downgrade-required state, or introduce an explicit trusted transition-application directive; C2 itself must not infer policy from timing or implementation order.

**Verdict:** `C2ROUTE-B04 = OPEN_AFTER_R1_RECHECK`.

## 4. Acceptance re-check

### 4.1 Five original failed C2.03 obligations

```text
C2-204  PASS
C2-221  PASS at stated lineage-retention level
C2-226  PASS
C2-227  PASS
C2-228  PASS under the R1 RouteStateKey clarification
```

`C2-228` is interpreted consistently with its “under the current requirement” scope: `SAME_ROUTE_REATTEMPT` remains the only revisit of the same **RouteStateKey**, while the same candidate under distinct authorized `R'` is a different state and uses the dedicated downgrade action.

### 4.2 R1 repair obligations

Reviewed: `C2-231..C2-269` (39 obligations)

```text
PASS: 39
FAIL: 0
```

The stated R1 obligations successfully cover the four repair mechanisms they name. In particular, they establish content-addressed routing identities, the exact continuation-rule predicate, external-admission block lineage/consumption, and same-candidate/new-requirement state semantics.

### 4.3 New adversarial coverage gap

Despite `44/44` targeted obligations passing at their stated scope, the independent review found a load-bearing state that the R1 acceptance delta does not test:

```text
valid current-R continuation action
AND
valid AuthorizedRequirementTransitionInput R -> R'
```

There is no acceptance obligation defining which action has precedence or when the authorized transition becomes applicable. Therefore the candidate cannot receive a PASS merely because the enumerated repair obligations pass.

A C2.03R2 acceptance delta must add adversarial vectors for at least:

1. current-R `NOMINATE_NEXT_ROUTE` plus valid R -> R';
2. current-R `NOMINATE_SAME_ROUTE_REATTEMPT` plus valid R -> R';
3. current-R terminal/default action plus valid R -> R';
4. valid R -> R' present before any attempt;
5. no eligible candidate under R but eligible candidate under R' with a valid transition;
6. replay equivalence: identical pinned input must select the same transition/continuation path.

## 5. Boundary re-check

PASS:

- C2.01 compatibility remains a hard semantic gate;
- route preference remains distinct from C5 source fitness/verification;
- C2.02 provider `FAILED`, `NO_DATA`, `PARTIAL`, and `CANCELLED` semantics are not rewritten;
- C2 still only nominates logical routes/reattempts;
- C3 retains admission, quota, backoff, cache, freshness, coalescing, and LKG authority;
- C6/C7 retain trusted authorization and orchestration/budget/cancellation authority;
- provider/native content cannot mutate candidate inventory, route policy, authorization, or side-effect intent;
- no concrete vendor/provider priority instance, production adapter, credential implementation, or PAPER/LIVE authority was introduced.

## 6. Non-blocking traceability notes

### N01 — R1 Stage Report range typo

The immutable R1 Stage Report says `C2-231..C2-268 (39)`. The actual acceptance file, construction summary, and decision ledger contain `C2-231..C2-269`, which is the correct 39-obligation range. This is a report-level traceability typo, not a semantic blocker. A successor report should state the correct range; the historical R1 report should not be rewritten.

### N02 — C2.07 must encode successor RouteStateKey semantics

The original C2-228 wording can be misread as candidate-ID-global revisit prohibition. C2.07 must encode the R1 successor semantics: revisit prohibition is keyed to `(route_candidate_ref, effective_requirement_identity)`, while a same candidate under authorized distinct `R'` is a different route state.

### N03 — C2.06 external-gate wire binding remains open

C2.06 must bind exact C3/C6/C7 external-admission refs and canonical wire representation without changing the C2.03R1 semantic distinction between provider attempts and non-dispatched external-admission block events.

## 7. Final verdict

`FAIL — C2.03R2 NARROW REPAIR REQUIRED`

State:

```text
C2ROUTE-B01 = CLOSED
C2ROUTE-B02 = CLOSED
C2ROUTE-B03 = CLOSED
C2ROUTE-B04 = OPEN_AFTER_R1_RECHECK

C2.OPEN-006 = NOT_CLOSED — R2_REQUIRED
C2.OPEN-007 = NOT_CLOSED — R2_REQUIRED_AT_C2_03_SEMANTIC_LEVEL

C2.03 = REPAIR_REQUIRED_NOT_FROZEN
C2.04 = NOT_AUTHORIZED
Production implementation = NOT_AUTHORIZED
External/PAPER/LIVE side effects = NOT_AUTHORIZED
```

The next permissible construction is a narrow `C2.03R2` repair limited to:

1. deterministic activation/precedence for a valid `AuthorizedRequirementTransitionInput` relative to current-R continuation/default/exhaustion;
2. corresponding adversarial acceptance coverage;
3. successor traceability correction for the non-authoritative R1 stage-report range typo.

No C2.04 construction, production implementation, or external/PAPER/LIVE side effect is authorized.
