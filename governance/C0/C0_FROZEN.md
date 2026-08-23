# C0 — System Invariants & Architecture Contract

C0 Candidate Version: 4.1-FR3

Status: C0_FR3_FINAL_CANONICAL_METADATA_SYNCHRONIZATION_COMPLETE_AWAITING_INDEPENDENT_METADATA_REGRESSION_RECHECK
Architecture: v4
Stage: C0-FR3 — Final Canonical Metadata Synchronization
Normative language: MUST / MUST NOT / SHOULD / SHOULD NOT / MAY
Supersession: This document is the C0 4.1-FR3 approval-candidate metadata-synchronization revision. It preserves the Architecture v4 normative semantics of C0 4.1-FR1 and changes only finalization metadata/lifecycle. It remains NOT FROZEN until C0-FR3 Independent Metadata Regression Re-Check, the short Refreshed Final Freeze Review, explicit user approval of the exact Freeze Manifest, and the additive freeze-seal transaction complete.

---

## 0. Authority and Purpose

C0 is the system constitution for the Investment Research OS.

It freezes architecture invariants and cross-contract semantics that later contracts C1–C12 MUST respect. It intentionally does NOT freeze specific framework vendors, database products, queue technologies, UI frameworks, LLM providers, or deployment topology unless the invariant itself requires such a choice.

C0 exists to prevent later implementation convenience from silently weakening:

- point-in-time correctness;
- evidence/provenance integrity;
- financial calculation rigor;
- provider failure semantics;
- policy governance;
- self-improvement safety;
- portfolio/execution risk controls;
- reproducibility and auditability;
- security boundaries.

If a later contract conflicts with a Frozen C0 invariant, the later contract is invalid until C0 is explicitly revised through a migration/ADR process.

```text
C0 FREEZE STATUS: NOT FROZEN
C1 AUTHORIZATION: NOT GRANTED
```

---

# 1. Mission

Build an:

> **Evidence-Centric, Point-in-Time-Safe, Policy-Governed, AI-Native Investment Research Operating System**

Canonical lifecycle:

```text
User Intent
    ↓
Canonical Workflow
    ↓
Data Acquisition
    ↓
Normalization
    ↓
Temporal / PIT Validation
    ↓
Evidence
    ↓
Verified / Derived Facts
    ↓
Analysis / Thesis / Forecast
    ↓
Decision Intent
    ↓
Portfolio Construction / Monitoring
    ↓
Risk
    ↓
Execution Intent
    ↓
Broker Reality
    ↓
Ledger / Audit / Learning
```

The system's durable intellectual assets are:

- Canonical Data;
- Evidence and Provenance;
- PIT / Revision State;
- Policies;
- Thesis and Forecast State;
- Decision History;
- Portfolio / Execution State;
- Experience and Learning State;
- Experiment History;
- Release / Promotion State;
- Audit and Lineage Records.

---

# 2. Explicit Non-Goals

C0 does NOT define the system as:

1. a generic financial terminal UI;
2. an autonomous live-trading bot with unrestricted self-modification;
3. a system where agent agreement substitutes for source verification;
4. a system where Markdown/chat history is the database;
5. a direct clone of Temporal, LEAN, OpenBB, FinceptTerminal, NautilusTrader, Qlib, or any other reference project;
6. an architecture that requires multi-agent operation;
7. a high-frequency trading engine;
8. a system that assumes providers agree;
9. a system that treats search summaries as first-party financial facts;
10. a system where successful backtests automatically graduate to live capital;
11. a system where raw PnL is the sole learning reward;
12. a system where external web/tool/document content can become control instructions.

Multi-agent orchestration MAY be used, but truth, policy, risk, PIT, evidence, and release semantics MUST work with one agent, many agents, or no LLM.

---

# 3. Logical Architecture

Architecture v4 remains a logical map:

1. User / AI Clients
2. Client Adapters
3. Canonical Workflow Registry
4. Research Control Plane
5. Learning & Research Lab
6. Decision Plane
7. Tool Plane
8. Data Access Plane
9. Freshness / Cache / Quota Plane
10. Temporal Evidence Plane
11. Durable State Plane
12. Portfolio / Risk / Execution Plane
13. Governance / Security / Observability Plane
14. Artifact Projection Plane

These are logical responsibilities, not mandatory microservices.

---

# 4. Physical Architecture Constraint

Initial implementation MUST use a **modular-monolith / ports-and-adapters** shape unless a later measured requirement and ADR justify a change.

Preferred physical dependency shape:

```text
domain
application
ports
↑
adapters
persistence
governance / observability
client integrations
```

Rules:

- Domain and Application MUST depend on contracts/ports, not infrastructure implementations.
- Provider SDKs, broker SDKs, MCP clients, database libraries, UI/client specifics, and network libraries MUST remain outside core domain semantics.
- A provider adapter MAY implement a port; the domain MUST NOT import Alpaca/Tushare/AKShare/IBKR/etc. directly.
- Logical planes MUST NOT be mechanically converted into separate services/packages without justification.
- Phase 1 SHOULD default to an embedded relational store such as SQLite plus a content-addressed filesystem raw store unless measured requirements justify another implementation through ADR.
- C0 freezes persistence semantics, not a database vendor.

---

# 5. Frozen-Candidate Invariants

## INV-01 — Ticker Is Not Identity

Ticker, provider symbol, and exchange symbol are mutable mappings, not canonical identity.

The system MUST support stable identity separately from display/listing symbols.

C1 MUST distinguish at least:

```text
EntityID
  ↓
InstrumentID
  ↓
ListingID
  ↓
ContractID where applicable
```

Ticker/provider symbols map to ListingID or ContractID.

---

## INV-02 — Explicit Historical Temporal Semantics

Any query whose answer can depend on information availability, revisions, index membership, corporate actions, prices, portfolio state, provider history, or other time-varying state MUST explicitly declare:

```text
mode = HISTORICAL
as_of = ...
```

Current-state queries MUST explicitly declare CURRENT semantics rather than infer CURRENT from a missing `as_of`.

A time-sensitive historical query without explicit `as_of` MUST fail.

---

## INV-03 — Knowledge Availability Governs PIT

Historical visibility is governed by when information was available to the market/system under the supported evidence model, not merely by the fiscal/statistical period to which it refers.

Minimum rule:

```text
available_from <= as_of
```

A fiscal period ending before `as_of` does not make a later filing visible.

The system MUST NOT fabricate unavailable timestamp precision.

---

## INV-04 — Revisions Are Preserved

Restatements, corrections, revised filings, provider revisions, corrected classifications, and later knowledge MUST be append-preserved.

Historical queries MUST be able to recover the version visible at the requested `as_of`.

No latest-state overwrite may silently destroy historical versions.

---

## INV-05 — Provider Failure Is Not NO_DATA

`NO_DATA` is a domain result, not an infrastructure failure.

Authentication errors, authorization errors, rate-limit exhaustion, network failures, server failures, pagination failures, parse errors, schema failures, and validation failures MUST remain machine-detectable failures.

The result model MUST separate:

```text
operation_status:
  SUCCESS | FAILED | CANCELLED

data_outcome:
  PRESENT | NO_DATA | PARTIAL   # meaningful only where operation semantics permit

degradations:
  typed metadata such as fallback/stale/quota-pressure

errors:
  typed structured failures
```

A failed operation MUST NOT be converted to an empty collection that looks like genuine no-data.

Critical CLI/tool failure MUST produce machine failure status independently of human-readable text.

