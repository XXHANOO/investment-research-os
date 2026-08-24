# C2.04 Independent Security-Boundary Review Report

Generated: 2026-08-24T15:58:00Z
Stage: `C2.04 — Credentials / Private-State / Secure Ingress Boundary`
Review type: `INDEPENDENT_SECURITY_BOUNDARY_REVIEW`
Entering state: `CONSTRUCTED_CANDIDATE_NOT_FROZEN`

## Verdict

**FAIL — C2.04R1 scoped repair required.**

Candidate pins reviewed:
- contract `198d194fbb3814676f1cb74aec5d56f19f8b1f9b081c6d77c16b4e66fd762cda`
- model `9d3609c775967fe374c1e1007828540d893852834bece09986148bf5a8aad5af`
- acceptance `2a0b24c0f9d67a03c565f16e2985d0a5ecbaaff090c4715b2b7ea9b8491c0b8a`
- ledger `719018dd73c1e80e9633d0468972e253dae4f77a3ffda75e1c0169c16c9aeac4`

Construction mechanical validation was not treated as independent evidence.

Acceptance range `C2-289..C2-348`: **58 PASS / 2 FAIL**.
Failed existing obligations: `C2-313`, `C2-319`.

## Blocking findings

### C2SEC-B01 — redirect forwarding semantics not closed

`CredentialBindingProfile` requires `redirect_forwarding_semantics`, but the candidate gives it no closed vocabulary or exact predicate. Cross-provider, unbound-endpoint, and cross-authority auto-forwarding are correctly forbidden, yet same-provider/same-authority redirects remain underdetermined when the target may resolve to another allowed endpoint. The same pinned profile/target can therefore produce FORWARD, BLOCK, or REBIND_REQUIRED in different implementations.

R1 must define a closed redirect vocabulary, exact authority/endpoint applicability, same-authority behavior, and deterministic rebind requirements. `C2-305` covers cross-authority leakage but does not cover this same-authority/bound-endpoint determinism gap.

### C2SEC-B02 — private-state least-scope is not machine-closed

`PrivateStateBindingProfile` has `declared_private_state_scope_refs[]` and `public_projection_rule`, while the contract requires actual provider-bound scope to be a subset of the trusted declared scope. Missing semantics:
- scope-ref identity/ownership;
- operation-local actual scope representation;
- canonical set/deduplication;
- exact subset predicate;
- unresolved/wrong-kind/unknown scope behavior;
- closed or exact pinned meaning of `public_projection_rule`.

Two implementations can therefore disagree on whether the same private-state request is within scope.

**Existing failure: `C2-313`.**

R1 must define exact scope refs, `actual_private_state_scope_refs[]` or equivalent, canonical subset semantics, fail-closed invalid refs, and a closed/pinned public-projection rule.

### C2SEC-B03 — secure-ingress assessment bundle integrity not closed

The four axes and precedence are good:

`secret_constraint`, `privacy_constraint`, `licensing_constraint`, `retention_constraint`.

But the formula applies only to a "complete trusted assessment bundle" without defining the replayable bundle. Missing semantics:
- exactly one result per axis;
- same ingress candidate for all axis results;
- exact secure-ingress profile;
- exact pinned security/privacy/licensing/retention policy refs;
- missing/duplicate/conflicting-axis handling;
- unresolved/mismatched policy refs;
- prohibition on mixing results from different candidates/policy snapshots;
- exact linkage from final decision to assessment record.

The precedence function is deterministic only after a valid bundle exists; the load-bearing bundle itself is not.

**Existing failure: `C2-319`.**

R1 must define a `SecureIngressAssessmentRecord` (or equivalent), exact candidate/profile/policy binding, exactly-one-per-axis completeness, fail-closed invalid bundles, and decision linkage.

### C2SEC-B04 — operation-local credential lease lacks operation identity

The auditable `CredentialLease` descriptor contains lease/credential/profile/provider/endpoint/capability identity and READY/BLOCKED, but no `provider_operation_ref`, route-attempt ref, or equivalent trusted operation identity. Thus the record cannot prove that a READY lease was issued for one exact operation rather than reused across two otherwise identical operations.

R1 must bind each lease to one exact operation/attempt identity and make cross-operation reuse invalid. The operation ref itself grants no capability.

Current acceptance coverage is insufficient: `C2-311` tests bounded secret lifetime, not operation-identity binding/reuse.

## Passed security surface

All other existing C2.04 obligations pass at their stated contract scope, including:
- no public real credentials or secret-derived public fingerprints;
- credential != C6 capability / PAPER/LIVE authority;
- provider/endpoint/capability mismatch blocking;
- trusted secret source only;
- cross-provider and cross-authority leakage prohibition;
- request-capture sanitation;
- provider content cannot expand/retarget private state;
- secure ingress before permitted raw;
- valid-bundle precedence `REJECT > QUARANTINE/INDETERMINATE > REDACT > ADMIT`;
- `INDETERMINATE -> QUARANTINE`;
- redaction requires full reassessment;
- permitted-raw hash uses exact admitted bytes;
- EPHEMERAL_ONLY forbids persisted raw/raw_payload_ref;
- quarantine/reject isolation and no false NO_DATA;
- diagnostic sanitation without C2.02 reclassification;
- ingress admission != C5 verification;
- ingress timestamp != C4 available_from;
- no vendor/secret-store/KMS choice;
- C2.OPEN-013 remains for C2.06.

## Non-blocking carried notes

1. Repeated `REASSESS_REDACTED` remains non-admitted; C7 may bound orchestration. C2.07 must ensure budget termination never converts a non-terminal redaction cycle to ADMIT.
2. C2.06 still owns exact C2/C6/C7/C11 wire bindings and frozen C1 OutcomeAxes reconciliation.
3. C2.07 must encode repaired semantics rather than inventing them.

## Open-question disposition

```text
C2.OPEN-008 = NOT_CLOSED / REPAIR_REQUIRED
C2.OPEN-009..012 = OPEN_UNCHANGED
C2.OPEN-013 = OPEN_UNCHANGED_C2_06_PERMITTED_RAW_HANDOFF
C2.OPEN-014..015 = OPEN_UNCHANGED
```

## Next gate

`C2.04R1 scoped repair -> C2.04R1 Independent Security-Boundary Re-Check`

R1 scope only:
1. redirect-forwarding closure;
2. private-state exact scope/subset/public-projection semantics;
3. secure-ingress assessment-bundle completeness/replay binding;
4. credential-lease exact operation identity;
5. corresponding acceptance additions/re-checks.

C2.05: `NOT_AUTHORIZED`.
Production implementation: `NOT_AUTHORIZED`.
External/PAPER/LIVE side effects: `NOT_AUTHORIZED`.
