# C2.05R2 Independent Certification Re-Check Report

Generated: 2026-09-07T07:42:00Z

Review type: `INDEPENDENT_CERTIFICATION_RECHECK`

Candidate under review: `C2.05R2 — Operation-Scope Provenance and Composite-Root Universe Scoped Repair`

## 1. Independent review posture

This re-check is independent of C2.05R2 construction self-checks. The C2.05R2 construction validation, construction summary, candidate selection, stage report, repair-diff assertions, and decision-ledger closure labels are treated only as candidate metadata. They are not evidence that C2CERT-B03 or C2CERT-B04 is closed.

The re-check re-read the effective C2.05 + C2.05R1 contract, the C2.05R1 Independent Certification Re-Check failure, the exact C2.05R2 repair contract/logical model/acceptance delta, and the pinned C2.01R1/C2.02R2 authorities needed to evaluate operation provenance.

The review adversarially tested:

- the seven residual failed obligations from C2.05R1;
- all 35 C2.05R2 obligations `C2-556..C2-590`;
- preservation of the already-closed C2CERT-B01/B02/B05 surfaces;
- preservation of C2.04 effective acceptance `C2-289..C2-401`;
- false-positive completeness caused by scope assertions that are not bound to the executed request;
- historical replay under duplicate/late provenance claims;
- end-to-end compatibility between composite-root scope semantics and the C2.02R2 attempted-response scope;
- C1/C3/C4/C5/C6/C7/C11/C12 ownership boundaries.

No C2.06 construction, provider/vendor selection, production adapter work, or external/PAPER/LIVE side effect is authorized by this review.

## 2. Exact reviewed pins

```text
C2.05 parent contract                 3642588dcc22a7564d55a9a72d3e6e328b007649005c866e7831dfa4b8571d4c
C2.05 parent logical model            0a6d7c4037c04ca04f87994507afb722661dbd9450a115492238b9d5dd9c776c
C2.05 parent acceptance delta         62714c720e2a9d6f24f066533ddac9c84f3360a6bff2cbe4d9aacbb9617cff6f

C2.05R1 repair contract               267c83480aa909e74cb5d87c54512878c3c9c7128fce8a394fb63f39c6ed2bcb
C2.05R1 logical model                 777b7ddc3530a088a127f3becb74bd1f644fc25f83703cb27799423671752262
C2.05R1 acceptance delta              24819163ea5c835ffcee5610f8d37bc8268a3621c62cf582aed85deaf339b749
C2.05R1 independent re-check report   2b829b9a3af45eade91efee1fea786a9b26128c39be0f4662953897bea0635f8
C2.05R1 independent re-check result   59578acccb8906637360f24c7fe190a3a6e6b92098ddf03c30a5133b9d5767bf

C2.05R2 repair contract               b68943c7773ba5abb596eafd2a572398d172ed3d0bd08cea1b12bdd5b51c29ff
C2.05R2 logical model                 129657e705dad194691e48edd09274297856e11a2e0b44d075392da9942e7437
C2.05R2 acceptance delta              a91d701743ca84d50e827ef149ae60493dacb88183458f4b90f9e4fd4c016ad0
C2.05R2 decision ledger               1af30d88c3bd02793e22bd3f4d2ccd026af6b2f26562e06c4b079621d692bbb9
C2.05R2 candidate archive commit      916847395b4817e7ed4ffa4342e4143439be10e8
C2.05R2 candidate subtree             b00d522089efb8be63a2d8dc2e5348dc28cd5c11

C2.01R1 registry model                0bcdd0c48d8cd614ee7a1cb6ee6519df8fb33731bcafd535f3313978dca4343a
C2.02R2 outcome contract              901445ca8f0f3f1a8cd04331d3def83f4a29ae3984e5917e723e2402f858f57d
C2.04R1 security re-check result      d1af240f4e6eff32b087295ef259fd4485c13fc0775f8abc24fa630993104f47
```

## 3. Final verdict

`FAIL — C2.05R2 REPAIR_REQUIRED_NOT_FROZEN`