---

## INV-06 — Data State Is Multi-Dimensional

The system MUST NOT encode data truth with one flat enum such as:

```text
REAL / DELAYED / CACHED / STALE / SYNTHETIC
```

These concepts are orthogonal.

At minimum, canonical data/evidence MUST be capable of expressing:

```text
origin:
  observed | estimated | synthetic | simulated

delivery:
  live | delayed | cached

freshness:
  fresh | stale | unknown

verification:
  unverified | cross_checked | verified

temporal:
  pit_safe | pit_unknown | pit_unsafe
```

Synthetic, simulated, or estimated data MUST NOT silently masquerade as observed data.

---

## INV-07 — Canonical Normalization Boundary

Provider-native payloads MUST NOT become domain truth directly.

Canonical path:

```text
Provider Native Payload
→ Provider Adapter
→ Validation
→ Normalization
→ Canonical Model
```

Raw provider structure MAY be preserved for provenance, but downstream domain logic MUST consume canonical types.

---

## INV-08 — Reports Are Projections

Markdown, HTML, PDF, chat responses, dashboards, and generated reports are projections of canonical state.

They MUST NOT be authoritative stores for:

- facts;
- evidence;
- thesis state;
- decisions;
- policies;
- portfolios;
- learning state;
- release state.

Changing a rendered report MUST NOT mutate canonical state unless an explicit structured write operation is performed through an authorized contract.

---

## INV-09 — Agent Agreement Is Not Evidence Independence

Multiple agents, URLs, or articles do not constitute independent verification when they derive from the same underlying source.

Evidence independence MUST be based on lineage.

C5 MUST support concepts such as:

```text
source_claim_id
root_source_id
parent_evidence_ids
derivation_type:
  original | quote | republish | transform | inference
```

Two pages quoting the same SEC filing count as one root authority for independence purposes.

---

## INV-10 — Skill / Client Adapter Is Not Canonical Business Logic

Skills, prompts, generated client adapters, and handwritten client adapters MAY orchestrate workflows and presentation.

They MUST NOT be the only canonical home for:

- financial formulas;
- risk rules;
- provider-routing rules;
- PIT rules;
- quota rules;
- verification tolerances;
- audit thresholds;
- promotion criteria;
- execution permissions.

Canonical business semantics live in versioned contracts, deterministic tools, and policy records.

---

## INV-11 — Policy Has One Canonical Source

Every material policy has:

```text
policy_id
version
scope
severity
parameters
effective_from
supersedes
```

Prompts, workflows, tools, and adapters reference canonical policy versions.

A threshold copied into multiple uncontrolled locations is governance drift and MUST fail policy/conformance validation.

Every released research artifact, experiment, decision run, and ReleaseBundle MUST retain relevant policy-version references.

---

## INV-12 — LLM Cannot Override Deterministic Risk or Execution Controls

LLMs MAY produce:

- research views;
- hypotheses;
- qualitative analysis;
- theses;
- forecasts;
- signals;
- recommended allocations.

They MUST NOT override deterministic:

- position limits;
- buying-power checks;
- margin constraints;
- leverage limits;
- order-admission rules;
- broker capability restrictions;
- reconciliation blocks;
- live-trading permissions.

Risk/execution admission is authoritative code/policy behavior.

---

## INV-13 — External Side Effects Have Explicit Semantics

Every side-effecting Activity/tool operation MUST declare:

```text
side_effect_class
idempotency_semantics
retry_policy
max_attempts
timeout
cancellation_behavior
```

Idempotent operations MAY be retried according to policy.

Non-idempotent operations MUST NOT be assumed idempotent; they may use zero-retry, deduplication/idempotency keys, transactional outbox, compensating action, or explicit at-most-once semantics.

Duplicate retry MUST NOT silently duplicate external effects.

---

## INV-14 — Material Transformations Are Lineage-Traceable

Every material transformation MUST be traceable to:

- input identifiers/snapshots;
- output identifiers;
- run_id;
- workflow/tool/code version;
- relevant policy versions;
- timestamps;
- source/provider metadata as applicable.

Lineage semantics are required; deployment of an OpenLineage server is not.

---

## INV-15 — Research Cannot Self-Promote

Research artifacts are candidates.

A research result, model, strategy, lesson, prompt variant, or agent output MUST NOT directly become Production behavior without:

```text
evaluation
→ validation
→ promotion decision
→ versioned release
→ rollback capability
```

Live-capital changes, deterministic risk-limit changes, canonical policy changes, and architecture changes require explicit human authorization under the default C0 security posture.

This authority may be relaxed only through the formal C0 revision/migration process. Lower contracts MAY define approval mechanics, but MUST NOT weaken, bypass, or redefine C0 authority.

LIVE capability is disabled by default.

## INV-16 — SIM / PAPER / LIVE Share Domain Semantics, Not Identical Mechanics

SIM, PAPER, and LIVE MUST share canonical:

- identity semantics;
- signal/decision semantics;
- portfolio-intent semantics;
- risk-policy semantics;
- order/event models;
- ledger concepts.

Environment-specific adapters MAY differ in:

- latency;
- fills;
- partial fills;
- rejects;
- session behavior;
- venue rules;
- fees;
- slippage;
- borrow;
- margin;
- buying power;
- corporate-action handling.

The system MUST NOT duplicate separate business strategies for each mode merely to accommodate environment differences.

---

## INV-17 — Critical Financial Computation Is Deterministic

Load-bearing arithmetic MUST be computed or validated by deterministic tools rather than unverified LLM arithmetic.

Examples include:

- market capitalization;
- enterprise value;
- free cash flow;
- per-share values;
- valuation formulas;
- returns;
- drawdowns;
- portfolio weights;
- exposure;
- risk constraints;
- transaction-cost calculations.

Deterministic computation verifies the calculation, not the truth of the input. Inputs remain evidence/PIT obligations.

---

## INV-18 — Load-Bearing Dependencies Receive 100% Validation

Facts and assumptions that materially support a released conclusion MUST receive full pre-release validation.

Where possible, load-bearing dependencies SHOULD be discovered by deterministic dependency graphs rather than only by LLM labeling.

Example:

```text
Valuation Result
├── Revenue
├── Margin
├── Tax
├── Capex
├── NWC
├── Discount Rate
├── Terminal Assumption
├── Debt
├── Cash
└── Diluted Shares
```

Audit tiers MAY sample lower-impact material, but Tier-1/load-bearing dependencies are 100% checked.

---

## INV-19 — Unvalidated Learning Cannot Alter Production Behavior

No unvalidated:

- ReflectionRecord;
- LessonCandidate;
- HypothesisCandidate;
- candidate memory;
- model update;
- strategy change;
- parameter;
- prompt fragment;
- workflow branch;
- policy proposal;
- research-generated executable artifact;

may alter Production behavior.

This prohibition includes indirect behavior change through retrieval/context injection.

Research Memory and Production Memory are separate trust domains.

Research-generated executable StrategyCandidate, ModelCandidate, tool, script, or code artifact MUST execute only inside a restricted Research Sandbox. No lower contract, workflow, capability policy, experiment policy, or runtime configuration may waive the Research Sandbox boundary. Lower-level policy MAY grant narrowly scoped resources or capabilities only within that boundary. Changing or removing the Research Sandbox boundary requires the formal C0 revision/migration process. The default sandbox MUST deny broker/live/paper credentials and execution authority, secrets, uncontrolled network egress, and uncontrolled filesystem/private-state access. Candidate execution MUST use pinned dependency/environment identity where feasible, pass static/runtime validation appropriate to the artifact, and emit auditable resource/capability access records.

