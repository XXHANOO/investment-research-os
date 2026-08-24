# C1.05R1 — Provider-Normalization Interface Contract Repair Candidate

Generated: 2026-08-19T12:21:15.517079+00:00

Status: `CANDIDATE_FOR_C1_05R1_INDEPENDENT_REGRESSION_RECHECK`

Repair basis: C1.05 independent review blockers `C1PN-B01` and `C1PN-B02` only.

Parent authority:

```text
Frozen C0
9585df6c0fbdb2cc40bc38571f8452b51f8ca69c9fd9432b10b87490b08a3b6f

C1.01R1 Identity Kernel
057303229ec7d169a19519edea256ce15f5a2dc92e654e820abddd9040c5b782

C1.02R1 Identifier / Symbol Mapping
dc5f2ec1295cf3afb9c8b585b3deca5f413de37db1a2d6c179a9e17f613531fb

C1.03R1 Corporate-Action Identity Effects
ea017504558532cce5e24929047cfbb94055f0a3cc25d80b3b1844216ea6b860

C1.04R1 Temporal / PIT Interface
9da9470cbb72ba4715c40fa9d7c1053f542381f0edf58b1f416a1c4be0d39118

C1.04R1 Independent Regression Re-Check
f63261e7c7ef27052e4e1a3ffea425506765ceafdabf84dada25d761ccd58850
```

Implementation:

```text
CONTRACT DESIGN ONLY
IMPLEMENTATION CODE NOT AUTHORIZED
```

---

# 1. Purpose and Ownership

C1.05 defines the **C1-facing normalization contract** by which provider/source-native identity, identifier, symbol, listing, contract and corporate-action material can become typed **C1 normalized assertion candidates** without allowing provider-native object models to become canonical truth.

Frozen path:

```text
Provider Native Payload
→ Provider Adapter
→ Validation
→ Normalization
→ Canonical Model
```

C1.05 owns:

```text
C1 semantic requirements at the provider-normalization boundary
C1 normalization-profile semantics and version pinning
which C1 assertion-candidate families may be emitted
C1 target-kind/cardinality/context validation
no-guess ambiguity/conflict behavior at normalization time
deterministic normalization requirement
C1-facing completeness dependency requirement when absence is load-bearing
referential-stability requirement for load-bearing foreign C2 semantic/capability/completeness dependencies
mandatory replay-lineage requirements for every materialized normalized candidate/result
propagation rules that prevent provider failure/partiality from becoming canonical NO_MATCH
```

C1.05 does NOT own:

```text
C2 provider selection, routing, credentials, retries, quota or fallback
C2 provider capability/coverage/completeness certification schema
C3 cache/freshness/quota/coalescing/last-known-good
C4 exact temporal/PIT/revision schema, available_from or precision encoding
C5 evidence fitness, verification, ranking or conflict adjudication
C11 raw/canonical persistence implementation
C12 release/promotion authority
```

---

# 2. Trust Boundary — C1 Does Not Parse Provider Truth Directly

C1 canonical domain code MUST NOT accept raw provider SDK/API objects as domain truth.

The C1 normalization port consumes a **validated provider-observation envelope** produced across the C2/provider-adapter boundary. This is a semantic interface, not a frozen serialization:

```text
ValidatedProviderObservationEnvelope:
  provider_operation_ref        # opaque C2-owned operation/result handle
  provider_capability_ref       # opaque C2-owned capability/certification handle
  normalization_profile_ref     # version-addressed C1 profile
  source_record_ref             # opaque provenance/raw-record handle
  source_group_ref              # optional grouping of fields from one provider record
  raw_payload_ref               # optional opaque retained-raw handle
  observations[]
  c2_operation_status           # preserves Frozen C0 operation semantics
  c2_data_outcome               # preserves Frozen C0 data-outcome semantics
  c2_degradation_refs[]         # opaque C2/C3-owned metadata when applicable
  c2_completeness_refs[]        # opaque C2-owned coverage/completeness dependencies when available
```

The exact C2 serialization remains C2/C1.06-owned later. C1.05 specifies only the semantic obligations it consumes.

The adapter may parse provider fields. It may not declare a provider field to be a canonical C1 ID by fiat.