C2.05R2 materially improves both residual areas. In particular, the actual C2.01 `CapabilityRequirement R` and the C2.02R2 attempted-response set are now linked into the coverage path, and the composite root no longer relies on human/informal semantic equivalence.

However, independent adversarial review found three remaining load-bearing defects under the two existing blocker families:

```text
C2CERT-B01 = CLOSED_UNCHANGED
C2CERT-B02 = CLOSED_UNCHANGED
C2CERT-B03 = OPEN
C2CERT-B04 = OPEN
C2CERT-B05 = CLOSED_UNCHANGED

C2.05R2 = REPAIR_REQUIRED_NOT_FROZEN
C2.06 = NOT_STARTED / NOT_AUTHORIZED
Production implementation = NOT_AUTHORIZED
Provider/vendor configuration = NOT_AUTHORIZED
External/PAPER/LIVE side effects = NOT_AUTHORIZED
```

## 4. C2CERT-B03 — OPEN

### 4.1 Finding B03-R2-01 — `NATIVE_SCOPE_COMMITMENT_NOT_EXECUTION_BOUND`

R2 correctly binds these fields to the actual replay-retained `CapabilityRequirement R` / C2.02R2 attempted-response state:

```text
access_pattern_family
required_observation_family_refs[]
required_query_semantic_refs[]
required_semantic_feature_refs[]
attempted_response_semantic_refs[]
provider/endpoint/capability/snapshot identity
```

That closes the R1 self-described `QUERY_A/RESPONSE_A` attack for those dimensions.

The remaining C2.05-native dimensions are different:

```text
provider_native_subject_semantic_refs[]
provider_native_identifier_namespace_refs[]
coverage_partition_refs[]
scope_constraint_refs[]
temporal_scope_dependency_ref?
```

R2 makes these values authoritative when they appear in an exact content-addressed provenance record marked `SEALED_FOR_COVERAGE_BEFORE_DISPATCH`, but it does not require that the actual provider request/dispatch boundary consume the same values, nor does it derive or exact-compare them against a replay-retained executed-request semantic state.

A pre-dispatch assertion is therefore still able to be internally self-consistent but false about the request that is actually sent.

Adversarial vector:

```text
actual operation request semantics:
  provider-native constraint = COUNTRY_US

replay-retained R:
  valid and compatible, but R has no field that carries COUNTRY_US

pre-dispatch OperationCoverageProvenance:
  scope_constraint_refs = [COUNTRY_GLOBAL]
  provenance_commitment_state = SEALED_FOR_COVERAGE_BEFORE_DISPATCH

OperationCoverageScopeBinding:
  exactly projects provenance

CoverageScopeDefinition:
  scope_constraint_refs = [COUNTRY_GLOBAL]
```

Every new R2 provenance-to-binding-to-scope equality can succeed even though the executed provider request was `COUNTRY_US`.

The same class of defect applies to native subject, identifier namespace, partition, and opaque temporal dependency dimensions whenever those dimensions affect the concrete candidate universe but are not machine-derived from the actual request semantic state.

This is not repaired by content addressing or by sealing before dispatch. Those properties prove immutability and timing of the assertion; they do not prove correspondence to the executed request.

The parent certification profile also does not universally require `REQUEST_SCOPE_CONFORMANCE` for every coverage-capable certification profile, so the missing per-operation binding cannot be assumed to be repaired elsewhere.

Result: **B03 remains OPEN**.

Required R3 closure:

- freeze one exact replay-retained **executed request semantic state** (or equivalent immutable request-scope commitment) that is an input to actual dispatch;
- deterministically derive or exact-compare every C2.05-native scope dimension from that state;
- make disagreement fail closed before any `COMPLETE_FOR_SCOPE` support;
- a coverage-only pre-dispatch assertion that is not consumed by request construction is insufficient.

### 4.2 Finding B03-R2-02 — `PROVENANCE_UNIQUENESS_DOMAIN_NOT_PINNED`

