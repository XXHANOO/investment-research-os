# C2.02R2 — Narrow Outcome-Semantics Repair Candidate

Generated: 2026-08-24T09:07:53Z

Status: `NARROW_REPAIR_CANDIDATE_PENDING_INDEPENDENT_OUTCOME_SEMANTICS_RECHECK`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

## 1. Authorization and exact repair scope

The user explicitly authorized **C2.02R2 narrow repair** after the C2.02R1 Independent Outcome-Semantics Re-Check returned `FAIL` with only two remaining blocking findings:

```text
C2OUT-B01 — multiple same-phase EXPLICIT_CANCELLATION candidates lack a total primary-origin rule
C2OUT-B04 — attempted_response_semantic_refs[] lacks an exact deterministic derivation rule
```

This successor candidate repairs only those two residual determinism gaps. C2OUT-B02 and C2OUT-B03 remain closed by the R1 independent re-check and are not reopened.

C2.03 routing/fallback, C2.04 credential/private-state mechanics, C2.05 completeness/certification methodology, C2.06 cross-contract serialization, C2.07 final machine schema/validators, concrete provider selection, and production adapters remain outside this repair.

The C2.02 and C2.02R1 candidates remain immutable historical evidence. This R2 document is a successor repair candidate only; it is **not independently approved or frozen**.

## 2. Exact parent pins

```text
C2.02R1 repaired contract          828b5c8794ad3458afe32ceeb33212cf210024c0ea5de765f7bae1d8e7d279b6
C2.02R1 repaired logical model     89d7905961776e47f637c6460bddda33067421328bdb205a30bc60d5901735dc
C2.02R1 repair acceptance delta    f548d2041b984c1b881c839689fe7c16fd6d4baa1e9b6f634cb1f2dca6c4877f
C2.02R1 repair decision ledger     369248cf6e25169e1b7168773059e36e2cf5d2cdcd7a0ed1fb85ac62988a4bbf
C2.02R1 independent re-check       0ad9f15e5c0f15b80136f737f2c8dceda318222813d1515622e29658e75ea4db
C2.02R1 re-check result            af007a9b05e3a7129d662ae7b4845efdd146d7a0804448d733a251326facc9d6
C2.01R1 capability registry        2cba76ffe8e308ade83778e26d24332c4ce019468a73875c36110c7bb5201e95
C2.01R1 independent result         e780ab10b6ed6e6108cc6fafc53ce329827b6135764b993f7a785fdd46e37937
C1.05R1 normalization interface    71d472e63044b9a7be2c6cc831705ed80dc6a06ccd0ef03e71a0618794bdef63
```

All C2.02R1 semantics not explicitly repaired below are inherited unchanged.

## 3. Total same-phase explicit-cancellation determinism — residual repair for C2OUT-B01

### 3.1 Closed cancellation-origin domain and canonical ordinal

C2.02R2 freezes the cancellation-origin domain and a deterministic audit ordinal:

```text
0 CALLER
1 ORCHESTRATOR
2 DEADLINE_CONTROLLER
3 SHUTDOWN
4 SUPERSEDED_REQUEST
5 UNKNOWN
```

This ordinal is **only a deterministic replay tie-break**. It does not claim causal, operational, economic, or policy importance and grants no cancellation authority.

No adapter may add a private cancellation-origin value. An unrecognized origin is represented as `UNKNOWN`; it cannot create a new enum member.

### 3.2 Primary and secondary cancellation-origin contract

When the terminal classifier reaches a same-phase `EXPLICIT_CANCELLATION` tie containing one or more established cancellation origins, define exactly:

```text
known_origins = unique(origins - {UNKNOWN})

if known_origins is non-empty:
    primary_cancellation_origin = member of known_origins with the lowest canonical ordinal
else:
    primary_cancellation_origin = UNKNOWN

secondary_cancellation_origins =
    all other unique established origins,
    excluding primary_cancellation_origin,
    sorted by canonical ordinal
```

The successor `ProviderCancellation` logical record therefore carries:

```text
ProviderCancellation:
  cancellation_origin                  # authoritative primary origin
  secondary_cancellation_origins[]     # replay lineage; canonical order; may be empty
  diagnostic_summary?
```

