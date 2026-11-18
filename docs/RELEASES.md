# Muse Hub downloads and versions

**Current release: [v1.5.0](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.5.0)** · [Latest release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/latest) · [SHA256SUMS](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.5.0/SHA256SUMS)

## v1.5.0 — a larger library for your work

[Choose one of the 15 assistants](DOWNLOAD_A_SPECIALIST.md). Each ZIP brings together its Main instructions, three subchat guides, selected skills, workflows, examples, and `START_HERE.md`.

The collection includes 461 skills, 58 workflows, 100 task starters, and setup references for 151 connectors. The current toolkit also includes Companion Home and its room notebook, Daily Desk, specialist tools, and command-line guides.

Extract your package into a new folder and start with its included guide. Assistant instructions require no Python. Optional local programs state their requirements beside their commands; repository examples use Python 3.12+.

This update adds **386 skills** across engineering, research, design, data, operations, creative work and personal planning. Each skill ZIP contains its instructions and supporting files. The [skill index](../collections/muse-starters-v1/SKILL_INDEX.md) groups them by subject.

The **33 new workflows** combine methods into complete tasks: build a cited research brief, evaluate a RAG system, prepare a mobile release, audit cloud costs, improve a design system, organize interviews or plan a garden. Every stage names its input, output and result check. [Browse all 58 workflows](../collections/library/WORKFLOWS.md).

**51 tool guides** provide setup steps, practical examples and checks for engineering, search, design, automation, data, research and creative tools. Relevant guides and workflows are included in every [specialist package](collection/SPECIALIST_LIBRARY.md). The [download page](https://atlas-origins.github.io/muse-ai-agent-presets/downloads.html) filters by type, specialist and subject, and lets you share a filtered selection.

## Complete collections

- [Complete toolkit](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.5.0/muse-specialist-toolkit-v1.5.0.zip)
- [All specialists](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.5.0/muse-specialists-v1.5.0.zip)
- [Skills](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.5.0/muse-skills-v1.5.0.zip)
- [Workflows](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.5.0/muse-workflows-v1.5.0.zip)
- [Tool guides](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.5.0/muse-tool-guides-v1.5.0.zip)
- [Task starters](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.5.0/muse-starters-v1.5.0.zip)

## Verify your download

Download `SHA256SUMS` from the same release. Calculate the archive's SHA-256 and compare it with the line for that exact filename.

**Windows PowerShell:**

```powershell
Get-FileHash -Algorithm SHA256 .\muse-personal-companion-v1.5.0.zip
```

**macOS:**

```sh
shasum -a 256 muse-personal-companion-v1.5.0.zip
```

**Linux:**

```sh
sha256sum muse-personal-companion-v1.5.0.zip
```

Keep the original ZIP and your customized working copy separately. [Setup and saved data](INSTALL_AND_PERSISTENCE.md) explains updates and backup.

## Earlier releases

### v1.4.0 — reusable plans and accessibility checks

The [v1.4.0 release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.4.0) added reminder, calendar and goal worksheets plus an HTML accessibility checker, with examples included in the relevant downloads.


### v1.3.0 - choose work that fits

The [v1.3.0 release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.3.0) added exact RICE scoring, prerequisite-aware planning, resource budgets and JSON/CSV examples to the existing Project Prioritization kit. Its original archives and checksums remain available.

### v1.2.0 - explore the whole Hub

The [v1.2.0 release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.2.0) opened six homepage paths, added guides for planning, engineering and creative work, and introduced shareable resource filters with browser Back and Forward. Its original archives and checksums remain available.

### v1.1.2 - consistent release labels

The [v1.1.2 release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.1.2) generates homepage, specialist and Downloads version labels from the release catalog. Its archives and checksums remain available.

### v1.1.1 - smoother setup and navigation

The [v1.1.1 release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.1.1) fixes skill-guide paths, includes kit practice files, improves keyboard and mobile navigation, and clarifies setup guides. Its original archives and checksums remain available.

### v1.1.0 — individual specialists, skills and workflows

The [v1.1.0 release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.1.0) introduced individual downloads for all 15 specialists, 75 skills and 25 workflows, together with the published Muse Hub website. Its original archives and checksums remain available.

### v1.0.0 — toolkit, collection, and connectors

The [v1.0.0 release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.0.0) contains the earlier complete toolkit, specialist collection, and connector directory. Use its included instructions when working with those archives.

- [Toolkit](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.0.0/muse-specialist-toolkit-v1.0.0.zip)
- [Specialist collection](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.0.0/muse-specialist-collection-v1.0.0.zip)
- [Connector directory](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.0.0/muse-custom-connectors-v1.0.0.zip)
- [Checksums](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.0.0/SHA256SUMS.txt)

### v0.4.1-alpha — eight runnable tools and eleven starter ZIPs

The [v0.4.1-alpha release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v0.4.1-alpha) preserves eight standalone Python tools and eleven starter profiles with their original guides and checksums.

For the archived Creative Studio executable, its extracted runner accepts:

```sh
python -I -B run.py --operation self-test
python -I -B run.py --operation demo --to "$HOME/creative-production-demo"
```

That command writes a production plan, shot-list CSV, and textual HTML storyboard. Current specialist downloads are listed at the top of this page.

[Get started](GETTING_STARTED.md) · [Terminal](TERMINAL.md) · [Security](SECURITY.md)
