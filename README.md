# Muse Specialist Toolkit

### Your Muse. Your Specialists. Your Possibilities.

**15 AI Specialists** · **100+ Configurations** · **150+ Custom Connectors**

Make more of your Muse personal assistant. Explore specialists for software, research, creativity, learning and everyday life—then customize the tools and workflows around what you want to accomplish.

**[Choose a specialist](#find-your-specialist)** · **[Browse task configurations](collections/muse-starters-v1/CATALOG.md)** · **[Explore custom connectors](docs/connectors/README.md)** · **[Try Daily Desk](docs/spaces/DAILY_DESK.md)**

## Find your specialist

Start with what you want to do. Every specialist has its own methods, examples and customization options.

### Build and automate

- **[Software Engineer](presets/software-engineer/)** — Debug, review code and check changes with real tests.
- **[Data Engineering & Database Architect](presets/data-engineering-architect/)** — Explore data quality, schemas and migrations.
- **[Automation Engineer](presets/automation-engineer/)** — Design workflows, inspect dependencies and plan safe execution.
- **[Infrastructure & Reliability Engineer](presets/infrastructure-reliability-engineer/)** — Investigate reliability, incidents and capacity.

### Research and evaluate

- **[Research Evaluator](presets/research-evaluator/)** — Examine sources and test claims against evidence.
- **[Claims Adjudicator](presets/claims-adjudicator/)** — Compare conflicting information and build supported conclusions.
- **[Adversarial Verifier](presets/adversarial-verifier/)** — Test assumptions and document defensive findings.
- **[Reverse Engineering & Security Researcher](presets/reverse-engineering-researcher/)** — Analyze artifacts and observed behavior.

### Create and learn

- **[Creative Studio](presets/creative-studio/)** — Plan media production, storyboards and continuity.
- **[Product & Interface Designer](presets/product-interface-designer/)** — Work with interface states and usability checks.
- **[Model Builder](presets/model-builder/)** — Explore experiments, datasets and evaluation.
- **[Learning Coach](presets/learning-coach/)** — Practice, review material and track learning.

### Life and planning

- **[Personal Companion](presets/personal-companion/)** — Organize tasks, ideas and personal projects.
- **[Garden Companion](presets/garden-companion/)** — Keep plant records, observations and care plans.
- **[Coordinator](presets/coordinator/)** — Organize goals, dependencies and the next useful action.

## See it work

These are more than instruction files. The toolkit includes executable specialist tools and a working personal workspace.

**Run a specialist tool:** From a checkout with Python 3.12+, get an inspectable result using the supplied example data.

```bash
python -B tools/muse_collection.py demo data-engineer
```

**Open Personal Companion:** [Daily Desk](docs/spaces/DAILY_DESK.md) keeps tasks and notes across sessions, protects edits and supports backup and restoration.

```bash
python -B examples/daily_desk.py
```

**Customize your workflow:** Explore [100 task configurations](collections/muse-starters-v1/CATALOG.md), [specialist examples](docs/collection/SPECIALIST_QUICKSTART.md) and the [full specialist catalog](docs/collection/SPECIALIST_CATALOG.md).

## Explore custom connectors

Bring the services you already use into Muse. Browse **151 custom connectors**, organized around what you want to accomplish—not a long alphabetical table.

**[Find your connectors by category](docs/connectors/README.md)**

Work & productivity · AI & data · Development · Creative work · Business · Connected home · Publishing · Everyday life.

## Get started

**[Start with Muse](docs/v1/START_HERE.md)** for four practical paths: use a specialist, run a tool, open Daily Desk or add a connector.

Want to learn the system in depth? See the [capability guide](docs/CAPABILITIES.md), [installation guide](docs/GITHUB_QUICKSTART.md) and [practical handbook](docs/handbook/README.md).

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
