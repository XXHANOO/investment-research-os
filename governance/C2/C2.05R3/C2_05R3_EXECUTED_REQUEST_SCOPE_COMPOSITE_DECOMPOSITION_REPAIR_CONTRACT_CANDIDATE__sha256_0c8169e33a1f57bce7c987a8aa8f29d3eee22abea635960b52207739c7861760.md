# C2.05R3 — Executed-Request Scope and Composite Semantic-Decomposition Scoped Repair Contract Candidate

Generated: 2026-09-07T16:27:00Z

Status: `SCOPED_REPAIR_CANDIDATE_PENDING_INDEPENDENT_CERTIFICATION_RECHECK`

Production implementation: `NOT_AUTHORIZED`

Provider/vendor configuration: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

## 1. Repair authority and exact scope

C2.05R3 is a narrow repair overlay on the effective C2.05 + C2.05R1 + C2.05R2 contract.

Exact parent pins:

```text
C2.05 parent contract SHA-256          3642588dcc22a7564d55a9a72d3e6e328b007649005c866e7831dfa4b8571d4c
C2.05R1 repair contract SHA-256        267c83480aa909e74cb5d87c54512878c3c9c7128fce8a394fb63f39c6ed2bcb
C2.05R1 independent result SHA-256     59578acccb8906637360f24c7fe190a3a6e6b92098ddf03c30a5133b9d5767bf
C2.05R2 repair contract SHA-256        b68943c7773ba5abb596eafd2a572398d172ed3d0bd08cea1b12bdd5b51c29ff
C2.05R2 logical model SHA-256          129657e705dad194691e48edd09274297856e11a2e0b44d075392da9942e7437
C2.05R2 independent report SHA-256     80e81deb17a1693daeebee0c59d40e7b7ad3cbc462dc0558a0d2413398e66128
C2.05R2 independent result SHA-256     12a4eb9bf451d91ba40fb0922a8d4704e109369c736127c9c474284e856998e8

C2.01R1 registry model SHA-256         0bcdd0c48d8cd614ee7a1cb6ee6519df8fb33731bcafd535f3313978dca4343a
C2.02R2 outcome contract SHA-256       901445ca8f0f3f1a8cd04331d3def83f4a29ae3984e5917e723e2402f858f57d
C2.04R1 security re-check result       d1af240f4e6eff32b087295ef259fd4485c13fc0775f8abc24fa630993104f47
```

The user authorized C2.05R3 only for the two residual blocker families:

```text
C2CERT-B03  operation/coverage-scope provenance and replay determinism
C2CERT-B04  composite root/component semantic closure
```

The exact R2 findings repaired here are:

```text
B03-R2-01  NATIVE_SCOPE_COMMITMENT_NOT_EXECUTION_BOUND
B03-R2-02  PROVENANCE_UNIQUENESS_DOMAIN_NOT_PINNED
B04-R2-01  COMPOSITE_ROOT_UNMATCHABLE_TO_ATTEMPT_RESPONSE_SCOPE
```

C2CERT-B01, C2CERT-B02, and C2CERT-B05 are already independently CLOSED and MUST remain closed.

C2.05R3 does not start C2.06, choose providers/vendors, implement adapters, alter C3/C4/C5/C6/C7/C11/C12 ownership, or authorize external side effects.

Construction cannot self-close B03 or B04. Construction status is only `ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK`.

## 2. Effective-contract rule

For the exact B03/B04 clauses amended below, this overlay supersedes conflicting C2.05R1/C2.05R2 clauses.

In particular:

1. R2's rule that a pre-dispatch coverage-only provenance assertion is sufficient authority for C2.05-native request-scope dimensions is superseded.
2. R2's global/claim-discovery interpretation of provenance uniqueness is superseded by the exact attempt-retained authority slot defined below.
3. R2's composite-root requirement that `required_query_semantic_refs[]` and `required_response_semantic_refs[]` be empty is superseded.
4. The R1/R2 per-operation attempted-response equality remains mandatory for a consuming composite-root operation.
5. R2's exact component-scope and partition closure improvements remain mandatory and are strengthened by an explicit semantic-decomposition relation.

No older ambiguous interpretation may remain as a parallel success path.

## 3. Stable-reference extension

C2.05R3 adds exactly three closed C2 stable-ref kinds:

```text
EXECUTED_REQUEST_SEMANTIC_STATE
OPERATION_COVERAGE_AUTHORITY_BINDING
COMPOSITE_SCOPE_DECOMPOSITION_RELATION
```

The stable identity remains:

```text
(authority=C2, ref_kind, logical_id, semantic_revision, content_sha256)
```

Field-kind contract:

```text
ExecutedRequestSemanticState.executed_request_semantic_state_ref
  -> EXECUTED_REQUEST_SEMANTIC_STATE

OperationCoverageAuthorityBinding.operation_coverage_authority_binding_ref
  -> OPERATION_COVERAGE_AUTHORITY_BINDING

OperationCoverageAuthorityBinding.executed_request_semantic_state_ref
  -> EXECUTED_REQUEST_SEMANTIC_STATE

OperationCoverageAuthorityBinding.operation_coverage_provenance_ref
  -> OPERATION_COVERAGE_PROVENANCE

OperationCoverageProvenance.executed_request_semantic_state_ref
  -> EXECUTED_REQUEST_SEMANTIC_STATE

CoverageScopeDefinition.composite_decomposition_relation_ref
  -> COMPOSITE_SCOPE_DECOMPOSITION_RELATION
```

Wrong-kind, dangling, ambiguous, floating, or content-hash-mismatched refs fail closed and cannot support `COMPLETE_FOR_SCOPE`.

## 4. ExecutedRequestSemanticState — B03 execution binding

### 4.1 Purpose

`ExecutedRequestSemanticState` is the exact coverage-relevant semantic request state that the provider request-construction/dispatch path consumes for one exact operation attempt.

It is not a coverage-only assertion and it is not inferred after execution.

A load-bearing C2.05 completeness claim is ineligible unless the exact state is:

1. sealed before provider dispatch;
2. consumed as a semantic input by the actual request-construction/dispatch path;
3. replay-retained for the exact operation/attempt;
4. referenced by the exact operation coverage authority binding;
5. projected exactly into `OperationCoverageProvenance`.

The exact wire field placement is deferred to C2.06. The semantic obligation that the same exact stable ref is both dispatch-consumed and replay-retained is frozen here.

### 4.2 Record shape

```text
ExecutedRequestSemanticState:
  executed_request_semantic_state_ref
  provider_operation_ref
  route_attempt_ref
  parent_semantic_registry_snapshot_ref
  provider_profile_ref
  endpoint_profile_ref
  provider_capability_ref

  capability_requirement_R
  capability_requirement_R_content_sha256

  provider_native_subject_semantic_refs[]
  provider_native_identifier_namespace_refs[]
  coverage_partition_refs[]
  scope_constraint_refs[]
  temporal_scope_dependency_ref?

  request_scope_commitment_state
```

Closed `request_scope_commitment_state`:

```text
SEALED_BEFORE_DISPATCH_FOR_EXECUTION
```

Any other value is ineligible for load-bearing coverage.

### 4.3 Exact dispatch-consumption relation

For an attempt that may later support completeness, define the logical attempt replay surface:

```text
dispatch_consumed_executed_request_semantic_state_ref
replay_retained_executed_request_semantic_state_ref
coverage_authority_binding_ref
```

These are semantic requirements; C2.06 owns their final serialization/wire placement.

A request state is execution-bound iff:

```text
dispatch_consumed_executed_request_semantic_state_ref
  == replay_retained_executed_request_semantic_state_ref
  == OperationCoverageAuthorityBinding.executed_request_semantic_state_ref
  == ExecutedRequestSemanticState.executed_request_semantic_state_ref
```

using full stable-ref identity.

The state provider/endpoint/capability/snapshot/operation/attempt identities MUST equal the actual attempt exactly.

If the dispatch path did not consume this exact state ref, later replay retention cannot retroactively create execution binding.

### 4.4 Coverage-universe completeness of request state

Every provider-native request semantic dimension that can narrow, broaden, partition, filter, key, namespace, or temporally bound the candidate universe relevant to C2.05 completeness MUST be represented in the executed state by one of:

```text
capability_requirement_R
provider_native_subject_semantic_refs[]
provider_native_identifier_namespace_refs[]
coverage_partition_refs[]
scope_constraint_refs[]
temporal_scope_dependency_ref?
```

A coverage-relevant request parameter or semantic condition that affects the candidate universe but is absent from this state makes the attempt:

```text
COVERAGE_INELIGIBLE_REQUEST_SCOPE_UNBOUND
```

The provider operation may still execute under C6/C7 authority, but it cannot later support `COMPLETE_FOR_SCOPE`, absence support, or uniqueness support.

Human labels, raw provider parameter names, SDK defaults, mutable aliases, post-hoc prose, or inferred wildcard scope cannot fill a missing semantic binding.

