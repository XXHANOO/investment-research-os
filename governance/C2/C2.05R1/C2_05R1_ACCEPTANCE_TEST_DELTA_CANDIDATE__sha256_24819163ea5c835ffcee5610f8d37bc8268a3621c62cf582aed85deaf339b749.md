# C2.05R1 — Acceptance Test Delta Candidate

Generated: 2026-09-07T06:31:00Z

Status: `SCOPED_REPAIR_CANDIDATE_PENDING_INDEPENDENT_CERTIFICATION_RECHECK`

Parent C2.05 acceptance range: `C2-402..C2-487`.

Independent C2.05 review result: `78/86 PASS; 8 FAIL`.

Failed parent obligations that MUST be independently re-run after this repair:

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

C2.05R1 adds `C2-488..C2-555` = 68 adversarial obligations. Construction does not mark any parent failed obligation or new obligation independently PASS.

| ID | Test | Required Behavior | Type |
|---|---|---|---|
| `C2-488` | Coverage evidence ref kind exists | coverage_evidence_bundle_ref resolves only as COVERAGE_EVIDENCE_BUNDLE; no convention/private kind may satisfy it. | `B01/type` |
| `C2-489` | Coverage evidence field-kind contract enforced | Wrong-kind/dangling/floating/hash-mismatched coverage evidence refs fail closed. | `B01/type` |
| `C2-490` | Coverage bundle subject binding exact | Bundle attestation_subject_binding must exactly equal consuming attestation registry/certification/scope/method/component subject. | `B01/binding` |
| `C2-491` | Coverage required checks exactly once | Every method-required CoverageMethodCheckClass appears exactly once. | `B01/checks` |
| `C2-492` | Unknown coverage check invalid | Unknown/private-extension coverage check classes make the bundle structurally invalid. | `B01/checks` |
| `C2-493` | Coverage evidence-role vocabulary closed | Only the frozen CoverageEvidenceRole vocabulary is load-bearing. | `B01/roles` |
| `C2-494` | Required evidence role present | Every method-required evidence role has at least one exact resolved evidence item. | `B01/roles` |
| `C2-495` | Unknown evidence role invalid | Unknown/private evidence roles cannot satisfy or supplement a required role for load-bearing success. | `B01/roles` |
| `C2-496` | Termination rule is method-total | Each of six method families maps to exactly its frozen termination rule; any other value invalidates the method profile. | `B01/method` |
| `C2-497` | Truncation rule closed | truncation_failure_rule is exactly ANY_MATERIAL_PARTIALITY_OR_TRUNCATION_PREVENTS_COMPLETE. | `B01/method` |
| `C2-498` | Coverage evidence secure-ingress binding | Provider-derived coverage evidence must be admitted/sanitized under C2.04R1 and quarantine/reject cannot support completeness. | `B01/security` |
| `C2-499` | No alternate private coverage carrier | Opaque implementation handles or CERTIFICATION_EVIDENCE_BUNDLE-by-convention cannot substitute for COVERAGE_EVIDENCE_BUNDLE. | `B01/type` |
| `C2-500` | Certification required/optional sets disjoint | Any CertificationCheckClass present in both required and optional sets invalidates the profile. | `B02/profile` |
| `C2-501` | Certification profile duplicates invalid | Duplicates inside required or optional class sets invalidate the profile before decision classification. | `B02/profile` |
| `C2-502` | Undeclared certification result invalid | A bundle check class not declared required/optional is structurally invalid. | `B02/bundle` |
| `C2-503` | Structural invalidity precedence | Any structural invalidity yields INDETERMINATE even when FAIL or INDETERMINATE results coexist. | `B02/precedence` |
| `C2-504` | FAIL beats INDETERMINATE when structurally valid | A structurally valid bundle containing required FAIL and required INDETERMINATE yields NOT_CERTIFIED. | `B02/precedence` |
| `C2-505` | FAIL plus invalid remains indeterminate | Required FAIL plus missing/duplicate/wrong-scope/unresolved structural defect yields INDETERMINATE. | `B02/precedence` |
| `C2-506` | All required PASS certifies | A structurally valid bundle with every required check PASS yields CERTIFIED. | `B02/decision` |
| `C2-507` | Optional FAIL is diagnostic only | Optional FAIL does not change CERTIFIED when all required checks PASS and structure is valid. | `B02/optional` |
| `C2-508` | Optional indeterminate is diagnostic only | Optional INDETERMINATE does not change CERTIFIED when all required checks PASS and structure is valid. | `B02/optional` |
| `C2-509` | Certification decision permutation invariant | Reordering check_results cannot change the total certification decision. | `B02/replay` |
| `C2-510` | Coverage scope binds parent registry snapshot | CoverageScopeDefinition requires one exact REGISTRY_SNAPSHOT parent semantic registry ref. | `B03/snapshot` |
| `C2-511` | Operation scope binding stable kind closed | OperationCoverageScopeBinding resolves only as OPERATION_COVERAGE_SCOPE_BINDING. | `B03/type` |
| `C2-512` | Operation/scope parent snapshot exact | Operation binding parent_semantic_registry_snapshot_ref must equal scope parent snapshot exactly. | `B03/snapshot` |
| `C2-513` | All scope semantic refs same parent snapshot | All participating provider/endpoint/capability/query/response/feature/subject/identifier refs resolve under the same parent registry snapshot. | `B03/snapshot` |
| `C2-514` | Provider endpoint capability exact match | Operation binding provider/endpoint/capability refs must exactly equal the attested coverage scope. | `B03/binding` |
| `C2-515` | Access pattern exact match | Operation access_pattern_family must exactly equal the coverage scope access pattern. | `B03/binding` |
| `C2-516` | Observation-family set exact match | Operation required observation-family refs must canonically equal the scope set. | `B03/binding` |
| `C2-517` | Query-semantic set exact match | Operation required query-semantic refs must canonically equal the scope set. | `B03/binding` |
| `C2-518` | Attempted-response set exact match | Operation attempted_response_semantic_refs must canonically equal scope required_response_semantic_refs. | `B03/binding` |
| `C2-519` | Semantic-feature set exact match | Operation required semantic-feature refs must canonically equal the scope set. | `B03/binding` |
| `C2-520` | Native-subject set exact match | Operation provider-native subject semantic refs must canonically equal the scope set. | `B03/binding` |
| `C2-521` | Identifier-namespace set exact match | Operation provider-native identifier namespace refs must canonically equal the scope set. | `B03/binding` |
| `C2-522` | Partition set exact match | Operation coverage_partition_refs must canonically equal the scope partition set. | `B03/binding` |
| `C2-523` | Scope-constraint set exact match | Operation scope_constraint_refs must canonically equal the scope constraint set. | `B03/binding` |
| `C2-524` | Temporal dependency exact match | Temporal dependency must be both absent or the exact same ref; mismatch fails support. | `B03/temporal` |
| `C2-525` | Scope ref pin alone insufficient | Matching required_coverage_scope_ref cannot support coverage when any operation-scope binding clause differs. | `B03/adversarial` |
| `C2-526` | Operation binding set order invariant | Canonical list ordering/deduplication makes equivalent set permutations yield the same binding decision. | `B03/replay` |
| `C2-527` | Partition component maps exactly one partition | PARTITION_EXHAUSTION component binding contains exactly one covered partition. | `B04/partition` |
| `C2-528` | Partition mapping is bijective | Canonical covered-partition set across components equals root required partition set with one-to-one mapping. | `B04/partition` |
| `C2-529` | Duplicate partition mapping invalid | Two components mapped to the same required partition fail closure. | `B04/partition` |
| `C2-530` | Missing partition fails closure | Any root required partition without exactly one complete component prevents COMPLETE_FOR_SCOPE. | `B04/partition` |
| `C2-531` | Extra partition fails closure | A component mapping to a partition outside the root required set fails closed. | `B04/partition` |
| `C2-532` | Repeated component attestation invalid | Repeated component_attestation_ref in a closure record is structurally invalid. | `B04/components` |
| `C2-533` | Unresolved component fails closed | Wrong-kind/dangling/hash-mismatched component attestation or scope refs prevent closure. | `B04/components` |
| `C2-534` | Composite component-scope set exact | COMPOSITE_EXPLICIT_CLOSURE requires exactly one component attestation for every root composite_component_scope_ref. | `B04/composite` |
| `C2-535` | Composite components complete active certified | Every composite component must be COMPLETE_FOR_SCOPE, ACTIVE, and backed by CERTIFIED state in the same registry snapshot. | `B04/composite` |
| `C2-536` | Composite partition union exact | When root partitions exist, pairwise-disjoint component partition sets must have canonical union exactly equal to root set. | `B04/composite` |
| `C2-537` | Composite partition overlap invalid | Any partition overlap between composite components prevents gap closure. | `B04/composite` |
| `C2-538` | Nested composite forbidden | A component whose method family is COMPOSITE_EXPLICIT_CLOSURE is structurally invalid in C2.05R1. | `B04/composite` |
| `C2-539` | Composite scope incompatibility fails | Component scope not explicitly listed or failing frozen non-partition compatibility cannot close the composite. | `B04/composite` |
| `C2-540` | Composite no-partition closure exact | With an empty root partition set, all component partition sets must be empty and exact component-scope-set bijection is the gap proof. | `B04/composite` |
| `C2-541` | Structural invalid classifies INVALID | Coverage classifier returns INVALID for any structural-invalid condition. | `B05/classifier` |
| `C2-542` | Unresolved classifies INDETERMINATE | With valid structure, unresolved/indeterminate required dependency returns INDETERMINATE. | `B05/classifier` |
| `C2-543` | Known partiality precedence | Known material partiality returns PARTIAL_KNOWN after structural/indeterminate checks, even with additional known non-exhaustive condition. | `B05/classifier` |
| `C2-544` | Known closure failure classifies NON_EXHAUSTIVE | A deterministic false completeness predicate with no higher-precedence state returns NON_EXHAUSTIVE. | `B05/classifier` |
| `C2-545` | All predicates true classify COMPLETE | Only when every complete predicate is true does classifier return COMPLETE_FOR_SCOPE. | `B05/classifier` |
| `C2-546` | Invalid plus partial stays INVALID | Invalid evidence/structure plus known partiality deterministically returns INVALID. | `B05/mixed` |
| `C2-547` | Indeterminate plus partial stays INDETERMINATE | Unresolved required dependency plus known partiality deterministically returns INDETERMINATE. | `B05/mixed` |
| `C2-548` | Coverage classifier permutation invariant | Reordering evidence/check/component inputs cannot change the recomputed classification. | `B05/replay` |
| `C2-549` | Stored classification mismatch blocks use | Stored coverage_classification differing from recomputed value is INVALID_FOR_LOAD_BEARING_USE and is not silently rewritten. | `B05/consistency` |
| `C2-550` | FAILED/CANCELLED classify non-exhaustive | With otherwise valid and determinate structure, FAILED or CANCELLED operations classify NON_EXHAUSTIVE. | `B05/outcome` |
| `C2-551` | Non-ACTIVE coverage cannot complete | Known non-ACTIVE coverage registry state prevents COMPLETE and deterministically yields NON_EXHAUSTIVE absent higher-precedence state. | `B05/state` |
| `C2-552` | Non-CERTIFIED certification cannot complete | Known NOT_CERTIFIED/REVOKED/SUPERSEDED certification state prevents COMPLETE and yields NON_EXHAUSTIVE absent higher-precedence state. | `B05/state` |
| `C2-553` | Complete NO_DATA remains eligibility only | SUCCESS+NO_DATA with recomputed COMPLETE_FOR_SCOPE and valid binding yields only ABSENCE_SUPPORT_ELIGIBLE, not C1 NO_MATCH. | `B05/C1` |
| `C2-554` | Complete PRESENT remains eligibility only | SUCCESS+PRESENT with recomputed COMPLETE_FOR_SCOPE and valid binding yields only UNIQUENESS_SUPPORT_ELIGIBLE, not C1 RESOLVED. | `B05/C1` |
| `C2-555` | Fallback classifier fails closed | Any valid-state combination not matched by earlier classifier predicates resolves to INDETERMINATE, never guessed COMPLETE. | `B05/totality` |

## Required re-check matrix

### C2CERT-B01
Re-run: `C2-402`.
New: `C2-488..C2-499`.

### C2CERT-B02
Re-run: `C2-411`, `C2-412`, `C2-481`.
New: `C2-500..C2-509`.

### C2CERT-B03
Re-run: `C2-437`, `C2-438`, `C2-481`.
New: `C2-510..C2-526`.

### C2CERT-B04
Re-run: `C2-459`, `C2-471`, `C2-481`.
New: `C2-527..C2-540`.

### C2CERT-B05
Re-run: `C2-481`.
New: `C2-541..C2-555`.

## Parent PASS-surface non-regression

The Independent Re-Check must also verify that the other 78 parent C2.05 obligations remain PASS and that C2.04 effective acceptance `C2-289..C2-401` remains non-regressed.

## Gate

No construction self-check closes C2CERT-B01..B05. Independent Certification Re-Check is required before C2.05 may become `REVIEW_PASSED_NOT_FROZEN`.
