# C2.02R1 Independent Outcome-Semantics Re-Check Report

Generated: 2026-08-24T09:01:06Z

Review type: `INDEPENDENT_OUTCOME_SEMANTICS_RECHECK`

Candidate under review: `C2.02R1 scoped repair candidate`

Production implementation: `NOT_AUTHORIZED`

External / PAPER / LIVE side effects: `NOT_AUTHORIZED`

C2.03: `NOT_AUTHORIZED`

## 1. Exact candidate pins re-checked

```text
repaired normative contract  828b5c8794ad3458afe32ceeb33212cf210024c0ea5de765f7bae1d8e7d279b6
repaired logical model       89d7905961776e47f637c6460bddda33067421328bdb205a30bc60d5901735dc
repair acceptance delta      f548d2041b984c1b881c839689fe7c16fd6d4baa1e9b6f634cb1f2dca6c4877f
repair decision ledger       369248cf6e25169e1b7168773059e36e2cf5d2cdcd7a0ed1fb85ac62988a4bbf
repair diffs                 6a48387438690561b77e972c559827544891da5a0a620df2fbd36d38318637d8
candidate selection          ee8c627ed65b96bed847fff52684eb1e272ee97bec00fe17e85494d45faaeb90
stage report                 4b32eb50d30d962048d2a0b036fc51cf371d1853960cf8bdee6e4d4c0a6acc7d
parent C2.02 review result   192d2ff5406697fccfc475e63abfc0029cc60a6a4d59760e4ed07c17759e5216
```

Mechanical re-hash of the local review target matched each content-addressed filename. The convenience re-check ZIP is non-authoritative; its current SHA-256 is `f0e356ef1b08465b387a755c69662db6abc0181ce2bea5217f25f43369eea5d1`.

## 2. Re-check method

The re-check did not assume that repair construction closed the original findings. It re-attacked:

- compound terminal-condition determinism;
- terminal-phase provenance coherence;
- FAILED/CANCELLED observation admission;
- material-partiality scope determinism;
- the six original failed acceptance obligations (`C2-101`, `C2-113`, `C2-115`, `C2-123`, `C2-125`, `C2-141`);
- all 24 R1 repair obligations (`C2-144..C2-167`);
- C1/C3/C4/C5/C2.05 boundaries;
- the frozen C1 serialization seam reserved for C2.06.

## 3. Original blocker re-check

### C2OUT-B02 — CLOSED

R1 establishes `ProviderOperationOutcome.operation_phase_terminal` as the sole authoritative terminal phase and removes nested failure/cancellation phase fields from the successor logical model. Any legacy duplicate must equal the top-level value or fail as `ADAPTER_INTERNAL / ADAPTER_INVARIANT_VIOLATION`.

The original provenance contradiction is closed.

### C2OUT-B03 — CLOSED

R1 explicitly requires:

```text
FAILED    -> admitted_observation_count = 0 -> C1 normalization NOT_RUN
CANCELLED -> admitted_observation_count = 0 -> C1 normalization NOT_RUN
```

Diagnostic/quarantined/raw-ingress bytes are explicitly non-admitted. Usable incomplete provider records belong to `SUCCESS + PARTIAL` instead.

The original admission ambiguity is closed.

### C2OUT-B01 — NOT CLOSED

R1 materially improves terminal-condition determinism by freezing phase order and defining a same-phase class tie-break. The required adversarial examples cancellation-vs-timeout, error-envelope-vs-authorized-absence, and decode-failure-vs-partiality are deterministic.

However, the tie-break is not total over the full declared candidate domain.

R1 defines:

```text
same phase:
ADAPTER_INTERNAL / invariant failure
> EXPLICIT_CANCELLATION
> other TYPED_FAILURE
```

and then defines a lexical `(failure_family, failure_code)` tie-break only when more than one non-adapter typed failure remains.

There is no deterministic rule for **two or more established `EXPLICIT_CANCELLATION` candidates at the same phase** with different `cancellation_origin` values. Yet the successor `ProviderCancellation` has one scalar `cancellation_origin`. Therefore two conforming adapters can observe the same pinned terminal-candidate set and serialize different cancellation origins while both claim conformance.

This is still a replay/outcome determinism defect within the exact scope of the original compound-terminal-condition blocker.

**Required repair:** define either (a) an exact cancellation-origin precedence/order, or (b) a primary cancellation origin plus stable secondary cancellation-origin lineage. Add an adversarial vector with at least two same-phase explicit cancellation origins.

**Affected R1 obligation:** `C2-145`.

### C2OUT-B04 — NOT CLOSED

