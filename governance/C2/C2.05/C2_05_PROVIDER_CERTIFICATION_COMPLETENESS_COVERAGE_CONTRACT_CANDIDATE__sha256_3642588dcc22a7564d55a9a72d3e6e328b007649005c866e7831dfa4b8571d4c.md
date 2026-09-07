# C2.05 — Provider Certification / Completeness / Coverage Attestations Candidate

Generated: 2026-09-07T06:01:18Z

Status: `CANDIDATE_FOR_C2_05_INDEPENDENT_CERTIFICATION_REVIEW`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

## 1. Authorization, scope, and authority

The user explicitly authorized **C2.05 — Provider Certification / Completeness / Coverage Attestations** after C2.04R1 Independent Security-Boundary Re-Check returned `PASS`.

C2.05 defines C2-owned semantic contracts for:

- provider/capability/endpoint certification state;
- replayable certification evidence requirements;
- deterministic invalidation/suspension/supersession semantics;
- exact completeness/coverage scope identity;
- closed coverage-method families and method-specific exhaustion requirements;
- load-bearing coverage attestations capable of supporting later C1 absence/uniqueness reasoning;
- snapshot-stable operational certification applicability without inventing C4 market-time/PIT semantics.

C2.05 does **not**:

- choose or enable concrete providers/vendors;
- implement provider adapters;
- define route priority, retry, backoff, quota, cache, freshness, coalescing, or LKG;
- define C4 `available_from`, revision, event-time visibility, PIT reconstructability, or historical truth;
- define C5 evidence fitness, verification, independence, source ranking, or conflict adjudication;
- grant C6 capability, trusted intent, destination/egress, or side-effect authority;
- define C7 orchestration/budgets/cancellation;
- choose C11 persistence implementation;
- define final cross-contract wire serialization;
- freeze or release C2.

C2.05 is contract construction only. It cannot self-approve. `C2.OPEN-009..011` may become candidate-closed only and remain pending Independent Certification Review.

## 2. Exact parent pins

```text
C1 Freeze Seal                         438274542570f7398af8622fdb511b85d69fc4c403b246b93a8a593b5d8070a5
C1.05R1 provider-normalization iface  71d472e63044b9a7be2c6cc831705ed80dc6a06ccd0ef03e71a0618794bdef63

C2.00 scope/authority                 b504211651839b1cd9c79a9706f05e1ad9c072f66bfb887aec2a0d65c9b17cf7
C2.01R1 capability registry model     0bcdd0c48d8cd614ee7a1cb6ee6519df8fb33731bcafd535f3313978dca4343a
C2.02R2 outcome contract              901445ca8f0f3f1a8cd04331d3def83f4a29ae3984e5917e723e2402f858f57d
C2.03R2 routing contract              e04158428fc030ca72d297b2cb3fd4226dccaba0aa35224b14fc4de89e039b6b

C2.04 parent security contract        198d194fbb3814676f1cb74aec5d56f19f8b1f9b081c6d77c16b4e66fd762cda
C2.04R1 security repair contract      4023224a9b0f23cd006279c217600412376588eced9c62010861ccddf065a548
C2.04R1 independent re-check result   d1af240f4e6eff32b087295ef259fd4485c13fc0775f8abc24fa630993104f47

Adopted C2 workflow plan              b7a4f2a3958417f155e24109edaf025c017d7fc8ac7980ff9765c90fe97e70d6
```

All parent artifacts remain immutable. C2.05 extends C2 semantics only where certification/completeness authority was explicitly reserved.

## 3. Non-negotiable certification principles

1. **Certification and completeness are different claims.**
   A provider/capability may be certified for semantic conformance without any claim that a concrete query exhausts the relevant candidate universe.

2. **Certification is not verification.**
   C2 certification means the provider boundary is contract-conformant under the pinned certification profile. It does not mean observations are true, corroborated, independent, or `C5 VERIFIED`.

