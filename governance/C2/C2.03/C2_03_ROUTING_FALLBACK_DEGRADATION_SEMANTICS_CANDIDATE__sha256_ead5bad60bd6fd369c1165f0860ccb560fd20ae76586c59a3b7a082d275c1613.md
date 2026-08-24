# C2.03 — Routing / Fallback / Degradation Semantics Candidate

Generated: 2026-08-24T10:49:00Z

Status: `CONSTRUCTED_CANDIDATE_PENDING_INDEPENDENT_ROUTING_REVIEW`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

## 1. Authorization and scope

The user explicitly authorized the next C2 stage after C2.02R2 Independent Outcome-Semantics Re-Check returned `PASS`. This candidate constructs only **C2.03 — Routing / Fallback / Degradation Semantics**.

C2.03 owns the provider/source route decision semantics that operate **after** C2.01 semantic compatibility has been proven and consume C2.02 typed provider-operation outcomes. It defines deterministic route candidate ordering, route continuation actions, fallback provenance, explicit semantic-degradation handling, and the semantic seam between C2 logical reattempt/fallback decisions and C3 quota/backoff admission.

C2.03 does **not** define concrete provider priorities, vendor instances, credentials, provider certification/completeness, C3 retry/backoff/quota/cache/freshness algorithms, C4 PIT semantics, C5 source-fitness/verification, C6 capability grants/trusted-intent policy, C7 orchestration budgets/cancellation policy, C11 persistence, C12 release authority, or production adapters.

## 2. Exact parent pins

```text
C2.00 scope/authority/vocabulary       b504211651839b1cd9c79a9706f05e1ad9c072f66bfb887aec2a0d65c9b17cf7
C2.01R1 capability registry           2cba76ffe8e308ade83778e26d24332c4ce019468a73875c36110c7bb5201e95
C2.01R1 independent re-check result   e780ab10b6ed6e6108cc6fafc53ce329827b6135764b993f7a785fdd46e37937
C2.02R2 outcome contract              901445ca8f0f3f1a8cd04331d3def83f4a29ae3984e5917e723e2402f858f57d
C2.02R2 logical model                 763a0c1995116a657621633bde6224df332287d76c7ce986066f2d493022d04d
C2.02R2 independent review report     48eba8055fdec4be85eed5c06bd8b809e7716d937cc05cbbeb5078c7b219f509
C2.02R2 independent review result     36d9048577fbaed39f1af1ae6352fe8de9fb803a55c59fadd05ee633597c34e5
C1.05R1 normalization interface       71d472e63044b9a7be2c6cc831705ed80dc6a06ccd0ef03e71a0618794bdef63
Adopted C2 stage plan                 b7a4f2a3958417f155e24109edaf025c017d7fc8ac7980ff9765c90fe97e70d6
```

## 3. Core routing principles

1. **Semantic compatibility is a hard precondition, never a score.** A route candidate for requirement `R` is semantically eligible only if `compatible(R,P,S)` is true under the exact C2.01R1 predicate and the same pinned registry snapshot `S`. C2.03 cannot weaken, approximate, or override that predicate.
2. **Routing preference is not source fitness.** A C2 route rank is an operational preference only. It does not assert C5 quality, credibility, truth, or claim/source fitness.
3. **A successful fallback does not erase earlier attempts.** Every material attempt, provider failure, genuine NO_DATA continuation, PARTIAL continuation, fallback transition, and explicit degradation remains replay-visible.
4. **NO_DATA remains NO_DATA.** Continuing to another route after `SUCCESS + NO_DATA` does not reclassify the first attempt as FAILED and does not prove C1 NO_MATCH.
5. **PARTIAL remains PARTIAL.** Routing may continue after a partial provider result, but the partiality lineage is preserved and C2.03 does not merge records across providers.
6. **Cancellation terminates the current route request.** C2.03 does not silently convert `CANCELLED` into fallback or a fresh route request. C7 or an upstream trusted caller may initiate a new route request under its own authority.
7. **No implicit semantic downgrade.** C2 cannot weaken `R` because preferred routes failed. Any weaker requirement must be a distinct, canonical `R'` supplied or explicitly authorized by the trusted request/policy boundary and revalidated through C2.01 compatibility.
8. **C2 nominates; external authorities admit.** C2 may decide the next logical route candidate or same-route reattempt candidate, but actual dispatch remains subject to C3 admission, C6 authorization, C7 orchestration/budget/cancellation, C2.04 credential readiness, and any later C2.05 certification gate.

