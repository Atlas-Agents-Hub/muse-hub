# Practice and evaluate a skill

Start with a task you can inspect. Give Muse the task, the required source material, and the selected skill. Compare the completed artifact with the skill's expected output, then try a meaningful edge case or interruption.

## Use the practice examples

The collection includes worked examples, expected results, alternative results that should fail, and checks for the developed methods. Browse a skill's `DEPTH.md` and the corresponding records in `depth_cases.json`. `evaluation_cases.json` contains task specifications and review rubrics. [Current inventory](COUNTS.json) lists the available practice material.

Use the worked examples to learn the method. For a comparison, choose a task whose answer is kept out of the participant's instructions.

## Prepare a comparison

Export the same task in two conditions:

```sh
python -B tools/muse_collection.py challenge daily-briefing-standard --arm plain --to "$HOME/practice-plain.zip"
python -B tools/muse_collection.py challenge daily-briefing-standard --arm candidate --to "$HOME/practice-with-skill.zip"
```

Use a new output filename for each export. The plain packet supplies the task and inputs. The skill packet adds the selected method. Both use the same `TASK.json`; comparison packets leave the expected and incorrect answers with the evaluator.

Keep the source files, available tools, requested time budget, and visible model settings the same. Use fresh conversations, vary the order of conditions, and retain every output and tool error. Record the settings you can observe in the application.

## Review the result

Evaluate the artifact against concrete criteria:

| Criterion | What to inspect |
| --- | --- |
| Correctness | Calculations, code behavior, and factual claims match the inputs and sources. |
| Completeness | The result covers the required parts of the task. |
| Usefulness | A person can use the output with clear next steps. |
| Source fidelity | References support the claims and uncertainty is preserved. |
| Tool use | The selected tools fit the task and respect the user's permissions. |
| Recovery | An interrupted or failed step preserves completed work and avoids duplicate effects. |
| Effort | The task finishes within its budget with a reasonable amount of user input. |

Inspect code by running the relevant tests, documents by opening the saved artifact, and interface work in a browser. Keep both strengths and failures in the review. Repeat useful cases with different inputs before choosing a lasting workflow change.

## Record a useful improvement

Keep the task, supplied files, skill version, observed settings, actual output, and review together. Describe the specific result that improved and any tradeoff, such as extra time or a new dependency. Use the evidence to revise the method, its example, or its recovery instructions.

[Skill standards](CURATION_POLICY.md) · [Skill index](SKILL_INDEX.md) · [Task starters](CATALOG.md)
