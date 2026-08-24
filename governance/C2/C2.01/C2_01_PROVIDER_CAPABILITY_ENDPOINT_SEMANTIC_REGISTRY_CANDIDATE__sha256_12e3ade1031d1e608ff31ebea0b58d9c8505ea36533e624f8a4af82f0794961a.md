# C2.01 — Provider Capability & Endpoint Semantic Registry Candidate

Generated: 2026-08-24T01:11:00Z

Status: `CANDIDATE_FOR_C2_01_INDEPENDENT_CAPABILITY_REVIEW`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

C2.01 independent verdict: `NOT_PERFORMED`

## 1. Authorization and Stage Boundary

The user explicitly authorized **C2.01 construction** after C2.00 independently passed scope review. C2.01 is the adopted-workflow stage:

```text
C2.01 — Provider Capability & Endpoint Semantic Registry
Gate: Independent Capability Review
```

C2.01 resolves only `C2.OPEN-001`, `C2.OPEN-002`, and `C2.OPEN-003` at candidate level. It does not construct C2.02 typed provider outcome/error semantics, C2.03 routing algorithms, C2.04 credential mechanics, C2.05 certification/completeness methodology, C2.06 cross-contract wire interfaces, C2.07 final machine schemas, or any production provider adapter.

C2.00 remains `REVIEW_PASSED_NOT_FROZEN`; this C2.01 candidate does not retroactively freeze C2.00.

## 2. Parent Authority Pins

| Parent authority | SHA-256 | Use in C2.01 |
|---|---|---|
| C0 frozen contract | `9585df6c0fbdb2cc40bc38571f8452b51f8ca69c9fd9432b10b87490b08a3b6f` | Provider-failure/security/ports invariants |
| C0 freeze seal | `eb2e11d4c425fee121feedc7ea6c4270722c85398afdab35917cbd6f667d93a2` | Frozen state |
| C1 freeze seal | `438274542570f7398af8622fdb511b85d69fc4c403b246b93a8a593b5d8070a5` | C1 frozen boundary |
| C1 final machine schema | `927f1916d3b4b0c0600c1988d6cff0c91dfaaf840b676ce8b6f6f86cb61e52d4` | Frozen C1 interface continuity |
| C1.05R1 provider-normalization interface | `71d472e63044b9a7be2c6cc831705ed80dc6a06ccd0ef03e71a0618794bdef63` | Non-negotiable C1-facing C2 refs and replay constraints |
| C1.05R1 provider-normalization registry | `422010036a00ad0d1fbfa4176ae27f107fec4761a92c0f0ad5b7db29eed2379b` | C1-facing observation/outcome categories |
| C1.05R1 evidence/decision ledger | `47315933c5369aa1aa3a9719874dee31348335efa1a2120677747ab7c9a47031` | Adopted downstream decisions |
| C1.05R1 acceptance delta | `bbf23c97dbab72844956fd6a751c63ba13eba2857fcf4bb62faa875709bc5b83` | Frozen regression obligations |
| C2 start authority | `316a17cda14058322999095036951647824a69bd0037e78b7eea810f6a76062d` | C2 ownership boundary |
| User-adopted C2 stage-plan snapshot | `b7a4f2a3958417f155e24109edaf025c017d7fc8ac7980ff9765c90fe97e70d6` | Workflow sequence only |
| C2.00 scope candidate | `b504211651839b1cd9c79a9706f05e1ad9c072f66bfb887aec2a0d65c9b17cf7` | Reviewed C2 vocabulary/boundary |
| C2.00 independent review report | `4a9d85bc99a0190b4a970b0f22723b4f7914d43a262a77e91a232399b41dbdb0` | Prior-stage PASS evidence |
| C2.00 independent review result | `6f42d8b29f0b5c15bd7cea0a053938364ddc431bd654b8601001118189a10c96` | `PASS / REVIEW_PASSED_NOT_FROZEN` |

No parent artifact is modified by C2.01.

## 3. C2.01 Design Principle — Capability Is a Static Semantic Contract

A **Provider Capability Definition** is an immutable semantic declaration that a specific provider operation surface can represent a specific class of request and produce a specific class of provider observations under pinned endpoint semantics.

It is **not** any of the following:

```text
current provider health or availability
credential possession or entitlement
quota/budget/backoff state
cache/freshness/LKG state
source fitness or verification strength
PIT/reconstructability guarantee
historical completeness certification
routing priority
production-adapter enablement
permission to perform side effects
```

