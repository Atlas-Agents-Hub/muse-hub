# Extend a specialist kit

Each kit is intentionally editable. Start with a new role package and preserve the original files when experimenting.

## Project structure

- `presets/catalog.json` indexes the fifteen source roles.
- `presets/ROLE/playbook.json` represents the methods and optional tool categories for a chosen role. Replace `ROLE` with a real slug such as `garden-companion`.
- `src/muse_presets/role_skills.py` stages and inspects local skill descriptions.
- `src/muse_presets/portable_connectors.py` defines connector configuration, permissions, and recorded results.
- `src/muse_presets/` contains the executable modules supplied by the toolkit.
- `tests/` contains examples of positive and refusal tests.

## Add a capability

1. Create a new source folder using [Get started](GITHUB_QUICKSTART.md). Never overwrite an owner's saved data.
2. Define one method, its inputs, outputs, required permissions, and a clear stopping condition.
3. Add a focused function when the capability needs executable code, and document its dependencies and setup.
4. Add a test with a valid fixture and at least one negative case (changed hash, invalid scope, replay or unsupported platform).
5. Run the doctor and complete test suite, then inspect the resulting package.
6. Keep source changes and recovery instructions in your development workspace; publish only clean, supported files.

## Skills, subchats and connectors

Role kits include editable profiles, three focused subchat guides, and skill descriptors. Use the [skills reference](SKILLS.md) for formats and validation, and the [connector guide](CONNECTORS.md) when the extension needs an account or service.

For a host integration, configure its account and permissions. Verify the recipient before an external action and check the returned result. Use the host's scheduling and deployment tools when your extension needs them.

## Validate the extension

```bash
PYTHONPATH=src python3 -B -m unittest discover -s tests -q
PYTHONPATH=src python3 -B -m muse_presets.cli doctor
PYTHONPATH=src python3 -B -m muse_presets.cli audit-neutrality
```

On Windows PowerShell, set `$env:PYTHONPATH = "src"` and use `python`. Keep private memory, credentials, machine paths and temporary recovery receipts out of public packages. See [security](SECURITY.md) and [releases](RELEASES.md).
