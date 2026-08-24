# C2.02 — Acceptance Test Delta Candidate

Generated: 2026-08-24T07:36:00Z

Status: `CANDIDATE_NOT_INDEPENDENTLY_REVIEWED_NOT_FROZEN`

Range: `C2-094..C2-143` (50 obligations)

These are contract-level acceptance obligations for Independent Outcome-Semantics Review; they are not production adapter tests.

## C2-094 — Operation status domain

Only SUCCESS/FAILED/CANCELLED are legal top-level operation statuses.

Decision refs: `C2.DEC-077`

## C2-095 — Data outcome domain

Only PRESENT/NO_DATA/PARTIAL are legal successful data outcomes.

Decision refs: `C2.DEC-078`

## C2-096 — SUCCESS requires data outcome

SUCCESS has exactly one data outcome.

Decision refs: `C2.DEC-079`

## C2-097 — FAILED forbids data outcome

FAILED has no PRESENT/NO_DATA/PARTIAL value.

Decision refs: `C2.DEC-079`

## C2-098 — CANCELLED forbids data outcome

CANCELLED has no PRESENT/NO_DATA/PARTIAL value.

Decision refs: `C2.DEC-079, C2.DEC-092`

## C2-099 — FAILED requires failure envelope

Every FAILED outcome has a structured failure object.

Decision refs: `C2.DEC-080`

## C2-100 — Failure family/code coherence

Every failure has reviewed family/code pair or UNKNOWN_PROVIDER_FAILURE/UNKNOWN_FAILURE.

Decision refs: `C2.DEC-080, C2.DEC-081`

## C2-101 — Failure operation phase

Every failure records the terminal operation phase.

Decision refs: `C2.DEC-080`

## C2-102 — Unknown failure explicit

Unknown provider errors cannot mint ad-hoc family or become NO_DATA.

Decision refs: `C2.DEC-081`

## C2-103 — No text-only failure

Natural-language text cannot be the sole machine failure representation.

Decision refs: `C2.DEC-080, C2.DEC-081`

## C2-104 — Transport failure != NO_DATA

DNS/connect/TLS/reset failures are FAILED.

Decision refs: `C2.DEC-082`

## C2-105 — Timeout != NO_DATA

Provider/client timeouts are FAILED/TIMEOUT unless explicit cancellation semantics apply.

Decision refs: `C2.DEC-082, C2.DEC-093`

## C2-106 — Server/upstream failure != NO_DATA

Provider 5xx/maintenance/upstream failure is FAILED.

Decision refs: `C2.DEC-082`

## C2-107 — Auth/authz failure != NO_DATA

Authentication/authorization/entitlement failures are FAILED.

Decision refs: `C2.DEC-083`

## C2-108 — Rate limit fails loud

Rate-limit rejection/exhaustion is FAILED/RATE_LIMIT.

Decision refs: `C2.DEC-084`

## C2-109 — 404 no universal meaning

HTTP 404 or analogous status is not automatically NO_DATA.

Decision refs: `C2.DEC-085`

## C2-110 — 404 absence requires pinned endpoint semantics

404-like signal becomes NO_DATA only if pinned endpoint semantics classify that exact signal as genuine absence.

Decision refs: `C2.DEC-085`

## C2-111 — NO_DATA zero observations

SUCCESS+NO_DATA has admitted_observation_count=0.

Decision refs: `C2.DEC-086`

## C2-112 — NO_DATA requires absence semantics

SUCCESS+NO_DATA retains matched endpoint-authorized absence semantics.

Decision refs: `C2.DEC-086`

## C2-113 — NO_DATA forbids known partiality

Known material partiality makes NO_DATA illegal.

Decision refs: `C2.DEC-086`

## C2-114 — PRESENT requires observation

SUCCESS+PRESENT has at least one admitted provider observation.

Decision refs: `C2.DEC-087`

## C2-115 — PRESENT forbids material partiality

Known incomplete scope prevents PRESENT classification.

Decision refs: `C2.DEC-087`

## C2-116 — PARTIAL requires evidence

SUCCESS+PARTIAL retains explicit incomplete-scope/partiality evidence.

Decision refs: `C2.DEC-088`

## C2-117 — Zero-observation PARTIAL guarded

PARTIAL with zero observations is legal only with explicit partiality evidence.

Decision refs: `C2.DEC-088`

