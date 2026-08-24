# C2.02 — Typed Provider Operation / Data Outcome Contract Candidate

Generated: 2026-08-24T07:36:00Z

Status: `CANDIDATE_FOR_INDEPENDENT_OUTCOME_SEMANTICS_REVIEW`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

## 1. Authorization and Stage Boundary

The user explicitly authorized **C2.02 — Typed Provider Operation / Data Outcome Contract** after C2.01R1 Independent Capability Re-Check returned `PASS`.

C2.02 closes only the C2.00 open questions assigned to this stage:

```text
C2.OPEN-004 — detailed structured provider failure/error families
C2.OPEN-005 — exact operation-specific legality rules for PRESENT / NO_DATA / PARTIAL
```

It does **not** construct routing/fallback policy (C2.03), credential/private-state mechanics (C2.04), completeness/certification methodology (C2.05), final C1/C3/C4/C5 wire interfaces (C2.06), final machine schema/validators (C2.07), provider selection, or production adapters.

C2.02 is a candidate contract only. Independent Outcome-Semantics Review has not yet been performed.

## 2. Parent Authority Pins

| Authority | SHA-256 | C2.02 use |
|---|---|---|
| C0 frozen contract | `9585df6c0fbdb2cc40bc38571f8452b51f8ca69c9fd9432b10b87490b08a3b6f` | failure != absence; orthogonal axes; security boundaries |
| C1 Freeze Seal | `438274542570f7398af8622fdb511b85d69fc4c403b246b93a8a593b5d8070a5` | frozen C1 authority |
| C1 final machine schema | `927f1916d3b4b0c0600c1988d6cff0c91dfaaf840b676ce8b6f6f86cb61e52d4` | exact downstream normalization continuity |
| C1.05R1 provider-normalization interface | `71d472e63044b9a7be2c6cc831705ed80dc6a06ccd0ef03e71a0618794bdef63` | FAILED/CANCELLED -> NOT_RUN; SUCCESS outcome constraints |
| C1.05R1 provider-normalization registry | `422010036a00ad0d1fbfa4176ae27f107fec4761a92c0f0ad5b7db29eed2379b` | frozen C1-facing outcome vocabulary |
| C2.00 scope candidate | `b504211651839b1cd9c79a9706f05e1ad9c072f66bfb887aec2a0d65c9b17cf7` | operation/data axis vocabulary and boundaries |
| C2.01R1 repaired registry | `2cba76ffe8e308ade83778e26d24332c4ce019468a73875c36110c7bb5201e95` | endpoint/capability/semantic refs used to interpret outcomes |
| C2.01R1 Independent Re-Check result | `e780ab10b6ed6e6108cc6fafc53ce329827b6135764b993f7a785fdd46e37937` | prior gate PASS |
| C1 archival remediation audit result | `b0cd63ee860aaae0a6b412f922ff50e31a0ab80bf7b98ee9530ba4b356b5fd73` | repository archive continuity only; not new semantics |

## 3. Normative Top-Level Axes

C2.02 preserves the frozen C0/C2.00 operation-status vocabulary exactly:

```text
SUCCESS | FAILED | CANCELLED
```

C2.02 preserves the frozen C0/C2.00 successful-data-outcome vocabulary exactly:

```text
PRESENT | NO_DATA | PARTIAL
```

The axes remain orthogonal. The contract does **not** create a flat combined status enum.

### 3.1 Legality matrix

| operation_status | data_outcome | Legal? | Required semantics |
|---|---|---:|---|
| SUCCESS | PRESENT | YES | >=1 admitted provider observation; no material known partiality |
| SUCCESS | NO_DATA | YES | zero admitted observations; endpoint semantics establish genuine absence; no known partiality |
| SUCCESS | PARTIAL | YES | semantic response usable enough to establish known incomplete scope; explicit partiality evidence retained |
| FAILED | any PRESENT/NO_DATA/PARTIAL | NO | failure envelope required; data outcome absent |
| CANCELLED | any PRESENT/NO_DATA/PARTIAL | NO | cancellation envelope required; data outcome absent |

A `SUCCESS` record MUST carry exactly one data outcome. A `FAILED` or `CANCELLED` record MUST carry no data outcome.

## 4. Provider Operation Outcome Record

Logical record; final wire schema belongs to C2.07:

```text
ProviderOperationOutcome:
  provider_operation_ref
  registry_snapshot_ref
  provider_profile_ref
  endpoint_semantic_profile_ref
  provider_capability_ref
  operation_status
  data_outcome?                # required iff SUCCESS
  failure?                     # required iff FAILED
  cancellation?                # required iff CANCELLED
  matched_absence_signal_refs[]
  matched_partiality_signal_refs[]
  admitted_observation_count
  operation_phase_terminal
  diagnostic_retry_hint?       # non-authoritative advisory only
  material_degradation_refs[]  # if already known; C2.03 owns routing/degradation semantics
```

The registry/profile/endpoint/capability refs MUST obey the C2.01R1 snapshot-stable semantic-ref rules. `provider_operation_ref` identifies an immutable operation outcome instance; exact persistence/wire mechanics are deferred to C2.06/C2.07/C11 boundaries.

## 5. Structured Failure Contract

A failed provider operation is machine-detectable and MUST carry:

```text
ProviderFailure:
  failure_family
  failure_code
  operation_phase
  provider_native_error_code?      # sanitized diagnostic only
  provider_native_status?          # sanitized diagnostic only
  retry_hint?                      # advisory; C3 owns retry policy
  diagnostic_summary?              # non-authoritative; must not contain secrets/private state
```

### 5.1 Core failure families and codes

**`TRANSPORT`**

```text
DNS_RESOLUTION_FAILED
CONNECT_FAILED
TLS_FAILED
CONNECTION_RESET
TRANSPORT_OTHER
```

**`TIMEOUT`**

```text
CONNECT_TIMEOUT
READ_TIMEOUT
TOTAL_TIMEOUT
TIMEOUT_OTHER
```

**`AUTHENTICATION`**

```text
CREDENTIAL_MISSING
CREDENTIAL_INVALID
CREDENTIAL_EXPIRED
AUTHENTICATION_OTHER
```

**`AUTHORIZATION`**

```text
ENTITLEMENT_INSUFFICIENT
SCOPE_INSUFFICIENT
ACCESS_DENIED
AUTHORIZATION_OTHER
```

**`RATE_LIMIT`**

```text
RATE_LIMIT_REJECTED
RATE_LIMIT_EXHAUSTED
RATE_LIMIT_OTHER
```

**`REQUEST_REJECTED`**

```text
REQUEST_SCHEMA_REJECTED
REQUEST_PARAMETER_REJECTED
REQUEST_SEMANTIC_REJECTED
REQUEST_REJECTED_OTHER
```

**`CAPABILITY_UNAVAILABLE`**

```text
ENDPOINT_UNAVAILABLE
CAPABILITY_NOT_SUPPORTED
FEATURE_DISABLED
CAPABILITY_UNAVAILABLE_OTHER
```

**`PROVIDER_SERVER`**

```text
PROVIDER_5XX
PROVIDER_MAINTENANCE
PROVIDER_OVERLOADED
PROVIDER_SERVER_OTHER
```

**`PROVIDER_UPSTREAM`**

```text
PROVIDER_DEPENDENCY_FAILED
PROVIDER_DEPENDENCY_TIMEOUT
PROVIDER_UPSTREAM_OTHER
```

**`RESPONSE_PROTOCOL`**

```text
UNEXPECTED_STATUS
UNEXPECTED_CONTENT_TYPE
MALFORMED_PROTOCOL_ENVELOPE
RESPONSE_PROTOCOL_OTHER
```

**`RESPONSE_DECODING`**

```text
BODY_DECODE_FAILED
STRUCTURE_PARSE_FAILED
RESPONSE_DECODING_OTHER
```

**`RESPONSE_SEMANTIC_INVALID`**

```text
RESPONSE_SCHEMA_INVALID
PROVIDER_ERROR_ENVELOPE
ABSENCE_SIGNAL_AMBIGUOUS
PARTIALITY_SIGNAL_AMBIGUOUS
RESPONSE_SEMANTIC_OTHER
```

**`ADAPTER_INTERNAL`**

```text
ADAPTER_BUG
ADAPTER_INVARIANT_VIOLATION
ADAPTER_INTERNAL_OTHER
```

**`UNKNOWN_PROVIDER_FAILURE`**

```text
UNKNOWN_FAILURE
```

The `(failure_family, failure_code)` pair is closed at C2.02 candidate level. Unknown/unmapped provider failures map to `UNKNOWN_PROVIDER_FAILURE / UNKNOWN_FAILURE`; adapters MUST NOT invent ad-hoc failure families that bypass review.