3. **Completeness is scope-bound.**
   No coverage attestation is meaningful without one exact, immutable `CoverageScopeDefinition`.

4. **Completeness is not inferred from access-pattern names.**
   `ENUMERATION`, `BULK_EXPORT`, `DIRECT_LOOKUP`, or any other C2.01 access pattern does not itself certify completeness.

5. **Runtime success is not completeness.**
   `SUCCESS + NO_DATA` does not prove absence. `SUCCESS + PRESENT` does not prove uniqueness. `SUCCESS + PARTIAL` cannot support load-bearing absence or uniqueness.

6. **Only exact, replayable, snapshot-stable refs may be load-bearing.**
   Floating `latest`, mutable certification aliases, mutable coverage labels, or undocumented provider behavior cannot support exact absence/uniqueness.

7. **Unknown or indeterminate certification/coverage state fails closed.**

8. **Provider documentation alone is not a completeness proof.**
   First-party documentation may be evidence input but cannot replace method-specific exhaustion evidence required by the pinned contract.

9. **Coverage cannot override C4 or C5.**
   A complete C2 coverage attestation cannot make a query PIT-safe and cannot make an observation verified.

10. **Certification/completeness cannot grant C6 authority or reorder C2.03 routes.**

11. **Historical replay uses the exact pinned certification-registry snapshot.**
    Later invalidation creates a new snapshot; it does not mutate old content-addressed history.

12. **No incomplete attestations are silently unioned into completeness.**
    Composite completeness requires an explicit, independently reviewable composite attestation with exact closure semantics.

## 4. C2.05 stable-reference domain

C2.05 extends the C2.01 stable identity shape unchanged:

```text
C2StableRef =
(authority = C2,
 ref_kind,
 logical_id,
 semantic_revision,
 content_sha256)
```

New closed C2.05 ref kinds:

```text
CERTIFICATION_REGISTRY_SNAPSHOT
PROVIDER_CERTIFICATION_PROFILE
PROVIDER_CERTIFICATION_RECORD
CERTIFICATION_EVIDENCE_BUNDLE
CERTIFICATION_INVALIDATION_RULESET
COVERAGE_SCOPE
COVERAGE_METHOD_PROFILE
COVERAGE_ATTESTATION
COVERAGE_PARTITION
```

Rules inherited from C2.01R1:

- exact kind + logical ID + semantic revision + content hash must resolve;
- wrong-kind, dangling, ambiguous, or hash-mismatched refs fail closed;
- no floating alias may be load-bearing;
- supersession creates a new immutable ref;
- old refs remain replay-resolvable;
- equality means the full stable-ref identity tuple.

C2.05 records MUST NOT contain credentials, secret-derived public hashes, provider-bound private-state values, or unsafe pre-ingress response bytes.

## 5. Certification registry snapshots

Operational certification applicability is represented by immutable **registry snapshots**, not by mutable "current" flags.

```text
ProviderCertificationRegistrySnapshot:
  certification_registry_snapshot_ref
  parent_registry_snapshot_ref?
  certification_entries[]
  coverage_entries[]
  invalidation_event_refs[]
  content_identity
```

Each `certification_entries[]` member contains:

```text
provider_certification_ref
effective_certification_state
```

Closed `effective_certification_state`:

```text
CERTIFIED
NOT_CERTIFIED
SUSPENDED
REVOKED
SUPERSEDED
INDETERMINATE
```

Each `coverage_entries[]` member contains:

```text
coverage_attestation_ref
effective_coverage_state
```

Closed `effective_coverage_state`:

```text
ACTIVE
SUSPENDED
REVOKED
SUPERSEDED
INDETERMINATE
```

Load-bearing certification use requires:

```text
effective_certification_state == CERTIFIED
```

Load-bearing coverage use requires:

```text
effective_coverage_state == ACTIVE
```

No implementation may infer a newer registry snapshot by querying a mutable alias. The exact registry snapshot used by an operation or later C1 dependency must be replay-retained. The exact C2/C1/C6/C7 wire field is deferred to C2.06.

