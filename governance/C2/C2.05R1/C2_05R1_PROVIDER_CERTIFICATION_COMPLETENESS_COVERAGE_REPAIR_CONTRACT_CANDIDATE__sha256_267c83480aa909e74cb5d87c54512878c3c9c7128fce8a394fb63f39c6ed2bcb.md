# C2.05R1 — Provider Certification / Completeness / Coverage Scoped Repair Contract Candidate

Generated: 2026-09-07T06:31:00Z

Status: `SCOPED_REPAIR_CANDIDATE_PENDING_INDEPENDENT_CERTIFICATION_RECHECK`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

## 1. Repair authority and scope

C2.05R1 is a repair overlay on the exact C2.05 candidate:

```text
C2.05 contract SHA-256          3642588dcc22a7564d55a9a72d3e6e328b007649005c866e7831dfa4b8571d4c
C2.05 logical model SHA-256     0a6d7c4037c04ca04f87994507afb722661dbd9450a115492238b9d5dd9c776c
C2.05 acceptance SHA-256        62714c720e2a9d6f24f066533ddac9c84f3360a6bff2cbe4d9aacbb9617cff6f
C2.05 decision ledger SHA-256   519cfd630f8f60772fe649b98297c2e32c2a912f9b36b2c59567d1e56fc57366
Independent review report       17853fd3e93d9a7d0cb611564004e85865d2fda20e05ee1ad885a249f2705c04
Independent review result       8edddb75c2fa556ecb1d688b1f543057e99171441e7ea3ec4466c02c7ddb0a10
```

The user authorized C2.05R1 only for the five blockers identified by the Independent Certification Review:

```text
C2CERT-B01  COVERAGE_EVIDENCE_CARRIER_NOT_TYPE_CLOSED
C2CERT-B02  CERTIFICATION_DECISION_NOT_TOTAL_FOR_MIXED_FAILURE_STATES
C2CERT-B03  OPERATION_TO_COVERAGE_SCOPE_BINDING_NOT_MACHINE_CLOSED
C2CERT-B04  PARTITION_COMPOSITE_CLOSURE_PREDICATE_UNDERDEFINED
C2CERT-B05  NON_COMPLETE_COVERAGE_CLASSIFICATION_NOT_TOTAL
```

This repair MUST NOT reopen passing C2.05 surfaces except where required to close those blockers. It does not start C2.06, choose providers/vendors, implement adapters, grant C6 capability, define C3 health/retry/cache/freshness, define C4 PIT/available_from, define C5 verification/source fitness, define C7 orchestration, or choose C11 persistence.

C2.05R1 cannot self-close any blocker. During construction every blocker is only `ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK`.

## 2. Effective-contract rule

For B01-B05 and the exact fields amended below, this repair overlay supersedes the corresponding underdefined C2.05 clauses. All non-conflicting C2.05 clauses remain effective unchanged.

No implementation may use an older ambiguous interpretation as a parallel success path.

## 3. Stable-reference extension and field-kind closure — B01

The C2 stable-ref identity shape remains:

```text
(authority=C2, ref_kind, logical_id, semantic_revision, content_sha256)
```

C2.05R1 adds exactly two closed kinds:

```text
COVERAGE_EVIDENCE_BUNDLE
OPERATION_COVERAGE_SCOPE_BINDING
```

The following field-kind contract is normative:

```text
CoverageAttestationRecord.coverage_evidence_bundle_ref
  -> COVERAGE_EVIDENCE_BUNDLE

OperationCoverageScopeBinding.operation_coverage_scope_binding_ref
  -> OPERATION_COVERAGE_SCOPE_BINDING

OperationCoverageScopeBinding.parent_semantic_registry_snapshot_ref
  -> REGISTRY_SNAPSHOT
```

Unknown, private-extension, wrong-kind, dangling, ambiguous, floating, or content-hash-mismatched refs fail closed and cannot support `COMPLETE_FOR_SCOPE` or any C1-side eligibility signal.

