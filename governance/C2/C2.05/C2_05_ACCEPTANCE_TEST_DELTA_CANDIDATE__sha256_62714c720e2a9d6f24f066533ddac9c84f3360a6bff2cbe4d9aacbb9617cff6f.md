# C2.05 — Acceptance Test Delta Candidate

Generated: 2026-09-07T06:01:18Z

Status: `CANDIDATE_FOR_C2_05_INDEPENDENT_CERTIFICATION_REVIEW`

Parent effective C2.04 acceptance after R1: `C2-289..C2-401` = `113/113 PASS`.

This C2.05 candidate adds certification/completeness/coverage obligations. Construction does not mark them independently passed.

| ID | Test | Required Behavior | Type |
|---|---|---|---|
| `C2-402` | Stable ref kinds are closed | Unknown/private C2.05 certification/coverage ref kinds fail closed and cannot become load-bearing. | `certification/contract` |
| `C2-403` | Floating certification alias rejected | A floating latest/current certification or coverage alias cannot support deterministic certification/completeness. | `certification/contract` |
| `C2-404` | Registry snapshot required | Load-bearing certification/coverage use pins one exact immutable ProviderCertificationRegistrySnapshot. | `certification/contract` |
| `C2-405` | Certification state vocabulary closed | Only CERTIFIED/NOT_CERTIFIED/SUSPENDED/REVOKED/SUPERSEDED/INDETERMINATE are valid registry certification states. | `certification/contract` |
| `C2-406` | Only CERTIFIED is load-bearing | NOT_CERTIFIED/SUSPENDED/REVOKED/SUPERSEDED/INDETERMINATE cannot satisfy a certification dependency. | `certification/contract` |
| `C2-407` | Coverage registry state vocabulary closed | Only ACTIVE/SUSPENDED/REVOKED/SUPERSEDED/INDETERMINATE are valid effective coverage states. | `certification/contract` |
| `C2-408` | Only ACTIVE coverage is load-bearing | Non-ACTIVE coverage attestations cannot support absence/uniqueness. | `certification/contract` |
| `C2-409` | Required certification check missing fails | Any required CertificationCheckClass missing from the bundle prevents CERTIFIED. | `certification/evidence` |
| `C2-410` | Duplicate required certification check invalid | Duplicate required check classes invalidate the bundle even when values agree. | `certification/evidence` |
| `C2-411` | Required FAIL blocks certification | Any required check result FAIL yields NOT_CERTIFIED. | `certification/evidence` |
| `C2-412` | Required INDETERMINATE blocks certification | Any required check result INDETERMINATE yields INDETERMINATE and cannot certify. | `certification/evidence` |
| `C2-413` | Required NOT_APPLICABLE invalid | Required check classes cannot be NOT_APPLICABLE. | `certification/evidence` |
| `C2-414` | Unknown check class invalid | Unknown/private-extension check classes invalidate the profile/bundle. | `certification/evidence` |
| `C2-415` | Evidence subject mismatch invalid | Evidence/check results bound to another provider/endpoint/capability/profile cannot certify the target. | `certification/evidence` |
| `C2-416` | Unresolved evidence ref fails closed | Dangling/wrong-kind/hash-mismatched load-bearing evidence refs prevent certification. | `certification/evidence` |
| `C2-417` | Percentage score cannot replace all checks | A high average or majority PASS cannot compensate for a missing/failed/indeterminate required check. | `certification/evidence` |
| `C2-418` | Provider documentation alone insufficient | First-party provider documentation without required conformance/exhaustion evidence cannot establish certification/completeness. | `certification/evidence` |
| `C2-419` | Certification is not C5 verification | CERTIFIED cannot set C5 VERIFIED, source fitness, evidence independence, or conflict state. | `boundary/non-regression` |
| `C2-420` | Certification grants no C6 authority | CERTIFIED grants no capability, trusted intent, destination, WRITE/PAPER/LIVE, or side-effect authority. | `boundary/non-regression` |
| `C2-421` | Certification does not rank routes | CERTIFIED/NOT_CERTIFIED cannot invent or reorder C2.03 route priority. | `boundary/non-regression` |
| `C2-422` | Certification is not current health | Certification state cannot be interpreted as uptime, latency, quota headroom, freshness, or cache state. | `boundary/non-regression` |
| `C2-423` | Semantic successor does not inherit certification | A new provider/endpoint/capability stable ref requires a new supported certification; old certification cannot auto-carry. | `certification/invalidation` |
| `C2-424` | Response-schema drift suspends | Trusted material response-schema drift makes continued load-bearing use fail closed until a successor snapshot supports recertification. | `certification/invalidation` |
| `C2-425` | Absence-signal drift suspends | Trusted absence-signal semantic drift prevents continued absence-support use. | `certification/invalidation` |
| `C2-426` | Partiality-signal drift suspends | Trusted partiality-signal drift prevents continued completeness use. | `certification/invalidation` |
| `C2-427` | Pagination/exhaustion drift suspends | Trusted pagination/terminal-condition drift prevents continued completeness use. | `certification/invalidation` |
| `C2-428` | Limit/truncation drift suspends | Trusted provider/client limit or truncation drift prevents continued completeness use. | `certification/invalidation` |
| `C2-429` | Unknown material change fails closed | UNKNOWN_MATERIAL_CHANGE cannot be ignored and yields SUSPENDED/INDETERMINATE semantics. | `certification/invalidation` |
| `C2-430` | Revocation is non-load-bearing | A registry snapshot marking a certification REVOKED makes it unusable for load-bearing coverage support. | `certification/invalidation` |
| `C2-431` | Superseded old ref remains replayable only | Historical replay may resolve an old certification ref, but a successor registry snapshot cannot treat it as current when SUPERSEDED. | `certification/invalidation` |
| `C2-432` | Coverage scope exact ref required | Every load-bearing coverage attestation binds exactly one immutable CoverageScopeDefinition. | `coverage/scope` |
| `C2-433` | Coverage scope list canonicalization | Exact duplicates deduplicate, conflicting same-logical-id revisions invalidate, and order is deterministic. | `coverage/scope` |
| `C2-434` | Coverage wildcard prohibited | Wildcard/prefix/display-name/hierarchy implication cannot broaden a coverage scope. | `coverage/scope` |
| `C2-435` | Exact scope match required | A completeness dependency is load-bearing only when required_coverage_scope_ref exactly equals attested coverage_scope_ref. | `coverage/scope` |
| `C2-436` | Provider/endpoint/capability scope mismatch fails | An attestation for a different provider, endpoint, or capability cannot support the operation. | `coverage/scope` |
| `C2-437` | Query-semantic scope mismatch fails | Required query semantic refs differing from the exact attested scope invalidate support. | `coverage/scope` |
| `C2-438` | Response-semantic scope mismatch fails | Attempted/required response semantic scope outside the attested scope invalidates support. | `coverage/scope` |
| `C2-439` | Partition scope mismatch fails | A missing/unexpected coverage partition prevents exact scope closure. | `coverage/scope` |
| `C2-440` | Historical temporal dependency required when applicable | Historical/time-bounded coverage that needs C4 interpretation carries an opaque temporal_scope_dependency_ref. | `coverage/temporal` |
| `C2-441` | Temporal dependency mismatch fails | A historical completeness dependency cannot substitute a different opaque temporal_scope_dependency_ref. | `coverage/temporal` |
| `C2-442` | C2 completeness does not imply C4 PIT | COMPLETE_FOR_SCOPE cannot set available_from, revision, PIT safety, visibility, or reconstructability. | `boundary/non-regression` |
| `C2-443` | Coverage classification vocabulary closed | Coverage classification is exactly COMPLETE_FOR_SCOPE/PARTIAL_KNOWN/NON_EXHAUSTIVE/INDETERMINATE/INVALID. | `coverage/attestation` |
| `C2-444` | Only COMPLETE_FOR_SCOPE is load-bearing | All non-complete coverage classifications are ineligible for exact absence/uniqueness support. | `coverage/attestation` |
| `C2-445` | Coverage requires certified provider | COMPLETE_FOR_SCOPE cannot be load-bearing unless its provider certification is CERTIFIED in the same pinned registry snapshot. | `coverage/attestation` |
| `C2-446` | Coverage attestation must be ACTIVE | A complete attestation marked SUSPENDED/REVOKED/SUPERSEDED/INDETERMINATE in the snapshot cannot support claims. | `coverage/attestation` |
| `C2-447` | Method family vocabulary closed | Only the six closed C2.05 CoverageMethodProfile families may establish exhaustion. | `coverage/method` |
| `C2-448` | Access-pattern name alone insufficient | ENUMERATION, DIRECT_LOOKUP, BULK_EXPORT, or any access-pattern label alone never proves completeness. | `coverage/method` |
| `C2-449` | SUCCESS+NO_DATA alone insufficient | SUCCESS+NO_DATA without valid complete coverage cannot support exact absence. | `coverage/outcome` |
| `C2-450` | SUCCESS+PRESENT alone insufficient | SUCCESS+PRESENT, including one returned row, cannot by itself support uniqueness. | `coverage/outcome` |
| `C2-451` | SUCCESS+PARTIAL never absence/uniqueness | PARTIAL can carry positive observations but cannot support absence or uniqueness. | `coverage/outcome` |
| `C2-452` | FAILED/CANCELLED never completeness support | FAILED or CANCELLED cannot support absence/uniqueness and cannot become NO_DATA through certification. | `coverage/outcome` |
| `C2-453` | Exact-key singleton requires closed absence semantics | EXACT_KEY_SINGLETON completeness requires exact key scope, bound absence semantics, closed cardinality, and no continuation/partiality. | `coverage/method` |
| `C2-454` | Exact-key scope is not provider-wide | An EXACT_KEY_SINGLETON attestation cannot prove completeness outside its exact singleton scope. | `coverage/method` |
| `C2-455` | Pagination must reach terminal condition | PAGINATION_EXHAUSTION requires every continuation to the pinned terminal condition. | `coverage/method` |
| `C2-456` | Pagination unresolved continuation fails | Missing/ambiguous continuation or terminal semantics prevents COMPLETE_FOR_SCOPE. | `coverage/method` |
| `C2-457` | Pagination cycle fails | Repeated/cyclic continuation tokens cannot be treated as exhaustion. | `coverage/method` |
| `C2-458` | Client/provider page cap fails | Max-page, SDK default limit, timeout/manual stop, or unresolved truncation prevents completeness. | `coverage/method` |
| `C2-459` | Partition exact closure required | PARTITION_EXHAUSTION requires exactly one complete component for every required partition with no gap. | `coverage/method` |
| `C2-460` | Missing partition fails | One missing required partition prevents COMPLETE_FOR_SCOPE. | `coverage/method` |
| `C2-461` | Incomplete component fails composite partition | A PARTITION_EXHAUSTION component that is non-complete prevents aggregate completeness. | `coverage/method` |
| `C2-462` | Bulk object alone insufficient | Receiving a bulk object without required manifest/segment/count closure evidence cannot prove completeness. | `coverage/method` |
| `C2-463` | Bulk segment omission fails | Missing/unresolved bulk segments or manifest mismatch prevents completeness. | `coverage/method` |
| `C2-464` | Window bounds exact | WINDOW_BOUNDARY_EXHAUSTION proves only the exact provider-native window with exact inclusion/exclusion semantics. | `coverage/method` |
| `C2-465` | Window claim cannot leak outside scope | A complete window attestation cannot support absence/uniqueness outside the exact window. | `coverage/method` |
| `C2-466` | Ranked search default non-exhaustive | Ranked/fuzzy SEARCH or first-N retrieval is NON_EXHAUSTIVE unless one closed method proves exact exhaustion. | `coverage/method` |
| `C2-467` | Stream default non-exhaustive | Open-ended STREAM_SUBSCRIPTION cannot imply complete historical universe coverage. | `coverage/method` |
| `C2-468` | Partial attestations cannot be silently unioned | Two or more PARTIAL/NON_EXHAUSTIVE attestations cannot become COMPLETE by union or provider count. | `coverage/composite` |
| `C2-469` | Composite requires explicit closure record | Composite completeness requires an exact COMPOSITE_EXPLICIT_CLOSURE attestation and exact component refs. | `coverage/composite` |
| `C2-470` | Composite components must be complete and active | Every component of a complete composite attestation must itself be COMPLETE_FOR_SCOPE and ACTIVE under certified provider state. | `coverage/composite` |
| `C2-471` | Composite gap proof is machine-closed | Human-readable provider labels or informal overlap claims cannot substitute for exact partition/scope gap closure. | `coverage/composite` |
| `C2-472` | Secure-ingress evidence prerequisite | Provider-derived certification/coverage evidence must pass C2.04 secure ingress or remain sanitized non-content-bearing metadata. | `security/non-regression` |
| `C2-473` | Quarantine/reject cannot certify | Quarantined or rejected provider material cannot support certification/completeness. | `security/non-regression` |
| `C2-474` | EPHEMERAL_ONLY cannot gain persisted raw | Certification evidence requirements cannot force persistence of EPHEMERAL_ONLY provider bytes. | `security/non-regression` |
| `C2-475` | Public certification artifact contains no secret/private material | Certification reports/ledgers cannot expose credential/private-state material or unsafe secret-derived identifiers. | `security/non-regression` |
| `C2-476` | ABSENCE_SUPPORT_ELIGIBLE is not NO_MATCH | Valid SUCCESS+NO_DATA+complete coverage produces only eligibility for C1 absence reasoning, not canonical NO_MATCH. | `c1/boundary` |
| `C2-477` | UNIQUENESS_SUPPORT_ELIGIBLE is not RESOLVED | Valid SUCCESS+PRESENT+complete coverage produces only eligibility for uniqueness reasoning, not canonical resolution. | `c1/boundary` |
| `C2-478` | Positive exact mapping may omit completeness | A positive exact mapping that does not depend on absence is not universally rejected for lacking completeness. | `c1/boundary` |
| `C2-479` | Coverage cannot override C2.02 partiality | A COMPLETE_FOR_SCOPE attestation cannot upgrade a material C2.02 PARTIAL result to exhaustive. | `coverage/outcome` |
| `C2-480` | Operation pins exact registry/certification/attestation refs | Replay retains exact certification registry snapshot and exact load-bearing certification/coverage refs. | `replay/contract` |
| `C2-481` | Replay is deterministic | Identical pinned semantic inputs and registry snapshot reproduce the same certification/coverage support decision. | `replay/contract` |
| `C2-482` | No mutable current-state lookup in replay | Historical reconstruction cannot consult floating current certification/coverage state. | `replay/contract` |
| `C2-483` | No concrete provider/vendor selected | C2.05 candidate contains zero provider instances, vendor priority choices, secret-store choices, or production adapters. | `scope/non-expansion` |
| `C2-484` | C2.OPEN-009 only candidate-closed | Construction may mark provider-certification question candidate-closed pending independent review, not final closed. | `governance` |
| `C2-485` | C2.OPEN-010 only candidate-closed | Construction may mark completeness-methodology question candidate-closed pending independent review, not final closed. | `governance` |
| `C2-486` | C2.OPEN-011 only candidate-closed | Construction may mark temporal-validity representation candidate-closed pending independent review, not final closed. | `governance` |
| `C2-487` | C2.OPEN-012..015 remain deferred | Cross-contract wires, C2->C11 handoff, machine schema, and concrete providers remain open at their assigned later stages. | `governance` |

## Required Independent Certification Review Focus

The independent review must not merely count rows. It must adversarially determine whether the candidate is deterministic, scope-exact, replayable, and fail-closed for:

- certification state/evidence-bundle completeness and invalidation;
- immutable registry-snapshot applicability and stale/superseded-ref misuse;
- exact coverage-scope identity and no wildcard/human-label broadening;
- pagination, partition, bulk, window, exact-key, ranked-search, stream, and composite exhaustion cases;
- `SUCCESS+NO_DATA`, `SUCCESS+PRESENT`, `SUCCESS+PARTIAL`, `FAILED`, and `CANCELLED` interaction with completeness support;
- absence/uniqueness eligibility remaining distinct from C1 conclusions;
- C4 temporal/PIT non-absorption and C5 verification non-absorption;
- C2.04 secure-ingress non-regression;
- no provider/vendor/adaptor selection or side-effect authority;
- exact replay from pinned stable refs.

C2.06 remains `NOT_AUTHORIZED` until an Independent Certification Review returns PASS or an explicitly scoped repair/re-check sequence completes.
