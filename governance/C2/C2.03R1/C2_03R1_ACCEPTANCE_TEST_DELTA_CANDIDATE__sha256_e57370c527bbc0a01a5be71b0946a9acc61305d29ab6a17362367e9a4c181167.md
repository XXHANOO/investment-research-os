# C2.03R1 — Acceptance Test Delta Candidate

Generated: 2026-08-24T11:34:41Z

Status: `REPAIR_CANDIDATE_PENDING_INDEPENDENT_ROUTING_RECHECK`

Range: `C2-231..C2-269`

Original failed obligations requiring re-check: `C2-204, C2-221, C2-226, C2-227, C2-228`

## C2-231

**Blocker surface:** `C2ROUTE-B01`

**Obligation:** CandidateSetDefinition has a C2.03-owned full-tuple content-addressed identity with ref_kind ROUTE_CANDIDATE_SET and SHA-256 over canonical normative body.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-232

**Blocker surface:** `C2ROUTE-B01`

**Obligation:** RoutePolicySnapshot has a C2.03-owned full-tuple content-addressed identity with ref_kind ROUTE_POLICY_SNAPSHOT and SHA-256 over canonical normative body.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-233

**Blocker surface:** `C2ROUTE-B01`

**Obligation:** Routing stable-ref equality uses authority, ref_kind, logical_id, semantic_revision, and content_sha256; floating/hashless/wrong-kind/dangling/hash-mismatched refs fail closed.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-234

**Blocker surface:** `C2ROUTE-B01`

**Obligation:** CandidateSetDefinition canonicalizes its member list by route_candidate_id, rejects duplicate IDs, and route_candidate_ref is bound to the exact candidate_set_ref plus ID.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-235

**Blocker surface:** `C2ROUTE-B01`

**Obligation:** RoutePolicySnapshot binds one exact candidate_set_ref and RouteDecisionInput must use the same full-tuple candidate-set ref.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-236

**Blocker surface:** `C2ROUTE-B01`

**Obligation:** candidate_permission_mode is closed to ALL_IN_CANDIDATE_SET and ALLOWLIST with deterministic exact semantics.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-237

**Blocker surface:** `C2ROUTE-B01`

**Obligation:** ALL_IN_CANDIDATE_SET requires an empty allowlist; ALLOWLIST permits only exact listed IDs; unknown/duplicate/non-member IDs invalidate the policy snapshot.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-238

**Blocker surface:** `C2ROUTE-B01`

**Obligation:** The route-policy-eligible candidate set is derivable only from the exact bound candidate inventory and exact permission predicate; provider names, docs, mutable defaults, and untrusted content have no permission authority.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-239

**Blocker surface:** `C2ROUTE-B01`

**Obligation:** Identical pinned candidate-set and route-policy refs reproduce the same policy-eligible candidate set and candidate ordering inputs.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-240

**Blocker surface:** `C2ROUTE-B02`

**Obligation:** ContinuationRule omitted qualifiers are wildcards and do not require corresponding attempt-field absence.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-241

**Blocker surface:** `C2ROUTE-B02`

**Obligation:** Every present ContinuationRule qualifier compares by exact equality to the corresponding inherited C2.02 attempt value.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-242

**Blocker surface:** `C2ROUTE-B02`

**Obligation:** failure_family, failure_code, and diagnostic_retry_hint qualifiers are legal only for FAILED; failure_code additionally requires failure_family.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-243

**Blocker surface:** `C2ROUTE-B02`

**Obligation:** A present qualifier with an absent attempt value is non-matching; unknown values/fields or illegal qualifier combinations fail closed.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-244

**Blocker surface:** `C2ROUTE-B02`

**Obligation:** Generic FAILED and more-specific FAILED rules may both match; after exact matching, deterministic selection is solely by (rule_priority, rule_id).

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-245

**Blocker surface:** `C2ROUTE-B02`

**Obligation:** Closed defaults are applied only after the exact match predicate returns an empty match set; SUCCESS_PRESENT and CANCELLED remain non-overridable.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-246

**Blocker surface:** `C2ROUTE-B03`

**Obligation:** Every non-positive external gate creates an immutable ExternalAdmissionBlockRecord with a non-empty exact gate-ref set and exact candidate/requirement/policy/candidate-set linkage.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-247

**Blocker surface:** `C2ROUTE-B03`

**Obligation:** ExternalAdmissionBlockRecord action is closed to YIELD_FOR_EXTERNAL_ADMISSION or NOMINATE_NEXT_ROUTE, and NEXT_ROUTE is legal only under pinned policy mode NEXT_ROUTE.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-248

**Blocker surface:** `C2ROUTE-B03`