## 4. Route request and pinned decision state

A C2 route decision is evaluated against an immutable logical snapshot:

```text
RouteDecisionInput:
  route_request_id
  registry_snapshot_ref                # S
  capability_requirement               # exact normalized R, replay retained
  route_policy_snapshot_ref            # C2 content-addressed routing policy semantics
  candidate_set_ref                    # exact content-addressed candidate inventory
  trusted_authorization_refs[]         # opaque here; exact C6/C7 binding deferred C2.06
  prior_route_attempt_refs[]            # ordered, immutable lineage
  prior_fallback_event_refs[]
  prior_route_degradation_refs[]
```

Provider payloads, provider documentation, SDK metadata, search results, untrusted external content, or mutable aliases MUST NOT alter `R`, the candidate inventory, route order, trusted authorization, or route policy.

## 5. Route candidate model

Each logical `RouteCandidate` contains at minimum:

```text
route_candidate_id
provider_capability_ref
source_binding_ref?                    # provider/source binding if required
policy_preference_tier                 # non-negative integer
policy_preference_ordinal              # non-negative integer
```

The candidate is interpreted only under the same pinned registry snapshot `S`.

### 5.1 Layered eligibility

C2.03 distinguishes three layers:

```text
SEMANTIC_ELIGIBILITY
  compatible(R, provider_capability_ref, S) == true

ROUTE_POLICY_ELIGIBILITY
  candidate is present in the trusted candidate inventory
  and permitted by the pinned route policy snapshot

DISPATCH_ADMISSIBILITY
  external gates required for actual execution are positively satisfied
```

Only the first two are C2.03 route-selection semantics. Dispatch admissibility depends on other authorities and MUST NOT be inferred from semantic compatibility.

A candidate with unknown, dangling, wrong-kind, hash-mismatched, or floating load-bearing refs is not semantically eligible.

### 5.2 Deterministic route ordering

For all candidates passing semantic and route-policy eligibility, the selection order is the ascending tuple:

```text
(policy_preference_tier,
 policy_preference_ordinal,
 route_candidate_id)
```

`route_candidate_id` MUST be unique inside the pinned candidate set and provides the final deterministic tie-break. If uniqueness or ordering cannot be proven, route construction fails closed; local iteration order, provider response timing, hash-map order, or adapter registration order MUST NOT decide the route.

Concrete provider/vendor priorities are configuration instances deferred beyond this contract. C2.03 freezes only the ordering semantics.

For `NOMINATE_NEXT_ROUTE`, C2 selects the first route-policy-eligible candidate in this deterministic order that has not already been attempted under the current effective requirement. A candidate may be revisited only through `NOMINATE_SAME_ROUTE_REATTEMPT`, never by disguising a revisit as NEXT_ROUTE. `NOMINATE_SAME_ROUTE_REATTEMPT` preserves the same route candidate and same effective requirement and creates a new strictly increasing attempt ordinal after external admission.

## 6. Pinned route-policy semantics

A `RoutePolicySnapshot` is content-addressed C2 routing configuration. This contract defines its generic semantics but contains **zero concrete provider/vendor policy instances**.

```text
RoutePolicySnapshot:
  route_policy_id
  semantic_revision
  continuation_rules[]
  external_gate_fallback_mode          # YIELD | NEXT_ROUTE
```

A `ContinuationRule` contains:

