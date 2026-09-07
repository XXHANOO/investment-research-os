# C2.05R2 — Operation-Scope Provenance and Composite-Root Universe Scoped Repair Contract Candidate

Generated: 2026-09-07T07:10:00Z

Status: `SCOPED_REPAIR_CANDIDATE_PENDING_INDEPENDENT_CERTIFICATION_RECHECK`

Production implementation: `NOT_AUTHORIZED`

Provider/vendor configuration: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

## 1. Repair authority and exact scope

C2.05R2 is a narrow repair overlay on the effective C2.05 + C2.05R1 contract.

Exact parent pins:

```text
C2.05 parent contract SHA-256          3642588dcc22a7564d55a9a72d3e6e328b007649005c866e7831dfa4b8571d4c
C2.05R1 repair contract SHA-256        267c83480aa909e74cb5d87c54512878c3c9c7128fce8a394fb63f39c6ed2bcb
C2.05R1 logical model SHA-256          777b7ddc3530a088a127f3becb74bd1f644fc25f83703cb27799423671752262
C2.05R1 acceptance delta SHA-256       24819163ea5c835ffcee5610f8d37bc8268a3621c62cf582aed85deaf339b749
C2.05R1 decision ledger SHA-256        19e6bd0a48b153de04a957b7176052af2947ec8e9bf7f7bf9f1c0ab05cbe5566
C2.05R1 independent re-check report    2b829b9a3af45eade91efee1fea786a9b26128c39be0f4662953897bea0635f8
C2.05R1 independent re-check result    59578acccb8906637360f24c7fe190a3a6e6b92098ddf03c30a5133b9d5767bf

C2.01R1 registry model SHA-256         0bcdd0c48d8cd614ee7a1cb6ee6519df8fb33731bcafd535f3313978dca4343a
C2.02R2 outcome contract SHA-256       901445ca8f0f3f1a8cd04331d3def83f4a29ae3984e5917e723e2402f858f57d
C2.04R1 security re-check result       d1af240f4e6eff32b087295ef259fd4485c13fc0775f8abc24fa630993104f47
```

The user authorized C2.05R2 only for the two residual blockers:

```text
C2CERT-B03  OPERATION_SCOPE_BINDING_PROVENANCE_NOT_MACHINE_CLOSED
C2CERT-B04  COMPOSITE_ROOT_COMPONENT_SCOPE_RELATION_NOT_CLOSED
```

C2CERT-B01, C2CERT-B02, and C2CERT-B05 are already independently CLOSED and MUST NOT be reopened except for direct non-regression checks.

C2.05R2 does not start C2.06, choose providers/vendors, implement adapters, change C3/C4/C5/C6/C7/C11 ownership, or authorize external side effects.

Construction cannot self-close B03 or B04. Their construction status is only `ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK`.

## 2. Effective-contract rule

For B03/B04 and the exact fields amended below, this overlay supersedes conflicting or underdefined C2.05/C2.05R1 clauses.

All non-conflicting parent clauses remain effective unchanged.

No implementation may use the older R1 self-described operation-binding path or the older composite root query/response interpretation as a parallel success path.

## 3. Stable-reference extension — B03

C2.05R2 adds exactly one closed C2 stable-ref kind:

```text
OPERATION_COVERAGE_PROVENANCE
```

The stable identity remains:

```text
(authority=C2, ref_kind, logical_id, semantic_revision, content_sha256)
```

Field-kind contract:

```text
OperationCoverageProvenance.operation_coverage_provenance_ref
  -> OPERATION_COVERAGE_PROVENANCE

OperationCoverageScopeBinding.operation_coverage_provenance_ref
  -> OPERATION_COVERAGE_PROVENANCE
```

Wrong-kind, dangling, ambiguous, floating, or content-hash-mismatched provenance refs fail closed and cannot support `COMPLETE_FOR_SCOPE`.

## 4. Authoritative OperationCoverageProvenance — B03

### 4.1 Purpose

`OperationCoverageProvenance` is the single C2.05 semantic provenance record for later completeness claims about one exact provider operation / route attempt.

It is not a second copy of an attested scope. It is the replay-retained bridge from the actual operation semantics into C2.05 coverage validation.