### 5.2 Operation phase

```text
PRE_DISPATCH
CONNECT
REQUEST_SEND
WAIT_RESPONSE
RESPONSE_HEADERS
RESPONSE_BODY
DECODE
SEMANTIC_VALIDATE
ADAPTER_POST_PROCESS
```

The phase is diagnostic/provenance state; it does not grant C3 retry authority or C4 temporal meaning.

## 6. Failure Versus Absence Decision Rules

The following MUST be `FAILED`, never `SUCCESS + NO_DATA`:

- DNS/connect/TLS/reset failures;
- provider/client timeouts;
- missing/invalid/expired credentials;
- authorization/entitlement denial;
- rate-limit rejection/exhaustion;
- request rejection where the semantic request did not successfully execute;
- endpoint/capability unavailability;
- provider 5xx/maintenance/overload failures;
- upstream-dependency failures reported by the provider;
- unexpected protocol/status/content-type responses;
- decode/parse/schema failures;
- provider error envelopes, even when transported under HTTP 2xx;
- ambiguous absence/partiality signaling that prevents deterministic outcome classification;
- adapter invariant violations.

### 6.1 HTTP 404 and analogous provider-native “not found” signals

A transport/status code such as HTTP 404 has **no universal C2 meaning**. It may represent:

- genuine record absence;
- endpoint/path failure;
- authorization obfuscation;
- invalid request semantics;
- provider-specific error envelope.

It becomes `SUCCESS + NO_DATA` **only** when the pinned endpoint semantic profile explicitly classifies that exact provider-native signal as an absence signal for the attempted semantic operation and no higher-priority failure/partiality condition applies. Otherwise it is a typed failure or remains semantically invalid and fails closed.

## 7. Successful Data Outcome Rules

### 7.1 `PRESENT`

`SUCCESS + PRESENT` requires all of:

1. the operation completed successfully under the pinned endpoint semantics;
2. at least one provider observation passed the provider-validation boundary and is admitted for downstream normalization;
3. no material partiality signal/truncation/incomplete-pagination condition is known;
4. absence is not simultaneously asserted for the same semantic scope.

`PRESENT` is not C1 canonical truth and not C5 verification.

### 7.2 `NO_DATA`

`SUCCESS + NO_DATA` requires all of:

1. successful operation semantics;
2. zero admitted provider observations for the requested semantic scope;
3. one or more endpoint-profile-authorized provider-native absence signals, or an endpoint semantic rule that explicitly defines a successful empty collection as genuine absence for that operation;
4. no material partiality signal or known missing segment;
5. the matched absence semantics are retained in replay lineage.

`NO_DATA` does **not** automatically imply C1 `NO_MATCH`, C4 PIT-safe absence, C5 verification, or C2.05 completeness certification.

### 7.3 `PARTIAL`

`SUCCESS + PARTIAL` requires:

1. enough response semantics were successfully decoded/validated to make the response usable as a successful provider result; and
2. explicit evidence shows the result scope is incomplete.

Partiality evidence may include pinned endpoint-semantic interpretations of:

- provider-native partial-result flags;
- incomplete pagination/cursor traversal;
- provider-declared result caps/limits;
- truncated response with semantically valid admitted records;
- missing required segments explicitly identified by provider semantics;
- successful degraded sub-results where the operation contract declares the overall data scope incomplete.

`PARTIAL` MAY contain zero or more admitted observations. Zero-observation `PARTIAL` is legal only with explicit partiality evidence; it is never inferred from an empty body alone.

If the body cannot be decoded/validated enough to know what was returned, the operation is `FAILED`, not `PARTIAL`.

## 8. Pagination, Truncation and Collection Semantics

- A page that contains observations is not automatically `PRESENT` if required pagination remains incomplete.
- An exhausted cursor/end-of-collection signal may support `PRESENT` or `NO_DATA` only under pinned endpoint semantics.
- Missing pages, broken cursors, provider caps or explicit truncation make the successful data outcome `PARTIAL` when the decoded material remains semantically usable; otherwise the operation is `FAILED`.
- C2.05 later owns whether any completed collection is complete enough to support load-bearing absence/uniqueness claims.

## 9. Cancellation Contract

`CANCELLED` means the attempted provider operation did not reach an outcome eligible for provider-data classification because execution was explicitly cancelled.

