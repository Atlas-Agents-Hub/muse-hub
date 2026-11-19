# Muse Task Board: turn a plan into progress

Give a project a clear next step. Muse Task Board keeps cards in **To do**, **In progress** and **Done**, with priorities, notes, saved progress and a portable export. Move a card by dragging it or using its status menu, then return to the same board when you resume.

Use it for a weekly plan, reading queue, research project, lesson plan or household project. Pair it with [Personal Companion](../../presets/personal-companion/INSTALL.md) for daily planning or [Coordinator](../../presets/coordinator/INSTALL.md) for projects with several moving parts.

## Open your board

Follow the [toolkit setup](../TERMINAL.md#run-muse-hub-tools) with Python 3.12 or later. From the toolkit root, run:

```sh
python -B examples/task_board/run.py --serve --database "$HOME/muse-task-board.sqlite"
```

The command works in PowerShell, macOS Terminal and Linux shells; use `python3` if that is your interpreter name. Choose an absolute database path in an existing private directory.

Open the address printed in the terminal on the same computer and enter the session key. Keep the terminal running while you work. Stop it with Ctrl+C, then reuse the same database path and enter the new session key to reopen your cards.

## Plan a useful first board

1. Add a card for each concrete action, with enough context to resume it later.
2. Choose a priority and move the first card into **In progress**.
3. Complete one action, move it to **Done**, and choose what comes next.
4. Use **Export board** to keep a JSON copy. **Import cards** merges cards into your current board while keeping the cards already there.

Start with this prompt for your Muse assistant:

```text
Turn this project into a task board: [PROJECT AND CURRENT NOTES].
Suggest a short card title, context, priority and starting status for each
action. Respect [TIME AND CONSTRAINTS]. End with the next three actions.
```

The board supports 24 cards and 7,500 characters of saved board content. Keep a project focused, and export completed work before starting another board.

## Connect planning to your assistant

**Queue a board plan** creates a request containing the selected cards. An assistant host claims that request, returns the next actions through the Space callback contract, and the board displays the saved result. The [integration example](../../examples/task_board/README.md#connect-the-request-to-your-assistant) supplies the request and result formats for connecting your assistant.

To try the complete save, reopen, plan and result flow with the included example:

```sh
python -B examples/task_board/run.py
```

## Make a Space of your own

The board combines a small interface, persistent card storage, an export format and the Muse Hub Space request contract. Its drag controls use [SortableJS](https://github.com/SortableJS/Sortable); keyboard and status controls provide another way to move cards. All interface assets are included in the toolkit.

Adapt the board into a reading list, research tracker or lesson planner. Keep the card IDs and saved revisions stable, then connect your host's documented storage, authentication and assistant adapters. The [Space starter](OPTIONAL_SPACE_STARTER.md) describes those connections; the [board source and examples](../../examples/task_board/README.md) provide the files to start from.

[Daily Desk](DAILY_DESK.md) · [Companion Home](../COMPANION_HOME.md) · [Organize your day](../journeys/ORGANIZE_YOUR_DAY.md) · [Muse Hub](../../README.md)
