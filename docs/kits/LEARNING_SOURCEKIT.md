# Study-session tool

Create questions from supplied definitions, review them, record practice scores, and reopen study history in SQLite. This portable Python kit includes the LearningSession engine, a disposable worked example, tests, and a runner. For assistant-guided study, start with [Learning Coach](../../presets/learning-coach/INSTALL.md).

## Build and verify

From the toolkit root with Python 3.12+:

```sh
PYTHONPATH=src python3 -B examples/export_learning_sourcekit.py --to "$HOME/learning-coach.zip"
PYTHONPATH=src python3 -B examples/export_learning_sourcekit.py --verify "$HOME/learning-coach.zip" --sha256 EXPECTED_SHA256
```

Replace `EXPECTED_SHA256` with the digest from a trusted release record or your retained export result. On Windows PowerShell, set `$env:PYTHONPATH = "src"` and use `python` instead of `python3`. Choose a new output file in an existing private directory; the exporter preserves existing files.

Verification compares the supplied digest and the exact canonical archive bytes. A recompressed or changed ZIP is refused before extraction. Keep the expected digest with your download so you can verify the same package later.

## Try a study session

Extract the verified kit into a new directory and open a terminal there:

```sh
python -I -B run.py --operation demo
python -I -B run.py --operation self-test
```

The example registers supplied definitions, creates questions with source locations, reviews one as a fictional owner, records an answer, and reopens its receipt. It also checks that a correctly answered item becomes due again after 24 hours. The sample SQLite database is removed when the example finishes.

The runner checks its files, manifest, and paths before importing the engine. Changed source, unexpected import files, linked paths, and malformed manifests are refused. The extracted kit uses Python's standard library and runs independently of the original repository on Windows, macOS, and Linux.

## Use your own study records

Follow the [study-session integration guide](../LEARNING_LOCAL_STUDY.md) to add the library to an application. The question generator reads `Term :: Definition.` lines. Scoring compares case- and whitespace-normalized text, and the review queue uses a fixed next-day schedule for correct answers. Review questions and choose an assessment method appropriate to the learner and subject.

Resolve users and sessions through the application's trusted host callback. Keep owner review and learner access separate; browser fields and model text cannot authenticate a person. Store personal databases outside the kit in a protected directory, with suitable backup and retention controls. SQLite stores readable source text and answers, so use a system with the required protections for confidential examinations or sensitive information.

Run reviewed Python code in a workspace you control, with the permissions you intend it to have. Updates use a newly verified kit while your records remain in their own location. Review storage compatibility before moving existing data.

## Developer checks

```sh
PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_learning_sourcekit.py -v
PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_learning_session.py -v
```

These checks exercise packaging, user and session separation, source changes, duplicate scoring, transaction rollback, and reopening.

[Learning Coach setup](../../presets/learning-coach/INSTALL.md) · [Study sessions](../LEARNING_LOCAL_STUDY.md) · [Terminal](../TERMINAL.md)