```text
rule_id
rule_priority                          # non-negative integer
continuation_class                     # SUCCESS_NO_DATA | SUCCESS_PARTIAL | FAILED
failure_family?
failure_code?
diagnostic_retry_hint?
action                                 # must be legal for the matched continuation class
```

Rules are evaluated deterministically: collect all exact matches, sort by `(rule_priority, rule_id)`, and select the first. `rule_id` is unique inside the snapshot. Unknown rule fields or an illegal class/action pairing fail closed.

If no rule matches, the closed defaults are:

```text
SUCCESS_PRESENT  -> TERMINATE_WITH_ATTEMPT
SUCCESS_NO_DATA  -> TERMINATE_WITH_ATTEMPT
SUCCESS_PARTIAL  -> TERMINATE_WITH_ATTEMPT
FAILED           -> TERMINATE_EXHAUSTED
CANCELLED        -> TERMINATE_CANCELLED
external gate not positively admitted -> YIELD_FOR_EXTERNAL_ADMISSION
```

`SUCCESS_PRESENT` and `CANCELLED` are not overridable by continuation rules in C2.03.

### 6.1 Action legality matrix

```text
SUCCESS_PRESENT:
  TERMINATE_WITH_ATTEMPT

SUCCESS_NO_DATA:
  TERMINATE_WITH_ATTEMPT
  NOMINATE_NEXT_ROUTE

SUCCESS_PARTIAL:
  TERMINATE_WITH_ATTEMPT
  NOMINATE_NEXT_ROUTE

FAILED:
  NOMINATE_SAME_ROUTE_REATTEMPT
  NOMINATE_NEXT_ROUTE
  TERMINATE_EXHAUSTED

CANCELLED:
  TERMINATE_CANCELLED

external admission not positive:
  YIELD_FOR_EXTERNAL_ADMISSION
  NOMINATE_NEXT_ROUTE only when external_gate_fallback_mode == NEXT_ROUTE
```

A rule that maps a class to an action outside this matrix is invalid and MUST fail closed.

## 7. Route-attempt record

Every dispatched attempt produces an immutable logical `RouteAttemptRecord`:

```text
route_attempt_id
route_request_id
attempt_ordinal
route_candidate_ref
capability_requirement_ref_or_exact_value
c2_provider_operation_outcome_ref       # exact C2.02 outcome
external_admission_refs[]               # load-bearing opaque refs only when applicable
route_action_after_attempt
route_decision_reason
```

`attempt_ordinal` is strictly increasing within one route request. Attempt records are append-only lineage; a later success cannot rewrite an earlier attempt.

## 8. Route continuation classes

C2.03 consumes C2.02 outcome semantics without altering them. The route evaluator classifies the observed attempt only for routing action selection:

```text
SUCCESS_PRESENT
SUCCESS_NO_DATA
SUCCESS_PARTIAL
FAILED
CANCELLED
```

Failure family/code and C2.02 `diagnostic_retry_hint`, when present, may be inputs to a pinned route policy. They remain diagnostics, not C3 retry authority.

## 9. Route actions

The closed C2.03 logical action set is:

```text
TERMINATE_WITH_ATTEMPT
NOMINATE_SAME_ROUTE_REATTEMPT
NOMINATE_NEXT_ROUTE
YIELD_FOR_EXTERNAL_ADMISSION
REQUIRE_EXPLICIT_REQUIREMENT_DOWNGRADE
TERMINATE_EXHAUSTED
TERMINATE_CANCELLED
```

No adapter may invent a private route action.

The closed `route_decision_reason` set is:

```text
PRESENT_ACCEPTED
GENUINE_NO_DATA_TERMINAL
GENUINE_NO_DATA_CONTINUATION
PARTIAL_ACCEPTED
PARTIAL_CONTINUATION
PROVIDER_FAILURE_REATTEMPT
PROVIDER_FAILURE_CONTINUATION
PROVIDER_FAILURE_EXHAUSTED
EXTERNAL_ADMISSION_YIELD
EXTERNAL_ADMISSION_CONTINUATION
CANCELLED_PROPAGATION
NO_ELIGIBLE_NEXT_ROUTE
EXPLICIT_REQUIREMENT_DOWNGRADE
```

