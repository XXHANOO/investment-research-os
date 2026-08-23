# C2.00 — Scope / Authority / Vocabulary Candidate

Generated: 2026-08-23T22:15:59Z

Status: `CANDIDATE_FOR_C2_00_INDEPENDENT_SCOPE_REVIEW`

Production implementation: `NOT_AUTHORIZED`

Independent C2.00 verdict: `NOT_PERFORMED`

## 1. Stage Authorization and Authority Classes

The exact bundled stage-plan snapshot remains byte-identical:

```text
C2_PROPOSED_STAGE_PLAN.yaml
sha256:b7a4f2a3958417f155e24109edaf025c017d7fc8ac7980ff9765c90fe97e70d6
```

Its embedded status (`PROPOSED_NOT_FROZEN_NOT_YET_ADOPTED`) records the handoff state at the time that immutable snapshot was emitted. In the current chat, the user explicitly adopted that exact proposed stage sequence and authorized **C2.00 only**. The plan is therefore **adopted as the C2 governance workflow**, but it is **not promoted into inherited C0/C1 frozen contract authority** and its bytes are not mutated to rewrite history.

Three authority classes are distinct:

1. **Frozen inherited authority** — C0, C1, and the exact C1.05R1 downstream interface.
2. **User-adopted C2 workflow authority** — the exact stage sequence in the bundled C2 stage-plan snapshot.
3. **C2.00 candidate semantics** — the material in this artifact, which has no authority beyond candidate status until an independent C2.00 review passes.

No C2.01+ construction and no production implementation is authorized by this artifact.

## 2. Exact Parent Authority Pins

| Parent | Exact artifact | SHA-256 | Authority used by C2.00 |
|---|---|---|---|
| Frozen C0 | `C0_FROZEN.md` | `9585df6c0fbdb2cc40bc38571f8452b51f8ca69c9fd9432b10b87490b08a3b6f` | C2 responsibility map, provider failure/normalization/security/ports invariants |
| C0 freeze state | `C0_FREEZE_SEAL.yaml` | `eb2e11d4c425fee121feedc7ea6c4270722c85398afdab35917cbd6f667d93a2` | Current frozen/authorization state of C0 |
| C0 acceptance catalog | `C0_ACCEPTANCE_TEST_CATALOG.md` | `8d5d7f45bd79cd3617968b6ebfbe1d0ddeb1956b7cf80cfcb285ebc4317de27c` | Provider/security/governance acceptance obligations |
| C0 evidence ledger | content-addressed C0 ledger | `abfa03aaa200bdd355de0a37d960b040fcb44c7b52696adcbebe8028420d5155` | Machine-governed C0 authority/evidence chain |
| Frozen C1 | C1 freeze seal | `438274542570f7398af8622fdb511b85d69fc4c403b246b93a8a593b5d8070a5` | C1 frozen state and exact downstream dependency set |
| C1 final schema | content-addressed final machine schema | `927f1916d3b4b0c0600c1988d6cff0c91dfaaf840b676ce8b6f6f86cb61e52d4` | Frozen C1 machine-interface continuity only |
| C1.05R1 interface | provider-normalization interface | `71d472e63044b9a7be2c6cc831705ed80dc6a06ccd0ef03e71a0618794bdef63` | Non-negotiable C1→C2 requirements |
| C1.05R1 registry | provider-normalization registry | `422010036a00ad0d1fbfa4176ae27f107fec4761a92c0f0ad5b7db29eed2379b` | Exact C1-facing foreign-reference/outcome requirements |
| C1.05R1 ledger | evidence/decision ledger | `47315933c5369aa1aa3a9719874dee31348335efa1a2120677747ab7c9a47031` | C1.05R1 adopted interface decisions |
| C1.05R1 tests | acceptance delta | `bbf23c97dbab72844956fd6a751c63ba13eba2857fcf4bb62faa875709bc5b83` | Frozen regression obligations C1-331..337 and predecessors |
| C2 start manifest | `C2_START_AUTHORITY_MANIFEST.yaml` | `316a17cda14058322999095036951647824a69bd0037e78b7eea810f6a76062d` | Curated C2 start authority and forbidden patterns |
| C2 handoff | `PROJECT_HANDOFF_C2_START.md` | `85e94ae4156279576e6e52518179fdf44392bfddd63946dbdc17cf938a44457b` | C2.00 construction rules and stop gate |
| Adopted workflow snapshot | `C2_PROPOSED_STAGE_PLAN.yaml` | `b7a4f2a3958417f155e24109edaf025c017d7fc8ac7980ff9765c90fe97e70d6` | Stage sequencing only; not C0/C1-frozen semantics |