### 4.5 Coverage-capable certification profile strengthening

For any `ProviderCertificationProfile` whose certification may back a load-bearing C2.05 coverage attestation, `REQUEST_SCOPE_CONFORMANCE` is now a mandatory required `CertificationCheckClass`.

This uses the already-closed parent vocabulary and does not change the B02 total certification classifier.

The check establishes that the certified provider request-construction boundary consumes the exact semantic request state dimensions used to express the provider-native candidate universe. A provider/endpoint/capability whose request construction leaves a coverage-relevant request dimension outside the executed state cannot be coverage-capable `CERTIFIED`.

This is conformance of request construction, not C5 verification and not C6 dispatch authority.

## 5. R3 amendment to OperationCoverageProvenance — B03

R2's exact `CapabilityRequirement R` and C2.02R2 attempted-response provenance remain authoritative.

`OperationCoverageProvenance` now additionally requires:

```text
executed_request_semantic_state_ref
```

For load-bearing use:

```text
provenance.executed_request_semantic_state_ref
  == exact attempt-retained ExecutedRequestSemanticState ref

provenance.provider_native_subject_semantic_refs
  == executed_state.provider_native_subject_semantic_refs

provenance.provider_native_identifier_namespace_refs
  == executed_state.provider_native_identifier_namespace_refs

provenance.coverage_partition_refs
  == executed_state.coverage_partition_refs

provenance.scope_constraint_refs
  == executed_state.scope_constraint_refs

provenance.temporal_scope_dependency_ref
  == executed_state.temporal_scope_dependency_ref
  with BOTH_ABSENT or EXACT_SAME_REF semantics
```

Additionally:

```text
provenance.capability_requirement_R
  == executed_state.capability_requirement_R
  == exact replay-retained C2.01 CapabilityRequirement R

provenance.capability_requirement_R_content_sha256
  == executed_state.capability_requirement_R_content_sha256
  == SHA256(canonical_bytes(R))
```

The R2 attempted-response requirement remains:

```text
provenance.attempted_response_semantic_refs
  == exact C2.02R2 stored/recomputed attempted_response_semantic_refs
```

Thus a coverage-only pre-dispatch statement that disagrees with the request state actually consumed by dispatch is not load-bearing.

## 6. OperationCoverageAuthorityBinding — B03 uniqueness authority

### 6.1 Exact authority domain

C2.05R3 replaces global provenance-claim discovery with one exact attempt-retained authority slot.

```text
OperationCoverageAuthorityBinding:
  operation_coverage_authority_binding_ref
  provider_operation_ref
  route_attempt_ref
  executed_request_semantic_state_ref
  operation_coverage_provenance_ref
  authority_binding_state
```

Closed `authority_binding_state`:

```text
SEALED_IN_ATTEMPT_REPLAY_SURFACE
```

For load-bearing coverage, the exact operation/attempt replay surface MUST retain exactly one `coverage_authority_binding_ref`.

That single retained ref is the entire authority domain for provenance selection.

### 6.2 Deterministic uniqueness rule

The exact rule is:

```text
authoritative_provenance_ref =
  exact_resolve(
    exact_attempt_replay.coverage_authority_binding_ref
  ).operation_coverage_provenance_ref
```

No global store scan, index scan, namespace scan, claim search, "all records with the same operation ID" search, mutable registry lookup, or later object discovery is permitted.

A later or unrelated content-addressed object that claims the same `(provider_operation_ref, route_attempt_ref)` but is not referenced by the exact attempt-retained authority binding has **zero load-bearing authority** and cannot alter historical replay.

Failure cases:

```text
no attempt-retained authority ref      -> NO_COMPLETE_FOR_SCOPE_SUPPORT
multiple authority refs in replay slot -> INVALID
wrong-kind/dangling/hash mismatch      -> INVALID
binding operation/attempt mismatch     -> INVALID
binding executed-state mismatch        -> INVALID
binding provenance mismatch            -> INVALID
```

This rule supersedes R2 wording that "multiple claiming provenance refs" discovered outside the attempt-retained authority domain can invalidate history.

## 7. R3 operation-scope support predicate — B03

For all non-composite and composite-consuming provider operations, the effective operation scope predicate is:

```text
operation_scope_binding_valid =
  exact attempt-retained coverage authority binding resolves
  AND exact executed request semantic state resolves
  AND dispatch consumed that exact state ref
  AND replay retained that exact state ref
  AND coverage-capable certification requires REQUEST_SCOPE_CONFORMANCE
  AND provenance is the exact authoritative provenance from the binding
  AND provenance exactly projects executed request state
  AND provenance R equals exact replay-retained R
  AND provenance attempted-response set equals exact C2.02R2 A
  AND OperationCoverageScopeBinding exactly projects provenance
  AND OperationCoverageScopeBinding exactly matches CoverageScopeDefinition
```