A later registry snapshot may suspend, revoke, or supersede an older record. The older snapshot remains historical evidence and MUST NOT be rewritten.

This snapshot model is C2 operational certification applicability. It is **not** C4 market-time visibility, `available_from`, or revision authority.

## 6. Provider certification profile

A `ProviderCertificationProfile` defines the exact conformance checks required for one certification class.

```text
ProviderCertificationProfile:
  provider_certification_profile_ref
  applicable_provider_profile_refs[]
  applicable_endpoint_profile_refs[]
  applicable_capability_refs[]
  required_check_classes[]
  optional_check_classes[]
  invalidation_ruleset_ref
  evidence_retention_rule_ref
```

Closed `CertificationCheckClass`:

```text
SEMANTIC_PIN_INTEGRITY
REQUEST_SCOPE_CONFORMANCE
RESPONSE_SCHEMA_CONFORMANCE
ABSENCE_SIGNAL_CONFORMANCE
PARTIALITY_SIGNAL_CONFORMANCE
PAGINATION_OR_EXHAUSTION_CONFORMANCE
LIMIT_TRUNCATION_CONFORMANCE
PARTITION_CLOSURE_CONFORMANCE
SECURE_INGRESS_EVIDENCE_CONFORMANCE
CHANGE_DETECTION_BINDING
```

A profile may require only classes from this closed vocabulary. Unknown/private-extension classes invalidate the profile.

At minimum, any profile that can later support a load-bearing coverage attestation MUST require:

```text
SEMANTIC_PIN_INTEGRITY
RESPONSE_SCHEMA_CONFORMANCE
ABSENCE_SIGNAL_CONFORMANCE
PARTIALITY_SIGNAL_CONFORMANCE
SECURE_INGRESS_EVIDENCE_CONFORMANCE
CHANGE_DETECTION_BINDING
```

Additional method-specific checks are required by Section 11.

## 7. Certification evidence bundle

A replayable `CertificationEvidenceBundle` contains exactly one result for every required check class.

```text
CertificationEvidenceBundle:
  certification_evidence_bundle_ref
  provider_certification_profile_ref
  provider_profile_ref
  endpoint_profile_ref
  provider_capability_ref
  check_results[]
```

Each `CertificationCheckResult` contains:

```text
check_result_id
check_class
subject_ref
evidence_refs[]
result
diagnostic_code
```

Closed `result`:

```text
PASS
FAIL
INDETERMINATE
NOT_APPLICABLE
```

Bundle validity rules:

1. every required check class appears exactly once;
2. duplicate required classes are invalid even when duplicate results agree;
3. unknown check classes are invalid;
4. required checks cannot be `NOT_APPLICABLE`;
5. all subject/provider/endpoint/capability/profile refs match the bundle;
6. all load-bearing evidence refs resolve exactly and immutably;
7. evidence derived from provider response material has passed the C2.04 secure-ingress boundary or is a sanitized non-content-bearing audit reference;
8. unsafe credential/private-state/pre-ingress bytes cannot be embedded in the evidence bundle;
9. any missing, conflicting, wrong-scope, unresolved, `FAIL`, or `INDETERMINATE` required check prevents certification.

A percentage score, majority vote, provider reputation score, or "mostly passing" bundle cannot substitute for all required checks passing.

C2.05 evidence is evidence of **contract conformance and exhaustion mechanics**. It is not C5 evidence verification of market facts.

## 8. Provider certification record

```text
ProviderCertificationRecord:
  provider_certification_ref
  provider_certification_profile_ref
  provider_profile_ref
  endpoint_profile_ref
  provider_capability_ref
  certification_evidence_bundle_ref
  certification_decision
  predecessor_certification_ref?
```

Closed `certification_decision`:

```text
CERTIFIED
NOT_CERTIFIED
INDETERMINATE
```

Exact certification predicate:

```text
CERTIFIED <=>
  all stable refs resolve exactly under the pinned semantic state
  AND evidence bundle is valid
  AND every required check result == PASS
  AND provider/endpoint/capability are within the certification profile's exact applicable sets
```

Otherwise:

```text
any required FAIL                 -> NOT_CERTIFIED
any required INDETERMINATE        -> INDETERMINATE
invalid/missing/unresolved bundle -> INDETERMINATE
```

The immutable record's decision is not enough by itself. Load-bearing use additionally requires that the exact pinned certification registry snapshot marks the record `CERTIFIED`.

`CERTIFIED` means only that this exact provider/endpoint/capability semantic boundary passed the pinned certification profile. It does not imply:

- current uptime or low latency;
- route priority;
- quota headroom;
- freshness;
- source truth;
- evidence independence;
- completeness of a particular query;
- C6 authority.

## 9. Invalidation, suspension, revocation, and supersession

A `CertificationInvalidationRuleset` uses the closed trigger classes:

```text
PROVIDER_PROFILE_SEMANTIC_CHANGE
ENDPOINT_PROFILE_SEMANTIC_CHANGE
CAPABILITY_SEMANTIC_CHANGE
RESPONSE_SCHEMA_DRIFT
ABSENCE_SIGNAL_DRIFT
PARTIALITY_SIGNAL_DRIFT
PAGINATION_OR_EXHAUSTION_DRIFT
LIMIT_OR_TRUNCATION_DRIFT
PARTITION_MODEL_DRIFT
SECURE_INGRESS_EVIDENCE_INVALID
TRUSTED_POLICY_REVOCATION
UNKNOWN_MATERIAL_CHANGE
```

Rules:

- a new provider/endpoint/capability stable ref does not inherit certification from the old ref;
- a matching trusted material-drift trigger makes continued load-bearing use fail closed until a later registry snapshot selects an independently supported successor certification;
- `UNKNOWN_MATERIAL_CHANGE` cannot be ignored; it yields `SUSPENDED` or `INDETERMINATE`;
- explicit trusted revocation yields `REVOKED`;
- semantic replacement yields `SUPERSEDED` for the old record in a successor registry snapshot;
- a suspended/revoked/superseded/indeterminate record cannot support completeness;
- invalidation does not rewrite the historical registry snapshot that was originally pinned.

C2.05 does not define monitoring frequency, retry timing, or health polling. Those are outside this contract.

## 10. Exact coverage-scope language

A `CoverageScopeDefinition` identifies the exact universe for which completeness may be claimed.

```text
CoverageScopeDefinition:
  coverage_scope_ref
  provider_profile_ref
  endpoint_profile_ref
  provider_capability_ref
  access_pattern_family
  required_observation_family_refs[]
  required_query_semantic_refs[]
  required_response_semantic_refs[]
  required_semantic_feature_refs[]
  provider_native_subject_semantic_refs[]
  provider_native_identifier_namespace_refs[]
  coverage_partition_refs[]
  temporal_scope_dependency_ref?
  scope_constraint_refs[]
```

`scope_constraint_refs[]` are exact immutable semantic references to provider/request-bound constraints needed to distinguish concrete candidate universes. They are not free-form prose.

Canonicalization rules for every ref list:

1. exact kind/content resolution;
2. exact duplicates deduplicated;
3. same logical ID with conflicting revision/hash in one list is invalid;
4. canonical deterministic ascending order by full stable-ref identity;
5. no wildcard, prefix, display-name, provider marketing label, or hierarchy implication.

For load-bearing absence/uniqueness support, **scope matching is exact**:

```text
required_coverage_scope_ref == attested coverage_scope_ref
```

No implementation may infer that a broader-looking human-readable scope covers a narrower operation. If broader-to-narrower reuse is desired, a separately content-addressed exact `CoverageScopeDefinition` and attestation must be minted for that scope.

For historical/time-bounded scope, `temporal_scope_dependency_ref` is an opaque foreign temporal dependency. C2.05 does not interpret it as C4 truth. Exact C4 wire binding is deferred to C2.06.