## 4. Coverage evidence carrier — B01

### 4.1 Closed coverage check vocabulary

`CoverageMethodCheckClass` is exactly:

```text
SCOPE_BINDING_INTEGRITY
METHOD_ACCESS_PATTERN_CONFORMANCE
REQUIRED_EVIDENCE_ROLE_COMPLETENESS
TERMINATION_CLOSURE
TRUNCATION_ABSENCE
PARTITION_COMPONENT_CLOSURE
COMPOSITE_GAP_CLOSURE
SECURE_INGRESS_EVIDENCE_CONFORMANCE
```

A `CoverageMethodProfile.required_check_classes[]` may contain only these values. Exact duplicates are invalid. The list is canonicalized by lexical ascending order.

Method minimums:

```text
ALL METHODS:
  SCOPE_BINDING_INTEGRITY
  METHOD_ACCESS_PATTERN_CONFORMANCE
  REQUIRED_EVIDENCE_ROLE_COMPLETENESS
  TERMINATION_CLOSURE
  TRUNCATION_ABSENCE
  SECURE_INGRESS_EVIDENCE_CONFORMANCE

PARTITION_EXHAUSTION additionally:
  PARTITION_COMPONENT_CLOSURE

COMPOSITE_EXPLICIT_CLOSURE additionally:
  COMPOSITE_GAP_CLOSURE
```

### 4.2 Closed evidence-role vocabulary

`CoverageEvidenceRole` is exactly:

```text
REQUEST_SCOPE_BINDING
RESPONSE_SCOPE_BINDING
TERMINAL_SIGNAL
CONTINUATION_EDGE
TRUNCATION_SIGNAL
PARTITION_MEMBERSHIP
BULK_MANIFEST
BULK_SEGMENT
WINDOW_BOUNDARY
COMPONENT_ATTESTATION
GAP_CLOSURE
SECURE_INGRESS_DECISION
```

`CoverageMethodProfile.required_evidence_roles[]` may contain only this vocabulary. Exact duplicates are invalid; lexical ascending order is canonical. A required role must be represented at least once by a resolved evidence item in the coverage evidence bundle. Unknown/private roles are invalid; they cannot become load-bearing by convention.

### 4.3 Closed termination and truncation rules

`termination_rule` is not free-form. It is a one-to-one function of `method_family`:

```text
EXACT_KEY_SINGLETON          -> EXACT_KEY_NO_CONTINUATION
PAGINATION_EXHAUSTION        -> PAGINATION_PINNED_TERMINAL_REACHED
PARTITION_EXHAUSTION         -> PARTITION_REQUIRED_SET_BIJECTION
BULK_MANIFEST_EXHAUSTION     -> BULK_MANIFEST_SEGMENT_SET_CLOSED
WINDOW_BOUNDARY_EXHAUSTION   -> WINDOW_EXACT_BOUNDARIES_CLOSED
COMPOSITE_EXPLICIT_CLOSURE   -> COMPOSITE_REQUIRED_SCOPE_SET_BIJECTION
```

`truncation_failure_rule` is exactly:

```text
ANY_MATERIAL_PARTIALITY_OR_TRUNCATION_PREVENTS_COMPLETE
```

Any other value is an invalid method profile.

### 4.4 CoverageEvidenceBundle

A load-bearing coverage evidence carrier is:

```text
CoverageEvidenceBundle:
  coverage_evidence_bundle_ref
  certification_registry_snapshot_ref
  parent_semantic_registry_snapshot_ref
  provider_certification_ref
  coverage_scope_ref
  coverage_method_profile_ref
  operation_coverage_scope_binding_ref
  attestation_subject_binding
  check_results[]
  evidence_items[]
  component_bindings[]
```

`attestation_subject_binding` contains exactly:

```text
certification_registry_snapshot_ref
provider_certification_ref
coverage_scope_ref
coverage_method_profile_ref
canonical_component_attestation_refs[]
```

