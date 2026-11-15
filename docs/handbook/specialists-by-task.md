# Specialists by task

Pick the specialist closest to your task. Each entry explains its scope, the tools included with the toolkit and a concrete starting point.

[Start here](../v1/START_HERE.md) · [All engines and evidence](../collection/SPECIALIST_SCOPE_AND_ENGINES.md) · [Machine-readable engine index](../discovery/specialist-engine-index.json) · [100 task configurations](../../collections/muse-starters-v1/CATALOG.md)

### Build and automate

- **[Software Engineer](../../presets/software-engineer/README.md)** (`software-engineer`) — Build, debug, refactor and release software. Work from reproduction and architecture decisions through implementation, regression tests, source integrity and reviewed delivery. [Role contract](../../presets/software-engineer/playbook.json).
  **Included tools:** [Engineering sourcekit](../../src/muse_presets/engineer_sourcekit.py) and [Claim Gate](../../presets/software-engineer/runtime/claim-gate/ENGINE.json). The engineering sourcekit runs bounded repair and test workflows. Claim Gate checks admission and recovery; Iron Ledger and Provenance Vault remain evidence-only candidates under separate qualification.
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
  **Included methods:** The public V1 includes a defensive testing playbook and editable review methods. No standalone security-testing engine is bundled with this role.
  [Set up the workroom](../../presets/adversarial-verifier/INSTALL.md) · [Full scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

- **[Reverse Engineering & Security Researcher](../../presets/reverse-engineering-researcher/README.md)** (`reverse-engineering-researcher`) — Understand software and protocol behavior with authorized observations, defensive trace analysis, scoped experiments and clean-room reconstructions. [Role contract](../../presets/reverse-engineering-researcher/playbook.json).
  **Included tools:** [Reverse-analysis engine](../../src/muse_presets/reverse.py) and [Reverse sourcekit](../../src/muse_presets/reverse_sourcekit.py). The reverse-analysis engine and sourcekit compare supplied observations. No live probing or new security-assistance executable is bundled in public V1.
  [Example or exporter](../../examples/export_reverse_sourcekit.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

### Create and learn

- **[Creative Studio](../../presets/creative-studio/README.md)** (`creative-studio`) — Develop original visual media, animation, video and interactive scenes—from creative direction, characters, environments and asset development to motion, render inspection, continuity and delivery. [Role contract](../../presets/creative-studio/playbook.json).
  **Included tools:** [Creative-production engine](../../src/muse_presets/creative_production.py) and [Creative sourcekit](../../src/muse_presets/creative_sourcekit.py). The bundled creative-production engine is a production planner, not an image or video renderer. It compiles briefs, dependencies, shots, timelines, continuity checks and textual storyboards; actual media uses authorized render tools.
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
  **Included tools:** [Coordinator sourcekit](../../src/muse_presets/coordinator_sourcekit.py) and [Review engine](../../src/muse_presets/coordinator_review.py). The coordinator sourcekit, review tools and drop-in implementation provide local plan and evidence checks; there is no built-in live worker dispatch.
  [Example or exporter](../../examples/export_coordinator_sourcekit.py) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)

## Source, engine and connection boundaries

An editable role profile and a built-in executable engine are different things. The source programs above run specific operations on provided inputs; additional tools, browsers, media renderers and service connectors work only when available and authorized in the receiving Muse environment.

The old 11-role compatibility catalog is preserved in [the original source list](../collection/SPECIALIST_CATALOG.md). The current registry has 15 unique roles; aliases such as `data-engineer` and `reliability-engineer` are not extra agents.

The public Adversarial Verifier currently supplies methods and configuration, not a standalone security-testing engine. Reverse Engineering includes supplied-observation analysis. Neither profile is an automatically installed native security agent.

For exact package contents, see the [V1 release](../RELEASES.md) and [capability matrix](../CAPABILITIES.md).