Action/reason pairings must be semantically coherent. For example, `NOMINATE_SAME_ROUTE_REATTEMPT` requires `PROVIDER_FAILURE_REATTEMPT`; `TERMINATE_CANCELLED` requires `CANCELLED_PROPAGATION`; and `SUCCESS + NO_DATA` cannot use a provider-failure reason.

### 8.1 Successful PRESENT

`SUCCESS + PRESENT` has only one conforming C2.03 action: `TERMINATE_WITH_ATTEMPT`. Multi-provider corroboration or collection is a separate explicitly authorized orchestration/route request, not silent continuation of this route.

### 8.2 Genuine NO_DATA

For `SUCCESS + NO_DATA`, the pinned route policy may either:

```text
TERMINATE_WITH_ATTEMPT
or
NOMINATE_NEXT_ROUTE
```

A `NOMINATE_NEXT_ROUTE` transition reason is `GENUINE_NO_DATA_CONTINUATION`. The original attempt remains `SUCCESS + NO_DATA`; it is not rewritten as failure and does not prove canonical absence.

### 8.3 PARTIAL

For `SUCCESS + PARTIAL`, the pinned route policy may terminate with the partial attempt or nominate a next route. A next-route transition reason is `PARTIAL_CONTINUATION`. Existing partial observations and partiality evidence remain attached to their original attempt. C2.03 does not union, deduplicate, reconcile, or verify cross-provider records.

### 8.4 FAILED

For `FAILED`, the route policy may choose one of:

```text
NOMINATE_SAME_ROUTE_REATTEMPT
NOMINATE_NEXT_ROUTE
TERMINATE_EXHAUSTED
```

The C2.02 diagnostic retry hint may be consulted but cannot itself dispatch or schedule a retry. A provider failure is never converted to NO_DATA.

### 8.5 CANCELLED

For `CANCELLED`, the only conforming C2.03 action for the current route request is:

```text
TERMINATE_CANCELLED
```

No same-route reattempt or fallback is automatically permitted inside the cancelled route request.

## 10. Exact C2 / C3 retry-quota-backoff seam

C2.03 closes the semantic portion of `C2.OPEN-007` as follows:

```text
C2 owns:
  which semantically compatible route candidate is logically next;
  whether the pinned route policy nominates SAME_ROUTE_REATTEMPT or NEXT_ROUTE;
  route/fallback provenance and transition reason.

C3 owns:
  whether an attempt may execute under quota/backoff/cache/freshness state;
  retry timing / delay / backoff computation;
  quota accounting and admission;
  cache, coalescing, stale/LKG selection and associated degradation semantics.

C7 owns:
  orchestration continuation;
  workflow attempt budgets;
  cancellation and durable resume policy.
```

Therefore:

1. A C2 `NOMINATE_SAME_ROUTE_REATTEMPT` is only a logical nomination.
2. C2 MUST NOT sleep, compute a backoff duration, decrement quota, or infer C3 admission.
3. Actual re-dispatch requires a positive C3 admission under the future cross-contract binding and continued C7 authorization/budget.
4. When admission is not currently positive or cannot be proven, C2 performs no dispatch. It yields the route with load-bearing external admission provenance; C7 decides whether/when orchestration resumes.
5. C2 may nominate a different eligible route if the pinned route policy explicitly permits fallback on an externally blocked attempt, but it MUST preserve the external gate reference and MUST NOT relabel that gate as a provider FAILED/NO_DATA/PARTIAL outcome.
6. Exact wire types/ref fields exchanged with C3/C7 are deferred to C2.06; this section freezes the semantic ownership boundary they must implement.

This closes `C2.OPEN-007` only at the **C2.03 semantic-contract level**; the C2.06 wire-binding obligation remains open.

