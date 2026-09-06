# C2.04 Independent Security-Boundary Review Report

Generated: 2026-08-24T15:52:00Z

Stage: `C2.04 — Credentials / Private-State / Secure Ingress Boundary`

Review type: `INDEPENDENT_SECURITY_BOUNDARY_REVIEW`

Candidate state entering review: `CONSTRUCTED_CANDIDATE_NOT_FROZEN`

## 1. Verdict

**FAIL — C2.04R1 scoped repair required.**

The candidate has a strong security architecture and correctly preserves the major C0/C1/C2.01/C2.02/C2.03 ownership boundaries, but four load-bearing semantic gaps remain. Two gaps cause existing C2.04 acceptance obligations to fail; two additional gaps are not adequately covered by the current acceptance catalog and therefore require new R1 adversarial obligations.

No C2.05 authorization is granted.

## 2. Candidate Pins Reviewed

- normative contract: `198d194fbb3814676f1cb74aec5d56f19f8b1f9b081c6d77c16b4e66fd762cda`
- logical model: `9d3609c775967fe374c1e1007828540d893852834bece09986148bf5a8aad5af`
- acceptance delta: `2a0b24c0f9d67a03c565f16e2985d0a5ecbaaff090c4715b2b7ea9b8491c0b8a`
- decision ledger: `719018dd73c1e80e9633d0468972e253dae4f77a3ffda75e1c0169c16c9aeac4`
- construction validation: `6a6c45ae2d9785a81f130b5142361d125ad40cb499962517d320f379200b176c`
- stage report: `afd19deeaeafd98ae9e10fa0c6ba953e4c8a2008dcc5652cab3c054f7619a55f`

The construction mechanical PASS was not treated as independent review evidence.

## 3. Review Method

The review re-derived the candidate security semantics from the exact candidate artifacts and attacked:

1. credential/public-boundary leakage;
2. secret-derived identifiers/fingerprints;
3. credential-as-capability confusion;
4. credential binding to provider/endpoint/capability;
5. redirect and cross-provider credential forwarding;
6. operation-local credential lease semantics;
7. private-state least-scope and retargeting;
8. public projection of private state;
9. secure-ingress assessment completeness and policy provenance;
10. deterministic precedence across secret/privacy/licensing/retention axes;
11. indeterminate fail-closed handling;
12. redaction followed by full re-assessment;
13. permitted-raw versus ephemeral-only separation;
14. quarantine/reject isolation;
15. sanitized C2.02 diagnostic boundary;
16. C1 raw-payload lineage restrictions;
17. C4/C5 non-inference;
18. C6/C7/C11 authority boundaries;
19. replay without historical secret bytes;
20. deterministic behavior under adversarial same-input cases.

## 4. Acceptance Review Summary

Acceptance range reviewed: `C2-289..C2-348` = 60 obligations.

- PASS: 58
- FAIL: 2
- Existing failed obligations: `C2-313`, `C2-319`

The fact that 58/60 existing obligations pass does not make the stage pass because two additional blocker classes are not adequately represented by the current acceptance catalog.

## 5. Blocking Findings

### C2SEC-B01 — `redirect_forwarding_semantics` is required but semantically undefined

**Status:** OPEN / BLOCKING

`CredentialBindingProfile` requires:

```text
redirect_forwarding_semantics
```

but the candidate does not define a closed vocabulary, exact predicate, or deterministic effect for this field.

The high-level red lines correctly forbid:
- Provider A credential → Provider B;
- unbound endpoint credential forwarding;
- automatic forwarding across a destination-authority-changing redirect without trusted rebind/admission.

However, the contract does not determine behavior for same-provider / same-authority redirect cases where:
- the original endpoint is allowed;
- the redirect target may or may not resolve to another allowed endpoint profile;
- the credential profile contains more than one allowed endpoint;
- `redirect_forwarding_semantics` is present but has no defined values or precedence.