These fields MUST equal the corresponding fields of the `CoverageAttestationRecord` that consumes the bundle. This avoids a recursive content-address cycle while binding the bundle to exactly one attestation semantic subject.

Each `CoverageMethodCheckResult` is:

```text
check_class
result
diagnostic_code
```

with result vocabulary:

```text
PASS
FAIL
INDETERMINATE
NOT_APPLICABLE
```

Every method-required check class appears exactly once. Missing, duplicate, undeclared, unknown, required `NOT_APPLICABLE`, wrong-scope, or unresolved check state is structurally invalid. Every required check must be `PASS` for `COMPLETE_FOR_SCOPE`.

Each `CoverageEvidenceItem` is:

```text
evidence_item_id
role
evidence_ref
subject_binding
```

`role` must be one closed `CoverageEvidenceRole`. `subject_binding` must match the bundle's exact registry/certification/scope/method/operation binding. Every required role must have at least one exact resolved item. Extra items are allowed only for declared closed roles and remain non-authoritative unless consumed by a required method predicate.

Provider-derived response material must already satisfy C2.04R1 secure ingress. Quarantined/rejected bytes, unsafe pre-ingress bytes, credential/private-state material, and unauthorized persistence remain forbidden exactly as before.

## 5. Total certification decision function — B02

### 5.1 Profile normalization

For one `ProviderCertificationProfile`:

- `required_check_classes[]` and `optional_check_classes[]` are canonical sets;
- duplicates inside either set are invalid;
- the two sets MUST be disjoint;
- unknown/private check classes are invalid.

A certification bundle may contain exactly one result for every required class and zero or one result for every declared optional class. Any undeclared class is structurally invalid. Optional results are diagnostic only and do not change the certification decision.

### 5.2 Structural-invalid predicate

`certification_bundle_structurally_invalid == true` if any of the following occurs:

```text
invalid profile check-class set
missing required class
duplicate required or optional class
undeclared/unknown class
required NOT_APPLICABLE
wrong provider/endpoint/capability/profile subject
wrong-kind/dangling/ambiguous/floating/hash-mismatched load-bearing ref
invalid secure-ingress evidence binding
```

### 5.3 Total deterministic classifier

The exact certification decision is evaluated in this order:

```text
1. if certification_bundle_structurally_invalid
      -> INDETERMINATE

2. else if ANY required check == FAIL
      -> NOT_CERTIFIED

3. else if ANY required check == INDETERMINATE
      -> INDETERMINATE

4. else
      -> CERTIFIED
```

Because structural validity excludes missing/duplicate/required-N/A/unknown conditions, step 4 means every required check is exactly one `PASS`.

This precedence is total. Examples:

```text
FAIL + INDETERMINATE                    -> NOT_CERTIFIED
FAIL + structural invalidity            -> INDETERMINATE
INDETERMINATE + structural invalidity   -> INDETERMINATE
all required PASS + optional FAIL       -> CERTIFIED
all required PASS + optional INDETERMINATE -> CERTIFIED
```

Permutation of `check_results[]` MUST NOT change the outcome.

## 6. Parent semantic-registry binding — B03

C2.05R1 amends `CoverageScopeDefinition` to require:

```text
parent_semantic_registry_snapshot_ref
```

of exact kind `REGISTRY_SNAPSHOT`.

All C2.01 provider/endpoint/capability/query/response/feature/observation/native-subject/native-identifier refs participating in that scope MUST resolve exactly under this same pinned parent semantic registry snapshot. No mutable/current registry lookup, transitive alternate snapshot, or mixed-snapshot satisfaction is allowed.

This is semantic authority only; C2.06 still owns the final wire field placement.

## 7. OperationCoverageScopeBinding — B03

A replay-retained semantic binding record is:

