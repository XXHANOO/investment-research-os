# C2.03R2 — Acceptance Test Delta Candidate

Generated: 2026-08-24T12:12:00Z

Status: `REPAIR_CANDIDATE_PENDING_INDEPENDENT_ROUTING_RECHECK`

Scope: residual `C2ROUTE-B04` transition activation/precedence only. `C2ROUTE-B01..B03` remain closed by the R1 independent re-check.

## C2-270

**Surface:** `C2ROUTE-B04`

**Obligation:** Presence of a valid AuthorizedRequirementTransitionInput is authorization only and does not by itself activate R-to-R-prime or preempt current-R routing.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-271

**Surface:** `C2ROUTE-B04`

**Obligation:** After validating any present transition input as a route-input precondition without activating it, the evaluator computes the exact ordinary current-R decision with the transition ignored, then evaluates transition applicability in a second deterministic pass.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-272

**Surface:** `C2ROUTE-B04`

**Obligation:** The Pass-A ordinary decision is deterministically classified by an ordered exhaustive partition into exactly one of CURRENT_R_TERMINAL, CURRENT_R_PROGRESS_AVAILABLE, or CURRENT_R_STRUCTURALLY_EXHAUSTED; unclassifiable states fail closed.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-273

**Surface:** `C2ROUTE-B04`

**Obligation:** CURRENT_R_TERMINAL includes accepted/cancelled terminal actions and policy/default terminal actions that are not structural exhaustion; it always takes precedence over a valid authorized requirement transition.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-274

**Surface:** `C2ROUTE-B04`

**Obligation:** CURRENT_R_PROGRESS_AVAILABLE includes initial eligible current-R selection, SAME_ROUTE_REATTEMPT, NEXT_ROUTE with a selected current-R key, and external-admission YIELD; each takes precedence over transition application.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-275

**Surface:** `C2ROUTE-B04`

**Obligation:** CURRENT_R_STRUCTURALLY_EXHAUSTED requires absence of accepted/cancelled terminal state, absence of current-R progress, and absence of any eligible unconsumed current-R RouteStateKey under the pinned policy; policy-selected terminal/default action while a current-R route still exists is CURRENT_R_TERMINAL instead.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-276

**Surface:** `C2ROUTE-B04`

**Obligation:** transition_applicable is true iff the present transition is valid, current-R is structurally exhausted, and at least one eligible unconsumed R-prime RouteStateKey exists.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-277

**Surface:** `C2ROUTE-B04`

**Obligation:** Current-R NOMINATE_NEXT_ROUTE with an eligible selected B@R plus a valid R-to-R-prime transition must continue to B@R and emit no RequirementTransitionEvent.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-278

**Surface:** `C2ROUTE-B04`

**Obligation:** Current-R NOMINATE_SAME_ROUTE_REATTEMPT plus a valid R-to-R-prime transition must retain the same A@R reattempt nomination and emit no RequirementTransitionEvent.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-279

**Surface:** `C2ROUTE-B04`

**Obligation:** A terminal accepted provider result under R plus a valid R-to-R-prime transition must retain TERMINATE_WITH_ATTEMPT under R and must not activate the downgrade.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-280

**Surface:** `C2ROUTE-B04`

**Obligation:** CANCELLED under R plus a valid R-to-R-prime transition must retain TERMINATE_CANCELLED and must not activate the downgrade.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-281

**Surface:** `C2ROUTE-B04`

**Obligation:** Before any provider attempt, if at least one eligible current-R RouteStateKey exists, current-R initial selection wins over a valid R-to-R-prime transition.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-282

**Surface:** `C2ROUTE-B04`

**Obligation:** Before any provider attempt, if current R has no selectable eligible RouteStateKey and valid R-prime has at least one, the transition applies and nominates the first deterministic R-prime key.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-283

**Surface:** `C2ROUTE-B04`

**Obligation:** When current R is structurally exhausted after attempts/blocks and valid R-prime has an eligible unconsumed key, the downgrade action supersedes only the ordinary exhausted/downgrade-required result.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-284

**Surface:** `C2ROUTE-B04`

**Obligation:** If current R is structurally exhausted but valid R-prime has no eligible unconsumed key, no transition event is emitted, R-prime does not become effective, and the exact ordinary current-R exhaustion/downgrade-required result remains.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-285

**Surface:** `C2ROUTE-B04`

**Obligation:** A present transition that is malformed, has wrong from_id, non-distinct to_id, missing trusted authorization, or otherwise fails Section 12.2 validation fails closed and cannot be silently ignored in favor of current-R routing.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-286

**Surface:** `C2ROUTE-B04`

**Obligation:** Identical pinned RouteDecisionInput and retained lineage must reproduce the same Pass-A class, transition_applicable result, route action, selected candidate, and requirement-transition lineage independent of code/thread/callback evaluation order.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-287

**Surface:** `TRACEABILITY`

**Obligation:** Successor traceability records the immutable R1 Stage Report typo without modifying history: the actual R1 repair-obligation range is C2-231..C2-269 (39), not C2-231..C2-268.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.

## C2-288

**Surface:** `NON_REGRESSION`

**Obligation:** R2 makes no semantic change to independently closed C2ROUTE-B01, C2ROUTE-B02, or C2ROUTE-B03; independent re-check must confirm no regression on those boundaries.

**Expected re-check result:** an independent reviewer must demonstrate the property from the exact R2 successor candidate and pinned R1 re-check artifacts.