C2.00 does not alter any parent artifact.

## 3. Purpose

C2 is the **Provider / Source Router / Provider Certification** contract.

C2.00 defines only:

- the authority boundary of C2;
- the minimum vocabulary needed for later C2 contract stages;
- cross-contract ownership seams;
- inherited non-negotiable constraints;
- explicit unresolved questions and their intended later stages;
- stage-level acceptance and traceability requirements.

C2.00 intentionally does **not** define provider-specific endpoints, concrete routing algorithms, credential technology, detailed error schemas, completeness algorithms, provider priorities, or production adapters.

## 4. Core Boundary

C2 owns **what a provider/source interface can semantically supply, how an eligible provider route is selected, what the provider operation outcome means, what provider-side certification/coverage state supports that result, and where provider credentials enter the boundary**.

C2 does not own the downstream truth those observations may eventually support.

A compact ownership statement is:

```text
C1  = what canonical financial object / identity assertion is being discussed
C2  = which provider/source capability is eligible, selected, certified, and what happened at that provider boundary
C3  = cache/quota/freshness/coalescing/last-known-good semantics
C4  = exact temporal/PIT/revision/available_from semantics
C5  = evidence/source-fitness/verification/conflict semantics
C6  = tool/capability/policy and trusted-intent enforcement
C7  = orchestration, durable tasks, budgets, cancellation
C11 = persistence implementation and repository ownership
C12 = validation/promotion/release authority
```

C2 MUST NOT acquire another contract's semantic authority merely because a provider adapter exposes convenient fields for it.

## 5. Ownership / Boundary Matrix

| Concept | Owner | C2 responsibility | C2 must not do |
|---|---|---|---|
| Canonical Entity/Instrument/Listing/Contract identity | C1 | Carry opaque C1 refs/context where needed | Mint, merge, rewrite, or redefine C1 identity |
| Provider profile / field semantics | C2 | Define provider-side semantic state and stable references in later stages | Treat mutable provider docs/README claims as replay-stable authority |
| Provider capability / endpoint semantics | C2 | Define what operation/scope a provider endpoint is certified to support | Infer C1 canonical meaning solely from a vendor-native object |
| Provider/source routing | C2 | Select among semantically eligible provider/source capabilities | Define C5 claim/source fitness or C3 cache/quota policy |
| Provider operation status / structured failures | C2 | Emit machine-detectable operation outcome semantics | Convert failures to empty/NO_DATA or text-only failure |
| Provider data outcome | C2 | Distinguish PRESENT / NO_DATA / PARTIAL where operation semantics permit | Treat data outcome as the same axis as operation status |
| Provider completeness / coverage attestation | C2 | Provide scope-matched certification dependencies used when absence/uniqueness is load-bearing | Decide C1 NO_MATCH or C5 verification strength |
| Provider routing fallback/degradation provenance | C2 for route/provider-originated degradation; C3 for cache/LKG/freshness degradation | Preserve material route/fallback lineage across boundary | Relabel degraded fallback as clean primary or absorb C3 LKG semantics |
| Credentials ingress boundary | C2 at provider boundary; C6 owns capability/policy authority | Define later how credentials are safely supplied to provider adapters | Store public secrets, grant tool capabilities, or authorize trading/side effects |
| Secure raw ingestion handoff | C2 boundary + C11 persistence implementation | Ensure external response crosses security/licensing/privacy admission before permitted-raw persistence | Persist external raw immutably before checks or redefine C11 storage semantics |
| Cache / quota / freshness / coalescing / LKG | C3 | Consume/emit opaque C3 state where interface requires | Define TTL, staleness, quota scheduler, cache key, LKG selection |
| Exact PIT / revision / available_from | C4 | Carry opaque C4 refs where required | Invent timestamps, visibility, revision or reconstructability rules |
| Evidence / provenance graph / source fitness / verification / conflict | C5 | Preserve source/provenance identifiers needed downstream | Rank source fitness, certify truth, adjudicate conflicting claims |
| Canonical persistence / repositories | C11 | Define semantic records/references that C11 may persist | Choose/redefine persistence semantics or make report files authoritative stores |
| Tool capability / trusted intent | C6 | Remain subordinate to granted capability and destination policy | Let provider content grant capabilities or originate/redirect side-effect intent |
| Workflow budget/cancellation | C7 | Return typed outcomes that orchestration can act upon | Own task orchestration or budget semantics |
| Release / validation | C12 | Supply candidate artifacts for later validation | Self-approve, self-freeze, or self-release C2 |

