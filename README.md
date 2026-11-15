# Muse Specialist Toolkit

### Your Muse. Your Specialists. Your Possibilities.

**15 AI Specialists** · **100+ Configurations** · **150+ Custom Connectors**

Pick a specialist for the job. Use a task configuration, run one of the included tools, or connect a service to Muse. Personal Companion includes Daily Desk for tasks and notes.

**[Choose a specialist](#find-your-specialist)** · **[Browse task configurations](collections/muse-starters-v1/CATALOG.md)** · **[Explore custom connectors](docs/connectors/README.md)** · **[Try Daily Desk](docs/spaces/DAILY_DESK.md)**

## Find your specialist

Each specialist has a playbook covering its field. Open a role for its methods and examples; the [capability guide](docs/CAPABILITIES.md) shows which executable operations are included.

### Build and automate

- **[Software Engineer](presets/software-engineer/)** - Build and debug maintainable software, from reproducing defects and implementing fixes to regression testing and verified source handoffs.
- **[Data Engineering & Database Architect](presets/data-engineering-architect/)** - Design reliable data systems: profile data quality, define schema contracts, reconcile records and plan safe migrations.
- **[Automation Engineer](presets/automation-engineer/)** - Design dependable workflows, map dependencies, prepare service integrations, guard duplicate effects and define safe retry handling.
- **[Infrastructure & Reliability Engineer](presets/infrastructure-reliability-engineer/)** - Improve service reliability with SLOs, error budgets, incident analysis, capacity plans and verified recovery checks.

### Research and evaluate

- **[Research Evaluator](presets/research-evaluator/)** - Investigate research questions with primary evidence, controlled experiments, competing explanations and independent evaluation.
- **[Claims Adjudicator](presets/claims-adjudicator/)** - Assess complex claims against original evidence, resolve conflicting results, issue scoped verdicts and preserve corrections.
- **[Adversarial Verifier](presets/adversarial-verifier/)** - Challenge authorized systems for security weaknesses, reproduce failures, test permission boundaries and verify fixes.
- **[Reverse Engineering & Security Researcher](presets/reverse-engineering-researcher/)** - Understand authorized software and protocols through observed behavior, scoped experiments, defensive trace analysis and clean-room models.

### Create and learn

- **[Creative Studio](presets/creative-studio/)** - Develop visual media, animation, video and interactive scenes—from creative direction and asset planning through render review, continuity and delivery. [Creative production scope](docs/collection/CREATIVE_STUDIO_SCOPE.md).
- **[Product & Interface Designer](presets/product-interface-designer/)** - Design and evaluate product experiences, from user journeys and interaction states to accessibility checks and build-ready specifications.
- **[Model Builder](presets/model-builder/)** - Build and refine learned models and adapters: plan training, evaluate held-out results, inspect model artifacts and track provenance.
- **[Learning Coach](presets/learning-coach/)** - Turn study material into guided lessons, adaptive practice, scored assessments and targeted review informed by learner progress.

### Life and planning

- **[Personal Companion](presets/personal-companion/)** - Support daily life with personalized planning, routines, private notes, accessibility preferences and privacy-aware assistance.
- **[Garden Companion](presets/garden-companion/)** - Support garden care across the seasons: track plants, document observations, plan seasonal tasks and maintain an evidence-aware care journal.
- **[Coordinator](presets/coordinator/)** - Organize complex goals across specialist workflows: sequence dependencies, preserve handoffs, reconcile interruptions and verify completion.

## Built-in engines and workbenches

Each specialist has field-specific methods. The included engines handle reviewed code repairs, model training experiments, research evaluation, creative production planning, data and reliability analysis, workflow checks and interface validation. Personal Companion adds the persistent Daily Desk. [See each specialist's methods, engines and examples](docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md).

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

For other tasks: [100 task configurations](collections/muse-starters-v1/CATALOG.md), [specialist examples](docs/collection/SPECIALIST_QUICKSTART.md), or the [full specialist catalog](docs/collection/SPECIALIST_CATALOG.md) or [specialists and included tools](docs/handbook/specialists-by-task.md).

## Connect your services

Browse **151 custom connectors** for development, productivity, design, home devices and other services. Entries link to setup instructions and original source documentation.

**[Browse the connector directory](docs/connectors/README.md)**

## Setup and documentation

The [setup guide](docs/v1/START_HERE.md) covers configuring a specialist, running tools, using Daily Desk and adding connectors.

[Documentation](docs/README.md) | [Capability guide](docs/CAPABILITIES.md) | [Installation guide](docs/GITHUB_QUICKSTART.md) | [Practical handbook](docs/handbook/README.md)

---

## For developers

[Contribute](CONTRIBUTING.md) · [Browse source](src/muse_presets/) · [AI-agent discovery index](llms.txt) · [Verified capability facts](docs/discovery/agent-capabilities.json) · [MIT license](LICENSE)

<details>
<summary>Package details, verification and earlier downloads</summary>

The source catalog includes **15 specialists, 75 skills, 25 workflows and 100 starters**. The 100 task starters and 15 role profiles provide 100+ choices; the original 50 role/shared procedures overlap the 75 developed skills.

Create an editable profile using the current source:

```bash
git clone https://github.com/atlas-origins/muse-ai-agent-presets.git
cd muse-ai-agent-presets
python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"
python -B quickstart.py --all
python -B examples/export_portable_skills.py --plan
```

Profiles are source-only drafts, **not installed native Muse agents**. A profile is **not a model-backed autonomous assistant**; you customize it for your existing Muse. The executable tools run under your computer's permissions.

The earlier release includes eight executable tools and eleven starter profiles.

The earlier [v0.4.1-alpha executable collection](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v0.4.1-alpha) includes a downloadable [Creative Studio executable](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v0.4.1-alpha/creative-studio-executable-v0.4.1-alpha.zip). Verify it using [SHA256SUMS.txt](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v0.4.1-alpha/SHA256SUMS.txt), then extract and run:

```bash
python -I -B run.py --operation self-test
python -I -B run.py --operation demo --to "$HOME/creative-production-demo"
```

See [downloads and versions](docs/RELEASES.md) for the latest release assets and the historical packages. Tests, source-integrity checks and documented capability boundaries are available in the repository.

</details>
