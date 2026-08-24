# C2.03 — Acceptance Test Delta Candidate

Generated: 2026-08-24T10:49:00Z

Status: `CANDIDATE_NOT_INDEPENDENTLY_REVIEWED`

Range: `C2-181..C2-230`

## C2-181

**Obligation:** Routing selects only capabilities that pass exact C2.01R1 compatibility for the same pinned R and S.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-182

**Obligation:** Unknown, wrong-kind, dangling, hash-mismatched, or floating load-bearing refs make semantic route eligibility false.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-183

**Obligation:** Operational route preference is never represented as C5 source fitness, credibility, truth, or verification.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-184

**Obligation:** Route candidate ordering is deterministic by (preference_tier, preference_ordinal, route_candidate_id).

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-185

**Obligation:** Duplicate/non-unique route_candidate_id or unprovable ordering fails closed rather than using local iteration order.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-186

**Obligation:** Concrete provider/vendor priority instances are absent from the C2.03 contract candidate.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-187

**Obligation:** Provider payload or untrusted content cannot add, remove, or reprioritize route candidates.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-188

**Obligation:** Every dispatched route attempt has append-only ordered lineage and references the exact C2.02 operation outcome.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-189

**Obligation:** A later successful attempt cannot erase or rewrite earlier FAILED attempts.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-190

**Obligation:** A later successful attempt cannot erase or rewrite earlier SUCCESS+NO_DATA attempts.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-191

**Obligation:** A later successful attempt cannot erase or rewrite earlier SUCCESS+PARTIAL attempts.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-192

**Obligation:** SUCCESS+NO_DATA continuation uses GENUINE_NO_DATA_CONTINUATION and does not reclassify the attempt as FAILED.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-193

**Obligation:** SUCCESS+NO_DATA fallback does not prove C1 NO_MATCH or canonical absence.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-194

**Obligation:** SUCCESS+PARTIAL may terminate or continue only with original partiality provenance preserved.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-195

**Obligation:** C2.03 performs no cross-provider union, deduplication, reconciliation, verification, or corroboration.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-196

**Obligation:** FAILED may lead to same-route nomination, next-route nomination, or exhaustion without converting failure to NO_DATA.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-197

**Obligation:** C2.02 diagnostic_retry_hint is diagnostic input only and does not itself authorize or schedule retry.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-198

**Obligation:** CANCELLED terminates the current route request and cannot automatically trigger fallback or same-route retry.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-199

**Obligation:** The C2.03 route action domain is closed and private adapter actions are forbidden.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-200

**Obligation:** C2 same-route reattempt is a logical nomination, not C3 attempt admission.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-201

**Obligation:** C2 does not compute backoff time, sleep for retry, decrement quota, or own C3 cache/freshness/coalescing/LKG.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-202

**Obligation:** Actual re-dispatch requires positive external admission under C3 plus continued C7 authorization/budget.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-203

**Obligation:** Unresolved or non-positive external admission causes no dispatch and remains distinct from provider FAILED/NO_DATA/PARTIAL.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-204

**Obligation:** Fallback triggered by external admission preserves the load-bearing external gate provenance.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-205

**Obligation:** C2.03 semantic ownership closes the retry/quota seam while exact C3/C7 wire binding remains deferred to C2.06.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-206

**Obligation:** Every candidate-to-candidate transition emits a FallbackEvent with from/to candidates, reason, requirement refs, and route-policy ref.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-207

**Obligation:** Equivalent fallback requires the same effective requirement and exact C2.01 compatibility for that requirement.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-208

**Obligation:** Equivalent fallback is still replay-visible even when it creates no semantic-degradation record.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-209

**Obligation:** A lower route preference tier is not automatically a lower-quality or lower-fitness source claim.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-210

**Obligation:** Requirement downgrade never mutates R in place and requires a distinct canonical R-prime.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-211

**Obligation:** Requirement downgrade requires trusted authorization, original-to-downgraded linkage, compatibility proof for R-prime, and a degradation record.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-212

**Obligation:** Absent authorized R-prime, C2 may request an explicit downgrade but cannot synthesize one from provider failure or content.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-213

**Obligation:** Route degradation kinds are closed to REQUIREMENT_DOWNGRADE, POLICY_PREFERENCE_TIER_DOWNGRADE, and PARTIAL_ACCEPTED_AS_TERMINAL.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-214

**Obligation:** C3 stale/cache/LKG degradation is never relabeled as a C2 route-degradation kind.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-215

**Obligation:** Material route degradation refs remain immutable and available for downstream replay lineage.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-216

**Obligation:** Route-level terminal disposition remains orthogonal to C2.02 provider operation/data outcomes.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-217

**Obligation:** EXHAUSTED is not provider NO_DATA, not provider FAILED, and not C1 NO_MATCH.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-218

**Obligation:** YIELDED_EXTERNAL_ADMISSION is not provider failure and performs no provider dispatch.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-219

**Obligation:** REQUIREMENT_DOWNGRADE_REQUIRED cannot continue until a trusted explicit R-prime is supplied/authorized.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-220

**Obligation:** Zero semantically compatible candidates is a route-level exhaustion reason and never synthetic provider NO_DATA.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-221

**Obligation:** Replay lineage retains S, exact R/R-prime, route policy, candidate inventory/order inputs, outcomes, external gates, fallback/degradation refs, and terminal disposition.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-222

**Obligation:** Successful fallback cannot be presented downstream as clean-primary provenance when material fallback/degradation occurred.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-223

**Obligation:** Provider/native payloads and untrusted content cannot authorize requirement downgrade, side-effect intent, C6 capability, C7 budget, or C3 admission changes.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-224

**Obligation:** C2.OPEN-006 is only candidate-closed pending Independent Routing Review; no self-approval/freeze occurs.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-225

**Obligation:** C2.OPEN-007 is candidate-closed only at the C2.03 semantic level; C2.06 cross-contract wire binding remains explicitly open.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-226

**Obligation:** RoutePolicySnapshot continuation rules are content-addressed, have unique rule_id, and resolve multiple matches deterministically by (rule_priority, rule_id).

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-227

**Obligation:** No matching route-policy rule uses the closed fail-safe defaults; SUCCESS_PRESENT and CANCELLED are not overridable.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-228

**Obligation:** NOMINATE_NEXT_ROUTE selects the first eligible unattempted candidate under the current requirement; candidate revisit is only SAME_ROUTE_REATTEMPT.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-229

**Obligation:** SAME_ROUTE_REATTEMPT preserves the same candidate and same effective requirement, creates a new attempt ordinal, and still requires external admission.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

## C2-230

**Obligation:** Higher numeric preference-tier fallback and terminal acceptance of PARTIAL emit their deterministic route-degradation records without making C5 quality claims.

**Expected review result:** independent reviewer must demonstrate this property from the pinned C2.03 candidate and inherited parent contracts.

