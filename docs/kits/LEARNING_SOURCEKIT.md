# Study-session tool

Create questions from supplied definitions, review them, record practice scores, and reopen study history in SQLite. The portable kit includes the LearningSession engine, a worked study example, tests, and a runner. Use Python 3.12+ on Windows, macOS, or Linux.

## Build and inspect

From this repository:

    PYTHONPATH=src python3 -B examples/export_learning_sourcekit.py --to "$HOME/learning-coach.zip"
    PYTHONPATH=src python3 -B examples/export_learning_sourcekit.py --verify "$HOME/learning-coach.zip" --sha256 EXPECTED_SHA256

On Windows set $env:PYTHONPATH='src' and use python instead of python3.
Export is create-only and requires an existing safe parent directory.
Verification compares bounded exact canonical bytes without parsing or
extracting a supplied ZIP. Recompressed or changed packages are refused even
when their caller-supplied hash matches. A separately trusted digest is still
needed to establish the expected artifact; hashes are not publisher signatures.

After verifying the digest and extracting into a new directory:

    python -I -B run.py --operation demo
    python -I -B run.py --operation self-test

The runner checks file names, sizes, hashes, directories, manifest and linked
paths before importing the engine. Unknown files, import shadows, duplicate
or deeply nested manifest JSON and optimized-interpreter operation refuse.
It supports Windows, macOS and Linux Python 3.12+; platform-specific skips
remain explicit. The extracted source does not need the original repository.

## Useful behavior and boundaries

The demo admits explicitly supplied definitions with source hashes and line
locators, creates held drafts, approves one as a synthetic owner, gives the
learner a question without its answer, records a score, reopens SQLite,
recovers the same receipt and calculates next-day review eligibility.
The original 25-test engine suite exercises wrong-role and cross-session
refusal, source tampering, injected lessons, stale versions, duplicate scoring,
transaction rollback and concurrent connections.

The generator accepts only simple Term :: Definition. lines. Scoring is literal
case/whitespace normalization, not semantic assessment. Review due times use
HEURISTIC_V1_NOT_FSRS, not validated adaptive mastery. Material is caller-supplied
and is not independently verified educational or clinical content.

Read [the local study contract](../LEARNING_LOCAL_STUDY.md) before integration.
LearningScope is not a credential: use a protected host-side authority callback,
never model/browser identity fields. SQLite is unencrypted local storage and is
not appropriate for clinical data, examination secrets or regulated scoring.
Python -I is not an OS sandbox. Demo databases are disposable; user databases
belong outside the immutable kit. Upgrade by creating a newly verified kit;
there is no automatic migration or state-deleting uninstall.

## Repository regression commands

    PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_learning_sourcekit.py -v
    PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_learning_session.py -v
    PYTHONPATH=src python3 -B -m unittest discover -s tests -v

[Learning Coach setup](../../presets/learning-coach/INSTALL.md) · [Study sessions](../LEARNING_LOCAL_STUDY.md)
