# C2.04R1 Independent Security-Boundary Re-Check Report

Generated: 2026-09-07T05:58:00Z

Review type: `INDEPENDENT_SECURITY_BOUNDARY_RECHECK`

Candidate under review: `C2.04R1 — Credentials / Private-State / Secure Ingress Boundary Scoped Repair Candidate`

## 1. Review posture

This re-check is independent of the C2.04R1 construction self-check. `C2_04R1_CONSTRUCTION_VALIDATION` is treated only as candidate metadata and is not used as independent security evidence.

The effective contract reviewed is the immutable C2.04 parent contract plus the explicit C2.04R1 repair contract. The review scope is limited to the four C2.04 security blockers, the two failed parent obligations, the 53 new R1 obligations, and non-regression of the previously passing C2.04 surface.

No C2.05 construction, production provider adapter, secret-store implementation, or external/PAPER/LIVE side effect is authorized by this re-check.

## 2. Exact reviewed pins

```text
C2.04 parent normative contract       198d194fbb3814676f1cb74aec5d56f19f8b1f9b081c6d77c16b4e66fd762cda
C2.04 parent logical model            9d3609c775967fe374c1e1007828540d893852834bece09986148bf5a8aad5af
C2.04 parent acceptance delta         2a0b24c0f9d67a03c565f16e2985d0a5ecbaaff090c4715b2b7ea9b8491c0b8a
C2.04 parent decision ledger          719018dd73c1e80e9633d0468972e253dae4f77a3ffda75e1c0169c16c9aeac4
C2.04 Independent Review report       12aead5a1d4fc5eea0813cedbf360fd68616b432f34100db341367d96405fe21
C2.04 Independent Review result       4eb3daf2cecb0478731b814dd7749f06e990b5748f9301b8792c84dff9c22f78

C2.04R1 repair contract               4023224a9b0f23cd006279c217600412376588eced9c62010861ccddf065a548
C2.04R1 logical model                 1759727de3dac14cabe8958762d3602c10859bc965f2919ac2fd785bf79a5ff5
C2.04R1 acceptance delta              4a6b1924a3af4e18ea0f8ddae56d09ed1df0a426f79f9212313c862cee63a43f
C2.04R1 decision ledger               5cc37ad59aad835b5f05138b94acd3b2818e5378ef5671b0ee4ce58477ce4e07
C2.04R1 repair diffs                  c4557c68f4833cd628f7685cf5ff5dc65076f90ef1840bfce0faa1f89524897c
C2.04R1 candidate archive commit      3c68da71384829248f30aeec584cca499c86ccd3
C2.04R1 candidate subtree             d33998b0fd896ccf6ef035093a370724ac86da00
```

## 3. Blocker re-check

### C2SEC-B01 — CLOSED

The parent failure was that `redirect_forwarding_semantics` was required but semantically open, allowing implementation-dependent same-authority forwarding behavior.

R1 replaces that field with the closed modes:

```text
BLOCK_ALL_REDIRECTS
REBIND_ON_ANY_REDIRECT
FORWARD_SAME_AUTHORITY_SAME_ENDPOINT
```

and the closed decisions:

```text
FORWARD_EXISTING_LEASE
REBIND_REQUIRED
BLOCK
```

The ordered predicate is total over the reviewed inputs:

1. unresolved trusted identity -> `BLOCK`;
2. provider mismatch -> `BLOCK`;
3. destination-authority mismatch -> `BLOCK`;
4. capability mismatch -> `BLOCK`;
5. target endpoint outside the allowed endpoint set -> `BLOCK`;
6. `BLOCK_ALL_REDIRECTS` -> `BLOCK`;
7. `REBIND_ON_ANY_REDIRECT` -> `REBIND_REQUIRED`;
8. `FORWARD_SAME_AUTHORITY_SAME_ENDPOINT` -> same endpoint `FORWARD_EXISTING_LEASE`, otherwise permitted different endpoint `REBIND_REQUIRED`.

Raw redirect content cannot mint trusted provider/endpoint/capability/authority identity, and HTTP/SDK automatic redirects cannot bypass the predicate. Rebind is explicitly non-dispatching for the old lease and requires a fresh lease descriptor.

Adversarial cases were reasoned through for cross-provider, cross-authority, same-authority unbound endpoint, same-authority different allowed endpoint, same exact endpoint, capability change, unresolved identity, unknown mode, and replay-equivalent inputs. No second valid redirect decision remains for the same pinned inputs.

