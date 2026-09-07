# C2.05R1 Independent Certification Re-Check Report

Generated: 2026-09-07T06:53:57Z

Review type: `INDEPENDENT_CERTIFICATION_RECHECK`

Candidate under review: `C2.05R1 — Provider Certification / Completeness / Coverage Scoped Repair`

## 1. Independent review posture

This re-check is independent of C2.05R1 construction self-checks. `C2_05R1_CONSTRUCTION_VALIDATION`, construction summary, candidate selection, stage report, and decision-ledger closure labels are treated only as candidate metadata. They are not used as independent evidence that C2CERT-B01..B05 are closed.

The review re-read the exact C2.05 parent contract, the C2.05 Independent Certification Review failure report/result, the C2.05R1 repair contract, logical model, acceptance delta, and the parent C2.01R1/C2.02R2 semantic authorities needed to test operation-scope provenance.

The re-check adversarially evaluated:

- the 8 parent C2.05 obligations that previously failed;
- all 68 C2.05R1 obligations `C2-488..C2-555`;
- preservation of the other 78 parent C2.05 PASS obligations;
- preservation of C2.04 effective acceptance `C2-289..C2-401`;
- deterministic replay and fail-closed behavior;
- C1/C3/C4/C5/C6/C7/C11/C12 ownership boundaries.

No C2.06 construction, provider/vendor selection, production implementation, or external/PAPER/LIVE side effect is authorized by this review.

## 2. Exact reviewed pins

```text
C2.05 parent contract                 3642588dcc22a7564d55a9a72d3e6e328b007649005c866e7831dfa4b8571d4c
C2.05 parent logical model            0a6d7c4037c04ca04f87994507afb722661dbd9450a115492238b9d5dd9c776c
C2.05 parent acceptance delta         62714c720e2a9d6f24f066533ddac9c84f3360a6bff2cbe4d9aacbb9617cff6f
C2.05 parent decision ledger          519cfd630f8f60772fe649b98297c2e32c2a912f9b36b2c59567d1e56fc57366
C2.05 independent review report       17853fd3e93d9a7d0cb611564004e85865d2fda20e05ee1ad885a249f2705c04
C2.05 independent review result       8edddb75c2fa556ecb1d688b1f543057e99171441e7ea3ec4466c02c7ddb0a10

C2.05R1 repair contract               267c83480aa909e74cb5d87c54512878c3c9c7128fce8a394fb63f39c6ed2bcb
C2.05R1 logical model                 777b7ddc3530a088a127f3becb74bd1f644fc25f83703cb27799423671752262
C2.05R1 acceptance delta              24819163ea5c835ffcee5610f8d37bc8268a3621c62cf582aed85deaf339b749
C2.05R1 decision ledger               19e6bd0a48b153de04a957b7176052af2947ec8e9bf7f7bf9f1c0ab05cbe5566
C2.05R1 candidate archive commit      76e956af847b96b36d1f8d04ccc779c88d9edb21
C2.05R1 candidate subtree             d8f6ba9ef1ec33ce2b90ad96f5433383a185060f

C2.01R1 registry model                0bcdd0c48d8cd614ee7a1cb6ee6519df8fb33731bcafd535f3313978dca4343a
C2.02R2 outcome contract              901445ca8f0f3f1a8cd04331d3def83f4a29ae3984e5917e723e2402f858f57d
C2.04R1 security re-check result      d1af240f4e6eff32b087295ef259fd4485c13fc0775f8abc24fa630993104f47
```

## 3. Final verdict

`FAIL — C2.05R1 REPAIR_REQUIRED_NOT_FROZEN`

The R1 repair successfully closes C2CERT-B01, C2CERT-B02, and C2CERT-B05 at the reviewed semantic level. It also materially improves B03 and B04. Two residual load-bearing defects remain:

```text
C2CERT-B01 = CLOSED
C2CERT-B02 = CLOSED
C2CERT-B03 = OPEN
C2CERT-B04 = OPEN
C2CERT-B05 = CLOSED

C2.05R1 = REPAIR_REQUIRED_NOT_FROZEN
C2.06 = NOT_STARTED / NOT_AUTHORIZED
Production implementation = NOT_AUTHORIZED
External/PAPER/LIVE side effects = NOT_AUTHORIZED
```

