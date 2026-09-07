# C2.05R3 — Acceptance Test Delta Candidate

Generated: 2026-09-07T16:27:00Z

Status: `SCOPED_REPAIR_CANDIDATE_PENDING_INDEPENDENT_CERTIFICATION_RECHECK`

Parent effective range before R3: `C2-402..C2-590`.

Residual failed obligations that MUST be independently re-run:

```text
C2-471
C2-481
C2-540
C2-557
C2-584
C2-585
```

C2.05R3 adds `C2-591..C2-640` = 50 adversarial obligations. Construction does not mark any residual failure or new obligation independently PASS.

| ID | Test | Required Behavior | Type |
|---|---|---|---|
| `C2-591` | Executed request semantic state ref kind closed | executed_request_semantic_state_ref resolves only as EXECUTED_REQUEST_SEMANTIC_STATE. | `B03/type` |
| `C2-592` | Coverage authority binding ref kind closed | coverage_authority_binding_ref resolves only as OPERATION_COVERAGE_AUTHORITY_BINDING. | `B03/type` |
| `C2-593` | Executed state sealed before dispatch | Load-bearing state has request_scope_commitment_state exactly SEALED_BEFORE_DISPATCH_FOR_EXECUTION. | `B03/timing` |
| `C2-594` | Exact state consumed by dispatch | dispatch_consumed_executed_request_semantic_state_ref equals the exact executed state ref. | `B03/execution` |
| `C2-595` | Exact state replay-retained | replay_retained_executed_request_semantic_state_ref equals the exact dispatch-consumed state ref. | `B03/replay` |
| `C2-596` | Executed state identity exact | State provider operation, route attempt, snapshot, provider, endpoint and capability identities match the actual attempt exactly. | `B03/identity` |
| `C2-597` | Executed state R exact | Executed state CapabilityRequirement R equals the exact replay-retained C2.01 R and its SHA-256 equals canonical R bytes. | `B03/R` |
| `C2-598` | Native subject bound to execution state | Provider-native subject scope used for completeness comes from the exact dispatch-consumed executed state. | `B03/native` |
| `C2-599` | Identifier namespace bound to execution state | Provider-native identifier namespace scope comes from the exact dispatch-consumed executed state. | `B03/native` |
| `C2-600` | Partition bound to execution state | Coverage partition scope comes from the exact dispatch-consumed executed state. | `B03/partition` |
| `C2-601` | Constraint bound to execution state | Scope constraints come from the exact dispatch-consumed executed state. | `B03/constraint` |
| `C2-602` | Temporal dependency bound to execution state | Temporal dependency is BOTH_ABSENT or exact same ref as the dispatch-consumed state. | `B03/temporal` |
| `C2-603` | Coverage-relevant unrepresented request dimension blocks support | Any request semantic condition changing candidate-universe scope but absent from executed state makes completeness support ineligible. | `B03/execution` |
| `C2-604` | SDK/default hidden scope cannot fill state | SDK defaults, raw parameter labels, provider docs or inferred wildcard scope cannot substitute for a missing executed-state dimension. | `B03/adversarial` |
| `C2-605` | Coverage-capable certification requires request-scope conformance | Any certification backing load-bearing coverage includes REQUEST_SCOPE_CONFORMANCE as a required check. | `B03/certification` |
| `C2-606` | B02 classifier unchanged by required request check | Adding REQUEST_SCOPE_CONFORMANCE to the required set does not alter B02 ordered certification-decision semantics. | `B03/non-regression` |
| `C2-607` | Provenance references executed state | OperationCoverageProvenance carries the exact executed_request_semantic_state_ref from the attempt authority binding. | `B03/provenance` |
| `C2-608` | Provenance native fields project executed state | Native subject, identifier, partition, constraint and temporal fields exactly project the executed state. | `B03/projection` |
| `C2-609` | Provenance R chain exact | Provenance R == executed-state R == replay-retained R and all canonical digests agree. | `B03/provenance` |
| `C2-610` | R2 attempted-response provenance preserved | Provenance attempted-response set remains exactly the C2.02R2 stored/recomputed set A. | `B03/non-regression` |
| `C2-611` | Pre-dispatch coverage assertion alone insufficient | A sealed provenance record not consumed by request construction cannot support completeness. | `B03/adversarial` |
| `C2-612` | Wrong native-scope attack blocked | Actual executed state COUNTRY_US cannot be supported by provenance/binding/scope claiming COUNTRY_GLOBAL. | `B03/adversarial` |
| `C2-613` | Wrong executed-state attempt blocked | An executed request state from another route attempt cannot support this attempt even when scope fields match. | `B03/identity` |
| `C2-614` | Exactly one attempt authority slot | Load-bearing attempt replay retains exactly one coverage_authority_binding_ref. | `B03/authority` |
| `C2-615` | Authority binding resolves singular provenance | The exact retained authority binding identifies exactly one authoritative operation_coverage_provenance_ref. | `B03/authority` |
| `C2-616` | Unreferenced provenance claim ignored | A later record claiming the same operation/attempt but not referenced by the authority binding has zero load-bearing authority. | `B03/replay` |
| `C2-617` | Global provenance scan forbidden | Historical replay may not scan a mutable/global store, index, namespace or claim set to determine provenance uniqueness. | `B03/replay` |
| `C2-618` | Later duplicate claim cannot change history | Adding an unreferenced P2 after T1 cannot change T1 support when the exact attempt-retained authority binding still points to P1. | `B03/adversarial` |
| `C2-619` | Missing authority slot cannot complete | An attempt lacking the exact attempt-retained coverage authority binding cannot support COMPLETE_FOR_SCOPE. | `B03/authority` |
| `C2-620` | Multiple authority refs in attempt slot invalid | A replay surface containing more than one authoritative coverage binding is invalid, not implementation-selected. | `B03/authority` |
| `C2-621` | Authority identity mismatch invalid | Authority binding operation/attempt/state/provenance identity mismatch fails closed. | `B03/identity` |
| `C2-622` | Operation binding projects authoritative provenance | OperationCoverageScopeBinding is valid only after exact projection from the provenance selected by the attempt authority binding. | `B03/projection` |
| `C2-623` | Execution-binding replay permutation invariant | Canonical set ordering in executed state/provenance cannot change the support decision. | `B03/replay` |
| `C2-624` | Composite decomposition ref kind closed | composite_decomposition_relation_ref resolves only as COMPOSITE_SCOPE_DECOMPOSITION_RELATION. | `B04/type` |
| `C2-625` | Composite root query is operation-bound | Root required query set exactly equals the consuming operation binding's required query set; R2 forced-empty rule is not a success path. | `B04/root` |
| `C2-626` | Composite root response equals exact C2.02 A | Root required response set exactly equals the consuming operation's C2.02R2 attempted-response set A. | `B04/root` |
| `C2-627` | Endpoint primary response present at root | A valid composite root response set includes E.response_semantics.response_semantic_ref and therefore cannot be empty. | `B04/C2.02` |
| `C2-628` | Empty root response composite rejected | A dispatched composite-root attempt with empty required_response_semantic_refs cannot be load-bearing. | `B04/adversarial` |
| `C2-629` | Relation binds exact root scope | Relation root_coverage_scope_ref and parent snapshot exactly equal the root scope. | `B04/relation` |
| `C2-630` | Relation component set exact | Relation component_scope_refs exactly equals root composite_component_scope_refs after canonicalization. | `B04/relation` |
| `C2-631` | Root query keys exact | Query decomposition entry keys equal the root required query set exactly, with each root key exactly once. | `B04/relation` |
| `C2-632` | Root response keys exact | Response decomposition entry keys equal the root required response set exactly, including the endpoint primary response semantic. | `B04/relation` |
| `C2-633` | Component semantic membership exact | Every relation component_semantic_ref is an exact member of the named component scope's corresponding axis set. | `B04/relation` |
| `C2-634` | Component semantic total coverage | Every query/response semantic ref in every component scope is represented exactly once on the corresponding axis. | `B04/relation` |
| `C2-635` | Component semantic double assignment invalid | One component semantic ref assigned under two root semantic keys fails closed. | `B04/relation` |
| `C2-636` | Cross-axis mapping invalid | Query refs cannot satisfy response decomposition and response refs cannot satisfy query decomposition. | `B04/relation` |
| `C2-637` | Missing/extra decomposition fails | Missing root key, extra root key, missing component semantic, extra component scope, unresolved relation member or hash mismatch fails closure. | `B04/adversarial` |
| `C2-638` | No inferred decomposition authority | Provider names, labels, query text similarity, schema similarity, marketing docs or manual unpinned mappings cannot substitute for the exact relation. | `B04/security` |
| `C2-639` | No-partition composite requires semantic plus scope closure | Empty root partitions require all-empty component partitions, exact component-scope bijection and exact semantic decomposition closure. | `B04/no-partition` |
| `C2-640` | Partitioned composite requires semantic plus partition dual closure | Root partitions require exact component-scope closure, exact semantic decomposition closure and pairwise-disjoint exact partition union; B01/B02/B05, C2.04 and ownership boundaries remain non-regressed. | `B04/non-regression` |

## Required re-check matrix

### C2CERT-B03
Re-run: `C2-481`, `C2-557`.
New: `C2-591..C2-623`.
Adversarially re-evaluate prior `C2-567..C2-571` against the stronger executed-request binding, not merely their R2 wording.

### C2CERT-B04
Re-run: `C2-471`, `C2-540`, `C2-584`, `C2-585`.
New: `C2-624..C2-640`.

### Non-regression
The independent re-check must preserve all currently passing C2.05/R1/R2 obligations and C2.04 effective acceptance `C2-289..C2-401 = 113/113 PASS`.

## Gate

No construction self-check closes C2CERT-B03 or C2CERT-B04.

Independent Certification Re-Check is required before C2.05 may become `REVIEW_PASSED_NOT_FROZEN`.