Exact sandbox/container technology is deferred to C6/C8/C12; the trust boundary is frozen here.

## INV-20 — Outcome Is Not Decision Ground Truth

Raw PnL alone MUST NOT be treated as proof of decision quality.

Learning/evaluation MUST distinguish:

```text
Outcome Quality
vs
Decision / Process Quality
```

Evaluation MAY include:

- benchmark-relative performance;
- factor/sector/style attribution;
- idiosyncratic alpha;
- risk taken;
- drawdown;
- transaction costs;
- forecast calibration;
- thesis correctness;
- evidence quality;
- process compliance;
- expected-horizon appropriateness.

Profit does not imply correct reasoning; loss does not imply incorrect reasoning.

---

## INV-21 — Learning Is Point-in-Time Bound

Every learning artifact MUST be temporally versioned and unavailable before it actually exists and its dependencies are available.

For a derived learning artifact:

```text
available_from
>= max(
    all dependency available_from values,
    materialized_at
)
```

Minimum fields:

```text
artifact_id
source_episode_ids
parent_ids
source_knowledge_cutoff
materialized_at
available_from
classification
status
version
```

For Production Memory:

```text
production_effective_from
>= PromotionDecision.effective_from
```

Historical replay MUST use `available_from` / `production_effective_from`, never the underlying economic event date.

No future outcome, reflection, lesson, model update, strategy version, or promoted memory may leak backward.

---

## INV-22 — Evaluation Cannot Be Trained Away

If an evaluation result influences candidate generation, parameter tuning, prompt tuning, model selection, strategy selection, or future hypothesis generation, that evaluation set is no longer untouched for that candidate lineage.

Evaluation roles:

```text
TRAIN
VALIDATION
RESEARCH_OOS
SEALED_OOS
FORWARD_PAPER
```

Rules:

- TRAIN and VALIDATION may be repeatedly consumed.
- RESEARCH_OOS may inform research but every exposure is logged.
- SEALED_OOS MUST NOT be iteratively exposed to candidate-generation logic.
- FORWARD_PAPER is unseen at initiation for the evaluated candidate lineage; once observed, it becomes part of exposure history for later adaptive candidate lineages.
- Any leak/exposure invalidates untouched status.
- Promotion MUST record adaptive trial counts and evaluation reuse.
- Promotion MUST apply an anti-overfitting / adaptive-search control appropriate to the experiment family and MUST record the method and version used. An unadjusted best-of-N result from an adaptive search family is insufficient by itself for promotion.

Historical LLM-assisted evaluation also has model-side temporal contamination risk. Every such evaluation MUST classify:

```text
model_temporal_contamination:
  CONTROLLED
  UNKNOWN
  CONTAMINATED
```

The run MUST record the LLM provider, requested/resolved model identifier as exposed by the provider, and any known model knowledge boundary or contamination-control method.

If model temporal contamination is UNKNOWN or CONTAMINATED, an evaluation policy that requires causal historical equivalence MUST NOT label the run fully `PIT_SAFE`, untouched `SEALED_OOS`, or forward-like evidence.

Permitted control approaches MAY include an appropriate-cutoff model, masking/anonymization, deterministic non-LLM evaluation, or another validated contamination-control method. Exact methods and thresholds belong to C8/C12.

## INV-23 — Production Behavior Is a Versioned ReleaseBundle

Every Production decision MUST reference a complete `release_id`.

A ReleaseBundle identifies the configured Production behavior:

```text
release_id
strategy_version
model_config_version
workflow_version
prompt_bundle_version
policy_bundle_version
risk_version
production_memory_snapshot
provider_config_version
tool_bundle_version
schema_versions
git_sha
released_at
approval_record
rollback_target
status
```

Rollback MUST restore a complete compatible ReleaseBundle, not an arbitrary subset of components.

---

## INV-24 — External Content Is Untrusted Data, Never Control Authority

Content obtained from:

- providers;
- tools;
- webpages;
- filings;
- documents;
- news;
- search engines;
- market feeds;
- model-generated memories;
- third-party APIs;

MUST be treated as untrusted DATA.

Instruction-like text embedded in external content MUST NOT modify:

- canonical workflow;
- system/developer policy;
- capability grants;
- tool permissions;
- security policy;
- release state;
- execution authority;
- live-trading permission.

Only explicitly authorized control channels may change control state.

External content cannot grant itself permissions.

Untrusted data also MUST NOT originate, expand, redirect, retarget, or replace side-effect intent by exploiting a capability that was already granted. Any `WRITE_EXTERNAL`, `PAPER_TRADE`, `LIVE_TRADE`, or `DESTRUCTIVE` action MUST be attributable to authorized user/workflow control intent and MUST pass applicable destination/egress/capability policy.

External content MAY influence analysis within the Data Plane, but cannot create a new side-effect objective.

The Control Plane and Data Plane therefore have an explicit trust boundary, including trusted-intent binding for side effects.

## INV-25 — Units, Currency, Scale, Precision, and Timezone Are Explicit

Material numeric facts MUST carry sufficient semantic metadata to prevent silent unit errors.

As applicable, canonical values MUST explicitly represent:

```text
unit
currency
scale
per_share / aggregate basis
adjustment basis
precision
```

Material timestamps MUST be either:

- timezone-aware timestamps; or
- explicitly date-only / period-only values with declared precision and authority timezone/semantics.

The system MUST NOT fabricate intraday precision from a date-only source.

Adjusted and unadjusted market-price semantics MUST be explicit in C1/C4.

---

# 6. Temporal Model

C0 freezes four semantic time concepts:

### event_time
When the underlying economic/market event occurred.

### period_time
The accounting/statistical period represented by the datum.

### knowledge_time / available_from
When the datum or derived artifact became supportably available under the evidence model.

`available_from` is the **single authoritative historical visibility boundary**. No second effective-visibility field may compete with it.

### system_time
When a version of the record entered, changed, or was superseded in this system.

Auxiliary provenance metadata MAY include:

```text
retrieved_at
provider_timestamp
published_at
filed_at
received_at
```

These are not silently substituted for one another.

Historical visibility is:

```text
available_from <= as_of
```

subject to applicable quality, authorization, and reconstructability policy.

---

## 6.1 Availability Precision and Conservative Visibility

Availability precision MUST be carried explicitly, e.g.:

```text
SECOND
MINUTE
DATE
PERIOD
UNKNOWN
```

If exact availability is uncertain, C0 requires conservative treatment.

Minimum semantic representation:

```text
available_from
availability_basis
availability_precision
availability_interval:
  earliest_possible
  latest_supported
```

For coarse or uncertain source precision, `available_from` MUST be the conservative supported visibility time. It MUST NOT be fabricated as the start of a day, period, or other earlier boundary merely because the source lacks finer precision.

Historical replay MUST use this same `available_from` field for Evidence, Facts, portfolio/time-varying state, and learning artifacts.

Temporal reconstructability MUST be representable at least as:

```text
PIT_SAFE
PIT_UNVERIFIED
UNRECONSTRUCTABLE
```

If a provider or source cannot support a defensible historical availability boundary, the system MUST record `PIT_UNVERIFIED` or `UNRECONSTRUCTABLE`; it MUST NOT fabricate PIT safety.

C4 defines exact field schemas.

---

## 6.2 Bitemporal Compatibility

