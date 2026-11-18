# Validate a Security Detection

Build a detection from a concrete behavior and measure it against representative events.

## Bring these inputs

- Authorized detection scenario
- Logs, event schemas, and expected benign activity

## 1. Threat Detection

Read [the Threat Detection method](../skills/threat-detection/SKILL.md). Define the behavior, telemetry, and detection hypothesis.

**Carry forward:** A detection specification and event requirements.

**Check:** Required fields are available and the hypothesis is tied to observable behavior.

## 2. SIEM Engineer

Read [the SIEM Engineer method](../skills/siem-engineer/SKILL.md). Implement the query or rule and inspect representative events.

**Carry forward:** A detection rule with example matches and exclusions.

**Check:** The rule parses the actual schema and handles missing or malformed events.

## 3. Detection Validation

Read [the Detection Validation method](../skills/purple-team/SKILL.md). Exercise the scenario and compare intended signals with observed alerts.

**Carry forward:** A validation report with false positives, missed events, and improvements.

**Check:** The alert fires for the intended behavior and benign cases are measured.

## Check the finished work

- Required fields are available and the hypothesis is tied to observable behavior.
- The rule parses the actual schema and handles missing or malformed events.
- The alert fires for the intended behavior and benign cases are measured.

## Finish

A validation report with false positives, missed events, and improvements. The alert fires for the intended behavior and benign cases are measured.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
