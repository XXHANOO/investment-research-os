# C2.03R1 — Routing / Fallback / Degradation Semantics Scoped Repair Candidate

Generated: 2026-08-24T11:34:41Z

Status: `REPAIR_CANDIDATE_PENDING_INDEPENDENT_ROUTING_RECHECK`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

## 1. Authorization and scope

The user explicitly authorized **C2.03R1 scoped repair** after the C2.03 Independent Routing Review returned `FAIL`. This successor candidate repairs only `C2ROUTE-B01..B04`; all other C2.03 semantics remain inherited unless explicitly restated here. It does not self-close any blocker and does not authorize C2.04.

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
C2.03 original routing contract        ead5bad60bd6fd369c1165f0860ccb560fd20ae76586c59a3b7a082d275c1613
C2.03 Independent Routing Review       4852c1109ab0175715a282d125871a2cd3215097eb27ba854e1616f4a48c2a3a
C2.03 Independent Review result        d1a46f949f42612b963b742107ef9fd819b257821b5e4bbfa0d422d3f62618ba
```

## 3. Core routing principles

Repair posture: `C2ROUTE-B01..B04 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_ROUTING_RECHECK`.

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
  registry_snapshot_ref                  # S
  capability_requirement                 # exact normalized current R, replay retained
  original_requirement_identity          # SHA-256(JCS(normalized original R))
  effective_requirement_identity         # SHA-256(JCS(normalized current R))
  route_policy_snapshot_ref              # exact C2.03 routing stable ref
  candidate_set_ref                      # exact C2.03 routing stable ref
  trusted_authorization_refs[]           # opaque here; exact C6/C7 binding deferred C2.06
  authorized_requirement_transition?     # exact logical input; absent unless trusted R' exists
  prior_route_attempt_refs[]              # ordered, immutable lineage
  prior_external_admission_block_refs[]  # ordered, immutable lineage
  prior_fallback_event_refs[]
  prior_requirement_transition_refs[]
  prior_route_degradation_refs[]
```

Provider payloads, provider documentation, SDK metadata, search results, untrusted external content, or mutable aliases MUST NOT alter `R`, the candidate inventory, route order, trusted authorization, or route policy.

## 5. C2.03 routing semantic identity and route candidate model

### 5.1 C2.03-owned stable routing refs

C2.03 owns two load-bearing routing semantic object kinds. They are **not** C2.01 provider-semantic refs and do not extend the C2.01R1 `ref_kind` domain.

```text
C2RoutingStableRef:
  authority = C2
  ref_kind  = ROUTE_CANDIDATE_SET | ROUTE_POLICY_SNAPSHOT
  logical_id
  semantic_revision
  content_sha256
```

Equality is the full tuple `(authority, ref_kind, logical_id, semantic_revision, content_sha256)`. A floating alias, omitted hash, wrong kind, dangling object, or content mismatch fails closed.

For both routing object kinds, `content_sha256` is `SHA-256(RFC8785_JCS(normative_body))`. The identity wrapper itself is not part of `normative_body`, avoiding a self-referential hash. Exact resolution MUST retrieve the declared object kind, verify `logical_id` and `semantic_revision`, recompute the body digest, and require exact equality with the ref. Same `logical_id`/revision with a different `content_sha256` is a different object and MUST NOT compare equal.

### 5.2 CandidateSetDefinition

```text
CandidateSetDefinition:
  identity: C2RoutingStableRef(ref_kind = ROUTE_CANDIDATE_SET)
  normative_body:
    route_candidates[]
```

Each `RouteCandidate` contains:

```text
route_candidate_id
provider_capability_ref
source_binding_ref?
policy_preference_tier
policy_preference_ordinal
```

`route_candidate_id` MUST be unique and non-empty inside one candidate set. For content identity, `route_candidates[]` is canonicalized by ascending `route_candidate_id` before JCS hashing. Array/storage iteration order has no routing authority.

A logical `route_candidate_ref` is the exact pair:

```text
(candidate_set_ref, route_candidate_id)
```

It resolves only when `candidate_set_ref` exact-resolves and that unique `route_candidate_id` exists in its body. This prevents a candidate ID from floating between inventories.

### 5.3 Layered eligibility