Records that can change over knowledge/system time SHOULD support concepts equivalent to:

```text
known_from / known_until
stored_from / superseded_at
```

Revisions append; they do not erase prior history.

# 7. Trust DAG

The system MUST NOT model epistemic state as one linear ladder.

Canonical semantic graph:

```text
RawArtifact
    ↓
EvidenceRecord
    ↓
FactRecord
   ↙       ↘
DerivedFact  Inference
      \       /
      Thesis / Forecast
             ↓
        Decision Intent
```

Key distinctions:

- `RawArtifact` is source material after secure-ingestion eligibility.
- `EvidenceRecord` links a claim/evidence item to source/provenance.
- `FactRecord` is a supported factual assertion.
- `DerivedFact` is deterministic or explicitly specified derivation from facts.
- `Inference` is interpretive, probabilistic, causal, or qualitative reasoning.
- `Thesis/Forecast` synthesizes facts and inferences.
- `Decision Intent` is not a fact.

Reflection output defaults to `INFERRED`, not `VERIFIED_FACT`.

---

# 8. Evidence Independence and Claim Lineage

C5 MUST support enough lineage to distinguish:

```text
SEC filing
  ├── news article A quoting filing
  └── blog B quoting article A
```

from truly independent evidence.

Minimum conceptual fields:

```text
evidence_id
claim_id
source_claim_id
root_source_id
parent_evidence_ids
derivation_type
source_locator
content_hash
retrieved_at
available_from
```

Root-source independence is necessary but not always sufficient; syndicated/derived relationships may require a lineage graph.

---

# 9. Claim-Type Source Fitness

C0 does not freeze a universal ranking such as `FIRST_PARTY > PROVIDER > SECONDARY`.

Source authority is evaluated relative to the claim.

Examples:

| Claim Type | Preferred Authority |
|---|---|
| Regulatory filing fact | regulator / official filing |
| Current trade/quote | exchange or appropriate market-data authority/provider |
| Management guidance | company IR / filing |
| Legal ruling | court / regulator |
| Official macro statistic | issuing agency / central bank |
| Analyst consensus | structured consensus provider |
| Company claim about itself | first-party evidence that the company made the claim, not automatic proof of objective truth |
| Rumor | discovery only until corroborated |

C5 defines fitness scores, conflict logic, and source-quality policy.

---

# 10. Secure Raw Ingestion

Raw immutability starts after a security/licensing boundary.

```text
External Response
    ↓
Secure Ingestion Boundary
    ├── credential / secret scan
    ├── PII / privacy classification
    ├── license / redistribution classification
    ├── retention classification
    └── quarantine / redact / reject as required
    ↓
Permitted RawArtifact
    ↓
Content-addressed immutable storage
```

A RawArtifact MAY later be tombstoned/quarantined or access-restricted under legal/security/retention policy while retaining audit metadata where permitted.

Secrets MUST NOT be preserved merely to satisfy immutability.

---

# 11. State-of-Truth Matrix

| Domain | Canonical Source of Truth | Not Authoritative |
|---|---|---|
| Entity / Instrument identity | Instrument Registry / Store | ticker text |
| Provider capability | Provider Registry | README claims |
| Provider raw source | Permitted RawArtifact Store | transformed report |
| PIT visibility | Temporal Store / temporal fields | latest API result |
| Evidence | Evidence Store | citation prose |
| Facts | Fact Store | agent message |
| Policy | Policy Registry | prompt copy |
| Workflow | Canonical Workflow Registry | client adapter |
| Task state | Task Journal | chat history |
| Thesis / Forecast | Thesis Store | Markdown memo |
| Decision | Decision Ledger | assistant prose |
| Experience | Experience Ledger | ad-hoc notes |
| Research Memory | Research Memory Store | prompt history |
| Production Memory | versioned Production Memory snapshot | unvalidated reflection |
| Experiment | Experiment Store | report text |
| Portfolio SIM | Simulation Ledger | report |
| Portfolio PAPER/LIVE | broker/custodian operational state + reconciled internal projection | stale internal assumption |
| Promotion / Release | Promotion / Release Registry | candidate report |
| Audit / Validation | Validation/Audit Store | console text |

All private durable state SHOULD carry an `owner_scope` / namespace even in the initial single-user implementation to avoid later ownership ambiguity.

---

# 12. Portfolio Truth and Reconciliation

### SIM
The internal simulation ledger is operational truth.

### PAPER
Where a paper broker exists, paper-broker execution state is external execution truth; internal state is a reconciled projection.

### LIVE
Broker/custodian state is external operational truth.

Internal Portfolio Ledger is the auditable synchronized projection.

Material mismatch produces a `ReconciliationRecord`.

Policy MAY place the system in:

```text
RECONCILIATION_BLOCK
```

until resolved.

The system MUST NOT continue LIVE actions on material unreconciled state when policy says execution is blocked.

---

# 13. Workflow and Durable Task Semantics

Canonical workflow definition SHOULD be declarative and versioned:

```text
workflow_id
version
inputs
required_capabilities
optional_capabilities
steps
policies
budgets
outputs
audit_profile
```

Typical lifecycle:

```text
PREFLIGHT
→ RESOLVE_IDENTITY
→ ACQUIRE
→ NORMALIZE
→ TEMPORAL_VALIDATE
→ EVIDENCE
→ VERIFY
→ ANALYZE
→ SYNTHESIZE
→ AUDIT
→ RELEASE
```

Durable task states SHOULD support:

```text
CREATED
PREFLIGHT
RUNNING
WAITING
PAUSED
RETRYING
BLOCKED
FAILED
COMPLETED
CANCELLED
```

Task state MUST be durable outside chat history.

Early implementation MAY use an append-only TaskJournal rather than Temporal.

---

# 14. Workflow vs Side-Effect Activity

Deterministic orchestration and external side effects are conceptually separate.

Network calls, filesystem writes, database writes, external messages, broker actions, and other side effects MUST be represented as Activities/tool operations with explicit INV-13 semantics.

Cancellation, timeout, retries, and budget exhaustion MUST be auditable.

---

# 15. Client Adapter Contract

The Canonical Workflow Registry is the semantic source of truth.

Client adapters MAY be:

- generated;
- handwritten;
- partially generated.

Every adapter MUST pass conformance tests proving that it does not redefine:

- finance policy;
- PIT semantics;
- risk rules;
- provider semantics;
- audit gates;
- release semantics.

Presentation and interaction MAY differ by client.

---

# 16. Tool / MCP / Capability Contract

Critical tools MUST use structured output.

Minimum envelope concept:

```text
operation_status
result
warnings
degradations
errors
policy_versions
provenance
run_id
```

Natural-language strings such as `✅ Looks good` are not machine success contracts.

Safety/capability classes SHOULD include:

```text
READ
ANALYZE
WRITE_LOCAL
WRITE_EXTERNAL
PAPER_TRADE
LIVE_TRADE
DESTRUCTIVE
```

MCP/tool annotations are metadata/hints, not authorization.

Actual authorization is enforced by Capability + Policy.

Capability preflight SHOULD return:

```text
READY
DEGRADED
BLOCKED
```

The system MUST NOT fabricate a critical missing input merely to continue.

`INSUFFICIENT_EVIDENCE` is a valid research outcome.

---

# 17. Policy Governance

Policy is data with identity/version, not copied prose.

Minimum semantic record:

```text
policy_id
version
scope
severity
parameters
effective_from
supersedes
status
```

Runs and releases retain the policy versions actually used.

