# Muse Specialist Toolkit

### Your Muse. Your Specialists. Your Possibilities.

**15 AI Specialists** · **100+ Configurations** · **150+ Custom Connectors**

Pick a specialist for the job. Use a task configuration, run one of the included tools, or connect a service to Muse. Personal Companion includes Daily Desk for tasks and notes.

**[Choose a specialist](#find-your-specialist)** · **[Browse task configurations](collections/muse-starters-v1/CATALOG.md)** · **[Explore custom connectors](docs/connectors/README.md)** · **[Try Daily Desk](docs/spaces/DAILY_DESK.md)**

## Find your specialist

Open a specialist to see its methods, examples and configuration.

### Build and automate

- **[Software Engineer](presets/software-engineer/)** - Reproduce bugs, inspect code changes and run regression tests.
- **[Data Engineering & Database Architect](presets/data-engineering-architect/)** - Check duplicate keys, field completeness and schema changes.
- **[Automation Engineer](presets/automation-engineer/)** - Validate dependencies and review retry rules.
- **[Infrastructure & Reliability Engineer](presets/infrastructure-reliability-engineer/)** - Calculate error budgets and examine incident evidence.

### Research and evaluate

- **[Research Evaluator](presets/research-evaluator/)** - Check quotations, sources and evaluation results.
- **[Claims Adjudicator](presets/claims-adjudicator/)** - Trace claims to sources and record conflicts.
- **[Adversarial Verifier](presets/adversarial-verifier/)** - Run bounded defensive checks and record findings.
- **[Reverse Engineering & Security Researcher](presets/reverse-engineering-researcher/)** - Compare artifacts and recorded system behavior.

### Create and learn

- **[Creative Studio](presets/creative-studio/)** - Produce briefs, storyboards and continuity records.
- **[Product & Interface Designer](presets/product-interface-designer/)** - Audit UI states, control labels and user journeys.
- **[Model Builder](presets/model-builder/)** - Review datasets, experiments and evaluation metrics.
- **[Learning Coach](presets/learning-coach/)** - Run practice sessions, score answers and review weak areas.

### Life and planning

- **[Personal Companion](presets/personal-companion/)** - Keep tasks and notes in Daily Desk and organize personal plans.
- **[Garden Companion](presets/garden-companion/)** - Record plant observations and track care routines.
- **[Coordinator](presets/coordinator/)** - Map dependencies, decisions and handoffs.

## Try the tools

Both examples run with the included data. One checks a schema change; the other creates and restores a task-and-note store.

**Data Engineer:** Review a 40-row schema change, including a newly added `note` field (Python 3.12+):

```bash
python -B tools/muse_collection.py demo data-engineer
```

**Daily Desk:** [Open the Personal Companion guide](docs/spaces/DAILY_DESK.md) for tasks, notes, revision-checked edits and backup/restore.

```bash
python -B examples/daily_desk.py
```

Expected result: `DAILY_DESK_VERTICAL_SLICE_PASS`, with three tasks, two notes, and a restored copy.

For other tasks: [100 task configurations](collections/muse-starters-v1/CATALOG.md), [specialist examples](docs/collection/SPECIALIST_QUICKSTART.md), or the [full specialist catalog](docs/collection/SPECIALIST_CATALOG.md).

## Connect your services

Browse **151 custom connectors** for development, productivity, design, home devices and other services. Entries link to setup instructions and original source documentation.

**[Browse the connector directory](docs/connectors/README.md)**

## Setup and documentation

The [setup guide](docs/v1/START_HERE.md) covers configuring a specialist, running tools, using Daily Desk and adding connectors.

[Capability guide](docs/CAPABILITIES.md) | [Installation guide](docs/GITHUB_QUICKSTART.md) | [Practical handbook](docs/handbook/README.md)

---

## For developers

[Contribute](CONTRIBUTING.md) · [Browse source](src/muse_presets/) · [AI-agent discovery index](llms.txt) · [Verified capability facts](docs/discovery/agent-capabilities.json) · [MIT license](LICENSE)

<details>
<summary>Package details, verification and earlier downloads</summary>

The source catalog includes **15 specialists, 75 skills, 25 workflows and 100 starters**. The 100 task starters and 15 role profiles provide 100+ choices; the original 50 role/shared procedures overlap the 75 developed skills.

Create an editable profile using the current source:

```bash
git clone https://github.com/sethburkhardt21-dev/muse-ai-agent-presets.git
cd muse-ai-agent-presets
python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"
python -B quickstart.py --all
python -B examples/export_portable_skills.py --plan
```

Profiles are source-only drafts, **not installed native Muse agents**. A profile is **not a model-backed autonomous assistant**; you customize it for your existing Muse. The executable tools run under your computer's permissions.

The earlier release includes eight executable tools and eleven starter profiles.

The earlier [v0.4.1-alpha executable collection](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/tag/v0.4.1-alpha) includes a downloadable [Creative Studio executable](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/download/v0.4.1-alpha/creative-studio-executable-v0.4.1-alpha.zip). Verify it using [SHA256SUMS.txt](https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/download/v0.4.1-alpha/SHA256SUMS.txt), then extract and run:

```bash
python -I -B run.py --operation self-test
python -I -B run.py --operation demo --to "$HOME/creative-production-demo"
```

See [downloads and versions](docs/RELEASES.md) for the latest release assets and the historical packages. Tests, source-integrity checks and documented capability boundaries are available in the repository.

</details>
