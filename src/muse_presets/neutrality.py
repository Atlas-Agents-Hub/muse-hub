"""Check source files for credentials, private paths and unsafe assets.

Reports contain relative file paths and reason codes. Callers can supply
additional private terms for a specific release review.
"""
from __future__ import annotations

import os
import hashlib
import re
from pathlib import Path

# Only VCS internals and local tooling caches are outside the distribution.
_EXCLUDED_DIRS = frozenset((
    ".git", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", ".tox", ".venv", "venv",
))
_TEXT_SUFFIXES = frozenset((
    ".md", ".json", ".jsonl", ".yaml", ".yml", ".toml", ".txt",
    ".py", ".sh", ".bash", ".js", ".mjs", ".cjs", ".ts", ".tsx",
    ".jsx", ".html", ".css", ".xml", ".ini", ".cfg", ".rst",
))
_TEXT_NAMES = frozenset((
    "license", "makefile", "dockerfile", ".gitignore",
    ".gitattributes", ".editorconfig", ".dockerignore",
))
REVIEWED_TEXT_FILES = frozenset({
    "collections/muse-starters-v1/skills/project-prioritization/backlog.csv",
    "collections/library/skills/cloud-finops/assets/focus_export.example.csv",
    "collections/library/skills/commit-craft/assets/commit-craft-allow.example",
    "collections/library/skills/commit-craft/assets/hooks/commit-msg",
    "collections/library/skills/commit-craft/assets/hooks/pre-commit",
    "collections/library/skills/commit-craft/assets/hooks/pre-push",
    "collections/library/skills/database-designer/assets/sample_schema.sql",
    "collections/library/skills/dependency-auditor/assets/sample_go.mod",
    "collections/library/skills/design-qa/assets/states.example.csv",
    "collections/library/skills/design-qa/assets/waivers.example.csv",
    "collections/library/skills/i18n-localization/assets/i18n-allow.example",
    "collections/library/skills/kubernetes-operator/assets/reconcile_skeleton.go",
    "collections/library/skills/linkedin-analytics/assets/example_post_export.csv",
    "collections/library/skills/mobile-release/assets/rollout.example.csv",
    "collections/library/skills/month-end-close/assets/bank_statement.example.csv",
    "collections/library/skills/month-end-close/assets/flux_input.example.csv",
    "collections/library/skills/month-end-close/assets/gl_cash.example.csv",
    "collections/library/skills/support-ops/assets/intervals.example.csv",
    "collections/library/skills/support-ops/assets/tickets.example.csv",
    "collections/library/skills/tdd-guide/assets/sample_coverage_report.lcov",
})
_SENSITIVE_NAMES = frozenset((
    ".env", ".env.local", ".env.production", ".env.development",
    "id_rsa", "id_ed25519", "credentials.json", "credentials.yml",
    "secrets.json", "secrets.yml", "token.json", "tokens.json",
    "auth.json", "service-account.json",
))
_SENSITIVE_SUFFIXES = frozenset((
    ".pem", ".p12", ".pfx", ".key", ".sqlite", ".sqlite3",
    ".db", ".bak", ".backup", ".log", ".p8", ".p7b",
    ".zip", ".tar", ".gz", ".7z", ".exe", ".dll", ".so",
    ".dylib", ".bin", ".wasm",
))
_PRIVATE_HOST_PATH = re.compile(
    r"(?i)(?:[a-z]:[\\/]Users[\\/][^\\/\s]+[\\/]|"
    r"/" + r"home/[^/\s]+/|/" + r"Users/[^/\s]+/)"
)
_POSSIBLE_SECRET = re.compile(
    r"(?i)(?:\bsk-(?:proj|live)-[A-Za-z0-9_-]{12,}\b|"
    r"\bAKIA[A-Z0-9]{16}\b|"
    r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}\b|"
    r"\bgithub_pat_[A-Za-z0-9_]{25,}\b|"
    r"-----BEGIN (?:OPENSSH |RSA |EC |DSA |)PRIVATE KEY-----|"
    r"\bBearer[ \t]+[A-Za-z0-9_./+=:-]{32,}\b)"
)
_POSSIBLE_PASSWORD = re.compile(
    r"(?i)\b(?:api[_-]?key|client_secret|private_key|access_token|"
    r"auth_token|password)\s*[:=]\s*['\"][A-Za-z0-9_./+=:@-]{20,}['\"]"
)
_PERSONAL_EMAIL = re.compile(
    r"\b[A-Za-z0-9._%+-]+@(?!(?:example\.(?:com|org|net)|localhost)\b)"
    r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", re.I
)
_MAX_BYTES = 2_000_000

