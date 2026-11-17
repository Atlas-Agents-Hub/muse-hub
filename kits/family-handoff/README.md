# H12 — Family Link offline envelope contract

**Status:** SOURCE_ONLY / PROPOSAL_ONLY_NOT_SENT / NOT_DELIVERED.

This directory captures the original 22-task executor graph's H12 requirements without creating a second Family Link controller. The only implementation is the existing `src/muse_presets/family.py` and `src/muse_presets/family_envelope.py`. The JSON files here are **read-only projections** of those sources and the 15 existing role policies, never authorization, route registration, a sender/recipient identity record, or an instruction to contact another account.

## Records and provenance

- [Envelope contract](envelope-contract.json) — schema, exact fields, disabled authority flags, consent/replay limitations, a 3,600-second maximum local validity window, and the SHA-256 of the existing envelope module.
- [Role boundaries](role-boundaries.json) — 15 role IDs from `presets/catalog.json`, source-file digests, and each role's suggested receivers. Every profile is `enabled: false`, `transport: unbound`, and has no trusted signer or native recipient.
- [Reusable offline source ZIP instructions](../../docs/kits/FAMILY_LINK_SOURCEKIT.md) — an optional 26-member ZIP that contains the original source modules and fictional two-process demonstration. It does not issue a native tool or send any message.

All JSON is deterministic and source-verified by `tests/test_offline_kits.py`; drift in the original module or any role policy requires review before an updated contract can pass tests.

## Deterministic fixture acceptance

From the Muse Hub source root:

```sh
PYTHONPATH=src python -B -m unittest discover -s tests -p test_offline_kits.py -v
PYTHONPATH=src python -B -m unittest discover -s tests -p test_family_envelope.py -v
PYTHONPATH=src python -B examples/family_offline_handoff_demo.py
```

The existing review_local_envelope consumer validates the pinned envelope against the supplied receiver-local role and untrusted replay history.

The source implementation must refuse: self-handoff, unknown/forged recipient, a receiver-local role mismatch, a request ID already declared seen, a revoked request ID, expired envelopes, modified finding digests and any forged authentication/effect grant. A successful synthetic comparison must still report `LOCAL_HANDOFF_REVIEW_ONLY_NOT_DELIVERED` and `effect_authorized: false`. The demo's positive result is a **two-process local test**, not two authenticated assistants.

## Unresolved live gates

Actual original receiving-agent identity, sender/receiver credentials, independent consent, approved transport, native recipient acknowledgment, durable replay fence, task-resource reservation, and independent cross-account readback are **NOT VERIFIED**. Only their original authorized owners can establish those facts. The original TaskGuard/retention P1 holds remain open. This kit does not make them safe, does not publish a release and cannot be promoted to an active Family Link adapter from these fixtures alone.
