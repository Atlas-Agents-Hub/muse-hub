---
name: data-quality-auditor
description: "Use before analysis or model training on any dataset, or when asked to profile data or hunt missing values and outliers. Profiles it with data_profiler.py, missing_value_analyzer.py and outlier_detector.py and writes a remediation plan."
---

# Data Quality Audit

## Inspect the data

Record the expected columns, types, units, keys, time range, and null conventions before interpreting the file. Keep an unchanged input copy and identify the dataset version used for the audit.

1. Run the profiler to inspect the actual columns and distributions:

   ```bash
   python3 scripts/data_profiler.py --file data.csv --format json
   ```

   The profiler reports row and column counts, observed types, nulls, cardinality, and numerical summaries. Its score is the percentage of non-null cells among the selected columns, labeled `completeness`. A complete dataset may still contain incorrect, duplicated, inconsistent, or stale values; inspect those properties separately against the project's rules. Sample standard deviation is undefined for a single observation and is reported accordingly.

2. Inspect missing-value patterns:

   ```bash
   python3 scripts/missing_value_analyzer.py --file data.csv
   ```

   Use the output to locate affected columns, rows, and groups. Treat explanations of missingness as hypotheses to investigate with domain evidence. Observed patterns alone do not establish whether missingness depends on an unobserved value.

3. Identify values needing review:

   ```bash
   python3 scripts/outlier_detector.py --file data.csv --method iqr
   ```

   Check flagged values against units, plausible ranges, collection errors, and legitimate rare cases. Choose the method to match the distribution. Preserve legitimate extremes and document every correction or exclusion.

4. Test the declared keys, cross-column relationships, value domains, and freshness requirement. Reconcile record counts across transformations. For duplicate events, use an explicit event identity and version rule instead of selecting an arbitrary last row.

5. Rank findings by their effect on the intended analysis or application. Assign each correction an owner, a rule, and a verification query. Rerun the relevant checks on the corrected dataset and compare the results with the retained input.

## Deliver

Provide the input identity, column profile, measured completeness, concrete counterexamples, and a prioritized remediation plan. Record how nulls, duplicates, outliers, and timestamps were treated. State each acceptance check in terms of the actual use case; use that check to decide whether the dataset is suitable for its next step.

## Reference

Read [data quality concepts](references/data-quality-concepts.md) for missingness assumptions, outlier methods, and additional quality checks.