C2.03 distinguishes:

```text
SEMANTIC_ELIGIBILITY
  compatible(R, provider_capability_ref, S) == true

ROUTE_POLICY_ELIGIBILITY
  candidate exact-resolves from CandidateSetDefinition
  AND route_policy_snapshot.candidate_set_ref == candidate_set_ref
  AND policy_permitted(candidate, route_policy_snapshot, candidate_set) == true

DISPATCH_ADMISSIBILITY
  external gates required for execution are positively satisfied
```

Only the first two are C2.03 selection semantics. Dispatch admissibility remains externally owned.

### 5.4 Deterministic route ordering and route-state consumption

For semantically and policy eligible candidates, order is ascending:

```text
(policy_preference_tier,
 policy_preference_ordinal,
 route_candidate_id)
```

If uniqueness or ordering cannot be proven, fail closed; local iteration order, provider timing, hash-map order, or adapter registration order MUST NOT decide the route.

C2.03 keys candidate consumption by the exact route state:

```text
RouteStateKey = (route_candidate_ref, effective_requirement_identity)

effective_requirement_identity(R) = SHA-256(RFC8785_JCS(normalized CapabilityRequirement R))
```

A `RouteStateKey` is consumed for `NOMINATE_NEXT_ROUTE` when either:

1. a dispatched `RouteAttemptRecord` exists for that exact key; or
2. an `ExternalAdmissionBlockRecord` exists for that exact key with `route_action_after_gate = NOMINATE_NEXT_ROUTE`.

A `YIELD_FOR_EXTERNAL_ADMISSION` block does **not** consume the key; it retains the same pending candidate for later externally admitted dispatch.

`NOMINATE_NEXT_ROUTE` selects the first eligible **unconsumed RouteStateKey** under the current effective requirement. `NOMINATE_SAME_ROUTE_REATTEMPT` is the only action that revisits the **same RouteStateKey** and therefore requires the same candidate and same effective requirement. The same `route_candidate_ref` under a distinct authorized `R'` has a different `RouteStateKey` and is governed by the requirement-transition semantics in Section 12.

## 6. Pinned route-policy semantics

A `RoutePolicySnapshot` is a C2.03 content-addressed routing object:

```text
RoutePolicySnapshot:
  identity: C2RoutingStableRef(ref_kind = ROUTE_POLICY_SNAPSHOT)
  normative_body:
    candidate_set_ref
    candidate_permission_mode            # ALL_IN_CANDIDATE_SET | ALLOWLIST
    permitted_route_candidate_ids[]      # closed semantics below
    continuation_rules[]
    external_gate_fallback_mode          # YIELD | NEXT_ROUTE
```

For content identity, `permitted_route_candidate_ids[]` is canonicalized ascending and deduplicated; duplicates are invalid rather than silently removed. `continuation_rules[]` is canonicalized by ascending `rule_id` before JCS hashing; `rule_id` MUST be unique.

`candidate_set_ref` inside the policy MUST equal the `RouteDecisionInput.candidate_set_ref` by full routing-ref tuple. Permission is exactly:

```text
policy_permitted(c, policy, set) =
  c exists in set
  AND (
    policy.candidate_permission_mode == ALL_IN_CANDIDATE_SET
    OR
    (policy.candidate_permission_mode == ALLOWLIST
     AND c.route_candidate_id in policy.permitted_route_candidate_ids)
  )
```

Rules:

- `ALL_IN_CANDIDATE_SET` requires `permitted_route_candidate_ids[]` to be empty.
- `ALLOWLIST` permits only listed IDs; an empty allowlist is legal and permits zero candidates.
- Every allowlist ID MUST exist uniquely in the bound candidate set; an unknown ID makes the policy snapshot invalid.
- There is no implicit deny/allow rule, provider-name inference, provider-wide default, or untrusted-content permission.

A `ContinuationRule` contains:

```text
rule_id
rule_priority
continuation_class                     # SUCCESS_NO_DATA | SUCCESS_PARTIAL | FAILED
failure_family?
failure_code?
diagnostic_retry_hint?
action
```

### 6.1 Exact ContinuationRule match predicate

Let `A` be the exact continuation view derived from the pinned C2.02 attempt. `matches(rule, A)` is true iff all of the following hold:

1. `rule.continuation_class == A.continuation_class` by exact closed-enum equality;
2. every **present** qualifier in the rule equals the corresponding attempt value exactly;
3. every **absent** qualifier is an unconstrained wildcard and imposes no absence requirement.

Qualifier legality is closed:

- `failure_family`, `failure_code`, and `diagnostic_retry_hint` are legal only when `continuation_class == FAILED`;
- `failure_code` is legal only when `failure_family` is also present;
- a present qualifier whose corresponding attempt value is absent does not match;
- unknown enum values, unknown qualifier fields, illegal qualifier combinations, or an attempt value that cannot be represented in the inherited closed C2.02 domains invalidate evaluation and fail closed.

A generic FAILED rule and a more specific FAILED rule may both match. C2.03 does **not** infer specificity precedence. After constructing the exact match set, rules are sorted by `(rule_priority, rule_id)` and the first is selected. This makes policy priority explicit rather than implementation inferred.

If no exact rule matches, the closed defaults remain:

```text
SUCCESS_PRESENT  -> TERMINATE_WITH_ATTEMPT
SUCCESS_NO_DATA  -> TERMINATE_WITH_ATTEMPT
SUCCESS_PARTIAL  -> TERMINATE_WITH_ATTEMPT
FAILED           -> TERMINATE_EXHAUSTED
CANCELLED        -> TERMINATE_CANCELLED
external gate not positively admitted -> YIELD_FOR_EXTERNAL_ADMISSION
```

`SUCCESS_PRESENT` and `CANCELLED` remain non-overridable by continuation rules.

### 6.2 Action legality matrix

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

`NOMINATE_CANDIDATE_UNDER_DOWNGRADED_REQUIREMENT` is **not** selectable by a `ContinuationRule`; it is legal only through the explicit trusted requirement-transition procedure in Section 12. Unknown/private actions fail closed.

## 7. Route-attempt record

Every dispatched attempt produces an immutable logical `RouteAttemptRecord`:

```text
route_attempt_id
route_request_id
attempt_ordinal
route_candidate_ref
effective_requirement_identity              # SHA-256(JCS(normalized exact requirement for this attempt))
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
NOMINATE_CANDIDATE_UNDER_DOWNGRADED_REQUIREMENT
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

## 10. Exact C2 / C3 retry-quota-backoff seam and external-admission lineage

The ownership boundary remains unchanged:

```text
C2 owns:
  next logical compatible route state;
  same-route reattempt nomination;
  next-route nomination;
  route/fallback/degradation provenance.

C3 owns:
  attempt admission;
  quota accounting;
  backoff/timing;
  cache/freshness/coalescing/LKG.

C7 owns:
  orchestration continuation;
  budgets;
  cancellation;
  durable resume.
```

A C2 nomination is never C3 admission. C2 MUST NOT sleep, compute backoff, decrement quota, infer freshness, or dispatch without positive external admission.

### 10.1 ExternalAdmissionBlockRecord

Whenever the currently nominated candidate cannot dispatch because one or more required external gates are unresolved or non-positive, C2 creates an immutable logical record even though there is no provider attempt:

```text
ExternalAdmissionBlockRecord:
  external_admission_block_id
  route_request_id
  route_candidate_ref
  effective_requirement_identity
  external_admission_refs[]             # non-empty exact load-bearing gate refs
  route_policy_snapshot_ref
  candidate_set_ref
  route_action_after_gate                # YIELD_FOR_EXTERNAL_ADMISSION | NOMINATE_NEXT_ROUTE
```

The exact C3/C6/C7 wire types of `external_admission_refs[]` remain C2.06-owned, but their semantic role and event linkage are frozen here. Provider content cannot create, remove, or reinterpret these gate refs.

Semantics:

- `YIELD_FOR_EXTERNAL_ADMISSION`: no dispatch, the exact `RouteStateKey` is **not consumed**, and the same `route_candidate_ref` remains the pending candidate for resume after positive external admission.
- `NOMINATE_NEXT_ROUTE`: legal only when the pinned policy has `external_gate_fallback_mode == NEXT_ROUTE`; no dispatch occurs, but the exact `RouteStateKey` is consumed for this route request/current requirement so deterministic next-route selection cannot loop back to it.

The ordered `prior_external_admission_block_refs[]` is append-only replay lineage.

## 11. Fallback semantics

A `FallbackEvent` is required whenever C2 leaves one route candidate and nominates another candidate inside the same route request.

```text
FallbackEvent:
  fallback_event_id
  from_route_candidate_ref
  to_route_candidate_ref
  route_decision_reason
  original_requirement_identity
  effective_requirement_identity
  route_policy_snapshot_ref
  candidate_set_ref
  triggering_attempt_ref?
  triggering_external_admission_block_ref?