Threshold changes require version change.

---

# 18. Run Lineage and Decision Reproducibility

`ReleaseBundle` identifies configured Production behavior.

It is necessary but not sufficient for stochastic LLM audit/reproduction.

Every Production-facing DecisionRecord MUST resolve through:

```text
DecisionRecord
   ↓
DecisionRunRecord / RunArtifactBundle
   ↓
ReleaseBundle
```

Minimum run-level semantics:

```text
run_id
decision_id
release_id
as_of
query_mode
workflow_version
policy_versions
input_snapshot_ids
evidence_snapshot_ids
portfolio_context_ref
production_memory_snapshot
model_invocations
tool_invocations
deterministic_output_refs
final_structured_output_ref/hash
started_at
completed_at
status
lineage
replay_level
```

Once a DecisionRunRecord is released/audited, its referenced input, evidence, portfolio-context, memory, deterministic-output, and final-output artifacts MUST resolve to immutable/versioned content with integrity hashes or equivalent immutable version identity. Retention, licensing, privacy, or tombstone policy MAY later restrict access, but MUST NOT silently substitute different content under the same identity.

For every actual LLM invocation, the run record MUST capture, as exposed/available from the provider:

```text
provider
requested_model_identifier
resolved_model_identifier
material inference configuration
invocation timestamp
input artifact/hash references
output artifact/hash references
```

It SHOULD additionally capture when available:

```text
model/version fingerprint
seed
provider request/response identifiers
prompt_template_version/hash
tool-call IDs/output hashes
non-determinism flags
```

Sensitive prompt/output content MAY be stored only in protected artifacts; default logs SHOULD prefer hashes/structural metadata.

---

## 18.1 Reproducibility Levels

The system MUST NOT claim a stronger replay guarantee than technically supported.

```text
EXACT_DETERMINISTIC_REPLAY
```
Deterministic components can reproduce exact outputs from frozen inputs/configuration.

```text
CONFIGURATION_REPLAY
```
The same frozen inputs/configuration can be rerun, but stochastic/provider-hosted LLM equality is not guaranteed.

```text
AUDIT_RECONSTRUCTION
```
The original input/output/tool/decision artifacts are preserved sufficiently to explain the historical decision without regenerating the same LLM output.

A stochastic LLM run MUST NOT be labeled EXACT_DETERMINISTIC_REPLAY unless exact equality is genuinely guaranteed.

# 19. Research Artifact Release State

Research artifacts MAY use:

```text
DRAFT
EVIDENCED
VERIFIED
AUDITED
RELEASED
```

Failure/retirement states MAY include:

```text
BLOCKED
REJECTED
SUPERSEDED
```

Only RELEASED research is considered formally released research output.

This is separate from Production strategy/model promotion.

---

# 20. Thesis / Forecast State

Thesis is structured state, not only prose.

Minimum concepts:

```text
thesis_id
instrument_id
as_of
core_thesis
assumptions
red_lines
valuation_anchors
risk_factors
evidence_links
forecast_horizon
confidence
created_at
updated_at
```

Assumption state MAY include:

```text
SUPPORTED
UNCHANGED
WEAKENED
BROKEN
UNKNOWN
```

Thesis drift must be evidence-driven rather than merely wording-driven.

---

## 20.1 Qualitative Confidence vs Calibrated Probability

`qualitative_confidence` is not equivalent to `calibrated_probability`.

A numeric probability presented as calibrated MUST be produced by a defined/calibrated forecasting or probabilistic model and MUST carry model/provenance/calibration identity.

LLM judgment or analyst confidence without such calibration MUST be represented as qualitative confidence or explicitly labeled as a non-calibrated estimate. The system MUST NOT silently convert rhetorical confidence into calibrated probability.


# 21. Decision Record

A Production-facing `DecisionRecord` MUST include:

```text
decision_id
instrument_id
as_of
decision_intent
run_id
release_id
policy_versions
created_at
```

The following MUST be present when applicable; when not applicable, the record MUST carry an explicit absence reason rather than silently omit decision context:

```text
thesis_id
forecast_ref
fact_snapshot_ref
valuation_snapshot_ref
portfolio_context_ref
```

Mandatory audit chain:

```text
DecisionRecord
→ DecisionRunRecord
→ ReleaseBundle
```

`portfolio_context_ref` is an opaque reference at C9 level; C10 owns PortfolioSnapshot semantics.

This avoids a C9↔C10 schema cycle while retaining mandatory portfolio-aware auditability when portfolio state influences the decision.

# 22. Watchlist Event Model

News itself is not automatically an alert.

Preferred flow:

```text
Event
→ Evidence Update
→ Fact Change
→ Affected Thesis Assumption
→ Thesis Drift
→ Materiality / Action Threshold
→ Alert
```

Watchlist automation should prioritize thesis-relevant material change rather than raw news volume.

---

# 23. Learning & Self-Improvement Architecture

The system supports experience-driven improvement, not uncontrolled self-modification.

## 23.1 Fast Experience Loop

```text
Frozen ReleaseBundle N
→ PAPER / SHADOW decision
→ ExperienceEpisode
→ Outcome maturation
→ Attribution
→ ReflectionRecord
→ LessonCandidate
→ Research Memory
```

This loop MAY run frequently/daily.

It does not change Production behavior.

## 23.2 Slow Improvement Loop

```text
Research Memory
→ HypothesisCandidate
→ Strategy / Model Candidate
→ Deterministic Experiments
→ Walk-forward / OOS / Cost / Stress / Regime tests
→ Challenger
→ SEALED_OOS / FORWARD_PAPER
→ C12 Validation / Promotion Audit
→ Approval
→ Production Memory / ReleaseBundle N+1
```

Core rule:

```text
LEARN != DEPLOY
```

## 23.3 Research Execution Sandbox

Any research-generated executable StrategyCandidate, ModelCandidate, script, tool, or code artifact MUST execute inside the Research Sandbox defined by INV-19.

Default sandbox posture:

```text
broker credentials: DENY
LIVE_TRADE: DENY
PAPER_TRADE: DENY unless explicitly granted for controlled evaluation
secrets/private account state: DENY
network egress: DENY or destination-allowlisted
filesystem/private-state access: DENY or scoped
dependency/environment identity: PINNED where feasible
static/runtime validation: REQUIRED as applicable
resource/capability access audit: REQUIRED
```

C6/C8/C12 own exact capability, sandbox, validation, and promotion mechanics.

# 24. Memory Trust Domains

### Episodic Memory
Observed/recorded experience:

- decisions;
- fills;
- outcomes;
- market context.

### Research Memory
Unpromoted research state:

- ReflectionRecords;
- failed hypotheses;
- candidate lessons;
- counterfactuals;
- experiment results;
- causal hypotheses.

ReflectionRecord default epistemic classification is `INFERRED`.

### Production Memory
Only promoted/versioned knowledge allowed to affect Production decisions.

Any Production Memory change requires a new versioned snapshot and therefore a new/updated ReleaseBundle.

A promoted lesson MUST remain scoped to what was actually validated. C8/C12 semantics MUST preserve, as applicable:

```text
supporting episode / experiment lineage
contradicting evidence
regime scope
time scope
confidence / maturity
version
supersedes / superseded_by history
```

Promotion MUST NOT silently convert a local/noisy lesson into an unscoped evergreen global rule. Supersession is versioned/non-destructive.

# 25. Experience / Outcome / Attribution and Promotion Ownership

