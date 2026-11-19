# Specialists and their working engines

Each profile has field-specific methods and skills. Some also ship executable Python engines or a local application. Use the role for the wider workflow; use an included engine when you need a reproducible local operation.

The descriptions below cover each role's methods and included software. Muse can also use separately authorized host tools for rendering, development, research or connected services.

[15 role profiles](../../presets/catalog.json) · [558 task starters](../../collections/muse-starters-v1/CATALOG.md) · [Run an example](SPECIALIST_QUICKSTART.md) · [Machine-readable engine index](../discovery/specialist-engine-index.json)

## Build and automate

### Software Engineer

Handles the software lifecycle: design decisions, debugging, implementation, refactoring, test coverage, code review and release checks. Its playbook begins with reproducible failures and retains source and verification evidence through handoff.

**Included tools:** The [engineering sourcekit](../../src/muse_presets/engineer_sourcekit.py) and [engineering pack](../../src/muse_presets/engineering_pack.py) run bounded source, patch and test workflows. The [Claim Gate runtime](../../presets/software-engineer/runtime/claim-gate/ENGINE.json) adds admission and recovery checks. [Iron Ledger](../../presets/software-engineer/runtime/iron-ledger/ENGINE.json) and [Provenance Vault](../../presets/software-engineer/runtime/provenance-vault/ENGINE.json) have source-integrated, evidence-only consumer candidates; their technical records describe the integration requirements.

[Software Engineer methods](../../presets/software-engineer/playbook.json) · [Run a software repair example](../../examples/software_engineer_workflow_demo.py)

### Data Engineering & Database Architect

Works on data modeling, schema evolution, storage and query design, ingestion quality, record identity, incremental pipelines and migration safety.

**Included tools:** The [data extension](../../src/muse_presets/specialist_extensions/data.py) executes schema-contract comparisons, versioned-event reconciliation and supplied query-plan classification. The [role engine](../../src/muse_presets/specialist_engines.py) also checks keys, duplicates, nulls and declared rows.