A load-bearing coverage attestation MUST NOT be supported by a post-hoc scope binding that cannot be traced to this exact provenance record.

### 4.2 Record shape

```text
OperationCoverageProvenance:
  operation_coverage_provenance_ref
  provider_operation_ref
  route_attempt_ref
  parent_semantic_registry_snapshot_ref
  provider_profile_ref
  endpoint_profile_ref
  provider_capability_ref

  capability_requirement_R
  capability_requirement_R_content_sha256

  attempted_response_semantic_refs[]

  provider_native_subject_semantic_refs[]
  provider_native_identifier_namespace_refs[]
  coverage_partition_refs[]
  scope_constraint_refs[]
  temporal_scope_dependency_ref?

  provenance_commitment_state
```

Closed `provenance_commitment_state`:

```text
SEALED_FOR_COVERAGE_BEFORE_DISPATCH
```

Any other value is invalid for load-bearing coverage support.

### 4.3 Exact authoritative sources

For one operation attempt:

```text
S = exact pinned C2.01 REGISTRY_SNAPSHOT
R = exact replay-retained C2.01 CapabilityRequirement for this attempt
P = exact resolved ProviderCapabilityDefinition under S
E = exact resolved endpoint profile under S
A = exact C2.02R2 attempted_response_semantic_refs[] for this attempt
```

The provenance record MUST satisfy:

```text
parent_semantic_registry_snapshot_ref == S
provider_profile_ref  == exact provider profile used by the attempt
endpoint_profile_ref  == P.endpoint_semantic_profile_ref
provider_capability_ref == exact capability used by the attempt

capability_requirement_R == R byte-for-byte under the canonical C2 value encoding
capability_requirement_R_content_sha256 == SHA256(canonical_bytes(R))

attempted_response_semantic_refs == A
A == attempted_response_semantic_refs(P, E, R, S)
```

The C2.02R2 derivation remains authoritative and is not redefined here.

If the exact replay-retained R or A is missing, non-unique, unresolved, or inconsistent, coverage provenance is invalid and the operation can never support `COMPLETE_FOR_SCOPE`.

### 4.4 C2.05-native request-scope dimensions

C2.01 `CapabilityRequirement R` does not carry every C2.05 coverage-universe dimension. Therefore C2.05R2 freezes the remaining dimensions as part of the pre-dispatch provenance commitment itself:

```text
provider_native_subject_semantic_refs[]
provider_native_identifier_namespace_refs[]
coverage_partition_refs[]
scope_constraint_refs[]
temporal_scope_dependency_ref?
```

These fields are authoritative for C2.05 coverage only if all of the following hold:

1. the provenance record is the exact `operation_coverage_provenance_ref` replay-retained by the operation/attempt for later coverage use;
2. the provenance commitment is sealed as `SEALED_FOR_COVERAGE_BEFORE_DISPATCH`;
3. every ref exact-resolves under the same pinned parent semantic registry snapshot where applicable;
4. canonical-set rules are satisfied;
5. no post-dispatch replacement, alternate provenance ref, mutable alias, human label, inferred wildcard, or transitive guessed scope is allowed;
6. the same exact provenance ref is later consumed by `OperationCoverageScopeBinding`.

An operation may execute without a C2.05 coverage provenance commitment, but then it is permanently ineligible to support C2.05 `COMPLETE_FOR_SCOPE`, absence support, or uniqueness support.

This rule does not grant dispatch authority and does not change C6/C7 ownership.

### 4.5 Canonicalization

All stable-ref lists in the provenance record use the existing C2 exact canonical-set discipline:

```text
- exact resolution;
- exact duplicate dedupe;
- conflicting same-logical-ID revision/hash invalid;
- deterministic ascending order by full stable-ref identity.
```

`capability_requirement_R` uses the exact C2.01R1 five-field normalized value:

```text
access_pattern_family
required_observation_family_refs[]
required_query_semantic_refs[]
required_response_semantic_refs[]
required_semantic_feature_refs[]
```

Each list inside R is canonicalized under the parent C2.01 contract before canonical byte encoding.

## 5. R2 amendment to OperationCoverageScopeBinding — B03

`OperationCoverageScopeBinding` now additionally requires:

```text
operation_coverage_provenance_ref
```