```

Exact trigger invariants:

- provider-outcome continuation reasons require `triggering_attempt_ref` and prohibit `triggering_external_admission_block_ref`;
- `EXTERNAL_ADMISSION_CONTINUATION` requires `triggering_external_admission_block_ref`, prohibits `triggering_attempt_ref`, and the referenced block MUST match the event's `from_route_candidate_ref`, effective requirement, policy, and candidate set;
- the block's `external_admission_refs[]` are therefore event-level load-bearing provenance for that exact fallback;
- a fallback event may not invent external gate refs or relabel them as provider FAILED/NO_DATA/PARTIAL outcomes.

Fallback-capable reasons remain:

```text
PROVIDER_FAILURE_CONTINUATION
GENUINE_NO_DATA_CONTINUATION
PARTIAL_CONTINUATION
EXTERNAL_ADMISSION_CONTINUATION
EXPLICIT_REQUIREMENT_DOWNGRADE
```

For `NOMINATE_NEXT_ROUTE`, the candidate search operates on the exact consumed `RouteStateKey` set from Section 5.4. A candidate externally blocked with fallback action is therefore skipped deterministically on subsequent NEXT_ROUTE evaluation under that same effective requirement. A yielded block is not consumed and does not silently advance the candidate set.

## 12. Equivalent fallback and explicit requirement transition

### 12.1 Equivalent fallback

If the effective requirement identity does not change and the next candidate passes exact C2.01 compatibility for that same requirement, the transition is semantic-equivalent fallback. It still requires a `FallbackEvent`; it does not itself create a C5 quality claim or a semantic-downgrade claim.

### 12.2 AuthorizedRequirementTransitionInput

C2 MUST NOT mutate `R` in place. A trusted explicit downgrade is represented as a distinct logical input. A single RouteDecisionInput may carry at most one such transition input; if several alternatives exist, the trusted upstream authority must choose one before C2 evaluates the route. C2 does not rank downgrade alternatives:

```text
AuthorizedRequirementTransitionInput:
  from_requirement                       # exact normalized R
  to_requirement                         # exact normalized R'
  authorization_ref                      # opaque trusted authority ref; wire binding C2.06
```

Let:

```text
from_id = SHA-256(JCS(normalized from_requirement))
to_id   = SHA-256(JCS(normalized to_requirement))
```

A conforming downgrade requires:

1. `from_id == current effective_requirement_identity`;
2. `to_id != from_id`;
3. `authorization_ref` is present from the trusted boundary; C2 does not mint it;
4. candidate selection for `R'` uses exact `compatible(R', P, S)` plus the pinned policy/candidate-set predicate;
5. `R'` becomes effective only by emitting the transition event below;
6. a `RouteDegradationRecord(kind = REQUIREMENT_DOWNGRADE)` is emitted and linked.

If any required fact cannot be proven, routing fails closed or emits `REQUIRE_EXPLICIT_REQUIREMENT_DOWNGRADE`; it never synthesizes `R'` from provider failure/content or untrusted text.

### 12.3 RequirementTransitionEvent and same-candidate/new-requirement semantics

The closed logical action for applying an already authorized downgrade is:

```text
NOMINATE_CANDIDATE_UNDER_DOWNGRADED_REQUIREMENT
```

It is not a `ContinuationRule` action and is valid only when an `AuthorizedRequirementTransitionInput` passes Section 12.2.

C2 selects the first eligible unconsumed `RouteStateKey` under `R'` using the same deterministic candidate order. Consumption is keyed by `(route_candidate_ref, requirement_identity)`. Therefore:

```text
A@R  !=  A@R'
```

