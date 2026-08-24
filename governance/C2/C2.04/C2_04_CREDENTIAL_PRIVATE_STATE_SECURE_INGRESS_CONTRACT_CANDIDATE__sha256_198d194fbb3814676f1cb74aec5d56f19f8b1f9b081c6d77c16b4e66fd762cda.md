# C2.04 — Credentials / Private-State / Secure Ingress Boundary Candidate

Generated: 2026-08-24T13:55:00Z

Status: `CANDIDATE_FOR_C2_04_INDEPENDENT_SECURITY_BOUNDARY_REVIEW`

Production implementation: `NOT_AUTHORIZED`

External/PAPER/LIVE side effects: `NOT_AUTHORIZED`

## 1. Purpose and Authority

C2.04 defines the semantic security boundary for supplying provider credentials and provider-bound private state to C2 provider operations, and for admitting external provider response material into downstream processing or the permitted-raw persistence handoff.

C2.04 is a contract construction stage only. It does **not** choose a secret-store product, KMS, vault, OAuth library, HTTP client, encryption algorithm, database, provider vendor, production adapter, or broker execution path.

The stage is governed by:

- frozen C0 security and secure-raw invariants, especially C0-041, C0-042, C0-049, C0-050, C0-056, C0-057 and C0-058;
- frozen C1 / C1.05R1 provider-normalization boundary;
- reviewed C2.01 capability/endpoint semantics;
- reviewed C2.02 operation/data-outcome semantics;
- reviewed C2.03 routing semantics;
- the user-adopted C2 stage workflow.

C2.04 may define C2-owned provider-security semantic profiles and boundary records. It MUST NOT grant C6 capability, define C7 orchestration, define C3 retry/quota/cache/freshness, define C4 PIT/available_from, define C5 source fitness/verification, or choose C11 persistence implementation.

## 2. Parent Authority Pins

```yaml
c0_frozen: 9585df6c0fbdb2cc40bc38571f8452b51f8ca69c9fd9432b10b87490b08a3b6f
c0_acceptance: 8d5d7f45bd79cd3617968b6ebfbe1d0ddeb1956b7cf80cfcb285ebc4317de27c
c1_freeze_seal: 438274542570f7398af8622fdb511b85d69fc4c403b246b93a8a593b5d8070a5
c1_provider_normalization_interface: 71d472e63044b9a7be2c6cc831705ed80dc6a06ccd0ef03e71a0618794bdef63
c2_00_scope: b504211651839b1cd9c79a9706f05e1ad9c072f66bfb887aec2a0d65c9b17cf7
c2_01r1_registry_model: 0bcdd0c48d8cd614ee7a1cb6ee6519df8fb33731bcafd535f3313978dca4343a
c2_02r2_contract: 901445ca8f0f3f1a8cd04331d3def83f4a29ae3984e5917e723e2402f858f57d
c2_03r2_contract: e04158428fc030ca72d297b2cb3fd4226dccaba0aa35224b14fc4de89e039b6b
c2_03r2_recheck_result: f8db42b0dce59cb021dfa12f5913fb3f79918808d73f5fbc853656a8b7633d43
workflow_plan: b7a4f2a3958417f155e24109edaf025c017d7fc8ac7980ff9765c90fe97e70d6
```

No parent artifact is modified.

## 3. Non-Negotiable Security Principles

1. **Credential material is data-plane secret material, never public contract state.**
2. **Possession of a credential does not grant execution capability.**
3. **Credential references and credential material are different objects.**
4. **Credential material MUST NOT be committed, rendered, logged, traced, hashed into public identifiers, embedded in error text, or copied into public examples.**
5. **Provider-native content cannot supply, replace, expand, redirect, or retarget trusted credential/private-state authority.**
6. **Provider credentials are bound to declared C2 provider/endpoint/capability semantics and cannot be forwarded to an unrelated provider or unbound redirect target.**
7. **Private state is least-scope and must remain subordinate to trusted upstream authorization.**
8. **External response bytes are untrusted before secure ingress.**
9. **Permitted raw immutability begins only after secure-ingress admission.**
10. **A redaction transform does not create automatic trust; the transformed candidate must be re-assessed.**
11. **Quarantined/rejected content is not a Permitted RawArtifact and cannot enter C1 normalization.**
12. **Ingress licensing/privacy/retention state does not become C5 verification or C4 PIT state.**
13. **Replay/audit retains semantic binding and sanitized lineage, not historical secret bytes.**

