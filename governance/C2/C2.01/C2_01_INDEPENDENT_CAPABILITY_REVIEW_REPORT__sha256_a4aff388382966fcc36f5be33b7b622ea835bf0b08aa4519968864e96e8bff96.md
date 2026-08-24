# C2.01 — Independent Capability Review Report

Generated: 2026-08-23

## 1. Review posture

This is an independent semantic review of the immutable C2.01 construction candidate after the candidate was synchronized to GitHub. Construction-time mechanical checks are treated as input evidence only; they are not reused as the review verdict.

Authority state entering review:

```text
C0 = FROZEN
C1 = FROZEN
C1 Freeze Seal SHA-256 = 438274542570f7398af8622fdb511b85d69fc4c403b246b93a8a593b5d8070a5
C2.00 Independent Scope Review = PASS
C2.00 = REVIEW_PASSED_NOT_FROZEN
C2.01 = CONSTRUCTED_CANDIDATE_NOT_REVIEWED
C2.02 = NOT_AUTHORIZED
Production implementation = NOT_AUTHORIZED
External/PAPER/LIVE side effects = NOT_AUTHORIZED
```

Review package SHA-256:

`2294f6d577b4fda3b902d087640d604549d7517f36cdb329f25b26060bbacdb6`

The review package was independently unpacked and all bundled content-addressed members matched their expected SHA-256 identities.

## 2. GitHub synchronization precondition

The independent review began only after the exact C2.01 construction candidate was present on GitHub `main`.

The reconstruction commit is:

`22c85cc54fcb0a25eb2fa87ec66ca0b7728c6fbe` — `governance(C2.01): archive exact construction candidate`

The two large candidate artifacts were verified by exact Git blob identity against the local canonical bytes:

| Artifact | SHA-256 | Expected/remote Git blob | Result |
|---|---|---|---|
| Provider Capability & Endpoint Semantic Registry Candidate | `12e3ade1031d1e608ff31ebea0b58d9c8505ea36533e624f8a4af82f0794961a` | `fcdf1b7e35a065f6f766e1c957467bd7b48a7daa` | EXACT |
| Evidence / Decision Ledger Candidate | `de64fd89c75cf24e56011ec4219a1967dc2de2b89b17ffd8d9516d6e48ba7ffc` | `f098893aca2cdab7085c6ac22aba5183bd74c265` | EXACT |

The temporary reconstruction chunks and temporary workflow were removed after exact reconstruction. The non-authoritative `governance/C1/C1_FROZEN_INDEX.md` is present separately and does not alter the C1 freeze seal or frozen C1 authority.

## 3. Candidate identities reviewed

| Artifact | SHA-256 | Identity result |
|---|---|---|
| Registry prose candidate | `12e3ade1031d1e608ff31ebea0b58d9c8505ea36533e624f8a4af82f0794961a` | MATCH |
| Registry logical model candidate | `85f580578722a7ce75d7a3e31929d58624d8e8ff1704c9f63c8c99600db3a589` | MATCH |
| Acceptance delta candidate | `0324f84b81f6f46e08e557c7de95ee596b9cc2bcaf7a6e3c428e5c6550180566` | MATCH |
| Evidence / decision ledger candidate | `de64fd89c75cf24e56011ec4219a1967dc2de2b89b17ffd8d9516d6e48ba7ffc` | MATCH |
| Candidate selection | `1b358c2ebd2149367f0727fd9bbf211881863d67aa6625bdd3b661dce9cf64d2` | MATCH |
| Construction stage report | `f1757c936984250b126a8c1f40aa865cbe03ffc51c5f36a4a5a924ede2039e45` | MATCH |
| Construction summary | `7fc842209f991f1d6602a8d0dd6c13e972eee41f22c9fb0f9eb1da0508bb8f20` | MATCH |
| Review-package manifest | `853ceefb22aa033ba38b5b952943595b2d45268ed86e0fec1554ba65ccdcbc37` | MATCH |

## 4. Independent attack-surface results

