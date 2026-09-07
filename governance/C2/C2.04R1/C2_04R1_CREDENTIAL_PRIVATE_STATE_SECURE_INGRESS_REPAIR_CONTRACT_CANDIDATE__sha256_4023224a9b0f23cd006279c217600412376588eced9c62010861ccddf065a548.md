# C2.04R1 — Credentials / Private-State / Secure Ingress Boundary Scoped Repair Candidate

Generated: 2026-09-07T05:36:00Z

Status: `REPAIR_CANDIDATE_PENDING_INDEPENDENT_SECURITY_BOUNDARY_RECHECK`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

## 1. Authorization, scope, and effective-contract rule

The user explicitly authorized **C2.04R1 scoped repair** after the C2.04 Independent Security-Boundary Review returned `FAIL`.

This repair is limited to the four review blockers:

- `C2SEC-B01` — redirect-forwarding semantic closure;
- `C2SEC-B02` — private-state exact scope/subset/public-projection closure;
- `C2SEC-B03` — secure-ingress assessment-bundle completeness/replay closure;
- `C2SEC-B04` — exact operation identity for operation-local credential leases.

No other C2.04 security semantics are intentionally changed. C3 retry/quota/cache/freshness, C4 PIT/revision/`available_from`, C5 evidence verification/source fitness/conflict, C6 capability/policy/trusted-intent authority, C7 orchestration/budgets/cancellation, C11 persistence implementation, and production provider adapters remain outside this repair.

The **effective C2.04R1 contract** is:

```text
pinned C2.04 parent contract
PLUS
this C2.04R1 scoped repair contract
```

Where this R1 contract explicitly replaces or closes a parent field/predicate, the R1 rule governs. Every other parent C2.04 rule remains inherited unchanged. No parent content-addressed artifact is rewritten.

No blocker is self-closed by construction. `C2SEC-B01..B04` are `ADDRESSED_NOT_CLOSED` until an independent C2.04R1 Security-Boundary Re-Check returns PASS.

## 2. Exact parent pins

```text
C2.04 parent normative contract      198d194fbb3814676f1cb74aec5d56f19f8b1f9b081c6d77c16b4e66fd762cda
C2.04 parent logical model           9d3609c775967fe374c1e1007828540d893852834bece09986148bf5a8aad5af
C2.04 parent acceptance delta        2a0b24c0f9d67a03c565f16e2985d0a5ecbaaff090c4715b2b7ea9b8491c0b8a
C2.04 parent decision ledger         719018dd73c1e80e9633d0468972e253dae4f77a3ffda75e1c0169c16c9aeac4
C2.04 candidate archive commit       8abaf5956b342780b85dc17fbb8ecf4142b12f8b
C2.04 independent review report      12aead5a1d4fc5eea0813cedbf360fd68616b432f34100db341367d96405fe21
C2.04 independent review result      4eb3daf2cecb0478731b814dd7749f06e990b5748f9301b8792c84dff9c22f78
C2.04 independent review archive     aa2a7b4c8c4c36cca66d6fa9cdf6f98d0866321d
```

The reviewed parent acceptance range is `C2-289..C2-348`: 58 PASS / 2 FAIL, with failed existing obligations `C2-313` and `C2-319`.

## 3. R1 stable-reference extensions

The parent `C2SecurityStableRef` identity shape remains unchanged:

```text
C2SecurityStableRef =
(authority = C2,
 ref_kind,
 logical_id,
 semantic_revision,
 content_sha256)
```

For C2.04R1, the closed C2.04 security ref-kind vocabulary is extended from the parent set to:

```text
CREDENTIAL_BINDING_PROFILE
PRIVATE_STATE_BINDING_PROFILE
SECURE_INGRESS_SEMANTIC_PROFILE
PRIVATE_STATE_SCOPE
PUBLIC_PROJECTION_RULE
```

The parent fail-closed stable-reference rules apply to the two new kinds:

- no floating `latest`/mutable alias is load-bearing;
- exact kind + logical ID + semantic revision + content hash must resolve;
- wrong-kind, dangling, unknown, hash-mismatched, or ambiguous refs fail closed;
- supersession creates a new ref; old exact refs remain replay-resolvable;
- these semantic objects contain no credential values and no private-state payload values.

C2.04 owns only the stable identity and comparison semantics of these refs. It does not acquire C6 authorization authority or the business-domain semantics of accounts, portfolios, theses, or other private-state domains.

## 4. C2SEC-B01 — closed redirect-forwarding semantics

### 4.1 Trusted redirect inputs

