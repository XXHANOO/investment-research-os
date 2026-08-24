# C2.02 Independent Outcome-Semantics Review Report

Generated: 2026-08-24

Stage: `C2.02 — Typed Provider Operation / Data Outcome Contract`

Review verdict: **FAIL — SCOPED REPAIR REQUIRED**

This is an independent semantic review of the content-addressed C2.02 construction candidate. It does not modify the candidate, does not authorize C2.03, and does not authorize production/PAPER/LIVE side effects.

## Reviewed candidate pins

- normative contract: `eb7636409e2dcdfe688a089c0dabceacd300ad8dee49febfbc6cdc149b96d7ef`
- logical model: `607d3839d66ab0cae9bf8192f38135dfdde05f112a1768d33360415cda229ed4`
- acceptance delta: `2d8233a17fa2ad2afc0ff386e4975869d138bfafdf7025a17eb2be5556fb10ed`
- decision ledger: `9a84cda469a79b9f807a45514744fd6b905fe88ca0607ef3fd25f2b6bcd0f5ae`

Parent continuity rechecked against:

- C1.05R1 provider-normalization interface: `71d472e63044b9a7be2c6cc831705ed80dc6a06ccd0ef03e71a0618794bdef63`
- C2.01R1 repaired registry: `2cba76ffe8e308ade83778e26d24332c4ce019468a73875c36110c7bb5201e95`

## Summary

The C2.02 candidate correctly preserves the major frozen boundaries: infrastructure failure is not NO_DATA, SUCCESS/FAILED/CANCELLED is separate from PRESENT/NO_DATA/PARTIAL, C3 retains retry policy, C4 retains PIT/revision/available_from, C5 retains source fitness/verification, C2.05 retains completeness certification, and C1 normalization remains NOT_RUN for failed/cancelled operations.

However, the contract is not yet deterministic enough for a frozen provider-outcome boundary. Four blocking semantic defects remain.

### C2OUT-B01 — Compound terminal-condition precedence is not deterministic

**Severity:** BLOCKING

The outcome record has one top-level `operation_status` and one structured primary `failure_family/failure_code`, but the contract does not define a total precedence rule or a primary-cause selection rule when multiple terminal conditions are simultaneously observable.

Examples include external cancellation racing with a provider/client timeout; a 404-like response that also carries a provider error envelope; rate-limit/error-envelope combinations; and a partiality/truncation signal followed by decode or semantic failure.

Section 6.1 refers to a "higher-priority failure/partiality condition" without defining the priority relation. Section 9 distinguishes timeout from cancellation, but does not close race ordering. Two conforming adapters could therefore assign different typed outcomes to the same observed exchange.

**Required repair:** define deterministic status/failure precedence, or define a deterministic primary-cause plus secondary-cause structure. Add adversarial vectors for cancellation-vs-timeout and multiple simultaneous provider failure signals.

**Affected current obligations:** `C2-125`, `C2-141`.

### C2OUT-B02 — Terminal phase is duplicated without a coherence invariant

**Severity:** BLOCKING

`ProviderOperationOutcome` requires `operation_phase_terminal`, while `ProviderFailure` separately requires `operation_phase`, and `ProviderCancellation` separately requires `operation_phase`.

No rule requires these values to be equal or derived from one another. A record can therefore claim, for example, terminal phase `RESPONSE_BODY` at the top level while the nested failure claims `CONNECT`.

This is a replay/provenance contradiction, not merely a wire-schema concern.

**Required repair:** establish a single source of truth or an explicit equality/derivation invariant for FAILED and CANCELLED outcomes.

**Affected current obligations:** `C2-101`, `C2-123`.

### C2OUT-B03 — Non-success admitted-observation semantics are under-specified

**Severity:** BLOCKING

`admitted_observation_count` is required for every operation outcome. The contract defines exact legality for successful PRESENT/NO_DATA/PARTIAL outcomes, but does not require `admitted_observation_count = 0` for FAILED or CANCELLED.