Two conforming implementations can therefore receive the same pinned credential profile and redirect target and choose different actions: forward, block, or require rebind.

This is a C2.04 semantic gap, not a C2.07 encoding problem. C2.07 can encode only a previously frozen redirect predicate.

**Required R1 repair:**
- define a closed `redirect_forwarding_semantics` vocabulary;
- define exact destination-authority / endpoint-profile applicability;
- define whether same-authority redirects are ever forwardable;
- require deterministic rebind behavior for any target not positively admitted;
- add same-input adversarial vectors for same-authority and cross-authority redirects.

**Current acceptance coverage:** insufficient. `C2-305` covers cross-authority leakage but does not close same-authority/bound-endpoint redirect determinism.

---

### C2SEC-B02 — Private-state least-scope is asserted but not machine-closed

**Status:** OPEN / BLOCKING

`PrivateStateBindingProfile` contains:

```text
declared_private_state_scope_refs[]
public_projection_rule
```

and the normative text says:

> actual provider-bound private-state scope MUST be a subset of the trusted, pre-authorized declared scope.

But the candidate does not define:
- the stable/ref domain for `declared_private_state_scope_refs[]`;
- the exact operation-local representation of the actual requested/supplied private-state scope;
- canonical set construction/deduplication;
- the exact subset predicate;
- malformed/unknown scope behavior;
- a closed or externally pinned semantic meaning for `public_projection_rule`.

Consequently, two implementations can agree on the same `PrivateStateBindingProfile` yet disagree over whether an actual private-state request is within scope.

This prevents C2.04 from proving its own least-scope claim.

**Existing failed obligation:** `C2-313` — Private state scope subset enforced.

**Required R1 repair:**
- define exact scope-ref identity/ownership;
- define operation-local `actual_private_state_scope_refs[]` or equivalent;
- define canonical set equality/subset semantics;
- fail closed for unresolved/wrong-kind/unknown scope refs;
- bind `public_projection_rule` to a closed C2.04 rule or an exact stable foreign policy ref without allowing provider content to supply it.

---

### C2SEC-B03 — Secure-ingress decision formula lacks a closed assessment-bundle integrity contract

**Status:** OPEN / BLOCKING

The candidate defines the four axes and a good deterministic precedence formula:

```text
secret_constraint
privacy_constraint
licensing_constraint
retention_constraint
```

but applies it only:

> "For a complete trusted assessment bundle"

without defining a normative assessment record or exact completeness predicate.

The candidate does not fully freeze:
- exactly one value for each of the four axes;
- same-ingress-candidate binding for all four axis results;
- exact `SECURE_INGRESS_SEMANTIC_PROFILE` identity used;
- exact pinned security/privacy/licensing/retention policy refs used for that assessment;
- behavior for a missing axis;
- behavior for duplicate/conflicting axis results;
- behavior for unresolved/mismatched policy refs;
- prohibition on mixing axis results from different ingress candidates or policy snapshots.

The precedence function is deterministic **after** a valid bundle exists, but the load-bearing input bundle is not yet deterministic.

A malicious or buggy implementation could mix three permissive axis results from one candidate/policy snapshot with a fourth result from another and still feed the precedence function.

**Existing failed obligation:** `C2-319` — Ingress axes retained separately.

The candidate states that the axes remain explicit, but it does not define the replayable record that proves which exact four axis results and policy refs formed one decision.

**Required R1 repair:**
- define `SecureIngressAssessmentRecord` (or equivalent);
- bind it to one exact `ingress_event_id` / candidate identity;
- require exactly one result for each of the four axes;
- retain exact profile/policy refs used;
- define missing/duplicate/wrong-candidate/wrong-policy bundle handling as fail closed;
- define exact decision-record linkage to the assessment record.

---

### C2SEC-B04 — "Operation-local" credential lease is not explicitly bound to an operation identity

**Status:** OPEN / BLOCKING

The public/auditable `CredentialLease` descriptor includes:

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