**Obligation:** EXTERNAL_ADMISSION_CONTINUATION FallbackEvent requires triggering_external_admission_block_ref, prohibits triggering_attempt_ref, and event/block from-candidate and requirement identities must agree.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-249

**Blocker surface:** `C2ROUTE-B03`

**Obligation:** External-admission-triggered fallback preserves event-level gate provenance through the exact referenced block record and never fabricates a provider outcome.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-250

**Blocker surface:** `C2ROUTE-B03`

**Obligation:** NEXT_ROUTE consumption is keyed by (route_candidate_ref,effective_requirement_identity) and includes both dispatched attempts and externally blocked records whose action is NOMINATE_NEXT_ROUTE.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-251

**Blocker surface:** `C2ROUTE-B03`

**Obligation:** A YIELD_FOR_EXTERNAL_ADMISSION block does not consume the RouteStateKey and retains the same pending candidate for future externally admitted dispatch.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-252

**Blocker surface:** `C2ROUTE-B03`

**Obligation:** NOMINATE_NEXT_ROUTE cannot reselect an externally blocked-and-fallback-consumed RouteStateKey under the same effective requirement.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-253

**Blocker surface:** `C2ROUTE-B03`

**Obligation:** RouteDecisionInput and RouteResolution/replay lineage retain ordered external-admission-block refs in addition to attempt/fallback/degradation refs.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-254

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** An authorized requirement transition is an explicit trusted input containing exact R, exact distinct R-prime, and an authorization ref; C2 cannot mint or infer it from provider content/failure.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-255

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** Requirement identities are deterministic SHA-256(JCS(normalized CapabilityRequirement)) values and an authorized downgrade requires to_id != from_id with from_id equal to the current effective requirement.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-256

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** NOMINATE_CANDIDATE_UNDER_DOWNGRADED_REQUIREMENT is a closed action usable only through a valid AuthorizedRequirementTransitionInput and cannot be emitted by ContinuationRule.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-257

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** Candidate selection under R-prime re-runs exact C2.01 compatibility and route-policy eligibility under the same S/pinned routing objects.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-258

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** RouteStateKey includes requirement identity, so A@R and A@R-prime are distinct; candidate A attempted under R may be selected under authorized R-prime when A@R-prime is eligible and unconsumed.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-259

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** SAME_ROUTE_REATTEMPT remains restricted to the identical candidate+effective-requirement RouteStateKey and cannot apply R-prime.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-260

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** Every applied R to R-prime downgrade emits a RequirementTransitionEvent with authorization, from/to requirement identities, selected candidate, policy/candidate-set refs, and linked degradation ref.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-261

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** Every applied downgrade emits RouteDegradationRecord(kind=REQUIREMENT_DOWNGRADE); same-candidate downgrade needs no FallbackEvent, while candidate-changing downgrade additionally requires FallbackEvent(reason=EXPLICIT_REQUIREMENT_DOWNGRADE).

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-262

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** Absent a valid authorized R-prime, C2 may emit REQUIRE_EXPLICIT_REQUIREMENT_DOWNGRADE but cannot silently change the effective requirement.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-263

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** Replay lineage retains all requirement-transition refs and reproduces the exact effective-requirement sequence.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-264

**Surface:** `ORIGINAL_FAILED_OBLIGATION_RECHECK`

**Obligation:** Original failed acceptance C2-204 is explicitly re-checked against event-level external-admission provenance.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-265

**Surface:** `ORIGINAL_FAILED_OBLIGATION_RECHECK`

**Obligation:** Original failed acceptance C2-221 is explicitly re-checked against exact candidate/policy identity plus block/requirement-transition replay lineage.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-266

**Surface:** `ORIGINAL_FAILED_OBLIGATION_RECHECK`

**Obligation:** Original failed acceptance C2-226 is explicitly re-checked against content-addressed policy identity and exact ContinuationRule matching.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-267

**Surface:** `ORIGINAL_FAILED_OBLIGATION_RECHECK`

**Obligation:** Original failed acceptance C2-227 is explicitly re-checked against exact match-set construction before closed defaults.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-268

**Surface:** `ORIGINAL_FAILED_OBLIGATION_RECHECK`

**Obligation:** Original failed acceptance C2-228 is explicitly re-checked using RouteStateKey consumption and same-candidate/new-requirement semantics.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

## C2-269

**Blocker surface:** `C2ROUTE-B04`

**Obligation:** A RouteDecisionInput carries at most one AuthorizedRequirementTransitionInput; multiple downgrade alternatives must be resolved by the trusted upstream authority before C2 routing evaluation.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R1 successor candidate and pinned parent/review artifacts.

