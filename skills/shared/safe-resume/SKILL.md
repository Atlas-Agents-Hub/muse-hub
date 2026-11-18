---
name: safe-resume
description: Use when interrupted tasks, partial writes, retries or concurrent work require safe recovery.
license: MIT
---

# Safe Resume

Recover original work without blind replay, deletion or writer takeover.

## When to use

Use when interrupted tasks, partial writes, retries or concurrent work require safe recovery.

## Procedure

1. Identify task identity, original operation, source revision, current owner and live writer.
2. Inspect exact output, scratch, worktrees, stashes, ignored files and effect provider state.
3. Classify already complete, still running, partial, conflicting or unknown.
4. Do not repeat consequential operations whose effects are unknown.
5. Resume only an authorized reversible next slice and record new receipt.

## Evidence

Return the exact source identity, measured result, uncertainty and next action. Do not report an unexecuted operation as done.

## Stop rule

Unknown prior external effect requires readback and HOLD before retry.

## Use with your assistant

Apply this procedure to the current task using the tools and account access authorized for that work. Preserve the user's preferences and memory. Configure any additional tool through the host's supported setup, and obtain approval when an action needs it.
