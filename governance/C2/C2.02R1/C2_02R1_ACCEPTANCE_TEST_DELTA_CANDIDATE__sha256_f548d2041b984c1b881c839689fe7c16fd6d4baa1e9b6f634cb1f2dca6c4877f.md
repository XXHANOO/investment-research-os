# C2.02R1 — Acceptance Test Delta Candidate

Generated: 2026-08-24T08:36:46Z

Status: `SCOPED_REPAIR_CANDIDATE_PENDING_INDEPENDENT_RECHECK`

Range: `C2-144..C2-167` (24 repair obligations)

These obligations supplement, not rewrite, the original `C2-094..C2-143` authority. Independent re-check must re-evaluate original failed IDs `C2-101, C2-113, C2-115, C2-123, C2-125, C2-141` against the R1 successor semantics.

## C2-144 — Terminal candidate set pinned

Outcome classification uses only conditions established by the same pinned registry/profile/endpoint/capability semantic state.

Decision refs: `C2.DEC-108`

## C2-145 — Fixed phase order

The operation phase ordering is fixed and used for primary terminal-condition selection.

Decision refs: `C2.DEC-109`

## C2-146 — Deterministic same-phase tie-break

Same-phase non-success candidates use the frozen class tie-break and closed tuple tie-break.

Decision refs: `C2.DEC-109`

## C2-147 — Cancellation versus timeout adversarial

Explicit cancellation and timeout in the same phase classify CANCELLED.

Decision refs: `C2.DEC-110`

## C2-148 — Provider error versus absence adversarial

Provider error envelope plus an authorized 404-like absence signal classifies FAILED.

Decision refs: `C2.DEC-110`

## C2-149 — Decode failure versus partiality adversarial

Partiality/truncation evidence plus required decode failure classifies FAILED.

Decision refs: `C2.DEC-110`

## C2-150 — Successful conditions provisional until validation

PRESENT/NO_DATA/PARTIAL cannot terminalize before required semantic validation.

Decision refs: `C2.DEC-108`

## C2-151 — Single terminal phase source

operation_phase_terminal is the sole authoritative terminal phase in successor semantics.

Decision refs: `C2.DEC-111`

## C2-152 — Duplicate phase mismatch fails closed

Any legacy duplicate nested phase must equal top-level terminal phase or fail ADAPTER_INVARIANT.

Decision refs: `C2.DEC-111`

## C2-153 — FAILED admits zero observations

FAILED requires admitted_observation_count=0.

Decision refs: `C2.DEC-112`

## C2-154 — CANCELLED admits zero observations

CANCELLED requires admitted_observation_count=0.

Decision refs: `C2.DEC-112`

## C2-155 — Diagnostic bytes are not admitted

Diagnostic/quarantined/raw-ingress material cannot increment admitted_observation_count.

Decision refs: `C2.DEC-112`

## C2-156 — Attempted response scope retained

Every outcome retains snapshot-stable attempted_response_semantic_refs under the same registry snapshot.

Decision refs: `C2.DEC-113`

## C2-157 — Whole-attempt partiality is material

WHOLE_ATTEMPT matched partiality is always material.

Decision refs: `C2.DEC-114`

## C2-158 — Scoped partiality intersection

RESPONSE_SEMANTIC_SET partiality is material iff affected refs intersect attempted response refs.

Decision refs: `C2.DEC-114`

## C2-159 — Irrelevant partiality does not force PARTIAL

A matched scope-disjoint partiality signal remains replay-visible but does not force PARTIAL.

Decision refs: `C2.DEC-114`

## C2-160 — Unresolved partiality materiality fails closed

Insufficient scope semantics cannot produce PRESENT or NO_DATA and maps to typed semantic failure.

Decision refs: `C2.DEC-115`

## C2-161 — Material subset invariant

material_partiality_signal_refs must be a subset of matched_partiality_signal_refs.

Decision refs: `C2.DEC-115`

## C2-162 — Material partiality dominates successful data classification

Any material partiality yields PARTIAL when usable, otherwise FAILED; never PRESENT/NO_DATA.

Decision refs: `C2.DEC-116`

## C2-163 — Single retry advisory

Only top-level diagnostic_retry_hint is authoritative; failure-level duplicate retry_hint is removed.

Decision refs: `C2.DEC-117`

## C2-164 — Absence semantics is not C2.05 certification

Pinned endpoint-profile-authorized absence semantics does not imply completeness certification.

Decision refs: `C2.DEC-118`

## C2-165 — Frozen C1 serialization seam recorded

C2.06 must losslessly reconcile frozen C1 OutcomeAxes without FAILED-to-NO_DATA semantic reinterpretation.

Decision refs: `C2.DEC-119`

## C2-166 — Original failed obligations repaired for re-check

R1 supplies explicit semantics addressing C2-101,113,115,123,125,141 without rewriting original evidence.

Decision refs: `C2.DEC-120`

## C2-167 — Repair scope remains narrow

No routing, credentials, completeness methodology, cross-wire implementation, provider selection, or production adapter semantics are introduced.

Decision refs: `C2.DEC-121`
