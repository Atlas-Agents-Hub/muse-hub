# Tools for your specialist

Muse Hub brings together 15 assistants, 5242 skills, 396 workflows, 558 task starters, and 273 connector guides. [Choose an assistant](DOWNLOAD_A_SPECIALIST.md), [run a tool](collection/SPECIALIST_QUICKSTART.md), or [connect a service](connectors/README.md).

## Find the right tools

| Specialist | Included methods and tools |
| --- | --- |
| Coordinator | Project plans, dependency review, task handoffs, and completion-evidence checks. |
| Software Engineer | Defect reproduction, focused repair, regression tests, Claim Gate, and source provenance. |
| Model Builder | Dataset preparation, small-model training, held-out metrics, and model-artifact inspection. |
| Research Evaluator | Quotation tracing, evidence comparison, numerical evaluation, and source-family checks. |
| Creative Studio | Creative direction, production planning, asset dependencies, shot timelines, continuity records, and storyboard exports. |
| Adversarial Verifier | Threat modeling, authorized failure testing, negative controls, and remediation review. |
| Personal Companion | Daily planning, preferences, Daily Desk tasks and notes, and Companion Home's room notebook. |
| Garden Companion | Plant observations, seasonal planning, versioned records, and a saved local calendar. |
| Learning Coach | Lessons, practice, scoring, review history, and study-session storage. |
| Claims Adjudicator | Claim comparison, source tracing, counterexamples, and qualified findings. |
| Reverse Engineering & Security Researcher | Authorized behavior analysis, protocol study, and comparison of application observations. |
| Data Engineering & Database Architect | Schema comparison, record quality, versioned-event reconciliation, and SQLite query-plan analysis. |
| Infrastructure & Reliability Engineer | Error budgets, capacity estimates, incident timelines, and recovery planning. |
| Automation Engineer | Workflow graphs, approval points, target selection, and interrupted-action reconciliation. |
| Product & Interface Designer | User journeys, design systems, label checks, contrast calculations, and interaction-state coverage. |

The [specialist methods guide](collection/SPECIALIST_SCOPE_AND_ENGINES.md) describes each role in more detail. Each assistant can use the tools and service connections you make available for its task.

## Run an example

From the toolkit root with Python 3.12+:

```sh
python -B tools/muse_collection.py demo data-engineer
python -B tools/muse_collection.py demo reliability-engineer
python -B tools/muse_collection.py demo automation-engineer
python -B tools/muse_collection.py demo product-interface-designer
python -B examples/daily_desk.py
```

The first four print reports from worked inputs. Daily Desk exercises task and note creation, editing, reopening, and restoration. [Workflows](WORKFLOWS.md) includes more examples and expected results.

## Choose your setup

- **Assistant instructions:** download a specialist and follow `START_HERE.md` in Muse.
- **Local tools:** use Python 3.12+; repository workflows also use Git. Follow each package's commands on Windows, macOS, or Linux.
- **Creative production:** use your chosen image, animation, video, or design tool for rendering. The included planner produces briefs, shot lists, and textual storyboards.
- **Services and devices:** use the [connector guide](connectors/README.md) for the account and permissions needed by that service.
- **Larger model training:** provide a suitable training host and dataset for the experiment you plan.

## Portable executable tools

[Creative Studio](kits/CREATIVE_SOURCEKIT.md) · [Claims](kits/CLAIMS_SOURCEKIT.md) · [Garden](kits/GARDEN_SOURCEKIT.md) · [Learning](kits/LEARNING_SOURCEKIT.md) · [Observation comparison](kits/REVERSE_SOURCEKIT.md) · [Engineering, Coordinator, and Model Builder](WORKFLOWS.md)

## Personal workspaces

[Daily Desk](spaces/DAILY_DESK.md) combines tasks and notes with revision checks, backup, and restore. [Companion Home](COMPANION_HOME.md) organizes notes across five rooms with Studio and Arcade activities. Choose a private database path and keep it when updating the application.

[Get started](GETTING_STARTED.md) · [Terminal](TERMINAL.md) · [Downloads](RELEASES.md)