C8 owns the research/learning semantics of:

```text
ExperienceEpisode
OutcomeRecord
AttributionRecord
ReflectionRecord
LessonCandidate
HypothesisCandidate
StrategyCandidate
ModelCandidate
ExperimentRun
EvaluationResult / candidate metrics
ChampionVersion / ChallengerVersion references
```

C12 exclusively owns the authoritative governance semantics of:

```text
ValidationRecord
PromotionDecision
ReleaseBundle issuance
release / audit status
```

C8 MAY reference C12 ValidationRecord/PromotionDecision/ReleaseBundle records, but MUST NOT authoritatively define or issue its own promotion/release decision.

C11 persists C8/C12 records through repository ports; persistence ownership does not transfer domain authority.

Outcome evaluation SHOULD be horizon-matched.

A long-horizon thesis MUST NOT be marked failed solely because of next-day price movement.

An unresolved outcome is a valid state.

# 26. Counterfactual Classification

Counterfactuals MUST state their epistemic status:

```text
EXACT_REPLAY
MODEL_BASED
SPECULATIVE
```

A modeled or speculative counterfactual MUST NOT be represented as observed history.

---

# 27. Evaluation Quarantine

Evaluation lineage MUST record dataset/window exposure by candidate lineage.

If a candidate-generation process observes an evaluation result, the system records that exposure and the evaluation is no longer untouched for that lineage.

`FORWARD_PAPER` means unseen at initiation for the evaluated candidate lineage. Once observed, it is part of the exposure history for any later adaptive candidate lineage.

Historical LLM-assisted evaluation MUST additionally record:

```text
model_temporal_contamination
model provider
requested/resolved model identifier
known knowledge boundary when available
contamination-control method/version when used
```

If contamination is UNKNOWN or CONTAMINATED, policies requiring causal historical equivalence MUST reject `PIT_SAFE`, untouched `SEALED_OOS`, or forward-like labels.

Promotion policy MUST apply an anti-overfitting / adaptive-search control appropriate to the experiment family and record its method/version. Exact method is not frozen by C0.

Permitted methods MAY include:

- rolling/nested OOS;
- CPCV/PBO;
- deflated Sharpe;
- multiple-testing correction;
- selection-adjusted confidence;
- independent forward paper evidence;
- another validated control.

Exact thresholds are C8/C12 policy, not frozen in C0.

# 28. Research Promotion Lifecycle

A canonical lifecycle MAY use:

```text
IDEA
→ CANDIDATE
→ BACKTESTED
→ VALIDATED
→ APPROVED
→ PAPER
→ LIVE_ELIGIBLE
```

No Agent, Reflection, Candidate, or C8 research component may jump directly to LIVE or issue authoritative promotion/release state.

Before C12 can issue a PromotionDecision, the promotion record MUST identify the applicable evaluation exposure lineage, adaptive trial/search history, and anti-overfit/adaptive-search method/version required by policy.

An unadjusted best-of-N metric from a large adaptive candidate family is insufficient by itself for promotion.

LIVE_ELIGIBLE does not itself grant LIVE permission.

# 29. Portfolio / Risk / Execution Separation

Canonical flow:

```text
Signal / Decision Intent
→ Portfolio Construction
→ Deterministic Risk
→ Execution Intent
→ Broker Reality
→ Order / Execution Event
→ Reconciliation / Ledger
```

Any portfolio context used by a historical or Production-facing decision MUST resolve to a versioned `PortfolioSnapshot` whose effective time is not after the decision boundary:

```text
PortfolioSnapshot.effective_at <= DecisionRecord.as_of
```

C10 policy MUST also evaluate snapshot staleness and reconciliation status. A materially unreconciled LIVE broker/internal-ledger divergence MUST be surfaced and MAY block dependent decisions/actions according to policy.

Broker reality includes:

- supported asset classes;
- order types;
- trading sessions;
- margin;
- buying power;
- fees;
- fills;
- restrictions;
- fractional support;
- short/borrow support;
- currency/FX behavior;
- corporate-action behavior.

A broker adapter is not merely `place_order()`.

# 30. Security and Privacy

Secrets MUST NOT be stored in:

- repository files;
- public examples;
- reports;
- prompt history by default;
- evidence text;
- normal logs.

Use environment/keychain/encrypted local storage or another approved secret mechanism.

Private user state includes:

- broker/account data;
- holdings;
- private portfolio notes;
- tax data;
- risk profile;
- private thesis;
- credentials.

Private state MUST NOT enter public repository/package/examples.

Every private durable record MUST carry an explicit `owner_scope` or equivalent ownership namespace sufficient to prevent cross-user/account/context ambiguity. C0 does not require full multi-tenancy; it does require explicit ownership identity.

Tests use synthetic fixtures.

Default logs SHOULD record structural metadata such as:

```text
run_id
tool/provider
timestamps
latency
status
token/cost metadata
error class
artifact hashes
```

rather than secrets, full private portfolios, or full sensitive prompts.

# 31. Raw and Artifact Storage Semantics

Initial logical storage:

### Relational state
Suitable for:

- instrument identity;
- evidence/fact metadata;
- policies;
- workflows/tasks;
- thesis/decision state;
- experiment/learning metadata;
- portfolio/reconciliation;
- release/audit metadata.

### Object/content store
Suitable for:

- filings;
- HTML;
- JSON;
- PDF;
- provider responses;
- protected run artifacts;
- generated report artifacts.

Permitted RawArtifact objects SHOULD be content-addressed and immutable after secure ingestion.

---

# 32. Versioning

Material components MUST be versioned as applicable:

```text
schema
workflow
policy
provider adapter
tool
strategy
model config
prompt bundle
risk config
Production Memory snapshot
ReleaseBundle
code / git SHA
```

Contract/schema evolution SHOULD use semantic-versioning principles:

- MAJOR: breaking;
- MINOR: backward-compatible capability;
- PATCH: clarification/bug fix without intended contract break.

A change to a Frozen invariant requires:

- explicit revision;
- migration note;
- affected-contract analysis;
- verification;
- approval.

---

# 33. ADR Requirement

Material architecture choices SHOULD have ADRs containing:

```text
context
decision
alternatives
evidence
consequences
risks
status
```

An ADR cannot override Frozen C0 without the formal C0 revision process.

---

# 34. Architecture Evidence Ledger

Every Frozen Design Decision MUST be represented in:

```text
C0_ARCHITECTURE_EVIDENCE_LEDGER.yaml
```

Required decision fields include:

```text
decision_id
statement
decision_classification
strongest_evidence_strength
reasoning_basis
evidence_refs
our_adaptation
risks
required_tests
```

Allowed decision classifications:

```text
VERIFIED
ADAPTED
INFERRED
ASPIRATIONAL
```

`strongest_evidence_strength`, when external evidence exists, MUST use exactly one value from:

```text
EXECUTABLE_CONTRACT_TEST
SOURCE_IMPLEMENTATION
MACHINE_READABLE_SCHEMA
REPOSITORY_ARCHITECTURE_SPEC
OFFICIAL_TECHNICAL_DOCUMENTATION
README
ISSUE_OR_DISCUSSION
BLOG
```

If an honestly INFERRED decision has no external evidence reference, `strongest_evidence_strength` MAY be null; this MUST NOT be represented as stronger evidence than exists.

`reasoning_basis` records OUR adaptation/inference mechanism and MUST NOT be overloaded into the evidence-strength field.