## 4. Blocker findings

### 4.1 C2CERT-B01 — CLOSED

The repair now freezes a dedicated `COVERAGE_EVIDENCE_BUNDLE` stable-ref kind, exact field-kind binding for `coverage_evidence_bundle_ref`, a replayable `CoverageEvidenceBundle`, a closed method-check vocabulary, a closed evidence-role vocabulary, method-family-specific termination-rule values, one closed truncation rule, exact bundle subject binding, and fail-closed ref handling.

The previously ambiguous coverage evidence carrier no longer admits a parallel private-kind or convention-based success path at the C2.05 contract layer.

Adversarial vectors checked included wrong-kind/dangling/floating/hash-mismatched evidence bundle refs, private check classes, private evidence roles, bundle/attestation subject mismatch, and use of quarantined/rejected provider material.

Result: **CLOSED**.

### 4.2 C2CERT-B02 — CLOSED

The repair defines a total certification decision function:

```text
structural invalidity -> INDETERMINATE
else any required FAIL -> NOT_CERTIFIED
else any required INDETERMINATE -> INDETERMINATE
else -> CERTIFIED
```

Required and optional class sets are closed, duplicate-free, and disjoint; undeclared classes are invalid; optional results are diagnostic only; check-result ordering is non-load-bearing.

Adversarial vectors checked:

```text
FAIL + INDETERMINATE -> NOT_CERTIFIED
FAIL + missing required class -> INDETERMINATE
FAIL + duplicate result -> INDETERMINATE
all required PASS + optional FAIL -> CERTIFIED
permuted check_results[] -> same decision
```

No same pinned valid/invalid bundle admits two certification decisions.

Result: **CLOSED**.

### 4.3 C2CERT-B03 — OPEN

Residual finding:

`OPERATION_SCOPE_BINDING_PROVENANCE_NOT_MACHINE_CLOSED`

R1 introduces `OperationCoverageScopeBinding` and an exact field-by-field equality predicate against `CoverageScopeDefinition`. This is useful, but the binding record is still not normatively derived from, nor compared against, the authoritative replay-retained operation requirement/outcome state.

C2.02R2 already freezes an exact replay-retained `CapabilityRequirement R` for each dispatched attempt and derives `attempted_response_semantic_refs[]` from the tuple `(S, provider_capability_ref, endpoint profile, R)`.

R1 does not require:

```text
OperationCoverageScopeBinding.access_pattern_family
  == R.access_pattern_family

OperationCoverageScopeBinding.required_observation_family_refs[]
  == R.required_observation_family_refs[]

OperationCoverageScopeBinding.required_query_semantic_refs[]
  == R.required_query_semantic_refs[]

OperationCoverageScopeBinding.required_semantic_feature_refs[]
  == R.required_semantic_feature_refs[]

OperationCoverageScopeBinding.attempted_response_semantic_refs[]
  == the exact C2.02R2 stored/derived attempted_response_semantic_refs[]
```

Nor does it freeze an equivalent authoritative derivation source for provider-native subject/identifier scope, partitions, scope constraints, or the temporal dependency.

Clause Q states that `provider_operation_ref` and `route_attempt_ref` identify the exact operation/attempt, but identity refs alone do not prove that the duplicated semantic fields in the binding record were derived from that operation.

Adversarial counterexample:

```text
Actual replay-retained R:
  required_query_semantic_refs = [QUERY_B]

Actual C2.02R2 attempted_response_semantic_refs:
  [RESPONSE_B]

Minted OperationCoverageScopeBinding:
  provider_operation_ref = actual operation
  route_attempt_ref = actual attempt
  required_query_semantic_refs = [QUERY_A]
  attempted_response_semantic_refs = [RESPONSE_A]
  required_coverage_scope_ref = scope_A

scope_A:
  required_query_semantic_refs = [QUERY_A]
  required_response_semantic_refs = [RESPONSE_A]
```

All R1 equality checks between the binding and `scope_A` can pass while the actual operation executed under `QUERY_B / RESPONSE_B`. The contract contains no mandatory comparison from the binding back to authoritative `R` / the C2.02R2 attempted-response record.

