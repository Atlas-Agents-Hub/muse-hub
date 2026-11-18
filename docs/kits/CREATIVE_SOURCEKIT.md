# Creative Studio production planner

Turn a creative brief into shot specifications, an exact frame timeline, asset dependencies, continuity checks, and an HTML storyboard. Use the resulting plan with your chosen image, animation, video, or design tools.

## What the planner produces

| Output | Use it for |
| --- | --- |
| Normalized creative brief | Keep project settings, assets, scenes, and stable shot IDs together. |
| Frame timeline and shot list | Coordinate shot order, duration, and asset use. |
| Asset and task graph | Identify dependencies before production. |
| Continuity checks | Catch contradictions in declared character and scene states. |
| Textual HTML storyboard | Review shot descriptions in a browser. |
| Revision comparison | See changed assets, scenes, shots, timing, and order. |

The kit includes Creative Studio's role instructions and Python tools. The planner works with written descriptions and declared states; use your production tools to render media and inspect its visual quality.

## Build and verify the kit

From the toolkit root with Python 3.12+:

```sh
PYTHONPATH=src python3 -B examples/export_creative_sourcekit.py --to "$HOME/creative-studio.zip"
PYTHONPATH=src python3 -B examples/export_creative_sourcekit.py --verify "$HOME/creative-studio.zip" --sha256 EXPECTED_ZIP_SHA256
```

Replace `EXPECTED_ZIP_SHA256` with the digest from the trusted release record or the export result you retained. Both commands refer to the same ZIP. In PowerShell, set `$env:PYTHONPATH = "src"` and use `python` instead of `python3`.

Choose a new ZIP path outside the toolkit in an existing directory. The exporter preserves existing files. Verification compares the expected canonical bytes and checks the supplied digest before extraction.

## Try a production plan

After verifying the download, extract it into a new directory. Open a terminal in that directory:

```sh
python -I -B run.py --operation self-test
python -I -B run.py --operation demo --to "$HOME/creative-production"
python -I -B run.py --operation verify --project "$HOME/creative-production" --sha256 EXPECTED_BRIEF_SHA256
```

The output folder must be new, with an existing parent. Replace `EXPECTED_BRIEF_SHA256` with the `brief_sha256` value printed by the demo or compile command, and retain that value with your project. These commands use Python's standard library. Store your briefs and outputs outside the extracted kit.

The worked example contains two scenes, three shots, and 168 frames at 24 fps. It checks a lantern changing from `off` to `warm` and a courier picking it up. A later shot that contradicts a declared earlier state is refused with an error explaining the conflict.

## Use your own brief

Copy `sample-brief.json` outside the kit and edit that copy. The repository example is `examples/creative_brief.json`.

```sh
python -I -B run.py --operation compile --brief /absolute/brief.json --to /absolute/new/production
python -I -B run.py --operation diff --before /absolute/brief.json --after /absolute/revised-brief.json
```

The brief has four top-level fields:

- `schema`: `muse-presets/creative-brief-v1`.
- `project`: `id`, `title`, `summary`, `audience`, `fps`, `aspect_ratio`, and `constraints`.
- `assets`: `id`, `kind`, `label`, `reference`, `rights`, `depends_on`, and `initial_state`.
- `scenes`: an ordered list with `id`, `title`, background-asset `location`, and `shots`.

Each shot contains `id`, `description`, `framing`, integer `duration_frames`, `assets`, `depends_on`, `requires`, and `changes`. Framing is `wide`, `medium`, `close`, or `detail`. Asset kinds are `character`, `prop`, `background`, `audio`, or `graphic`. Use lowercase symbolic identifiers and references in the form `asset:ASSET_ID`.

Record each asset's license, credit, and source in `rights`. Supported declarations are `original`, `CC0-1.0`, or `CC-BY-4.0`, with `restricted:false` and `person_copy:false`. Confirm the underlying rights before using the actual media; the planner validates the fields you supply.

Dependencies must exist and form an acyclic graph. Shot dependencies must appear earlier in the sequence. A shot's `requires` values must match the prior state; its `changes` update that state for later shots. Keep state keys in the asset's `initial_state`.

Input limits are 256 KiB, 128 assets, 64 scenes, 256 shots, 1,000,000 frames, 16 state keys per asset, and 32 asset/dependency references per shot. Frame rates are 12, 24, 25, 30, 48, 50, or 60 fps. Unknown fields, duplicate JSON keys, nonfinite values, excessive nesting, and contradictory states are refused. Prose constraints remain available for your production review.

## Open the results

The new project folder contains `BRIEF.json`, `PRODUCTION.json`, `SHOT_LIST.csv`, `STORYBOARD.html`, and `MANIFEST.json`. Open the HTML file to review the textual storyboard. Use the CSV and JSON files in your production workflow, then inspect rendered media in its intended application.

Verification reconstructs the expected artifacts from the brief and checks their exact bytes. Keep the original brief digest and export result so you can verify later revisions. Checksums identify the expected files; trust the publisher and source through your normal review process.

## Recover and update

An interrupted export leaves its partial output in place. Inspect it before choosing a new destination. Keep earlier briefs and outputs, and compile a revised brief into a new folder to compare versions.

The runner checks its source files and input paths before execution. Use a private workspace and reviewed Python installation; isolated import mode is not an operating-system sandbox. Updates use a new verified kit while your project files stay in their existing location.

## Developer checks

```sh
PYTHONPATH=src python3 -B -m unittest discover -s tests -p 'test_creative*.py' -v
```

[Creative Studio setup](../../presets/creative-studio/INSTALL.md) · [Creative workflow](../collection/CREATIVE_STUDIO_SCOPE.md) · [Terminal](../TERMINAL.md)