Every `evidence_ref` MUST resolve to a Source Catalog record. Every load-bearing Source Catalog record MUST pin, where repository evidence is available:

```text
repository
commit
exact file path
blob_sha
source_role
authority_scope
```

Source role is independent of evidence strength:

```text
CONTRACT_AUTHORITY
SUPPORTING
INSPIRATION
```

Strong source-code evidence from an INSPIRATION project does not make that project a Contract Authority.

Freeze status is separate from evidence classification.

Evidence preference:

```text
Executable Contract Test
> Source Implementation
> Machine-Readable Schema
> Repository Architecture Spec
> Official Technical Documentation
> README
> Issue / Discussion
> Blog
```

The Ledger MUST pass machine-readable schema/conformance validation before C0 freeze.

Pre-freeze conformance is bidirectional:

```text
Every Ledger required_test
→ MUST resolve to an acceptance obligation in C0_ACCEPTANCE_TEST_CATALOG.md

Every C0 acceptance obligation
→ MUST be referenced by at least one Evidence Ledger decision
```

A catalog obligation with zero Ledger decision mappings is a freeze blocker because its Frozen semantic is not machine-governed.

# 35. Contract Responsibility Map

## C1 — Entity / Instrument / Listing / Contract / Corporate Action
Owns identity semantics, symbol mapping, asset/listing/contract representation, corporate-action identity effects.

## C2 — Provider / Source Router / Provider Certification
Owns provider capabilities, routing, certification, credentials boundary, typed provider outcomes.

## C3 — Cache / Quota / Freshness / Coalescing
Owns freshness/cache/quota/coalescing/last-known-good semantics.
Does NOT require an early centralized pub/sub DataHub runtime.

## C4 — Temporal / PIT / Revision
Owns exact temporal schemas, the single authoritative `available_from` visibility boundary, availability precision, revision queries, and corporate-action temporal semantics.

## C5 — Evidence / Provenance / Source Fitness / Verification / Conflict
Owns evidence graph, claim/source fitness, independence, verification/conflict rules.

## C6 — Tool / MCP / Capability / Policy
Owns tool schemas, capability enforcement, tool safety classes, canonical policy interfaces, trusted-intent enforcement interfaces, and research-execution capability boundaries.

## C7 — Workflow / Durable Task / Client Adapter / Budget
Owns orchestration, durable tasks, budgets, cancellation, adapter conformance.

## C8 — Learning & Research Evolution
Owns:
- ExperienceEpisode;
- OutcomeRecord;
- AttributionRecord;
- ReflectionRecord;
- LessonCandidate;
- HypothesisCandidate;
- StrategyCandidate;
- ModelCandidate;
- ExperimentRun;
- EvaluationResult / candidate metrics;
- Champion/Challenger references.

C8 does NOT own authoritative ValidationRecord, PromotionDecision, or ReleaseBundle issuance semantics.

## C9 — Production Signal / Thesis / Forecast / Decision
Owns production-facing thesis, qualitative confidence/calibrated-probability distinction, forecast, signal, and decision-intent semantics.

## C10 — Portfolio / Risk / Execution / Broker Reality
Owns portfolio construction, PortfolioSnapshot/effective-time semantics, reconciliation-dependent decision context, risk, execution intent, order/broker semantics.

## C11 — Durable State / Ledger / Memory / Watchlist / Reconciliation
Owns persistence interfaces/repositories for durable objects defined by C8/C9/C10/C12, including:
- Thesis;
- Decision;
- Experience;
- Experiment;
- Research Memory;
- Production Memory;
- Portfolio;
- Watchlist;
- Reconciliation;
- PromotionDecision;
- ReleaseBundle;
- Validation/Audit records;
- snapshots.

C11 owns persistence semantics, not the domain meaning of those objects.

## C12 — Validation / Audit / Promotion / Release / Observability
Exclusively owns the authoritative semantics of:
- ValidationRecord;
- PromotionDecision;
- ReleaseBundle issuance;
- release/audit status;
- promotion/rejection gates;
- release observability requirements.

Boundary shorthand:

```text
C8 produces research evidence and Candidates.
C9 defines Production decision meaning.
C10 converts Production intent into portfolio/risk/execution semantics.
C11 persists durable state through repository ports.
C12 validates/promotes/releases and audits.
```

A C8 component MAY reference a C12 record but MUST NOT issue authoritative C12 promotion/release state.

# 36. Dependency Topology

C0 freezes dependency direction, not a simplistic acyclic “layer number” graph.

### Foundation domain
C1, C2, C3, C4, C5.

### Control/orchestration
C6, C7 consume Foundation contracts.

### Production/research domain
C8 and C9 consume validated Foundation/Control contracts.

C10 consumes, through ports/contracts rather than concrete storage/adapters:

```text
C1 identity semantics
C4 temporal/PIT semantics
C6 policy/capability semantics
C9 decision/signal semantics
portfolio/reconciliation state through owned or repository ports
```

C10 MUST NOT redefine these upstream semantics locally.

### Persistence overlay
C11 implements repository/persistence ports for durable domain objects.
Domain contracts MUST NOT depend on concrete C11 storage adapters.

### Governance overlay
C12 evaluates artifacts/runs from C1–C10 and issues authoritative validation/promotion/release state.
C12 is cross-cutting governance, not merely a terminal leaf.

This topology avoids forcing semantic cycles such as C9↔C11 or C10↔C11.

# 37. Release and Audit Severity

Validation findings SHOULD have at least:

```text
CRITICAL
WARNING
INFO
```

CRITICAL findings block the applicable release/promotion under default policy.

Tier-1/load-bearing facts are fully validated.

Tier-2 MAY be stratified by financial/valuation/industry/management/market/macro category.

Tier-3 MAY be random audit.

Exact sampling percentages belong to C12 policy.

---

# 38. Forbidden Patterns

The following are explicitly forbidden by C0:

F-01 ticker used as canonical identity  
F-02 time-sensitive HISTORICAL query without explicit `as_of`  
F-03 latest revision silently substituted into historical state  
F-04 provider failure converted to empty/no-data  
F-05 silent synthetic/simulated fallback represented as observed  
F-06 one flat data-status enum mixing origin/freshness/delivery/etc.  
F-07 duplicated policy threshold outside canonical PolicyRegistry  
F-08 canonical finance/risk/PIT logic living only in Skill/prompt text  
F-09 report/Markdown/chat used as authoritative database  
F-10 unverified LLM arithmetic for critical financial values  
F-11 agent consensus treated as evidence independence  
F-12 external side effect without explicit retry/idempotency/timeout semantics  
F-13 failure represented only by natural-language text  
F-14 broker integration reduced to `place_order()`  
F-15 research/backtest automatically promoted to LIVE  
F-16 unvalidated Reflection/Lesson injected into Production context  
F-17 future learning artifact visible in earlier replay  
F-18 evaluation exposed to candidate generation while still labeled untouched  
F-19 secrets/private state committed to public repository/package/examples  
F-20 external response persisted immutably before secure-ingestion checks  
F-21 generated/handwritten client adapter redefining canonical workflow semantics  
F-22 roadmap/aspirational claim represented as implemented  
F-23 candidate issuing its own PromotionDecision  
F-24 raw positive PnL alone marking learning as validated  
F-25 external content granting capabilities or changing control policy  
F-26 learning artifact backdated before dependency/materialization availability  
F-27 stochastic LLM run mislabeled exact deterministic replay  
F-28 rollback restoring only partial incompatible behavior configuration  
F-29 material numeric fact lacking required unit/currency/scale semantics  
F-30 fabricated timestamp precision or timezone assumptions  
F-31 material lineage missing input/run/code/policy references  
F-32 syndicated/republished evidence counted as independent without lineage basis

