# C2.01R1 — Acceptance Test Delta Candidate

Generated: 2026-08-24T02:02:00Z

Status: `REPAIR_CANDIDATE / NOT INDEPENDENTLY RECHECKED / NOT FROZEN`

This delta is additive. It does **not** rewrite C2.01 `C2-044..C2-083`. It adds targeted repair obligations for `C2CAP-B01` and `C2CAP-B02`. Independent re-check must also re-evaluate the previously failed `C2-057`, `C2-063`, `C2-065`, and `C2-066` against the C2.01R1 successor semantics.

| ID | Decision | Obligation | Adversarial / negative test |
|---|---|---|---|
| `C2-084` | `C2.DEC-067` | The stable-ref kind domain explicitly represents observation families, semantic features, provider-native identifier namespaces, provider-native subject semantics, record grouping semantics, and provider-native defaulting semantics. | Any load-bearing slot requires an invented/private kind because the declared domain lacks a representable kind => fail. |
| `C2-085` | `C2.DEC-068` | Every load-bearing `*_ref` / `*_refs[]` slot in the C2.01R1 logical model declares an explicit permitted `ref_kind` set. | A ref-bearing slot has no slot→kind contract or accepts an undeclared kind => fail. |
| `C2-086` | `C2.DEC-069` | Unknown kinds and known-but-wrong kinds are rejected before semantic compatibility evaluation. | Put `FIELD_SEMANTIC` into `produced_observation_family_refs[]` or an unknown private kind into any load-bearing slot => fail closed. |
| `C2-087` | `C2.DEC-070` | Provider-native identifier namespace and subject-semantic refs are typed provider semantics and never mint canonical C1 identity/classes by fiat. | A `PROVIDER_NATIVE_IDENTIFIER_NAMESPACE` or `PROVIDER_NATIVE_SUBJECT_SEMANTIC` ref is treated as an `InstrumentID`/canonical C1 class without C1 resolution => fail. |
| `C2-088` | `C2.DEC-071` | `CapabilityRequirement` is typed: observation requirements use `OBSERVATION_FAMILY_SEMANTIC`, query requirements use `QUERY_SEMANTIC`, response requirements use only the enumerated response-closure kinds, and feature requirements use `SEMANTIC_FEATURE`. | Wrong-kind requirement ref is accepted because its logical_id looks related => fail. |
| `C2-089` | `C2.DEC-072` | `effective_response_semantic_refs(P,S)` is exactly the union of capability-declared response refs plus the endpoint profile's response semantic, grouping, field, pagination-if-present, absence-signal and partiality-signal refs. | A required response ref not in that exact union is considered satisfied => fail. |
| `C2-090` | `C2.DEC-073` | Response compatibility closure is one-hop only; provider-wide refs, transitive dereferences, provider docs/names and implicit inference do not enter the satisfaction set. | A field definition points to another semantic ref and that transitive ref is used to satisfy a requirement, or provider-wide default auto-enters closure => fail. |
| `C2-091` | `C2.DEC-074` | Stable-ref equality for compatibility is equality of `(authority, ref_kind, logical_id, semantic_revision, content_sha256)`. | Same logical_id/revision with different content hash is treated as the same semantic ref => fail. |
| `C2-092` | `C2.DEC-075` | Any dangling, unknown-kind, wrong-kind, content-mismatched, floating-alias or private-extension ref involved in compatibility makes semantic compatibility unproven and therefore false. | Broken/wrong-kind ref is ignored or treated as probably compatible => fail. |
| `C2-093` | `C2.DEC-076` | C2.01R1 only addresses `C2CAP-B01/B02`; blocker closure and `C2.OPEN-003` closure require Independent Capability Re-Check, and C2.02 remains unauthorized until that gate passes. | Repair construction marks blocker CLOSED, marks OPEN-003 frozen, or starts C2.02 before independent re-check => fail. |

Count: **10** (`C2-084..C2-093`).

Required re-check targets from the predecessor review:

```text
C2-057
C2-063
C2-065
C2-066
C2-084..C2-093
C2CAP-B01
C2CAP-B02
```

No obligation in this delta authorizes production provider adapters, external/PAPER/LIVE side effects, C2.02 construction, route selection, credential wiring, completeness certification, C4 PIT conclusions, or C5 source-fitness conclusions.
