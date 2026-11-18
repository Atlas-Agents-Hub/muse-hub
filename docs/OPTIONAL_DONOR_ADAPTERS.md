# Run a specialist example through the adapter interface

Reuse five included local engines through a common adapter interface. Choose the capability, inspect its inputs, and enable the example explicitly when you want to run it.

| Capability | Reused local module | What actually runs |
| --- | --- | --- |
| Evaluation | Research Evaluator | Synthetic exact-source citation/research fixture |
| Garden | Garden Companion | Local SQLite owner-review and lost-ack recovery fixture |
| Study | Learning Coach | Local nonclinical SQLite review/reopen fixture |
| Claims | Claims Adjudicator | Pure local scope/overclaim decision fixture |
| Security | Reverse Engineering & Security Researcher | Pure comparison of fictional supplied UI-observation records |
| Animation | Creative Studio | **Source link only** — original renderer is not included and cannot run |

## Inspect before executing

From this repository root, after setting the import path:

```bash
PYTHONPATH=src python3 -B -m muse_presets.cli donor-list
PYTHONPATH=src python3 -B -m muse_presets.cli donor-inspect --capability garden
```

The catalog and inspection commands read existing files and compare their hashes with the reviewed source manifest. A changed module is refused. Review the source and use the account authorized for your task before running an example.

## Run an explicitly reviewed local fixture

Only execute source you trust under an account you control. The fixtures can execute Python code with that account's ordinary filesystem/network capabilities. **This repository does not provide an OS isolation sandbox.**

```bash
PYTHONPATH=src python3 -B -m muse_presets.cli donor-fixture --capability garden --allow-reviewed-fixture
PYTHONPATH=src python3 -B examples/role_donor_demo.py --run-fixtures
```

On Windows PowerShell, set `$env:PYTHONPATH = "src"` and use `python`.

Examples run only after explicit selection and use synthetic or temporary data. Python import isolation reduces environment-driven imports; run reviewed code in a workspace you control.

For animation work, use the [Creative Studio guide](collection/CREATIVE_STUDIO_SCOPE.md) and your chosen renderer.

## Add an adapter

When adding a reviewed first-party source engine, include its actual module, all necessary transitive local dependencies, a pinned source manifest, a deterministic offline fixture, explicit approval of any local code execution, and negative tests for byte tampering, root mismatch, invalid types and unsupported platforms. Keep private agent identity, original owner state, runtime credentials, scratch evidence and internal task logs out of any public distribution.

For a provider-backed adapter, configure the target account and permissions, then test its result through the original service.