Any false, unresolved, ambiguous, or mismatched clause makes the operation ineligible for load-bearing completeness support.

## 8. Composite model choice — B04

C2.05R3 chooses the **explicit immutable machine-checkable root-to-component semantic-decomposition relation** model.

It does not choose an aggregate-root model.

The reason is to preserve the parent/R1 `CoverageAttestationRecord` and `CoverageEvidenceBundle` operation-binding shape while removing the R2 contradiction.

### 8.1 R2 root neutralization is superseded

For `COMPOSITE_EXPLICIT_CLOSURE`, R2's rules:

```text
root.required_query_semantic_refs    MUST be empty
root.required_response_semantic_refs MUST be empty
```

are superseded.

A composite root is again an exact operation-bound `CoverageScopeDefinition`.

Therefore:

```text
root.required_query_semantic_refs
  == consuming OperationCoverageScopeBinding.required_query_semantic_refs

root.required_response_semantic_refs
  == consuming OperationCoverageScopeBinding.attempted_response_semantic_refs
  == exact C2.02R2 attempted_response_semantic_refs A
```

Since C2.02R2 `A` always contains the endpoint primary response semantic for a valid dispatched attempt, a load-bearing composite root's required response set is necessarily non-empty.

No composite success path may use an empty root response set for a dispatched attempt.

### 8.2 Composite relation field

A `CoverageScopeDefinition` used as a `COMPOSITE_EXPLICIT_CLOSURE` root additionally requires:

```text
composite_component_scope_refs[]       non-empty exact canonical set
composite_decomposition_relation_ref   exact COMPOSITE_SCOPE_DECOMPOSITION_RELATION
```

For non-composite methods:

```text
composite_component_scope_refs[]       MUST be empty
composite_decomposition_relation_ref   MUST be absent
```

## 9. CompositeScopeDecompositionRelation — B04

### 9.1 Record shape

```text
CompositeScopeDecompositionRelation:
  composite_decomposition_relation_ref
  parent_semantic_registry_snapshot_ref
  root_coverage_scope_ref
  root_required_query_semantic_refs[]
  root_required_response_semantic_refs[]
  component_scope_refs[]
  query_decomposition_entries[]
  response_decomposition_entries[]
  decomposition_state
```

Closed `decomposition_state`:

```text
EXACT_MACHINE_CLOSED_DECOMPOSITION
```

Each `CompositeSemanticDecompositionEntry` is:

```text
root_semantic_ref
component_semantic_bindings[]
```

Each `component_semantic_binding` is:

```text
component_scope_ref
component_semantic_ref
```

The list container determines whether the entry is on the QUERY or RESPONSE axis; cross-axis substitution is forbidden.

### 9.2 Exact root binding

The relation is valid only if:

```text
relation.root_coverage_scope_ref == root.coverage_scope_ref
relation.parent_semantic_registry_snapshot_ref
  == root.parent_semantic_registry_snapshot_ref

canonical(relation.component_scope_refs)
  == canonical(root.composite_component_scope_refs)

canonical(relation.root_required_query_semantic_refs)
  == canonical(root.required_query_semantic_refs)

canonical(relation.root_required_response_semantic_refs)
  == canonical(root.required_response_semantic_refs)
```

All participating provider semantic refs exact-resolve under the same pinned parent semantic registry snapshot.

### 9.3 Exact axis decomposition

For QUERY and RESPONSE independently:

1. every root semantic ref appears as exactly one decomposition-entry key;
2. no unknown/extra root key is permitted;
3. every component binding names one exact member of `component_scope_refs`;
4. the bound component semantic ref is an exact member of that component scope's corresponding query or response semantic set;
5. every component semantic ref in every component scope's corresponding axis appears exactly once across the relation;
6. one component semantic ref cannot be assigned to two different root semantic keys;
7. a root semantic key may map to one or more component semantic refs;
8. empty component QUERY sets are permitted and contribute no query binding;
9. component RESPONSE sets for ordinary operation-provenanced components remain subject to C2.02R2 and therefore contain their exact attempted-response semantics;
10. missing, duplicate, extra, wrong-axis, unresolved, wrong-scope, or hash-mismatched bindings fail closed.