Those remain C3/C4/C5/C6/C7/C2.03/C2.04/C2.05 or configuration concerns as already frozen/scoped.

## 4. Capability Granularity

C2.01 adopts the following granularity rule **at candidate level**:

> One capability record describes **one provider semantic operation surface × one access-pattern family × one query-signature contract × one produced observation-family set × one response-semantic contract**.

A physical endpoint MUST be represented by more than one capability record when request modes materially change:

- query interpretation;
- output record meaning;
- response cardinality/collection semantics;
- provider-native absence signals;
- field meaning/unit/sentinel semantics;
- pagination/truncation behavior;
- provider-native temporal-filter interpretation.

A broad provider-level statement such as “Provider X supports historical data” is not a valid capability record.

## 5. Capability Taxonomy

C2.01 uses an **access-pattern taxonomy** plus pinned semantic dimensions. The access-pattern family is not a canonical financial-object hierarchy.

### 5.1 Access-pattern families

```text
DIRECT_LOOKUP
SEARCH
ENUMERATION
SNAPSHOT_FETCH
WINDOWED_SERIES_FETCH
EVENT_COLLECTION_FETCH
DOCUMENT_DISCOVERY
DOCUMENT_RETRIEVAL
BULK_EXPORT
STREAM_SUBSCRIPTION
```

Normative meanings:

| Family | Provider-side meaning | Explicit non-meaning |
|---|---|---|
| `DIRECT_LOOKUP` | Request by one or more provider-native exact lookup keys/tuples | Does not mean C1 exact identity resolution |
| `SEARCH` | Provider-native ranked/fuzzy/text/criteria search | Does not mean unique canonical match |
| `ENUMERATION` | Traverse a provider-declared collection according to endpoint collection semantics | Does not itself certify completeness; C2.05 owns that |
| `SNAPSHOT_FETCH` | Obtain provider observations presented as a current/request-boundary snapshot | Does not imply C4 PIT safety or `available_from` |
| `WINDOWED_SERIES_FETCH` | Obtain provider-native observations constrained by a provider-native range/window | Does not establish C4 reconstructability |
| `EVENT_COLLECTION_FETCH` | Obtain provider-native event records | Does not decide C1 identity effects or C5 truth |
| `DOCUMENT_DISCOVERY` | Discover provider-indexed document descriptors | Does not establish document/source fitness |
| `DOCUMENT_RETRIEVAL` | Retrieve a provider-identified document/content object | Does not authorize immutable persistence before secure ingress |
| `BULK_EXPORT` | Obtain a provider-declared bulk dataset/export object | Does not prove exhaustive universe coverage |
| `STREAM_SUBSCRIPTION` | Subscribe to provider-pushed observations | Does not grant orchestration or external side-effect authority |

### 5.2 Observation-family dimension

For the frozen C1-facing boundary, capability records may produce the exact interface categories already accepted by C1.05R1:

```text
IDENTITY_DESCRIPTOR_OBSERVATION
REGISTERED_IDENTIFIER_OBSERVATION
SYMBOL_OBSERVATION
LISTING_OBSERVATION
CONTRACT_OBSERVATION
CONTRACT_VENUE_ADMISSION_OBSERVATION
CORPORATE_ACTION_EVENT_OBSERVATION
CORPORATE_ACTION_RELATION_OBSERVATION
TERMS_OBSERVATION
```

C2 may also serve non-C1 consumers. C2.01 therefore permits additional C2 provider-observation families, but they MUST remain provider-side observation semantics and MUST NOT mint canonical C1 identity objects or C5 truth states. Initial vendor-neutral families are:

```text
MARKET_OBSERVATION
FUNDAMENTAL_OBSERVATION
DOCUMENT_DESCRIPTOR_OBSERVATION
DOCUMENT_CONTENT_OBSERVATION
PROVIDER_REFERENCE_OBSERVATION
```

Adding/changing an observation-family definition is load-bearing registry change and requires a new snapshot-stable semantic state.

## 6. Exact Logical Record Model

C2.01 defines logical semantic records. C2.07 remains owner of final JSON Schema/wire serialization/validator code.

### 6.1 `C2StableSemanticRef`

Every load-bearing C2.01 semantic reference logically contains:

```text
C2StableSemanticRef:
  authority: C2
  ref_kind
  logical_id
  semantic_revision
  content_sha256
```

Allowed `ref_kind` values at this stage:

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

Rules:

1. `content_sha256` binds the exact semantic payload represented by the ref.
2. `semantic_revision` is human/audit-friendly but is not sufficient without immutable content identity for load-bearing replay.
3. A floating alias (`latest`, `current`, mutable registry key) MAY be a convenience lookup but MUST NOT be persisted as the load-bearing ref.
4. Supersession creates a new ref; it never mutates the old semantic payload in place.
5. Exact canonical serialization/hash-verification mechanics are deferred to C2.07, but the semantic identity tuple above is already mandatory.

### 6.2 `ProviderSemanticProfileDefinition`

```text
ProviderSemanticProfileDefinition:
  provider_profile_id
  semantic_revision
  provider_semantic_namespace
  adopted_provider_wide_semantic_refs[]
  provider_native_identifier_namespace_refs[]
  provider_native_subject_semantic_refs[]
  content_identity
```

Provider-wide defaults are never implicit. An endpoint profile MUST explicitly reference any provider-wide semantic ref it adopts. This prevents replay meaning from changing when a provider-wide “default” changes.

The provider profile MUST NOT contain credentials, routing priority, current health, quota state, C4 `available_from`, C5 source-fitness decisions, or C2.05 completeness certification.

### 6.3 `FieldSemanticDefinition`

```text
FieldSemanticDefinition:
  field_semantic_id
  semantic_revision
  provider_profile_ref
  provider_native_selector
  provider_native_meaning
  value_shape
  unit_scale_semantics
  null_missing_sentinel_semantics
  enumeration_semantics
  provider_native_timestamp_role
  source_record_grouping_semantics
  content_identity
```

`provider_native_timestamp_role` is descriptive only. Permitted candidate roles include:

```text
NOT_TEMPORAL
PROVIDER_EVENT_TIME
PROVIDER_OBSERVED_TIME
PROVIDER_EFFECTIVE_TIME_CLAIM
PROVIDER_PUBLISHED_TIME_CLAIM
PROVIDER_RETRIEVAL_METADATA_TIME
PROVIDER_OTHER_TIME
```

A timestamp role MUST NOT be promoted by C2 into C4 visibility, `available_from`, revision, effectivity, or PIT-safe semantics.

`null_missing_sentinel_semantics` describes provider-native representation only. It does not itself authorize C2.02 `NO_DATA` or C1 `NO_MATCH`.

### 6.4 `EndpointSemanticProfileDefinition`

```text
EndpointSemanticProfileDefinition:
  endpoint_profile_id
  semantic_revision
  provider_profile_ref
  endpoint_logical_id
  adopted_provider_wide_semantic_refs[]
  request_semantics:
    query_semantic_refs[]
    required_query_refs[]
    optional_query_refs[]
    mutually_exclusive_query_groups[]
    provider_native_defaulting_semantic_refs[]
  response_semantics:
    response_semantic_ref
    response_cardinality
    record_grouping_semantic_refs[]
    field_semantic_refs[]
    pagination_semantic_ref
    provider_native_absence_signal_refs[]
    provider_native_partiality_signal_refs[]
  content_identity
```

`response_cardinality` candidate values:

```text
ZERO_OR_ONE
ONE
COLLECTION
PAGED_COLLECTION
SERIES
EVENT_COLLECTION
DOCUMENT
BULK_OBJECT
STREAM
```

An endpoint semantic profile describes **what provider response elements mean**. It does not classify provider operation status/error families (C2.02), route eligibility/priority (C2.03), credentials (C2.04), completeness strength (C2.05), or current operational health.

Endpoint URLs, SDK class names, credential names and transport-client implementation details are not load-bearing semantic fields in this contract. Adapter binding may refer to the semantic profile later, not vice versa.

### 6.5 `ProviderCapabilityDefinition`

```text
ProviderCapabilityDefinition:
  capability_id
  semantic_revision
  provider_profile_ref
  endpoint_semantic_profile_ref
  access_pattern_family
  produced_observation_family_refs[]
  accepted_query_semantic_refs[]
  required_response_semantic_refs[]
  semantic_feature_refs[]
  compatibility_ruleset_ref
  content_identity
```

A capability record MUST NOT encode:

```text
priority / preferred provider
retry count / backoff / quota budget
credential secret or private entitlement value
current enabled/disabled health
claim/source fitness
verification/conflict strength
PIT/reconstructability conclusion
completeness/coverage certification strength
production adapter class or executable code
```

## 7. Field-semantic Binding Model

C2.01 resolves the C1-facing field-binding seam as follows:

```text
provider raw field selector
    ↓
C2 FieldSemanticDefinition (snapshot-stable)
    ↓
C1 NormalizationProfileDefinition.provider_field_semantic_refs[]
    ↓
C1 profile binds that provider semantic to a permitted C1 semantic slot
```

C2 describes the provider field. C1 decides whether and how that field can populate a C1 candidate assertion.

Therefore C2 field semantics MUST NOT directly name an internal `EntityID`, `InstrumentID`, `ListingID` or `ContractID` as the meaning of a provider-native value. A provider-native “permanent ID” remains a provider identifier observation unless C1 independently resolves/adopts it.

## 8. Capability Compatibility Model

C2.01 defines compatibility as a deterministic semantic predicate over pinned records, not a fuzzy provider score.

A capability requirement `R` is compatible with provider capability `P` only when **all** of the following hold under the same snapshot-stable registry state:

```text
1. R.access_pattern_family == P.access_pattern_family
2. R.required_observation_families ⊆ P.produced_observation_family_refs
3. R.required_query_semantics ⊆ P.accepted_query_semantic_refs
4. R.required_response_semantics ⊆ P.required_response_semantic_refs or
   are explicitly satisfied by P.endpoint_semantic_profile_ref
5. every required semantic feature is explicitly provided by P.semantic_feature_refs
6. every referenced semantic record resolves exactly and passes content-identity verification
7. no required semantic constraint is answered by implicit provider-wide default or by guessing
```

If the compatibility predicate cannot be proven from pinned semantic records, the capability is **not eligible as semantically compatible**. C2.03 may later define routing among compatible capabilities; it may not weaken this semantic compatibility predicate.

Compatibility does not mean:

```text
provider is online
credentials are available
quota is available
route should be selected
response will contain data
response will be complete
source is fit for a claim
result is PIT-safe or verified
```

## 9. Endpoint Semantic Change Rules

Any change that can alter interpretation of a request or observation requires a new semantic payload/ref. Examples include:

```text
provider-native identifier meaning changes
query parameter meaning/default changes
response record grouping changes
field unit/scale/sign changes
null/missing/sentinel meaning changes
enum value meaning changes
timestamp-role meaning changes
pagination/truncation semantics change
provider-native absence/partiality signal meaning changes
observation-family mapping eligibility changes
```

A transport-only implementation change that provably does not alter any C2 semantic record may use a different adapter binding without rewriting the semantic profile. C2.07 will define exact validator/canonicalization machinery.

## 10. Registry Snapshot Model

The C2.01 registry is itself snapshot-stable.

```text
ProviderCapabilitySemanticRegistrySnapshot:
  registry_id
  semantic_revision
  taxonomy_version
  compatibility_ruleset_ref
  provider_profile_refs[]
  endpoint_profile_refs[]
  field_semantic_refs[]
  capability_refs[]
  auxiliary_semantic_refs[]
  content_identity
```

At C2.01 contract-construction time, the **provider-instance lists remain empty by design**. This stage freezes no Alpaca, Tushare, AKShare, Serper, Bocha, Exa, or other vendor as canonical/priority configuration. Concrete provider enablement remains `C2.OPEN-015` post-contract configuration/ADR work.

The registry candidate therefore contains the normative taxonomy/record/compatibility model but no vendor selection.

## 11. C1.05R1 Referential Compatibility

C2.01 explicitly satisfies the frozen C1 requirements:

| C1.05R1 ref | C2.01 semantic target |
|---|---|
| `provider_profile_ref` | `C2StableSemanticRef(ref_kind=PROVIDER_SEMANTIC_PROFILE)` |
| `provider_field_semantic_refs[]` | `C2StableSemanticRef(ref_kind=FIELD_SEMANTIC)` |
| `provider_capability_ref` | `C2StableSemanticRef(ref_kind=CAPABILITY_DEFINITION)` |
| `c2_completeness_refs[]` | Reserved for C2.05; MUST use the same stable-ref discipline |

A capability definition pins its endpoint semantic profile and provider profile. If downstream replay load-bearing semantics depend on a field definition, the exact field-semantic refs remain separately retained as required by C1.05R1.

C2.01 does not redefine the exact C1.06/C2.06 wire serialization.

## 12. Provider-native Absence, Partiality and Pagination — Deliberate Boundary

C2.01 may describe provider-native signals such as:

```text
empty collection token
provider-declared not-found token
truncation flag
next-page cursor presence/absence
provider result-count semantics
field-level missing/sentinel representation
```

But C2.01 does **not** decide when those signals produce C2 `PRESENT`, `NO_DATA`, `PARTIAL`, `FAILED`, or `CANCELLED`. That is C2.02.

