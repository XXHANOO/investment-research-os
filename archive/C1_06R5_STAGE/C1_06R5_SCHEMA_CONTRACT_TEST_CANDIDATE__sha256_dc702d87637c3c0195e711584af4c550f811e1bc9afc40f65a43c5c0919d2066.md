# C1.06R5 — Query Expected-Target Binding Repair Candidate

Generated: 2026-08-23T18:34:47Z

Status: `CANDIDATE_FOR_C1_06R5_INDEPENDENT_REGRESSION_RECHECK`

Exact R4 parent schema: `C1_06R4_MACHINE_SCHEMA_CANDIDATE__sha256_48ecdff49cec2dbfce91a8f81e97ce7f9a0c94f23168384b9fd7aefd451251cd.json` / `48ecdff49cec2dbfce91a8f81e97ce7f9a0c94f23168384b9fd7aefd451251cd`.

R5 adds `ResolutionQueryBinding`. If the exact source query supplied `expected_target_kind` and the result is `RESOLVED`, the unique target kind must equal it. The result-side echo is machine-enforced in CURRENT_ONLY and TEMPORAL; authenticity against the exact source query is an explicit semantic contract.

Mismatch -> `TARGET_KIND_MISMATCH`.

SchemeDefinition target compatibility remains independently mandatory.

New obligations C1-535..C1-545 are mapped by C1.DEC-181..185.

C1.OPEN-010 remains NOT CLOSED pending independent re-check.
Production implementation remains NOT AUTHORIZED.
Next gate: `C1.06R5 Independent Regression Re-Check`.
