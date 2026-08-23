# C0 Acceptance Test Catalog

Status: CANDIDATE_FOR_C0_R2V2_COVERAGE_REGRESSION_CHECK
Purpose: Machine-checkable obligations for the Frozen C0 architecture.

Tests may be implemented under later owning contracts, but the obligation and intent are defined here.

| ID | Maps To | Test | Required Behavior | Type |
|---|---|---|---|---|
| `C0-001` | `INV-01` | Stable identity survives ticker/listing-symbol change | Changing ticker/provider symbol does not change EntityID/InstrumentID; mapping history changes instead. | `contract` |
| `C0-002` | `INV-02` | Historical query requires as_of | A time-sensitive HISTORICAL query without as_of fails before provider access. | `contract` |
| `C0-003` | `INV-02` | CURRENT mode is explicit | Current-state query cannot rely on omitted as_of to infer semantics; query mode is explicit. | `contract` |
| `C0-004` | `INV-03` | Later filing is invisible | A filing/metric whose available_from is after as_of is not returned. | `contract` |
| `C0-005` | `INV-03` | Coarse availability is conservative | DATE/UNKNOWN availability cannot be exposed earlier than the supported conservative available_from. | `contract` |
| `C0-006` | `INV-04` | Revision-as-of returns historical version | Historical query before a revision returns the old record, not latest. | `contract` |
| `C0-007` | `INV-04` | Revision append preservation | Creating a correction preserves prior version and bitemporal/system history. | `contract` |
| `C0-008` | `INV-05` | HTTP/server/auth/network failure is not NO_DATA | Provider 500/401/network failure raises typed failure; does not return empty as genuine no-data. | `provider-contract` |
| `C0-009` | `INV-05` | Rate-limit exhaustion fails loud | 429 retry policy exhaustion returns typed failure. | `provider-contract` |
| `C0-010` | `INV-05` | Genuine 404/no-data remains domain NO_DATA | Provider-established absence can return NO_DATA without being classified as infrastructure failure. | `provider-contract` |
| `C0-011` | `INV-05` | Operation status and data outcome are separate | FAILED cannot coexist with a silently authoritative NO_DATA result; PARTIAL requires explicit semantics/degradation. | `contract` |
| `C0-012` | `INV-06` | Synthetic origin cannot masquerade as observed | Synthetic/simulated records fail validation if origin is observed. | `contract` |
| `C0-013` | `INV-06` | Orthogonal quality states can coexist | A record can validly be observed+cached+fresh+verified+pit_safe without enum collision. | `schema` |
| `C0-014` | `INV-07` | Provider payload cannot bypass normalization | Domain service rejects native provider payload where canonical type is required. | `dependency/schema` |
| `C0-015` | `INV-08` | Report projection cannot mutate canonical state | Editing/deleting a rendered report leaves Fact/Thesis/Decision stores unchanged. | `integration` |
| `C0-016` | `INV-09` | Same root source is not independent | Two agents/pages citing same root_source_id count as one independent authority. | `contract` |
| `C0-017` | `INV-09` | Republished lineage is deduplicated | Republish/quote chain resolves to root lineage and is not counted as independent corroboration. | `contract` |
| `C0-018` | `INV-10` | Adapter cannot redefine canonical financial policy | Generated or handwritten client adapter changing policy/PIT semantics fails conformance. | `static/conformance` |
| `C0-019` | `INV-11` | Policy threshold single-source | Duplicated material threshold outside canonical PolicyRegistry/reference fails governance/static validation. | `static` |
| `C0-020` | `INV-11` | Release retains policy versions | Released research, DecisionRunRecord, ExperimentRun and ReleaseBundle resolve policy versions actually used. | `contract` |
| `C0-021` | `INV-12` | LLM cannot bypass LIVE risk/order admission | LLM recommendation that violates deterministic risk cannot produce admitted LIVE order. | `integration` |
| `C0-022` | `INV-13` | Duplicate idempotency key does not duplicate side effect | Retry with same idempotency identity creates one external effect. | `integration` |
| `C0-023` | `INV-13` | Non-idempotent action cannot receive unsafe retry policy | Policy validation rejects retries for non-idempotent side effect unless protected by explicit mechanism. | `contract` |
| `C0-024` | `INV-14` | Missing lineage blocks release | Material transformation lacking run/input/code/workflow/policy lineage cannot pass release audit. | `contract` |
| `C0-025` | `INV-14` | Evidence lineage reaches raw/root authority | EvidenceRecord lineage resolves to permitted RawArtifact/root source or explicitly documented external authority. | `contract` |
| `C0-026` | `INV-15` | Research candidate cannot self-promote | Candidate cannot issue/authorize its own PromotionDecision or ReleaseBundle. | `capability` |
| `C0-027` | `INV-15` | LIVE disabled by default | Without explicit LIVE capability/approval, execution remains blocked even if strategy is LIVE_ELIGIBLE. | `security` |
| `C0-028` | `INV-16` | SIM/PAPER/LIVE share canonical order semantics | Equivalent intent produces same canonical order/risk object shape across environments before adapter mechanics. | `contract` |
| `C0-029` | `INV-17` | Critical financial output uses deterministic computation | Market cap/EV/valuation/return/risk output must carry deterministic calculation record or validation record. | `contract` |
| `C0-030` | `INV-18` | Missing load-bearing dependency blocks RELEASE | If a deterministic dependency graph contains unvalidated critical input, artifact cannot reach RELEASED. | `contract` |
| `C0-031` | `INV-19` | Research Memory cannot enter Production context | Unpromoted Reflection/Lesson retrieved from Research Memory is rejected by Production context builder. | `security/contract` |
| `C0-032` | `INV-20` | Positive PnL alone cannot validate lesson | Outcome profit without decision/process validation cannot set LessonCandidate status to VALIDATED/PROMOTED. | `contract` |
| `C0-033` | `INV-20` | Horizon mismatch does not auto-fail thesis | Long-horizon thesis remains unresolved when only short-horizon outcome exists unless policy says otherwise. | `contract` |
| `C0-034` | `INV-21` | Future Reflection invisible in past replay | Reflection created/available after replay as_of is not retrievable. | `contract` |
| `C0-035` | `INV-21` | Derived artifact availability not backdated | available_from >= max(parent availability, materialized_at). | `schema/contract` |
| `C0-036` | `INV-21` | Production memory effective only after promotion | production_effective_from >= PromotionDecision.effective_from. | `contract` |
| `C0-037` | `INV-22` | SEALED_OOS exposure invalidates untouched status | If candidate-generation process receives sealed result, candidate lineage cannot claim untouched SEALED_OOS. | `contract` |
| `C0-038` | `INV-22` | Adaptive trial count is preserved | Promotion record contains experiment count/evaluation exposures for candidate lineage. | `contract` |
| `C0-039` | `INV-23` | Every Production decision resolves ReleaseBundle | DecisionRecord.release_id resolves to complete compatible ReleaseBundle. | `contract` |
| `C0-040` | `INV-23` | Rollback restores complete bundle | Rollback cannot restore strategy while leaving incompatible prompt/policy/memory/tool versions. | `integration` |
| `C0-041` | `INV-24` | Instruction-like external content cannot alter control state | Provider/web/tool text attempting to change policy/capability/workflow is treated as data and ignored as control. | `security` |
| `C0-042` | `INV-24` | External content cannot grant tool capability | Tool/provider response cannot elevate READ to WRITE/LIVE/DESTRUCTIVE capability. | `security` |
| `C0-043` | `INV-25` | Material financial values require unit/currency/scale | Schema validation rejects ambiguous monetary material fact lacking required semantic units. | `schema` |
| `C0-044` | `INV-25` | Timestamp precision/timezone is explicit | Material timestamp is timezone-aware or explicitly date/period-only with precision semantics. | `schema` |
| `C0-045` | `INV-25` | Adjusted price basis is explicit | Adjusted/unadjusted price series cannot be mixed without explicit adjustment basis. | `contract` |
| `C0-046` | `RUN-REPRO` | DecisionRunRecord resolves run lineage | DecisionRecord resolves DecisionRunRecord → ReleaseBundle → inputs/evidence/tool/model/deterministic outputs. | `contract` |
| `C0-047` | `RUN-REPRO` | Stochastic replay not mislabeled exact | Run with non-guaranteed LLM determinism cannot be labeled EXACT_DETERMINISTIC_REPLAY. | `contract` |
| `C0-048` | `RUN-REPRO` | Original stochastic output remains auditable | AUDIT_RECONSTRUCTION can recover protected original structured output/hash and input/evidence references. | `contract` |
| `C0-049` | `SECURE-RAW` | Secret/PII response cannot enter immutable store before ingestion policy | Raw response containing forbidden secret/PII is quarantined/redacted/rejected before Permitted RawArtifact. | `security` |
| `C0-050` | `SECURE-RAW` | Permitted raw hash is immutable | Once admitted as Permitted RawArtifact, content mutation changes content identity rather than overwriting original. | `storage` |
| `C0-051` | `SOURCE-FITNESS` | Claim-type source mismatch is surfaced | Using an inappropriate source class for a load-bearing claim generates validation failure/warning per C5 policy. | `contract` |
| `C0-052` | `PORTS` | Core domain cannot import infrastructure adapters | Static architecture test prevents domain/application imports of provider/broker/client-specific infrastructure. | `static` |
| `C0-053` | `C11-BOUNDARY` | Semantic ownership and persistence ownership remain separate | Repository layer persists Thesis/Release/Audit records without redefining their C9/C12 domain meaning. | `architecture` |
| `C0-054` | `REFLECTION` | Reflection cannot become VerifiedFact directly | ReflectionRecord requires separate evidence/verification path before any derived factual claim can become FactRecord. | `contract` |
| `C0-055` | `COUNTERFACTUAL` | Modeled counterfactual is not observed history | MODEL_BASED/SPECULATIVE counterfactual cannot be labeled EXACT_REPLAY/observed. | `schema` |
| `C0-056` | `PRIVATE-STATE` | Private state is not emitted to public artifact by default | Portfolio/account/private thesis/credentials are excluded or redacted from public report/export path. | `security` |
| `C0-057` | `INV-24` | Untrusted content cannot originate side-effect intent | A malicious webpage/provider/tool payload cannot cause WRITE_EXTERNAL/PAPER_TRADE/LIVE_TRADE/DESTRUCTIVE action merely because the workflow already holds that capability; authorized control intent and destination/egress policy are still required. | `security` |
| `C0-058` | `INV-19` | Research-generated executable candidate is sandboxed | Generated Strategy/Model/tool/code candidate MUST execute inside the Research Sandbox. No lower contract/policy may waive the sandbox boundary; scoped capabilities may be granted only inside it. Broker/live/paper credentials, secrets, network egress and private-state access remain denied unless explicitly scoped within sandbox policy, and access attempts are auditable. | `security/integration` |
| `C0-059` | `EVIDENCE-LEDGER` | Evidence Ledger conforms to frozen schema vocabulary and bidirectional coverage | Every decision uses decision_classification, strongest_evidence_strength, reasoning_basis, evidence_refs, and required_tests; non-null strength values are canonical; every evidence_ref resolves; every Ledger required_test resolves to the catalog; every C0 acceptance obligation is referenced by at least one Ledger decision. | `schema/conformance` |
| `C0-060` | `EVIDENCE-LEDGER` | Load-bearing source refs are remotely resolved, exactly pinned and role-scoped | Repository evidence used by load-bearing decisions MUST resolve `repository + commit + exact file path` against the source repository; the returned blob SHA MUST equal the Ledger blob_sha. Placeholder/non-resolving/mismatched pins fail. source_role and authority_scope are also required. | `governance/remote-conformance` |
| `C0-061` | `C8-C12-OWNERSHIP` | C8 cannot issue authoritative promotion state | C8 may emit EvaluationResult/Candidates but cannot authoritatively issue ValidationRecord, PromotionDecision, or ReleaseBundle; those are C12 semantics. | `architecture/capability` |
| `C0-062` | `C0-AUTHORITY` | Lower contract cannot weaken C0 authority | A later C1–C12 contract that attempts to relax C0 human/live/risk/policy/architecture authority without formal C0 revision fails governance validation. | `governance` |
| `C0-063` | `INV-23` | Production decision has mandatory audit chain | Every Production DecisionRecord has mandatory run_id/release_id and resolves DecisionRecord → DecisionRunRecord → ReleaseBundle. | `contract` |
| `C0-064` | `INV-22` | LLM temporal contamination constrains PIT/OOS labels | Historical LLM-assisted run with UNKNOWN/CONTAMINATED model temporal state cannot claim causal PIT_SAFE, untouched SEALED_OOS, or forward-like evidence where policy requires causal equivalence. | `contract` |
| `C0-065` | `INV-22` | Adaptive best-of-N cannot promote without adjustment | Promotion from an adaptive candidate family fails if based only on unadjusted best-of-N metric; PromotionDecision records applicable anti-overfit/adaptive-search method and version. | `validation` |
| `C0-066` | `RUN-REPRO` | Released run artifacts are immutable/versioned | Released DecisionRunRecord input/evidence/portfolio/memory/output references resolve to immutable/versioned identities with integrity hashes or equivalent; silent content substitution fails audit. | `storage/audit` |
| `C0-067` | `RUN-REPRO` | Actual LLM invocation records mandatory provenance | Any actual LLM invocation records provider, requested/resolved model identifiers as exposed, material inference configuration, invocation time, and input/output artifact/hash references. | `audit` |
| `C0-068` | `C10-PORTFOLIO` | Decision portfolio snapshot is causally and temporally consistent | PortfolioSnapshot used by a decision MUST satisfy both `effective_at <= DecisionRecord.as_of` and `available_from <= DecisionRecord.as_of`, and the decision MUST use the staleness/reconciliation/version state knowable at that boundary. | `contract` |
| `C0-069` | `C9-CONFIDENCE` | Qualitative confidence is not calibrated probability | Uncalibrated LLM/analyst confidence cannot be emitted as calibrated numeric probability; calibrated probability requires defined model/calibration/provenance identity. | `schema/contract` |
| `C0-070` | `C8-LESSON-SCOPE` | Promoted lesson preserves validated scope and supersession | Promoted lesson retains supporting/contradicting lineage and applicable regime/time/confidence/version/supersession semantics; it cannot silently become an unscoped evergreen rule. | `contract` |