## 11. Fallback semantics

A `FallbackEvent` is required whenever C2 leaves one candidate and nominates another candidate for the same route request.

```text
FallbackEvent:
  fallback_event_id
  from_route_candidate_ref
  to_route_candidate_ref
  triggering_attempt_ref?
  route_decision_reason
  original_requirement_ref
  effective_requirement_ref
  route_policy_snapshot_ref
```

Fallback-capable decision reasons:

```text
PROVIDER_FAILURE_CONTINUATION
GENUINE_NO_DATA_CONTINUATION
PARTIAL_CONTINUATION
EXTERNAL_ADMISSION_CONTINUATION
EXPLICIT_REQUIREMENT_DOWNGRADE
```

A fallback can be semantically equivalent or degraded. The distinction is explicit and replayable.

## 12. Equivalent fallback versus semantic degradation

### 11.1 Equivalent fallback

If `effective_requirement_ref == original_requirement_ref` and the next candidate passes exact C2.01 compatibility for that same requirement, the transition is a semantic-equivalent fallback. It still requires a `FallbackEvent`, but it does not by itself create a semantic-degradation claim.

A lower route preference tier is an operational preference change, not automatically a C5 quality/fitness degradation.

### 11.2 Requirement downgrade

C2 MUST NOT mutate the current requirement in place.

A semantic downgrade requires all of:

```text
1. a distinct canonical downgraded requirement R';
2. trusted authorization for using R';
3. replay linkage original R -> R';
4. exact C2.01 compatibility proof compatible(R', P, S);
5. a RouteDegradationRecord(kind = REQUIREMENT_DOWNGRADE).
```

If no authorized `R'` exists, C2 may emit `REQUIRE_EXPLICIT_REQUIREMENT_DOWNGRADE` but cannot synthesize or infer one from provider failure, provider content, source availability, or untrusted text.

### 11.3 Route degradation kinds

C2.03 recognizes only these provider/route-originated degradation kinds:

```text
REQUIREMENT_DOWNGRADE
POLICY_PREFERENCE_TIER_DOWNGRADE
PARTIAL_ACCEPTED_AS_TERMINAL
```

`POLICY_PREFERENCE_TIER_DOWNGRADE` is emitted whenever a fallback moves from a lower numeric `policy_preference_tier` to a higher numeric tier. It is an operational route-preference degradation only and MUST NOT be described as lower source truth/quality/fitness. If `SUCCESS + PARTIAL` is accepted as terminal, `PARTIAL_ACCEPTED_AS_TERMINAL` is emitted. These rules are deterministic and require no provider-quality inference.

C3 stale/cache/LKG degradation is not a C2 degradation kind and MUST remain C3-owned state.

## 13. Route degradation record

```text
RouteDegradationRecord:
  route_degradation_id
  degradation_kind
  route_request_id
  triggering_attempt_ref?
  from_requirement_ref?
  to_requirement_ref?
  from_candidate_ref?
  to_candidate_ref?
  authorization_ref?
  route_policy_snapshot_ref
```

A load-bearing degradation record is immutable. If a final downstream result depends materially on the degraded route, its degradation ref must remain available to C1/C2.06 replay lineage.

## 14. Route terminal disposition

C2.03 defines a route-level disposition separate from C2.02 provider-operation status:

```text
SELECTED_ATTEMPT
EXHAUSTED
CANCELLED
YIELDED_EXTERNAL_ADMISSION
REQUIREMENT_DOWNGRADE_REQUIRED
```

Meanings:

- `SELECTED_ATTEMPT`: route policy selected a C2.02 attempt as the terminal provider result for this route request. The referenced attempt still carries its own `SUCCESS/PRESENT|NO_DATA|PARTIAL` semantics.
- `EXHAUSTED`: no further conforming action remains under the current pinned requirement, route policy, candidate set, and available authorizations. It is **not** provider NO_DATA and does not prove C1 NO_MATCH.
- `CANCELLED`: current route request terminated by cancellation semantics; it is not a provider data outcome.
- `YIELDED_EXTERNAL_ADMISSION`: no dispatch occurs while a load-bearing external gate is unresolved/not positive. It is not provider failure and not NO_DATA.
- `REQUIREMENT_DOWNGRADE_REQUIRED`: current requirement cannot be weakened implicitly; a trusted upstream authority must explicitly provide/authorize `R'` before routing continues.

## 15. Route exhaustion and zero-candidate cases

These are route-level conditions, never synthetic provider outcomes:

```text
NO_SEMANTICALLY_COMPATIBLE_CANDIDATE
NO_ROUTE_POLICY_ELIGIBLE_CANDIDATE
ALL_ELIGIBLE_CANDIDATES_CONSUMED
NO_AUTHORIZED_DOWNGRADE
```

An empty route candidate set MUST NOT be represented as `SUCCESS + NO_DATA`, `FAILED`, or C1 `NO_MATCH`.

## 16. Replay lineage

A reconstructable route decision must retain enough immutable identity to reproduce:

```text
registry snapshot S
exact capability requirement R (and R' if degraded)
pinned route policy snapshot
exact candidate inventory and deterministic ordering inputs
selected/attempted route-candidate refs
all C2.02 operation-outcome refs
all material external admission refs
fallback-event refs
route-degradation refs
terminal route disposition
```

A final successful fallback MUST NOT present itself downstream as though the successful provider was the clean primary route when earlier material fallback/degradation occurred.

## 17. Security and trusted-intent boundary

Provider/native payloads and untrusted external content cannot:

- add or reprioritize route candidates;
- change a route policy snapshot;
- authorize a requirement downgrade;
- grant C6 capabilities;
- originate/redirect a side-effect intent;
- change C7 budgets/cancellation;
- rewrite C3 admission/backoff state.

C2.03 routing remains subordinate to trusted authorization and does not create side-effect authority.

## 18. Explicit non-ownership

C2.03 does not decide:

- credentials/private-state ingress — C2.04;
- completeness/certification/coverage strength — C2.05;
- final C1/C3/C4/C5/C6/C7 reference serialization — C2.06;
- exact JSON Schema/validators — C2.07;
- C3 cache/quota/backoff/freshness/coalescing/LKG policy;
- C4 PIT/revision/available_from;
- C5 source fitness/verification/conflict resolution;
- C6 capability grants/trusted policy;
- C7 orchestration budgets/durable scheduling/cancellation;
- concrete provider/vendor ranking instances;
- production/PAPER/LIVE side effects.

## 19. Open-question disposition candidate

```text
C2.OPEN-006 = CANDIDATE_CLOSED_PENDING_INDEPENDENT_ROUTING_REVIEW
C2.OPEN-007 = CANDIDATE_CLOSED_AT_C2_03_SEMANTIC_LEVEL_PENDING_INDEPENDENT_ROUTING_REVIEW_AND_C2_06_WIRE_BINDING
C2.OPEN-008..015 = OPEN_UNCHANGED
```

Only an Independent Routing Review may close the C2.03 semantic contract. C2.06 must still bind the C3/C6/C7 opaque references without changing this ownership seam.

## 20. Forbidden interpretations

```text
semantic compatibility -> route score
route priority -> C5 source fitness
FAILED fallback -> erase original failure
NO_DATA fallback -> relabel first attempt FAILED
PARTIAL fallback -> erase partiality
successful fallback -> pretend clean primary provenance
empty route set -> provider NO_DATA
route exhaustion -> C1 NO_MATCH
C2 reattempt nomination -> C3 retry authorization
C2 -> sleep/backoff/quota accounting
C2 route degradation -> absorb C3 stale/cache/LKG semantics
provider payload -> route policy / priority change
provider failure -> implicit weaker CapabilityRequirement
CANCELLED -> automatic fallback inside same route request
```
