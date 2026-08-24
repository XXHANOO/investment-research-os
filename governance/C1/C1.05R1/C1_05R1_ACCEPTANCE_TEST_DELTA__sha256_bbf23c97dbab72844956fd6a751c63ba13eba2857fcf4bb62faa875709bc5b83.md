# C1.05R1 Acceptance Test Delta — Provider-Normalization Determinism & Replay-Lineage Repair

Status: `CANDIDATE_FOR_C1_05R1_INDEPENDENT_REGRESSION_RECHECK`

C1-257..C1-330 below are preserved from the C1.05 candidate; C1-331..C1-337 are the narrow R1 additions.

These obligations are additive to C1-001..C1-256.

| ID | Area | Obligation | Expected result |
|---|---|---|---|
| C1-257 | boundary | raw provider SDK/API object or payload is passed directly as a C1 canonical domain object | contract violation / normalization boundary required |
| C1-258 | boundary | C1 normalization receives a validated provider-observation envelope with source/provider references rather than unvalidated transport payload | validated boundary required |
| C1-259 | ownership | provider routing, credentials, endpoint capability and provider certification remain referenced through C2-owned opaque handles | C2 boundary preserved |
| C1-260 | profile | normalization request without an explicit versioned normalization_profile_ref fails | NORMALIZATION_PROFILE_REQUIRED |
| C1-261 | profile | normalization output records the exact profile version/content address used | profile lineage pinned |
| C1-262 | profile | profile cannot silently infer undeclared provider-field semantics or capability scope | fail closed |
| C1-263 | raw preservation | raw provider value/source record remains preserved or referencable after normalized candidate emission | raw/provenance retained |
| C1-264 | normalization | identifier/symbol lexical transformation follows only the declared C1.02 scheme/profile rules | scheme-specific transform only |
| C1-265 | normalization | lexical shape alone cannot autodetect LEI/ISIN/CUSIP/FIGI/provider-symbol scheme | scheme declaration required |
| C1-266 | normalization | blank/zero/null/sentinel provider values are not globally coerced without provider/profile-declared semantics | no generic sentinel rewrite |
| C1-267 | context | missing scheme-required namespace/market/security-type context cannot be guessed from provider popularity | CONTEXT_REQUIRED |
| C1-268 | target kind | provider observation declared for a target kind forbidden by C1 scheme/profile fails semantic validation | TARGET_KIND_MISMATCH |
| C1-269 | identity | provider symbol/native asset code cannot be copied into EntityID/InstrumentID/ListingID/ContractID | external mapping only |
| C1-270 | identity | provider object ID cannot become a canonical ID merely because provider documents it as stable/permanent | external identifier only |
| C1-271 | identity | name + ticker/provider symbol + provider object ID cannot by themselves mint or merge a canonical identity | IDENTITY_AMBIGUOUS / candidate only |
| C1-272 | identity | a provider adapter may reference an existing canonical target only through a prior C1-governed resolution result | C1 resolution authority preserved |
| C1-273 | output | normalizer emits only C1-approved normalized assertion candidate families; arbitrary provider-native object kinds cannot enter canonical schema | output kind constrained |
| C1-274 | output | normalized provider assertion is candidate material and does not become adopted/verified canonical truth merely by normalization success | candidate-not-truth |
| C1-275 | mapping | identifier/symbol output uses C1.02 RegisteredIdentifierAssignment/SymbolAssignment semantics and target-kind/context rules | mapping contract preserved |
| C1-276 | mapping | grouping/search alias returned as a single provider hit cannot exact-resolve solely because result count is one | GROUPING_IDENTIFIER_NOT_EXACT / non-exact candidate |
| C1-277 | mapping | generic PROVIDER_SYMBOL/EXCHANGE_SYMBOL abstract profile cannot exact-resolve without a concrete certified child profile | exactness certification required |
| C1-278 | listing | provider listing observation cannot reparent an existing ListingID to a different InstrumentID | LISTING_REPARENT_FORBIDDEN |
| C1-279 | listing | symbol/exchange field change alone cannot decide that a venue transfer created/preserved a ListingID | C1.03 continuity semantics required |
| C1-280 | contract | contract observation whose parent derivative InstrumentID conflicts with referenced ListingID fails | CONTRACT_ADMISSION_INSTRUMENT_MISMATCH |
| C1-281 | contract | same governed standardized contract observed on multiple valid venue listings does not create duplicate ContractIDs | one ContractID + multiple admissions |
| C1-282 | contract | normalized admission candidate is typed Contract -> Listing and preserves C1.01/C1.03 admission invariants | typed admission candidate |
| C1-283 | corporate action | provider-native corporate-action event label normalizes only as external classification/observation and cannot itself become an identity effect | event class != identity effect |
| C1-284 | corporate action | provider label merger/acquisition/spin-off cannot choose surviving/replaced canonical IDs by itself | object-by-object identity decision required |
| C1-285 | corporate action | provider status such as completed/effective cannot by itself set IdentityEffectAssertion to REALIZED or active | C4/C5/C1.03 gates preserved |
| C1-286 | corporate action | normalized PROJECTED effect cannot mutate active canonical graph | no active mutation |
| C1-287 | relation | relational/admission effect candidate enforces C1.03R1 endpoint kinds, roles, direction and relation type | typed relation contract enforced |
| C1-288 | relation | non-relational normalized effect cannot carry undeclared secondary endpoint/relation fields | relation smuggling rejected |
| C1-289 | provider outcome | C2 FAILED operation is propagated and C1 normalization is NOT_RUN rather than normalizing an empty set | UPSTREAM_FAILURE / NOT_RUN |
| C1-290 | provider outcome | C2 CANCELLED operation is propagated and cannot be represented as successful empty normalization | CANCELLED / NOT_RUN |
| C1-291 | provider outcome | auth/rate-limit/network/server/pagination/parse/schema/validation failures remain typed failures and never become NO_DATA/NO_MATCH | fail loud |
| C1-292 | absence | SUCCESS + NO_DATA without exhaustive coverage support means no provider observations, not canonical NO_MATCH | NON_EXHAUSTIVE_EMPTY |
| C1-293 | absence | SUCCESS + NO_DATA may become NO_MATCH-eligible only when relevant C2 completeness/coverage scope supports exhaustive absence and other C1/C4/C5 gates hold | conditional NO_MATCH eligibility |
| C1-294 | partial | SUCCESS + PARTIAL may emit valid candidates but cannot prove uniqueness/no-match through missing records | PARTIAL_NORMALIZATION / non-exhaustive |
| C1-295 | partial | incomplete pagination cannot support exhaustive absence or uniqueness claims | non-exhaustive |
| C1-296 | search | search/top-k/best-match provider endpoint returning one record cannot prove uniqueness without certified exhaustive semantics | candidate set only |
| C1-297 | coverage | PRESENT data may still be non-exhaustive; positive result count alone does not establish coverage completeness | coverage axis separate |
| C1-298 | coverage | when exact negative/unique resolution relies on absence of competing assertions, opaque C2 coverage/completeness dependency refs are required | COMPLETENESS_DEPENDENCY_REQUIRED |
| C1-299 | coverage | C1 cannot author or upgrade provider coverage certification; it only consumes/propagates C2-owned dependency handles | C2 authority preserved |
| C1-300 | coverage | coverage/completeness dependency whose declared scope does not match scheme/namespace/security-type/query scope cannot support exactness | scope mismatch blocks exactness |
| C1-301 | historical coverage | historical exact resolution that depends on provider history cannot be stronger than C4 temporal reconstructability at the requested cutoff/state point | PIT weakest-link preserved |
| C1-302 | temporal | normalizer cannot derive authoritative available_from from provider timestamp/retrieved_at/published_at on its own | C4 available_from authority preserved |
| C1-303 | precision | date-only/provider-coarse time remains coarse through normalization; no start-of-day/market-open timestamp is invented | precision preserved |
| C1-304 | precision | unknown temporal precision cannot be upgraded to exact/PIT-safe by normalization | no temporal strength upgrade |
| C1-305 | temporal ref | C4 temporal_ref remains opaque and normalization profile cannot redefine its exact schema | C4 boundary preserved |
| C1-306 | evidence ref | C5 evidence/provenance refs remain opaque and normalization profile cannot define verification/ranking semantics | C5 boundary preserved |
| C1-307 | verification | provider confidence/quality/rank field cannot become C5 verification strength or canonical identity certainty | no confidence promotion |
| C1-308 | conflict | incompatible provider-native representations produce multiple candidate assertions/conflict material with source/evidence linkage rather than silent reconciliation | conflict preserved |
| C1-309 | conflict | provider order, newest response, source count or model confidence cannot silently break an identity/mapping conflict | C5 adjudication required |
| C1-310 | ambiguity | missing structural context is AMBIGUOUS/CONTEXT_REQUIRED and remains distinct from evidence conflict | ambiguity != conflict |
| C1-311 | ambiguity | multiple structurally valid C1 targets remaining after declared context yield AMBIGUOUS, not guessed RESOLVED | no guessing |
| C1-312 | determinism | same validated semantic input + same normalization profile version + same parent C1 contract versions yields same normalized candidate set | deterministic candidate semantics |
| C1-313 | determinism | provider transport/record ordering differences that are semantically equivalent cannot change canonical candidate ordering or chosen target | stable deterministic ordering |
| C1-314 | profile evolution | changed normalization behavior requires a new profile version/content address and cannot silently mutate prior outputs | version bump required |
| C1-315 | reproducibility | materialized normalized candidate records exact profile version and source/validated-input lineage needed for audit replay | replay lineage recorded |
| C1-316 | renormalization | re-normalizing old raw/provider observations under a newer profile does not overwrite prior normalized lineage in place | append/version preserved |
| C1-317 | loss boundary | unknown optional provider fields stay raw/provenance-only and do not create ad-hoc canonical fields | no schema pollution |
| C1-318 | loss boundary | required provider semantics that cannot be represented without lossy coercion cause typed item rejection rather than fabricated canonical precision | lossy required field rejected |
| C1-319 | item outcome | invalid observation item cannot disappear silently from a successful batch | item failure explicit |
| C1-320 | batch outcome | batch containing valid and invalid items emits valid candidates plus machine-distinguishable partial normalization/errors; it is not full success | PARTIAL_NORMALIZATION |
| C1-321 | downstream | downstream C1 domain consumer cannot consume raw provider payload/SDK model as canonical assertion even if raw is retained | canonical normalized types only |
| C1-322 | provenance grouping | one provider source record that emits multiple normalized candidates preserves common source_group/source_record linkage | one-to-many provenance retained |
| C1-323 | profile conflict | same provider field cannot be interpreted under incompatible scheme/target semantics inside one active profile without explicit rejection/version separation | profile conflict rejected |
| C1-324 | strength | normalization cannot invent verification strength, identity certainty, exactness certification or PIT status beyond upstream dependencies | no strength fabrication |
| C1-325 | degradation | if C2 used fallback/degraded provider behavior, normalization preserves the opaque degradation/provenance signal rather than presenting clean primary-source semantics | degradation propagated |
| C1-326 | routing | C1 normalizer never performs provider retry/routing/fallback when normalization fails; it returns typed outcome to C2/workflow | no C2 takeover |
| C1-327 | no match | C1 canonical NO_MATCH requires successful relevant retrieval plus normalization validity and any load-bearing completeness dependencies; empty list alone is insufficient | NO_MATCH guarded |
| C1-328 | completeness | exact resolution that depends on absence of competitors but lacks required coverage/completeness dependency is explicitly non-exhaustive/unverified | exactness withheld |
| C1-329 | temporal handoff | normalized historical mapping/effect candidate preserves C1.04 T/S semantics: visibility remains C4 at knowledge cutoff T and applicability at state point S | C1.04 parent semantics preserved |
| C1-330 | raw bypass | retaining raw provider structure for provenance never authorizes raw/native fields to bypass normalized canonical assertion validation downstream | raw is not domain truth |

