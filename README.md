# Muse Hub

**One dedicated Muse assistant for each kind of work. Skills, workflows, source tools, and connector guides in one repository.**

Muse Hub is a community-built project for configuring and extending Muse assistants. It includes **15 independent assistants**, each with its own Main conversation and **three subchats**, plus **75 skills**, **25 workflows**, **100 task starters**, and **151 connector records**. Those records are not connected accounts.

**[Choose an assistant](docs/DOWNLOAD_A_SPECIALIST.md)** · [Specialist methods and engines](docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md) · **[Get the current published release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/latest)** · **[Browse tools](docs/CAPABILITIES.md)** · **[Explore connector records](docs/connectors/README.md)**

## Start with an assistant

1. [Choose a specialist](docs/DOWNLOAD_A_SPECIALIST.md) that matches your work.
2. Get its individual ZIP when **v1.1.0** is published. The 15 ZIPs are currently staged in a **draft** release; they are not yet public downloads. The [current published v1.0.0 release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.0.0) is available now.
3. Create a **separate Muse assistant** for that specialist. Use its Main files, then set up its three subchats inside the same assistant.
4. Start with a task. Use optional local tools or service connectors only when you need them and have authorized their setup.

Each assistant has its own instructions, documents, and memory. **Muse Hub does not put the 15 specialists inside one shared Muse account.** A downloaded package does not create accounts, grant permissions, or connect services.

## The 15 specialists

### Build and automate

- **[Software Engineer](presets/software-engineer/INSTALL.md)** — Reproduce bugs, implement changes, and check regressions.
- **[Data Engineering & Database Architect](presets/data-engineering-architect/INSTALL.md)** — Work with data quality, schemas, and migrations.
- **[Automation Engineer](presets/automation-engineer/INSTALL.md)** — Design workflows with approval, retry, and recovery boundaries.
- **[Infrastructure & Reliability Engineer](presets/infrastructure-reliability-engineer/INSTALL.md)** — Investigate incidents, capacity, and service reliability.

### Research and review

- **[Research Evaluator](presets/research-evaluator/INSTALL.md)** — Compare evidence, evaluate results, and record uncertainty.
- **[Claims Adjudicator](presets/claims-adjudicator/INSTALL.md)** — Trace claims to their evidence and preserve corrections.
- **[Adversarial Verifier](presets/adversarial-verifier/INSTALL.md)** — Find failures with authorized negative testing.
- **[Reverse Engineering & Security Researcher](presets/reverse-engineering-researcher/INSTALL.md)** — Study authorized software behavior and suspicious messages.

### Create and learn

- **[Creative Studio](presets/creative-studio/INSTALL.md)** — Plan visual work, animation, continuity, and delivery.
- **[Product & Interface Designer](presets/product-interface-designer/INSTALL.md)** — Design and review interfaces, states, and accessibility.
- **[Model Builder](presets/model-builder/INSTALL.md)** — Plan small-model training and held-out evaluation.
- **[Learning Coach](presets/learning-coach/INSTALL.md)** — Create source-grounded lessons, practice, and review.

### Life and planning

- **[Personal Companion](presets/personal-companion/INSTALL.md)** — Organize tasks, notes, and routines with Daily Desk.
- **[Garden Companion](presets/garden-companion/INSTALL.md)** — Record plants, seasons, observations, and care.
- **[Coordinator](presets/coordinator/INSTALL.md)** — Plan complex work, dependencies, and evidence-based handoffs.

## Tools, skills, and connectors

- **[Skills and workflows](docs/SKILLS.md):** 75 developed skills and 25 source workflows; the original role/shared procedures overlap these rather than increasing the unique count.
- **[Task starters](collections/muse-starters-v1/CATALOG.md):** 100 starters are task configurations, not 100 additional assistants.
- **[Local examples](docs/collection/SPECIALIST_QUICKSTART.md):** bounded Python engines for schema checks, research evaluation, reliability and other tasks. The [capability guide](docs/CAPABILITIES.md) identifies what ships and what requires a separate authorized runtime.
- **[Personal Companion Daily Desk](docs/spaces/DAILY_DESK.md):** a local SQLite task-and-note workbench with backup and restore.
- **[151 connector records](docs/connectors/README.md):** discover integrations and their original setup instructions. Listing a connector does not install or authenticate it.

To run the included source examples with Python 3.12+:

```sh
python -B tools/muse_collection.py demo data-engineer
python -B examples/daily_desk.py
```

The Daily Desk example should report `DAILY_DESK_VERTICAL_SLICE_PASS`. These are local calculations; they do **not** demonstrate native Muse agent installation or a model-backed autonomous assistant.

## The wider Muse Hub

Muse Hub is expanding beyond downloadable specialist kits to a discovery and workspace experience. See [Hub scope and maturity](hub/README.md) for what is available as source, what is still being integrated, and what remains private. Hub does **not** provide live Family Link routing, device control, a shared memory system, or automatic account access in this public repository.

## Documentation and versions

**[Documentation index](docs/README.md) · [Browse specialists by task](docs/handbook/specialists-by-task.md)** · [First-use guide](docs/v1/START_HERE.md) · [Installation and saved data](docs/INSTALL_AND_PERSISTENCE.md) · [Downloads and version status](docs/RELEASES.md) · [AI-agent discovery index](llms.txt) · [Developer source setup](docs/GITHUB_QUICKSTART.md) · [Verified capability facts](docs/discovery/agent-capabilities.json) · [Contribute](CONTRIBUTING.md) · [Security](SECURITY.md) · [MIT license](LICENSE)

[Original role contracts](docs/collection/SPECIALIST_CATALOG.md) document the historical specialist scope. The 50 original role/shared procedures overlap the 75 developed skills; configurations are not additional live assistants. The historical **v0.4.1-alpha** release included eight executable tools and eleven starter profiles. The published **v1.0.0** source and the historical [v0.4.1-alpha](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v0.4.1-alpha) executable kits are still available. The **v1.1.0** individual assistant ZIPs are draft assets pending required GitHub checks and publication. Read the version guide before following a ZIP link.

<details>
<summary>Developer setup and older standalone tool</summary>

Clone the repository and run local examples with Python 3.12+:

```sh
git clone https://github.com/atlas-origins/muse-ai-agent-presets.git
cd muse-ai-agent-presets
python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"
python -B quickstart.py --all
python -B examples/export_portable_skills.py --plan
```

An earlier [Creative Studio standalone ZIP](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v0.4.1-alpha/creative-studio-executable-v0.4.1-alpha.zip) runs with Python 3.12+ and no Git:

```sh
python -I -B run.py --operation self-test
python -I -B run.py --operation demo --to "$HOME/creative-production-demo"
```

The latter produces a textual storyboard and source artifacts, not rendered video. Verify release ZIPs against `SHA256SUMS.txt` and review local permissions before execution. Profiles are source-only, **not installed native Muse agents**; they are not a model-backed autonomous assistant out of the box, and they do not establish an authenticated Muse connection.

</details>