**Verdict:** `C2SEC-B01 = CLOSED`.

### C2SEC-B04 — CLOSED

The parent lease descriptor lacked exact operation identity and could not prove operation-local use.

R1 requires both:

```text
provider_operation_ref
route_attempt_ref
```

and requires exact equality at credential-use time for operation, route attempt, provider, endpoint, capability, binding profile, credential handle, and credential version. Any mismatch prohibits dispatch and yields `LEASE_OPERATION_IDENTITY_MISMATCH`.

The same `credential_lease_id` cannot span different provider-operation or route-attempt identities. A new operation, new route attempt, or redirect rebind requires a fresh lease ID. Operation and route-attempt refs remain audit/binding identities only and grant no C6 capability or side-effect authority.

Cross-operation reuse, cross-attempt reuse, same-credential-version reuse, redirect rebind reuse, and exact-match use were adversarially checked. The contract is single-valued and fail-closed for the blocker identified in the parent review.

**Verdict:** `C2SEC-B04 = CLOSED`.

### C2SEC-B02 — CLOSED

The parent private-state boundary lacked machine-closed scope identity, canonical-set semantics, exact operation-local actual scope, exact subset evaluation, and a pinned public-projection meaning.

R1 introduces exact `PRIVATE_STATE_SCOPE` stable refs as atomic authorization-set identities. There is no wildcard, prefix, display-name, hierarchy, or inferred containment semantics. Both declared and actual scope sets are built by exact ref resolution, reject wrong-kind/dangling/hash-mismatched/unknown refs, reject same-logical-id conflicting revision/hash identities, deduplicate exact duplicates, and sort by a closed bytewise key.

Every provider operation supplying provider-bound private state carries an operation-local `PrivateStateOperationScopeRecord` with provider-operation, route-attempt, binding-profile, private-state-handle, actual-scope, and scope-decision fields. The actual scope originates only from trusted operation authorization/state; external provider/web/tool/model content cannot expand it.

The exact decision is:

```text
WITHIN_DECLARED_SCOPE
    iff declared and actual canonical sets are valid
    and every exact actual scope ref is in the declared set

BLOCKED_SCOPE
    otherwise
```

`BLOCKED_SCOPE` prohibits private-state injection and dispatch for an operation requiring that private state. This closes the original `C2-313` failure.

The free-form parent `public_projection_rule` is replaced by an exact `PUBLIC_PROJECTION_RULE` stable ref. Projection modes and metadata fields are closed. Private-state handles/values, account identifiers, portfolio/order/transaction contents, private thesis/research material, credential identities, secret-store locators, and secret material cannot be projected by the rule. Unresolved projection-rule binding blocks private-state preparation.

The remaining exact C2/C6/C7/C11 record/wire binding is correctly retained for C2.06 and does not reopen the semantic subset decision.

**Verdict:** `C2SEC-B02 = CLOSED`.

### C2SEC-B03 — CLOSED

The parent ingress precedence was deterministic only after an undefined "complete trusted assessment bundle" existed.

R1 defines a load-bearing `SecureIngressAssessmentRecord` and `SecureIngressAxisResult` model. A valid record contains exactly four axis results, exactly one each for:

```text
SECRET
PRIVACY
LICENSING
RETENTION
```

Every result must bind to the same ingress candidate, provider operation, ingress semantic profile, and its exact corresponding pinned policy ref. Axis-result IDs must be unique. Unknown/missing/duplicate axes, unknown constraints, unresolved or non-immutable profile/policy refs, mixed candidate/operation/profile/policy snapshots, or stored decision/retention mismatch make the bundle `INVALID_FAIL_CLOSED`.

Invalid bundles do not enter ordinary precedence. They deterministically produce:

```text
ingress_decision = QUARANTINE
retention_mode = NONE
permitted_raw_handoff = forbidden
ephemeral_admit = forbidden
C1_normalization = forbidden
```

For a valid bundle, the parent precedence is preserved exactly:

```text
REJECT
> QUARANTINE / INDETERMINATE
> REASSESS_REDACTED
> ADMIT
```

with `EPHEMERAL_ONLY` versus `PERMITTED_RAW` retention preserved under ADMIT.

A load-bearing decision must resolve to the exact assessment record; bare decision enums cannot authorize admission. Stored decision/retention must recompute from that exact record. Redaction creates a new ingress event, new assessment record, and four new axis-result identities; old assessment material is lineage only.

