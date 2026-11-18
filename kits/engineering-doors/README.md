# Engineering repair workflow

Work through a complete repair: capture the case, reproduce the failure, make a focused change, run regression tests, and review the result. The included example creates its own temporary Git repository and uses the existing Claim Gate to coordinate the work.

## Run the example

From the toolkit root, use Python 3.12+ and Git:

```sh
PYTHONPATH=src python3 -B examples/five_door_offline_demo.py
```

In Windows PowerShell, set `$env:PYTHONPATH = "src"` and run `python -B examples/five_door_offline_demo.py`.

The example reproduces a failing test, applies a change against the expected source, reruns four tests, and reopens the result for review in a separate process. Read the returned report to inspect the failure, repair, passing checks, and review result.

## Use the method for your work

| Step | Useful result |
| --- | --- |
| Capture | A clear task, source version, and expected behavior. |
| Reproduce | A command or test that demonstrates the failure. |
| Repair | A focused change tied to the reproduced cause. |
| Check | Passing regression checks and reviewed source changes. |
| Review | A second inspection of the result and its supporting evidence. |

Run code in a workspace you control. If execution is interrupted or a result is uncertain, inspect the original operation before repeating it. Keep the source and test results together through the handoff.

## Developer reference

The example composes the existing `engineering_workflow.py` execution and review operations. The [manifest](manifest.json) and [route descriptions](stage-routes.json) document its source relationship and integration contract. They are useful when extending the workflow.

```sh
PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_h11_engineering_doors.py -v
```

[Software Engineer](../../presets/software-engineer/INSTALL.md) · [Workflows](../../docs/WORKFLOWS.md) · [Terminal](../../docs/TERMINAL.md)