Therefore `required_coverage_scope_ref + operation_coverage_scope_binding_ref` is still not a machine-closed proof that the executed operation had the attested scope.

Failed obligations:

```text
C2-437
C2-438
C2-481
C2-525
```

R2 requirement:

Freeze exact semantic provenance for every load-bearing operation-scope field. At minimum, bind the coverage-scope validation to the exact replay-retained C2.01 `CapabilityRequirement R` and the exact C2.02R2 attempted-response semantic set, and define authoritative sources/derivations for provider-native subject/identifier scope, partitions, constraints, and temporal dependency. C2.06 may serialize those bindings later, but it must not invent the missing semantic provenance.

### 4.4 C2CERT-B04 — OPEN

Residual finding:

`COMPOSITE_ROOT_COMPONENT_SCOPE_RELATION_NOT_CLOSED`

R1 successfully closes partition exhaustion as a one-component-to-one-partition bijection and closes duplicate/missing/extra/nested/unresolved component cases.

The residual defect is in `COMPOSITE_EXPLICIT_CLOSURE`.

The root-to-component compatibility predicate requires equality for observation families, semantic features, provider-native subjects/identifier namespaces, constraints, and temporal dependency. But it explicitly permits provider-specific query/response semantics to differ solely because each component scope is enumerated in `composite_component_scope_refs[]`.

That enumeration is an exact membership declaration; it is not a semantic proof that the component query/response universes cover the root query/response universe.

Adversarial counterexample with no root partitions:

```text
root scope:
  required_query_semantic_refs = [US_EQUITY_QUERY]
  required_response_semantic_refs = [US_EQUITY_RESPONSE]
  composite_component_scope_refs = [scope_crypto, scope_bonds]

scope_crypto:
  required_query_semantic_refs = [CRYPTO_QUERY]
  required_response_semantic_refs = [CRYPTO_RESPONSE]

scope_bonds:
  required_query_semantic_refs = [BOND_QUERY]
  required_response_semantic_refs = [BOND_RESPONSE]
```

Assume the equality dimensions currently required by R1 are otherwise identical and both components are complete/active/certified.

Under R1's no-partition rule, exact component-scope-set bijection is sufficient to close the gap. The contract has no exact semantic relation proving that `CRYPTO_QUERY ∪ BOND_QUERY` covers `US_EQUITY_QUERY`, nor an exact trusted translation/equivalence relation for provider-specific query/response semantics.

Because `required_query_semantic_refs[]` and `required_response_semantic_refs[]` are part of `CoverageScopeDefinition`'s exact universe identity in the parent C2.05 contract, they cannot be ignored when proving composite scope closure.

The same issue exists in partitioned composites: pairwise-disjoint partition union closes the partition dimension, but it does not by itself prove the root/component query-response semantic relation.

Failed obligations:

```text
C2-471
C2-539
C2-540
```

R2 requirement:

Freeze an exact root-to-component semantic coverage relation. Acceptable contract-level forms include a new immutable composite-scope-relation object whose full stable refs explicitly prove root-to-component query/response equivalence/decomposition, or a stricter rule that makes the root composite universe definition exactly the canonical component-scope set and removes/neutralizes conflicting root query/response dimensions. Human interpretation or mere component enumeration is insufficient.

### 4.5 C2CERT-B05 — CLOSED

The R1 classifier is total and ordered:

```text
INVALID
> INDETERMINATE
> PARTIAL_KNOWN
> NON_EXHAUSTIVE
> COMPLETE_FOR_SCOPE
```

with a mandatory final fail-closed `INDETERMINATE`.

Mixed-defect cases have deterministic precedence, stored classification must equal the recomputed value for load-bearing use, and `SUCCESS+NO_DATA/PRESENT` remain C2 eligibility signals rather than C1 conclusions.

The classifier remains dependent on its input predicates. B03/B04 still prevent the stage from passing, but the B05 precedence/classification defect itself is closed.

Result: **CLOSED**.

## 5. Acceptance re-check

### 5.1 Previously failed parent obligations

Re-run set: 8.

```text
PASS:
C2-402
C2-411
C2-412
C2-459

FAIL:
C2-437
C2-438
C2-471
C2-481
```

