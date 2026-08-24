# C2.01 — Acceptance Test Delta Candidate

Generated: 2026-08-24T01:11:00Z

Status: `CANDIDATE / NOT REVIEWED / NOT FROZEN`

This delta extends the C2 candidate acceptance namespace after C2.00 `C2-001..C2-043` and covers C2.01 only.

| ID | Decision | Obligation | Adversarial/negative test |
|---|---|---|---|
| `C2-044` | `C2.DEC-027` | Capability granularity is one semantic operation surface × access pattern × query signature × observation families × response contract. | A provider-level marketing claim cannot satisfy a capability record. |
| `C2-045` | `C2.DEC-028` | Access-pattern taxonomy is vendor-neutral and does not define canonical financial identity. | DIRECT_LOOKUP cannot be interpreted as C1 exact identity resolution. |
| `C2-046` | `C2.DEC-029` | Capability semantics are separate from health, credentials, quota, cache, certification and routing priority. | Inject current health/credential/quota into capability record => reject. |
| `C2-047` | `C2.DEC-030` | Materially different operation modes require separate endpoint semantic state/capability records. | One broad endpoint profile covering different null/pagination/query meanings => fail. |
| `C2-048` | `C2.DEC-031` | Provider-wide semantic defaults are never implicit; endpoint profiles explicitly adopt stable refs. | Mutable provider-wide default silently changes endpoint meaning => fail. |
| `C2-049` | `C2.DEC-032` | Field semantics preserve provider-native selector, meaning, shape, units, sentinels, enum and timestamp role. | Blind blank/zero/null coercion without pinned field semantics => fail. |
| `C2-050` | `C2.DEC-033` | C1-facing observation families exactly preserve C1.05R1 interface categories. | Provider field mapped to ad-hoc canonical C1 type outside supported categories => fail. |
| `C2-051` | `C2.DEC-034` | Additional provider-observation families remain provider-side and cannot mint C1 canonical identities. | PROVIDER_REFERENCE_OBSERVATION copied into InstrumentID => fail. |
| `C2-052` | `C2.DEC-035` | Endpoint request semantics explicitly pin required/optional/mutually-exclusive/defaulting query semantics. | Implicit provider default changes request meaning during replay => fail. |
| `C2-053` | `C2.DEC-036` | Endpoint response semantics explicitly pin cardinality, grouping, fields, pagination, absence and partiality signals. | Global provider semantics assumed without endpoint ref => fail. |
| `C2-054` | `C2.DEC-037` | Provider-native absence signals are descriptive and do not by themselves authorize C2 NO_DATA. | Empty collection => NO_DATA in C2.01 => fail. |
| `C2-055` | `C2.DEC-038` | Provider-native partiality/truncation signals are descriptive and do not freeze C2 PARTIAL rules. | Truncation flag => final C2 PARTIAL logic in C2.01 => fail. |
| `C2-056` | `C2.DEC-039` | Pagination semantics are endpoint semantics, not completeness certification. | Cursor exhausted => certified exhaustive universe without C2.05 attestation => fail. |
| `C2-057` | `C2.DEC-040` | Stable semantic refs bind authority, kind, logical id, semantic revision and content SHA-256. | Version string without immutable content identity used load-bearing => fail. |
| `C2-058` | `C2.DEC-041` | Floating aliases are never persisted as load-bearing C2 semantic refs. | provider_profile_ref=latest => fail. |
| `C2-059` | `C2.DEC-042` | Supersession creates new immutable refs; historical refs remain resolvable. | Update old semantic payload in place under same ref => fail. |
| `C2-060` | `C2.DEC-043` | Registry snapshot itself is snapshot-stable and pins all semantic entry refs. | Replay resolves same registry id to different entry set => fail. |
| `C2-061` | `C2.DEC-044` | Semantic changes to query/response/field/pagination/signal meaning require new semantic content identity. | Unit scale changes without new ref => fail. |
| `C2-062` | `C2.DEC-045` | Compatibility requires exact access-pattern match. | SEARCH silently substituted for DIRECT_LOOKUP => incompatible. |
| `C2-063` | `C2.DEC-046` | Required observation families must be a subset of provider capability outputs. | Missing required LISTING_OBSERVATION still compatible => fail. |
| `C2-064` | `C2.DEC-047` | Required query semantics must be explicitly accepted by provider capability. | Provider-native time filter guessed from arbitrary parameter => fail. |
| `C2-065` | `C2.DEC-048` | Required response semantics/features must be explicitly satisfied by pinned capability/endpoint records. | Compatibility inferred from provider name/docs rather than pinned records => fail. |
| `C2-066` | `C2.DEC-049` | Unresolvable or content-mismatched semantic refs fail compatibility closed. | Broken ref treated as probably compatible => fail. |
| `C2-067` | `C2.DEC-050` | C2.03 routing may choose only among semantically compatible capabilities and cannot weaken C2.01 compatibility. | Routing priority overrides semantic incompatibility => fail. |
| `C2-068` | `C2.DEC-051` | C1 provider_profile_ref maps to stable PROVIDER_SEMANTIC_PROFILE ref. | Mutable provider profile used by normalization replay => fail. |
| `C2-069` | `C2.DEC-052` | C1 provider_field_semantic_refs map to stable FIELD_SEMANTIC refs. | Field semantics omitted from replay when load-bearing => fail. |
| `C2-070` | `C2.DEC-053` | C1 provider_capability_ref maps to stable CAPABILITY_DEFINITION ref. | Capability handle resolves different endpoint profile later => fail. |
| `C2-071` | `C2.DEC-054` | C2 completeness refs are not defined here but must later obey same stable-ref discipline. | C2.01 invents completeness certification strength => fail. |
| `C2-072` | `C2.DEC-055` | Provider-native timestamp roles never become C4 available_from/revision/PIT-safe semantics. | PROVIDER_PUBLISHED_TIME_CLAIM copied to available_from by C2 => fail. |
| `C2-073` | `C2.DEC-056` | Capability/endpoint semantics never encode C5 source fitness, verification or conflict strength. | Provider quality score converted to VERIFIED => fail. |
| `C2-074` | `C2.DEC-057` | Capability/endpoint semantics never encode C3 TTL/cache/quota/LKG policy. | Rate limit or TTL scheduler field in capability semantic record => fail. |
| `C2-075` | `C2.DEC-058` | Capability semantics do not grant C6 tool capability or C7 workflow authority. | Provider entry causes WRITE_EXTERNAL/PAPER/LIVE permission => fail. |
| `C2-076` | `C2.DEC-059` | Endpoint semantics do not authorize raw persistence before secure-ingress admission. | DOCUMENT_RETRIEVAL writes immutable raw before admission => fail. |
| `C2-077` | `C2.DEC-060` | Registry contains no concrete provider instances or priority configuration in C2.01. | Alpaca/Tushare/etc marked canonical/preferred in registry => fail. |
| `C2-078` | `C2.DEC-061` | C2.01 constructs no production adapter executable or endpoint credential wiring. | Production SDK/API client code added => fail. |
| `C2-079` | `C2.DEC-062` | C2.OPEN-001 is candidate-closed only by taxonomy/granularity subject to independent review. | Mark OPEN-001 frozen before review => fail. |
| `C2-080` | `C2.DEC-063` | C2.OPEN-002 is candidate-closed only by logical record/binding model subject to independent review. | Mark OPEN-002 frozen before review => fail. |
| `C2-081` | `C2.DEC-064` | C2.OPEN-003 is candidate-closed only by stable-ref/compatibility/version model subject to independent review. | Mark OPEN-003 frozen before review => fail. |
| `C2-082` | `C2.DEC-065` | C2.OPEN-004..015 remain open and are not silently resolved by C2.01. | Detailed error/routing/credential/completeness algorithm appears in C2.01 => fail. |
| `C2-083` | `C2.DEC-066` | Final machine JSON Schema, canonicalization and executable validators remain C2.07-owned. | C2.01 claims final wire schema is frozen => fail. |

Count: **40** (`C2-044..C2-083`).

No test in this delta authorizes production adapters, external side effects, or C2.02 construction.