```text
OperationCoverageScopeBinding:
  operation_coverage_scope_binding_ref
  provider_operation_ref
  route_attempt_ref
  parent_semantic_registry_snapshot_ref
  provider_profile_ref
  endpoint_profile_ref
  provider_capability_ref
  access_pattern_family
  required_observation_family_refs[]
  required_query_semantic_refs[]
  attempted_response_semantic_refs[]
  required_semantic_feature_refs[]
  provider_native_subject_semantic_refs[]
  provider_native_identifier_namespace_refs[]
  coverage_partition_refs[]
  scope_constraint_refs[]
  temporal_scope_dependency_ref?
  required_coverage_scope_ref
```

All list-valued fields use the C2 exact canonical-set discipline: exact resolution, exact duplicate dedupe, conflicting same-logical-ID revision/hash invalid, deterministic full-ref ordering.

The `operation_scope_binding_valid` predicate is true iff:

```text
A. required_coverage_scope_ref resolves exactly to one CoverageScopeDefinition;
B. binding.parent_semantic_registry_snapshot_ref
   == scope.parent_semantic_registry_snapshot_ref;
C. all participating C2 semantic refs resolve under that exact parent snapshot;
D. provider_profile_ref == scope.provider_profile_ref;
E. endpoint_profile_ref == scope.endpoint_profile_ref;
F. provider_capability_ref == scope.provider_capability_ref;
G. access_pattern_family == scope.access_pattern_family;
H. required_observation_family_refs
   == scope.required_observation_family_refs;
I. required_query_semantic_refs
   == scope.required_query_semantic_refs;
J. attempted_response_semantic_refs
   == scope.required_response_semantic_refs;
K. required_semantic_feature_refs
   == scope.required_semantic_feature_refs;
L. provider_native_subject_semantic_refs
   == scope.provider_native_subject_semantic_refs;
M. provider_native_identifier_namespace_refs
   == scope.provider_native_identifier_namespace_refs;
N. coverage_partition_refs
   == scope.coverage_partition_refs;
O. scope_constraint_refs
   == scope.scope_constraint_refs;
P. temporal_scope_dependency_ref equality holds exactly,
   including BOTH_ABSENT or EXACT_SAME_REF;
Q. provider_operation_ref and route_attempt_ref identify the exact
   operation/attempt whose result requests coverage support.
```

Any FALSE or unresolved clause makes `operation_scope_binding_valid == false`.

Merely pinning the same `required_coverage_scope_ref` is insufficient.

The repaired C1 support predicate additionally requires the exact `operation_coverage_scope_binding_ref` and `operation_scope_binding_valid == true`.

## 8. Partition closure — B04

`CoverageComponentBinding` is embedded in the coverage evidence bundle:

```text
CoverageComponentBinding:
  component_attestation_ref
  component_scope_ref
  covered_partition_refs[]
```

All refs must resolve exactly; repeated `component_attestation_ref` is structurally invalid.

For `PARTITION_EXHAUSTION`:

1. root `CoverageScopeDefinition.coverage_partition_refs[]` MUST be non-empty;
2. every component binding has exactly one `covered_partition_ref`;
3. every component attestation is `COMPLETE_FOR_SCOPE`, ACTIVE, and supported by CERTIFIED state under the exact registry snapshot;
4. `component_scope_ref == component_attestation.coverage_scope_ref`;
5. each component scope is exact and compatible with the root by the partition compatibility rule below;
6. the mapping from component attestations to root required partitions is a bijection:

```text
canonical(covered_partition_refs from all component bindings)
==
canonical(root_scope.coverage_partition_refs)
```

with no duplicate mapping, missing partition, or extra partition.

A component may not cover multiple partitions in `PARTITION_EXHAUSTION`.

`partition_scope_compatible(root, component, p)` requires:

- same parent semantic registry snapshot;
- same access pattern family;
- same required observation/query/response/feature/native-subject/native-identifier sets;
- same scope constraints;
- same temporal dependency;
- component `coverage_partition_refs == [p]`.

