# Skill library standards

Each skill should help someone complete a distinct task. It should explain when to use it, what to provide, how to work through the task, what a useful result contains, and how to recover when a step fails.

## Choose the right level

Use a **skill** for one reusable method, a **workflow** for a sequence of related methods, and a **task starter** for a ready-to-use selection with a first task. Connect each addition to the specialists whose work it improves.

Prefer a clear existing method over another entry with a similar name. Combine overlapping instructions when they lead to the same output. Keep specialist identities and personal preferences separate from the selected task methods.

## Make the instructions useful

- Name the inputs and give a concrete example.
- Explain how to choose between meaningful alternatives.
- Identify the required tools and provide a useful fallback when an optional tool is unavailable.
- Describe the expected output and a practical way to check it.
- Include common failures and recovery steps that preserve completed work.
- Keep instructions concise enough to load only what the task needs.

## Include working tools

When a skill contains a script, include its required local files, dependency instructions, and a representative input. Check the output and at least one relevant failure case. Keep generated files in a new destination, preserve user data, and document the command needed to run it.

## Respect source licenses

Keep applicable license and attribution notices with redistributed material. Check the terms of individual files and dependencies as well as the enclosing package. Use references for material whose terms permit linking but not redistribution.

## Keep the catalog consistent

Every skill, workflow, starter, and specialist has a stable ID. Workflow and specialist references must resolve to entries in the current library. The [inventory](COUNTS.json) reports counts calculated from the shipped catalogs and practice files.

Run the collection and compatibility checks after an update:

```sh
python -B tools/muse_collection.py check
python -B tools/collection_compatibility.py
python -B tools/collection_compatibility.py --inventory
```

Use [practice and evaluation](EVALUATION.md) to check an actual result, and [choose an expansion](ROADMAP.md) when a task needs more coverage.
