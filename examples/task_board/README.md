# Muse Task Board

A calm workspace for the next thing you want to do. Add cards, move them through **To do → In progress → Done**, keep your place across restarts, and export a portable copy of the board.

## Open your board

Use Python 3.12+ and a browser. Create a private working directory, then launch from the repository root:

```sh
python -B examples/task_board/run.py --serve --database /absolute/working-directory/board.db
```

On Windows, use an absolute database path such as `C:\my-work\board.db`. The containing directory must already exist.

Open the printed address on the same computer and enter the session key. Use the same database path when reopening the board. Cards save to SQLite after each change.

- **Add a card:** write one useful action, a little context, and its priority.
- **Move it:** drag the handle or use the card’s status menu. The arrow moves a card earlier in its column.
- **Refine it:** choose Edit to change a card’s title, context or priority. Save card keeps its place and status; Cancel edit keeps the saved version.
- **Make room:** remove a card when you no longer need it. Undo removal restores the card and its original position until your next saved board change or refresh.
- **Take a copy:** Export board downloads JSON. Import cards merges a board into the current one and keeps existing cards.
- **Work with Muse:** Queue a board plan. The request carries the selected cards and asks for three concrete next actions. Results appear beside the board as the host returns them.

The board supports 24 cards and 7,500 characters of saved board content. Export completed work, then remove finished cards to make room for your next project.

## Run the complete example

```sh
python -B examples/task_board/run.py
```

The example saves three cards, reopens them, queues a plan, computes next actions from the actual board, stores a result through the Space request contract, and reads it after reopening. It also checks that repeating the result callback keeps the same revision.

## Connect the request to your assistant

The board uses the existing [`space-starter/1` contract](../../docs/spaces/OPTIONAL_SPACE_STARTER.md). A `muse-board-plan/v1` request contains the task plus each card’s ID, title, status, and priority. The host claims the request, supplies the selected assistant with that prompt, and returns its result through the existing authenticated callback path. The browser displays the saved request state and result.

Use this result shape for a structured next-action list:

```json
{
  "schema": "muse-board-result/v1",
  "actions": [
    {"card_id": "brief", "action": "Finish the project brief", "priority": "high"}
  ]
}
```

The notebook stores the board under `muse-task-board`; expected revisions prevent one window from overwriting another window’s changes. The launcher reuses Muse Hub’s session checks, scoped storage, request queue, and callback contract. The board is also small enough to use as a starting point for a hosted Muse Space: keep its UI and data contract, and connect the host’s documented storage and authentication adapters.

## Build on it

The interface supports dragging and keyboard-accessible controls, with all assets included. Adapt the layout, card labels and planning prompt to the kind of project you want to organize.

Useful next variations include a reading queue, a research board, a lesson plan, and a household project board. Keep the same card schema, saved revisions, export format, and request/result flow when adapting the presentation.
