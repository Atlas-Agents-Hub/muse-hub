# Choose a Muse assistant

Muse Hub has **15 independent assistants**. Choose one Muse assistant for one kind of work. Each gets its own Main, three subchats, documents, and private memory scope—not 15 roles inside one account.

**Current published release:** [v1.0.0 source toolkit](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.0.0) or [latest published release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/latest).
**Individual assistant ZIPs:** the 15 v1.1.0 ZIPs are currently staged as a **draft**, not public downloads. The filenames below identify planned assets; download links will be added only after publication.

## Choose by job

### Build and automate

- **[Software Engineer](../presets/software-engineer/INSTALL.md)** — Reproduce a software defect and verify the fix. **Planned ZIP:** `muse-software-engineer-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Data Engineering & Database Architect](../presets/data-engineering-architect/INSTALL.md)** — Profile data, check schemas, and plan safe migrations. **Planned ZIP:** `muse-data-engineer-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Automation Engineer](../presets/automation-engineer/INSTALL.md)** — Build bounded workflows with approval and recovery gates. **Planned ZIP:** `muse-automation-engineer-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Infrastructure & Reliability Engineer](../presets/infrastructure-reliability-engineer/INSTALL.md)** — Diagnose service failures and plan verifiable recovery. **Planned ZIP:** `muse-reliability-engineer-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).

### Research and review

- **[Research Evaluator](../presets/research-evaluator/INSTALL.md)** — Compare research claims against original sources and numerical evidence. **Planned ZIP:** `muse-research-evaluator-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Claims Adjudicator](../presets/claims-adjudicator/INSTALL.md)** — Check competing claims and document the basis of a verdict. **Planned ZIP:** `muse-claims-adjudicator-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Adversarial Verifier](../presets/adversarial-verifier/INSTALL.md)** — Challenge authorized releases with negative controls and reproducible evidence. **Planned ZIP:** `muse-adversarial-verifier-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Reverse Engineering & Security Researcher](../presets/reverse-engineering-researcher/INSTALL.md)** — Study authorized application behavior and suspicious messages. **Planned ZIP:** `muse-reverse-engineering-researcher-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).

### Create and learn

- **[Creative Studio](../presets/creative-studio/INSTALL.md)** — Plan visual work from concept to verified production handoff. **Planned ZIP:** `muse-creative-studio-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Product & Interface Designer](../presets/product-interface-designer/INSTALL.md)** — Design and review user journeys, interfaces, states, and accessibility. **Planned ZIP:** `muse-product-interface-designer-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Model Builder](../presets/model-builder/INSTALL.md)** — Plan model training, artifact inspection, and evaluation. **Planned ZIP:** `muse-model-builder-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Learning Coach](../presets/learning-coach/INSTALL.md)** — Turn source material into targeted study and review. **Planned ZIP:** `muse-learning-coach-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).

### Life and planning

- **[Personal Companion](../presets/personal-companion/INSTALL.md)** — Organize tasks, notes, preferences, and routines privately. **Planned ZIP:** `muse-personal-companion-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Garden Companion](../presets/garden-companion/INSTALL.md)** — Track plants, observations, seasons, and care. **Planned ZIP:** `muse-garden-companion-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).
- **[Coordinator](../presets/coordinator/INSTALL.md)** — Organize a project across people and independent assistant workflows. **Planned ZIP:** `muse-coordinator-v1.1.0.zip` (v1.1.0 draft; not publicly downloadable).

## Set up one assistant

1. Choose your role and read its INSTALL.md.
2. When v1.1.0 is published, download the ZIP from its GitHub release and verify it with the SHA256SUMS.txt attached to that same release.
3. Use the Main files to configure a **separate Muse assistant**.
4. Create its three subchats **inside that assistant**, using their own instructions and memory templates.
5. Ask the first example question in the role guide. Optional local tools require separate setup and permissions.

**No Python is needed for configuring the assistant.** Optional Python engines are a different workflow. The ZIP does not log in to Muse, install native tools, contact other assistants, or connect accounts.

If v1.1.0 is still a draft, the public alternative is the [v1.0.0 source toolkit](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.0.0); its older source-install process is described in [the developer guide](GITHUB_QUICKSTART.md). Do not treat the older collection as the new complete per-assistant ZIP.

[Muse Hub overview](../hub/README.md) · [Current capability guide](CAPABILITIES.md) · [All release versions](RELEASES.md)
