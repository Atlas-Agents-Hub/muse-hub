# Create something

Start with an idea, shape it into a clear brief and carry it through the tools that make it real. Use Muse for the conversation, Creative Studio for the plan, and the image, design or video tools that suit your project.

## 1. Shape the idea in Muse

Bring the purpose, audience, format and reference material you can use. Start with:

```text
Help me develop [PROJECT] for [AUDIENCE]. The output should be [FORMAT],
with [STYLE OR REFERENCES] and [CONSTRAINTS]. Ask for the missing decisions,
then propose a concise creative brief and an asset list.
```

[Muse supports image and document creation](https://ai.meta.com/muse/), and you can [talk through an idea using voice](https://muse.ai/). Decide what a successful result should communicate before choosing the production tool.

## 2. Add Creative Studio

[Download Creative Studio](../../presets/creative-studio/INSTALL.md), extract the ZIP and open `START_HERE.md`. Follow the guide to configure its assistant and three subchats, then give it your brief and references.

```text
Use the Creative Studio guide to turn this brief into a shot plan, asset
list and continuity checklist. Include what should stay consistent between
scenes and what needs a review before production.
```

Keep a short record of the choices you accept: visual style, characters, colors, framing, duration and output format. Use that record when reviewing later versions.

## 3. Turn the brief into a production plan

The [Creative Studio production planner](../kits/CREATIVE_SOURCEKIT.md) creates a frame timeline, shot-list CSV, asset dependencies and an HTML storyboard of shot descriptions.

For the optional planner, use Python 3.12+ from a toolkit checkout. The [terminal guide](../TERMINAL.md#run-muse-hub-tools) covers setup. Choose a new ZIP path in an existing directory and export the portable production kit.

**macOS or Linux:**

```sh
PYTHONPATH=src python3 -B examples/export_creative_sourcekit.py --to "$HOME/creative-studio.zip"
```

**Windows PowerShell:**

```powershell
$env:PYTHONPATH = "src"
python -B examples/export_creative_sourcekit.py --to "$HOME/creative-studio.zip"
```

Follow the production planner guide's verification step, extract that ZIP into a new folder, and open a terminal in the extracted folder. Choose a new output folder with an existing parent directory for the worked example:

```sh
python -I -B run.py --operation self-test
python -I -B run.py --operation demo --to "$HOME/creative-production"
```

Use `python3` where appropriate. The new project contains:

| File | What to do with it |
| --- | --- |
| `BRIEF.json` | Keep the project's settings, scenes and assets together. |
| `PRODUCTION.json` | Review the planned timeline and dependencies. |
| `SHOT_LIST.csv` | Bring the shot order, durations and asset use into production. |
| `STORYBOARD.html` | Open the shot descriptions in a browser. |
| `MANIFEST.json` | Keep the generated file record with the project. |

To use your own project, copy the kit's `sample-brief.json` outside the kit and edit that copy. The [brief guide](../kits/CREATIVE_SOURCEKIT.md#use-your-own-brief) explains the scene, shot and asset fields and the commands for compiling or comparing versions.

## 4. Make and review the media

Use Muse's creation features or browse [design and creative connectors](../connectors/CATALOG.md#design-and-creative) for your image, sound, design and video tools. Follow the selected tool's setup, then carry your brief and shot list into production.

Review the actual output against the brief:

- Does it communicate the intended idea to the intended audience?
- Are characters, objects and scene details consistent?
- Do framing, timing, text and sound work in the final format?
- Can you identify the files and decisions used for this version?

Save revised briefs and outputs in separate folders so you can compare them. For a project dashboard or mood board inside the Muse app, describe the Space you want; [Muse supports custom Spaces in the sidebar or main tabs](https://apps.apple.com/us/app/muse-from-meta/id6760173601).

## 5. Play with motion and companion ideas

[Companion Home](../COMPANION_HOME.md) gives your creative work a place to experiment. In **Studio**, try the four poses with **Pause**, **Resume** and **Next pose**. Its motion controls respect reduced-motion settings.

In the **Arcade**, try **Signal Trail**: choose the highlighted tile with touch, a click or keys **1–4**. The game keeps its progress in your browser. Follow the [Companion Home guide](../COMPANION_HOME.md#explore-the-five-rooms) to open the room tour or launch the workspace with saved notes.

For another starting point, explore [companion and creative projects](https://atlas-origins.github.io/muse-ai-agent-presets/public/index.html?route=companion). Open a project's details, choose the tools for your idea and follow its setup guide.

## Your first useful result

Keep a brief that defines the audience and deliverables, a shot plan you can follow, and an actual output reviewed in its intended format. Use those artifacts as the starting point for the next revision or specialist handoff.

[Muse Hub](../../README.md) · [Organize your day](ORGANIZE_YOUR_DAY.md) · [Build and automate](BUILD_AND_AUTOMATE.md)
