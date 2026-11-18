# Architecture

Muse Hub combines assistant profiles, a skill and workflow library, Python tools, browser workspaces, and guides for connecting services. Use the components together or choose the ones that fit your task.

## Collection and engine layers

The current source includes **461 task skills**, **58 workflows** and **100 task starters** alongside the original **50 unique procedures** (45 role-specific methods plus five shared). The catalogs map the original procedure layer to the larger collection so related methods stay easy to find.

Different specialists include different executable engines. [Specialist methods and tools](collection/SPECIALIST_SCOPE_AND_ENGINES.md) describes what each role handles and which local operations are available. Browse [specialists by task](handbook/specialists-by-task.md) to choose the right role and tools.

## Role profiles

`presets/catalog.json` lists the 15 source roles. Each role has a `preset.json` for its settings and a `playbook.json` for its working methods. The files in `templates/profile/` provide editable instructions, preferences and memory placeholders.

The renderer creates a new folder and preserves existing assistants. Its receipt records source and output hashes so you can identify unchanged files, personal edits, and missing files.

## Generated profiles and procedures

`quickstart.py` composes three inspectable parts: `system-profile/profile/` for editable assistant instructions, `subchat-scopes/` for three method-specific contexts with separate blank memory, and `role-skills/` for skill definitions. Identity, preferences, voice, and prompt defaults are editable in the working copy.

The catalog has **45 role-specific methods plus five shared procedures = 50 unique procedures**. These procedures are assigned across the roles as 120 reusable skill definitions. The separate `portable_skill_export` adapter emits 50 hyphen-named folders with matching frontmatter without renaming the native-style registry IDs. The receiving host loads the selected format and manages tool permissions.

## Local tools

`src/muse_presets/` contains the executable Python modules. The `examples/` directory demonstrates how to use them, and `tests/` covers normal operation, refusals and recovery.

| Component | Responsibility |
| --- | --- |
| Coordinator | Check supplied task plans, dependencies and completion evidence. |
| Software Engineer | Stage reviewed code, track local claims and run repair exercises in disposable repositories. |
| Model Builder | Run small-model examples and check development and held-out results. |
| Research Evaluator | Match excerpts to source text and calculate metrics from supplied predictions and labels. |
| Evidence Finder | Preserve findings and their local receipt history for other tools to read. |
| Role packaging | Combine profiles, working methods and supported local tools into inspectable packages. |

Combine components through their documented inputs and outputs. Review the evidence for each result, and use the connected service to authorize and confirm external actions.

## Host integration

A host supplies the model, authenticated identity, tool permissions and live service connections. The host and connector checks inspect your configuration. Enable selected skills, hooks, and connectors through the host as you add them to a workflow.

Choose the matching configuration for Personal Muse/Hatch or Muse Code in [Host compatibility](HOST_COMPATIBILITY.md), then test the integration in that host.

## Data and permissions

Keep personal memory, credentials and host configuration outside the repository. The package owns its defaults; you own your working copies; the host owns its authentication and registrations. Do not merge these into one shared file.

Local programs use your operating-system account's permissions. Review code before running it and verify permissions for external actions through the connected service. Use package hashes to check file integrity.

## Where to make a change

Edit a role's playbook for its methods, profile templates for generated instructions, and Python modules for executable behavior. Add a regression test for each changed behavior. Keep the role catalog, package documentation and actual examples consistent.

[Get started](GITHUB_QUICKSTART.md) · [Installation and saved data](INSTALL_AND_PERSISTENCE.md)
