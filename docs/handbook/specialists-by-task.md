# Specialists by task

Pick the specialist closest to your task. Each entry explains its scope, the tools included with the toolkit and a concrete starting point.

[Download an assistant](../DOWNLOAD_A_SPECIALIST.md) · [Get started](../GETTING_STARTED.md) · [Methods and tools](../collection/SPECIALIST_SCOPE_AND_ENGINES.md) · [Task starters](../../collections/muse-starters-v1/CATALOG.md)

### Build and automate

- **[Software Engineer](../../presets/software-engineer/README.md)** (`software-engineer`) — Build, debug, refactor and release software. Work from reproduction and architecture decisions through implementation, regression tests, source integrity and reviewed delivery. [Role contract](../../presets/software-engineer/playbook.json).
  **Included tools:** [Engineering sourcekit](../../src/muse_presets/engineer_sourcekit.py) and [Claim Gate](../../presets/software-engineer/runtime/claim-gate/ENGINE.json). Engineering tools run focused repair and test workflows. Claim Gate supports admission and recovery; the linked technical records describe the evidence tools.
  [Example or exporter](../../examples/software_engineer_workflow_demo.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Data Engineering & Database Architect](../../presets/data-engineering-architect/README.md)** (`data-engineering-architect`) — Design and maintain reliable data systems, from schemas and ingestion quality to record identity, event reconciliation, query performance and safe migrations. [Role contract](../../presets/data-engineering-architect/playbook.json).
  **Included tools:** [Data extension](../../src/muse_presets/specialist_extensions/data.py) and [Role engine](../../src/muse_presets/specialist_engines.py). The data extension reviews schema contracts, versioned events and supplied query plans; the role engine checks key identity, duplicates and nulls.
  [Example or exporter](../../examples/specialist_engine_demo.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Automation Engineer](../../presets/automation-engineer/README.md)** (`automation-engineer`) — Build repeatable workflows across tools and services, with dependency graphs, triggers, approval points, idempotency, retry policy and uncertain-effect recovery. [Role contract](../../presets/automation-engineer/playbook.json).
  **Included tools:** [Automation extension](../../src/muse_presets/specialist_extensions/automation.py) and [Dependency engine](../../src/muse_presets/specialist_engines.py). The automation extension validates approvals, locator evidence and effect records; the role engine checks graph validity and ordering. Live actions use host-authorized connectors.
  [Example or exporter](../../examples/specialist_engine_demo.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Infrastructure & Reliability Engineer](../../presets/infrastructure-reliability-engineer/README.md)** (`infrastructure-reliability-engineer`) — Improve service reliability using SLOs, error budgets, capacity forecasts, incident investigation, recovery plans and evidence from real measurements. [Role contract](../../presets/infrastructure-reliability-engineer/playbook.json).
  **Included tools:** [Reliability extension](../../src/muse_presets/specialist_extensions/reliability.py) and [Reliability engine](../../src/muse_presets/specialist_engines.py). The reliability extension calculates capacity and incident timing; the role engine computes error-budget consumption from supplied metrics.
  [Example or exporter](../../examples/specialist_engine_demo.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

### Research and evaluate

- **[Research Evaluator](../../presets/research-evaluator/README.md)** (`research-evaluator`) — Investigate scientific and technical questions, compare explanations, audit primary evidence and design controlled, held-out evaluations. [Role contract](../../presets/research-evaluator/playbook.json).
  **Included tools:** [Research engine](../../src/muse_presets/research_evaluator.py) and [Numerical evaluation](../../src/muse_presets/numeric_evaluation.py). The research engine validates quotations and source separation; numerical evaluation scores supplied predictions and checks group leakage.
  [Example or exporter](../../examples/research_evaluator_demo.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Claims Adjudicator](../../presets/claims-adjudicator/README.md)** (`claims-adjudicator`) — Resolve competing factual and technical claims by tracing original evidence, testing counterexamples, qualifying uncertainty and recording defensible conclusions. [Role contract](../../presets/claims-adjudicator/playbook.json).
  **Included tools:** [Claims engine](../../src/muse_presets/claims.py) and [Claims sourcekit](../../src/muse_presets/claims_sourcekit.py). The claims engine and portable sourcekit produce source-bound findings with reproducible evidence and limitations.
  [Example or exporter](../../examples/export_claims_sourcekit.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Adversarial Verifier](../../presets/adversarial-verifier/README.md)** (`adversarial-verifier`) — Challenge authorized software, agent systems and releases with threat models, failure injection, negative controls and independent remediation reviews. [Role contract](../../presets/adversarial-verifier/playbook.json).
  **Included methods:** Use the defensive testing playbook and editable review methods with the tools available for your authorized target.
  [Set up the workroom](../../presets/adversarial-verifier/INSTALL.md) · [Full scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Reverse Engineering & Security Researcher](../../presets/reverse-engineering-researcher/README.md)** (`reverse-engineering-researcher`) — Understand software and protocol behavior with authorized observations, defensive trace analysis, scoped experiments and clean-room reconstructions. [Role contract](../../presets/reverse-engineering-researcher/playbook.json).
  **Included tools:** [Reverse-analysis engine](../../src/muse_presets/reverse.py) and [Reverse sourcekit](../../src/muse_presets/reverse_sourcekit.py). The reverse-analysis tools compare supplied observations and help test explanations of application behavior.
  [Example or exporter](../../examples/export_reverse_sourcekit.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

### Create and learn

- **[Creative Studio](../../presets/creative-studio/README.md)** (`creative-studio`) — Develop original visual media, animation, video and interactive scenes—from creative direction, characters, environments and asset development to motion, render inspection, continuity and delivery. [Role contract](../../presets/creative-studio/playbook.json).
  **Included tools:** [Creative-production engine](../../src/muse_presets/creative_production.py) and [Creative sourcekit](../../src/muse_presets/creative_sourcekit.py). The production planner compiles briefs, dependencies, shots, timelines, continuity checks, and textual storyboards. Use your chosen render tools to create and inspect the media.
  [Example or exporter](../../examples/creative_studio_demo.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Product & Interface Designer](../../presets/product-interface-designer/README.md)** (`product-interface-designer`) — Design and evaluate complete product experiences: user research, information architecture, responsive layouts, interaction flows, accessibility and build-ready handoffs. [Role contract](../../presets/product-interface-designer/playbook.json).
  **Included tools:** [Interface extension](../../src/muse_presets/specialist_extensions/interface.py) and [Role engine](../../src/muse_presets/specialist_engines.py). The interface extension tests color contrast and declared interaction states; the role engine reviews labels in supplied screen definitions.
  [Example or exporter](../../examples/specialist_engine_demo.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Model Builder](../../presets/model-builder/README.md)** (`model-builder`) — Design datasets, models and adapters, conduct training experiments, compare candidates on held-out data and preserve model, tokenizer and artifact provenance. [Role contract](../../presets/model-builder/playbook.json).
  **Included tools:** [Model-building sourcekit](../../src/muse_presets/model_builder_sourcekit.py) and [Toy-model training engine](../../src/muse_presets/model_toy_bundle.py). The model sourcekit performs bounded local model training, mathematical checks and evaluations; larger GPU training requires a separate host.
  [Example or exporter](../../examples/export_model_builder_sourcekit.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Learning Coach](../../presets/learning-coach/README.md)** (`learning-coach`) — Build lessons, flashcards, practice sessions, scored quizzes and adaptive review from trusted study material, keeping learner progress and weak areas visible. [Role contract](../../presets/learning-coach/playbook.json).
  **Included tools:** [Learning engine](../../src/muse_presets/learning.py) and [Session store](../../src/muse_presets/learning_session.py). The learning engine, session store and portable sourcekit provide local scoring, study history and repeatable practice.
  [Example or exporter](../../examples/learning_session_demo.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

### Life and planning

- **[Personal Companion](../../presets/personal-companion/README.md)** (`personal-companion`) — Support daily life with personal planning, routines, accessible interactions and privacy-aware assistance shaped to the owner's preferences. [Role contract](../../presets/personal-companion/playbook.json).
  **Included tools:** [Daily Desk workbench](../../src/muse_presets/daily_desk.py) and [Companion storage](../../src/muse_presets/personal_companion.py). Daily Desk is a working local SQLite workbench for task and note editing, revision conflicts, persistence, export and restore. Connected calendars and reminders use host-authorized services.
  [Example or exporter](../../examples/daily_desk.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Garden Companion](../../presets/garden-companion/README.md)** (`garden-companion`) — Organize plants, growing seasons and gardening projects through observations, evidence-aware care guidance, planting plans and owner-managed schedules. [Role contract](../../presets/garden-companion/playbook.json).
  **Included tools:** [Garden records engine](../../src/muse_presets/garden.py) and [Garden calendar](../../src/muse_presets/garden_calendar.py). The garden engine, local calendar and sourcekit retain versioned observations and care schedules without silently changing external calendars.
  [Example or exporter](../../examples/garden_calendar_demo.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Coordinator](../../presets/coordinator/README.md)** (`coordinator`) — Turn complex goals into scoped work across specialists: sequence dependencies, manage owner approvals and resources, recover interrupted work and verify handoffs. [Role contract](../../presets/coordinator/playbook.json).
  **Included tools:** [Coordinator sourcekit](../../src/muse_presets/coordinator_sourcekit.py) and [Review engine](../../src/muse_presets/coordinator_review.py). The coordinator tools review plans, dependencies, evidence, and handoffs so the next step is clear.
  [Example or exporter](../../examples/export_coordinator_sourcekit.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

## Start your task

Download the selected specialist, open its START_HERE.md, and bring your task and source material. Choose additional tools or service connections when the work needs them.

The [specialist catalog](../collection/SPECIALIST_CATALOG.md) links all 15 roles to their methods and examples. The toolkit aliases `data-engineer` and `reliability-engineer` are the short command names for their corresponding specialists.

For terminal commands and tool requirements, use the [terminal guide](../TERMINAL.md).

For package contents, see [downloads](../RELEASES.md) and the [tools guide](../CAPABILITIES.md).