`cancellation_origin` retains the R1 field name for compatibility but means the **authoritative primary cancellation origin selected by this exact rule**.

Invariants:

```text
secondary_cancellation_origins contains no duplicates
secondary_cancellation_origins excludes cancellation_origin
secondary_cancellation_origins is canonical-ordinal sorted
UNKNOWN is primary only when no known origin is established
all established same-phase cancellation origins are represented by primary ∪ secondary
```

If an implementation observes a same-phase explicit-cancellation candidate set but cannot reconstruct the complete origin set deterministically, classification fails closed as:

```text
FAILED / ADAPTER_INTERNAL / ADAPTER_INVARIANT_VIOLATION
```

It MUST NOT select whichever cancellation happened to win a local scheduling race.

### 3.3 R2 adversarial cancellation vectors

```text
WAIT_RESPONSE: CALLER + ORCHESTRATOR
  -> CANCELLED
  -> cancellation_origin = CALLER
  -> secondary_cancellation_origins = [ORCHESTRATOR]

WAIT_RESPONSE: DEADLINE_CONTROLLER + SHUTDOWN + UNKNOWN
  -> CANCELLED
  -> cancellation_origin = DEADLINE_CONTROLLER
  -> secondary_cancellation_origins = [SHUTDOWN, UNKNOWN]

WAIT_RESPONSE: UNKNOWN + UNKNOWN
  -> CANCELLED
  -> cancellation_origin = UNKNOWN
  -> secondary_cancellation_origins = []
```

Given the same pinned terminal-candidate multiset, all conforming adapters MUST emit the same primary and secondary cancellation-origin representation.

## 4. Exact attempted-response semantic scope — residual repair for C2OUT-B04

### 4.1 Replay-retained attempt requirement

For every dispatched provider operation attempt, the exact normalized C2.01 `CapabilityRequirement` used to prove the selected `provider_capability_ref` compatible MUST be replay-retained as `R` (embedded value or content-addressed equivalent; final wire representation is deferred to C2.07).

At minimum `R` contains the C2.01R1 fields:

```text
access_pattern_family
required_observation_family_refs[]
required_query_semantic_refs[]
required_response_semantic_refs[]
required_semantic_feature_refs[]
```

All refs in `R` resolve against the same pinned registry snapshot `S` as the operation outcome. `compatible(R, P, S)` under the C2.01R1 exact predicate MUST be true before dispatch.

C2.02R2 does not redefine C2.01 compatibility; it consumes the exact C2.01R1 contract.

For C2.02 outcome semantics, `R` is the **load-bearing normalized request boundary**. Raw natural-language intent, SDK argument objects, or an unnormalized query document are not alternative inputs to attempted-scope derivation. If the upstream request/capability-requirement boundary cannot produce one unique canonical `R` for the pinned request semantic state, provider dispatch is forbidden and the operation fails closed under §4.3. C2.02 does not choose among competing `R` values.

### 4.2 Exact derivation

Let:

```text
S = the operation's pinned registry snapshot
P = exact_resolve(provider_capability_ref, S)
E = exact_resolve(P.endpoint_semantic_profile_ref, S)
R = exact replay-retained CapabilityRequirement for this operation attempt
```

Then define exactly:

```text
attempted_response_semantic_refs(P, E, R, S) = canonical_set(
    { E.response_semantics.response_semantic_ref }
    ∪ set(P.required_response_semantic_refs)
    ∪ set(R.required_response_semantic_refs)
)
```

where `canonical_set` means:

```text
1. every member uses one of the C2.01R1 allowed response-closure kinds;
2. every member exact-resolves under S with matching ref_kind and content_sha256;
3. equality/deduplication uses the full C2 stable-ref identity, not logical_id alone;
4. members are serialized in deterministic ascending order of
   (ref_kind, logical_id, semantic_revision, content_sha256).
```

The stored `attempted_response_semantic_refs[]` MUST equal that derived set exactly. It is **not caller-supplied free-form data** and cannot contain extra refs "for safety" or omit required refs "for convenience".

### 4.3 Query-dependent response requirements

