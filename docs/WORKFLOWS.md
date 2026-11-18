# Workflows you can use

Bring a goal, the relevant files, and a result to check. The [25-workflow collection](collection/MUSE_CURATED_COLLECTION.md) connects specialist methods for engineering, research, data, design, and planning. The commands below run worked examples from the toolkit.

## Run the examples

Use Python 3.12+ from the repository root. Engineering workflows also need Git. For these lower-level examples:

- **macOS/Linux:** use `PYTHONPATH=src python3 -B`.
- **Windows PowerShell:** set `$env:PYTHONPATH = "src"`, then use `python -B`.

Examples supply their own sample data. For personal Muse chat and the simpler toolkit commands, see [Terminal](TERMINAL.md).

## Engineering: reproduce, repair, review

```sh
PYTHONPATH=src python3 -B examples/software_engineer_workflow_demo.py
```

This creates a temporary Git repository, reproduces a failing assertion, applies a focused repair, and runs the passing tests. Add `--to /absolute/new-candidate-folder` to keep the candidate, then use [Family Link](FAMILY_LINK.md) to prepare an independent review. The [build and automate guide](journeys/BUILD_AND_AUTOMATE.md) walks through both steps. Run reviewed code in a workspace you control; local programs use your operating-system permissions.

## Research quotations and evaluation

```sh
PYTHONPATH=src python3 -B examples/research_evaluator_demo.py
PYTHONPATH=src python3 -B examples/numeric_evaluation_demo.py
```

The first checks quoted bytes and locations against supplied source text. The second calculates prediction metrics and checks group separation. To process your own reviewed input, follow the example schema:

```sh
PYTHONPATH=src python3 -B -m muse_presets.cli research-trace --file /absolute/case.json
PYTHONPATH=src python3 -B -m muse_presets.cli research-numeric --file /absolute/predictions.json
```

Use the returned checks alongside your interpretation of the original evidence and study design.

## Data, reliability, automation, and interface design

These commands set up their own import path:

```sh
python -B tools/muse_collection.py workflow-demo pipeline-validation
python -B tools/muse_collection.py workflow-demo incident-recovery
python -B tools/muse_collection.py workflow-demo interface-quality
python -B tools/muse_collection.py workflow-demo automation-readiness
python -B tools/muse_collection.py workflow-demo product-to-implementation
```

Each report identifies the calculation or review stages that ran and the remaining handoffs. Use its outputs with your project files and the tools required for the next step. [Specialist tools](collection/SPECIALIST_QUICKSTART.md) documents individual commands and input formats.

## Builder delivery

```sh
PYTHONPATH=src python3 -B examples/builder_delivery_demo.py
PYTHONPATH=src python3 -B -m muse_presets.cli builder-plan --help
PYTHONPATH=src python3 -B -m muse_presets.cli builder-stage --help
PYTHONPATH=src python3 -B -m muse_presets.cli builder-run --help
```

Staging uses `--allow-disposable-stage`; running reviewed code uses `--allow-reviewed-execution`. Choose a new output folder. The example runs a Python test and, on macOS with Swift installed, typechecks a Swift file. Use your project's build and signing process for an application release.

## Save and resume work

```sh
PYTHONPATH=src python3 -B examples/continuum_checkpoint_demo.py
PYTHONPATH=src python3 -B examples/family_offline_handoff_demo.py
PYTHONPATH=src python3 -B examples/omnium_plan_only_demo.py
```

The checkpoint example saves and reopens a work record in a separate process. Family Link prepares and reviews handoff records. The plan example checks dependencies and identifies required workers. See [Family Link](FAMILY_LINK.md) to carry the reviewed handoff into your chosen communication route.

## Garden, study, and notes

```sh
PYTHONPATH=src python3 -B examples/garden_calendar_demo.py
PYTHONPATH=src python3 -B examples/learning_session_demo.py
python -B examples/daily_desk.py
```

These examples exercise saved records, revisions, and recovery. Continue with [Garden calendar](GARDEN_LOCAL_CALENDAR.md), [Learning sessions](LEARNING_LOCAL_STUDY.md), or [Daily Desk](spaces/DAILY_DESK.md).

## Export a portable tool

Choose a new absolute ZIP destination:

```sh
PYTHONPATH=src python3 -B examples/export_coordinator_sourcekit.py --to /absolute/coordinator.zip
PYTHONPATH=src python3 -B examples/export_software_engineer_sourcekit.py --to /absolute/software-engineer.zip
PYTHONPATH=src python3 -B examples/export_model_builder_sourcekit.py --to /absolute/model-builder.zip
PYTHONPATH=src python3 -B examples/export_creative_sourcekit.py --to "$HOME/creative-studio.zip"
```

Each export includes a start guide, examples, and integrity information. Creative Studio's runner creates a production plan, shot-list CSV, and textual HTML storyboard; its [tool guide](kits/CREATIVE_SOURCEKIT.md) covers the exact commands. Use the package's own guide after extraction.

[Skills](SKILLS.md) · [Tools](CAPABILITIES.md) · [Terminal](TERMINAL.md)
