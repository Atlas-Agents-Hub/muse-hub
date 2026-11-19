# Muse Hub

**Get more out of Muse.** Bring AI agent skills, workflow automation and custom tools to your personal AI assistant. This open-source toolkit for Meta's Muse AI helps you build, research, create and plan: choose a specialist, connect your services, and start a useful project.

Choose from **15 independent assistants**, each with Main and **three subchats**. Add **5242 skills**, **396 workflows**, **51 tool guides**, **558 task starters**, and **273 connectors**. Explore Companion Home, persistent notes, Studio, Arcade, and a library of 63 tools and projects.

**[Choose an assistant](docs/DOWNLOAD_A_SPECIALIST.md)** · **[Download v1.6.0](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.6.0)** · **[Visit Muse Hub](https://atlas-origins.github.io/muse-ai-agent-presets/)** · [Get started](docs/GETTING_STARTED.md)

## Start with what you want to do

- **[Organize your day](docs/journeys/ORGANIZE_YOUR_DAY.md):** ready-to-copy reminder, calendar and goal worksheets, a Personal Companion, and a place for your notes.
- **[Build and automate](docs/journeys/BUILD_AND_AUTOMATE.md):** an engineering specialist, terminal tools, HTML accessibility checks, browser testing, and a review handoff.
- **[Create something](docs/journeys/CREATE_SOMETHING.md):** a creative brief, a production plan, media tools, and time to explore the Studio.

## Choose your assistant

1. [Choose a specialist](docs/DOWNLOAD_A_SPECIALIST.md) for your task and download its ZIP.
2. Extract it into its own folder and give Muse the included `START_HERE.md`, or attach the ZIP with your current task.
3. Follow the guide to configure a separate Muse assistant, add its Main instructions and three subchats, and try the first task.

Each package brings the role's methods, skills, workflows and examples together. [Setup and saved data](docs/INSTALL_AND_PERSISTENCE.md) covers customization and updates.

## The 15 specialists

<details>
<summary><strong>Build and automate</strong> — 4 specialists</summary>

- [Software Engineer](presets/software-engineer/INSTALL.md) — Build apps, design APIs, debug, refactor, test and release software.
- [Data Engineering & Database Architect](presets/data-engineering-architect/INSTALL.md) — Design databases, build pipelines, analyze SQL and manage data quality.
- [Automation Engineer](presets/automation-engineer/INSTALL.md) — Connect steps into repeatable workflows, manage permissions, and recover interrupted work.
- [Infrastructure & Reliability Engineer](presets/infrastructure-reliability-engineer/INSTALL.md) — Deploy infrastructure, improve reliability, investigate incidents and plan recovery.

</details>
<details>
<summary><strong>Research and review</strong> — 4 specialists</summary>

- [Research Evaluator](presets/research-evaluator/INSTALL.md) — Compare research claims against original sources and numerical evidence.
- [Claims Adjudicator](presets/claims-adjudicator/INSTALL.md) — Check competing claims and document the basis of a verdict.
- [Adversarial Verifier](presets/adversarial-verifier/INSTALL.md) — Test failure cases, find security weaknesses, and check that fixes hold up.
- [Reverse Engineering & Security Researcher](presets/reverse-engineering-researcher/INSTALL.md) — Analyze software, protocols and application behavior in authorized projects.

</details>
<details>
<summary><strong>Create and learn</strong> — 4 specialists</summary>

- [Creative Studio](presets/creative-studio/INSTALL.md) — Create visual concepts, images, animation, video and interactive scenes.
- [Product & Interface Designer](presets/product-interface-designer/INSTALL.md) — Design and review user journeys, interfaces, states, and accessibility.
- [Model Builder](presets/model-builder/INSTALL.md) — Build AI applications, design datasets, plan training and evaluate models.
- [Learning Coach](presets/learning-coach/INSTALL.md) — Create lessons, flashcards, practice sessions and adaptive study plans.

</details>
<details>
<summary><strong>Life and planning</strong> — 3 specialists</summary>

- [Personal Companion](presets/personal-companion/INSTALL.md) — Organize tasks, notes, preferences, and routines privately.
- [Garden Companion](presets/garden-companion/INSTALL.md) — Track plants, observations, seasons, and care.
- [Coordinator](presets/coordinator/INSTALL.md) — Plan complex goals, coordinate specialists and carry projects through delivery.

</details>

## Put your assistant to work

- **[Tools for each specialist](docs/collection/SPECIALIST_LIBRARY.md):** find included methods, workflows and recommended plugins for your work.
- **[51 tool guides](docs/tools/README.md):** follow setup instructions and practical recipes for research, automation, design, software and data tools.
- **[Skills and workflows](docs/SKILLS.md):** find methods for research, data analysis, design reviews and project handoffs.
- **[Task starters](collections/muse-starters-v1/CATALOG.md):** start from one of 558 focused configurations, then bring your own brief and files.
- **[Engineering](docs/WORKFLOWS.md#engineering-reproduce-repair-review):** reproduce a failure, make a focused repair, run regression checks, and review the result.
- **[Family Link](docs/FAMILY_LINK.md):** prepare a handoff with clear context, a recipient role, and an expected result.
- **[Companion workspaces](docs/COMPANION_HOME.md):** move between five rooms, save room notes, explore the Studio, and take an Arcade break. [Daily Desk](docs/spaces/DAILY_DESK.md) keeps tasks and notes together; [Muse Task Board](docs/spaces/TASK_BOARD.md) moves project cards from To do to Done.
- **[Connectors](docs/connectors/README.md):** find setup instructions for 273 services, then choose the account and permissions for the service you need.

Explore [specialists by task](docs/handbook/specialists-by-task.md) or browse the [included tools](docs/CAPABILITIES.md).

## Use Muse from your terminal

The [terminal guide](docs/TERMINAL.md) covers chatting with your personal Muse through `muse-cli`, working with side chats, and running the included Python tools on Windows, macOS, and Linux.

For the toolkit commands below, use Python 3.12+ and Git:

```sh
git clone https://github.com/atlas-origins/muse-ai-agent-presets.git
cd muse-ai-agent-presets
python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"
python -B tools/muse_collection.py demo data-engineer
```

Prepare an editable assistant kit, then run a worked data-engineering example. The [developer quickstart](docs/GITHUB_QUICKSTART.md) covers more tools and exports.

## Find and build your own pack

Search the catalog from your toolkit checkout:

```sh
python -B tools/discover.py search "sql query"
```

Filter by specialist, preview a selection with `plan`, then use `build` to create a ZIP with its skills, workflows and supporting files. [Find and build guide](docs/collection/FIND_AND_BUILD.md).

## Explore Muse Hub

Explore [Muse features](https://muse.ai/), companion spaces, computer tools and automation on [the website](https://atlas-origins.github.io/muse-ai-agent-presets/). Search the [63-resource library](https://atlas-origins.github.io/muse-ai-agent-presets/public/index.html) for your next tool or project.

[All downloads](https://atlas-origins.github.io/muse-ai-agent-presets/downloads.html) · [Current release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/latest) · [Downloads and checksums](docs/RELEASES.md) · [Documentation](docs/README.md) · [AI-agent discovery index](llms.txt) · [Security](SECURITY.md) · [Contributing](CONTRIBUTING.md) · [MIT license](LICENSE)