The binding is load-bearing only if that ref resolves to exactly one valid `OperationCoverageProvenance` for the same `provider_operation_ref` and `route_attempt_ref`.

The R1 duplicated semantic fields are no longer free-standing assertions. They are a deterministic projection of the provenance record:

```text
binding.access_pattern_family
  == provenance.capability_requirement_R.access_pattern_family

binding.required_observation_family_refs
  == provenance.capability_requirement_R.required_observation_family_refs

binding.required_query_semantic_refs
  == provenance.capability_requirement_R.required_query_semantic_refs

binding.required_semantic_feature_refs
  == provenance.capability_requirement_R.required_semantic_feature_refs

binding.attempted_response_semantic_refs
  == provenance.attempted_response_semantic_refs

binding.provider_native_subject_semantic_refs
  == provenance.provider_native_subject_semantic_refs

binding.provider_native_identifier_namespace_refs
  == provenance.provider_native_identifier_namespace_refs

binding.coverage_partition_refs
  == provenance.coverage_partition_refs

binding.scope_constraint_refs
  == provenance.scope_constraint_refs

binding.temporal_scope_dependency_ref
  == provenance.temporal_scope_dependency_ref
  with BOTH_ABSENT or EXACT_SAME_REF semantics
```

The binding's provider/endpoint/capability/parent snapshot refs MUST also exactly equal the provenance record.

Only after all provenance equalities pass may the binding be compared to `CoverageScopeDefinition`.

Thus the exact predicate is:

```text
operation_scope_binding_valid =
  provenance_valid
  AND binding_exactly_projects(provenance)
  AND binding_exactly_matches_required_coverage_scope
```

A matching `required_coverage_scope_ref` or an internally self-consistent binding record is never sufficient by itself.

### 5.1 No post-hoc minting success path

If the operation/attempt did not replay-retain the exact provenance ref committed before dispatch, a later minted binding/provenance pair cannot retroactively create coverage support.

If multiple provenance refs claim the same operation/attempt, load-bearing coverage support is `INVALID`.

## 6. Composite root-universe repair — B04

### 6.1 Design choice

C2.05R2 chooses the stricter closure form permitted by the R1 independent review:

> for `COMPOSITE_EXPLICIT_CLOSURE`, the root composite universe is exactly the canonical set of component `CoverageScopeDefinition` refs.

Therefore root query/response semantics are not an independent parallel universe dimension for a composite root.

### 6.2 Composite root query/response neutralization

For a `CoverageScopeDefinition` used as the root of a `COMPOSITE_EXPLICIT_CLOSURE` method:

```text
required_query_semantic_refs[]    MUST be empty
required_response_semantic_refs[] MUST be empty
composite_component_scope_refs[]  MUST be non-empty
```

For all non-composite coverage methods, this R2 rule does not alter the parent query/response requirements and `composite_component_scope_refs[]` remains empty.

A composite root with any non-empty root query or response semantic ref set is structurally invalid for composite completeness.

### 6.3 Exact composite root universe

Define:

```text
CompositeRootUniverse(root) =
  canonical_set(root.composite_component_scope_refs[])
```

This exact set is the entire query/response decomposition authority for the composite root.

There is no separate inferred root query universe, no separate inferred root response universe, no human-label relation, and no provider-name equivalence path.

Each component scope retains its own exact query and response semantic refs as part of its own immutable `CoverageScopeDefinition`.

### 6.4 Composite closure with root partitions

If `root.coverage_partition_refs[]` is non-empty, completeness requires BOTH:

```text
A. exact component-scope closure:
   exactly one complete, ACTIVE, CERTIFIED component attestation
   for every member of CompositeRootUniverse(root),
   and no extra component scope;

B. exact partition closure:
   each component binding's covered_partition_refs[]
   equals that component scope's partition set,
   component covered sets are pairwise disjoint,
   canonical union == root.coverage_partition_refs[].
```

Component-scope closure and partition closure are independent mandatory predicates. Partition union alone cannot close the composite.

### 6.5 Composite closure without root partitions

If `root.coverage_partition_refs[]` is empty:

```text
- every component scope partition set is empty;
- every component binding partition set is empty;
- exact component-scope-set bijection against CompositeRootUniverse(root)
  is the complete gap proof.
```

