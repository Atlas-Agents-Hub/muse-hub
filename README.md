# Muse Hub

**Get more out of Muse.** Independently developed, open-source resources for exploring Muse, customizing assistants, connecting tools, and creating useful workspaces.

Choose from **15 independent assistants**, each with Main and **three subchats**. Add **75 skills**, **25 workflows**, **100 task starters**, and guides to **151 connectors**. Explore Companion Home, persistent notes, Studio, Arcade, and a library of 63 tools and projects.

**[Choose an assistant](docs/DOWNLOAD_A_SPECIALIST.md)** · **[Download v1.3.0](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.3.0)** · **[Visit Muse Hub](https://atlas-origins.github.io/muse-ai-agent-presets/)** · [Get started](docs/GETTING_STARTED.md)

## Start with what you want to do

- **[Organize your day](docs/journeys/ORGANIZE_YOUR_DAY.md):** goals and reminders in Muse, a Personal Companion, calendar connections, and a place for your notes.
- **[Build and automate](docs/journeys/BUILD_AND_AUTOMATE.md):** an engineering specialist, browser or terminal access, a reproducible workflow, and a review handoff.
- **[Create something](docs/journeys/CREATE_SOMETHING.md):** a creative brief, a production plan, media tools, and time to explore the Studio.

Explore [Muse's features](https://muse.ai/) and choose the Hub tools that fit your task. On the website, **Inside Muse**, **Included with Muse Hub**, and **Community project** labels show where each resource comes from.

## Choose your assistant

1. [Choose a specialist](docs/DOWNLOAD_A_SPECIALIST.md) for your task and download its ZIP.
2. Extract it into its own folder and give Muse the included `START_HERE.md`, or attach the ZIP with your current task.
3. Follow the guide to configure a separate Muse assistant, add its Main instructions and three subchats, and try the first task.

No Python is needed to use the assistant instructions. Each package includes the role's methods, selected skills, workflows, and examples. [Setup and saved data](docs/INSTALL_AND_PERSISTENCE.md) explains customization and updates.

## The 15 specialists

Choose a field to find its setup guides and first tasks.

<details>
<summary><strong>Build and automate</strong> — 4 specialists</summary>

- [Software Engineer](presets/software-engineer/INSTALL.md) — Reproduce a software defect and verify the fix.
- [Data Engineering & Database Architect](presets/data-engineering-architect/INSTALL.md) — Profile data, check schemas, and plan safe migrations.
- [Automation Engineer](presets/automation-engineer/INSTALL.md) — Build bounded workflows with approval and recovery gates.
- [Infrastructure & Reliability Engineer](presets/infrastructure-reliability-engineer/INSTALL.md) — Diagnose service failures and plan verifiable recovery.

</details>
<details>
<summary><strong>Research and review</strong> — 4 specialists</summary>

- [Research Evaluator](presets/research-evaluator/INSTALL.md) — Compare research claims against original sources and numerical evidence.
- [Claims Adjudicator](presets/claims-adjudicator/INSTALL.md) — Check competing claims and document the basis of a verdict.
- [Adversarial Verifier](presets/adversarial-verifier/INSTALL.md) — Challenge authorized releases with negative controls and reproducible evidence.
- [Reverse Engineering & Security Researcher](presets/reverse-engineering-researcher/INSTALL.md) — Study authorized application behavior and suspicious messages.

</details>
<details>
<summary><strong>Create and learn</strong> — 4 specialists</summary>

- [Creative Studio](presets/creative-studio/INSTALL.md) — Plan visual work from concept to verified production handoff.
- [Product & Interface Designer](presets/product-interface-designer/INSTALL.md) — Design and review user journeys, interfaces, states, and accessibility.
- [Model Builder](presets/model-builder/INSTALL.md) — Plan model training, artifact inspection, and evaluation.
- [Learning Coach](presets/learning-coach/INSTALL.md) — Turn source material into targeted study and review.

</details>
<details>
<summary><strong>Life and planning</strong> — 3 specialists</summary>

- [Personal Companion](presets/personal-companion/INSTALL.md) — Organize tasks, notes, preferences, and routines privately.
- [Garden Companion](presets/garden-companion/INSTALL.md) — Track plants, observations, seasons, and care.
- [Coordinator](presets/coordinator/INSTALL.md) — Organize a project across people and independent assistant workflows.

</details>

## Put your assistant to work

- **[Skills and workflows](docs/SKILLS.md):** choose a method for the task in front of you, from research checks and data analysis to design reviews and project handoffs.
- **[Task starters](collections/muse-starters-v1/CATALOG.md):** start from one of 100 focused configurations, then bring your own brief and files.
- **[Engineering](docs/WORKFLOWS.md#engineering-reproduce-repair-review):** reproduce a failure, make a focused repair, run regression checks, and review the result.
- **[Family Link](docs/FAMILY_LINK.md):** prepare a handoff with clear context, a recipient role, and an expected result.
- **[Companion Home](docs/COMPANION_HOME.md):** move between five rooms, save room notes, explore the Studio, and take an Arcade break. [Daily Desk](docs/spaces/DAILY_DESK.md) keeps tasks and notes together.
- **[Connectors](docs/connectors/README.md):** find setup instructions for 151 services, then choose the account and permissions for the service you need.

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

The first command prepares an editable assistant kit in a new folder. The second prints a worked data-engineering report. Continue with the [developer quickstart](docs/GITHUB_QUICKSTART.md) for more tools and exports.

## Explore Muse Hub

[The website](https://atlas-origins.github.io/muse-ai-agent-presets/) connects six starting points: Explore Muse, Specialists & Skills, Connect & Automate, Companion Spaces, Computer & Devices, and Resource Library. Its [resource explorer](https://atlas-origins.github.io/muse-ai-agent-presets/public/index.html) links to 63 tools, libraries, and projects from their original publishers.

[All downloads](https://atlas-origins.github.io/muse-ai-agent-presets/downloads.html) · [Current release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/latest) · [Downloads and checksums](docs/RELEASES.md) · [Documentation](docs/README.md) · [AI-agent discovery index](llms.txt) · [Security](SECURITY.md) · [Contributing](CONTRIBUTING.md) · [MIT license](LICENSE)
