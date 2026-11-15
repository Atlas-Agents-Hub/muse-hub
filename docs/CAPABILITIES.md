# Capabilities

**15 specialist profiles · 100 task starters · 75 developed skills · 25 workflows · 151 custom connectors.**

[Choose a specialist](collection/SPECIALIST_CATALOG.md), [run a tool](collection/SPECIALIST_QUICKSTART.md), open [Daily Desk](spaces/DAILY_DESK.md), or [find a connector](connectors/README.md). [Downloads](RELEASES.md) lists the published V1 packages.

The original **50 role/shared instruction procedures** are retained within the wider skills architecture and overlap the 75 developed task skills. The [full specialist and engine guide](collection/SPECIALIST_SCOPE_AND_ENGINES.md) describes each role's field-wide methods alongside its shipped engines. The table below covers **bundled operations**, not the limits of work the specialist can perform with authorized host tools.

The published **v1.0.0** source package contains these components. Historical **v0.4.1-alpha** downloads included eight executable ZIPs and eleven starter profiles.

## Choose a tool or profile

| Specialist | Included source operation | Host/integration boundary |
| --- | --- | --- |
| `coordinator` | Review task plans, dependencies and supplied completion evidence; export a standalone tool. | Does not dispatch workers or run a scheduler. |
| `software-engineer` | Engineering sourcekit, Claim Gate, reviewed repair/test workflows and source provenance; Iron Ledger and Provenance Vault source candidates. | Local execution is not an OS sandbox; evidence-only candidates retain separate approval requirements. |
| `model-builder` | Train small synthetic models, calculate held-out metrics and inspect local model artifacts. | No GPU service or large-model fine-tuning. |
| `research-evaluator` | Match quotations to supplied text; score predictions and check group leakage. | Does not authenticate publishers or establish scientific truth. |
| `creative-studio` | Compile briefs into asset dependencies, shot timelines, continuity records and reviewed production exports. | Real images, animation and video are created and inspected through authorized render/design tools; source planner does not replace them. |
| `adversarial-verifier` | Defensive review instructions and refusal-test patterns. **Template only** as a standalone public package. | No autonomous testing or third-party access. |
| `personal-companion` | Daily Desk tasks and notes with SQLite persistence, revision-safe edits and backup/restore, plus editable personalization methods. | Calendar sync, hosted reminders and connected services require separate host setup. |
| `garden-companion` | Record observations and review local calendar changes in SQLite. | No external calendar writes or biological diagnosis. |
| `learning-coach` | Build source-based study sessions, score practice and store review history. | No clinical approval or independent mastery assessment. |
| `claims-adjudicator` | Review claims against supplied evidence and record qualifications. | Not an independently authenticated verdict. |
| `reverse-engineering-researcher` | Compare supplied application-observation records. | No live capture, network probing or attack engine. |
| `data-engineering-architect` | Schema evolution, record quality, versioned-event reconciliation and supplied SQLite query-plan analysis. | Production database access or schema migration requires explicit credentials and approval. |
| `infrastructure-reliability-engineer` | Error budgets, capacity estimates, incident timing and reliability calculations on supplied measurements. | Live telemetry and infrastructure changes require authorized provider access. |
| `automation-engineer` | Dependency graphs, approval contracts, locator selection and effect-evidence consistency checks. | Running live adapters or scheduling jobs is a separate host-permitted operation. |
| `product-interface-designer` | Label checks, sRGB contrast calculations and declared interaction-state graph coverage. | Rendered-browser and real usability reviews need actual interface evidence. |

The [Evidence Finder](../services/evidence-finder/) preserves local findings for these tools. It is a shared service, not another assistant.

## Run an example

[Workflows](WORKFLOWS.md) provides the commands and expected results. Start with `examples/research_evaluator_demo.py` for quotation checks, `examples/numeric_evaluation_demo.py` for scoring, or `examples/software_engineer_workflow_demo.py` for a disposable repair exercise.

The `research-numeric` result `LOCAL_NUMERIC_HELDOUT_EVALUATED` means the supplied data passed the numerical checks. It does not prove the truth of a scientific hypothesis. The [capability catalog](../presets/capabilities.json) connects declared features to their modules and examples.

For the four newer roles, run `PYTHONPATH=src python3 -B examples/specialist_engine_demo.py --role automation-engineer` from the source checkout, substituting one of the four role IDs above. On PowerShell, set `$env:PYTHONPATH = "src"` and use `python`. The demo processes a fictional fixture and returns explicit offline-only evidence. Skill text alone does not execute these engines.

## Requirements and permissions

Use Python 3.12+. Git is required for repository workflows; individual packages document other prerequisites. Core tools support Windows, macOS and Linux, with platform-specific limitations. Swift typechecking needs an installed Swift toolchain on macOS.

Reviewed code executes under your OS account and can access its files and network. Explicit execution consent is **not a sandbox**. Local handoff, plan and restart utilities do not authenticate another account or authorize an external action.

These are source-only distributions: runnable code and editable profiles, not a hosted service or installed native assistants. [Host compatibility](HOST_COMPATIBILITY.md) explains the separate integration checks.

## Standalone offline packages

| Package | Guide |
| --- | --- |
| Creative Studio | [Build, verify and run](kits/CREATIVE_SOURCEKIT.md) |
| Claims Adjudicator | [Build, verify and run](kits/CLAIMS_SOURCEKIT.md) |
| Garden Companion | [Build, verify and run](kits/GARDEN_SOURCEKIT.md) |
| Learning Coach | [Build, verify and run](kits/LEARNING_SOURCEKIT.md) |
| Reverse Engineering & Security Researcher | [Build, verify and run](kits/REVERSE_SOURCEKIT.md) |
| Coordinator, Software Engineer and Model Builder | [Runnable workflows](WORKFLOWS.md) |

[Get started](GITHUB_QUICKSTART.md) · [Downloads](RELEASES.md) · [Security](SECURITY.md)

## Richer task collection, without replacing the original fixtures

The [75-skill collection](collection/MUSE_CURATED_COLLECTION.md) reuses eleven bounded local implementations across four standalone toolkits. `python -B tools/muse_collection.py demo data-engineer` runs logical schema comparison, versioned-event reconciliation and supplied-query-plan classification. The other toolkit IDs are `reliability-engineer`, `automation-engineer` and `product-interface-designer`; their actual operations and limits are in the [specialist quickstart](collection/SPECIALIST_QUICKSTART.md).

These tools complement the simpler source fixtures above; they do not rename existing public role IDs or establish native integration. Five workflow demos run only their local registered stages and explicitly report the remaining host/human handoffs. A 100-starter bundle selects instructions rather than creating agents. Existing tagged release assets remain unchanged.

## Daily Desk local workbench

[Daily Desk](spaces/DAILY_DESK.md) joins task and note editors to the existing local companion storage and loopback server. The disposable `python -B examples/daily_desk.py` demo verifies three tasks/two notes, editing, reopening, stale-revision refusal and checked restoration into a new store. `--serve` opens the local browser application explicitly. Operation receipts, scoped access and no-overwrite restore are local mechanisms; no native Muse Space, model, scheduler or cloud sync is installed.