A candidate attempted under `R` may be selected under distinct authorized `R'` if `A@R'` is eligible and unconsumed. This is **not** `NOMINATE_SAME_ROUTE_REATTEMPT`, because SAME_ROUTE_REATTEMPT revisits the identical candidate+requirement key only.

Every applied downgrade emits:

```text
RequirementTransitionEvent:
  requirement_transition_id
  route_request_id
  from_requirement_identity
  to_requirement_identity
  authorization_ref
  selected_route_candidate_ref
  candidate_set_ref
  route_policy_snapshot_ref
  route_degradation_ref
```

If `selected_route_candidate_ref` is the same candidate as before, no `FallbackEvent` is required because the candidate did not change; the `RequirementTransitionEvent` plus degradation record is the replay-visible transition. If the selected candidate also changes, a `FallbackEvent(reason = EXPLICIT_REQUIREMENT_DOWNGRADE)` is additionally required and MUST reference the new effective requirement identity.

### 12.4 Route degradation kinds

C2.03 still recognizes only:

```text
REQUIREMENT_DOWNGRADE
POLICY_PREFERENCE_TIER_DOWNGRADE
PARTIAL_ACCEPTED_AS_TERMINAL
```

Higher numeric preference-tier fallback deterministically emits `POLICY_PREFERENCE_TIER_DOWNGRADE`. Terminal acceptance of `SUCCESS + PARTIAL` deterministically emits `PARTIAL_ACCEPTED_AS_TERMINAL`. Neither is a C5 source-quality claim. C3 stale/cache/LKG degradation remains C3-owned.

## 13. Route degradation record

```text
RouteDegradationRecord:
  route_degradation_id
  degradation_kind
  route_request_id
  triggering_attempt_ref?
  from_requirement_identity?
  to_requirement_identity?
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
- `YIELDED_EXTERNAL_ADMISSION`: no dispatch occurs while a load-bearing external gate is unresolved/not positive; the exact pending route candidate and block lineage remain replay-visible. It is not provider failure and not NO_DATA.
- `REQUIREMENT_DOWNGRADE_REQUIRED`: current requirement cannot be weakened implicitly; a trusted upstream authority must explicitly provide/authorize `R'` before routing continues.

The logical terminal record is:

```text
RouteResolution:
  route_request_id
  terminal_disposition
  route_policy_snapshot_ref
  candidate_set_ref
  original_requirement_identity
  effective_requirement_identity
  attempt_refs[]
  external_admission_block_refs[]
  fallback_event_refs[]
  requirement_transition_refs[]
  route_degradation_refs[]
  selected_attempt_ref?
  exhaustion_reason?
  pending_route_candidate_ref?
  unresolved_external_admission_refs[]?
```

`YIELDED_EXTERNAL_ADMISSION` retains the exact `pending_route_candidate_ref`, at least one relevant block ref, and unresolved/non-positive external gate provenance; it does not consume a yielded RouteStateKey. `SELECTED_ATTEMPT` identifies the selected attempt without erasing prior blocks/fallbacks/transitions. Exact conditional machine-schema enforcement is deferred to C2.07, but these semantic fields and invariants are C2.03-owned.

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
all external-admission block refs and their exact gate provenance
fallback-event refs and trigger linkage
requirement-transition refs
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
C2.OPEN-006 = REPAIRED_CANDIDATE_PENDING_INDEPENDENT_ROUTING_RECHECK
C2.OPEN-007 = REPAIRED_CANDIDATE_AT_C2_03_SEMANTIC_LEVEL_PENDING_INDEPENDENT_ROUTING_RECHECK_AND_C2_06_WIRE_BINDING
C2.OPEN-008..015 = OPEN_UNCHANGED
```

Only an Independent Routing Re-Check may close the repaired C2.03 semantic contract. C2.06 must still bind the C3/C6/C7 opaque references without changing this ownership seam.

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
candidate_set_ref / route_policy_snapshot_ref -> floating or hashless identity
omitted ContinuationRule qualifier -> requires attempt-field absence
external-admission blocked+fallback candidate -> silently remains unconsumed
A@R -> A@R' -> SAME_ROUTE_REATTEMPT
provider failure -> manufacture AuthorizedRequirementTransitionInput
```