Mixed-candidate, mixed-operation, mixed-profile, mixed-policy, missing-axis, duplicate-axis, unknown-axis/constraint, invalid stored decision, bare-decision, and redaction-reuse attacks were adversarially reasoned through. No path was found from an invalid or incompletely replay-bound bundle to ADMIT.

This closes the original `C2-319` failure.

**Verdict:** `C2SEC-B03 = CLOSED`.

## 4. Failed parent-obligation re-check

```text
C2-313 PASS
  Actual provider-bound private-state scope is now an exact canonical subset check.
  Extra or invalid scope yields BLOCKED_SCOPE and prohibits private-state dispatch.

C2-319 PASS
  Secret/privacy/licensing/retention remain separate axis results and are now
  exactly-one-per-axis inside one replay-bound assessment record.
```

## 5. R1 acceptance re-check

Reviewed: `C2-349..C2-401` (53 obligations).

```text
C2-349 PASS  unknown redirect mode fails closed
C2-350 PASS  unresolved redirect identity blocks
C2-351 PASS  cross-provider redirect blocks
C2-352 PASS  cross-authority redirect blocks
C2-353 PASS  same-authority unbound endpoint blocks
C2-354 PASS  different allowed endpoint requires rebind under forward-same-endpoint mode
C2-355 PASS  exact same endpoint may forward only under the explicit forward mode
C2-356 PASS  rebind-on-any mode is deterministic
C2-357 PASS  block-all mode is deterministic
C2-358 PASS  redirect capability change blocks
C2-359 PASS  HTTP/SDK auto-redirect cannot bypass the predicate
C2-360 PASS  identical pinned redirect inputs replay to the same decision

C2-361 PASS  lease requires provider_operation_ref
C2-362 PASS  lease requires route_attempt_ref
C2-363 PASS  READY lease use requires exact issued identity match
C2-364 PASS  provider-operation mismatch rejects reuse
C2-365 PASS  route-attempt mismatch rejects reuse
C2-366 PASS  lease ID cannot span operation/attempt identities
C2-367 PASS  new operation/attempt requires a fresh lease
C2-368 PASS  operation identity grants no capability
C2-369 PASS  redirect rebind requires a fresh lease ID

C2-370 PASS  wrong-kind/unresolved private-state scope fails closed
C2-371 PASS  conflicting scope revisions in one set are invalid
C2-372 PASS  exact duplicate scope refs deduplicate
C2-373 PASS  scope canonicalization is order invariant
C2-374 PASS  exact actual subset passes
C2-375 PASS  out-of-scope actual ref blocks
C2-376 PASS  empty actual scope is a valid subset
C2-377 PASS  wildcard/hierarchy implication is forbidden
C2-378 PASS  external content cannot add actual scope
C2-379 PASS  free-form public-projection rule is not load-bearing
C2-380 PASS  unresolved projection rule blocks private-state preparation
C2-381 PASS  exclude-all emits no private-state handles/values
C2-382 PASS  metadata allowlist is closed
C2-383 PASS  forbidden projection fields invalidate the rule

C2-384 PASS  valid assessment has exactly one result per axis
C2-385 PASS  missing axis -> INVALID_FAIL_CLOSED -> QUARANTINE/NONE
C2-386 PASS  duplicate axis fails closed
C2-387 PASS  unknown axis/constraint fails closed
C2-388 PASS  mixed ingress candidates fail closed
C2-389 PASS  mixed provider operations fail closed
C2-390 PASS  mixed ingress profiles fail closed
C2-391 PASS  mixed policy snapshots fail closed
C2-392 PASS  unresolved/non-immutable profile or policy fails closed
C2-393 PASS  valid bundle preserves parent precedence
C2-394 PASS  stored decision/retention must recompute
C2-395 PASS  decision must link to exact assessment record
C2-396 PASS  redacted candidate requires a new complete assessment record
C2-397 PASS  old axis results cannot admit the redacted candidate
C2-398 PASS  explicit INDETERMINATE is valid but quarantined
C2-399 PASS  invalid bundle cannot admit under any retention mode
C2-400 PASS  four axes remain separate and integrity-closed
C2-401 PASS  previously passing C2.04 security surface is not weakened

PASS: 53
FAIL: 0
```

## 6. Parent C2.04 non-regression

The R1 effective-contract rule explicitly preserves every parent C2.04 rule not replaced by the scoped repair. The re-check found no weakening of the prior 58/60 passing surface.