---

# 3. Two Validation Layers

The Frozen `Validation` step is intentionally split by authority:

## 3.1 Provider / transport validation — C2 side

C2/provider integration validates matters such as:

```text
transport success/failure
provider response/schema shape
pagination completion
provider-field availability
provider endpoint semantics
provider authentication/authorization state
provider capability/certification scope
```

C1.05 does not redefine those schemas.

## 3.2 Canonical-semantic validation — C1 side

C1 validates:

```text
observation kind is supported by the profile
declared identifier/symbol scheme is permitted
required namespace/context exists
target kind is allowed by C1.01/C1.02
parent cardinalities are compatible with C1.01
corporate-action effect semantics are compatible with C1.03
relation/admission endpoints match C1.03R1 taxonomy
temporal/evidence references are treated as foreign-owned opaque interfaces
```

Failure at either layer is fail-loud. C1 MUST NOT repair a provider-shape failure by guessing canonical meaning.

---

# 4. Versioned Normalization Profile

Every normalization operation MUST specify a version-addressed C1 normalization profile.

Logical profile contract:

```text
NormalizationProfileDefinition:
  profile_id
  profile_version_or_content_address
  parent_c1_contract_refs
  provider_profile_ref             # opaque C2-owned provider semantic profile
  supported_observation_kinds[]
  provider_field_semantic_refs[]   # opaque C2 field-semantics references
  c1_scheme_profile_refs[]         # C1.02 SchemeDefinition/child profiles
  required_context_slots[]
  allowed_output_assertion_kinds[]
  multiplicity_rule
  transformation_policy_refs[]
  loss_policy
  deterministic_ordering_rule
  absence_exactness_policy
```

The profile MAY bind provider semantic fields to C1 semantic slots. It MUST NOT:

```text
declare provider routing priority
store credentials
claim provider availability/freshness
self-certify historical coverage completeness
redefine C4 available_from or precision
assign C5 verification strength
change C1 identity equivalence rules
```

A change that can alter normalized semantics requires a new profile version/content address.

Historical/audit replay MUST record which profile version produced each normalized candidate. Re-normalizing old source material under a newer profile creates a new lineage; it does not overwrite the prior normalized result in place.

## 4.1 R1 Referential Stability of Load-Bearing C2 Dependencies

Any C2-owned provider semantic, capability, or completeness reference that can affect normalization meaning, exactness eligibility, absence/uniqueness inference, or audit replay **MUST resolve to an immutable, version-addressed, content-addressed, or otherwise snapshot-stable C2 semantic state**.

At minimum, when load-bearing, this requirement applies to:

```text
provider_profile_ref
provider_field_semantic_refs[]
provider_capability_ref
c2_completeness_refs[]
```

A floating alias such as `latest`, a mutable provider-profile handle, or a mutable coverage/capability reference that may resolve to different semantics over time **MUST NOT** satisfy deterministic or audit-safe normalization and **MUST NOT** support exact `NO_MATCH` or uniqueness when the conclusion depends on that mutable state.

C1 owns only the referential-stability requirement. C1 does **not** define the C2 record schema, capability taxonomy, routing policy, certification algorithm, or completeness methodology.

A C2-owned stable reference MAY be implemented by a version, immutable snapshot identifier, content address, or an equivalent mechanism, provided replay resolves the same semantic state.

---

# 5. Provider Observation Vocabulary

C1.05 accepts provider observations only through typed semantic categories such as:

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

This vocabulary is an interface category set, not a new canonical identity hierarchy.

Provider-native objects that do not map safely into a supported category remain raw/provenance material or fail as unsupported. C1 MUST NOT create ad-hoc canonical fields merely to mirror a provider schema.

---

# 6. Normalized Output Families — Candidate, Not Truth

Permitted C1-facing outputs are typed candidate assertions compatible with trusted parents:

```text
IDENTITY_RESOLUTION_CANDIDATE
REGISTERED_IDENTIFIER_ASSIGNMENT_CANDIDATE
SYMBOL_ASSIGNMENT_CANDIDATE
LISTING_ASSERTION_CANDIDATE
CONTRACT_ASSERTION_CANDIDATE
CONTRACT_VENUE_ADMISSION_CANDIDATE
CORPORATE_ACTION_EVENT_OBSERVATION
IDENTITY_EFFECT_CANDIDATE
RELATION_EFFECT_CANDIDATE
TERMS_UPDATE_CANDIDATE
```

Normalization success means:

```text
provider observation
→ valid C1-shaped candidate material
```

It does **not** mean:

```text
candidate == adopted canonical truth
candidate == C5 VERIFIED
candidate == PIT_SAFE
candidate == unique identity
```

Identity adoption remains governed by C1 identity semantics plus the required C4/C5 dependencies.

---

# 7. Identity Firewall

The following provider-native values remain external observations/mappings:

```text
provider asset_id / security_id / company_id
provider symbol
exchange symbol
ticker
provider issuer code
provider display name
vendor permanent identifier
```

Even if a provider describes one as "permanent" or "unique", it MUST NOT be copied into an internal `EntityID`, `InstrumentID`, `ListingID` or `ContractID`.

A provider adapter may carry a previously resolved canonical target reference only when that reference came from a C1-governed resolution/adoption path.

No normalization profile may redefine canonical equality.

---

# 8. Identifier and Symbol Normalization

C1.02R1 remains authoritative.

Rules:

```text
raw_value is preserved
normalization is scheme/profile-specific
lexical auto-detection is forbidden
required namespace/context is explicit
generic PROVIDER_SYMBOL / EXCHANGE_SYMBOL parents are non-exact
exact resolution requires a concrete certified child profile where C1.02 requires one
grouping/search identifiers remain non-exact
symbol/provider identifiers never become canonical IDs
```

The following are forbidden as global behavior:

```text
blind upper/lower-casing
punctuation stripping
share-class delimiter rewriting
leading-zero removal
root-symbol truncation
blank/zero/null sentinel conversion without provider/profile semantics
```

If required context is missing, emit a context/ambiguity outcome rather than guessing.

---

# 9. Listing and Contract Normalization

## 9.1 Listing

A provider listing observation may propose attributes or a candidate mapping, but it cannot:

```text
reparent an existing ListingID to another InstrumentID
infer cross-Venue listing continuity solely from symbol/exchange fields
collapse execution venue into listing identity
```

Venue-transfer continuity remains C1.03-owned.

## 9.2 Contract

Contract observations preserve C1.01R1:

```text
ContractID → exactly one parent DERIVATIVE_PRODUCT InstrumentID
same governed standardized series may have multiple ContractVenueAdmissions
ContractVenueAdmission:
  Contract -> Listing
  contract.parent_instrument_id == listing.instrument_id
```

Provider venue-specific symbols or duplicate venue rows MUST NOT fragment one governed ContractID merely because the provider exposes one row per venue.

---

# 10. Corporate-Action Normalization

Provider-native corporate-action labels/statuses are external semantics, not identity decisions.

Normalization may preserve:

```text
provider event type/code
provider event status
old/new external identifiers/symbols
announced dates/terms as observations
provider event linkage
```

But the normalizer MUST NOT infer from an event label alone:

```text
which canonical Entity/Instrument/Listing/Contract survives
which canonical object is created/terminated
whether a successor relation exists
whether an effect is REALIZED
whether the active graph mutates now
```

C1.03 identity-effect semantics remain authoritative. C4 controls visibility/effectivity. C5 controls verification/evidence sufficiency.

`PROJECTED` output remains non-mutating.

Relational/admission candidates MUST satisfy the C1.03R1 typed endpoint/direction contract before they can be emitted.

---

# 11. Provider Operation Status and Data Outcome

Frozen C0 orthogonal provider semantics are preserved.

Conceptually:

```text
operation_status:
  SUCCESS | FAILED | CANCELLED

data_outcome:
  PRESENT | NO_DATA | PARTIAL
```

C1.05 does not freeze final enum serialization; C1.06/C2 will do so.

Rules:

## FAILED / CANCELLED

```text
normalization_outcome = NOT_RUN
```

No empty list may be normalized as if it meant canonical no-data/no-match.

## SUCCESS + PRESENT