| Surface | Result | Finding |
|---|---|---|
| Capability granularity | PASS | The one-operation-surface × access-pattern × query-signature × observation-family-set × response-contract rule prevents provider-level marketing claims from acting as capabilities. |
| Access-pattern taxonomy | PASS | Taxonomy is vendor-neutral and explicitly does not grant C1 identity, C4 PIT, C5 fitness, completeness, or side-effect authority. |
| Field-semantic/C1 boundary | PASS | Provider fields remain provider semantics and cannot directly mint C1 canonical IDs. |
| Provider-native timestamp/C4 boundary | PASS | Provider timestamp roles are descriptive only and cannot define `available_from`, revision, or PIT safety. |
| Absence/partiality/C2.02 boundary | PASS | Provider-native absence and truncation signals remain descriptive; C2.02 outcome legality is not preempted. |
| Pagination/completeness/C2.05 boundary | PASS | Enumeration and cursor semantics are not treated as completeness certification. |
| C3/C5/C6/C7/C11 boundaries | PASS | Cache/quota, source fitness, tool/workflow authority, and persistence authority remain outside C2.01. |
| Vendor neutrality | PASS | Provider instance list is intentionally empty; no provider priority or canonical vendor is selected. |
| Replay / no-floating-alias discipline | PASS WITH BLOCKER BELOW | The tuple requires content identity and rejects load-bearing `latest/current`; however the ref-kind domain is not closed over all load-bearing refs. |
| Capability compatibility | FAIL | The candidate calls the predicate deterministic but leaves one response-satisfaction branch semantically under-specified and leaves some required capability refs without representable stable ref kinds. |
| Open-question discipline | FAIL FOR OPEN-003 ONLY | OPEN-001 and OPEN-002 are reviewable; OPEN-003 cannot be closed because exact stable-ref/compatibility representation is incomplete. |
| Production boundary | PASS | No provider adapter, credential wiring, routing algorithm, certification algorithm, final wire schema, or external side effect was introduced. |

## 5. Blocking finding C2CAP-B01 — Stable-ref kind domain is not closed over the candidate's own load-bearing references

**Severity: BLOCKER**

The prose candidate states that every load-bearing C2.01 semantic reference logically uses `C2StableSemanticRef` and gives a closed list of allowed `ref_kind` values:

```text
REGISTRY_SNAPSHOT
PROVIDER_SEMANTIC_PROFILE
ENDPOINT_SEMANTIC_PROFILE
FIELD_SEMANTIC
CAPABILITY_DEFINITION
COMPATIBILITY_RULESET
QUERY_SEMANTIC
RESPONSE_SEMANTIC
PAGINATION_SEMANTIC
PROVIDER_NATIVE_SIGNAL_SEMANTIC
```

However the same logical model contains load-bearing reference fields that have no representable type in that allowed domain, including at minimum:

```text
ProviderCapabilityDefinition.produced_observation_family_refs[]
ProviderCapabilityDefinition.semantic_feature_refs[]
ProviderSemanticProfileDefinition.provider_native_identifier_namespace_refs[]
ProviderSemanticProfileDefinition.provider_native_subject_semantic_refs[]
```

This is not merely a C2.07 serialization detail. The candidate itself says observation-family definitions are load-bearing registry semantics and that capability compatibility depends on exact observation-family and semantic-feature refs. C1.05R1 also requires load-bearing C2 semantic/capability dependencies to resolve to snapshot-stable semantic state.

Consequences:

1. A compliant implementation cannot deterministically select a legal `ref_kind` for every required load-bearing ref.
2. Implementations could diverge by using bare strings, reusing an unrelated ref kind, or inventing private kinds.
3. `all_refs_resolve_with_exact_content_identity` cannot be enforced over a reference domain that is not type-closed.
4. `C2.OPEN-003` therefore is not actually candidate-closed at the required exactness level.

Affected acceptance obligations:

```text
C2-057  FAIL — stable semantic ref model is not representationally closed
C2-063  FAIL — produced observation-family refs lack an allowed stable ref kind
C2-065  FAIL — semantic-feature refs lack an allowed stable ref kind
C2-066  FAIL — not every reference can be resolved under the declared exact typed-ref domain
```

Required repair direction:

- introduce explicit stable ref kinds and semantic definitions for every load-bearing ref-bearing slot, or explicitly map each slot to an existing kind without ambiguity;
- at minimum cover observation families and semantic features, and explicitly type provider-native identifier-namespace and subject-semantic refs;
- define an invariant that every `*_ref` / `*_refs[]` field in the C2.01 logical model declares its permitted `ref_kind` set;
- add an adversarial test rejecting unknown, untyped, or wrong-kind refs.