A redirect is untrusted transport data. Before any credential can follow a redirect, the target must resolve through trusted provider/destination metadata into the following exact comparison inputs:

```text
source_provider_profile_ref
source_endpoint_profile_ref
source_provider_capability_ref
source_destination_authority_ref

target_provider_profile_ref
target_endpoint_profile_ref
target_provider_capability_ref
target_destination_authority_ref
```

`destination_authority_ref` is an opaque trusted authority identity supplied by the trusted destination/egress authority boundary. C2.04 does not grant or redefine that authority; it only requires exact identity resolution and equality comparison.

A raw redirect URL, `Location` header, provider body, webpage text, SDK message, or model output cannot self-assert a trusted provider, endpoint, capability, or authority identity.

If any required source/target identity is unresolved, wrong-kind, ambiguous, or mismatched to the selected operation snapshot, the redirect decision is fail-closed `BLOCK`.

### 4.2 Closed `redirect_forwarding_semantics` vocabulary

The parent free-form/undefined field is replaced by the following closed enum:

```text
BLOCK_ALL_REDIRECTS
REBIND_ON_ANY_REDIRECT
FORWARD_SAME_AUTHORITY_SAME_ENDPOINT
```

Unknown values are invalid and make credential preparation `BLOCKED`.

Closed redirect decision vocabulary:

```text
FORWARD_EXISTING_LEASE
REBIND_REQUIRED
BLOCK
```

### 4.3 Exact redirect predicate

Let `M` be the pinned `redirect_forwarding_semantics` value on the exact `CredentialBindingProfile`.

Evaluate in the following order:

```text
1. If any required trusted identity cannot be resolved exactly:
       BLOCK

2. If target_provider_profile_ref != source_provider_profile_ref:
       BLOCK

3. If target_destination_authority_ref != source_destination_authority_ref:
       BLOCK

4. If target_provider_capability_ref != source_provider_capability_ref:
       BLOCK

5. If target_endpoint_profile_ref is not a member of the profile's
   allowed_endpoint_profile_refs:
       BLOCK

6. If M == BLOCK_ALL_REDIRECTS:
       BLOCK

7. If M == REBIND_ON_ANY_REDIRECT:
       REBIND_REQUIRED

8. Otherwise M == FORWARD_SAME_AUTHORITY_SAME_ENDPOINT:
       if target_endpoint_profile_ref == source_endpoint_profile_ref:
           FORWARD_EXISTING_LEASE
       else:
           REBIND_REQUIRED
```

No implementation-defined tie-break exists.

Consequences:

- cross-provider redirect: always `BLOCK`;
- cross-authority redirect: always `BLOCK` for the existing redirect attempt;
- same-provider/same-authority redirect to an unbound endpoint: `BLOCK`;
- same-provider/same-authority redirect to a different but allowed endpoint: `REBIND_REQUIRED` unless `BLOCK_ALL_REDIRECTS`, which is `BLOCK`;
- same-provider/same-authority redirect to the exact same endpoint may forward the existing lease only under `FORWARD_SAME_AUTHORITY_SAME_ENDPOINT`.

A higher-level trusted authority may create a **new** separately authorized provider operation for a cross-authority destination. That is not forwarding or reuse of the existing lease and is outside this redirect predicate.

### 4.4 Rebind requirements

`REBIND_REQUIRED` is non-dispatching for the old lease:

- existing credential material MUST NOT be forwarded to the target;
- a fresh `CredentialLease` descriptor must be issued for the target endpoint;
- the new lease must independently pass provider/endpoint/capability/private-state/security checks;
- the new lease uses a new `credential_lease_id`;
- HTTP/SDK automatic redirect behavior cannot bypass this predicate.

`FORWARD_EXISTING_LEASE` is permitted only while the exact operation/route-attempt identity in Section 5 remains unchanged.

## 5. C2SEC-B04 — exact operation identity for `CredentialLease`

### 5.1 Required descriptor fields

The parent `CredentialLease` public/auditable descriptor is extended to require:

```text
credential_lease_id
provider_operation_ref
route_attempt_ref
credential_handle_ref
credential_version_ref
credential_binding_profile_ref
provider_profile_ref
endpoint_profile_ref
provider_capability_ref
lease_decision
```

`provider_operation_ref` identifies one exact C2 provider operation request/instance.

`route_attempt_ref` identifies one exact C2.03 logical route-attempt lineage item for that provider operation.

They are trusted opaque identities for binding/audit. Possession of either ref grants no C6 capability, no network egress, and no PAPER/LIVE/write authority.

### 5.2 Exact lease-use predicate