R1 correctly defines a deterministic materiality predicate **given** `attempted_response_semantic_refs[]`:

```text
WHOLE_ATTEMPT -> material
RESPONSE_SEMANTIC_SET -> material iff intersection(affected, attempted) != empty
```

and unresolved signal scope now fails closed.

But the load-bearing `attempted_response_semantic_refs[]` set itself is not defined by an exact derivation rule. The contract describes it as the set the concrete attempt "required, after applying" the selected capability, endpoint profile, and explicit request/query semantics, but does not specify an exact set expression or deterministic transformation comparable to C2.01R1's `effective_response_semantic_refs(P,S)` closure.

Because materiality is a function of this set, two conforming adapters can use the same pinned capability/profile/query state yet construct different attempted-response sets and consequently disagree on whether the same provider-native partiality signal is material.

The predicate is deterministic only after accepting an under-specified input; end-to-end classification is therefore still not deterministic.

**Required repair:** freeze an exact derivation of `attempted_response_semantic_refs[]` from the pinned capability/endpoint/query state, including fail-closed handling for any conditional response requirement that cannot be resolved. The rule must not import implicit provider-wide defaults or transitive semantics forbidden by C2.01R1. Add adversarial vectors proving identical pinned attempt semantics yield identical attempted-response scope.

**Affected R1 obligation:** `C2-156`.

## 4. Original failed acceptance obligations

All six original C2.02 failed obligations are now satisfied at their stated contract level:

```text
C2-101 PASS
C2-113 PASS
C2-115 PASS
C2-123 PASS
C2-125 PASS
C2-141 PASS
```

The remaining blockers arise from incompleteness in the R1 repair semantics themselves, not from failure to repair those six original obligation statements.

## 5. R1 acceptance review

Reviewed: `C2-144..C2-167` (24 obligations)

```text
PASS: 22
FAIL: 2
FAIL IDs: C2-145, C2-156
```

- `C2-145` fails because the declared primary-selection rule is not total over multiple same-phase explicit cancellation candidates.
- `C2-156` fails as an attempted-response-scope contract because snapshot stability is defined, but exact derivation of the scope set is not.

All other R1 obligations pass at C2.02 contract level.

Combined targeted re-check surface:

```text
6 original failed obligations + 24 R1 obligations = 30
PASS = 28
FAIL = 2
```

## 6. Non-blocking consistency notes

### N01 — RESOLVED

`ProviderOperationOutcome.diagnostic_retry_hint` is the single authoritative retry advisory. Retry scheduling/policy remains C3-owned.

### N03 — RESOLVED

The wording is now `pinned endpoint-profile-authorized absence semantics`; it does not import C2.05 completeness/certification authority.

### N02 — PRESERVED AS MANDATORY C2.06 OBLIGATION

C2.02R1 correctly does not rewrite frozen C1 serialization. C2.06 must losslessly reconcile frozen C1 `OutcomeAxes` with C2.02 semantic truth and must not reinterpret FAILED as genuine provider NO_DATA.

This remains non-blocking for C2.02R1 because it is explicitly C2.06-owned.

## 7. Boundary review

PASS:

- FAILED/CANCELLED are not coerced into NO_DATA;
- provider infrastructure/protocol/decode failures remain machine-detectable failures;
- C3 retains retry/backoff/quota/cache/freshness policy;
- C4 retains available_from/revision/PIT semantics;
- C5 retains source fitness/verification/conflict;
- C2.05 retains completeness/certification methodology;
- C1 normalization remains NOT_RUN for FAILED/CANCELLED;
- provider NO_DATA remains distinct from C1 NO_MATCH;
- no provider/vendor selection, production adapter, credential mechanism, routing algorithm, or PAPER/LIVE authority was introduced.

## 8. Final verdict

`FAIL — C2.02R2 NARROW REPAIR REQUIRED`

State:

```text
C2OUT-B01 = OPEN_AFTER_R1_RECHECK
C2OUT-B02 = CLOSED
C2OUT-B03 = CLOSED
C2OUT-B04 = OPEN_AFTER_R1_RECHECK

C2.02R1 = INDEPENDENT_RECHECK_FAIL / NOT_FROZEN
C2.02 = REPAIR_REQUIRED_NOT_FROZEN
C2.03 = NOT_AUTHORIZED
```

The next permissible construction is a narrow C2.02R2 repair limited to:

1. total deterministic handling of multiple same-phase explicit cancellations; and
2. exact deterministic derivation of `attempted_response_semantic_refs[]` plus targeted adversarial acceptance vectors.

No production implementation or external/PAPER/LIVE side effect is authorized.
