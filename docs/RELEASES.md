# Downloads and versions

## Muse Specialist Toolkit v1.0.0

The V1 source covers 15 specialists, 100 task starters, 75 developed skills, 25 workflows and 151 connector records. The 50 original role/shared procedures remain available and overlap the developed skills.

[**Download V1.0.0 on GitHub**](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/tag/v1.0.0)

Choose the package for what you want to do:

- [**Complete toolkit — source and examples**](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/download/v1.0.0/muse-specialist-toolkit-v1.0.0.zip): The complete public source tree, specialist profiles, runnable tools and Daily Desk.
- [**Specialist collection — skills and starters**](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/download/v1.0.0/muse-specialist-collection-v1.0.0.zip): 100 task starter configurations, specialist kits and worked example reports.
- [**Custom connectors — searchable directory**](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/download/v1.0.0/muse-custom-connectors-v1.0.0.zip): All 151 connector records, setup guides and a local HTML directory.
- [**SHA256SUMS.txt**](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/download/v1.0.0/SHA256SUMS.txt): Checksums for the published assets.

For a quick test, extract the **complete toolkit**, open a terminal in its project directory and run:

```sh
python -B examples/daily_desk.py
```

The demonstration creates three tasks and two notes, checks stale edits, reopens the store and verifies a separate restored copy. Python 3.12+ is required for current source examples. No paid API is needed for these local demonstrations.

Use the [V1 start guide](v1/START_HERE.md) for specialist instructions, data tools, Daily Desk and custom connectors. The [capability guide](CAPABILITIES.md) explains what each package can execute.

## Verify your download

Download the checksum file alongside the asset. Calculate its SHA-256 and compare the digest with the matching line in ``SHA256SUMS.txt``. Then extract the archive and run its documented self-test or first-use example.

Checksums verify that the downloaded bytes match the published index; they do not grant permissions or install tools into your Muse account.

## Earlier releases

### v0.4.1-alpha — eight runnable tools and eleven starter ZIPs

The [historical v0.4.1-alpha release](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/tag/v0.4.1-alpha) provides eight standalone executable Python tools and 11 starter profiles. Its assets and checksums have not been replaced.

An **executable kit** runs a local program on supplied data. A **starter profile** gives you editable instructions; it is not a model-backed autonomous assistant.

For the Creative Studio executable, download the [ZIP](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/download/v0.4.1-alpha/creative-studio-executable-v0.4.1-alpha.zip), verify its [checksums](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/download/v0.4.1-alpha/SHA256SUMS.txt), extract and run:

```sh
python -I -B run.py --operation self-test
python -I -B run.py --operation demo --to "$HOME/creative-production-demo"
```

This writes JSON, CSV and a textual HTML storyboard. It does not render a film. Other packages may require Git or optional components; check their included instructions.

[Eleven starter profiles — v0.2.0-alpha](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/tag/v0.2.0-alpha) · [Software Engineer sourcekit](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/tag/software-engineer-sourcekit-r56-alpha) · [Initial source — v0.1.0-alpha](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/tag/v0.1.0-alpha)

## Source code and Muse access

No native Muse installation is performed by downloading a source ZIP or starter configuration. A Muse account is not required to run local examples; use a clean extraction and keep private account credentials outside the source package. They do not enable connectors, credentials, remote services or accounts. Use Muse's supported customization and connector setup when applying source instructions to an existing assistant.

Local programs run under your OS account and are not operating-system sandboxes. For platform requirements, see [installation](GITHUB_QUICKSTART.md) and [security](SECURITY.md).
