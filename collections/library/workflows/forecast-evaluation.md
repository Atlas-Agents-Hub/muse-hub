# Evaluate a Forecast

Compare forecasts with temporal validation and useful uncertainty estimates.

## Bring these inputs

- Time-stamped observations
- Forecast horizon and decision cost

## 1. Time Series Analysis

Read [the Time Series Analysis method](../skills/time-series-analysis/SKILL.md). Inspect seasonality, trend, gaps, and changes in measurement.

**Carry forward:** A cleaned series and temporal split plan.

**Check:** The split preserves time order and prevents information leakage.

## 2. Statistical Modeling

Read [the Statistical Modeling method](../skills/statistical-modeling/SKILL.md). Fit a baseline and candidate models on the split plan.

**Carry forward:** Forecasts, fitted assumptions, and error estimates.

**Check:** Each candidate uses the same training and evaluation windows.

## 3. Statistical Review Checklist

Read [the Statistical Review Checklist method](../skills/statistical-review-checklist/SKILL.md). Review the comparison, uncertainty, and failure periods.

**Carry forward:** A model choice with limits and a monitoring trigger.

**Check:** The selected model improves the relevant decision metric over the baseline.

## Check the finished work

- The split preserves time order and prevents information leakage.
- Each candidate uses the same training and evaluation windows.
- The selected model improves the relevant decision metric over the baseline.

## Finish

A model choice with limits and a monitoring trigger. The selected model improves the relevant decision metric over the baseline.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
