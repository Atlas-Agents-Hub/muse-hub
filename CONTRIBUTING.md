# Contributing

Contributions are welcome when they improve the public source kits, documentation, tests or accessibility.

## Before opening a pull request

1. Use a separate branch based on the current public `main`.
2. Keep private assistant memory, credentials, machine-specific records and internal work logs out of public files.
3. Make one bounded change with an executable example or a test where appropriate.
4. Run the source tests and privacy check.
5. Describe the user-visible improvement and any unsupported platforms or untested integrations.

```bash
PYTHONPATH=src python3 -B -m unittest discover -s tests -q
PYTHONPATH=src python3 -B -m muse_presets.cli audit-neutrality
PYTHONPATH=src python3 -B -m muse_presets.cli doctor
```

On Windows PowerShell, set `$env:PYTHONPATH = "src"` and use `python`.

## Develop and check locally

Run focused tests locally while making a change. Finish the relevant regression, packaging and public-content checks before pushing the completed batch. Use GitHub Actions for the final pull-request checks and substantial integrated changes; avoid repeated pushes or manual runs for routine edits. Required branch checks still apply before merging, and release and deployment jobs run when the finished change is ready to publish.

The public repository is a **product source distribution**, not an engineering scratchpad. Do not add milestone-numbered progress documents, internal task trackers, temporary checkpoints or machine-local receipts to its default branch.

In your pull request, describe the changed behavior, commands you ran, observed results, and any remaining checks. Verify external actions through the service that performed them before reporting completion.

For coding conventions and role APIs, see [Extend the toolkit](docs/EXTENDING_GENERIC_AGENTS.md). For sensitive reports, follow [Security](SECURITY.md). Code and documentation contributions must be compatible with the [MIT license](LICENSE).

## Write for the reader
Follow the [documentation standards](docs/handbook/EDITORIAL_STANDARDS.md) when editing public product, setup, role or AI-facing pages.

Name the tool and explain what it does, what it produces, how to run it and where its limits are. Describe differences between packages by their actual contents rather than vague comparisons. Keep development milestones and acceptance history out of introductory guides. Preserve exact command names, API identifiers, download versions and compatibility requirements. Check examples against the code, and do not describe a profile, test fixture or local receipt as a deployed service.