This is valid because R2 defines the root composite universe itself as exactly that canonical component-scope set and forbids independent root query/response semantics.

### 6.6 Component requirements retained

All R1 component requirements remain effective:

```text
- each component attestation is COMPLETE_FOR_SCOPE;
- each component is ACTIVE in the exact registry snapshot;
- each provider certification is CERTIFIED in the same pinned registry snapshot;
- component_attestation.coverage_scope_ref == component_scope_ref;
- repeated component attestation refs invalid;
- repeated component scope refs invalid;
- nested COMPOSITE_EXPLICIT_CLOSURE components forbidden;
- same parent semantic registry snapshot;
- exact equality for observation-family, semantic-feature,
  provider-native subject, identifier namespace, scope constraints,
  and temporal dependency dimensions required by R1;
- unresolved/wrong-kind/hash-mismatched refs fail closed.
```

### 6.7 No inferred equivalence

The following are explicitly non-authoritative:

```text
provider names
endpoint names
human-readable labels
asset-class labels
query text similarity
response schema similarity
marketing documentation
set-size similarity
manual declarations outside the content-addressed component-scope set
```

If a desired composite cannot be represented as the exact component-scope set under this rule, a new exact root/component scope construction must be minted; implementations may not infer coverage.

## 7. Repaired C2.05 support predicate

The effective `coverage_support_valid` predicate retains all C2.05/R1 requirements and additionally requires:

```text
exact operation_coverage_provenance_ref resolves
AND provenance_commitment_state == SEALED_FOR_COVERAGE_BEFORE_DISPATCH
AND provenance matches exact operation/attempt
AND provenance.capability_requirement_R == replay-retained R
AND provenance.attempted_response_semantic_refs == exact C2.02R2 attempted set
AND binding_exactly_projects(provenance)
AND binding_exactly_matches_required_coverage_scope
AND, for composite roots, the R2 root-universe rules pass
```

Then and only then may a recomputed `COMPLETE_FOR_SCOPE` attestation support the existing C2 eligibility signals.

No C1 conclusion is created by this repair.

## 8. B01/B02/B05 non-regression

R2 does not change:

- `COVERAGE_EVIDENCE_BUNDLE` type/ref/check closure;
- certification decision precedence;
- required/optional certification check semantics;
- total coverage classification precedence;
- stored-vs-recomputed classification consistency;
- C1 eligibility-only boundary.

Any implementation interpreting R2 as relaxing those surfaces is non-conformant.

## 9. Ownership boundaries

Unchanged:

- C1 owns final normalization/identity/resolution/NO_MATCH/uniqueness.
- C3 owns retry/quota/cache/freshness/coalescing/LKG.
- C4 owns PIT/revision/available_from/temporal reconstructability.
- C5 owns evidence fitness/verification/independence/conflict.
- C6 owns capability/policy/trusted-intent/destination/side-effect authority.
- C7 owns orchestration/budgets/cancellation/durable continuation.
- C11 owns persistence implementation.
- C12 owns validation/promotion/release.
- C2.06 owns exact cross-contract wire placement, including where the provenance ref/value is serialized.
- C2.07 owns executable schema/validators and must encode these semantics, not invent them.
- C2.04R1 secure-ingress semantics remain unchanged.
- Concrete provider/vendor configuration remains deferred under C2.OPEN-015.

## 10. Construction blocker disposition

Construction may record only:

```text
C2CERT-B03 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
C2CERT-B04 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
```

Previously closed blockers remain:

```text
C2CERT-B01 = CLOSED_UNCHANGED
C2CERT-B02 = CLOSED_UNCHANGED
C2CERT-B05 = CLOSED_UNCHANGED
```

## 11. Exit gate

C2.05R2 construction stops at:

```text
C2.05R2 Independent Certification Re-Check
```

The independent re-check must re-run at least:

```text
C2-437
C2-438
C2-471
C2-481
C2-525
C2-539
C2-540
```

plus all C2.05R2 adversarial obligations and parent PASS-surface non-regression.

C2.06, production implementation, provider/vendor configuration, and external/PAPER/LIVE side effects remain `NOT_AUTHORIZED`.