but no exact `provider_operation_ref`, route-attempt ref, or equivalent trusted operation identity.

The prose requires operation-local lifetime, but the logical descriptor cannot prove that a READY lease was issued for one exact operation rather than reused across two otherwise similar operations against the same provider/endpoint/capability.

This weakens:
- replay;
- audit;
- operation-locality;
- safe reuse prevention;
- future C2.06 binding to C6/C7 authority.

This is not a requirement to retain secret bytes. It is a requirement to retain the non-secret identity of the operation for which the lease was authorized.

**Required R1 repair:**
- bind every lease descriptor to one exact provider operation / route-attempt identity;
- define lease reuse across a different operation identity as invalid;
- preserve the rule that the operation ref grants no capability by itself;
- add adversarial tests for lease reuse across two operations with identical provider/endpoint/capability semantics.

**Current acceptance coverage:** insufficient. `C2-311` tests bounded secret lifetime but does not test operation-identity binding/reuse.

## 6. Existing Acceptance Results

### Failed

- `C2-313` — FAIL: the contract states subset enforcement but does not define a deterministic actual-scope/ref/subset model.
- `C2-319` — FAIL: four axes are named, but no closed replayable assessment-bundle record binds exactly one value per axis to one candidate and one pinned policy set.

### Passed

All other existing obligations in `C2-289..C2-348` pass at their stated contract scope, including:
- no real/public credential leakage;
- no secret-derived public fingerprints;
- credential != capability;
- provider/endpoint/capability mismatch blocks;
- untrusted credential sources block;
- cross-provider and cross-authority redirect leakage prohibition;
- request-capture sanitation;
- private-state external-content expansion prohibition;
- ingress-before-permitted-raw;
- deterministic precedence for a valid complete bundle;
- INDETERMINATE → QUARANTINE;
- redaction → full re-assessment;
- exact-admitted-byte hashing;
- EPHEMERAL_ONLY raw-persistence prohibition;
- quarantine/reject isolation;
- sanitized diagnostics;
- no C4/C5 semantic collapse;
- no vendor/secret-store selection;
- C2.OPEN-013 remains deferred to C2.06.

## 7. Non-Blocking Notes

1. **Redaction no-progress/cycle behavior:** repeated `REASSESS_REDACTED` can require orchestration/budget handling. This is not treated as a C2.04 confidentiality blocker because every intermediate state remains non-admitted and C7 owns orchestration/budgets/cancellation. C2.07 should nevertheless include a fail-closed invariant that a non-terminal redaction cycle cannot become ADMIT merely because a budget ends.
2. **C2.06 wire binding:** exact C2↔C6 policy refs, C2↔C7 operation/lease linkage, C2↔C11 permitted-raw/quarantine handoff, and the frozen C1 OutcomeAxes seam remain mandatory.
3. **C2.07 validator:** must encode the repaired closed domains and fail-closed ref resolution rather than inventing new security semantics.

## 8. Open-Question Disposition After Review

```text
C2.OPEN-008 =
NOT_CLOSED
REPAIR_REQUIRED

C2.OPEN-009..012 =
OPEN_UNCHANGED

C2.OPEN-013 =
OPEN_UNCHANGED_C2_06_PERMITTED_RAW_HANDOFF

C2.OPEN-014..015 =
OPEN_UNCHANGED
```

## 9. Required Next Gate

```text
C2.04R1 scoped repair
→ C2.04R1 Independent Security-Boundary Re-Check
```

R1 scope must be limited to:
1. redirect-forwarding semantic closure;
2. private-state exact scope/subset/public-projection semantics;
3. secure-ingress assessment-bundle completeness and replay binding;
4. operation-local credential-lease operation identity;
5. corresponding acceptance additions/re-checks.

C2.05 remains NOT AUTHORIZED.
Production implementation remains NOT AUTHORIZED.
External/PAPER/LIVE side effects remain NOT AUTHORIZED.