Logical cancellation record:

```text
ProviderCancellation:
  cancellation_origin: CALLER | ORCHESTRATOR | DEADLINE_CONTROLLER | SHUTDOWN | SUPERSEDED_REQUEST | UNKNOWN
  operation_phase
  diagnostic_summary?
```

Rules:

- cancellation is distinct from failure;
- a provider/client timeout is normally a `FAILED / TIMEOUT` outcome unless an external controller explicitly cancelled the operation;
- bytes received before cancellation may be retained only as diagnostic/quarantined ingress material under later security/persistence rules; they MUST NOT be emitted as provider observations for C1 normalization from a `CANCELLED` operation;
- C1 normalization is `NOT_RUN` for `CANCELLED`.

## 10. Retry Hint Boundary

C2.02 MAY record a diagnostic retry hint:

```text
UNKNOWN
LIKELY_TRANSIENT
LIKELY_PERMANENT
PRECONDITION_CHANGE_REQUIRED
PROVIDER_DIRECTED_DELAY
```

This is **not a retry decision**. C3 exclusively owns retry/backoff/quota/budget/coalescing/freshness policy. A provider `Retry-After` or equivalent may be preserved as sanitized diagnostic metadata later, but C2.02 does not schedule execution.

## 11. Replay and Provenance

Every material operation outcome retains enough pinned semantic context to explain the classification:

```text
registry_snapshot_ref
provider_profile_ref
endpoint_semantic_profile_ref
provider_capability_ref
matched_absence_signal_refs[]
matched_partiality_signal_refs[]
material_degradation_refs[]  # when applicable; C2.03 semantics later
```

No floating `latest/current` semantic alias may be the load-bearing replay reference.

Failure/cancellation records do not erase the attempted endpoint/capability lineage. Later C2.03 fallback cannot rewrite a failed primary attempt as if only the fallback occurred.

## 12. Frozen C1.05R1 Consequences

C2.02 preserves exactly:

```text
FAILED      -> C1 normalization NOT_RUN
CANCELLED   -> C1 normalization NOT_RUN
SUCCESS + NO_DATA   -> does not automatically establish C1 NO_MATCH
SUCCESS + PARTIAL   -> valid admitted observations may normalize, but missing data cannot prove absence/uniqueness
```

A positive exact C1 mapping does not automatically require universe-wide completeness when exactness does not depend on absence. C2.05 owns completeness/coverage attestations when absence/uniqueness reasoning depends on them.

## 13. Ownership Boundaries

C2.02 does not absorb:

- **C1:** canonical identity, normalization result, resolution result;
- **C3:** cache, quota, retry/backoff, freshness, coalescing, LKG;
- **C4:** `available_from`, revision, exact PIT/reconstructability;
- **C5:** source fitness, verification, conflict, truth status;
- **C11:** persistence implementation;
- **C6/C7:** capability grants, trusted intent, workflow/side-effect authority.

Provider-native timestamps, retry hints, error text and status codes remain provider/operation diagnostics and do not acquire those downstream meanings by implication.

## 14. Fail-Closed Invalid Combinations

The following are invalid and MUST be rejected by C2.07 validators rather than coerced:

```text
FAILED + PRESENT
FAILED + NO_DATA
FAILED + PARTIAL
CANCELLED + PRESENT
CANCELLED + NO_DATA
CANCELLED + PARTIAL
SUCCESS without exactly one data outcome
SUCCESS + NO_DATA + admitted_observation_count > 0
SUCCESS + NO_DATA without certified endpoint absence semantics
SUCCESS + PRESENT with known material partiality
SUCCESS + PARTIAL inferred solely from empty response
FAILED without structured failure envelope
CANCELLED without structured cancellation envelope
unknown failure family silently treated as NO_DATA
parse/schema error converted to PARTIAL
provider error envelope converted to empty success
```

## 15. C2.00 Open-Question Status After Candidate Construction

```text
C2.OPEN-004 = CANDIDATE_CLOSED_PENDING_INDEPENDENT_REVIEW
C2.OPEN-005 = CANDIDATE_CLOSED_PENDING_INDEPENDENT_REVIEW
C2.OPEN-006..015 = OPEN_UNCHANGED
```

Independent Outcome-Semantics Review is required before C2.02 can be described as review-passed. No C2.03 construction is authorized by this candidate.
