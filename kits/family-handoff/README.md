# Family Link handoffs

Prepare a task for another specialist with the context it needs, a clear receiving role, and an expected result. Review the handoff record before sharing it through your chosen connection.

## Try a handoff

From the toolkit root with Python 3.12+:

```sh
PYTHONPATH=src python3 -B examples/family_offline_handoff_demo.py
```

In Windows PowerShell, set `$env:PYTHONPATH = "src"` and use `python -B`.

The worked example prepares and reviews a handoff in separate processes. It checks the requested role, capability, request ID, supplied replay declarations, and recipient context. Use the resulting proposal as input to the communication route you choose, then confirm delivery and the returned result in that service.

## Prepare your own task

1. Choose the receiving specialist and the work it should handle.
2. Include the relevant source material, constraints, and requested output.
3. Review the proposed handoff and keep the recipient's own context and memory in place.
4. Share through your selected account or service connection and retain the request ID.
5. Inspect the returned result before continuing the larger task.

## Developer reference

- [Envelope contract](envelope-contract.json) — fields and validation rules.
- [Role boundaries](role-boundaries.json) — suggested receiving roles and capabilities.
- [Portable handoff kit](../../docs/kits/FAMILY_LINK_SOURCEKIT.md) — build, verify, and run the example independently.

The implementation is in `src/muse_presets/family.py` and `family_envelope.py`. When integrating a delivery service, use its account setup and check the original operation before retrying an uncertain result.

[Family Link guide](../../docs/FAMILY_LINK.md) · [Coordinator](../../presets/coordinator/INSTALL.md) · [Connectors](../../docs/connectors/README.md)
