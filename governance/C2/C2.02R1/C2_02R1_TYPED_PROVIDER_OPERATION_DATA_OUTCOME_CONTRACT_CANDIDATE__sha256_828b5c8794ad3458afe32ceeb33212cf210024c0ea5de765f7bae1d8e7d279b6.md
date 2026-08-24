# C2.02R1 — Typed Provider Operation / Data Outcome Scoped Repair Candidate

Generated: 2026-08-24T08:36:46Z

Status: `SCOPED_REPAIR_CANDIDATE_PENDING_INDEPENDENT_OUTCOME_SEMANTICS_RECHECK`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

## 1. Repair Authorization and Scope

The user explicitly authorized **C2.02R1 scoped repair** after C2.02 Independent Outcome-Semantics Review returned `FAIL / REPAIR_REQUIRED`.

This successor candidate repairs only:

```text
C2OUT-B01 — compound terminal-condition precedence is not deterministic
C2OUT-B02 — terminal phase duplicated without a coherence invariant
C2OUT-B03 — non-success admitted-observation semantics under-specified
C2OUT-B04 — material partiality lacks a deterministic scope predicate
```

It also closes the three closely related non-blocking consistency notes N01..N03 without expanding stage ownership.

C2.03 routing/fallback, C2.04 credential/private-state mechanics, C2.05 certification/completeness methodology, C2.06 cross-contract wire mapping, C2.07 final schema/validators, provider selection, and production adapters remain outside this repair.

The original C2.02 candidate remains immutable historical evidence. This R1 document is its successor repair candidate; it is **not** independently approved or frozen.

## 2. Exact Parent Pins

```text
C2.02 normative contract    eb7636409e2dcdfe688a089c0dabceacd300ad8dee49febfbc6cdc149b96d7ef
C2.02 logical model         607d3839d66ab0cae9bf8192f38135dfdde05f112a1768d33360415cda229ed4
C2.02 acceptance delta      2d8233a17fa2ad2afc0ff386e4975869d138bfafdf7025a17eb2be5556fb10ed
C2.02 decision ledger       9a84cda469a79b9f807a45514744fd6b905fe88ca0607ef3fd25f2b6bcd0f5ae
C2.02 independent review    5626d1eb030c9132516458f38a81dd2753f34641b73bbb139b3a8f7cdf028cd1
C2.02 review result         192d2ff5406697fccfc475e63abfc0029cc60a6a4d59760e4ed07c17759e5216
C1.05R1 interface           71d472e63044b9a7be2c6cc831705ed80dc6a06ccd0ef03e71a0618794bdef63
C2.01R1 registry            2cba76ffe8e308ade83778e26d24332c4ce019468a73875c36110c7bb5201e95
C2.01R1 independent result  e780ab10b6ed6e6108cc6fafc53ce329827b6135764b993f7a785fdd46e37937
```

All C2.02 rules not explicitly repaired below are inherited unchanged.

## 3. R1 Terminal Classification State Machine — Repair for C2OUT-B01

### 3.1 Candidate terminal conditions

An adapter MUST first collect every outcome-defining condition that is actually established by the pinned provider/endpoint semantics for the operation attempt. A condition is not permitted to become terminal merely because raw text, an SDK exception name, or an HTTP code resembles a known condition.

Candidate classes are:

```text
TYPED_FAILURE
EXPLICIT_CANCELLATION
MATERIAL_PARTIALITY
AUTHORIZED_ABSENCE
PRESENT_OBSERVATIONS
```

A successful data candidate is **provisional until required decoding and semantic validation complete**. Therefore an observed 404-like absence signal, partiality flag, or returned record does not outrank a later decode/semantic-validation failure required to interpret that same response.

### 3.2 Fixed operation-phase order

For deterministic primary-cause selection, C2.02R1 freezes the phase order:

```text
0 PRE_DISPATCH
1 CONNECT
2 REQUEST_SEND
3 WAIT_RESPONSE
4 RESPONSE_HEADERS
5 RESPONSE_BODY
6 DECODE
7 SEMANTIC_VALIDATE
8 ADAPTER_POST_PROCESS
```

For failure/cancellation candidates, the candidate phase is the phase in which that terminal condition is established. Successful-data candidates terminalize only at `SEMANTIC_VALIDATE` after all required provider-response validation has passed.

### 3.3 Deterministic primary terminal condition

The primary terminal condition is selected as follows:

1. Resolve all load-bearing provider semantic refs against the same pinned registry snapshot.
2. Discard any condition not established by those pinned semantics.
3. If one or more `TYPED_FAILURE` or `EXPLICIT_CANCELLATION` candidates exist, choose the candidate with the **lowest phase ordinal**.
4. If multiple non-success candidates share the same phase ordinal, apply this fixed class tie-break:

```text
ADAPTER_INTERNAL / invariant failure
> EXPLICIT_CANCELLATION
> other TYPED_FAILURE
```

5. If more than one non-adapter typed failure remains at the same phase, select the lexicographically smallest closed `(failure_family, failure_code)` tuple as the primary diagnostic cause. All other established terminal conditions MUST remain available as secondary sanitized terminal diagnostics; they cannot be erased or used to change the primary typed outcome.
6. Only when no non-success terminal candidate exists may successful-data classification run, using the exact order in §6 below.

The lexical tie-break is an audit determinism rule, not a claim that one provider failure is economically or operationally more important than another.

### 3.4 Required adversarial classifications

```text
explicit cancellation + timeout in same phase
  -> CANCELLED (explicit cancellation wins same-phase tie)

404-like authorized absence + provider error envelope
  -> FAILED (successful absence remains provisional; typed provider error prevents success)

partiality/truncation evidence + decode failure required to interpret payload
  -> FAILED/RESPONSE_DECODING

rate-limit signal + provider generic error envelope in same phase
  -> FAILED; primary family/code selected by fixed tuple tie-break; secondary condition retained
```

No adapter-local scheduling race may alter these results when the same candidate terminal-condition set and pinned semantic state are supplied.

## 4. Single Terminal Phase Source — Repair for C2OUT-B02

`ProviderOperationOutcome.operation_phase_terminal` is the **single authoritative terminal phase**.

R1 logical nested records are:

```text
ProviderFailure:
  failure_family
  failure_code
  provider_native_error_code?
  provider_native_status?
  diagnostic_summary?

ProviderCancellation:
  cancellation_origin
  diagnostic_summary?
```

Nested `ProviderFailure.operation_phase` and `ProviderCancellation.operation_phase` are removed from the successor logical contract.

For any legacy/intermediate representation that temporarily duplicates a nested phase before C2.07 final serialization, exact equality with `operation_phase_terminal` is mandatory; disagreement is `ADAPTER_INTERNAL / ADAPTER_INVARIANT_VIOLATION` and MUST fail closed.

## 5. Non-Success Observation Admission — Repair for C2OUT-B03

The term **admitted observation** means a provider observation eligible to cross the C2 provider-validation boundary toward C1 normalization.

Therefore:

```text
FAILED:
  admitted_observation_count = 0
  C1 normalization = NOT_RUN

CANCELLED:
  admitted_observation_count = 0
  C1 normalization = NOT_RUN
```

Bytes or decoded fragments observed before failure/cancellation may later be retained as permitted diagnostic/quarantined/raw-ingress material under C2.04/C11 rules, but they are **not admitted observations** and MUST NOT increment `admitted_observation_count`.

If semantically usable records are intentionally admitted while the requested provider-result scope is incomplete, the correct top-level state is `SUCCESS + PARTIAL`, not `FAILED` or `CANCELLED`.

## 6. Deterministic Partiality Materiality — Repair for C2OUT-B04

### 6.1 Attempted response scope

Every operation outcome MUST retain:

```text
attempted_response_semantic_refs[]
```

This is the snapshot-stable set of response-semantic refs that the concrete provider operation attempt required, after applying the selected `provider_capability_ref`, pinned endpoint semantic profile, and explicit request/query semantics. It is provider-response scope only; it does not define C1 identity scope, C4 temporal scope, C5 evidence fitness, or C2.05 completeness.

Every member MUST be an allowed C2.01R1 response-closure ref kind and resolve under the same `registry_snapshot_ref` used by the operation outcome.

### 6.2 Partiality signal scope contract

A load-bearing provider-native partiality signal semantic consumed by C2.02 MUST resolve to one of these scope modes:

```text
WHOLE_ATTEMPT
RESPONSE_SEMANTIC_SET
```

For `RESPONSE_SEMANTIC_SET`, the pinned signal semantics MUST provide a non-empty `affected_response_semantic_refs[]`, each of an allowed response-closure kind.

Define exactly:

```text
is_material_partiality(signal, attempt) =
  true,  if signal.scope_mode == WHOLE_ATTEMPT
  true,  if signal.scope_mode == RESPONSE_SEMANTIC_SET
         and intersection(signal.affected_response_semantic_refs,
                          attempt.attempted_response_semantic_refs) is non-empty
  false, if signal.scope_mode == RESPONSE_SEMANTIC_SET
         and the intersection is empty
```

If the pinned signal semantics do not provide enough information to evaluate this predicate deterministically, the operation MUST NOT be classified as `PRESENT` or `NO_DATA`. It fails closed as:

```text
FAILED / RESPONSE_SEMANTIC_INVALID / PARTIALITY_SCOPE_UNRESOLVED
```

R1 adds `PARTIALITY_SCOPE_UNRESOLVED` to the closed `RESPONSE_SEMANTIC_INVALID` failure-code family.