## 11. Coverage method profiles

A `CoverageMethodProfile` defines a closed exhaustion methodology.

```text
CoverageMethodProfile:
  coverage_method_profile_ref
  method_family
  allowed_access_pattern_families[]
  required_check_classes[]
  required_evidence_roles[]
  termination_rule
  truncation_failure_rule
```

Closed `method_family`:

```text
EXACT_KEY_SINGLETON
PAGINATION_EXHAUSTION
PARTITION_EXHAUSTION
BULK_MANIFEST_EXHAUSTION
WINDOW_BOUNDARY_EXHAUSTION
COMPOSITE_EXPLICIT_CLOSURE
```

### 11.1 EXACT_KEY_SINGLETON

May support `COMPLETE_FOR_SCOPE` only when:

- the exact request key/constraint universe is represented in `CoverageScopeDefinition`;
- endpoint cardinality/absence semantics resolve under pinned C2.01 semantics;
- the absence signal is contract-bound;
- no pagination/partition/limit continuation exists for the exact scope;
- no partiality/truncation signal is present or unresolved.

This method proves completeness only for that exact singleton request scope. It does not prove provider-wide universe completeness.

### 11.2 PAGINATION_EXHAUSTION

Requires:

- exact pagination semantic ref;
- deterministic initial-page boundary;
- every continuation token/page link followed until the pinned terminal condition;
- no unresolved continuation;
- no token cycle/loop;
- no hidden max-page/client limit termination;
- no provider truncation/partiality signal;
- all page records remain within the exact scope.

A timeout, page cap, SDK default limit, manual stop, missing continuation token with ambiguous semantics, or unresolved terminal signal makes completeness `INDETERMINATE` or `NON_EXHAUSTIVE`.

### 11.3 PARTITION_EXHAUSTION

Requires:

- canonical exact `coverage_partition_refs[]`;
- exactly one complete component result for every required partition;
- no missing partition;
- no unexpected partition expansion;
- every component independently complete under its pinned inner method;
- deterministic union with no unresolved gap.

A partition name alone is not authority. `COVERAGE_PARTITION` refs are atomic stable identities.

### 11.4 BULK_MANIFEST_EXHAUSTION

Requires:

- exact bulk object/dataset scope;
- pinned manifest/closure evidence when the method requires it;
- all required objects/segments present;
- any declared count/hash/segment closure checks pass when applicable;
- no provider/client truncation or omitted segment is unresolved.

Receiving one bulk object is not sufficient by itself.

### 11.5 WINDOW_BOUNDARY_EXHAUSTION

Requires:

- exact provider-native window constraints in the coverage scope;
- exact boundary inclusion/exclusion semantics;
- complete pagination/partition closure inside the window;
- no claim outside the exact window;
- an opaque `temporal_scope_dependency_ref` when the conclusion is historical and later C4 interpretation is required.

### 11.6 COMPOSITE_EXPLICIT_CLOSURE

A composite attestation may be complete only when:

- it names exact component `coverage_attestation_ref`s;
- each component is independently `COMPLETE_FOR_SCOPE`, active, and supported by a certified provider record;
- the composite method proves exact partition/scope closure;
- component semantic scopes are compatible by explicit machine rules;
- no gap is inferred from human labels or provider names.

Two partial or non-exhaustive attestations never become complete merely because their union "looks broad."

### 11.7 Non-exhaustive access patterns

`SEARCH`, `DOCUMENT_DISCOVERY`, `STREAM_SUBSCRIPTION`, ranked/fuzzy retrieval, first-N results, and open-ended feeds are non-exhaustive by default.

They cannot support `COMPLETE_FOR_SCOPE` unless the exact pinned `CoverageMethodProfile` is one of the closed method families above and all of that method's closure conditions are machine-provable for the exact scope. A provider claim such as "searches all securities" is not sufficient.

## 12. Coverage attestation record