The relation is the explicit C2.05 semantic decomposition authority. Implementations may not infer decomposition from provider names, query text, response schema similarity, labels, marketing documentation, set size, or human judgment.

Concrete provider-specific relation instances remain deferred under `C2.OPEN-015`.

### 9.4 No circular semantic shortcut

A relation cannot establish validity merely by pointing to itself or by restating the root component list.

Validity requires the exact set-equality and per-axis total/disjoint membership predicates above against the already-content-addressed root/component scopes.

Nested `COMPOSITE_EXPLICIT_CLOSURE` components remain forbidden.

## 10. Composite closure predicate — B04

The R2 exact component and partition closure rules remain, with the semantic-decomposition relation added as a mandatory independent predicate.

For a composite root:

```text
composite_support_valid =
  root operation_scope_binding_valid
  AND exact composite_decomposition_relation_ref resolves
  AND decomposition_relation_valid
  AND exact one complete/ACTIVE/CERTIFIED component attestation
      for every root composite_component_scope_ref
  AND no extra component scope
  AND all inherited non-query/response compatibility predicates pass
  AND no nested composite
  AND component operation provenance/support is valid
  AND partition closure passes when root partitions are non-empty
  AND no-partition closure passes when root partitions are empty
```

With root partitions:

```text
exact component-scope closure
AND exact semantic decomposition closure
AND exact pairwise-disjoint partition union to root partition set
```

are all mandatory.

With no root partitions:

```text
all component scope/binding partition sets empty
AND exact component-scope bijection
AND exact semantic decomposition closure
```

are all mandatory.

Partition closure cannot substitute for semantic decomposition; semantic decomposition cannot substitute for partition closure.

## 11. C2.02 attempted-response invariant

For the consuming composite-root operation:

```text
A = canonical_set(
    { E.response_semantics.response_semantic_ref }
    ∪ P.required_response_semantic_refs
    ∪ R.required_response_semantic_refs
)
```

remains authoritative.

The root scope MUST satisfy:

```text
root.required_response_semantic_refs == A
```

Therefore the endpoint primary response semantic is present in the root response set.

A composite relation that omits that root semantic, maps it on the wrong axis, or cannot provide a complete exact component decomposition for it is invalid.

This directly removes the R2 empty-root contradiction.

## 12. Closed-blocker non-regression

R3 does not weaken:

- B01 `COVERAGE_EVIDENCE_BUNDLE` type/ref/check/evidence-role closure;
- B02 certification decision precedence;
- B05 total coverage-classification precedence;
- stored-vs-recomputed classification consistency;
- C1 eligibility-only boundary;
- C2.04R1 secure-ingress semantics.

The B03 strengthening that `REQUEST_SCOPE_CONFORMANCE` is mandatory for coverage-capable certification profiles uses the existing closed B02 check vocabulary and does not alter B02 decision totality.

## 13. Ownership boundaries

Unchanged:

- C1 owns final normalization/identity/resolution/NO_MATCH/uniqueness.
- C3 owns retry/quota/cache/freshness/coalescing/LKG.
- C4 owns PIT/revision/available_from/temporal reconstructability.
- C5 owns evidence fitness/verification/independence/conflict.
- C6 owns capability/policy/trusted-intent/destination/side-effect authority.
- C7 owns orchestration/budgets/cancellation/durable continuation.
- C11 owns persistence implementation.
- C12 owns validation/promotion/release.
- C2.06 owns exact cross-contract wire placement, including serialization of the exact executed-request-state and coverage-authority refs.
- C2.07 owns executable schema/validators and must encode these semantics, not invent them.
- Concrete provider/vendor configuration and concrete decomposition-relation instances remain deferred under C2.OPEN-015.
- C2.04R1 secure-ingress semantics remain unchanged.

## 14. Construction blocker disposition

Construction may record only:

```text
C2CERT-B01 = CLOSED_UNCHANGED
C2CERT-B02 = CLOSED_UNCHANGED
C2CERT-B03 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
C2CERT-B04 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
C2CERT-B05 = CLOSED_UNCHANGED
```

## 15. Exit gate

C2.05R3 construction stops at:

```text
C2.05R3 Independent Certification Re-Check
```

The independent re-check must re-run at least:

```text
C2-471
C2-481
C2-540
C2-557
C2-584
C2-585
```

plus all C2.05R3 adversarial obligations and all previously passing C2.05/R1/R2 and C2.04 security non-regression surfaces.

C2.06, production implementation, provider/vendor configuration, and external/PAPER/LIVE side effects remain `NOT_AUTHORIZED`.