A `READY` lease may expose credential material to an adapter only when all of the following presented-use fields exactly equal the issued descriptor:

```text
provider_operation_ref
route_attempt_ref
provider_profile_ref
endpoint_profile_ref
provider_capability_ref
credential_binding_profile_ref
credential_handle_ref
credential_version_ref
```

If any field differs, credential use is invalid, provider dispatch is prohibited, and the structured security block reason is:

```text
LEASE_OPERATION_IDENTITY_MISMATCH
```

The parent blocked-reason vocabulary is therefore extended by:

```text
LEASE_OPERATION_IDENTITY_MISMATCH
PUBLIC_PROJECTION_RULE_UNRESOLVED
PRIVATE_STATE_SCOPE_INVALID
SECURE_INGRESS_ASSESSMENT_INVALID
```

### 5.3 No cross-operation reuse

The same `credential_lease_id` MUST NOT be associated with two different `provider_operation_ref` values or two different `route_attempt_ref` values.

A new provider operation or a new route attempt requires a fresh lease ID even when credential handle/version, provider, endpoint, and capability are otherwise identical.

Rebinding after a redirect also requires a fresh lease ID. A same-authority/same-endpoint redirect may retain the existing lease only when Section 4 returns `FORWARD_EXISTING_LEASE` and the exact operation/route-attempt identity remains unchanged.

Historical replay retains the operation/attempt binding descriptor without retaining secret bytes.

## 6. C2SEC-B02 — machine-closed private-state least-scope

### 6.1 `PRIVATE_STATE_SCOPE` is an atomic stable scope ref

A `PRIVATE_STATE_SCOPE` object is a C2-owned stable semantic atom used only for exact authorization-set comparison.

Its load-bearing identity is its exact `C2SecurityStableRef`. C2.04 does not infer hierarchy, wildcard expansion, prefix implication, business-domain containment, or “broader/narrower” semantics between two scope refs.

Therefore:

```text
scope A authorizes scope B  <=>  exact stable ref A == exact stable ref B
```

No `*`, prefix match, human-readable label match, or implicit parent/child relationship is valid for subset evaluation.

### 6.2 Canonical scope-set construction

For any `declared_private_state_scope_refs[]` or operation-local `actual_private_state_scope_refs[]`:

1. resolve every element as an exact `PRIVATE_STATE_SCOPE` stable ref;
2. unresolved/wrong-kind/dangling/hash-mismatched/unknown refs make the set invalid;
3. if the same `logical_id` occurs with different revision/hash identities in one set, the set is invalid;
4. exact duplicate refs are deduplicated;
5. the canonical set is sorted lexicographically by the UTF-8 bytes of:
   `logical_id || 0x00 || semantic_revision || 0x00 || content_sha256`.

Canonical ordering therefore does not depend on input order.

### 6.3 Operation-local actual scope record

Every provider operation that supplies provider-bound private state has an operation-local:

```text
PrivateStateOperationScopeRecord:
  provider_operation_ref
  route_attempt_ref
  private_state_binding_profile_ref
  private_state_handle_ref
  actual_private_state_scope_refs[]
  scope_check_decision
```

Closed `scope_check_decision`:

```text
WITHIN_DECLARED_SCOPE
BLOCKED_SCOPE
```

The actual scope list is supplied only from trusted operation authorization/state. Provider/web/tool/model content cannot create or add an actual scope ref.

An empty canonical actual-scope set is valid when no private-state scope is supplied.

### 6.4 Exact subset predicate

Let `D` be the canonical declared set from the exact `PrivateStateBindingProfile`.

Let `A` be the canonical actual set from the exact operation-local scope record.

```text
WITHIN_DECLARED_SCOPE  <=>  both sets are valid AND every ref in A is exactly in D
BLOCKED_SCOPE          <=>  otherwise
```

`BLOCKED_SCOPE` prohibits private-state injection and provider dispatch for an operation requiring that private state.

This exact predicate repairs existing failed obligation `C2-313`.

### 6.5 Stable public-projection rule binding

The parent `PrivateStateBindingProfile.public_projection_rule` free-form field is replaced for R1 by:

```text
public_projection_rule_ref
```

It must resolve exactly to a `PUBLIC_PROJECTION_RULE` stable ref.

Closed rule payload:

```text
projection_mode:
  EXCLUDE_ALL_PRIVATE_STATE
  ALLOWLIST_METADATA_ONLY

allowed_metadata_fields[]   # required only for ALLOWLIST_METADATA_ONLY
```

Closed `allowed_metadata_fields` vocabulary:

```text
provider_profile_ref
endpoint_profile_ref
provider_capability_ref
private_state_scope_refs
scope_check_decision
public_projection_rule_ref
```

Rules:

- `EXCLUDE_ALL_PRIVATE_STATE` emits none of the provider-bound private-state handle/value material.
- `ALLOWLIST_METADATA_ONLY` may emit only the closed metadata fields named in the exact rule.
- Unknown metadata field IDs make the rule invalid.
- The rule can never allow `private_state_handle_ref`, account identifiers, portfolio contents, transaction/order contents, private thesis/research contents, credential handles/versions, secret-store locators, or secret material.
- unresolved/wrong-kind/hash-mismatched projection-rule refs fail closed with `PUBLIC_PROJECTION_RULE_UNRESOLVED`; private-state preparation is blocked because safe projection/audit behavior is not established.
- a raw/free-form `public_projection_rule` string is not load-bearing under R1.

## 7. C2SEC-B03 — closed secure-ingress assessment-bundle integrity

### 7.1 Runtime assessment identities

The R1 runtime/private reference vocabulary is extended with:

```text
secure_ingress_assessment_record_id
secure_ingress_axis_result_id
```

These are opaque non-bearer runtime/audit identities and MUST NOT be deterministically derived from pre-admission secret/private response bytes.

`ingress_event_id` remains the exact opaque identity of one untrusted ingress candidate. A redaction output receives a new `ingress_event_id`.

### 7.2 `SecureIngressAxisResult`

Each axis result has:

```text
secure_ingress_axis_result_id
assessment_axis
ingress_event_id
provider_operation_ref
secure_ingress_semantic_profile_ref
policy_ref
constraint
```

Closed `assessment_axis`:

```text
SECRET
PRIVACY
LICENSING
RETENTION
```

Closed `constraint` remains the parent vocabulary:

```text
ALLOW
REDACT_REQUIRED
EPHEMERAL_ONLY
QUARANTINE_REQUIRED
REJECT_REQUIRED
INDETERMINATE
```

The required policy mapping is exact:

```text
SECRET     -> security_policy_ref
PRIVACY    -> privacy_policy_ref
LICENSING  -> licensing_policy_ref
RETENTION  -> retention_policy_ref
```

An assessor that cannot determine an axis under an otherwise valid policy/profile must emit that axis once with `INDETERMINATE`; absence is not equivalent to indeterminate.

### 7.3 `SecureIngressAssessmentRecord`

A replayable load-bearing assessment record contains:

```text
secure_ingress_assessment_record_id
ingress_event_id
provider_operation_ref
secure_ingress_semantic_profile_ref

security_policy_ref
privacy_policy_ref
licensing_policy_ref
retention_policy_ref

axis_results[]              # exactly four, one per closed axis

bundle_validity
ingress_decision
retention_mode
```

Closed `bundle_validity`:

```text
VALID
INVALID_FAIL_CLOSED
```

Closed `retention_mode`:

```text
NONE
PERMITTED_RAW
EPHEMERAL_ONLY
```

Policy authority remains outside C2.04. For bundle integrity, each profile/policy ref must nevertheless be an exact immutable pinned ref whose trusted resolver reports `resolved=true`, `immutable=true`, and an exact content/version identity. C2.04 only verifies resolution and identity equality; C2.06 still owns the exact cross-contract wire binding.

### 7.4 Exact bundle-validity predicate

A `SecureIngressAssessmentRecord` is `VALID` if and only if all conditions hold:

1. `ingress_event_id` identifies exactly one ingress candidate.
2. `provider_operation_ref` identifies exactly one provider operation.
3. `secure_ingress_semantic_profile_ref` resolves exactly and immutably.
4. all four top-level policy refs resolve exactly and immutably through trusted resolvers.
5. `axis_results[]` contains exactly four elements.
6. each closed axis appears exactly once; no duplicate axis is permitted even if duplicate values agree.
7. every axis result has a unique `secure_ingress_axis_result_id`.
8. every axis result has the same `ingress_event_id` as the record.
9. every axis result has the same `provider_operation_ref` as the record.
10. every axis result has the same `secure_ingress_semantic_profile_ref` as the record.
11. every axis result's `policy_ref` exactly equals the corresponding top-level policy ref for its axis.
12. every axis result uses a closed constraint value.
13. no axis result is mixed from a different candidate, operation, profile, or policy snapshot.
14. the stored `ingress_decision` and `retention_mode` exactly equal the deterministic function in Sections 7.5–7.6.

Missing axes, duplicate axes, conflicting duplicates, unknown axes, unknown constraints, unresolved refs, mixed candidates, mixed operations, mixed profiles, mixed policy snapshots, or a stored-decision mismatch make the record `INVALID_FAIL_CLOSED`.