---

F-33 untrusted external data originating/redirecting a side-effect objective through an already-granted capability  
F-34 research-generated executable Strategy/Model/tool/code running outside the mandatory Research Sandbox; lower policy may grant only scoped capabilities inside the Sandbox, and changing/removing the Sandbox boundary requires formal C0 revision/migration  
F-35 historical LLM-assisted run labeled causal `PIT_SAFE`/untouched `SEALED_OOS` while required model temporal contamination control is UNKNOWN/CONTAMINATED  
F-36 adaptive best-of-N candidate promoted without recorded anti-overfit/adaptive-search control  
F-37 Production DecisionRecord missing mandatory DecisionRunRecord/ReleaseBundle linkage  
F-38 released DecisionRun artifact identity silently resolving to mutable/substituted content  
F-39 LLM/analyst qualitative confidence silently represented as calibrated probability  
F-40 local/noisy promoted lesson silently generalized beyond validated regime/time/evidence scope


# 39. Acceptance Test Catalog

The authoritative acceptance catalog is maintained in:

```text
C0_ACCEPTANCE_TEST_CATALOG.md
```

Every Frozen invariant MUST map to at least one executable or statically enforceable acceptance test.

A test may be implemented later under its owning contract, but the obligation is frozen now.

---

# 40. C0 Definition of Done

C0 is eligible for freeze only if:

1. one self-contained canonical C0 specification exists;
2. superseded C0 patch documents are explicitly historical;
3. invariant set is internally non-contradictory;
4. each load-bearing design decision has evidence classification;
5. source references are pinned to commit/ref/file where available;
6. C1–C12 boundaries are clear;
7. no implementation-vendor choice is frozen accidentally;
8. self-improvement leakage paths are closed;
9. stochastic-run auditability is addressed without false reproducibility claims;
10. prompt-injection/control-data trust boundary is explicit;
11. acceptance tests cover the Frozen core;
12. security/private-state review passes;
13. migration/versioning rules are explicit;
14. all required independent verification/integrity/root-of-trust gates through C0-FR2.2 pass;
15. C0-FR3 independent metadata regression re-check passes;
16. the short Refreshed Final Freeze Review passes and emits an approval-ready exact Freeze Manifest;
17. user explicitly approves that exact Freeze Manifest and the additive freeze-seal transaction completes before C1 authorization.

---

# 41. What C0 Does NOT Freeze

C0 does NOT freeze:

- Python framework;
- ORM;
- exact relational database product;
- queue/bus product;
- web/UI framework;
- Temporal vs local TaskJournal;
- OPA vs custom policy engine;
- OpenLineage server deployment;
- exact C1–C12 field-level schemas;
- exact Alpaca/Tushare/AKShare/Serper/Bocha/Exa routing priorities;
- exact valuation thresholds;
- exact risk limits;
- exact audit sampling percentages;
- exact learning reward weights;
- exact promotion minimum sample sizes.

Those belong to lower contracts/policies/ADRs.

---

# 42. What C0 Intends to Freeze After Approval

The final C0 freeze will lock the architecture obligations around:

- stable identity;
- explicit historical `as_of`;
- availability-time PIT;
- revision preservation;
- fail-loud provider semantics;
- canonical normalization;
- multidimensional data quality;
- secure raw ingestion;
- raw artifact immutability after ingestion;
- evidence lineage and independence;
- claim-type source fitness;
- report-not-database;
- canonical policy source;
- Skill/adapter-not-business-logic;
- deterministic critical finance;
- typed tool failures;
- idempotency/retry semantics;
- LLM/risk separation;
- research/Production separation;
- self-improvement promotion gate;
- learning PIT;
- evaluation quarantine;
- ReleaseBundle;
- DecisionRunRecord/audit reconstruction;
- external-content trust boundary;
- unit/currency/time precision;
- SIM/PAPER/LIVE semantic parity;
- portfolio reconciliation;
- release/audit gates;
- ports-and-adapters dependency inversion;
- private/public-state separation.

---

# 43. Supersession and Freeze Lifecycle

Current lifecycle:

```text
C0 Initial Candidate                                  → historical
C0 Red-Team Audit                                     → historical audit evidence
C0-R1 Repair                                          → historical repair artifact
C0-R1 Verification                                    → historical verification artifact
C0-R2 Final Candidate                                 → historical candidate
C0-R2 Independent Verification                        → historical failed verification
C0-R2V Freeze-Blocker Repair                          → historical repair artifact
C0-R2V Independent Re-Verification                    → historical failed re-verification
C0-R2V.1 Narrow Defect Repair                         → historical repair artifact
C0-R2V.1 Independent Regression Re-Check              → historical failed re-check
C0-R2V.2 Evidence-Ledger Coverage Repair              → historical repair artifact
C0-R2V.2 Independent Coverage Regression Check        → historical PASS
Final Freeze Review                                   → historical FAIL (FR-B01, FR-B02)
C0-FR1 Final Freeze Defect Repair                     → historical repair artifact
C0-FR1 Independent Finalization Regression Re-Check   → historical PASS
Refreshed Final Freeze Review (post-FR1)              → historical FAIL (canonical Ledger artifact regression)
C0-FR2 Canonical Ledger Integrity Restoration         → historical repair artifact
C0-FR2 Independent Ledger Integrity Re-Check          → historical FAIL (canonical path persistence)
C0-FR2.1 Canonical Artifact Binding & Persistence Repair → historical repair artifact
C0-FR2.1 Independent Binding Integrity Re-Check       → historical FAIL (BR-B01 binding root of trust)
C0-FR2.2 Binding Root-of-Trust Repair                 → historical repair artifact
C0-FR2.2 Independent Binding Root-of-Trust Re-Check   → historical PASS
Refreshed Final Freeze Review (FR3)                   → historical FAIL (RFR3-B01 stale final metadata)
C0-FR3 Final Canonical Metadata Synchronization       → CURRENT
C0-FR3 Independent Metadata Regression Re-Check       → NEXT
Short Refreshed Final Freeze Review
Approval-ready Freeze Manifest
Explicit User Approval
Additive C0 Freeze Seal
C0-FROZEN
C1
```

Once C0 is frozen:

- the approved final candidate is promoted/renamed byte-for-byte to the frozen canonical C0 specification;
- the approved Freeze Manifest and additive Freeze Seal pin the exact Candidate, Acceptance Catalog, authoritative Ledger, trusted Binding, trusted Verifier, and final-review identities;
- prior C0 candidates/repair documents remain available for audit history but are marked `SUPERSEDED`;
- new chats/Codex stages must resolve the Frozen C0 package through its approved content-addressed identities rather than reconstruct it from patches or trusting mutable convenience filenames.

---

# 44. Current Status

```text
C0-FR3 FINAL CANONICAL METADATA SYNCHRONIZATION: COMPLETE
C0 FREEZE STATUS: NOT FROZEN
C1 AUTHORIZATION: NOT GRANTED
NEXT GATE: C0-FR3 INDEPENDENT METADATA REGRESSION RE-CHECK
```

No C1 work is authorized until C0-FR3 Independent Metadata Regression Re-Check and the short Refreshed Final Freeze Review pass, the user explicitly approves the exact approval-ready Freeze Manifest, and the additive C0 Freeze Seal is created.
