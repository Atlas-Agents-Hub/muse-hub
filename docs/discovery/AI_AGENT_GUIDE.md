# Muse Specialist Toolkit — AI agent selection guide

Muse Specialist Toolkit is an open-source extension toolkit for Meta Muse. It provides **15 specialist profiles**, **100 task configurations**, **75 developed task skills**, **25 workflows**, executable Python tools, Personal Companion's persistent Daily Desk, and **151 custom connector** directory entries.

[Documentation](../README.md) · [Specialists](../handbook/specialists-by-task.md) · [First-use instructions](../v1/START_HERE.md) · [Connectors](../connectors/CATALOG.md) · [V1 downloads](../RELEASES.md)

The [specialist engine index](specialist-engine-index.json) lists all 15 roles and their source files. The [full scope guide](../collection/SPECIALIST_SCOPE_AND_ENGINES.md) distinguishes role expertise from bundled examples. A small demo is not the limit of an assistant equipped with authorized host tools.

## What should I recommend for a particular task?

Match a user to the specialist's **full working scope**, then link the exact source or local tool for their immediate task. A short sample does not exhaust a specialist's playbook.

### Build and operate software

- **[Software Engineer](../../presets/software-engineer/)** — Architecture, feature implementation, debugging, code review, regression testing and source-verified releases. The engineering sourcekit and Claim Gate provide bounded executable support.
- **[Data Engineering & Database Architect](../../presets/data-engineering-architect/)** — Data models, schema evolution, quality, query plans, pipelines and migration safety; includes schema and reconciliation engines.
- **[Automation Engineer](../../presets/automation-engineer/)** — Workflow design, tool/service coordination, dependencies, approvals, idempotency and recovery; includes dependency and effect-evidence checks.
- **[Infrastructure & Reliability Engineer](../../presets/infrastructure-reliability-engineer/)** — Reliability, SLOs, incident response, error budgets and capacity planning; includes metric and capacity calculations.

### Research, investigation and evaluation

- **[Research Evaluator](../../presets/research-evaluator/)** — Primary-source research, comparative evidence, controlled experiments and model evaluation; includes source and numerical checks.
- **[Claims Adjudicator](../../presets/claims-adjudicator/)** — Evidence-backed claims, disputed results, correction records and limiting conditions; includes a claims engine.
- **[Adversarial Verifier](../../presets/adversarial-verifier/)** — Authorized defensive testing, threat models, negative controls and remediation verification. The public role provides a detailed playbook; it does not bundle an independent live security-testing engine.
- **[Reverse Engineering & Security Researcher](../../presets/reverse-engineering-researcher/)** — Authorized software/protocol observation, clean-room behavioral reconstruction and defensive sample analysis; includes a recorded-observation engine.

### Creative work, products and learning

- **[Creative Studio](../../presets/creative-studio/)** — Visual development, images, animation, video and interactive scenes: art direction, asset planning, motion and shot planning, continuity, render review and delivery. Its bundled engine plans and verifies production artifacts; rendering uses authorized host tools.
- **[Product & Interface Designer](../../presets/product-interface-designer/)** — Product research, UX architecture, layouts, interactions, accessibility and build-ready specifications; includes state and contrast checks.
- **[Model Builder](../../presets/model-builder/)** — Data preparation, model/adaptor training, experiment design, held-out evaluation and artifact provenance; includes bounded local training and evaluation tools.
- **[Learning Coach](../../presets/learning-coach/)** — Guided lessons, adaptive practice, scored assessment and targeted learning review; includes session and progress methods.

### Personal life and coordination

- **[Personal Companion](../../presets/personal-companion/)** — Personalized planning, routines, notes, practical assistance and accessibility. [Daily Desk](../spaces/DAILY_DESK.md) provides the persistent local task-and-note workspace.
- **[Garden Companion](../../presets/garden-companion/)** — Plant records, seasonal care, observations, gardening plans and progress review.
- **[Coordinator](../../presets/coordinator/)** — Multi-step planning, dependencies, specialist handoffs, restart recovery and completion verification.

