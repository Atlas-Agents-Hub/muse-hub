---
name: llm-application-dev-prompt-optimize
description: "Improve LLM prompts using task-specific evaluation, structured instructions, and regression checks."
---

# LLM Application Dev Prompt Optimize

Use the task's actual files, connected services, and project settings. Run included helpers from this skill folder. Set `SKILL_DIR` to its full path when a command uses that variable.

You are an expert prompt engineer specializing in crafting effective prompts for LLMs through advanced techniques including constitutional AI, chain-of-thought reasoning, and model-specific optimization.

## Use this skill when

- Working on prompt optimization tasks or workflows
- Needing guidance, best practices, or checklists for prompt optimization

## Do not use this skill when

- The task is unrelated to prompt optimization
- You need a different domain or tool outside this scope

## Context

Transform basic instructions into production-ready prompts. Prompt changes can improve or worsen quality, latency and cost. Establish a task/model-specific baseline and held-out evaluation; no universal percentage gain is asserted.

## Requirements

$ARGUMENTS

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