| C1-331 | foreign dependency stability | normalization profile or validated input uses a load-bearing C2 provider semantic/capability reference that resolves through mutable `latest`/floating semantics | UNSTABLE_FOREIGN_SEMANTIC_REFERENCE / deterministic replay ineligible |
| C1-332 | foreign dependency stability | otherwise identical normalization uses an immutable/version-addressed/content-addressed or equivalent snapshot-stable C2 semantic/capability reference | deterministic/audit-safe eligibility preserved, subject to all other gates |
| C1-333 | completeness stability | exact NO_MATCH/uniqueness depends on a C2 completeness reference that is mutable/floating and may resolve to a different coverage state later | exactness prohibited / UNSTABLE_FOREIGN_SEMANTIC_REFERENCE |
| C1-334 | replay lineage | materialized normalized candidate/result omits validated-input/source lineage needed to identify the producing observation | REPLAY_LINEAGE_REQUIRED / non-materializable as replay-safe result |
| C1-335 | replay lineage | materialized normalized candidate/result omits exact normalization profile, parent C1 contract refs, or load-bearing foreign dependency refs | REPLAY_LINEAGE_REQUIRED / non-materializable as replay-safe result |
| C1-336 | partial replay lineage | materialized result from mixed valid/invalid batch omits item/batch outcome context needed to reconstruct partiality | REPLAY_LINEAGE_REQUIRED / partiality provenance invalid |
| C1-337 | degradation lineage | fallback/stale/last-known-good/degraded source path materially affected provenance but materialized result omits the degradation/fallback reference and appears clean-primary | DEGRADATION_PROVENANCE_REQUIRED / invalid replay lineage |

Coverage target:

```text
legacy range preserved: C1-257..C1-330
legacy count: 74
R1 added range: C1-331..C1-337
R1 added count: 7
combined range: C1-257..C1-337
combined count: 81
mapped by C1.05R1 decision ledger: 81
unmapped: 0
```

This is a contract-test delta only. No implementation test code is authorized in C1.05R1.