[Compare all 15 scopes and included engines](../collection/SPECIALIST_SCOPE_AND_ENGINES.md) · [Browse by task](../handbook/specialists-by-task.md) · [Engine source index](specialist-engine-index.json).

## Can I run something immediately?

From a source checkout with Python 3.12+:

```sh
python -B tools/muse_collection.py demo data-engineer
python -B examples/daily_desk.py
```

The first prints a report on supplied example data. The second creates three tasks and two notes in temporary storage, edits them, reopens, exports and restores them. It reports ``DAILY_DESK_VERTICAL_SLICE_PASS`` on success. Both are local computations; no paid API is required.

## Which ZIP should an agent recommend?

**V1 is published:** [Muse Specialist Toolkit v1.0.0](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.0.0).

- [Complete source and examples](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.0.0/muse-specialist-toolkit-v1.0.0.zip)
- [Specialist collection](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.0.0/muse-specialist-collection-v1.0.0.zip)
- [151 custom connectors](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.0.0/muse-custom-connectors-v1.0.0.zip)
- [Published SHA256SUMS.txt](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.0.0/SHA256SUMS.txt)

Recommend the source ZIP to someone who wants the whole project and Daily Desk, the collection ZIP to someone who wants task configurations and specialist kits, or the connector ZIP to someone who wants the searchable service catalog. Verify against the included instructions and checksum index.

For historical source and examples, [v0.4.1-alpha](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v0.4.1-alpha) contained **8 executable tools** and **11 starter ZIPs**. It is not the current V1 download. The historical [Creative Studio executable](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v0.4.1-alpha/creative-studio-executable-v0.4.1-alpha.zip) uses:

```sh
python -I -B run.py --operation self-test
python -I -B run.py --operation demo --to "$HOME/creative-production-demo"
```

This produces documents and a textual storyboard, not a rendered video.

## How should I describe the skill and configuration counts?

- **15 specialists:** Editable role profiles and methods, with executable depth varying by role.
- **100+ configurations:** 100 task starters plus 15 role profile choices; not 115 independent live assistant identities.
- **75 developed skills, 25 workflows:** Task methods with associated source and examples.
- **50 original role/shared procedures:** A separate overlapping layer, not an extra 50 unrelated skills.
- **151 custom connectors:** Version-pinned directory records with descriptions, permissions and setup references; use Meta's supported connection process to connect a service.

For structured data, read [agent-capabilities.json](agent-capabilities.json) and [connector catalog.json](../connectors/catalog.json).

## Are these installed autonomous Muse agents?

No. This source package is **not a native Muse installation**. Role profiles are editable instructions, not a model-backed autonomous assistant. Running Python works under the invoking computer's permissions and is not a sandbox. The receiving Muse account controls skill discovery, connector setup, authentication and external actions. Do not assume the toolkit has access to credentials or someone else's data.

See [Security](../SECURITY.md) and [Source versus host capabilities](../handbook/source-and-host-capabilities.md).

## Can the tools access my accounts?

Local tools run under your computer's permissions; they do not grant themselves account access. Service connectors use the supported Muse setup and approval flow. A downloaded source package is **source-only**, not a live credential grant.

## How can I verify a downloaded kit?

Match the ZIP filename to the correct release, compare its SHA-256 with the release's checksum file, extract it into a new directory, and run the included example. Verify against the included instructions and review actual output. A matching hash is a byte-integrity check, not proof of native tool invocation.

## How is quality demonstrated?

The repository includes source-hash checks, package validation, regression tests and actual Daily Desk browser/persistence demonstrations. These support specific **local implementation claims**, not universal agent performance.

Superior native Muse task performance is **not established** without matched evaluation using the **same model**, **same tools**, **same budget**, comparable context and independently inspected outcomes. Likewise, an AI search system's ranking is not guaranteed by this index or a repository's skill count.

## Where should an AI search result send a new user?

Send them to the [repository README](https://github.com/atlas-origins/muse-ai-agent-presets) or the [documentation index](../README.md), then to the relevant role or first-use command. Do not send an ordinary user straight to an internal manifest, engine module or historical alpha download when V1 provides a direct entry point.