```text
CoverageAttestationRecord:
  coverage_attestation_ref
  certification_registry_snapshot_ref
  provider_certification_ref
  coverage_scope_ref
  coverage_method_profile_ref
  coverage_evidence_bundle_ref
  component_attestation_refs[]
  coverage_classification
```

Closed `coverage_classification`:

```text
COMPLETE_FOR_SCOPE
PARTIAL_KNOWN
NON_EXHAUSTIVE
INDETERMINATE
INVALID
```

Exact `COMPLETE_FOR_SCOPE` predicate requires all of:

1. exact registry snapshot resolves;
2. referenced provider certification is present in that snapshot with `effective_certification_state == CERTIFIED`;
3. exact coverage scope resolves;
4. exact coverage method profile resolves;
5. method family is allowed for the scope's access pattern;
6. every method-required check appears exactly once and `PASS`;
7. no required check is missing, duplicated, `FAIL`, `INDETERMINATE`, or `NOT_APPLICABLE`;
8. secure-ingress evidence requirements are satisfied;
9. all method-specific exhaustion/termination/truncation/partition rules pass;
10. any component attestation required by the method is exact, active, complete, compatible, and gap-closed;
11. the registry snapshot marks this attestation `ACTIVE`;
12. stored classification recomputes exactly as `COMPLETE_FOR_SCOPE`.

Any violation prevents `COMPLETE_FOR_SCOPE`.

`PARTIAL_KNOWN`, `NON_EXHAUSTIVE`, `INDETERMINATE`, and `INVALID` are never load-bearing for C1 absence or uniqueness.

## 13. C1 completeness-dependency support predicate

C1.05R1 requires opaque C2 completeness dependencies when exact C1 conclusions load-bearingly depend on absence.

C2.05 defines the C2-side support predicate. It does **not** define C1's final resolution decision.

For one exact operation/result and one exact coverage attestation:

```text
coverage_support_valid <=>
  operation pins the exact certification_registry_snapshot_ref
  AND attestation is ACTIVE in that snapshot
  AND provider certification is CERTIFIED in that snapshot
  AND attestation.coverage_classification == COMPLETE_FOR_SCOPE
  AND operation provider/endpoint/capability refs exactly match the attestation scope
  AND operation's required_coverage_scope_ref exactly equals attestation.coverage_scope_ref
  AND no C2.02 material partiality/truncation state is present
```

Then:

```text
SUCCESS + NO_DATA + coverage_support_valid
  -> ABSENCE_SUPPORT_ELIGIBLE

SUCCESS + PRESENT + coverage_support_valid
  -> UNIQUENESS_SUPPORT_ELIGIBLE

SUCCESS + PARTIAL
  -> NO_ABSENCE_OR_UNIQUENESS_SUPPORT

FAILED or CANCELLED
  -> NO_ABSENCE_OR_UNIQUENESS_SUPPORT
```

These are **eligibility signals only**.

`ABSENCE_SUPPORT_ELIGIBLE` does not equal C1 `NO_MATCH`.

`UNIQUENESS_SUPPORT_ELIGIBLE` does not equal C1 `RESOLVED` and does not assert that exactly one candidate exists.

C1 still owns semantic scope match, ambiguity handling, canonical identity, and final resolution. C4 still gates historical/PIT applicability. C5 still gates evidence fitness/verification/conflict.

A positive exact mapping may be usable under frozen C1 rules without a complete universe when the mapping does not depend on absence. C2.05 MUST NOT impose universal completeness on all positive observations.

## 14. C2.02 operation/outcome interaction

C2.05 consumes, but does not redefine, C2.02:

```text
operation_status: SUCCESS | FAILED | CANCELLED
data_outcome: PRESENT | NO_DATA | PARTIAL
```

Rules:

- `SUCCESS + NO_DATA` is a provider outcome, not completeness;
- `SUCCESS + PRESENT` may carry valid observations but does not prove the result set was exhaustive;
- `SUCCESS + PARTIAL` can carry valid positive observations but cannot support absence/uniqueness;
- `FAILED` and `CANCELLED` never support completeness;
- a coverage attestation cannot overwrite or "upgrade" `PARTIAL` to complete;
- a complete attestation cannot convert a failed/cancelled operation into `NO_DATA`;
- C2.02 `attempted_response_semantic_refs[]` must remain compatible with the exact coverage scope; C2.06/C2.07 own final machine binding.

## 15. Temporal validity without absorbing C4

C2.OPEN-011 is addressed by a two-layer rule.

### 15.1 Operational certification applicability

Operational certification applicability is represented by the exact immutable `ProviderCertificationRegistrySnapshot` pinned to the operation or dependency.

A later suspension/revocation/supersession is a new snapshot. Historical replay uses the originally pinned snapshot. No mutable "current certification" lookup is load-bearing.

This provides deterministic operational applicability **without defining a clock-based C4 rule**.

### 15.2 Historical/market-time coverage

When a completeness claim is historical or time-bounded, the exact `CoverageScopeDefinition` must carry:

```text
temporal_scope_dependency_ref
```

This is an opaque foreign temporal dependency. C2.05 does not define:

- `available_from`;
- observation visibility at decision time;
- event/effective-time truth;
- revision lineage;
- PIT reconstructability;
- time precision;
- temporal interval comparison.

Those remain C4-owned. The exact C2↔C4 wire binding is deferred to C2.06.

Therefore:

```text
C2 COMPLETE_FOR_SCOPE
does not imply
C4 PIT_SAFE
```

## 16. Multiple providers and composite coverage

Multiple provider results remain separate unless an explicit composite attestation exists.

Forbidden:

```text
Provider A PARTIAL + Provider B PARTIAL -> COMPLETE
Provider A NON_EXHAUSTIVE + Provider B NON_EXHAUSTIVE -> COMPLETE
two first pages -> exhaustive universe
two ranked searches -> uniqueness proof
```

A `COMPOSITE_EXPLICIT_CLOSURE` attestation must identify exact component attestations and prove machine-closed partition/scope coverage. It cannot use provider count or provider diversity as a proxy for completeness.

This is not C5 source independence. It is only C2 coverage closure.

## 17. Secure-ingress and public evidence boundary

Certification/coverage evidence derived from external provider content remains subject to C2.04.

- unsafe pre-ingress response bytes are not certification artifacts;
- quarantined/rejected response content cannot support certification/completeness;
- `EPHEMERAL_ONLY` content cannot gain a persisted raw payload merely because certification wants evidence;
- sanitized audit metadata may be retained when allowed;
- a certification evidence ref may point to a permitted-raw artifact only through the exact later C2/C11 handoff contract;
- no credential/private-state content may be copied into public certification reports.

C2.05 cannot weaken the C2.04R1 security boundary.

## 18. Cross-contract ownership

### C1

C1 consumes opaque snapshot-stable completeness refs and owns final normalization/resolution semantics.

C2.05 does not emit canonical `NO_MATCH`, `RESOLVED`, canonical identity, or uniqueness truth.

### C2.01

C2.05 consumes exact provider/endpoint/capability/access-pattern/semantic refs. It does not mutate capability compatibility.

### C2.02

C2.05 consumes exact operation/data outcomes and attempted response scope. It does not redefine `SUCCESS/FAILED/CANCELLED` or `PRESENT/NO_DATA/PARTIAL`.

### C2.03

Certification/completeness does not reorder routes, create route eligibility, or define fallback.

### C2.04

All certification evidence crossing from provider material obeys secure-ingress, credential, and private-state boundaries.

### C3

C3 owns retry/backoff/quota/cache/freshness/coalescing/LKG. Certification state is not current health or cache state.

### C4

C4 owns historical visibility, revision, `available_from`, PIT, and temporal reconstruction. C2.05 may carry only opaque temporal dependencies.

### C5

C5 owns source fitness, verification, evidence independence, source ranking, and conflict adjudication. C2 certification is not C5 verification.

