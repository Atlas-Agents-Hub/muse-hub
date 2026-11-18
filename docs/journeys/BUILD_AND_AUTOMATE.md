# Build and automate

Bring a project, a concrete problem and the tools you use. Choose a specialist, work through a reproducible example, then carry a clear result into your own workflow.

## 1. Choose the specialist for the job

Start with [Software Engineer](../../presets/software-engineer/INSTALL.md) for a code change or [Automation Engineer](../../presets/automation-engineer/INSTALL.md) for a repeated process. Download its ZIP, extract it and open `START_HERE.md` to configure the assistant and its three subchats.

For a software problem:

```text
Use the Software Engineer guide on [PROJECT]. Reproduce [PROBLEM], identify
the cause, make the smallest maintainable repair and run the relevant
regression checks. Show the changed files, test results and anything that
still needs attention.
```

For an automation:

```text
Use the Automation Engineer guide for [REPEATED TASK]. Define its trigger,
inputs, target service and expected result. Work through a small example,
including how to recognize a completed action and recover an interrupted
reply. Show the decisions I need to make before using it with my real work.
```

## 2. Choose your browser, computer or terminal route

Have more work than capacity? Use the [Project Prioritization calculator](../../collections/muse-starters-v1/skills/project-prioritization/PRIORITIZE.md) with your task estimates and resource budgets. It compares RICE scores and includes prerequisite work before choosing a feasible batch. The Coordinator download includes the calculator, guide and sample backlog.

[Muse's shared cloud computer and browser](https://muse.ai/) can handle web work. [Muse for Mac](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) can work with Mac apps using the permissions you grant.

For personal Muse chat from a terminal, follow the [muse-cli setup guide](../TERMINAL.md#chat-with-your-personal-muse). Once your connection is ready:

```sh
muse-cli --version
muse-cli status
muse-cli threads
muse-cli history --limit 5
muse-cli chat
```

`status` shows the connected account, `threads` lists Main and side chats, and `chat` starts an interactive conversation. Use the personal Muse command, `muse-cli`, for this route.

Explore [desktop and computer tools](https://atlas-origins.github.io/muse-ai-agent-presets/public/index.html?route=desktop) or [terminal projects](https://atlas-origins.github.io/muse-ai-agent-presets/public/index.html?route=cli) when you need another connection method. Each project links to its publisher's setup instructions.

## 3. Try a reproducible repair

The Hub's engineering example creates a temporary project, reproduces a failure and checks a focused repair. Use Python 3.12+ and Git from the toolkit root; the [terminal guide](../TERMINAL.md#run-muse-hub-tools) covers checkout setup.

Choose a new absolute output folder to keep the example's reports and candidate for review.

**macOS or Linux:**

```sh
PYTHONPATH=src python3 -B examples/software_engineer_workflow_demo.py --to "$HOME/muse-repair-demo"
```

**Windows PowerShell:**

```powershell
$env:PYTHONPATH = "src"
python -B examples/software_engineer_workflow_demo.py --to "$HOME/muse-repair-demo"
```

The report shows the initial failure followed by **four passing repair tests** and the saved candidate. Read those results, then use the handoff step below for a separate review. [Engineering workflows](../WORKFLOWS.md#engineering-reproduce-repair-review) covers the wider workflow.

For an automation example with its own supplied inputs, run:

```sh
python -B tools/muse_collection.py workflow-demo automation-readiness
```

This reviews the workflow's dependencies, declared approvals and expected results. Use `python3` where appropriate. The [specialist tool guide](../collection/SPECIALIST_QUICKSTART.md) shows how to run the other tools and supply your own inputs.

### Check a web app in the browser

Start with the [HTML source checker](../../collections/muse-starters-v1/skills/accessible-ui/SOURCE_CHECK.md) included in the [Accessible UI download](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.4.0/muse-skill-accessible-ui-v1.4.0.zip). Extract the ZIP and run its included example from that folder with Python 3.10 or newer:

```sh
python -B tools/accessibility_check.py --input skills/accessible-ui/examples/clean.html
```

Replace the input path with your own HTML page to check its source. Add `--format text` for a readable report. Follow the source check with keyboard, focus, zoom and rendered-state review of the task.

For reusable browser testing examples, explore Anthropic's [Web Application Testing guide](https://github.com/anthropics/skills/tree/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/webapp-testing). It uses Python, Playwright and an installed browser to inspect pages, exercise interactions and capture screenshots. The linked revision includes its [Apache 2.0 license](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/webapp-testing/LICENSE.txt).

Start your application with its own documented command. Check the page title or a distinctive element to confirm you reached the intended app, then wait for the specific state the task needs. Give each check a bounded timeout. Exercise the changed flow and one unaffected flow, and save the results with the change you reviewed.

## 4. Connect the service your work needs

Browse [development and infrastructure connectors](../connectors/CATALOG.md#development-and-infrastructure) for code hosting, cloud services and monitoring. [Work and productivity connectors](../connectors/CATALOG.md#work-and-productivity) include project tracking and team communication.

Follow the selected service's setup, choose the intended account and operations, and try a small check. Keep the original issue, task or operation link with your work so you can inspect its result later.

For recurring work, use [Muse's scheduled-task controls](https://www.meta.com/help/superintelligence/1484325780075655/): specify the task, interval and time zone, confirm its schedule, then check **Upcoming**. Update or cancel that existing task when the workflow changes.

## 5. Hand the result to a reviewer

[Family Link](../FAMILY_LINK.md) helps prepare the context a receiving specialist needs. Try:

```text
Prepare a handoff for [REVIEWER ROLE]. Include the original request, the
source files and revision, the changes, the test results and the questions
the reviewer should answer. Define what a complete review should return.
```

Review the handoff and share it through your chosen connection. Ask the reviewer to identify defects, explain the checks they performed and point to the result you should inspect. Keep their response with the original task.

## Finish with a result you can use

- The original problem has a reproducible example.
- The change has relevant passing checks and a saved result.
- The service account and target are the ones you intended.
- The review addresses the actual files and revision you delivered.

Use the same sequence on your project: reproduce, repair, check and review. For an interrupted service action, inspect its original status before trying it again.

[Muse Hub](../../README.md) · [Organize your day](ORGANIZE_YOUR_DAY.md) · [Create something](CREATE_SOMETHING.md)