Records may be normalized, but PRESENT does not itself prove the provider covered the entire resolution universe.

## SUCCESS + PARTIAL

Valid records may be normalized with explicit partial/item errors. Missing records cannot be used to prove absence or uniqueness.

## SUCCESS + NO_DATA

Means only that the successful provider operation returned no observations under its certified endpoint semantics.

It does **not** automatically mean C1 canonical `NO_MATCH`.

---

# 12. Normalization and Resolution Outcomes Are Orthogonal

The eventual machine schema MUST keep at least these semantic axes separate:

```text
provider operation status      # C0/C2
provider data outcome          # C0/C2
normalization outcome          # C1.05
identity/mapping resolution    # C1
PIT/reconstructability         # C4
verification/conflict state    # C5
```

Candidate normalization semantics equivalent to:

```text
NOT_RUN
NORMALIZED
PARTIAL_NORMALIZATION
NO_OBSERVATIONS
REJECTED
```

Candidate resolution semantics equivalent to:

```text
RESOLVED
NO_MATCH
AMBIGUOUS
CONFLICT
CONTEXT_REQUIRED
NON_EXHAUSTIVE
NOT_APPLICABLE
```

Exact names/serialization remain C1.06-owned.

No flat enum may collapse these axes in a way that makes FAILED indistinguishable from NO_MATCH.

---

# 13. Historical Provider Coverage / Completeness Dependency

This section closes the carry-forward hardening from the C1.04R1 independent re-check.

A positive exact mapping does **not** always require exhaustive enumeration. For example, an explicit exact identifier assertion may be usable without proving that one provider can enumerate every security in the market.

However, when an exact conclusion load-bearingly depends on **absence**, C1 must know that the relevant candidate universe was sufficiently covered.

Examples:

```text
"there is no matching historical assignment"
"this is the only possible provider-symbol target"
"no competing assertion existed in the relevant provider history"
```

C1.05 therefore requires an opaque completeness dependency when absence is load-bearing:

```text
CompletenessDependencyRequirement:
  c2_completeness_ref            # opaque; C2 owns certification/schema
  required_resolution_scope      # C1 semantic scope to be matched
  temporal_dependency_ref        # opaque C4 handle when historical
  evidence_dependency_ref        # opaque C5 handle when claim fitness matters
```

C1 owns only the requirement and semantic scope match.

C1 MUST NOT define:

```text
how C2 certifies an endpoint
how provider pagination is implemented
how historical coverage intervals are stored
how source fitness is scored
```

If completeness is absent, partial, or out of scope, the result remains explicitly non-exhaustive/unverified. It MUST NOT be promoted to exact `NO_MATCH` or unique resolution merely because only one provider candidate was seen.

For historical queries, exactness is additionally capped by C4 PIT reconstructability. The C1.04R1 rule remains:

```text
knowledge/decision cutoff = T
state/effective point = S <= T
visibility at T
effectivity/applicability at S
```

Coverage/completeness cannot override these temporal conditions.

---

# 14. Ambiguity vs Conflict

C1.02R1 distinction remains mandatory.

## Structural ambiguity

Occurs when C1 semantics/context leave multiple possible targets or required context is missing.

Examples:

```text
bare reusable ticker
provider symbol without security-type discriminator
one grouping identifier matching several canonical objects
```

Outcome is `AMBIGUOUS` / `CONTEXT_REQUIRED` equivalent.

## Evidence conflict

Occurs when incompatible candidate assertions remain under the same required semantic scope and need evidence adjudication.

C1 normalization must preserve:

```text
all load-bearing candidates
source_record/source_group links
opaque evidence/provenance refs
provider/degradation context
```

It MUST NOT silently choose by:

```text
provider order
newest response
source count
LLM/model confidence
market capitalization/popularity
```

Conflict adjudication remains C5-owned.

---

# 15. Temporal and Evidence References Stay Opaque

C1.05 may require/pass through:

```text
temporal_ref
resolution_anchor_ref
reconstructability_ref
evidence_ref
source_record_ref
coverage/completeness refs
```

But C1.05 MUST NOT:

```text
compute available_from from provider timestamp
invent missing timestamp precision
turn retrieved_at/published_at into a second visibility boundary
mark a candidate PIT_SAFE because provider says historical
mark a candidate VERIFIED because provider supplies confidence/quality score
```

C4 and C5 remain the respective authorities.

---

# 16. Determinism and Reproducibility

For the same:

```text
validated semantic observation set
+ exact normalization profile version/content address
+ exact parent C1 contract versions
+ exact load-bearing foreign semantic/capability/completeness dependency states
```

C1 normalized candidate semantics MUST be deterministic.

The final term is satisfied only through the snapshot-stable foreign-reference rule in Section 4.1. A floating C2 semantic dependency makes the input contract replay-unstable and therefore ineligible for deterministic/audit-safe materialization.

Semantically irrelevant provider transport ordering MUST NOT change:

```text
which candidates are emitted
which target is selected by C1 structural rules
canonical candidate ordering used for replay/comparison
```

If the input is ambiguous, the deterministic result is an ambiguity/candidate set — not a guessed target.

Each materialized normalized candidate/result **MUST** retain sufficient immutable or snapshot-stable lineage to identify:

```text
validated input or immutable validated-input reference
source_record_ref / source_group_ref
exact normalization_profile_ref
exact parent C1 contract refs
provider_operation_ref
load-bearing provider semantic/capability refs
load-bearing c2_completeness_refs[]
load-bearing C4 temporal dependency refs
load-bearing C5 evidence/provenance refs
item/batch normalization outcome context needed to explain partiality
c2_degradation_refs[] / fallback provenance when materially relevant
```

A result missing replay-critical lineage is not eligible for replay-safe materialization. This rule does not prescribe the internal C2/C4/C5 schemas or storage layout.

Hash algorithms/storage layout remain C11/C1.06 concerns.

---

# 17. Loss / Unknown Field Policy

Raw provider structure may contain fields that C1 does not understand or own.

Rules:

```text
unknown optional field
→ preserve in raw/provenance if permitted
→ do not add ad-hoc C1 canonical field

required semantic field cannot be represented without lossy coercion
→ typed rejection / item failure
→ do not invent precision or meaning
```

One provider record may emit multiple normalized C1 candidates. All such candidates preserve common `source_group_ref` / `source_record_ref` lineage.

---

# 18. Batch and Item Failure Semantics

Normalization must expose both item-level and batch-level failure information.

Example:

```text
10 validated provider observations
8 normalize successfully
2 fail semantic validation
```

Permitted result:

```text
8 candidate assertions
+ 2 typed item errors
+ batch normalization outcome = PARTIAL_NORMALIZATION
```

Forbidden result:

```text
8 candidate assertions
+ no record that 2 inputs failed
+ apparent full success
```

A partial normalized candidate set is not exhaustive merely because all emitted items are valid.

---

# 19. Degradation and Fallback Context

If C2/C3 indicates fallback, stale/last-known-good use, quota pressure, or another degradation that materially changes source/provenance semantics, every materialized normalized candidate/result **MUST preserve** the applicable opaque degradation/fallback provenance reference in replay lineage.

A degraded or fallback path **MUST NOT** be materialized as clean primary-source provenance by omitting the degradation signal.

C1 does not define fallback policy and does not initiate a fallback provider.

A normalization failure returns to the owning C2/workflow boundary as a typed outcome.

---

# 20. Typed Contract Errors — Candidate Semantics

C1.06 will freeze exact enum names/serialization. C1.05 requires machine-distinguishable failures equivalent to:

```text
NORMALIZATION_PROFILE_REQUIRED
UNSUPPORTED_NORMALIZATION_PROFILE
PROVIDER_OBSERVATION_NOT_VALIDATED
PROVIDER_FIELD_SEMANTICS_REQUIRED
NORMALIZATION_CONTEXT_REQUIRED
NORMALIZATION_TARGET_KIND_MISMATCH
NORMALIZATION_LOSSY_COERCION_FORBIDDEN
NORMALIZATION_PROFILE_CONFLICT
NORMALIZATION_ITEM_REJECTED
UPSTREAM_PROVIDER_FAILURE
UPSTREAM_OPERATION_CANCELLED
NON_EXHAUSTIVE_PROVIDER_RESULT
COMPLETENESS_DEPENDENCY_REQUIRED
COMPLETENESS_SCOPE_MISMATCH
RAW_PROVIDER_OBJECT_NOT_CANONICAL
PROVIDER_NATIVE_ID_NOT_CANONICAL
CONFLICT_REQUIRES_C5
UNSTABLE_FOREIGN_SEMANTIC_REFERENCE
REPLAY_LINEAGE_REQUIRED
DEGRADATION_PROVENANCE_REQUIRED
```