The parent C2.05 acceptance surface therefore improves from `78/86` to:

```text
C2-402..C2-487
PASS = 82
FAIL = 4
```

### 5.2 New R1 obligations

Reviewed range:

```text
C2-488..C2-555
total = 68
PASS  = 65
FAIL  = 3
```

Failed new obligations:

```text
C2-525
C2-539
C2-540
```

`C2-525` fails because a content-addressed binding record that internally matches the scope can still be detached from the actual replay-retained operation semantics.

`C2-539` and `C2-540` fail because the frozen composite compatibility/gap rule does not prove the root-to-component query/response semantic coverage relation.

### 5.3 Effective C2.05 + R1 surface

```text
C2-402..C2-555
total = 154
PASS  = 147
FAIL  = 7
```

Failed effective obligations:

```text
C2-437
C2-438
C2-471
C2-481
C2-525
C2-539
C2-540
```

## 6. Non-regression

The following remain PASS and must not be reopened except where directly necessary for B03/B04 repair:

- certification/completeness separation;
- immutable certification-registry snapshots;
- closed certification states and B02 total decision precedence;
- certification is not C5 verification;
- certification grants no C6 capability, trusted intent, destination, WRITE/PAPER/LIVE, or side-effect authority;
- certification/completeness do not reorder C2.03 routes;
- certification is not C3 health/freshness/quota/cache state;
- exact scope refs remain content-addressed and wildcard/human-label broadening remains forbidden;
- exact-key/pagination/partition/bulk/window method families remain closed;
- `SUCCESS+NO_DATA` does not become C1 `NO_MATCH`;
- `SUCCESS+PRESENT` does not become C1 `RESOLVED`;
- `SUCCESS+PARTIAL`, FAILED, and CANCELLED do not support absence/uniqueness;
- C2 completeness does not imply C4 PIT safety;
- C2.04R1 secure-ingress restrictions remain unchanged;
- no concrete provider/vendor/adaptor is selected;
- C11 persistence implementation remains outside C2.05.

C2.04 effective acceptance remains:

```text
C2-289..C2-401 = 113/113 PASS
```

## 7. Open-question disposition

Because B03/B04 remain open:

```text
C2.OPEN-009 = NOT_CLOSED_REPAIR_REQUIRED
C2.OPEN-010 = NOT_CLOSED_REPAIR_REQUIRED
C2.OPEN-011 = NOT_CLOSED_REPAIR_REQUIRED

C2.OPEN-012 = OPEN_UNCHANGED_C2_06
C2.OPEN-013 = OPEN_UNCHANGED_C2_06_PERMITTED_RAW_HANDOFF
C2.OPEN-014 = OPEN_UNCHANGED_C2_07
C2.OPEN-015 = OPEN_UNCHANGED_POST_CONTRACT_CONFIGURATION
```

## 8. Required next repair scope

If explicitly authorized, `C2.05R2` must be scoped only to:

1. B03 operation-scope semantic provenance:
   - exact binding to replay-retained C2.01 `CapabilityRequirement R`;
   - exact binding to C2.02R2 attempted-response semantics;
   - exact authoritative derivation/binding for native subject/identifier dimensions, partitions, constraints, and temporal dependency;
   - no self-asserted duplicate semantic fields as a success path.

2. B04 composite root/component semantic closure:
   - exact query/response semantic coverage/equivalence/decomposition relation;
   - exact root-universe definition for composite scope;
   - no component enumeration alone as gap proof;
   - preserve the already-closed partition bijection, component integrity, and nested-composite fail-closed rules.

3. Corresponding acceptance additions and independent re-checks only.

B01, B02, and B05 are closed by this re-check and should not be reopened except where an R2 change directly touches them.

## 9. Governance stop

Final state:

`C2.05R1 INDEPENDENT CERTIFICATION RE-CHECK FAIL — C2.05R2 REPAIR_REQUIRED_NOT_FROZEN`

Next gate:

`Explicit user authorization for C2.05R2 scoped repair`

Do not start C2.05R2, C2.06, production implementation, concrete provider/vendor configuration, or external/PAPER/LIVE side effects without explicit authorization.