# Reviewed API routes, cloud resource paths and credential-detector expressions.
# Exact hashes keep new private content subject to the normal scanner.
REVIEWED_EXAMPLE_TEXT = {'collections/library/skills/aws-solution-architect/references/best_practices.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                                    'sha256': '4db8f6c550aa959537feab6dcdd4a6d16dbfd4a0ec8dd3ad964a2d5b7e948661'},
 'collections/library/skills/code-to-prd/assets/sample-analysis.json': {'reason': 'PRIVATE_HOST_PATH',
                                                                        'sha256': 'db88ba2cb560173db5d83155ee9a064e70154248407ee0d2d10e14a87f873016'},
 'collections/library/skills/javascript-pro/references/async-patterns.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                            'sha256': '0a4e9a195d3f7f2d4e8b6c8a8c8a80c886733968e5d6aa3043900ae7975d8f52'},
 'collections/library/skills/laravel-specialist/references/routing.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                         'sha256': '108ebc7524de46262914bbfe3a754252858d5029dcc0b91be980fc15329986e1'},
 'collections/library/skills/migration-architect/assets/sample_service_migration.json': {'reason': 'PRIVATE_HOST_PATH',
                                                                                         'sha256': '09a7084eb3d15cfa00a158c26c5778a5f4798c40cd1ba6fe340455512022f9bd'},
 'collections/library/skills/nextjs-developer/references/app-router.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                          'sha256': '6ad5dcb2db0c98b13e87846936670c861da27346edebe75bf096cb08b78f6330'},
 'collections/library/skills/nextjs-developer/references/data-fetching.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                             'sha256': 'abbea7c3351c7ad77ca820e48e6f27cd68f29638b82e39dc65560a75f5151255'},
 'collections/library/skills/security-pen-testing/references/attack_patterns.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                                   'sha256': '66898510c8f672b7efad7b6a3ace8bbf58508f7903cec3ebbfd5e1fe00c1346c'},
 'collections/library/skills/security-pen-testing/references/owasp_top_10_checklist.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                                          'sha256': '524e9e3109ede2d01c41eab68063a669d5846f0210e66c67e5361489447000e9'},
 'collections/library/skills/senior-backend/references/api_design_patterns.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                                 'sha256': 'b474416e963f7538af0d60d28f570e20b5bbb4bf546c1ae5627c2b8c9132d845'},
 'collections/library/skills/senior-backend/references/backend_security_practices.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                                        'sha256': 'af4a48e93978bb772c3585b3ed5ecd347b37cc6cd656ec7c7f37cece2095d6c7'},
 'collections/library/skills/senior-fullstack/references/architecture_patterns.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                                     'sha256': 'a4efd7bf910148c9792aafd4263aa8a90db7b0d4b102e49d6909847b3e946877'},
 'collections/library/skills/senior-fullstack/references/tech_stack_guide.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                                'sha256': '883e6f19db2e6043f95233766ceb2554a2a2221cbcc0c929800c276cd1f7c4c3'},
 'collections/library/skills/senior-security/scripts/secret_scanner.py': {'reason': 'POSSIBLE_SECRET',
                                                                          'sha256': '066fe3d2d53e72648c113474a20cdc72c5892bbddb19139eaa03fd0d4122c1ec'},
 'collections/library/skills/test-master/references/security-testing.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                           'sha256': '47833ae4c258f1d729ac747006d29b56621a6f9323253ececc2ae1931323b7ab'},
 'collections/library/skills/typescript-pro/references/advanced-types.md': {'reason': 'PRIVATE_HOST_PATH',
                                                                            'sha256': '273042ee8dba7fe809085856cea8e71eaa363d2cd19d2ba021d852d971777f20'}}



