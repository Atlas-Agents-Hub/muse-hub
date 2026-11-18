# Study sessions and saved practice

Turn source material into questions, review the answers, and keep useful practice records. Start with the [Learning Coach](../presets/learning-coach/INSTALL.md) and a lesson or reference you are allowed to use. The toolkit also includes a Python study ledger for applications that need reviewed questions and SQLite history.

## Try a study session

From the toolkit root with Python 3.12+:

```sh
PYTHONPATH=src python3 -B examples/learning_session_demo.py
```

In Windows PowerShell, set `$env:PYTHONPATH = "src"` and run `python -B examples/learning_session_demo.py`.

The example registers supplied definitions, prepares questions, reviews one, records an answer and score, and reopens the receipt. It uses fictional users and a temporary database that is removed when the example finishes. The [portable study kit](kits/LEARNING_SOURCEKIT.md) runs the same workflow after extraction into a separate folder.

## How a session works

1. **Add source material.** `register_source(source_id=..., version=..., text=...)` records the supplied text, version, and digest. Keep the source reference and permission to use it with your study material.
2. **Prepare questions.** `propose_source_facts(source_id, limit=20)` reads lines in `Term :: Definition.` form and keeps their source locations. The limit applies to new questions as well as returned results; skipped lines and truncation remain explicit.
3. **Review questions.** The owner checks the exact question and source version before approving it. Changed text or a stale digest requires another review.
4. **Practice.** `issue` supplies an approved question, source location, and expiry while withholding the stored answer. The learner submits an answer in the same session.
5. **Score and reopen.** `submit` compares normalized text with the approved answer and saves the attempt in one transaction. `score_receipt` reopens the result after an interrupted response.
6. **Review again.** The review queue makes unanswered and incorrect items due now and correct items due after 24 hours. This is a fixed practice schedule; choose a learning method appropriate to your goals.

Scoring normalizes case and whitespace. Use a reviewed rubric or your chosen teaching tools when a task needs interpretation, partial credit, or subject-matter judgment.

## Keep your own study history

Integrate [`LearningSession`](../src/muse_presets/learning_session.py) with an absolute database path inside an existing private directory. Store the database outside the application package and retain it when updating. It contains readable study text and stored answers; keep it out of public repositories and shared folders, and apply suitable backup and retention controls.

The application supplies an `authority: () -> LearningScope` callback on every operation. Resolve the real owner, Space, learner, and session through the trusted host, then enforce owner review and learner access separately. Browser IDs and model text must not authenticate a person. The example's fictional callback illustrates the API sequence.

Review material and questions for the intended learner before use. For confidential examinations, regulated assessments, or sensitive health information, use a system with the storage, access controls, and review process required for that setting.

## Recover a missing result

Reuse the original operation ID to read the saved receipt. A changed answer, different session, stale source version, or conflicting operation ID is refused. Inspect the original attempt before creating another one. Keep source versions and recorded attempts so you can understand an earlier score after the material changes.

## Developer checks

```sh
PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_learning_session.py -v
```

The tests cover source changes, owner and session separation, duplicate scoring, expiry, hidden extra writes, unsafe paths, transaction rollback, and reopening. The library uses Python's standard library.

[Learning Coach](../presets/learning-coach/INSTALL.md) · [Portable kit](kits/LEARNING_SOURCEKIT.md) · [Setup and saved data](INSTALL_AND_PERSISTENCE.md)
