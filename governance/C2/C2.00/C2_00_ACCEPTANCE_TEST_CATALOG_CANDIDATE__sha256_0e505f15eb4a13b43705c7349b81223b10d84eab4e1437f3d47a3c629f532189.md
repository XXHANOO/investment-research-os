# C2.00 — Acceptance Test Catalog Candidate

Generated: 2026-08-23T22:15:59Z

Status: `CANDIDATE_FOR_C2_00_INDEPENDENT_SCOPE_REVIEW`

Scope: C2.00 scope / authority / vocabulary governance only. These are contract/governance obligations, **not production implementation tests**.

Parent authority includes Frozen C0, Frozen C1, exact C1.05R1 interface, and the user-adopted-but-not-frozen C2 workflow plan.

| Test | Area | Given / attack | Expected | Class | Mapped decision(s) |
|---|---|---|---|---|---|
| `C2-001` | stage authority | The immutable proposed stage plan still contains its pre-adoption status while the current user explicitly adopts that exact snapshot. | Record user adoption as workflow authority without mutating the snapshot or describing it as inherited C0/C1 frozen authority. | `governance` | `C2.DEC-022` |
| `C2-002` | implementation gate | C2.00 construction completes. | Production implementation remains NOT_AUTHORIZED. | `governance` | `C2.DEC-023` |
| `C2-003` | C2 scope | A C2.00 artifact assigns C2 a new canonical identity/evidence/PIT/cache/persistence responsibility. | Reject; C2 scope remains Provider / Source Router / Provider Certification only. | `architecture` | `C2.DEC-001` |
| `C2-004` | C1 boundary | C2 attempts to mint/merge/redefine Entity/Instrument/Listing/Contract identity. | Reject; canonical identity is C1-owned. | `architecture` | `C2.DEC-002` |
| `C2-005` | C3 boundary | C2.00 defines TTL, quota scheduling, freshness, coalescing or last-known-good selection. | Reject/defer to C3. | `architecture` | `C2.DEC-002` |
| `C2-006` | C4 boundary | C2.00 invents exact available_from, revision selection, PIT timestamp or reconstructability semantics. | Reject/defer to C4. | `architecture` | `C2.DEC-002` |
| `C2-007` | C5 boundary | C2.00 defines claim/source fitness, verification strength or conflict adjudication. | Reject/defer to C5. | `architecture` | `C2.DEC-002` |
| `C2-008` | C11 boundary | C2.00 chooses/redefines database/object-store persistence semantics or treats C2 artifacts as authoritative persistence. | Reject/defer persistence implementation to C11 while preserving semantic handoff boundaries. | `architecture` | `C2.DEC-002`, `C2.DEC-017` |
| `C2-009` | C6/C7/C12 seam | Possession of provider credentials or route selection is treated as a tool capability grant, workflow authority or release authority. | Reject; C6/C7/C12 ownership remains separate. | `architecture/security` | `C2.DEC-003` |
| `C2-010` | vocabulary | Provider, underlying source and endpoint are treated as synonymous by definition. | Reject; they are distinct concepts and may coincide only in a particular case. | `semantic` | `C2.DEC-004` |
| `C2-011` | provider capability | A mutable README/marketing page alone is used as the canonical replay-stable provider capability state. | Reject; C2 capability is governed provider-registry semantic state. | `governance` | `C2.DEC-005` |
| `C2-012` | foreign ref stability | C1 load-bearing provider_profile_ref resolves through floating latest semantics. | Reject as replay/audit stable dependency. | `contract` | `C2.DEC-006` |
| `C2-013` | foreign ref stability | C1 load-bearing provider_field_semantic_refs resolve through mutable aliases. | Reject as replay/audit stable dependencies. | `contract` | `C2.DEC-006` |
| `C2-014` | foreign ref stability | C1 load-bearing provider_capability_ref resolves to different semantic state over time. | Reject as replay/audit stable dependency. | `contract` | `C2.DEC-006` |
| `C2-015` | completeness ref stability | Exact absence/uniqueness depends on a floating c2_completeness_ref. | Reject exactness support; completeness dependency must be snapshot-stable. | `contract` | `C2.DEC-006` |
| `C2-016` | outcome axes | A single status field encodes FAILED, NO_DATA, CACHED, PIT_SAFE and VERIFIED. | Reject; operation/data/downstream quality axes remain orthogonal. | `contract` | `C2.DEC-007` |
| `C2-017` | failure vs no-data | Provider authentication/network/server/pagination/parse/schema failure produces SUCCESS+NO_DATA or empty authoritative collection. | Reject; typed FAILED path, no masquerading as NO_DATA. | `provider-contract` | `C2.DEC-008` |
| `C2-018` | rate limit | 429/rate-limit retry exhaustion is returned as genuine NO_DATA. | Reject; typed failure after retry exhaustion. | `provider-contract` | `C2.DEC-008` |
| `C2-019` | successful absence | Provider operation succeeds and certified endpoint semantics establish no observations. | SUCCESS+NO_DATA is permitted but does not automatically establish C1 NO_MATCH. | `contract` | `C2.DEC-009` |
| `C2-020` | partiality | Provider operation succeeds with a partial result and omitted/unavailable records. | Valid present observations may continue; missing records cannot prove absence/uniqueness. | `contract` | `C2.DEC-010` |
| `C2-021` | completeness | C1 exact NO_MATCH/uniqueness relies on the absence of competing provider observations. | Require scope-compatible C2 completeness/coverage dependency in addition to successful retrieval and other gates. | `contract` | `C2.DEC-011` |
| `C2-022` | positive exact mapping | A positive exact mapping is established without relying on absence of any competing universe item. | Do not require universe-wide enumeration solely by rule; other exactness gates still apply. | `contract` | `C2.DEC-012` |
| `C2-023` | normalization firewall | Provider SDK/native payload is passed directly to C1 canonical/domain truth. | Reject; provider native payload remains outside canonical truth and must cross validation/normalization boundary. | `dependency/schema` | `C2.DEC-013` |
| `C2-024` | vendor selection | C2.00 names Alpaca/Tushare/AKShare/other provider as canonical or freezes provider priority. | Reject; vendor/priority selection is not a C2.00 semantic decision. | `governance` | `C2.DEC-014`, `C2.DEC-023` |
| `C2-025` | route degradation | Primary route fails and fallback provider is used, but downstream lineage is emitted as clean primary with no material fallback reference. | Reject; preserve material provider/route fallback/degradation provenance. | `contract` | `C2.DEC-015` |
| `C2-026` | C3 degradation boundary | Cached/stale/LKG semantics are modeled as C2 provider-route degradation and C2 defines their rules. | Reject; preserve C3 ownership while retaining opaque provenance dependencies as needed. | `architecture` | `C2.DEC-015` |
| `C2-027` | credentials boundary | Provider API key/token/account private state appears in public C2 package/example/artifact. | Reject; secret/private state must remain behind credential boundary. | `security` | `C2.DEC-016` |
| `C2-028` | secure raw ingress | External response is immutably persisted as permitted raw before secret/PII/license/retention admission. | Reject; secure ingestion precedes permitted-raw immutability. | `security/storage` | `C2.DEC-017` |
| `C2-029` | untrusted content | Provider/web payload contains instruction text that changes route policy, grants capabilities or redirects a side-effect objective. | Treat as untrusted data; no control-state change or new/redirected side-effect intent. | `security` | `C2.DEC-018` |
| `C2-030` | replay lineage | Materialized C1-facing candidate/result lacks load-bearing provider operation/semantic/capability/completeness or material degradation refs needed to reconstruct production. | Reject as replay-safe materialization; preserve replay-critical C2 lineage. | `contract` | `C2.DEC-019` |
| `C2-031` | orthogonality | Provider SUCCESS is used as proof that C1 normalization/resolution, C4 PIT or C5 verification also succeeded. | Reject; each axis is independently evaluated by its owner. | `contract` | `C2.DEC-007`, `C2.DEC-020` |
| `C2-032` | open questions | A C2.01+ design question is placed in adopted decisions with a TBD value or silently assumed. | Reject; keep unresolved design in explicit OPEN questions with target stage. | `governance` | `C2.DEC-021` |
| `C2-033` | construction scope | C2.00 emits production adapter code, detailed provider endpoint registry/schema, routing algorithm, credential implementation, certification algorithm or machine contract schema. | Reject; C2.00 is scope/authority/vocabulary only. | `governance` | `C2.DEC-014`, `C2.DEC-021`, `C2.DEC-023` |
| `C2-034` | adjacent semantics | C2.00 solves C3 freshness/cache, C4 temporal visibility, C5 source fitness/conflict, or C11 persistence details while claiming convenience. | Reject; adjacent ownership boundaries remain explicit. | `architecture` | `C2.DEC-002`, `C2.DEC-021` |
| `C2-035` | traceability | A C2.00 acceptance obligation has no mapped decision, or a decision required_test points outside the C2.00 catalog. | Fail construction conformance; require bidirectional complete mapping. | `schema/conformance` | `C2.DEC-024` |
| `C2-036` | review gate | Construction report states PASS/FROZEN or proceeds to C2.01 without independent C2.00 review. | Reject; next gate is Independent Scope Review only. | `governance` | `C2.DEC-003`, `C2.DEC-024` |
| `C2-037` | side effects | C2.00 authorization is interpreted as permission for WRITE_EXTERNAL/PAPER_TRADE/LIVE_TRADE or other external side effect. | Reject; production and external side effects remain unauthorized. | `security/governance` | `C2.DEC-003`, `C2.DEC-016`, `C2.DEC-018`, `C2.DEC-023` |
| `C2-038` | source fitness | C2 routing/certification declares a provider source fit for a load-bearing claim merely because capability exists. | Reject; claim/source fitness and verification belong to C5. | `contract` | `C2.DEC-002` |
| `C2-039` | machine failure | Critical provider/tool failure exists only as human-readable text with no typed error/machine failure status. | Reject; failure must be machine-detectable independently of prose. | `provider-contract` | `C2.DEC-008` |
| `C2-040` | ports boundary | Core domain/application imports provider SDK/client-specific infrastructure directly instead of depending on a provider port/contract boundary. | Reject per C0-052 / canonical ports boundary. | `static/architecture` | `C2.DEC-013` |
| `C2-041` | load-bearing repository evidence | A future C2 load-bearing decision cites repository evidence through an unpinned branch/latest path, unresolved exact file, blob mismatch, or source with no role/authority scope. | Reject as load-bearing authority; require exact repository+commit+path/blob resolution and role/scope per C0-060. | `governance/remote-conformance` | `C2.DEC-026` |
| `C2-042` | permitted raw immutability | A response has passed secure ingestion and become a Permitted RawArtifact, then later content is overwritten in place while retaining the same identity. | Reject; admitted raw content is immutable by identity and mutation must produce a new content identity, while C11 retains persistence implementation ownership. | `storage` | `C2.DEC-017` |
| `C2-043` | failed/cancelled normalization gate | Provider operation status is FAILED or CANCELLED while C1 normalization runs or an empty normalized result is promoted as absence. | Reject; normalization is NOT_RUN and no infrastructure/cancellation state may masquerade as NO_DATA/NO_MATCH. | `contract` | `C2.DEC-025` |

## Coverage Contract

```text
C2.00 acceptance obligations: 43
range: C2-001..C2-043
unique IDs: 43
unmapped obligations: 0
C2.00 decisions: 26
decisions with zero required tests: 0
```

Every acceptance obligation maps to at least one C2.00 candidate decision, and every candidate decision maps to one or more obligations. Independent review must re-check semantics, not merely counts.

C2.00 does not authorize executable provider code or production test fixtures.