R2 requires exactly one load-bearing provenance ref per `(provider_operation_ref, route_attempt_ref)` and states that multiple provenance refs claiming the same operation/attempt make support invalid.

The contract does not freeze the authoritative finite set over which that uniqueness check is evaluated.

Adversarial replay:

```text
T1:
  operation retains provenance P1
  verifier sees only P1
  -> uniqueness appears satisfied

T2:
  unrelated/later content-addressed record P2 is minted
  P2 also claims the same operation/attempt

historical replay of T1:
  implementation A scans only the operation-retained authority -> one provenance
  implementation B scans a wider store/index -> two claiming provenance refs
```

The same pinned historical operation/attestation can therefore receive different support decisions depending on discovery scope unless the contract defines one exact provenance authority domain.

A later unreferenced object must not be able to retroactively change historical support.

Result: **C2-557 FAIL** and **C2-481 remains FAIL**.

Required R3 closure must choose one deterministic rule, for example:

- the exact singular provenance ref replay-retained by the operation/attempt is the sole authority and unreferenced claims are non-authoritative; or
- an exact immutable provenance-set/registry snapshot is pinned and uniqueness is evaluated only inside that set.

No mutable/global store scan is acceptable.

## 5. C2CERT-B04 — OPEN

### 5.1 Improvement achieved

R2 removes the R1 semantic-coverage ambiguity by defining:

```text
COMPOSITE_EXPLICIT_CLOSURE root:
  required_query_semantic_refs[]    = []
  required_response_semantic_refs[] = []

CompositeRootUniverse(root)
  = canonical_set(root.composite_component_scope_refs[])
```

This is a valid way to remove the old informal `root query/response ~= components` inference in isolation.

### 5.2 Finding B04-R2-01 — `COMPOSITE_ROOT_UNMATCHABLE_TO_ATTEMPT_RESPONSE_SCOPE`

The stricter root-universe design conflicts with the inherited operation-to-scope support predicate.

R1 requires:

```text
OperationCoverageScopeBinding.attempted_response_semantic_refs
  == CoverageScopeDefinition.required_response_semantic_refs
```

R2 additionally requires the binding's attempted-response set to equal the exact C2.02R2 attempted-response set `A`.

But C2.02R2 defines:

```text
A = canonical_set(
    { E.response_semantics.response_semantic_ref }
    ∪ P.required_response_semantic_refs
    ∪ R.required_response_semantic_refs
)
```

Therefore every contract-valid dispatched attempt contains at least the endpoint primary response semantic in `A`.

For a C2.05R2 composite root, however:

```text
root.required_response_semantic_refs = []
```

So a load-bearing composite root simultaneously requires:

```text
binding.attempted_response_semantic_refs == A
binding.attempted_response_semantic_refs == []
A contains endpoint primary response semantic
```

These conditions cannot all be true for a valid dispatched provider attempt.

The conflict is end-to-end, not merely a wire-placement issue. R2 Section 7 explicitly retains the operation provenance/binding requirements for `coverage_support_valid`, including for composite roots.

Consequences:

- a composite root may be structurally content-addressed and may have complete components;
- its gap structure may be internally deterministic;
- but it cannot become a valid load-bearing coverage dependency for any ordinary C2.02R2 dispatched operation under the effective support predicate.

A method family that can never reach the stage's load-bearing support predicate is not a closed completeness contract.

Result:

```text
C2-471 = FAIL
C2-540 = FAIL
C2-584 = FAIL
C2-585 = FAIL
```

Required R3 closure must choose one coherent model:

1. **Aggregate-root model:** composite root is an aggregate/derived coverage subject not required to match one provider operation's C2.02 attempted-response set; each component remains operation-provenanced and the root gets a separately closed aggregate support predicate; or
2. **Explicit decomposition-relation model:** retain non-empty root query/response semantics that can match the consuming operation and add an immutable machine-checkable root-to-component decomposition/equivalence relation.

The current hybrid — empty root response scope plus mandatory per-operation attempted-response equality — is contradictory.

## 6. Acceptance re-check

### 6.1 Seven residual failed obligations from C2.05R1

