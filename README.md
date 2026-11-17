# Muse Hub

**Independently developed for focused work inside Muse.** Configure one specialist at a time, with its own Main conversation and **three subchats**. The toolkit contains **15 independent assistants**, **75 skills**, **25 workflows**, **100 task starters**, and **151 connector records**—not automatically connected accounts.

**[Choose an assistant](docs/DOWNLOAD_A_SPECIALIST.md)** · **[Get the current published release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/latest)** · [Browse tools](docs/CAPABILITIES.md) · [Explore connector records](docs/connectors/README.md)

## Start with an assistant

1. [Choose a specialist](docs/DOWNLOAD_A_SPECIALIST.md) below and read its setup guide.
2. Use the **[published v1.0.0 source release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.0.0)** or [source checkout](docs/v1/START_HERE.md). The 15 individual **v1.1.0 ZIPs remain a draft**; they are not public downloads.
3. Set up a **separate Muse assistant** for the chosen role, then add its Main instructions and three subchats as appropriate. Source profiles do not provision Muse accounts, memory, credentials, or tools.

**Explore first:** [Find specialists by task](docs/handbook/specialists-by-task.md) · [Specialist methods and engines](docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md) · [Verified capability facts](docs/discovery/agent-capabilities.json).

## The 15 specialists

Choose a discipline to expand its independently maintained role guides.

<details>
<summary><strong>Build and automate</strong> — 4 specialists</summary>

- [Software Engineer](presets/software-engineer/INSTALL.md) — Debugging, real tests, bounded code repair.
- [Data Engineering & Database Architect](presets/data-engineering-architect/INSTALL.md) — Pipelines, migrations, schemas and data quality.
- [Automation Engineer](presets/automation-engineer/INSTALL.md) — Scoped workflows, recovery and approval boundaries.
- [Infrastructure & Reliability Engineer](presets/infrastructure-reliability-engineer/INSTALL.md) — Incident investigation and system reliability.

</details>

<details>
<summary><strong>Research and review</strong> — 4 specialists</summary>

- [Research Evaluator](presets/research-evaluator/INSTALL.md) — Evidence, evaluation and uncertainty.
- [Claims Adjudicator](presets/claims-adjudicator/INSTALL.md) — Claim provenance and correction.
- [Adversarial Verifier](presets/adversarial-verifier/INSTALL.md) — Authorized negative testing.
- [Reverse Engineering & Security Researcher](presets/reverse-engineering-researcher/INSTALL.md) — Defensive research and permitted software analysis.

</details>

<details>
<summary><strong>Create and learn</strong> — 4 specialists</summary>

- [Creative Studio](presets/creative-studio/INSTALL.md) — Media planning, animation and continuity.
- [Product & Interface Designer](presets/product-interface-designer/INSTALL.md) — Design systems, usability and accessibility.
- [Model Builder](presets/model-builder/INSTALL.md) — Datasets, training experiments and held-out evaluation.
- [Learning Coach](presets/learning-coach/INSTALL.md) — Lessons, practice and review.

</details>

<details>
<summary><strong>Life and planning</strong> — 3 specialists</summary>

- [Personal Companion](presets/personal-companion/INSTALL.md) — Notes, routines and a local Daily Desk.
- [Garden Companion](presets/garden-companion/INSTALL.md) — Plants, seasons, observations and care.
- [Coordinator](presets/coordinator/INSTALL.md) — Dependencies, task plans and evidence-based handoffs.

</details>

## Tools, skills, and connectors

These are working **source-only and offline** capabilities, not a claim that they have been installed into a Muse account.

- **[Five-door engineering (H11)](kits/engineering-doors/README.md):** an S1 capture → S2 RED → S3 scoped repair → S4 GREEN → S5 local independent review demonstration, reusing the existing Claim Gate.
- **[Family Link (H12)](kits/family-handoff/README.md):** a bounded, replay-aware offline envelope and [portable source kit](docs/kits/FAMILY_LINK_SOURCEKIT.md). No authenticated cross-account delivery is claimed.
- **[Muse CLI compatibility (H03)](docs/discovery/ROUTE_COMPATIBILITY.md):** pinned 258/402 historical method comparison, not verified live API access.
- **[Skills and workflows](docs/SKILLS.md):** 75 skills and 25 workflows. The 100 starters are [selectable task configurations](collections/muse-starters-v1/CATALOG.md), not additional agents.
- **[Daily Desk](docs/spaces/DAILY_DESK.md):** local SQLite tasks and notes with backup/restore. [151 connector records](docs/connectors/README.md) are research and setup references, not authorized services.

**[H00–H21 feature and acceptance tracker](docs/HUB_FEATURE_READINESS.md)** separates source-tested features from provider, device, security, and release work that remains unverified.

For role details, read the [specialist quickstart](docs/collection/SPECIALIST_QUICKSTART.md) and [specialist catalog](docs/collection/SPECIALIST_CATALOG.md).

## Try a local tool

Python 3.12+ is required for the included tools. Use reviewed source in a disposable workspace.

```sh
git clone https://github.com/atlas-origins/muse-ai-agent-presets.git
cd muse-ai-agent-presets
python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"
python -B quickstart.py --all
python -B examples/export_portable_skills.py --plan
python -B tools/muse_collection.py demo data-engineer
python -B examples/daily_desk.py
PYTHONPATH=src python -B examples/five_door_offline_demo.py
```

For configuration, see [developer source setup](docs/GITHUB_QUICKSTART.md), the [general first-use guide](docs/v1/START_HERE.md), and [installation and saved data](docs/INSTALL_AND_PERSISTENCE.md).

## Standalone Muse Hub website

The [Muse Hub website source](hub/site/index.html) and [63-reference source explorer](hub/site/public/index.html) are independently branded; the site is **not deployed**. The source preview does not authenticate Muse accounts, issue permissions, or connect devices.

## Releases and boundaries

**v1.0.0** is the current published source release; **v1.1.0** is a draft. The historical **v0.4.1-alpha** executable examples remain available. That earlier scope included **eleven roles and eight runnable offline tools**, not the current 15 specialist packages. The **50 original role/shared procedures** overlap the 75 developed skills. [See verified downloads and checksums](docs/RELEASES.md).

These profiles are **not installed native Muse agents** and do not imply an authenticated assistant, model, or remote capability. Original TaskGuard/retention production holds and native Family Link acceptance remain open. Read the [capability ledger](docs/CAPABILITIES.md) before enabling an extension.

For the historical Creative Studio standalone ZIP, use its extracted \`run.py\` with:

\`\`\`sh
python -I -B run.py --operation demo --to "$HOME/creative-production-demo"
\`\`\`

[Documentation](docs/README.md) · [AI-agent discovery index](llms.txt) · [Security](SECURITY.md) · [Contributing](CONTRIBUTING.md) · [MIT license](LICENSE)
