# Choose a specialist

Pick the role closest to your task. Each specialist has methods and examples, and several include runnable Python tools. [Capabilities](../CAPABILITIES.md) describes what executes now.

For a ready-made task, choose from [100 starter configurations](../../collections/muse-starters-v1/CATALOG.md). To run a program, use the [specialist quickstart](SPECIALIST_QUICKSTART.md).

## All 15 specialists

Choose a role to open its full instructions. Each entry links to the original role contract and a working example or setup guide.

### Build and automate

- **[Software Engineer](../../presets/software-engineer/README.md)** (`software-engineer`) ? Reproduces defects, implements maintainable repairs and tests exact source. [Role contract](../../presets/software-engineer/preset.json) ? Example: [examples/software_engineer_workflow_demo.py](../../examples/software_engineer_workflow_demo.py)
- **[Data Engineering & Database Architect](../../presets/data-engineer/COLLECTION_README.md)** (`data-engineering-architect`; CLI: `data-engineer`) ? Design safe data contracts, reconcile incremental records and review query access paths with reproducible offline tools. [Role contract](../../presets/data-engineer/specialist.json) ? Run `python tools/muse_collection.py demo data-engineer`
- **[Automation Engineer](../../presets/automation-engineer/COLLECTION_README.md)** (`automation-engineer`) ? Prepare bounded application workflows, review target observations and reconcile uncertain effects through the existing host authority. [Role contract](../../presets/automation-engineer/specialist.json) ? Run `python tools/muse_collection.py demo automation-engineer`
- **[Infrastructure & Reliability Engineer](../../presets/reliability-engineer/COLLECTION_README.md)** (`infrastructure-reliability-engineer`; CLI: `reliability-engineer`) ? Turn service measurements into explicit error budgets, capacity estimates and incident timelines without changing infrastructure. [Role contract](../../presets/reliability-engineer/specialist.json) ? Run `python tools/muse_collection.py demo reliability-engineer`

### Research and evaluate

- **[Research & Evaluation Scientist](../../presets/research-evaluator/README.md)** (`research-evaluator`) ? Runs independent research, held-out experiments and model evaluations. [Role contract](../../presets/research-evaluator/preset.json) ? Example: [examples/research_evaluator_demo.py](../../examples/research_evaluator_demo.py)
- **[Claims Adjudicator](../../presets/claims-adjudicator/README.md)** (`claims-adjudicator`) ? Judges claims against exact evidence and preserves limiting conditions. [Role contract](../../presets/claims-adjudicator/preset.json) ? Example: [examples/export_claims_sourcekit.py](../../examples/export_claims_sourcekit.py)
- **[Adversarial Verifier](../../presets/adversarial-verifier/README.md)** (`adversarial-verifier`) ? Challenges source, security boundaries, tests and failure recovery. [Role contract](../../presets/adversarial-verifier/preset.json) ? Example: [Public profile setup](../../presets/adversarial-verifier/INSTALL.md)
- **[Reverse Engineering & Security Researcher](../../presets/reverse-engineering-researcher/README.md)** (`reverse-engineering-researcher`) ? Authorized supplied-observation and protocol review; no new live security adapter is included in this collection. [Original role contract](../../presets/reverse-engineering-researcher/preset.json) ? Example: [Existing source-kit guide](../../presets/reverse-engineering-researcher/INSTALL.md)

### Create and learn

- **[Creative Studio](../../presets/creative-studio/README.md)** (`creative-studio`) ? Builds source-backed creative artifacts and verifies real rendered output. [Role contract](../../presets/creative-studio/preset.json) ? Example: [examples/creative_studio_demo.py](../../examples/creative_studio_demo.py)
- **[Product & Interface Designer](../../presets/product-interface-designer/COLLECTION_README.md)** (`product-interface-designer`) ? Specify coherent interface states and measure real design-token contrast before handing off implementation and rendered-product review. [Role contract](../../presets/product-interface-designer/specialist.json) ? Run `python tools/muse_collection.py demo product-interface-designer`
- **[Model Builder](../../presets/model-builder/README.md)** (`model-builder`) ? Plans and executes approved model training, adapter work and candidate provenance. [Role contract](../../presets/model-builder/preset.json) ? Example: [examples/export_model_builder_sourcekit.py](../../examples/export_model_builder_sourcekit.py)
- **[Learning Coach](../../presets/learning-coach/README.md)** (`learning-coach`) ? Runs source-grounded, adaptive study and evidence-based learning reviews. [Role contract](../../presets/learning-coach/preset.json) ? Example: [examples/learning_session_demo.py](../../examples/learning_session_demo.py)

### Life and planning

- **[Personal Companion](../../presets/personal-companion/README.md)** (`personal-companion`) ? Helps with daily planning, safe wellness information and enjoyable experiences. [Role contract](../../presets/personal-companion/preset.json) ? Example: [Public profile setup](../../presets/personal-companion/INSTALL.md)
- **[Garden Companion](../../presets/garden-companion/README.md)** (`garden-companion`) ? Supports garden observations, planting plans and owner-approved seasonal schedules. [Role contract](../../presets/garden-companion/preset.json) ? Example: [examples/garden_calendar_demo.py](../../examples/garden_calendar_demo.py)
- **[Coordinator](../../presets/coordinator/README.md)** (`coordinator`) ? Coordinates bounded work, memory, leases and independent acceptance. [Role contract](../../presets/coordinator/preset.json) ? Example: [examples/export_coordinator_sourcekit.py](../../examples/export_coordinator_sourcekit.py)
## Pick the right package

A specialist kit provides an executable capability plus an operational contract. A starter selects relevant skills and workflows for a narrower task. A workflow describes a sequence of outputs and handoffs; it does not create a scheduler or new authority.

The four new kits export with `python tools/muse_collection.py kit SPECIALIST --to ./new-kit.zip` and run independently with `python run.py --demo`. The original eleven specialists retain their established exporters and examples rather than being silently moved into an incompatible packaging protocol.

For the new toolkits, direct calculations are available through `muse_presets.specialist_extensions.evaluate(skill_id, inputs)`. Integrations remain subject to the existing host, source scope and approval controls.

Start with the [working quickstart](SPECIALIST_QUICKSTART.md), browse [all skills](../../collections/muse-starters-v1/SKILL_INDEX.md), or choose a [task starter](../../collections/muse-starters-v1/CATALOG.md).

The Adversarial Verifier and Personal Companion entries above use the current public profile routes. Their separate development-only engines are not silently included in this promotion. A role purpose is not a claim that every possible operation is executable.

## Source IDs and compatibility

The current 15-role registry is [catalog.json](../../presets/catalog.json), with collection metadata in [specialists.json](../../collections/muse-starters-v1/specialists.json). The historical eleven-role protocol is retained for compatibility. `data-engineer` maps to `data-engineering-architect`; `reliability-engineer` maps to `infrastructure-reliability-engineer`. These are aliases, not additional specialists.

Role configurations are **not installed** native assistant identities. A receiving host controls actual model and tool access.