## 4. Security Reference Domains

### 4.1 C2.04 stable semantic references

Load-bearing C2.04 semantic profiles use the same stable identity shape established by C2.01R1:

```text
C2SecurityStableRef =
(authority = C2,
 ref_kind,
 logical_id,
 semantic_revision,
 content_sha256)
```

Closed C2.04 ref kinds:

```text
CREDENTIAL_BINDING_PROFILE
PRIVATE_STATE_BINDING_PROFILE
SECURE_INGRESS_SEMANTIC_PROFILE
```

Rules:

- no floating `latest` alias may be load-bearing;
- exact kind + logical ID + semantic revision + content hash must resolve;
- wrong-kind, dangling or hash-mismatched references fail closed;
- supersession creates a new ref; old refs remain resolvable for audit.

These profiles MUST NOT contain credential values or private-state payloads.

### 4.2 Runtime/private references

The following are **not** content-addressed semantic definitions:

```text
credential_handle_ref
credential_version_ref
private_state_handle_ref
credential_lease_id
ingress_event_id
quarantine_ref
```

They are opaque runtime/private audit references.

A runtime/private ref:

- MUST NOT itself be provider-usable bearer/authentication material;
- MUST NOT be deterministically derived from secret bytes;
- MAY be non-public even when non-secret;
- MUST NOT be treated as C6 capability or side-effect authorization;
- need not permit future re-authentication during historical replay.

Semantic replay requires the binding/profile/version identity used, but **does not require retaining the secret bytes**.

## 5. Provider Credential Binding

### 5.1 `CredentialBindingProfile`

A C2-owned `CredentialBindingProfile` declares how one credential class may be injected for a declared C2 provider boundary.

Required semantic fields:

```text
credential_binding_profile_ref
provider_profile_ref
allowed_endpoint_profile_refs[]
allowed_capability_refs[]
credential_class
injection_channel
secret_selector
redirect_forwarding_semantics
request_capture_redaction_required
response_echo_scan_required
```

Closed `credential_class` vocabulary:

```text
API_KEY
ACCESS_TOKEN
SESSION_SECRET
CLIENT_KEY_MATERIAL
OPAQUE_PROVIDER_SECRET
```

Closed `injection_channel` vocabulary:

```text
AUTHORIZATION_HEADER
OTHER_HEADER
QUERY_PARAMETER
REQUEST_BODY_FIELD
COOKIE
MUTUAL_TLS_PRIVATE_CHANNEL
SDK_PRIVATE_CHANNEL
```

`secret_selector` describes the semantic injection location (for example a header/field name) but MUST NOT contain a secret value.

A profile may bind to one or more C2.01 endpoint/capability refs. If a provider operation's exact endpoint/capability is outside the allowed set, credential injection is forbidden.

### 5.2 No capability grant

A valid credential and a valid `CredentialBindingProfile` mean only:

> "this secret material is semantically eligible to authenticate this provider operation if some trusted authority separately permits the operation."

They do **not** mean:

- the C6 capability exists;
- network egress is allowed;
- the user authorized a private-data disclosure;
- PAPER/LIVE/trading is allowed;
- a route candidate becomes eligible despite C2.01/C2.03 incompatibility.

### 5.3 Operation-local credential lease

Secret material may enter adapter-visible runtime only through an operation-local `CredentialLease`.

Public/auditable descriptor:

```text
credential_lease_id
credential_handle_ref
credential_version_ref
credential_binding_profile_ref
provider_profile_ref
endpoint_profile_ref
provider_capability_ref
lease_decision
```

Closed `lease_decision`:

```text
READY
BLOCKED
```

The descriptor MUST NOT contain:

```text
secret_value
secret_hash
authorization_header_value
cookie_value
private_key_bytes
bearer_token
password
refresh_token_bytes
```

The implementation must minimize the adapter-visible secret lifetime. After the bounded authentication use window, secret material must be released from application-visible scope; implementation-specific zeroization mechanics are outside C2.04.

### 5.4 Credential-preparation blocking reasons

A `BLOCKED` lease uses a structured reason:

