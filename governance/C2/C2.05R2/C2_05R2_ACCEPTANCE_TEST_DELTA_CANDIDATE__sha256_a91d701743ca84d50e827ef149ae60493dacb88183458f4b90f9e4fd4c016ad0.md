# C2.05R2 — Acceptance Test Delta Candidate

Generated: 2026-09-07T07:10:00Z

Status: `SCOPED_REPAIR_CANDIDATE_PENDING_INDEPENDENT_CERTIFICATION_RECHECK`

Parent effective range before R2: `C2-402..C2-555`.

Residual failed obligations that MUST be independently re-run:

```text
C2-437
C2-438
C2-471
C2-481
C2-525
C2-539
C2-540
```

C2.05R2 adds `C2-556..C2-590` = 35 adversarial obligations. Construction does not mark any residual parent/R1 failure or new obligation independently PASS.

| ID | Test | Required Behavior | Type |
|---|---|---|---|
| `C2-556` | Provenance stable kind closed | operation_coverage_provenance_ref resolves only as OPERATION_COVERAGE_PROVENANCE. | `B03/type` |
| `C2-557` | Exact attempt provenance uniqueness | Load-bearing coverage uses exactly one provenance ref for the exact provider_operation_ref + route_attempt_ref; absent or multiple refs fail closed. | `B03/identity` |
| `C2-558` | Provenance R exact replay binding | capability_requirement_R equals the exact replay-retained C2.01 CapabilityRequirement R for the attempt. | `B03/R` |
| `C2-559` | Provenance R digest exact | capability_requirement_R_content_sha256 equals SHA256 of canonical R bytes. | `B03/R` |
| `C2-560` | Access pattern derived from R | Binding access_pattern_family equals provenance R access pattern. | `B03/projection` |
| `C2-561` | Observation set derived from R | Binding observation-family set equals provenance R set exactly. | `B03/projection` |
| `C2-562` | Query set derived from R | Binding query-semantic set equals provenance R set exactly. | `B03/projection` |
| `C2-563` | Feature set derived from R | Binding semantic-feature set equals provenance R set exactly. | `B03/projection` |
| `C2-564` | Attempted response exact C2.02R2 source | Provenance attempted_response_semantic_refs equals the exact C2.02R2 stored/derived set for the same attempt. | `B03/response` |
| `C2-565` | Attempted response recomputation | Same S/P/E/R recomputes exactly the provenance attempted-response set; mismatch fails support. | `B03/response` |
| `C2-566` | Provider/endpoint/capability provenance exact | Provenance provider, endpoint, capability and parent snapshot equal the actual attempt's pinned semantic identities. | `B03/identity` |
| `C2-567` | Native subject source committed | Native-subject scope comes only from the exact pre-dispatch provenance commitment later replay-retained by the attempt. | `B03/native` |
| `C2-568` | Identifier namespace source committed | Native identifier namespace scope comes only from the exact pre-dispatch provenance commitment. | `B03/native` |
| `C2-569` | Partition source committed | Coverage partitions come only from the exact pre-dispatch provenance commitment; later substitution fails. | `B03/partition` |
| `C2-570` | Constraint source committed | Scope constraints come only from the exact pre-dispatch provenance commitment. | `B03/constraint` |
| `C2-571` | Temporal dependency source committed | Temporal scope dependency is BOTH_ABSENT or exact same committed ref; later replacement fails. | `B03/temporal` |
| `C2-572` | Binding projects provenance exactly | Every duplicated load-bearing scope field in OperationCoverageScopeBinding equals its authoritative provenance source. | `B03/projection` |
| `C2-573` | Post-hoc provenance forbidden | An operation without a pre-dispatch committed provenance cannot gain completeness support by minting provenance/binding after execution. | `B03/adversarial` |
| `C2-574` | Self-consistent wrong-scope attack blocked | A binding+scope pair internally matching QUERY_A/RESPONSE_A cannot pass when actual R/A are QUERY_B/RESPONSE_B. | `B03/adversarial` |
| `C2-575` | Wrong-attempt provenance blocked | Provenance from a different route attempt cannot support the current attempt even when scope fields match. | `B03/identity` |
| `C2-576` | Provenance snapshot mismatch blocked | Provenance and operation/scope parent registry snapshots must match exactly. | `B03/snapshot` |
| `C2-577` | Provenance canonical-set order invariant | Permuting equivalent canonical sets in R/native/partition/constraint fields cannot change the provenance validation outcome. | `B03/replay` |
| `C2-578` | Composite root query set empty | COMPOSITE_EXPLICIT_CLOSURE root required_query_semantic_refs must be empty. | `B04/root` |
| `C2-579` | Composite root response set empty | COMPOSITE_EXPLICIT_CLOSURE root required_response_semantic_refs must be empty. | `B04/root` |
| `C2-580` | Composite root component set nonempty exact | CompositeRootUniverse is exactly the non-empty canonical composite_component_scope_refs set. | `B04/root` |
| `C2-581` | Root non-empty query invalid | Any non-empty root query semantic set makes composite completeness structurally invalid. | `B04/adversarial` |
| `C2-582` | Root non-empty response invalid | Any non-empty root response semantic set makes composite completeness structurally invalid. | `B04/adversarial` |
| `C2-583` | Component scope is the query/response decomposition authority | Each component retains its own exact query/response semantics; no independent root query/response universe exists. | `B04/semantics` |
| `C2-584` | No-partition composite exact set proof | With empty root partitions, exact component-scope bijection plus empty component partition sets is the gap proof. | `B04/no-partition` |
| `C2-585` | Partitioned composite needs dual closure | With root partitions, both exact component-scope bijection and pairwise-disjoint exact partition union are mandatory. | `B04/partition` |
| `C2-586` | Partition union alone insufficient | Exact partition union cannot compensate for a missing or extra component scope. | `B04/adversarial` |
| `C2-587` | Component enumeration cannot coexist with conflicting root query/response | A root that enumerates components but also asserts independent query/response refs fails closed. | `B04/adversarial` |
| `C2-588` | No inferred semantic equivalence | Provider names, labels, query text similarity, or schema similarity cannot substitute for exact component-scope membership. | `B04/security` |
| `C2-589` | Closed B01/B02/B05 surfaces preserved | R2 does not weaken evidence-carrier closure, certification totality, or coverage-classifier totality. | `non-regression` |
| `C2-590` | Parent C2.04 and ownership non-regression | C2.04R1 remains 113/113 PASS and C1/C3/C4/C5/C6/C7/C11/C12 ownership boundaries remain unchanged. | `non-regression` |

## Required re-check matrix

### C2CERT-B03
Re-run: `C2-437`, `C2-438`, `C2-481`, `C2-525`.
New: `C2-556..C2-577`.

### C2CERT-B04
Re-run: `C2-471`, `C2-481`, `C2-539`, `C2-540`.
New: `C2-578..C2-588`.

### Non-regression
New: `C2-589..C2-590`.
The independent re-check must also preserve all currently passing C2.05/R1 obligations.

## Gate

No construction self-check closes C2CERT-B03 or C2CERT-B04.

Independent Certification Re-Check is required before C2.05 may become `REVIEW_PASSED_NOT_FROZEN`.
