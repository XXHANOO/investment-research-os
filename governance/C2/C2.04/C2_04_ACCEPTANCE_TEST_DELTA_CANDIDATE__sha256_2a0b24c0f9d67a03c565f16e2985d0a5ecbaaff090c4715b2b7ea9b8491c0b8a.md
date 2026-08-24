# C2.04 — Acceptance Test Delta Candidate

Generated: 2026-08-24T13:55:00Z

Status: `CANDIDATE_FOR_C2_04_INDEPENDENT_SECURITY_BOUNDARY_REVIEW`

This catalog defines C2.04 construction obligations. It is not evidence of independent review.

| ID | Test | Required Behavior | Type |
|---|---|---|---|
| `C2-289` | Secret literal in public artifact rejected | A public repo/report/example containing provider-usable credential material fails security conformance. | `security/contract` |
| `C2-290` | Secret-derived public fingerprint rejected | A public hash/fingerprint deterministically derived from secret material fails security conformance. | `security/contract` |
| `C2-291` | Synthetic credential fixture allowed only if non-usable | Example credentials must be explicitly synthetic/non-authenticating. | `security/contract` |
| `C2-292` | Credential ref cannot contain bearer material | Opaque credential_handle_ref must not itself authenticate to provider. | `security/contract` |
| `C2-293` | Replay does not require secret bytes | Audit replay succeeds from semantic binding/version lineage without historical secret value. | `security/contract` |
| `C2-294` | Floating security semantic ref rejected | Load-bearing C2.04 semantic profile using latest/floating alias fails closed. | `security/contract` |
| `C2-295` | Wrong-kind security ref rejected | Credential binding slot supplied a private-state/ingress profile ref fails closed. | `security/contract` |
| `C2-296` | Dangling/hash-mismatch security ref rejected | Unresolvable or content-mismatched C2.04 stable ref fails closed. | `security/contract` |
| `C2-297` | Credential does not grant capability | Valid credential without trusted C6 operation capability cannot authorize provider dispatch. | `security/contract` |
| `C2-298` | Credential does not authorize side effect | Market-data credential cannot create WRITE/PAPER/LIVE intent or authority. | `security/contract` |
| `C2-299` | Provider binding mismatch blocked | Provider A-bound credential presented to Provider B produces BLOCKED and no dispatch. | `security/contract` |
| `C2-300` | Endpoint binding mismatch blocked | Credential bound outside selected endpoint profile produces BLOCKED and no dispatch. | `security/contract` |
| `C2-301` | Capability binding mismatch blocked | Credential bound outside selected C2 capability produces BLOCKED and no dispatch. | `security/contract` |
| `C2-302` | Credential class mismatch blocked | Secret material class incompatible with binding profile produces structured BLOCKED. | `security/contract` |
| `C2-303` | Untrusted secret source blocked | Credential value extracted from provider/web/model content is rejected as credential authority. | `security/contract` |
| `C2-304` | Missing credential blocks before dispatch | Required credential absent produces BLOCKED and no provider dispatch. | `security/contract` |
| `C2-305` | Cross-authority redirect does not forward secret | Redirect changing destination authority cannot receive existing secret without new trusted binding/admission. | `security/contract` |
| `C2-306` | Request log strips Authorization | Ordinary persisted request capture cannot contain Authorization secret value. | `security/contract` |
| `C2-307` | Request log strips bound query secret | Ordinary persisted URL/query capture removes bound API-key value. | `security/contract` |
| `C2-308` | Request log strips cookie/session secret | Ordinary persisted capture removes cookie/session credential values. | `security/contract` |
| `C2-309` | Unsanitizable request capture not persisted | If sanitation proof is absent/indeterminate, ordinary request capture persistence is forbidden. | `security/contract` |
| `C2-310` | Lease descriptor contains no secret fields | CredentialLease public/audit descriptor rejects secret_value/secret_hash/token/private_key fields. | `security/contract` |
| `C2-311` | Operation-local lease released | Credential material is not retained in adapter-visible ordinary state beyond bounded authentication use. | `security/contract` |
| `C2-312` | External content cannot rotate/replace credential | Provider instruction cannot replace trusted credential_handle_ref/version. | `security/contract` |
| `C2-313` | Private state scope subset enforced | Actual provider-bound private-state scope outside authorized declared scope is blocked. | `security/contract` |
| `C2-314` | Provider content cannot expand private state | Provider response asking for more private data cannot self-authorize expansion. | `security/contract` |
| `C2-315` | Private handle cannot retarget from external content | External content cannot replace account/private_state_handle destination. | `security/contract` |
| `C2-316` | Private state public projection redacted | Public projection excludes private account/portfolio/thesis values by default. | `security/contract` |
| `C2-317` | Secure ingress precedes permitted raw | External response cannot acquire Permitted RawArtifact identity before final secure-ingress ADMIT. | `security/contract` |
| `C2-318` | Provider payload cannot set ingress policy | security/privacy/licensing/retention policy refs from response content are ignored/rejected as control. | `security/contract` |
| `C2-319` | Ingress axes retained separately | Assessment records secret/privacy/licensing/retention constraints as separate fields. | `security/contract` |
| `C2-320` | Reject has highest precedence | Any REJECT_REQUIRED yields REJECT regardless of other axes. | `security/contract` |
| `C2-321` | Quarantine precedes redaction/admit | Absent reject, QUARANTINE_REQUIRED yields QUARANTINE. | `security/contract` |
| `C2-322` | Indeterminate fails closed | Absent reject, any INDETERMINATE yields QUARANTINE, never ADMIT. | `security/contract` |
| `C2-323` | Redaction required yields re-assessment state | Absent reject/quarantine/indeterminate, REDACT_REQUIRED yields REASSESS_REDACTED. | `security/contract` |
| `C2-324` | Ephemeral-only beats raw persistence | All other axes allow but one EPHEMERAL_ONLY yields ADMIT+EPHEMERAL_ONLY. | `security/contract` |
| `C2-325` | All allow yields permitted raw | All constraints ALLOW yields ADMIT+PERMITTED_RAW. | `security/contract` |
| `C2-326` | Decision is permutation invariant | Reordering assessment axes does not change final ingress decision. | `security/contract` |
| `C2-327` | Redacted output fully re-assessed | Redaction output cannot transition directly to ADMIT without complete new assessment. | `security/contract` |
| `C2-328` | Redaction record excludes removed plaintext | Redaction lineage cannot store removed secret/PII plaintext. | `security/contract` |
| `C2-329` | Redaction record excludes secret-derived fingerprint | Removed secret cannot be represented by public deterministic secret hash. | `security/contract` |
| `C2-330` | Secret echo response protected | Provider response echoing credential cannot enter permitted raw unmodified. | `security/contract` |
| `C2-331` | PII policy restriction enforced | Response with privacy restriction follows normalized REDACT/QUARANTINE/REJECT result before raw admission. | `security/contract` |
| `C2-332` | License ephemeral restriction enforced | Licensing constraint EPHEMERAL_ONLY prevents Permitted RawArtifact persistence. | `security/contract` |
| `C2-333` | Retention prohibition enforced | Retention policy REJECT_REQUIRED/QUARANTINE_REQUIRED prevents permitted raw persistence. | `security/contract` |
| `C2-334` | Permitted raw hash is admitted-byte hash | For REDACTED admit, content hash equals redacted admitted bytes, not original unsafe bytes. | `security/contract` |
| `C2-335` | Permitted raw mutation creates new identity | Changing admitted bytes cannot overwrite old content identity. | `security/contract` |
| `C2-336` | Ephemeral-only has no persisted raw payload ref | C1-facing envelope cannot point raw_payload_ref at ephemeral-only bytes. | `security/contract` |
| `C2-337` | Quarantine cannot feed C1 normalization | Quarantined response cannot produce admitted C1 provider observations. | `security/contract` |
| `C2-338` | Rejected content cannot become NO_DATA | REJECT cannot be converted to SUCCESS+NO_DATA. | `security/contract` |
| `C2-339` | Quarantine cannot become NO_DATA | QUARANTINE cannot be converted to SUCCESS+NO_DATA. | `security/contract` |
| `C2-340` | Sanitized 401 diagnostics | 401 body/header echoing token is sanitized before structured failure/audit storage. | `security/contract` |
| `C2-341` | Sanitized URL diagnostics | Provider error URL containing API key stores a redacted locator only. | `security/contract` |
| `C2-342` | Sanitization does not change failure family | Removing secret from diagnostics does not reclassify C2.02 operation/data outcome. | `security/contract` |
| `C2-343` | Ingress admit is not verification | ADMIT cannot set C5 VERIFIED/source fitness. | `security/contract` |
| `C2-344` | Ingress timestamp is not available_from | retrieved_at/ingress time cannot set C4 available_from/PIT safety. | `security/contract` |
| `C2-345` | Credential/private state cannot alter route ordering | Availability of credential/private state cannot bypass C2.03 candidate order/compatibility. | `security/contract` |
| `C2-346` | No concrete vendor/secret-store selected | Candidate contains zero provider instances and zero secret-store/KMS/vendor choices. | `security/contract` |
| `C2-347` | C2.OPEN-008 only candidate-closed | Construction marks OPEN-008 pending independent security review, not final closed. | `security/contract` |
| `C2-348` | C2.OPEN-013 remains open | Exact C2->C11 permitted-raw wire/repository handoff remains deferred to C2.06. | `security/contract` |

## Required Independent Review Focus

The independent review must not merely count rows. It must adversarially determine whether the candidate is deterministic and fail-closed for:

- credential/public artifact leakage;
- credential-as-capability confusion;
- cross-provider/redirect secret forwarding;
- private-state scope expansion;
- secret/privacy/license/retention precedence;
- indeterminate assessment handling;
- redaction followed by mandatory re-assessment;
- ephemeral-only versus permitted-raw separation;
- quarantine/reject isolation;
- sanitized C2.02 diagnostics;
- C1 raw_payload_ref semantics;
- C6/C11 authority boundaries.

C2.05 is not authorized by this catalog.