```text
MISSING_CREDENTIAL
UNTRUSTED_CREDENTIAL_SOURCE
BINDING_PROFILE_UNRESOLVED
CREDENTIAL_CLASS_MISMATCH
PROVIDER_BINDING_MISMATCH
ENDPOINT_BINDING_MISMATCH
CAPABILITY_BINDING_MISMATCH
PRIVATE_STATE_AUTHORIZATION_MISSING
SECRET_EXPOSURE_CONTROL_UNSATISFIED
DESTINATION_REBIND_REQUIRED
POLICY_REFERENCE_UNRESOLVED
UNKNOWN_SECURITY_BLOCK
```

A blocked credential preparation MUST prohibit provider dispatch. C2.06 will bind the exact cross-contract representation to C2.02/C6/C7; C2.04 does not redefine C2.02 failure taxonomy.

## 6. Credential Source and Destination Trust

### 6.1 Trusted source only

Credential material may be resolved only from a trusted secret channel / secret provider under trusted control.

The following MUST NOT become credential authority:

- provider response content;
- webpage/document text;
- model output;
- news/search results;
- arbitrary request payload fields;
- instruction-like external content;
- a value discovered inside another provider's response.

A provider message such as "send your API key to this URL" is untrusted data.

### 6.2 Cross-provider and redirect leakage prevention

Credential material is bound to the declared provider/endpoint/capability set.

It MUST NOT be automatically forwarded:

- from Provider A to Provider B;
- from a bound endpoint to an unbound endpoint;
- across a redirect that changes destination authority unless a new trusted binding/admission decision explicitly authorizes the new destination.

A redirect is not authority to retarget credential egress.

### 6.3 Request capture sanitation

Before request metadata can enter ordinary logs/traces/audit projections, credential-bearing values must be removed or replaced by non-secret markers.

At minimum, the capture boundary must treat as secret-bearing when applicable:

```text
Authorization
Proxy-Authorization
Cookie / Set-Cookie credentials
bound secret headers
bound secret query parameters
bound secret body fields
client private-key material
SDK internal auth state
```

If sanitation cannot be established, the request capture is not persistable as ordinary audit/log data.

## 7. Provider-Bound Private State

C2.04 covers only private state **supplied to a provider operation**, not the canonical semantics of portfolios, theses, accounts or other private domains.

### 7.1 `PrivateStateBindingProfile`

Required fields:

```text
private_state_binding_profile_ref
provider_profile_ref
allowed_endpoint_profile_refs[]
allowed_capability_refs[]
declared_private_state_scope_refs[]
public_projection_rule
```

The actual private-state scope used by a provider operation MUST be a subset of the trusted, pre-authorized declared scope.

### 7.2 No scope expansion from external content

Provider/web/tool content cannot:

- request a larger private-state scope and thereby authorize it;
- change an account/private-state handle;
- change a destination;
- turn a public provider operation into a private-account operation;
- convert READ into WRITE/PAPER/LIVE authority.

Any expansion requires a new trusted upstream authorization outside untrusted content.

### 7.3 Public projection

Private-state values and private handles are excluded/redacted from public artifacts by default.

Public artifacts MAY retain synthetic/non-sensitive identifiers and policy-safe metadata, but they MUST NOT reveal account identifiers, private portfolio contents, private thesis material, credentials, or secret-store locators when those are classified private.

## 8. Secure External-Response Ingress

### 8.1 Boundary position

```text
Provider External Response
        |
        v
Ephemeral Untrusted Response Candidate
        |
        v
Secure Ingress Assessment
  - secret/credential leakage
  - privacy/private-data policy
  - licensing/redistribution policy
  - retention policy
        |
        +--> REASSESS_REDACTED
        +--> QUARANTINE
        +--> REJECT
        |
        v
       ADMIT
   /           \
PERMITTED_RAW   EPHEMERAL_ONLY
```

No response is a `Permitted RawArtifact` before final `ADMIT + PERMITTED_RAW`.

### 8.2 Trusted policy inputs

C2.04 defines the decision semantics, not the legal/security policy authority or detection thresholds.

The assessment consumes pinned trusted policy references such as:

```text
security_policy_ref
privacy_policy_ref
licensing_policy_ref
retention_policy_ref
```

These refs cannot be supplied or modified by the provider payload.

Exact C2↔C6/other policy-owner wire bindings are deferred to C2.06.

### 8.3 Normalized ingress constraints

Each assessment axis returns one normalized constraint:

```text
ALLOW
REDACT_REQUIRED
EPHEMERAL_ONLY
QUARANTINE_REQUIRED
REJECT_REQUIRED
INDETERMINATE
```

The axes remain explicit:

```text
secret_constraint
privacy_constraint
licensing_constraint
retention_constraint
```

An `INDETERMINATE` axis is fail-closed and cannot result in direct admission.

### 8.4 Deterministic decision precedence

For a complete trusted assessment bundle:

```text
if any REJECT_REQUIRED:
    decision = REJECT

else if any QUARANTINE_REQUIRED or INDETERMINATE:
    decision = QUARANTINE

else if any REDACT_REQUIRED:
    decision = REASSESS_REDACTED

else:
    decision = ADMIT
    if any EPHEMERAL_ONLY:
        retention_mode = EPHEMERAL_ONLY
    else:
        retention_mode = PERMITTED_RAW
```

There is no implementation-defined tie-break.

### 8.5 Redaction is not trust

`REASSESS_REDACTED` is non-terminal.

A redaction transform creates a **new ingress candidate**. The redacted output must pass the complete secure-ingress assessment again before it can become `ADMIT`.

`RedactionTransformationRecord` may contain:

```text
input_ingress_event_id
redaction_rule_refs[]
transform_version_ref
output_ingress_event_id
```

It MUST NOT contain the removed secret/private plaintext or a secret-derived public fingerprint.

### 8.6 `ADMIT + PERMITTED_RAW`

This decision permits a C2→C11 permitted-raw handoff candidate.

The handoff semantics must include an identity of the **admitted bytes**, e.g.:

```text
provider_operation_ref
ingress_decision_ref
admitted_content_sha256
byte_length
media_type
content_form = UNMODIFIED | REDACTED
```

The `admitted_content_sha256` is computed from the exact admitted bytes, never from forbidden pre-redaction secret-bearing bytes merely for public/audit convenience.

C11 owns storage implementation. C2.06 owns the exact opaque handoff interface.

Once C11 persists an admitted `Permitted RawArtifact`, mutation requires a new content identity; in-place overwrite under the old content identity is forbidden by C0-050.

### 8.7 `ADMIT + EPHEMERAL_ONLY`

`EPHEMERAL_ONLY` means:

- downstream processing may occur only if the trusted ingress policy allows it;
- the original/admitted response bytes MUST NOT become a `Permitted RawArtifact`;
- no persisted `raw_payload_ref` may falsely point to those bytes;
- transient memory/buffer implementation is not C2.04 semantics.

Validated observations may still be emitted if all other C2/C1 boundaries are satisfied and policy permits ephemeral processing. The absence of a persisted raw artifact must remain explicit in lineage.

### 8.8 `QUARANTINE`

Quarantined content:

- is not a `Permitted RawArtifact`;
- MUST NOT enter C1 normalization;
- MUST NOT become ordinary downstream evidence;
- MAY be retained only in a restricted quarantine mechanism under trusted policy;
- uses an opaque `quarantine_ref` if an audit pointer is required;
- MUST NOT expose quarantined secret/private payload in public artifacts.

Exact quarantine storage is outside C2.04.

### 8.9 `REJECT`

Rejected content:

- is not admitted for downstream normalization;
- is not a `Permitted RawArtifact`;
- must not be silently converted to `NO_DATA`;
- may retain only sanitized audit metadata allowed by policy.

## 9. Sanitized Failure and Diagnostic Boundary

C2.02 owns provider failure semantics. C2.04 adds a security constraint:

> Any diagnostic text, headers, request locator, response excerpt, SDK exception or provider-native error material crossing into an ordinary C2.02 failure/audit record MUST first be sanitized so it cannot expose credential/private-state material.

Therefore:

- a 401 response body echoing a token cannot be copied verbatim into `diagnostic_summary`;
- a URL containing an API key must be rendered with the secret value removed;
- `Set-Cookie` / session material cannot be copied into public error logs;
- a sanitation failure is a security block, not a reason to persist the unsafe error body.

Sanitization does not change the underlying C2.02 status/data-outcome classification.

## 10. Replay and Audit Without Secret Retention

Historical audit/reconstruction should be able to answer:

- which C2 credential binding profile applied;
- which opaque credential version/handle identity was used, when policy permits retention of that metadata;
- which provider/endpoint/capability the credential was bound to;
- whether credential preparation was READY or BLOCKED;
- which ingress profile/policy refs were used;
- which ingress decision occurred;
- whether admitted bytes were unmodified/redacted/ephemeral-only;
- which admitted content hash was handed toward C11 where permitted.

