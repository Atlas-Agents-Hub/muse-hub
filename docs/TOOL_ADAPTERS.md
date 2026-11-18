# Specialist adapter examples

Run the included research, garden, study, claims, and observation-comparison tools through one adapter interface. Inspect the selected capability, run its worked example, and use the result to build your integration.

| Capability | Included module | Worked example |
| --- | --- | --- |
| Evaluation | Research Evaluator | Check citations against supplied research sources. |
| Garden | Garden Companion | Review calendar changes, save them in SQLite, and recover an interrupted response. |
| Study | Learning Coach | Record practice and reopen a saved study session. |
| Claims | Claims Adjudicator | Compare a claim with its evidence and scope. |
| Security | Reverse Engineering & Security Researcher | Compare two sets of recorded interface observations. |

## Inspect an adapter

From this repository root, after setting the import path:

```bash
PYTHONPATH=src python3 -B -m muse_presets.cli component-list
PYTHONPATH=src python3 -B -m muse_presets.cli component-inspect --capability garden
```

These commands list the included files and check their hashes against the package manifest. Review changed source before updating its manifest.

## Run a worked example

Use a workspace and account with the permissions you intend the Python program to have. The examples use temporary or sample data.

```bash
PYTHONPATH=src python3 -B -m muse_presets.cli component-fixture --capability garden --allow-reviewed-fixture
PYTHONPATH=src python3 -B examples/role_component_demo.py --run-fixtures
```

On Windows PowerShell, set `$env:PYTHONPATH = "src"` and use `python`.

For animation work, follow the [Creative Studio guide](collection/CREATIVE_STUDIO_SCOPE.md) to prepare shots, assets, and timing for your chosen renderer.

## Add an adapter

Include the module and its dependencies, document the inputs and outputs, and provide a repeatable example with a known expected result. Test changed files, mismatched package paths, invalid input types, and unsupported platforms. Keep examples free of personal data and credentials.

For a service connection, configure the account and permissions, then verify the returned result in the original service.
