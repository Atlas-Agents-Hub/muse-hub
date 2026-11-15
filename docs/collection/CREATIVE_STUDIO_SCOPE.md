# Creative Studio — visual production from concept to delivery

Creative Studio is the specialist for **original images, animation, video and interactive work**. Its playbook covers the creative process: establish visual direction, plan assets and scenes, develop shot and interaction requirements, inspect rendering and continuity, and package a reviewed deliverable.

## What the specialist can help with

- **Creative direction:** Develop the brief, audience, style, format, dimensions, accessibility requirements and approved visual references.
- **Asset and scene development:** Plan characters, environments, props and licensed media, including dependency and rights records.
- **Animation and interaction:** Define shots, motion, timing, scene changes, interactive states and intended output formats.
- **Render and continuity review:** Examine real images, frames, video or browser output for composition, motion, safe areas, legibility and consistency.
- **Production handoff:** Preserve source and asset hashes, rendering requirements, review decisions and what the target consumer actually opened.

These describe the specialist's **role methods**, including stages that use host-provided rendering or design tools. The source-only role profile does not automatically connect those tools.

## What the bundled Python tool does today

The included standalone executable is a **production planner, not an image or video renderer**. It compiles approved briefs into asset dependencies, shot timelines, continuity reports and a textual storyboard. It can compare input briefs and verify exported projects.

From a repository checkout with Python 3.12+:

```sh
PYTHONPATH=src python3 -B examples/creative_studio_demo.py
```

See the [Creative Studio sourcekit guide](../kits/CREATIVE_SOURCEKIT.md) for the executable's self-test, compile, verify and diff operations.

## How to judge real creative output

When an authorized image/video renderer, animation program or browser build is available, the role's render-and-inspect method calls for checking **actual media or interactive states**, not just source files or storyboards. Review motion, continuity, accessibility, asset rights and handoff quality against the brief.

[Creative Studio profile](../../presets/creative-studio/README.md) · [Role playbook](../../presets/creative-studio/playbook.json) · [Current capability matrix](../CAPABILITIES.md) · [Full specialist catalog](SPECIALIST_CATALOG.md)