## 6. Blocking finding C2CAP-B02 — Response semantic compatibility is not yet deterministic enough for OPEN-003 closure

**Severity: BLOCKER**

The candidate defines compatibility rule 4 as:

```text
R.required_response_semantics ⊆ P.required_response_semantic_refs
or are explicitly satisfied by P.endpoint_semantic_profile_ref
```

The phrase **“explicitly satisfied by `endpoint_semantic_profile_ref`”** does not define the exact semantic closure used for the subset test. The endpoint profile itself contains several different ref-bearing surfaces — response semantic, record grouping, fields, pagination, and provider-native signals — but the candidate does not state which of those are members of the compatibility satisfaction set, whether transitive dereference is allowed, or how wrong-kind refs fail.

Because C2.01 claims a deterministic fail-closed compatibility predicate, two implementations must not be able to disagree on this relation while both claiming contract compliance.

Required repair direction:

- define an exact `effective_response_semantic_refs(P)` (or equivalent) function over pinned endpoint/capability records;
- enumerate the permitted ref kinds that enter that set;
- define whether dereference is one-hop or transitive and forbid implicit inference;
- require wrong-kind, dangling, content-mismatched, or unenumerated refs to fail compatibility closed;
- add an explicit adversarial compatibility test.

This finding reinforces the failure of `C2-065` and prevents `C2.OPEN-003` closure.

## 7. Acceptance and decision review

All 40 acceptance obligations (`C2-044..C2-083`) and all 40 C2.01 decision records (`C2.DEC-027..C2.DEC-066`) were independently reviewed.

```text
Acceptance obligations reviewed: 40
PASS:                           36
FAIL:                            4
BLOCKING findings:               2

Decision records reviewed:      40
Unblocked/acceptable:            36
Blocked by B01/B02:               4
```

The failed acceptance IDs are `C2-057`, `C2-063`, `C2-065`, and `C2-066`. No other reviewed obligation requires repair before the capability contract can be rechecked.

The mechanical 40/40 bidirectional decision↔acceptance mapping remains valid; the failure is semantic, not referential bookkeeping.

## 8. Open-item disposition

```text
C2.OPEN-001 = REVIEWABLE / NO BLOCKER FOUND IN TAXONOMY-GRANULARITY DECISION
C2.OPEN-002 = REVIEWABLE / NO BLOCKER FOUND IN ENDPOINT-FIELD BOUNDARY MODEL
C2.OPEN-003 = NOT CLOSED — BLOCKED BY C2CAP-B01 AND C2CAP-B02
C2.OPEN-004..015 = OPEN / UNCHANGED
```

Because the stage exit requires the full C2.01 capability contract to pass, partial acceptance of OPEN-001/002 does not authorize C2.02.

## 9. Independent verdict

```text
C2.01 INDEPENDENT CAPABILITY REVIEW: FAIL
C2.01 state: REPAIR_REQUIRED
C2.01 frozen: NO
C2.02 construction: NOT_AUTHORIZED
Production implementation: NOT_AUTHORIZED
External/PAPER/LIVE side effects: NOT_AUTHORIZED
```

The correct next governance gate is a scoped **C2.01R1 repair** that addresses only the two capability-contract blockers above, followed by an independent capability re-check. The existing C2.01 candidate must remain immutable and content-addressed; repair artifacts must be successor artifacts rather than in-place rewrites.

## 10. Exact stop state

```text
C0 = FROZEN
C1 = FROZEN
C2.00 = INDEPENDENT_SCOPE_REVIEW_PASS / NOT_FROZEN
C2.01 = INDEPENDENT_CAPABILITY_REVIEW_FAIL / REPAIR_REQUIRED
C2.02 = NOT_STARTED / NOT_AUTHORIZED
Production implementation = NOT_AUTHORIZED

BLOCKERS:
C2CAP-B01 — stable-ref kind domain not closed over load-bearing refs
C2CAP-B02 — response semantic compatibility closure under-specified

NEXT GATE:
Explicit authorization for C2.01R1 scoped repair, then Independent Capability Re-Check
```