## C2-118 — Decode failure is FAILED

Undecodable/unparseable response cannot be coerced to PARTIAL or NO_DATA.

Decision refs: `C2.DEC-089`

## C2-119 — Semantic ambiguity fails closed

Ambiguous absence/partiality classification is FAILED/RESPONSE_SEMANTIC_INVALID.

Decision refs: `C2.DEC-089`

## C2-120 — 2xx provider error still failure

Provider error envelope under transport success is FAILED.

Decision refs: `C2.DEC-090`

## C2-121 — Incomplete pagination yields PARTIAL

Known incomplete cursor/page traversal yields PARTIAL when decoded material remains usable.

Decision refs: `C2.DEC-091`

## C2-122 — Unusable truncation yields FAILED

Truncation that prevents semantic usability yields FAILED rather than PARTIAL.

Decision refs: `C2.DEC-091`

## C2-123 — Cancellation envelope

CANCELLED requires structured cancellation origin and phase.

Decision refs: `C2.DEC-092`

## C2-124 — Cancellation distinct from failure

Cancellation is not rewritten as FAILED solely for convenience.

Decision refs: `C2.DEC-092`

## C2-125 — Timeout/cancellation distinction

Timeout is FAILED unless an external controller explicitly cancelled the operation.

Decision refs: `C2.DEC-093`

## C2-126 — Cancelled bytes cannot normalize

Cancelled response bytes cannot be emitted as provider observations to C1.

Decision refs: `C2.DEC-094`

## C2-127 — FAILED -> C1 NOT_RUN

Frozen C1 normalization consequence for FAILED is NOT_RUN.

Decision refs: `C2.DEC-095`

## C2-128 — CANCELLED -> C1 NOT_RUN

Frozen C1 normalization consequence for CANCELLED is NOT_RUN.

Decision refs: `C2.DEC-095`

## C2-129 — NO_DATA != C1 NO_MATCH

SUCCESS+NO_DATA does not automatically establish canonical NO_MATCH.

Decision refs: `C2.DEC-096`

## C2-130 — PARTIAL missing data not absence

Missing records under PARTIAL cannot prove absence/uniqueness.

Decision refs: `C2.DEC-097`

## C2-131 — Completeness deferred

C2.02 does not define completeness/coverage certification methodology.

Decision refs: `C2.DEC-098`

## C2-132 — Positive exact mapping not universe-bound

C2.02 does not impose universe-wide enumeration on positive exact mapping when absence is not load-bearing.

Decision refs: `C2.DEC-098`

## C2-133 — Retry hint non-authoritative

Diagnostic retry hint cannot itself cause retry/backoff.

Decision refs: `C2.DEC-099`

## C2-134 — C3 retry ownership

Retry/backoff/quota/budget/coalescing/freshness decisions remain C3-owned.

Decision refs: `C2.DEC-099`

## C2-135 — C4 boundary

Provider operation diagnostics do not establish C4 available_from/revision/PIT state.

Decision refs: `C2.DEC-100`

## C2-136 — C5 boundary

SUCCESS/PRESENT/NO_DATA/PARTIAL do not establish C5 verification/source fitness.

Decision refs: `C2.DEC-101`

## C2-137 — Pinned replay refs

Outcome retains snapshot-stable registry/profile/endpoint/capability refs.

Decision refs: `C2.DEC-102`

## C2-138 — Matched signal lineage

Matched absence/partiality semantic refs are replay-retained when load-bearing.

Decision refs: `C2.DEC-102`

## C2-139 — Degradation provenance

Material C2 degradation refs cannot be erased; routing meaning remains C2.03-owned.

Decision refs: `C2.DEC-103`

## C2-140 — Sanitized diagnostics

Provider-native diagnostic code/status/summary cannot carry secrets/private state or override typed outcome semantics.

Decision refs: `C2.DEC-104`

## C2-141 — Illegal combinations rejected

Illegal status/data/failure/cancellation combinations fail closed; no coercion.

Decision refs: `C2.DEC-105`

## C2-142 — Vendor-neutral construction

No concrete provider priority/instance or production adapter is selected/implemented.

Decision refs: `C2.DEC-106`

## C2-143 — No side-effect authority

C2.02 grants no external/PAPER/LIVE side-effect authority.

Decision refs: `C2.DEC-107`