Provider/endpoint/capability refs may differ only when the exact component scope was separately minted and all its refs resolve under the same parent semantic registry snapshot. No human-label equivalence is allowed.

## 9. Composite closure — B04

C2.05R1 amends `CoverageScopeDefinition` with optional:

```text
composite_component_scope_refs[]
```

Canonicalization follows exact stable-ref set rules.

For all methods except `COMPOSITE_EXPLICIT_CLOSURE`, this list MUST be empty.

For `COMPOSITE_EXPLICIT_CLOSURE`:

1. `composite_component_scope_refs[]` MUST be non-empty;
2. each listed scope ref resolves exactly;
3. there is exactly one component attestation binding for each listed component scope;
4. every component attestation is `COMPLETE_FOR_SCOPE`, ACTIVE, and backed by CERTIFIED state in the same pinned certification registry snapshot;
5. each component's `coverage_scope_ref` equals its bound component scope ref;
6. repeated component attestation refs or repeated component scope refs are invalid;
7. a component whose method family is itself `COMPOSITE_EXPLICIT_CLOSURE` is invalid; nested composite closure is forbidden in C2.05R1;
8. all component scopes share the root's exact parent semantic registry snapshot;
9. root/component non-partition semantic compatibility requires exact equality of:
   - required observation family refs,
   - required semantic feature refs,
   - provider-native subject semantic refs,
   - provider-native identifier namespace refs,
   - scope constraint refs,
   - temporal dependency;
10. provider-specific query/response semantics may differ only because each component scope is explicitly enumerated in `composite_component_scope_refs[]`; no inferred compatibility path exists;
11. if root `coverage_partition_refs[]` is non-empty:
   - every component binding's `covered_partition_refs[]` is non-empty;
   - each component binding's covered set equals its component scope's partition set;
   - component covered sets are pairwise disjoint;
   - their canonical union equals root `coverage_partition_refs[]`;
12. if root `coverage_partition_refs[]` is empty:
   - every component scope and binding MUST also have an empty partition set;
   - gap closure is the exact component-scope-set bijection in clauses 1-6.

Any duplicate, overlap, missing, extra, nested, unresolved, incompatible, or non-active/non-complete component fails closed.

## 10. Total coverage-classification function — B05

Coverage classification is recomputed from pinned semantics. Define the following mutually evaluated predicates:

```text
STRUCTURAL_INVALID:
  invalid/wrong-kind/dangling/floating/hash-mismatched ref
  OR invalid method profile
  OR invalid coverage evidence bundle structure
  OR invalid operation-scope binding structure
  OR duplicate/undeclared required method check
  OR required NOT_APPLICABLE
  OR invalid component structure
  OR illegal nested composite
  OR stored subject binding mismatch

HAS_INDETERMINATE:
  no STRUCTURAL_INVALID
  AND any required semantic/evidence/certification/termination/
      component/closure dependency is unresolved or INDETERMINATE

HAS_KNOWN_PARTIALITY:
  no STRUCTURAL_INVALID
  AND not HAS_INDETERMINATE
  AND (operation == SUCCESS+PARTIAL
       OR a pinned material partiality/truncation condition is affirmatively present)

HAS_KNOWN_NONEXHAUSTIVE:
  no STRUCTURAL_INVALID
  AND not HAS_INDETERMINATE
  AND not HAS_KNOWN_PARTIALITY
  AND any required completeness predicate is deterministically FALSE,
      including known method termination failure, known missing/extra partition,
      known bulk omission, known non-exhaustive search/stream state,
      FAILED/CANCELLED operation, certification not CERTIFIED,
      coverage registry state not ACTIVE, required method check FAIL,
      or operation_scope_binding_valid == false

ALL_COMPLETE:
  none of the above
  AND every COMPLETE_FOR_SCOPE predicate is TRUE
```

The total classifier is:

```text
if STRUCTURAL_INVALID       -> INVALID
else if HAS_INDETERMINATE   -> INDETERMINATE
else if HAS_KNOWN_PARTIALITY-> PARTIAL_KNOWN
else if HAS_KNOWN_NONEXHAUSTIVE -> NON_EXHAUSTIVE
else if ALL_COMPLETE        -> COMPLETE_FOR_SCOPE
else                        -> INDETERMINATE
```

The final `else -> INDETERMINATE` is mandatory fail-closed totality and may not be replaced by guessing.

Examples:

```text
invalid evidence ref + known partiality      -> INVALID
unresolved continuation + known partiality   -> INDETERMINATE
known partiality + known page cap            -> PARTIAL_KNOWN
known page cap only                          -> NON_EXHAUSTIVE
FAILED or CANCELLED with otherwise valid refs-> NON_EXHAUSTIVE
all exact complete predicates true           -> COMPLETE_FOR_SCOPE
```

`CoverageAttestationRecord.coverage_classification` MUST equal the recomputed result. A stored mismatch makes the record `INVALID_FOR_LOAD_BEARING_USE`; implementations use the recomputed classifier for diagnostics but MUST NOT silently rewrite the immutable record.

## 11. Repaired support predicate

`coverage_support_valid` is true only if all parent C2.05 conditions remain true AND:

```text
exact operation_coverage_scope_binding_ref resolves
AND operation_scope_binding_valid == true
AND exact COVERAGE_EVIDENCE_BUNDLE resolves
AND evidence bundle subject binding matches the attestation
AND recomputed coverage classification == COMPLETE_FOR_SCOPE
AND stored coverage classification == recomputed classification
```

Then, and only then:

```text
SUCCESS + NO_DATA    -> ABSENCE_SUPPORT_ELIGIBLE
SUCCESS + PRESENT    -> UNIQUENESS_SUPPORT_ELIGIBLE
SUCCESS + PARTIAL    -> NO_ABSENCE_OR_UNIQUENESS_SUPPORT
FAILED/CANCELLED     -> NO_ABSENCE_OR_UNIQUENESS_SUPPORT
```

These remain C2 eligibility signals, never C1 `NO_MATCH` or `RESOLVED`.

## 12. Non-regression and ownership

The following remain unchanged:

- C1 owns final normalization, identity, ambiguity, NO_MATCH, uniqueness, and RESOLVED.
- C3 owns retry/backoff/quota/cache/freshness/coalescing/LKG.
- C4 owns PIT, revision, available_from, historical visibility, and temporal reconstructability.
- C5 owns verification, evidence fitness, independence, ranking, and conflict.
- C6 owns capability, trusted intent, destination, policy, and side-effect authority.
- C7 owns orchestration, budgets, cancellation, and durable continuation.
- C11 owns persistence implementation.
- C12 owns validation/promotion/release.
- C2.06 owns exact cross-contract wire serialization and C2->C11 handoff.
- C2.07 owns executable schema/validators and must encode these semantics rather than invent them.
- C2.04R1 secure-ingress semantics remain authoritative and unchanged.
- Concrete provider/vendor configuration remains deferred under C2.OPEN-015.

## 13. Blocker disposition after construction

Construction may record only:

```text
C2CERT-B01 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
C2CERT-B02 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
C2CERT-B03 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
C2CERT-B04 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
C2CERT-B05 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
```

`C2.OPEN-009..011` may be `REPAIR_CANDIDATE_PENDING_INDEPENDENT_RECHECK`, not finally closed.

## 14. Exit gate

C2.05R1 construction stops at:

```text
C2.05R1 Independent Certification Re-Check
```

The re-check must independently re-run failed obligations:

```text
C2-402
C2-411
C2-412
C2-437
C2-438
C2-459
C2-471
C2-481
```

and all new C2.05R1 adversarial obligations.

C2.06, production implementation, and external/PAPER/LIVE side effects remain `NOT_AUTHORIZED`.