## 6. Vocabulary Candidate

These terms establish a shared language only. Detailed schemas and algorithms belong to later C2 stages.

### 6.1 Provider

An external system/operator/API/feed/tool boundary through which the OS attempts a typed data operation.

A provider is **not automatically the underlying evidentiary source**. A provider may redistribute or transform material originating elsewhere.

### 6.2 Source

The underlying origin/publication/authority lineage associated with obtained material. Provider and source MAY coincide, but C2 MUST NOT assume they are identical.

C2 may route to a provider/source channel. C5, not C2, determines whether that source is fit for a particular claim.

### 6.3 Endpoint / Provider Operation Surface

A provider-defined callable operation or endpoint whose request, response, pagination, field, and absence semantics may differ from other operations of the same provider.

Endpoint semantics must not be inferred globally from the provider name.

### 6.4 Provider Semantic Profile

A C2-owned semantic snapshot describing provider/endpoint interpretation needed by downstream normalization or replay. When load-bearing, its reference must resolve to snapshot-stable state.

The exact record schema is deferred to C2.01.

### 6.5 Provider Field Semantic Binding

A C2-owned description of what a provider-native field means in a defined provider/endpoint context. It is not a C1 normalization rule and cannot itself mint canonical identity.

When load-bearing to C1 normalization, its reference must be snapshot-stable.

### 6.6 Provider Capability

A C2-owned, explicitly scoped statement that a provider/endpoint is capable of an operation or semantic coverage class under declared conditions.

Capability is not equivalent to source fitness, truth verification, cache availability, or execution permission.

### 6.7 Provider Certification

A C2-owned attestation about provider capability/endpoint semantics/coverage established under C2 governance. Certification does not mean that a resulting financial claim is C5 `VERIFIED`.

The certification model is deferred to C2.05.

### 6.8 Coverage / Completeness Attestation

A C2-owned, scope-specific dependency describing the extent to which an operation can support absence or uniqueness reasoning under certified endpoint semantics.

It is **not** a generic quality score and is **not** automatically required for a positive exact mapping when exactness does not depend on absence.

The scope language and certification method are deferred to C2.05.

### 6.9 Provider Operation

One attempted interaction with a provider operation surface, identified by a replay/audit reference.

C0 freezes the top-level operation-status axis:

```text
SUCCESS | FAILED | CANCELLED
```

Detailed typed failure families are deferred to C2.02, but failures must be structured and machine-detectable.

### 6.10 Data Outcome

The semantic result of a successful operation, kept orthogonal to operation status. C0 freezes the top-level vocabulary:

```text
PRESENT | NO_DATA | PARTIAL
```

`NO_DATA` is meaningful only where endpoint semantics establish genuine absence. `PARTIAL` must preserve partiality/degradation semantics.

### 6.11 Provider Observation

A provider-derived observation admitted across the provider-validation boundary for downstream normalization. It is candidate material, not canonical C1 truth.

The exact C1-facing observation categories are inherited from C1.05R1 and are not redefined by C2.00.

### 6.12 Routing Decision

A C2-owned decision to select an eligible provider/source capability for a requested semantic need. Exact candidate eligibility, ordering, fallback, retry, and degradation rules are deferred to C2.03.

Routing does not decide C5 source fitness and must not silently choose a concrete vendor in C2.00.

### 6.13 Fallback / Degradation

A material change from the preferred/initial provider route or operation quality that can affect interpretation, coverage, or provenance.

C2-originated provider/route degradation must remain explicit. C3-owned cache/stale/LKG degradation remains C3 semantic state; C2 must not absorb it.

### 6.14 Credential Boundary

The C2 boundary through which provider authentication material is supplied to an adapter without becoming public contract data. It does not grant tool/execution capability and it does not authorize PAPER/LIVE/external side effects.

Exact secret-management mechanics are deferred to C2.04.

### 6.15 Secure Ingress Boundary

The pre-persistence boundary at which external response material is checked for secret/credential leakage, privacy/PII constraints, licensing/redistribution constraints, retention classification, and quarantine/redaction/rejection needs before it becomes a permitted raw artifact.

C11 owns persistence implementation; C2.00 does not specify a storage product.

### 6.16 Snapshot-Stable Reference

A reference that resolves the same load-bearing semantic state during replay/audit. A version, immutable snapshot ID, content address, or equivalent mechanism may satisfy this property; a floating `latest` alias does not.

At minimum, C1.05R1 requires snapshot-stability when load-bearing for:

```text
provider_profile_ref
provider_field_semantic_refs[]
provider_capability_ref
c2_completeness_refs[]
```

### 6.17 Replay-Critical Lineage

The set of immutable/stable references needed to reconstruct why materialized downstream normalized candidate/result semantics were produced. C2 must preserve its load-bearing provider-operation, provider-semantic/capability/completeness, and material fallback/degradation dependencies so C1 can satisfy its frozen replay-lineage contract.

### 6.18 Orthogonal Outcome Axes

C2.00 recognizes, but does not collapse, these distinct axes:

```text
provider operation status       # C2
data outcome                    # C2
normalization result            # C1
identity resolution result      # C1
cache/freshness/LKG state       # C3
PIT/reconstructability state    # C4
verification/conflict state     # C5
```

A convenience enum MUST NOT merge these axes.

## 7. Inherited C0 Constraints C2 Must Preserve

The C2 start manifest names these mandatory C0 acceptance obligations:

```text
C0-008  HTTP/server/auth/network failure is not NO_DATA
C0-009  rate-limit exhaustion fails loud
C0-010  provider-established genuine absence may be NO_DATA
C0-011  operation status and data outcome are separate
C0-014  provider payload cannot bypass canonical normalization
C0-049  security/privacy admission precedes immutable permitted-raw storage
C0-050  admitted permitted raw content is immutable by content identity
C0-051  claim/source fitness belongs to C5 policy
C0-052  domain/application cannot directly import provider infrastructure
C0-057  untrusted external content cannot originate/redirect side-effect intent
C0-060  load-bearing repository evidence is exact-path/blob pinned and authority-scoped
```

C2 also preserves the provider-relevant forbidden patterns pinned by the C2 start manifest:

```text
F-04  provider failure converted to empty/no-data
F-06  flat status enum collapsing orthogonal state axes
F-13  failure represented only by natural-language text
F-19  secrets/private state committed to public artifacts
F-20  external response persisted immutably before secure-ingestion checks
F-25  external content granting capabilities or changing control policy
F-33  external data originating/redirecting side-effect intent
```

## 8. Frozen C1.05R1 Downstream Constraints

C2.00 adopts these as non-negotiable inherited interface requirements, not new C2 inventions:

1. load-bearing C2 semantic/capability/completeness references used by C1 must be snapshot-stable;
2. materialized normalized candidates/results require replay-critical lineage;
3. material provider-route fallback/degradation provenance cannot be erased;
4. `FAILED` / `CANCELLED` implies C1 normalization `NOT_RUN`;
5. `SUCCESS + NO_DATA` means successful provider operation yielded no observations under certified endpoint semantics and does not automatically prove C1 `NO_MATCH`;
6. `SUCCESS + PARTIAL` may yield valid normalized records, but missing records cannot prove absence or uniqueness;
7. load-bearing exact absence/uniqueness requires a scope-compatible C2 completeness/coverage dependency;
8. provider/data/normalization/resolution/PIT/verification axes remain orthogonal;
9. positive exact mapping may remain valid without universe-wide enumeration when exactness does not depend on absence.

C2 will define its own provider capability/certification/completeness records in later stages without redefining C1 canonical identity semantics.

## 9. C2.00 Candidate Decisions

C2.00 decides only the following scope-level propositions:

1. C2's role is Provider / Source Router / Provider Certification.
2. Provider, source, endpoint, capability, certification, completeness, operation, data outcome, routing, degradation, credential boundary, and secure ingress are distinct concepts.
3. C2 owns provider-side semantic/capability/certification/routing/outcome records, but not C1/C3/C4/C5/C11 semantics.
4. C2 credential handling does not imply C6 capability grants or side-effect authorization.
5. Load-bearing C2 references consumed by frozen C1 must be snapshot-stable and replayable.
6. Provider failures, successful absence, and partial results remain semantically distinct.
7. Exact absence/uniqueness may depend on C2 completeness; positive exact mapping need not always do so.
8. Raw/provider-native objects cannot bypass validation/normalization into canonical domain truth.
9. Provider/route fallback provenance that materially changes semantics cannot be erased.
10. C2.00 does not select vendors or define production provider adapters.
11. The adopted C2 stage sequence is workflow authority only and is not C0/C1-frozen authority.
12. Production implementation and external/PAPER/LIVE side effects remain unauthorized.
13. `FAILED` or `CANCELLED` upstream provider operations imply downstream C1 normalization `NOT_RUN`; neither can be converted into absence.
14. Load-bearing C2 repository evidence remains subject to C0-060 exact repository/commit/path/blob pinning and authority-scope discipline.