def audit_public_tree(root: Path, *,
                      forbidden_terms: tuple[str, ...] = ()) -> list[dict[str, str]]:
    """Inspect every distributed file except .git and runtime caches.

    All findings contain a repository-relative path and fixed reason code.
    A caller's private forbidden_terms are never copied into these results
    or stored by the function. The caller must still audit Git history.
    """
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise ValueError("INVALID_PUBLIC_ROOT")
    if len(forbidden_terms) > 128 or any(
        type(word) is not str or not 3 <= len(word) <= 128
        for word in forbidden_terms
    ):
        raise ValueError("INVALID_FORBIDDEN_TERMS")
    denied = tuple(
        re.compile(r"(?<![A-Za-z0-9])" + re.escape(word) +
                   r"(?![A-Za-z0-9])", re.I)
        for word in forbidden_terms
    )
    findings: list[dict[str, str]] = []
    def add(path: Path, reason: str) -> None:
        findings.append({"path":path.relative_to(root).as_posix(),
                         "reason":reason})

    for dirname, dirs, files in os.walk(root, topdown=True, followlinks=False):
        parent = Path(dirname)
        # Never inspect .git internals, or follow a directory symlink.
        for name in list(dirs):
            if name in _EXCLUDED_DIRS:
                dirs.remove(name)
                continue
            path = parent / name
            if path.is_symlink():
                add(path, "SYMLINK_REFUSED")
                dirs.remove(name)
        for name in files:
            # A Git linked-worktree .git pointer is VCS metadata, never a
            # distributable source file; exclude it like a .git directory.
            if name == ".git":
                continue
            path = parent / name
            if path.is_symlink():
                add(path, "SYMLINK_REFUSED")
                continue
            lowered = name.lower()
            if (lowered in _SENSITIVE_NAMES or lowered.startswith(".env.")
                or path.suffix.lower() in _SENSITIVE_SUFFIXES
                and path.suffix.lower() not in _TEXT_SUFFIXES):
                add(path, "SENSITIVE_FILE" if path.suffix.lower() in
                    {".sqlite", ".sqlite3", ".db", ".pem", ".p12", ".pfx", ".key",
                     ".bak", ".backup", ".log", ".p8", ".p7b"} or
                    lowered in _SENSITIVE_NAMES or lowered.startswith(".env.")
                    else "UNREVIEWED_BINARY_ASSET")
                continue
            if (path.suffix.lower() not in _TEXT_SUFFIXES and
                lowered not in _TEXT_NAMES and
                path.relative_to(root).as_posix() not in REVIEWED_TEXT_FILES):
                add(path, "UNREVIEWED_BINARY_ASSET")
                continue
            try:
                size = path.stat().st_size
                if size > _MAX_BYTES:
                    add(path, "OVERSIZED_ASSET")
                    continue
                raw = path.read_bytes()
                if b"\0" in raw:
                    add(path, "UNREVIEWED_BINARY_ASSET")
                    continue
                content = raw.decode("utf-8")
            except (OSError, UnicodeError):
                add(path, "UNREADABLE_OR_NON_UTF8")
                continue
            reviewed=REVIEWED_EXAMPLE_TEXT.get(path.relative_to(root).as_posix(),{})
            accepted_reason=reviewed.get("reason") if reviewed.get("sha256")==hashlib.sha256(raw).hexdigest() else None
            if _PRIVATE_HOST_PATH.search(content) and accepted_reason!="PRIVATE_HOST_PATH":
                add(path, "PRIVATE_HOST_PATH")
            if (_POSSIBLE_SECRET.search(content) or _POSSIBLE_PASSWORD.search(content)) and accepted_reason!="POSSIBLE_SECRET":
                add(path, "POSSIBLE_SECRET")
            if _PERSONAL_EMAIL.search(content):
                add(path, "PERSONAL_EMAIL_REVIEW_REQUIRED")
            if any(pattern.search(content) for pattern in denied):
                add(path, "FORBIDDEN_IDENTITY_LABEL")
    return sorted(findings, key=lambda row:(row["path"],row["reason"]))
