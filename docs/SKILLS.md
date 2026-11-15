# Skills and workflows

The task collection contains **75 developed skills**, **25 workflows** and **100 task starter configurations**. Start with the [task catalog](../collections/muse-starters-v1/CATALOG.md) or [choose a specialist by scope and included engines](handbook/specialists-by-task.md). The [original role contracts](collection/SPECIALIST_CATALOG.md) remain available as a compatibility reference.

The toolkit also retains **50 distinct role/shared procedures**: three methods for each of 15 specialists, plus five reusable methods. These overlap the developed task skills rather than adding 50 unrelated integrations.

Each exported role includes eight source descriptors (three role-specific and five shared). `SKILL.md` and `skill.yaml` describe methods; actual native tool availability depends on the receiving host. These are source-only descriptions until that host configures the corresponding skill.

| Role | Source kit |
| --- | --- |
| `coordinator` | [Open](../presets/coordinator/) |
| `software-engineer` | [Open](../presets/software-engineer/) |
| `model-builder` | [Open](../presets/model-builder/) |
| `research-evaluator` | [Open](../presets/research-evaluator/) |
| `creative-studio` | [Open](../presets/creative-studio/) |
| `adversarial-verifier` | [Open](../presets/adversarial-verifier/) |
| `personal-companion` | [Open](../presets/personal-companion/) |
| `garden-companion` | [Open](../presets/garden-companion/) |
| `learning-coach` | [Open](../presets/learning-coach/) |
| `claims-adjudicator` | [Open](../presets/claims-adjudicator/) |
| `reverse-engineering-researcher` | [Open](../presets/reverse-engineering-researcher/) |
| `data-engineering-architect` | [Open](../presets/data-engineering-architect/) |
| `infrastructure-reliability-engineer` | [Open](../presets/infrastructure-reliability-engineer/) |
| `automation-engineer` | [Open](../presets/automation-engineer/) |
| `product-interface-designer` | [Open](../presets/product-interface-designer/) |

Some roles provide local Python engines and executable examples; others provide source descriptions and review methods only. See [Capabilities](CAPABILITIES.md) for the actual distinction.

## Five shared source skills

[Evidence Audit](../skills/shared/evidence-audit/SKILL.md), [Safe Resume](../skills/shared/safe-resume/SKILL.md), [Research Verification](../skills/shared/research-verification/SKILL.md), [Consent And Effects](../skills/shared/consent-and-effects/SKILL.md), [Quality Handoff](../skills/shared/quality-handoff/SKILL.md). These are original source guidance, disabled until the receiving host grants real permissions.

## Verify source kits

```bash
PYTHONPATH=src python3 -B examples/verify_role_packages.py --all
PYTHONPATH=src python3 -B -m muse_presets.cli doctor
```

The role verifier tests clean local package creation, receipt consistency and synthetic source exercises. It does not confirm native host credentials or tool registration. The default `skills.yaml` registries are disabled.

For real permissions and provider APIs, use the receiving platform's documented installation and review process. Generated role/skill metadata alone is not an authorization or a successful invocation.

[Customize](CUSTOMIZE.md) · [Connectors](CONNECTORS.md) · [Extend](EXTENDING_GENERIC_AGENTS.md)

## Portable instruction library

Native-style descriptor IDs use underscores for compatibility with their receiving registry. They are **not** automatically valid Agent Skills folder names. Use the separate standard-format exporter for other compatible assistants:

```bash
python -B examples/export_portable_skills.py --plan
python -B examples/export_portable_skills.py --to "$HOME/my-portable-skills"
python -B examples/export_portable_skills.py --inspect "$HOME/my-portable-skills"
```

No PYTHONPATH setting, dependency install or account is needed. The new directory contains 50 unique hyphen-named folders, each with matching name/description frontmatter and a license declaration. It contains instruction text, not installed native tools or model weights. The exporter preserves all existing owner files and refuses reuse of a destination. Import or read one skill through the receiving assistant's supported flow and verify a harmless task; persistence, routing and native permissions remain host-specific. Standard-format inspection is not evidence that a model selected or executed a skill.

The source [donor ledger](donors/DONOR_RESEARCH.json) records exact primary files and the compatibility decision. No external donor code is executed or redistributed by the exporter.

## Task-oriented collection: 75 curated skills

The [curated collection](collection/MUSE_CURATED_COLLECTION.md) offers 75 deeper task procedures selected into 100 starters and 25 workflows. It preserves the original 50 procedure IDs and portable exporter above; related entries are mapped in [PUBLIC_COMPATIBILITY.json](../collections/muse-starters-v1/PUBLIC_COMPATIBILITY.json), not added together as 125 unique capabilities. Start with `python -B tools/muse_collection.py show daily-planner` and select only what the current task needs. [Skill setup](handbook/skill-setup.md) distinguishes reading instructions, exporting a kit, host discovery and actual execution.