Still preserved:

- no real credential/secret bytes or secret-derived public fingerprint in public artifacts;
- credential possession does not grant C6 capability or PAPER/LIVE authority;
- provider/endpoint/capability binding remains mandatory;
- credential source remains trusted-only;
- cross-provider and cross-authority secret leakage remains prohibited;
- request-capture and diagnostics remain sanitized;
- provider content cannot expand or retarget private state;
- secure ingress precedes permitted raw;
- valid ingress precedence and INDETERMINATE fail-closed behavior remain unchanged;
- redaction still requires complete reassessment;
- permitted-raw hash remains the hash of admitted bytes;
- EPHEMERAL_ONLY cannot create persisted raw payload;
- QUARANTINE/REJECT cannot enter C1 normalization or become false NO_DATA;
- secure-ingress ADMIT is not C5 verification;
- ingress time is not C4 available_from;
- no provider vendor, secret-store/KMS, or production adapter is selected;
- exact C2->C11 permitted-raw handoff remains deferred to C2.06.

Effective acceptance after repair:

```text
C2-289..C2-401
113 PASS
0 FAIL
```

## 7. Additional adversarial checks

The re-check also exercised interactions not reducible to one acceptance-row label:

1. Same provider + same authority + same capability + different allowed endpoint cannot preserve the old lease; it is `REBIND_REQUIRED` or `BLOCK` according to the pinned mode.
2. A same-endpoint redirect cannot preserve the old lease if operation/route-attempt identity changes; B01 forwarding permission is subordinate to B04 exact lease identity.
3. A newly trusted cross-authority operation is not a redirect-forward of the old credential lease and cannot reuse that lease ID.
4. Scope-set equality cannot be manufactured by input ordering, exact duplicates, wildcard labels, or a newer revision sharing the same logical ID.
5. A valid smaller-scope record cannot authorize an extra actual scope ref; the exact-set subset rule remains monotone fail-closed.
6. External/provider content cannot convert a scope or projection identifier into trusted authority merely by naming it.
7. Four individually valid axis results cannot be spliced across candidate, provider operation, ingress profile, or policy snapshot.
8. Duplicate axis results are invalid even when duplicate values agree, preventing majority/tie-break implementation variance.
9. A stored ADMIT decision cannot survive if recomputation from the bound assessment record yields any other result.
10. Repeated `REASSESS_REDACTED` remains non-admitted; later C7 budget termination cannot be interpreted as admission authority.

No alternative valid security decision was found for identical pinned semantic inputs.

## 8. Boundary and ownership re-check

PASS:

- C3 retains retry/quota/cache/freshness/coalescing/LKG semantics.
- C4 retains PIT/revision/available_from authority.
- C5 retains evidence verification/source-fitness/conflict authority.
- C6 retains capability, policy, trusted-intent, destination/egress, and side-effect authority.
- C7 retains orchestration, budgets, cancellation, and durable continuation.
- C11 retains persistence implementation.
- C2.06 retains exact C2/C6/C7/C11 wire bindings, including permitted-raw/quarantine handoff and frozen C1 OutcomeAxes serialization reconciliation.
- C2.07 must encode these repaired closed semantics and must not invent alternatives.
- Production provider/adaptor instances remain zero.
- External/PAPER/LIVE side effects remain unauthorized.

## 9. Open-question disposition

```text
C2.OPEN-008 = CLOSED_AT_C2_04_SECURITY_BOUNDARY_CONTRACT_LEVEL
C2.OPEN-009..012 = OPEN_UNCHANGED
C2.OPEN-013 = OPEN_UNCHANGED_C2_06_PERMITTED_RAW_HANDOFF
C2.OPEN-014..015 = OPEN_UNCHANGED
```

## 10. Final verdict

`PASS — C2.04 REVIEW_PASSED_NOT_FROZEN`

```text
C2SEC-B01 = CLOSED
C2SEC-B02 = CLOSED
C2SEC-B03 = CLOSED
C2SEC-B04 = CLOSED

C2.04 = REVIEW_PASSED_NOT_FROZEN
C2.05 = NOT_STARTED / NOT_AUTHORIZED
Production implementation = NOT_AUTHORIZED
External/PAPER/LIVE side effects = NOT_AUTHORIZED
```

The next permissible gate is explicit user authorization for:

`C2.05 — Provider Certification / Completeness / Coverage Attestations`.
