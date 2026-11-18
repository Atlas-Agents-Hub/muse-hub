# Collect Structured Data from the Web

Extract a bounded set of web records and turn it into a checked dataset.

## Bring these inputs

- Target pages and fields to collect
- Authorized browsing context and expected record structure

## 1. Browser Automation

Read [the Browser Automation method](../skills/browser-automation/SKILL.md). Inspect the actual pages and extract the required fields with source URLs and collection times.

**Carry forward:** A structured record set with source locations and extraction errors.

**Check:** The extract covers the intended records and retains enough evidence to inspect any value.

## 2. Data Quality Auditor

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Check types, completeness, duplicate records, and field consistency in the extract.

**Carry forward:** A quality report and corrected dataset.

**Check:** Invalid records are reported explicitly and corrections can be traced to the source.

## 3. SQL Database Assistant

Read [the SQL Database Assistant method](../skills/sql-database-assistant/SKILL.md). Load the checked dataset into the chosen schema and answer the original query.

**Carry forward:** A reproducible import and query result.

**Check:** Imported counts and query totals reconcile with the checked dataset.

## Check the finished work

- The extract covers the intended records and retains enough evidence to inspect any value.
- Invalid records are reported explicitly and corrections can be traced to the source.
- Imported counts and query totals reconcile with the checked dataset.

## Finish

A reproducible import and query result. Imported counts and query totals reconcile with the checked dataset.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