### 7.5 Invalid-bundle fail-closed result

Precedence is **not** applied to an invalid bundle.

For every `INVALID_FAIL_CLOSED` bundle:

```text
ingress_decision = QUARANTINE
retention_mode = NONE
permitted_raw_handoff = forbidden
ephemeral_admit = forbidden
C1_normalization = forbidden
```

The structured reason is `SECURE_INGRESS_ASSESSMENT_INVALID`.

This is a security quarantine, not `NO_DATA`, not C5 verification, and not C4 PIT state.

### 7.6 Valid-bundle deterministic decision

For a `VALID` bundle, use the parent precedence unchanged:

```text
if any REJECT_REQUIRED:
    ingress_decision = REJECT
    retention_mode = NONE

else if any QUARANTINE_REQUIRED or INDETERMINATE:
    ingress_decision = QUARANTINE
    retention_mode = NONE

else if any REDACT_REQUIRED:
    ingress_decision = REASSESS_REDACTED
    retention_mode = NONE

else:
    ingress_decision = ADMIT
    if any EPHEMERAL_ONLY:
        retention_mode = EPHEMERAL_ONLY
    else:
        retention_mode = PERMITTED_RAW
```

No implementation-defined tie-break exists.

This repairs existing failed obligation `C2-319` by making the four separate axes not only visible but exactly-one-per-axis, candidate/profile/policy coherent, and replay-bound.

### 7.7 Exact decision linkage

Every load-bearing `ingress_decision_ref` must resolve to exactly one `SecureIngressAssessmentRecord`.

A downstream admission check MUST NOT accept a bare decision enum detached from its assessment record.

If a supplied `ingress_decision`/`retention_mode` disagrees with recomputation from the exact record, the record is invalid and Section 7.5 applies.

### 7.8 Redaction requires a new complete bundle

A `REASSESS_REDACTED` transform creates:

- a new `ingress_event_id`;
- a new `secure_ingress_assessment_record_id`;
- four new axis-result IDs;
- a fresh complete assessment under the exact profile/policy refs selected for that new candidate.

Axis results or the assessment record from the pre-redaction candidate may be retained only as sanitized lineage. They cannot be load-bearing inputs for the redacted candidate's admission.

## 8. Closed interaction rules

The following are explicit non-regression rules:

1. Credential possession, operation identity, route-attempt identity, private-state scope, redirect identity, and ingress admission do not grant C6 capability or side-effect authority.
2. Credentials/private state do not create C2.03 route eligibility or reorder routes.
3. Redirect `BLOCK`/`REBIND_REQUIRED` does not define C3 retry or C7 orchestration policy.
4. Private-state scope refs are authorization-set atoms only; they do not redefine portfolio/account/thesis domain schemas.
5. Secure-ingress `ADMIT` is not C5 verification/source fitness.
6. Ingress timestamps/assessment records are not C4 `available_from` or PIT authority.
7. Invalid/quarantined/rejected ingress content cannot become C1 `NO_DATA`.
8. C11 persistence implementation and exact C2->C11 wire handoff remain deferred to C2.06 / `C2.OPEN-013`.
9. Repeated `REASSESS_REDACTED` remains non-admitted; C7 may bound orchestration, and any budget termination must never convert the state to ADMIT.
10. No secret-store/KMS/vendor/provider instance/production adapter is selected by R1.

## 9. R1 blocker disposition

```text
C2SEC-B01 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
C2SEC-B02 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
C2SEC-B03 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK
C2SEC-B04 = ADDRESSED_NOT_CLOSED_PENDING_INDEPENDENT_RECHECK

C2.OPEN-008 = NOT_CLOSED_REPAIR_CANDIDATE_PENDING_RECHECK
C2.OPEN-009..012 = OPEN_UNCHANGED
C2.OPEN-013 = OPEN_UNCHANGED_C2_06_PERMITTED_RAW_HANDOFF
C2.OPEN-014..015 = OPEN_UNCHANGED
```

## 10. Exit gate

C2.04R1 construction may only advance to:

```text
C2.04R1 Independent Security-Boundary Re-Check
```

The re-check must adversarially verify B01–B04, re-check existing failed obligations `C2-313` and `C2-319`, verify the new R1 acceptance additions, and verify non-regression of the other C2.04 PASS surface.

C2.05 remains `NOT_AUTHORIZED`.

Production implementation remains `NOT_AUTHORIZED`.

External / PAPER / LIVE side effects remain `NOT_AUTHORIZED`.
