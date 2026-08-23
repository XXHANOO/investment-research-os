# C1.04R1 Uploaded ZIP — File-by-File Integrity Audit

ZIP: `C1_04R1_NEW_CHAT_HANDOFF_PACKAGE(2).zip`

## Overall verdict

```text
ZIP CRC test: PASS
Entries: 18
Content-addressed filename SHA-256 checks: PASS
Manifest-declared SHA-256 checks: PASS
Candidate Selection: PASS
```

The uploaded ZIP is internally intact as a C1.04R1 handoff package. Its content-addressed candidate, registry, ledger, acceptance delta and Candidate Selection all match their declared SHA-256 values. `C0_FROZEN.md` and `C0_FREEZE_SEAL.yaml` are also present and exactly match the authoritative C0 hashes.

However, this is not a complete C0 archive. It does not contain the full seal-pinned C0 approval/evidence set, including the approval-ready freeze manifest, acceptance catalog, authoritative ledger, canonical artifact bindings and canonical binding verifier.

The handoff manifest also records historical local-integrity checks for earlier C1.01R1/C1.02R1/C1.03R1 artifacts that are not all physically present in this 18-file ZIP. Therefore the ZIP is the declared minimum C1.04R1 handoff set, not a complete C0→C1.04 byte archive.

Verified C0 root hashes:

```text
C0_FROZEN.md
9585df6c0fbdb2cc40bc38571f8452b51f8ca69c9fd9432b10b87490b08a3b6f

C0_FREEZE_SEAL.yaml
eb2e11d4c425fee121feedc7ea6c4270722c85398afdab35917cbd6f667d93a2
```