Likewise, describing an endpoint as enumerable/paginated does not certify that it covered a required universe. C2.05 owns completeness/coverage attestations.

## 13. Cross-contract Non-Absorption Rules

C2.01 MUST preserve these seams:

- **C1** — provider semantic refs may support normalization; C2 never mints canonical identity.
- **C3** — capability records do not include TTL, cache key, freshness, quota scheduler, retry budget, coalescing or LKG selection.
- **C4** — provider-native temporal filtering/timestamps are descriptive inputs only; no `available_from`, revision, visibility or PIT-safe conclusion.
- **C5** — provider/source identity is not source fitness, claim verification, or conflict adjudication.
- **C6/C7** — capability registry entries do not grant tools, trusted intent, workflow budgets or external-action authority.
- **C11** — registry semantics do not choose persistence technology or authorize raw persistence before secure ingress.
- **C12** — this candidate does not self-validate, self-freeze or self-release.

## 14. Candidate Resolution of C2.00 Open Items

### `C2.OPEN-001` — candidate closed

**Question:** exact provider capability taxonomy and granularity.

**Candidate resolution:** access-pattern taxonomy in §5 plus the one-surface/one-signature capability granularity rule in §4 and the exact `ProviderCapabilityDefinition` in §6.5.

### `C2.OPEN-002` — candidate closed

**Question:** exact endpoint-semantic/profile record and field-semantic binding model.

**Candidate resolution:** `ProviderSemanticProfileDefinition`, `FieldSemanticDefinition`, `EndpointSemanticProfileDefinition`, `ProviderCapabilityDefinition`, and the C2-field → C1-profile binding model in §§6–7.

### `C2.OPEN-003` — candidate closed

**Question:** snapshot-stable capability compatibility and endpoint-semantic version representation.

**Candidate resolution:** `C2StableSemanticRef` tuple, immutable registry snapshot model, explicit semantic-change rules, and deterministic compatibility predicate in §§6.1, 8–10.

These are **candidate closures only** until Independent Capability Review passes.

## 15. Still-Open Items

The following remain explicitly unresolved and MUST NOT be inferred from C2.01:

```text
C2.OPEN-004 detailed provider failure/error families                    → C2.02
C2.OPEN-005 legality/consistency rules for PRESENT/NO_DATA/PARTIAL      → C2.02
C2.OPEN-006 route selection/retry/fallback/degradation                  → C2.03
C2.OPEN-007 C2 retry vs C3 quota/backoff seam                           → C2.03/C2.06
C2.OPEN-008 credential/private-state/secure-ingress mechanics           → C2.04
C2.OPEN-009 certification states/evidence/invalidation                  → C2.05
C2.OPEN-010 completeness/coverage methodology                           → C2.05
C2.OPEN-011 certification temporal validity vs C4                       → C2.05/C2.06
C2.OPEN-012 exact opaque cross-contract interfaces                      → C2.06
C2.OPEN-013 C2→C11 permitted-raw handoff                                → C2.06
C2.OPEN-014 final machine schema/validators/contract vectors            → C2.07
C2.OPEN-015 concrete provider enablement/priority/configuration         → post-contract ADR/config
```

## 16. Hard Red Lines at C2.01

Forbidden by this candidate:

```text
provider-level marketing claim used as endpoint capability truth
one provider-global endpoint semantic profile covering materially different operations
capability = current provider health/credential/quota/certification
implicit/fuzzy semantic compatibility
floating latest ref used as load-bearing provider semantic authority
provider-wide defaults inherited without explicit stable ref
provider-native field directly declared a canonical C1 ID
provider-native timestamp declared C4 available_from/PIT-safe
endpoint enumeration declared completeness proof
provider-native empty response automatically declared C2 NO_DATA
provider partiality signal automatically declared C2 PARTIAL
route priority/retry/fallback algorithm
credential storage or secret examples
source-fitness/verification ranking
production provider adapter implementation
concrete provider priority selection
PAPER/LIVE/external side-effect enablement
self-approval / self-freeze
```

## 17. C2.01 Exit Gate

Construction stops at:

```text
C2.01 Independent Capability Review
```

The independent reviewer must attack taxonomy granularity, semantic-ref stability, endpoint/profile/field binding, capability compatibility, parent-boundary leakage, C1.05R1 continuity, accidental C2.02/C2.03/C2.04/C2.05 preemption, vendor neutrality, and governance traceability.

No C2.02 construction is authorized by this candidate.
