---
name: varlock-claude-skill
description: "Secure environment variable management with explicit checks to reduce secret exposure in Claude sessions, terminals, logs, or git commits"
---

# Varlock Claude Skill

Use the task's actual files, connected services, and project settings. Run included helpers from this skill folder. Set `SKILL_DIR` to its full path when a command uses that variable.

## Overview

Secure environment variable management with explicit checks to reduce secret exposure in Claude sessions, terminals, logs, or git commits

## When to Use This Skill

Use this skill when you need to work with secure environment variable management with explicit checks to reduce secret exposure in claude sessions, terminals, logs, or git commits.

## Procedure

This entrypoint does not bundle Varlock or enforce secret redaction. Inspect a reviewed installed version and its schema using non-secret examples. Establish which environment files and variable names are in scope; never dump values into the conversation, terminal logs or generated reports. Keep real secrets in the authorized local secret store and use placeholders in tests. Verify handling with synthetic canary values and check the destination permissions and ignore rules. Report the actual checks and remaining exposure paths; no guide can guarantee that secrets are never exposed.

Source: [Varlock Claude Skill](https://github.com/wrsmith108/varlock-claude-skill).

## Example

**User request:**

> Use @varlock-claude-skill for this task: Secure environment variable management with explicit checks to reduce secret exposure in Claude sessions, terminals, logs, or git commits.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