### 6.3 Material/non-material lineage

The outcome retains:

```text
matched_partiality_signal_refs[]
material_partiality_signal_refs[]
```

with the invariant:

```text
material_partiality_signal_refs ⊆ matched_partiality_signal_refs
```

A matched but scope-disjoint signal remains replay-visible but does not force `PARTIAL`.

### 6.4 Successful data classification order

After §3 proves no FAILED/CANCELLED terminal condition exists:

1. Evaluate materiality for every matched partiality signal.
2. If any material partiality signal exists, classify `SUCCESS + PARTIAL` if decoded material is semantically usable; otherwise `FAILED`.
3. If no material partiality exists and `admitted_observation_count > 0`, classify `SUCCESS + PRESENT`, unless a same-scope authorized absence assertion simultaneously exists; such a contradiction fails closed as `RESPONSE_SEMANTIC_INVALID`.
4. If no material partiality exists, admitted count is zero, and pinned endpoint-profile-authorized absence semantics establish genuine absence for the attempted scope, classify `SUCCESS + NO_DATA`.
5. Otherwise zero observations without material partiality and without authorized absence semantics fail closed; they are not guessed into `NO_DATA`.

This yields deterministic `PRESENT / NO_DATA / PARTIAL` classification for the same pinned operation attempt.

## 7. Retry Diagnostic Normalization — N01

C2.02R1 retains exactly one authoritative retry advisory field:

```text
diagnostic_retry_hint?
```

at `ProviderOperationOutcome` level.

`ProviderFailure.retry_hint` is removed from the successor logical contract. The field remains diagnostic only; C3 exclusively owns retry/backoff/quota/budget/coalescing/freshness policy.

## 8. Endpoint Absence Wording — N03

The original phrase `certified endpoint absence semantics` is replaced by:

```text
pinned endpoint-profile-authorized absence semantics
```

This means only that the exact pinned C2.01 endpoint semantic state defines the provider-native signal as genuine absence for the attempted operation. It is **not** a C2.05 completeness/certification attestation and cannot by itself support load-bearing universe completeness, C1 `NO_MATCH`, C4 PIT-safe absence, or C5 verification.

## 9. Frozen C1 Serialization Seam — N02 / Mandatory C2.06 Obligation

C2.02R1 does not change frozen C1 serialization. C2.02 semantic truth remains:

```text
FAILED    -> no successful C2 data outcome
CANCELLED -> no successful C2 data outcome
```

The frozen C1.07R2 `OutcomeAxes` schema has a broader serialization surface, including a contract vector where `FAILED + provider_data_outcome: NO_DATA` is schema-valid. C2.06 MUST define a lossless cross-contract representation that preserves C2.02 meaning and MUST NOT reinterpret a failed operation as genuine provider `NO_DATA`.

If frozen C1 serialization cannot encode the distinction without semantic distortion, C2.06 MUST surface a governance incompatibility rather than inventing meaning.

This obligation is recorded now but remains C2.06-owned.

## 10. Repaired Invalid-Combination Rules

C2.07 validators MUST eventually reject at least:

```text
FAILED with admitted_observation_count != 0
CANCELLED with admitted_observation_count != 0
FAILED/CANCELLED with any successful data_outcome
nested terminal phase that differs from operation_phase_terminal
PRESENT or NO_DATA when any matched partiality signal has unresolved materiality
PRESENT or NO_DATA with non-empty material_partiality_signal_refs
material_partiality_signal_refs not subset of matched_partiality_signal_refs
PARTIAL without >=1 material_partiality_signal_ref or other explicit operation-scope incomplete condition
NO_DATA without pinned endpoint-profile-authorized absence semantics
conflicting same-scope PRESENT observations and authorized absence assertion
contradictory duplicate retry advisory fields in any legacy/intermediate representation
```

## 11. Repair Status

```text
C2OUT-B01 = ADDRESSED_NOT_CLOSED
C2OUT-B02 = ADDRESSED_NOT_CLOSED
C2OUT-B03 = ADDRESSED_NOT_CLOSED
C2OUT-B04 = ADDRESSED_NOT_CLOSED

C2.OPEN-004 = REPAIRED_CANDIDATE_PENDING_INDEPENDENT_RECHECK
C2.OPEN-005 = REPAIRED_CANDIDATE_PENDING_INDEPENDENT_RECHECK
C2.OPEN-006..015 = OPEN_UNCHANGED
```

Only an Independent Outcome-Semantics Re-Check may close B01..B04 or pass C2.02.

## 12. Stop State

`C2.02R1 scoped repair construction complete as candidate.`

Next required gate: **Independent Outcome-Semantics Re-Check**.

C2.03 remains `NOT STARTED / NOT AUTHORIZED`. Production implementation and external/PAPER/LIVE side effects remain `NOT AUTHORIZED`.
