# Choose a Muse assistant

Muse Hub has **15 independent assistants**. Choose one Muse assistant for one kind of work. Each gets its own Main, three subchats, documents, and private memory scope—not 15 roles inside one account.

**Current published release:** [v1.0.0 source toolkit](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.0.0) or [latest published release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/latest).
**Individual assistant ZIPs:** the 15 v1.1.0 ZIPs are currently staged as a **draft**, not public downloads. The links below become usable when the release is published.

## Choose by job

### Build and automate

- **[Software Engineer](../presets/software-engineer/INSTALL.md)** — Reproduce a software defect and verify the fix. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-software-engineer-v1.1.0.zip).
- **[Data Engineering & Database Architect](../presets/data-engineering-architect/INSTALL.md)** — Profile data, check schemas, and plan safe migrations. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-data-engineer-v1.1.0.zip).
- **[Automation Engineer](../presets/automation-engineer/INSTALL.md)** — Build bounded workflows with approval and recovery gates. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-automation-engineer-v1.1.0.zip).
- **[Infrastructure & Reliability Engineer](../presets/infrastructure-reliability-engineer/INSTALL.md)** — Diagnose service failures and plan verifiable recovery. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-reliability-engineer-v1.1.0.zip).

### Research and review

- **[Research Evaluator](../presets/research-evaluator/INSTALL.md)** — Compare research claims against original sources and numerical evidence. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-research-evaluator-v1.1.0.zip).
- **[Claims Adjudicator](../presets/claims-adjudicator/INSTALL.md)** — Check competing claims and document the basis of a verdict. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-claims-adjudicator-v1.1.0.zip).
- **[Adversarial Verifier](../presets/adversarial-verifier/INSTALL.md)** — Challenge authorized releases with negative controls and reproducible evidence. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-adversarial-verifier-v1.1.0.zip).
- **[Reverse Engineering & Security Researcher](../presets/reverse-engineering-researcher/INSTALL.md)** — Study authorized application behavior and suspicious messages. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-reverse-engineering-researcher-v1.1.0.zip).

### Create and learn

- **[Creative Studio](../presets/creative-studio/INSTALL.md)** — Plan visual work from concept to verified production handoff. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-creative-studio-v1.1.0.zip).
- **[Product & Interface Designer](../presets/product-interface-designer/INSTALL.md)** — Design and review user journeys, interfaces, states, and accessibility. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-product-interface-designer-v1.1.0.zip).
- **[Model Builder](../presets/model-builder/INSTALL.md)** — Plan model training, artifact inspection, and evaluation. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-model-builder-v1.1.0.zip).
- **[Learning Coach](../presets/learning-coach/INSTALL.md)** — Turn source material into targeted study and review. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-learning-coach-v1.1.0.zip).

### Life and planning

- **[Personal Companion](../presets/personal-companion/INSTALL.md)** — Organize tasks, notes, preferences, and routines privately. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-personal-companion-v1.1.0.zip).
- **[Garden Companion](../presets/garden-companion/INSTALL.md)** — Track plants, observations, seasons, and care. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-garden-companion-v1.1.0.zip).
- **[Coordinator](../presets/coordinator/INSTALL.md)** — Organize a project across people and independent assistant workflows. [Individual ZIP (v1.1.0 draft)](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/muse-coordinator-v1.1.0.zip).

## Set up one assistant

1. Choose your role and read its INSTALL.md.
2. After v1.1.0 is published, download the individual ZIP and verify it with the [release checksums](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/SHA256SUMS.txt).
3. Use the Main files to configure a **separate Muse assistant**.
4. Create its three subchats **inside that assistant**, using their own instructions and memory templates.
5. Ask the first example question in the role guide. Optional local tools require separate setup and permissions.

**No Python is needed for configuring the assistant.** Optional Python engines are a different workflow. The ZIP does not log in to Muse, install native tools, contact other assistants, or connect accounts.

If v1.1.0 is still a draft, the public alternative is the [v1.0.0 source toolkit](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.0.0); its older source-install process is described in [the developer guide](GITHUB_QUICKSTART.md). Do not treat the older collection as the new complete per-assistant ZIP.

[Muse Hub overview](../hub/README.md) · [Current capability guide](CAPABILITIES.md) · [All release versions](RELEASES.md)