## 10. Open Questions — Explicitly Not Decisions

| Open ID | Question | Target stage |
|---|---|---|
| `C2.OPEN-001` | What is the exact provider capability taxonomy and capability granularity? | C2.01 |
| `C2.OPEN-002` | What is the exact endpoint-semantic/profile record and field-semantic binding model? | C2.01 |
| `C2.OPEN-003` | How are capability compatibility and endpoint semantic versions represented as snapshot-stable refs? | C2.01 |
| `C2.OPEN-004` | What are the detailed structured provider failure/error families beneath SUCCESS/FAILED/CANCELLED? | C2.02 |
| `C2.OPEN-005` | What exact operation-specific rules make PRESENT/NO_DATA/PARTIAL legal and internally consistent? | C2.02 |
| `C2.OPEN-006` | What are route eligibility, selection, retry, fallback and provider-originated degradation semantics? | C2.03 |
| `C2.OPEN-007` | Where is the exact retry/quota seam between C2 provider retry/fallback and C3 quota/backoff state? | C2.03 / C2.06 |
| `C2.OPEN-008` | What exact credential/private-state/secure-ingress contract supplies secrets without public persistence? | C2.04 |
| `C2.OPEN-009` | What are the provider certification states, certification evidence requirements and invalidation rules? | C2.05 |
| `C2.OPEN-010` | What scope language and methodology make a completeness/coverage attestation strong enough for load-bearing absence/uniqueness? | C2.05 |
| `C2.OPEN-011` | How is certification/coverage temporal validity represented without C2 inventing C4 `available_from`/revision semantics? | C2.05 / C2.06 |
| `C2.OPEN-012` | What exact opaque reference interfaces are exchanged with C1/C3/C4/C5, including degradation and replay dependencies? | C2.06 |
| `C2.OPEN-013` | What is the exact C2→C11 permitted-raw/repository handoff without transferring semantic ownership to persistence? | C2.06 |
| `C2.OPEN-014` | What machine schema, validators and executable contract-test vectors encode C2 semantics? | C2.07 |
| `C2.OPEN-015` | Which concrete providers/vendors are enabled and what operational priority/configuration do they receive? This is not a C2.00 semantic decision and must not be silently selected. | post-contract configuration / ADR, subject to later C2 semantics |

An OPEN item MUST NOT be represented as an adopted semantic decision merely to make construction appear complete.

## 11. Hard Red Lines at C2.00

C2.00 forbids:

```text
provider failure -> [] -> NO_DATA
FAILED + authoritative NO_DATA
CANCELLED + normalization runs
one flat status mixing failure/data/cache/PIT/verification
provider README/latest docs as mutable load-bearing semantic authority
floating latest provider_profile/capability/completeness ref supporting deterministic replay
SUCCESS+NO_DATA -> automatic C1 NO_MATCH
SUCCESS+PARTIAL -> proof of absence/uniqueness
raw SDK/provider object -> canonical C1 truth
provider-native ID -> canonical identity by definition
provider fallback -> clean-primary provenance
C2 route degradation absorbing C3 stale/cache/LKG semantics
C2 completeness certification -> C5 VERIFIED claim
C2 credentials -> C6 capability grant
provider/web payload -> new/redirected side-effect objective
secret/private state -> public repository/package/example
external response -> immutable raw store before secure-ingress checks
permitted raw artifact -> in-place content overwrite under same identity
load-bearing repository evidence -> floating branch/path or blob-mismatched authority
C2 defining C4 available_from/revision/PIT rules
C2 defining C5 source-fitness/conflict rules
C2 defining C3 TTL/quota/cache/LKG rules
C2 defining C11 database/storage implementation
production Alpaca/Tushare/AKShare/etc adapter construction
vendor priority selection as if frozen semantics
PAPER/LIVE/external side-effect authorization
self-approval / self-freeze
```

## 12. C2.00 Exit Gate

C2.00 construction is a candidate only.

The next exact gate is:

```text
C2.00 Independent Scope Review
```

That independent review must determine whether the candidate:

- preserves every pinned C0/C1 boundary;
- does not weaken the exact C1.05R1 interface;
- keeps open questions machine-distinct from adopted candidate decisions;
- does not absorb C3/C4/C5/C11 or C6/C7/C12 authority;
- does not select implementation vendors;
- keeps production implementation and side effects unauthorized;
- has complete decision↔acceptance traceability.

C2.01 MUST NOT begin before an independent PASS or an explicitly scoped repair/re-check sequence.
