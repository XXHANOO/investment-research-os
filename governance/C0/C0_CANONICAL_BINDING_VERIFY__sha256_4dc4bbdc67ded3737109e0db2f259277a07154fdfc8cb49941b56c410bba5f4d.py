#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, re, sys, yaml

ERR = "CANONICAL_ARTIFACT_INTEGRITY_ERROR"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def fail(msg: str, code: int = 2):
    print(f"{ERR}: {msg}", file=sys.stderr)
    raise SystemExit(code)

def safe_bound_path(root: Path, rel_value: str, field_name: str) -> Path:
    if not isinstance(rel_value, str) or not rel_value:
        fail(f"missing/invalid {field_name}")
    rel = Path(rel_value)
    if rel.is_absolute():
        fail(f"{field_name} must be relative to binding root")
    if any(part in ("..", "") for part in rel.parts):
        fail(f"{field_name} contains forbidden path traversal")
    resolved = (root / rel).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError:
        fail(f"{field_name} escapes binding root")
    return resolved

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--binding", required=True)
    ap.add_argument("--binding-sha256", required=True)
    ap.add_argument("--logical", required=True)
    ap.add_argument("--mode", choices=["canonical", "projection"], default="canonical")
    args = ap.parse_args()

    expected_binding_sha = args.binding_sha256.strip().lower()
    if not SHA256_RE.fullmatch(expected_binding_sha):
        fail("--binding-sha256 must be an exact lowercase 64-hex SHA-256")

    binding_path = Path(args.binding).resolve()
    if not binding_path.exists() or not binding_path.is_file():
        fail(f"binding manifest does not exist: {binding_path}")

    # Root of trust: authenticate binding bytes before parsing/trusting contents.
    observed_binding_sha = sha256(binding_path)
    if observed_binding_sha != expected_binding_sha:
        fail(
            "binding SHA mismatch "
            f"expected={expected_binding_sha} observed={observed_binding_sha} path={binding_path.name}"
        )

    root = binding_path.parent.resolve()

    try:
        doc = yaml.safe_load(binding_path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"cannot parse authenticated binding manifest: {e}")

    b = (doc or {}).get("bindings", {}).get(args.logical)
    if not b:
        fail(f"logical artifact not bound: {args.logical}")

    expected_artifact_sha = b.get("authoritative_sha256")
    if not isinstance(expected_artifact_sha, str) or not SHA256_RE.fullmatch(expected_artifact_sha):
        fail("missing/invalid authoritative_sha256")

    if args.mode == "canonical":
        path = safe_bound_path(root, b.get("authoritative_path"), "authoritative_path")
    else:
        path = safe_bound_path(root, b.get("projection_path"), "projection_path")

    if not path.exists() or not path.is_file():
        fail(f"bound path does not exist or is not a file: {path.name}")

    observed_artifact_sha = sha256(path)
    if observed_artifact_sha != expected_artifact_sha:
        fail(
            f"{args.mode} SHA mismatch expected={expected_artifact_sha} "
            f"observed={observed_artifact_sha} path={path.name}"
        )

    print(
        "PASS "
        f"logical={args.logical} "
        f"binding_sha256={observed_binding_sha} "
        f"mode={args.mode} "
        f"path={path.name} "
        f"sha256={observed_artifact_sha}"
    )

if __name__ == "__main__":
    main()
