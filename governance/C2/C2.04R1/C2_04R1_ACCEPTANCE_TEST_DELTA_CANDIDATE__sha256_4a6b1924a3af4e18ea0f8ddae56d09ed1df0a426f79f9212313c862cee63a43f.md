# C2.04R1 — Acceptance Test Delta Candidate

Generated: 2026-09-07T05:36:00Z

Status: `REPAIR_CANDIDATE_PENDING_INDEPENDENT_SECURITY_BOUNDARY_RECHECK`

Parent reviewed acceptance: `C2-289..C2-348` (`58 PASS / 2 FAIL`, failed `C2-313`, `C2-319`).

This R1 delta adds adversarial coverage for `C2SEC-B01..B04`. It does not mark any blocker closed.

| ID | Test | Required Behavior | Type |
|---|---|---|---|
| `C2-349` | Unknown redirect mode rejected | A CredentialBindingProfile using a redirect_forwarding_semantics value outside the closed R1 enum fails closed and cannot dispatch. | `security/repair-contract` |
| `C2-350` | Unresolved redirect identity blocks | Any unresolved/ambiguous source or target provider, endpoint, capability, or destination-authority identity yields BLOCK. | `security/repair-contract` |
| `C2-351` | Cross-provider redirect blocks | A redirect whose target provider_profile_ref differs from the source yields BLOCK for the existing lease. | `security/repair-contract` |
| `C2-352` | Cross-authority redirect blocks | A redirect whose target_destination_authority_ref differs from the source yields BLOCK for the existing lease even when target endpoint is otherwise known. | `security/repair-contract` |
| `C2-353` | Same-authority unbound endpoint blocks | Same-provider/same-authority redirect to an endpoint outside allowed_endpoint_profile_refs yields BLOCK. | `security/repair-contract` |
| `C2-354` | Same-authority different allowed endpoint requires rebind | Under FORWARD_SAME_AUTHORITY_SAME_ENDPOINT, a different but allowed endpoint yields REBIND_REQUIRED, never forwarding. | `security/repair-contract` |
| `C2-355` | Same-authority exact endpoint may forward | Under FORWARD_SAME_AUTHORITY_SAME_ENDPOINT, same provider/authority/capability/exact endpoint yields FORWARD_EXISTING_LEASE. | `security/repair-contract` |
| `C2-356` | Rebind-on-any redirect is deterministic | Under REBIND_ON_ANY_REDIRECT, an otherwise eligible same-authority redirect yields REBIND_REQUIRED. | `security/repair-contract` |
| `C2-357` | Block-all redirect is deterministic | Under BLOCK_ALL_REDIRECTS, every redirect yields BLOCK after identity resolution. | `security/repair-contract` |
| `C2-358` | Redirect capability change blocks | A redirect that would change provider_capability_ref yields BLOCK even within the same authority. | `security/repair-contract` |
| `C2-359` | HTTP client auto-redirect cannot bypass predicate | Automatic HTTP/SDK redirect behavior must not forward credential material when the R1 predicate returns BLOCK or REBIND_REQUIRED. | `security/repair-contract` |
| `C2-360` | Redirect replay is deterministic | The same pinned profile plus identical trusted redirect identity inputs produces the same redirect decision across implementations. | `security/repair-contract` |
| `C2-361` | Lease requires provider operation identity | A CredentialLease missing provider_operation_ref is invalid/BLOCKED. | `security/repair-contract` |
| `C2-362` | Lease requires route-attempt identity | A CredentialLease missing route_attempt_ref is invalid/BLOCKED. | `security/repair-contract` |
| `C2-363` | Lease exact-use identity matches | A READY lease may be used only when all presented operation/attempt/provider/endpoint/capability/binding/credential identity fields exactly match the issued descriptor. | `security/repair-contract` |
| `C2-364` | Provider-operation mismatch rejects reuse | Presenting a READY lease to a different provider_operation_ref yields LEASE_OPERATION_IDENTITY_MISMATCH and no dispatch. | `security/repair-contract` |
| `C2-365` | Route-attempt mismatch rejects reuse | Presenting a READY lease to a different route_attempt_ref yields LEASE_OPERATION_IDENTITY_MISMATCH and no dispatch. | `security/repair-contract` |
| `C2-366` | Lease ID cannot span operation identities | The same credential_lease_id associated with two different provider_operation_ref or route_attempt_ref values is invalid. | `security/repair-contract` |
| `C2-367` | New operation requires fresh lease | A new provider operation/route attempt using the same credential version still requires a fresh credential_lease_id. | `security/repair-contract` |
| `C2-368` | Operation identity grants no capability | provider_operation_ref and route_attempt_ref never grant C6 capability, egress, or side-effect authority. | `security/repair-contract` |
| `C2-369` | Redirect rebind requires fresh lease ID | REBIND_REQUIRED cannot reuse the prior credential_lease_id for the target endpoint. | `security/repair-contract` |
| `C2-370` | Scope ref wrong-kind or unresolved fails closed | Any wrong-kind/dangling/hash-mismatched/unknown PRIVATE_STATE_SCOPE ref makes the relevant scope set invalid. | `security/repair-contract` |
| `C2-371` | Conflicting scope revisions in one set invalid | Two scope refs sharing logical_id but differing in revision/hash within one set produce INVALID scope set. | `security/repair-contract` |
| `C2-372` | Exact duplicate scope refs canonicalize | Exact duplicate scope refs are deduplicated without changing canonical set meaning. | `security/repair-contract` |
| `C2-373` | Scope canonicalization is order invariant | Input ordering of valid scope refs does not change the canonical scope set or subset decision. | `security/repair-contract` |
| `C2-374` | Exact actual subset passes | A valid canonical actual scope set whose every ref exactly belongs to the declared set yields WITHIN_DECLARED_SCOPE. | `security/repair-contract` |
| `C2-375` | Out-of-scope actual ref blocks | Any valid actual scope ref not exactly present in the declared canonical set yields BLOCKED_SCOPE and no private-state dispatch; re-checks C2-313. | `security/repair-contract` |
| `C2-376` | Empty actual scope is valid | An empty canonical actual scope set is valid and is a subset of any valid declared set. | `security/repair-contract` |
| `C2-377` | No wildcard or hierarchy implication | A scope ref cannot authorize another ref via wildcard, prefix, display-name, hierarchy, or implied containment. | `security/repair-contract` |
| `C2-378` | External content cannot add actual scope | Provider/web/tool/model content cannot add or replace actual_private_state_scope_refs. | `security/repair-contract` |
| `C2-379` | Free-form public projection rule rejected | A raw/unpinned public_projection_rule string is not load-bearing under R1. | `security/repair-contract` |
| `C2-380` | Unresolved projection rule blocks | Unresolved/wrong-kind/hash-mismatched public_projection_rule_ref blocks private-state preparation. | `security/repair-contract` |
| `C2-381` | Exclude-all projection emits no private state | EXCLUDE_ALL_PRIVATE_STATE emits no private-state handles or values into public artifacts. | `security/repair-contract` |
| `C2-382` | Metadata allowlist is closed | ALLOWLIST_METADATA_ONLY may emit only metadata IDs in the closed R1 vocabulary and only when named in the exact rule. | `security/repair-contract` |
| `C2-383` | Forbidden projection field invalid | A projection rule attempting to allow private_state_handle_ref/account/portfolio/transaction/order/thesis/credential/secret-store/secret material is invalid. | `security/repair-contract` |
| `C2-384` | Assessment bundle has exactly one result per axis | A VALID SecureIngressAssessmentRecord has exactly four axis results and exactly one each for SECRET, PRIVACY, LICENSING, RETENTION. | `security/repair-contract` |
| `C2-385` | Missing ingress axis fails closed | A bundle missing any required axis is INVALID_FAIL_CLOSED -> QUARANTINE/NONE. | `security/repair-contract` |
| `C2-386` | Duplicate ingress axis fails closed | A bundle containing a duplicate axis is invalid even when duplicate constraints agree. | `security/repair-contract` |
| `C2-387` | Unknown ingress axis or constraint fails closed | Unknown axis or constraint values invalidate the bundle and prevent admission. | `security/repair-contract` |
| `C2-388` | Mixed ingress candidates fail closed | Axis results from different ingress_event_id values cannot be combined; bundle becomes INVALID_FAIL_CLOSED. | `security/repair-contract` |
| `C2-389` | Mixed provider operations fail closed | Axis results from different provider_operation_ref values cannot be combined. | `security/repair-contract` |
| `C2-390` | Mixed ingress profiles fail closed | Axis results using different secure_ingress_semantic_profile_ref values cannot be combined. | `security/repair-contract` |
| `C2-391` | Mixed policy snapshots fail closed | An axis result whose policy_ref differs from the record's corresponding exact pinned policy ref invalidates the bundle. | `security/repair-contract` |
| `C2-392` | Unresolved profile or policy fails closed | Any unresolved/non-immutable secure-ingress profile or policy ref invalidates the bundle and prevents admission. | `security/repair-contract` |
| `C2-393` | Valid bundle preserves parent precedence | For a VALID bundle, REJECT > QUARANTINE/INDETERMINATE > REDACT > ADMIT with EPHEMERAL_ONLY retention precedence remains unchanged. | `security/repair-contract` |
| `C2-394` | Stored ingress decision must recompute | A stored ingress_decision or retention_mode that disagrees with recomputation invalidates the record. | `security/repair-contract` |
| `C2-395` | Ingress decision links to assessment record | A load-bearing ingress_decision_ref must resolve to exactly one SecureIngressAssessmentRecord; a bare decision enum cannot authorize admission. | `security/repair-contract` |
| `C2-396` | Redacted candidate requires new complete record | REASSESS_REDACTED output receives a new ingress_event_id, new assessment record ID, and four new axis result IDs. | `security/repair-contract` |
| `C2-397` | Old axis results cannot admit redacted candidate | Pre-redaction axis results/assessment record may be lineage only and cannot be load-bearing for the redacted candidate. | `security/repair-contract` |
| `C2-398` | Explicit INDETERMINATE is valid but quarantined | If an assessor cannot determine an axis under otherwise valid bindings, that axis appears once as INDETERMINATE and the valid bundle yields QUARANTINE/NONE. | `security/repair-contract` |
| `C2-399` | Invalid bundle cannot admit in any retention mode | INVALID_FAIL_CLOSED cannot produce ADMIT+PERMITTED_RAW or ADMIT+EPHEMERAL_ONLY and cannot enter C1 normalization. | `security/repair-contract` |
| `C2-400` | Ingress axes separate plus integrity-closed | Re-check C2-319: all four constraints remain separate fields/results and are bound exactly once to one candidate/profile/policy set. | `security/repair-contract` |
| `C2-401` | C2.04 PASS surface non-regression | R1 does not weaken the other previously PASS C2-289..C2-348 obligations; only C2-313/C2-319 are repaired and B01/B04 receive new coverage. | `security/repair-contract` |

## Required R1 independent re-check focus

The independent re-check must:

- re-run/reason through parent failed obligations `C2-313` and `C2-319` against the combined parent + R1 contract;
- test every new R1 obligation `C2-349..C2-401`;
- verify deterministic same-authority and cross-authority redirect behavior;
- verify exact CredentialLease operation/route-attempt binding and cross-operation reuse rejection;
- verify stable atomic private-state scope refs, canonical set/subset semantics, and pinned public-projection rules;
- verify exactly-one-per-axis secure-ingress bundle integrity, candidate/profile/policy coherence, fail-closed invalid bundles, and exact decision linkage;
- verify the remaining parent PASS surface is not weakened;
- treat mechanical construction checks as non-independent evidence only.

C2.05 remains `NOT_AUTHORIZED`.
