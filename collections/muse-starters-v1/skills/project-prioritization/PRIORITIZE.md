# Choose the next batch of work

Compare your backlog with RICE scores, then choose work that fits the capacity of each team or resource. The calculator includes prerequisite work before selecting a task, charges shared prerequisites once, and explains why deferred work does not fit.

Use Python 3.10 or newer. Everything needed is included in the download; the calculator uses Python's standard library.

## Try the example

From the extracted package folder, run:

```sh
python -B tools/prioritize.py --input skills/project-prioritization/backlog.json
```

Use `python3` if that is your interpreter's name. The [example backlog](backlog.json) gives engineering ten person-days and design two. The highest-scoring project needs twelve engineering days, so it is deferred. The selected execution order is:

1. Prepare the customer data: two engineering days.
2. Improve onboarding: six engineering days, after the data is ready.
3. Write the first-run guide: two design days.

Engineering has two days left; design has none. The completed tracking task costs nothing in this batch. Mobile polish needs three engineering days and is deferred with a one-day shortfall. The result lists priority ranking separately from execution order so a prerequisite can run before the higher-scoring work it enables.

## Make your own backlog

Copy [backlog.json](backlog.json) to a new file, keep its structure, and replace the examples with your work. Each batch declares a common reach period, effort unit and resource capacities:

```json
{
  "schema": "muse-prioritization/v1",
  "reach_period": "customers per quarter",
  "effort_unit": "person-days",
  "capacity": {"engineering": 10},
  "items": [
    {
      "id": "improve-search",
      "name": "Help customers find the right document",
      "reach": 1000,
      "impact": 2,
      "confidence_pct": 80,
      "effort": 4,
      "resource": "engineering",
      "dependencies": [],
      "status": "todo"
    }
  ]
}
```

This task scores **400**: `1000 × 2 × 0.8 ÷ 4`. The original [RICE method](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/) uses reach, impact, confidence and effort to compare opportunities.

| Field | What to enter |
| --- | --- |
| `reach_period` | A shared measure and period, such as `customers per quarter`. Use the same basis for every item. |
| `effort_unit` | `person-hours`, `person-days` or `person-months`. All effort and capacity figures use this unit. |
| `capacity` | Available effort for each resource, including resources with zero availability. |
| `id` / `resource` | Stable lowercase names separated by hyphens, such as `improve-search` or `design-team`. |
| `name` | A useful description of the work. |
| `reach` | The estimated people or events affected in the declared period; zero is allowed. |
| `impact` | `3` for massive, `2` for high, `1` for medium, `0.5` for low or `0.25` for minimal impact. |
| `confidence_pct` | Confidence from `0` to `100`. For example, enter `80` for 80%. |
| `effort` | A positive estimate for this task, excluding prerequisites recorded as separate tasks. |
| `dependencies` | IDs that must finish first. Omit this field or use `[]` for independent work. |
| `status` | `todo` or `done`; omitted status means `todo`. Completed work remains in the dependency graph and uses no new capacity. |

Each task has one resource. Split work that requires different teams into separate tasks and connect them with dependencies. Include an item for every dependency and a capacity for every resource. Keep completed tasks in the file when other tasks refer to them.

## Use a spreadsheet

The supplied [backlog.csv](backlog.csv) describes the same example. A `.csv` input filename selects CSV reading. Give the shared metadata on the command line:

```sh
python -B tools/prioritize.py --input skills/project-prioritization/backlog.csv --reach-period "customers per quarter" --effort-unit person-days --capacity engineering=10 --capacity design=2
```

Use the same item columns as JSON. Separate dependency IDs with semicolons. The `dependencies` and `status` columns are optional; empty cells in those columns mean no dependencies and `todo`. Other cells are required. Save as UTF-8 CSV with normal CSV quoting for names containing commas or quotes. JSON files already contain this metadata, so use the metadata flags only with CSV input.

To create a ranked CSV report from either input format, use `--format csv` and choose a new filename:

```sh
python -B tools/prioritize.py --input skills/project-prioritization/backlog.json --format csv --output priorities.csv
```

The report includes priority rank, execution order, selection status, deferral reasons and resource budgets. CSV reports are for reading; keep the original backlog as the editable input. Text that could be interpreted as a spreadsheet formula receives a leading apostrophe in CSV output. JSON preserves the original text.

## Read the result

The JSON report contains:

- `ranked_items`: every task, ordered by its exact RICE score descending, then by ID for ties. `score` is a display value rounded to six decimal places; `score_exact` preserves the fraction used for ranking.
- `selected_order`: the next batch in dependency order. Shared prerequisites appear once.
- `deferred`: each task that did not fit, its unmet prerequisite bundle and the shortfall for each constrained resource at the time it was considered.
- `completed_ids`: the tasks you marked done.
- `budgets`: capacity, used effort and remaining effort for each resource.

The calculator considers unfinished tasks in score order. For each one, it checks the full unmet prerequisite bundle against every affected resource. It selects the whole bundle when it fits and leaves all budgets unchanged when it does not. Already selected or completed prerequisites cost nothing on later passes. Numeric quantities in the JSON report are decimal strings so another tool can retain their exact values.

Use this greedy selection to choose a feasible batch. Review deadlines, obligations, estimate quality and strategic value with the [prioritization procedure](SKILL.md). The calculator does not optimize all possible task combinations or assign calendar dates. A low-confidence estimate still needs investigation even if its score is high.

## Fix an input error

An invalid request exits with code `2`, writes a specific message to the error stream and produces no report. Unknown fields, duplicate IDs or JSON keys, missing dependencies, cycles, invalid impact levels and incompatible numbers must be corrected before the whole backlog is processed.

Use a regular UTF-8 file no larger than 1 MiB, with 1–1,000 items. Numbers must use JSON decimal syntax, have magnitude at most `10^12`, at most twelve decimal places and an exponent from `-12` to `12`. Numeric JSON values are numbers, not quoted strings. IDs and resources are limited to 64 characters, names to 500, and the reach-period label to 200.

Existing output files are preserved. Choose another name when `--output` reports that a destination exists. With no `--output`, the complete report is printed to the terminal; with it, a new file is created and successful execution is silent.

## Run from the repository

The downloadable package keeps the skill under `skills/`; the repository keeps it under `collections/muse-starters-v1/skills/`. From the repository root, run:

```sh
python -B tools/prioritize.py --input collections/muse-starters-v1/skills/project-prioritization/backlog.json
```

[Skill procedure](SKILL.md) · [Worked examples](DEPTH.md) · [Sources and implementation](PROVENANCE.md)