```text
PASS:
C2-437
C2-438
C2-525
C2-539

FAIL:
C2-471
C2-481
C2-540
```

The effective C2.05 + R1 surface becomes:

```text
C2-402..C2-555
total = 154
PASS  = 151
FAIL  = 3
```

### 6.2 New C2.05R2 obligations

Reviewed range:

```text
C2-556..C2-590
total = 35
PASS  = 32
FAIL  = 3
```

Failed new obligations:

```text
C2-557
C2-584
C2-585
```

Important adequacy note:

`C2-567..C2-571` pass **as written** because R2 does make those dimensions come from the sealed pre-dispatch provenance record. They are nevertheless insufficient to close B03 because they do not test correspondence between that record and the executed provider request. Independent review is not limited to the candidate-authored test matrix.

### 6.3 Effective C2.05 through R2 surface

```text
C2-402..C2-590
total = 189
PASS  = 183
FAIL  = 6
```

Failed effective obligations:

```text
C2-471
C2-481
C2-540
C2-557
C2-584
C2-585
```

## 7. Non-regression

The following remain independently preserved:

- C2CERT-B01 coverage-evidence carrier/ref/check closure;
- C2CERT-B02 certification total decision precedence;
- C2CERT-B05 total coverage classifier precedence;
- certification remains distinct from completeness and from C5 verification;
- no certification/completeness state grants C6 capability, trusted intent, destination, WRITE/PAPER/LIVE, or side-effect authority;
- C2 completeness does not absorb C4 PIT/revision/`available_from` authority;
- C2.03 route ordering, C3 retry/quota/cache/freshness/coalescing/LKG, and C7 orchestration authority are unchanged;
- C2.04R1 secure-ingress restrictions remain unchanged;
- no concrete provider/vendor/adaptor is selected;
- C11 persistence implementation remains outside C2.05.

C2.04 effective acceptance remains:

```text
C2-289..C2-401 = 113/113 PASS
```

## 8. Open-question disposition

Because B03 and B04 remain open:

```text
C2.OPEN-009 = NOT_CLOSED_REPAIR_REQUIRED
C2.OPEN-010 = NOT_CLOSED_REPAIR_REQUIRED
C2.OPEN-011 = NOT_CLOSED_REPAIR_REQUIRED

C2.OPEN-012 = OPEN_UNCHANGED_C2_06
C2.OPEN-013 = OPEN_UNCHANGED_C2_06_PERMITTED_RAW_HANDOFF
C2.OPEN-014 = OPEN_UNCHANGED_C2_07
C2.OPEN-015 = OPEN_UNCHANGED_POST_CONTRACT_CONFIGURATION
```

## 9. Required next repair scope

If explicitly authorized, `C2.05R3` must be narrow and limited to:

### B03
- machine-bind native subject / identifier namespace / partition / constraint / temporal coverage dimensions to the **executed request semantic state**, not merely a coverage-only pre-dispatch assertion;
- freeze the exact provenance uniqueness authority domain so later unrelated claims cannot change historical replay;
- preserve the R2 `R` and C2.02R2 attempted-response provenance improvements.

### B04
- remove the composite-root / per-operation attempted-response contradiction;
- use either an aggregate-root support model or an explicit machine-checkable root-to-component decomposition relation;
- add adversarial acceptance vectors that include the C2.02R2 invariant that a valid attempted-response set includes the endpoint primary response semantic.

C2CERT-B01/B02/B05 must remain closed and must not be unrelatedly reopened.

## 10. Governance stop

```text
C2.05R2 Independent Certification Re-Check = FAIL
C2.05 = REPAIR_REQUIRED_NOT_FROZEN
C2.05R3 = NOT_STARTED / NOT_AUTHORIZED
C2.06 = NOT_STARTED / NOT_AUTHORIZED
Production implementation = NOT_AUTHORIZED
Provider/vendor configuration = NOT_AUTHORIZED
External/PAPER/LIVE side effects = NOT_AUTHORIZED
```

Next gate: **explicit user authorization for C2.05R3 scoped repair**.