C2.02R2 does not recursively infer response semantics from query-semantic definitions.

Instead, before dispatch, every explicit request/query option that changes the response semantics required for the concrete attempt MUST already be materialized into `R.required_response_semantic_refs[]` by the request/capability-requirement construction boundary.

Therefore:

```text
query semantic ref alone is not permission to guess response scope
provider-wide defaults are not imported
transitive semantic dereference is not performed
endpoint documentation/SDK names are not semantic authority
```

If the pinned request/query state contains a condition that can alter required response semantics but the corresponding exact response-semantic requirement cannot be deterministically materialized in `R.required_response_semantic_refs[]` before dispatch, the attempt is not contract-provable and MUST fail closed before provider dispatch as:

```text
FAILED
operation_phase_terminal = PRE_DISPATCH
failure_family = RESPONSE_SEMANTIC_INVALID
failure_code = ATTEMPT_RESPONSE_SCOPE_UNRESOLVED
admitted_observation_count = 0
```

This failure is not provider NO_DATA and grants no C3 retry policy.

### 4.4 Relationship to C2.01R1 one-hop closure

The R2 derivation is intentionally narrower than `effective_response_semantic_refs(P,S)`.

`effective_response_semantic_refs(P,S)` is the C2.01R1 **capability compatibility satisfaction set**. It can include endpoint field/grouping/pagination/provider-signal semantics that the endpoint supports but that a particular operation does not require.

`attempted_response_semantic_refs[]` is the **concrete operation-required response scope** used by C2.02 partiality materiality. It therefore includes only:

```text
endpoint primary response semantic
+ capability-mandatory response semantics
+ concrete requirement response semantics
```

No other member of the broader C2.01R1 one-hop closure enters attempted scope unless it is explicitly required by `P.required_response_semantic_refs[]` or `R.required_response_semantic_refs[]`.

### 4.5 Determinism property

For any two conforming implementations given the same exact tuple:

```text
(S, provider_capability_ref, P.endpoint_semantic_profile_ref, R)
```

they MUST derive byte-equivalent canonical `attempted_response_semantic_refs[]`.

Consequently, the R1 material-partiality predicate receives a deterministic load-bearing input set.

## 5. R2 effect on R1 successful-data classification

The R1 materiality rule remains unchanged:

```text
WHOLE_ATTEMPT -> material
RESPONSE_SEMANTIC_SET -> material iff
    intersection(affected_response_semantic_refs,
                 attempted_response_semantic_refs) != empty
```

R2 only closes how `attempted_response_semantic_refs[]` is derived.

If attempted scope cannot be derived exactly, successful-data classification MUST NOT run. The operation fails at `PRE_DISPATCH` with `ATTEMPT_RESPONSE_SCOPE_UNRESOLVED`.

## 6. Explicit non-expansion boundaries

This R2 repair does not define:

- C2.03 provider routing, retry/fallback ordering, or degradation policy;
- C3 retry/backoff/quota/cache/freshness policy;
- C2.04 credentials/private-state mechanics;
- C2.05 completeness/coverage certification methodology;
- C4 PIT/available_from/revision semantics;
- C5 source fitness/verification/conflict semantics;
- C2.06 final C1/C2 serialization mapping;
- C2.07 JSON Schema/validator encoding;
- provider/vendor priority or production adapter enablement;
- PAPER/LIVE side-effect authority.

## 7. Repair status

```text
C2OUT-B01 = ADDRESSED_NOT_CLOSED
C2OUT-B02 = CLOSED_BY_R1_INDEPENDENT_RECHECK
C2OUT-B03 = CLOSED_BY_R1_INDEPENDENT_RECHECK
C2OUT-B04 = ADDRESSED_NOT_CLOSED

C2.OPEN-004 = REPAIRED_CANDIDATE_PENDING_INDEPENDENT_RECHECK
C2.OPEN-005 = REPAIRED_CANDIDATE_PENDING_INDEPENDENT_RECHECK
C2.OPEN-006..015 = OPEN_UNCHANGED
```

Only an Independent Outcome-Semantics Re-Check may close B01/B04 and C2.OPEN-004/005 at the C2.02 contract level.