Historical audit MUST NOT require or retain the historical secret bytes.

A secret value is not a replay artifact.

## 11. Cross-Contract Ownership

### C1

C1 receives only validated provider observations through the frozen C1.05R1 seam.

- raw provider payload never bypasses C2 validation;
- `raw_payload_ref`, when present, must not resolve to rejected/quarantined/ephemeral-only bytes;
- `FAILED` / `CANCELLED` remains C1 normalization `NOT_RUN`;
- C2.04 does not redefine C1 canonical identity.

### C2.01

C2.04 binds credentials/private-state use to reviewed provider/endpoint/capability semantic refs. It does not modify capability compatibility.

### C2.02

C2.04 does not redefine `SUCCESS | FAILED | CANCELLED` or `PRESENT | NO_DATA | PARTIAL`. Security blocking before dispatch and sanitized failure representation are bound exactly in C2.06/C2.07.

### C2.03

Credentials/private state do not create route eligibility and do not reorder routes. A route still must satisfy C2.01/C2.03 semantics independently.

### C3

C2.04 does not own retry, quota, cache, freshness, coalescing or LKG.

Credential refresh/reauth timing, if it consumes retry/quota/budget, must not be silently invented as C2.04 retry policy.

### C4

Ingress timestamps or credential validity metadata do not define financial `available_from`, revision or PIT safety.

### C5

Secure-ingress admission does not mean the source is fit, true, corroborated, or `VERIFIED`.

### C6

C6 retains capability, trusted-intent, destination/egress and policy authority. Credentials are resources, not capability grants.

Exact foreign-ref wire binding is C2.06 work.

### C7

C7 retains orchestration, budgets, cancellation and durable task semantics.

### C11

C11 owns persistence implementation. C2.04 defines only the semantic eligibility boundary for a permitted-raw handoff.

The exact C2→C11 wire/repository handoff remains `C2.OPEN-013` for C2.06.

### C12

C12 retains validation/promotion/release authority. C2.04 cannot self-freeze or self-release.

## 12. Security Red Lines

The following are invalid:

```text
real secret -> git/public report/example
secret value -> public hash/fingerprint
secret value -> error string/log/trace
credential possession -> C6 capability grant
credential binding -> PAPER/LIVE authorization
Provider A credential -> Provider B
cross-authority redirect -> automatic secret forwarding
provider content -> credential source
provider content -> private-state scope expansion
provider content -> security/privacy/license/retention policy ref
raw external response -> immutable Permitted RawArtifact before ingress decision
secret-bearing response -> public raw hash merely for audit convenience
redaction -> admission without full re-assessment
QUARANTINE -> C1 normalization
REJECT -> NO_DATA
EPHEMERAL_ONLY -> persisted raw_payload_ref
secure-ingress ADMIT -> C5 VERIFIED
secure-ingress retrieved_at -> C4 available_from
public artifact -> private account/portfolio/thesis/credential content
C2.04 -> secret-store/KMS/database implementation choice
C2.04 -> production provider adapter
C2.04 -> side-effect authorization
```

## 13. Candidate Open-Question Disposition

```text
C2.OPEN-008 =
CANDIDATE_CLOSED_PENDING_INDEPENDENT_SECURITY_BOUNDARY_REVIEW

C2.OPEN-009..012 =
OPEN_UNCHANGED

C2.OPEN-013 =
OPEN_UNCHANGED
(target C2.06 exact C2->C11 permitted-raw handoff)

C2.OPEN-014..015 =
OPEN_UNCHANGED
```

No OPEN item is represented as final authority before independent review.

## 14. Exit Gate

C2.04 remains a candidate.

Required next gate:

```text
C2.04 Independent Security-Boundary Review
```

The review must adversarially test at least:

- secret/public-boundary leakage;
- secret-derived fingerprint leakage;
- cross-provider and redirect credential forwarding;
- credential-as-capability confusion;
- private-state scope expansion;
- deterministic ingress constraint precedence;
- indeterminate ingress fail-closed behavior;
- redaction/reassessment recursion;
- ephemeral-only versus permitted-raw separation;
- quarantine/reject downstream isolation;
- sanitized C2.02 diagnostic boundary;
- C1 raw-payload lineage constraints;
- C2/C6/C11 ownership boundaries;
- replay without secret retention.

C2.05 MUST NOT begin before an independent PASS or an explicitly scoped repair/re-check sequence.