### C6

C6 owns capability/trusted-intent/destination/policy/side-effect authority. Certification grants none of these.

### C7

C7 owns orchestration, budgets, cancellation, and durable continuation.

### C11

C11 owns persistence implementation. C2.05 does not select a database, certification store, or raw-artifact repository.

### C12

C12 owns validation/promotion/release. C2.05 cannot self-freeze.

## 19. Security and semantic red lines

The following are invalid:

```text
provider says "complete" -> COMPLETE_FOR_SCOPE
ENUMERATION access pattern -> completeness by definition
BULK_EXPORT -> completeness by definition
SUCCESS+NO_DATA -> C1 NO_MATCH
SUCCESS+PRESENT + one row -> unique canonical resolution
SUCCESS+PARTIAL -> absence support
FAILED/CANCELLED -> completeness support
floating latest certification ref -> exact absence support
mutable coverage label -> replay authority
old superseded certification silently reused as current
two partial providers -> complete by union
ranked search first page -> exhaustive universe
provider documentation alone -> exhaustion proof
C2 certification -> C5 VERIFIED
C2 completeness -> C4 PIT_SAFE
C2 certification -> C6 capability
C2 certification -> route priority
certification state -> C3 current health/freshness
quarantined/rejected provider content -> certification evidence
EPHEMERAL_ONLY -> persisted raw evidence by certification fiat
secret/private material -> public certification report
C2.05 -> concrete provider selection
C2.05 -> production adapter
C2.05 -> PAPER/LIVE/external side effect
self-approval / self-freeze
```

## 20. Candidate open-question disposition

```text
C2.OPEN-009 =
CANDIDATE_CLOSED_PENDING_INDEPENDENT_CERTIFICATION_REVIEW
(provider certification states, evidence requirements, invalidation rules)

C2.OPEN-010 =
CANDIDATE_CLOSED_PENDING_INDEPENDENT_CERTIFICATION_REVIEW
(exact scope language and completeness/coverage methodology)

C2.OPEN-011 =
CANDIDATE_CLOSED_PENDING_INDEPENDENT_CERTIFICATION_REVIEW
(snapshot-stable operational applicability + opaque C4 temporal dependency)

C2.OPEN-012 =
OPEN_UNCHANGED
(exact C1/C3/C4/C5/C6/C7 wire binding remains C2.06)

C2.OPEN-013 =
OPEN_UNCHANGED_C2_06_PERMITTED_RAW_HANDOFF

C2.OPEN-014 =
OPEN_UNCHANGED
(machine schema/validators remain C2.07)

C2.OPEN-015 =
OPEN_UNCHANGED
(concrete provider/vendor configuration remains post-contract)
```

No OPEN item is represented as final authority before Independent Certification Review.

## 21. Exit gate

C2.05 remains a construction candidate.

Required next gate:

```text
C2.05 Independent Certification Review
```

The review must adversarially verify at least:

- certification/completeness separation;
- exact immutable registry-snapshot applicability;
- closed certification states and evidence-bundle completeness;
- fail-closed invalidation/drift behavior;
- exact coverage-scope identity and no wildcard/human-label broadening;
- method-specific exhaustion/termination/truncation closure;
- pagination, partition, bulk, window and composite adversarial cases;
- `SUCCESS+NO_DATA` not becoming absence without valid coverage;
- `PARTIAL/FAILED/CANCELLED` not becoming completeness;
- absence/uniqueness support remaining eligibility rather than C1 conclusions;
- no C4/C5/C6/C3/C7/C11 authority absorption;
- C2.04 secure-ingress non-regression;
- no concrete providers/adapters/vendors;
- deterministic replay from exact pinned refs.

C2.06 MUST NOT begin before an independent PASS or an explicitly scoped repair/re-check sequence.

Production implementation remains `NOT_AUTHORIZED`.

External / PAPER / LIVE side effects remain `NOT_AUTHORIZED`.