These do not replace C1.01/C1.02/C1.03/C1.04 errors; they are interface-layer failure semantics.

---

# 21. Resolved Pressure / Later-Stage Boundaries

C1.05 resolves the provider-normalization interface pressure by adopting:

```text
validated observation envelope
+ versioned C1 normalization profile
+ typed candidate-only outputs
+ deterministic/no-guess normalization
+ orthogonal provider/normalization/resolution/PIT/verification outcomes
+ explicit historical completeness dependency when absence is load-bearing
+ snapshot-stable load-bearing C2 semantic/capability/completeness dependencies
+ mandatory replay-critical lineage on every materialized candidate/result
```

Still later-stage:

```text
C1.OPEN-010 exact ID/result/error serialization             → C1.06
exact normalization/result enum serialization               → C1.06
provider capability/coverage/completeness record schema     → C2
provider routing/credentials/retry/fallback                  → C2/C3
exact temporal/revision/precision/reconstructability schema → C4
verification/source-fitness/conflict adjudication           → C5
persistence/index/raw artifact implementation               → C11
```

---


# 21A. C1.05R1 Repair Delta — Normative Scope

This R1 changes only the two failed review points:

```text
C1PN-B01 → snapshot-stable load-bearing C2 semantic/capability/completeness references
C1PN-B02 → mandatory materialized replay lineage, including degradation/fallback provenance when material
```

All other C1.05 semantics remain unchanged. No C1.01/C1.02/C1.03/C1.04 ownership or canonical semantics are redesigned, and no implementation is authorized.


# 22. C1.05R1 Exit Gate

C1.05R1 is eligible for independent regression re-check only if:

1. raw provider payloads cannot become C1 canonical truth directly;
2. the C1 input boundary requires validated provider observations;
3. C2 routing/capability/certification remains external and opaque;
4. normalization profiles are explicit/version-addressed;
5. provider symbols/native IDs cannot become canonical IDs;
6. normalization targets only trusted C1 assertion families and remains candidate-not-truth;
7. C1.02 mapping exactness/context/grouping rules survive;
8. C1.01 listing/contract cardinalities survive;
9. C1.03 corporate-action and relation semantics survive;
10. C1.04 temporal/PIT semantics survive;
11. C0 provider failure versus NO_DATA separation survives;
12. NO_DATA/PARTIAL/search results cannot prove absence by convenience;
13. load-bearing absence/uniqueness exactness requires matching C2 completeness dependencies;
14. C1 does not take over completeness certification;
15. C4/C5 refs remain opaque and no precision/verification strength is invented;
16. ambiguity remains distinct from conflict;
17. conflicts preserve candidate assertions and cannot be silently reconciled;
18. normalization is deterministic only when all load-bearing foreign semantic/capability/completeness dependencies are snapshot-stable;
19. materialized normalized candidates/results retain mandatory replay-critical lineage;
20. fallback/degraded paths retain mandatory degradation provenance when materially relevant;
21. profile evolution/re-normalization is version-addressed and non-destructive;
22. item/batch failures are fail-loud and partial normalization is explicit;
23. raw/provider-specific unknown fields cannot pollute canonical schema;
24. downstream logic consumes normalized C1 types only;
25. all C1-257..C1-330 obligations remain mapped and the targeted R1 obligations C1-331..C1-337 are mapped;
26. Frozen C0 and trusted parent hashes remain pinned/unchanged;
27. implementation code is not started.

If these conditions are satisfied locally, the repair candidate may proceed to **C1.05R1 Independent Regression Re-Check**.

C1.05R1 repair construction does **not** self-authorize C1.06.