That omission is material because C1.05R1 requires normalization `NOT_RUN` for FAILED/CANCELLED; C2.02 explicitly forbids cancelled bytes from becoming C1 provider observations; and usable incomplete records are already represented by SUCCESS+PARTIAL rather than FAILED.

As written, `FAILED` with a positive `admitted_observation_count` is not explicitly illegal, even though the term "admitted" implies downstream eligibility.

**Required repair:** either require zero admitted observations for FAILED/CANCELLED, or split diagnostic/decoded/quarantined counts from the downstream-admitted count and define each precisely.

**Affected current obligation:** `C2-141`.

### C2OUT-B04 — "Material partiality" lacks a deterministic scope predicate

**Severity:** BLOCKING

PRESENT and NO_DATA legality depends on the absence of "material" known partiality. C2.01R1 correctly provides stable provider-native partiality-signal semantics, but C2.02 does not define the rule that determines whether a matched partiality signal is material to the attempted semantic scope.

Without a scope-matching/materiality predicate, two adapters can observe the same pinned partiality signal and disagree on PRESENT versus PARTIAL or NO_DATA versus PARTIAL.

**Required repair:** define material partiality in terms of the attempted semantic operation and required response scope, using only pinned endpoint/profile semantics. Add tests where a provider-native partiality signal is relevant to the requested scope and where it is explicitly irrelevant.

**Affected current obligations:** `C2-113`, `C2-115`.

## Acceptance review

- reviewed obligations: 50 (`C2-094..C2-143`)
- PASS: 44
- FAIL: 6
- FAIL IDs: `C2-101`, `C2-113`, `C2-115`, `C2-123`, `C2-125`, `C2-141`

The remaining 44 obligations are semantically acceptable at C2.02 contract level.

## Non-blocking observations / mandatory downstream obligations

### N01 — Duplicate retry advisory fields should be normalized in repair

The top-level outcome has `diagnostic_retry_hint`, while `ProviderFailure` also has `retry_hint`. Both are advisory and do not leak C3 retry authority, so this does not independently block the stage. Still, R1 should either use one authoritative diagnostic field or define strict equality/derivation to avoid contradictory replay diagnostics.

### N02 — Frozen C1 final schema has a broader outcome-axis serialization surface

The frozen C1.07R2 contract vectors include `C1-397`, where an `OutcomeAxes` instance with `provider_operation_status: FAILED` and `provider_data_outcome: NO_DATA` is expected schema-valid. C2.02, by contrast, makes `data_outcome` absent for FAILED/CANCELLED.

This is not treated as a C2.02 blocker because C1.05R1 explicitly left exact C2/C1 serialization to later interface work and C2.06 owns cross-contract wire interfaces. But **C2.06 MUST resolve this seam losslessly**. It must not silently reinterpret a failed operation as genuine provider NO_DATA. If the frozen C1 wire surface cannot represent the C2.02 semantic distinction without semantic distortion, C2.06 must surface a governance incompatibility rather than inventing meaning.

### N03 — "certified endpoint absence semantics" wording is potentially confusing

The invalid-combination section uses the phrase `certified endpoint absence semantics`, while the rest of C2.02 relies on pinned endpoint-profile-authorized absence semantics and C2.05 owns certification/completeness. R1 should replace or explicitly define this phrase so it cannot be read as importing C2.05 certification authority into C2.02.

## Boundary review

PASS:

- FAILED is not coerced into NO_DATA;
- authentication/authorization/rate-limit/server/transport/decode failures remain failures;
- 404-like status is provider-semantic, not globally NO_DATA;
- C3 retry ownership remains intact;
- C4 PIT/revision/available_from ownership remains intact;
- C5 verification/source-fitness ownership remains intact;
- C2.05 completeness/certification ownership remains intact;
- C1 `NO_DATA != NO_MATCH` and partiality constraints remain intact;
- replay refs remain snapshot-stable;
- no provider/vendor selection or production adapter implementation is introduced.

## Final verdict

`FAIL — C2.02R1 SCOPED REPAIR REQUIRED`

Required repair scope is limited to C2OUT-B01..B04 and closely related consistency tests. C2.03 remains NOT AUTHORIZED.