[Data Engineer methods](../../presets/data-engineering-architect/playbook.json) · [Run the complete local toolkit](SPECIALIST_QUICKSTART.md#run-a-specialist-locally)

### Automation Engineer

Designs workflows that have dependencies, approvals, retries and external side effects. It helps turn repeatable work into explicit graphs and verifiable execution contracts.

**Included tools:** The [automation extension](../../src/muse_presets/specialist_extensions/automation.py) checks dependency declarations, approvals, locator observations and effect-evidence consistency. The [role engine](../../src/muse_presets/specialist_engines.py) validates and orders dependency graphs. Real scheduling and service actions require host connections and the user's permission.

[Automation methods](../../presets/automation-engineer/playbook.json) · [Run a workflow check](SPECIALIST_QUICKSTART.md#run-a-specialist-locally)

### Infrastructure & Reliability Engineer

Assesses service reliability, SLOs, error budgets, capacity, incident response and recovery evidence. The role uses observed service data when an authorized monitoring source is available.

**Included tools:** The [reliability extension](../../src/muse_presets/specialist_extensions/reliability.py) calculates capacity and analyzes incident timing; the [role engine](../../src/muse_presets/specialist_engines.py) computes error-budget use from supplied event records. Use those reports when planning infrastructure changes.

[Infrastructure methods](../../presets/infrastructure-reliability-engineer/playbook.json) · [Run local reliability calculations](SPECIALIST_QUICKSTART.md#run-a-specialist-locally)

## Research, investigation and evaluation

### Research Evaluator

Builds research questions, checks primary sources, designs independent experiments, evaluates model claims and compares competing explanations. Source custody, controls and disjoint evaluation data are part of the method—not optional closing remarks.

**Included tools:** The [research evaluator](../../src/muse_presets/research_evaluator.py) verifies quotations and source-family separation. [Numerical evaluation](../../src/muse_presets/numeric_evaluation.py) scores supplied predictions and checks group leakage.

[Research methods](../../presets/research-evaluator/playbook.json) · [Quotation and evaluation example](../../examples/research_evaluator_demo.py)

### Claims Adjudicator

Investigates claims about results, correctness, quality, safety and completion. It establishes what was observed, how evidence supports the claim and what remains uncertain. Corrections and changing evidence stay attached to the conclusion.

**Included tools:** The [claims engine](../../src/muse_presets/claims.py) and [portable sourcekit](../../src/muse_presets/claims_sourcekit.py) support source-bound claim reviews and reproducible evidence records.

[Claims methods](../../presets/claims-adjudicator/playbook.json) · [Build the claims sourcekit](../../examples/export_claims_sourcekit.py)

### Adversarial Verifier

Performs authorized, defensive testing of software, services and AI systems. The specialist develops threat models, tests failure and permission boundaries, checks negative controls and evaluates whether remediation actually fixes the problem.

**Included tools:** The public specialist provides a detailed [testing playbook](../../presets/adversarial-verifier/playbook.json) and editable review configuration. Use the testing tools available for your authorized targets.

[Adversarial Verifier profile](../../presets/adversarial-verifier/README.md) · [Set up the workroom](../../presets/adversarial-verifier/INSTALL.md)

### Reverse Engineering & Security Researcher

Investigates application behavior, protocol traces, device/software observations and defensive samples under authorized scope. It can develop clean-room reconstructions and compare hypotheses using recorded behavior and controlled experiments.

**Included tools:** The [reverse-analysis engine](../../src/muse_presets/reverse.py) and [sourcekit](../../src/muse_presets/reverse_sourcekit.py) compare supplied application observations. Use your authorized capture tools to collect additional observations for analysis.

[Reverse Engineering methods](../../presets/reverse-engineering-researcher/playbook.json) · [Build the observation sourcekit](../../examples/export_reverse_sourcekit.py)

## Creative work, products and learning

### Creative Studio

Develops original visual work across images, animation, video and interactive scenes. It handles creative direction, visual references, characters and assets, shot and motion planning, scene continuity, actual render review and production handoff.

**Included tools:** The [creative-production engine](../../src/muse_presets/creative_production.py) compiles briefs into asset dependencies, shot plans, timeline and continuity records, and a textual storyboard. It also verifies and compares those production artifacts. Use your chosen renderer or design environment to create and inspect images, animation, and video.

[Creative Studio scope](CREATIVE_STUDIO_SCOPE.md) · [Creative methods](../../presets/creative-studio/playbook.json) · [Try the production planner](../../examples/creative_studio_demo.py)

### Product & Interface Designer

Works on product design, information architecture, user research, layouts, interaction states, responsive behavior, accessibility and developer handoff.

**Included tools:** The [interface extension](../../src/muse_presets/specialist_extensions/interface.py) evaluates color contrast and declared interaction-state coverage. The [role engine](../../src/muse_presets/specialist_engines.py) checks control labels in supplied screen definitions. Review of an actual design or implementation uses its rendered UI, not only its source.

[Design methods](../../presets/product-interface-designer/playbook.json) · [Run the interface toolkit](SPECIALIST_QUICKSTART.md#run-a-specialist-locally)

### Model Builder

Plans datasets, model architectures, adapters and training experiments, then trains, compares and validates candidates against held-out data. The role tracks model, tokenizer, data rights, artifacts and evaluator provenance.

**Included tools:** The [model-building sourcekit](../../src/muse_presets/model_builder_sourcekit.py), [toy-model training bundle](../../src/muse_presets/model_toy_bundle.py), [model mathematics](../../src/muse_presets/model_toy_math.py) and [evaluation module](../../src/muse_presets/model_eval.py) provide actual bounded local training, scoring and artifact checks. Use a suitable training host and GPU for larger experiments.

[Model Builder methods](../../presets/model-builder/playbook.json) · [Export the training sourcekit](../../examples/export_model_builder_sourcekit.py)

### Learning Coach

Turns trusted study material into lessons, flashcards, retrieval practice, scored quizzes and adaptive follow-up. It preserves source references, learner progress and misunderstandings rather than only generating new questions.

**Included tools:** The [learning engine](../../src/muse_presets/learning.py), [session store](../../src/muse_presets/learning_session.py) and [sourcekit](../../src/muse_presets/learning_sourcekit.py) support local sessions, scoring and review history.

[Learning methods](../../presets/learning-coach/playbook.json) · [Run a study session](../../examples/learning_session_demo.py)

## Life and coordinating work

### Personal Companion

Supports personal organization and everyday decisions with user preferences, routines, accessible interactions and consent-aware assistance. Your own memory, identity and accounts remain separate from generic starter material.

**Included tools:** [Daily Desk](../../src/muse_presets/daily_desk.py) is a working local task-and-note application built on [Personal Companion storage](../../src/muse_presets/personal_companion.py) and the [Space Companion interface](../../src/muse_presets/space_companion.py). It supports revision-checked editing, persistence, backup and create-only restoration.

[Personal Companion methods](../../presets/personal-companion/playbook.json) · [Run Daily Desk](../../examples/daily_desk.py) · [Application guide](../spaces/DAILY_DESK.md)

### Garden Companion

Keeps plant observations, garden records and seasonal care plans organized. Its playbook separates observed symptoms from inferred plant health and can help plan owner-approved care routines.

**Included tools:** [Garden records](../../src/muse_presets/garden.py), [local calendar logic](../../src/muse_presets/garden_calendar.py) and the [garden sourcekit](../../src/muse_presets/garden_sourcekit.py) provide versioned observations and local schedule review.

[Garden methods](../../presets/garden-companion/playbook.json) · [Run the calendar example](../../examples/garden_calendar_demo.py)

### Coordinator

Manages work spanning multiple specialists or tools. It sets scope, dependencies, owners and success criteria, records handoffs and reconciles interrupted operations before a retry.

**Included tools:** The [coordinator sourcekit](../../src/muse_presets/coordinator_sourcekit.py), [review methods](../../src/muse_presets/coordinator_review.py) and [drop-in implementation](../../src/muse_presets/coordinator_dropin.py) provide local planning, evidence review and handoff checks.

[Coordinator methods](../../presets/coordinator/playbook.json) · [Export the coordinator kit](../../examples/export_coordinator_sourcekit.py)

## Choosing a specialist or an engine

Use a **specialist** when you want reasoning and workflows across the full field. Use an **included engine** when you need a reproducible local operation. When connecting a model, browser, rendering program, database, code editor or other service, use the receiving host's own tool registrations and approvals.

The toolkit includes portable Python programs, research and model evaluation tools, and Personal Companion's Daily Desk and Companion Home. See the [tools guide](../CAPABILITIES.md) for examples and setup.

**The [engine index](../discovery/specialist-engine-index.json)** is the machine-readable reference for the fifteen role IDs, public engine paths, first-use examples and delivery types. Its paths can be verified against source.