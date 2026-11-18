# Companion Home

Move between five rooms, keep notes where they belong, try the Studio's motion controls, and take a break with Signal Trail in the Arcade. Companion Home runs in your browser and stores room notes in a SQLite database you choose.

## Open Companion Home

Use a toolkit checkout and Python 3.12+. Choose a database path in an existing private directory outside the application folder:

```sh
python -B examples/space_starter.py --serve --companion-home --database "$HOME/companion-notes.sqlite3"
```

The command works in PowerShell, macOS Terminal, and Linux; use `python3` where appropriate. You can replace the example with another absolute path.

Open the **127.0.0.1 URL printed in your terminal** on the same computer. Keep that terminal running while using the application. The [terminal guide](TERMINAL.md) has more setup help.

## Explore the five rooms

The room selector takes you between Focus Room, Notebook, Garden, Arcade, and Studio. Each room has its own notebook view. Use the room buttons by mouse, touch, or keyboard. The layout adapts to narrow phone-sized browser windows and larger displays.

You can also open `examples/companion_home/index.html` for a quick tour of the rooms, Studio, and Arcade. Launch the command above when you want to save notebook entries.

## Use the real local Notebook

Choose **Notebook** and enter the session token printed by the current launch. Keep the token private; enter it only in the local page. It stays in the page's memory and is cleared when the page locks or closes.

Select a room, write a note, and choose **Save note**. Select a saved note to edit it or choose **Delete** and confirm. Notes support up to 8,000 Unicode characters, including emoji. The app checks the current revision so another open editor cannot silently overwrite your newer changes.

### When a save needs attention

If the response is interrupted, keep the draft and choose **Refresh saved notes** to inspect what was saved before making another change. If a newer revision exists, compare it with your draft before explicitly opening the saved note or starting a new one. The app displays an acknowledged write separately from a failed refresh so you can reconcile the result.

If the session is refused or changes scope, the page locks and clears its displayed notes, draft, and token. Reopen the correct local session and inspect its saved notes. The interface waits for that readback before allowing another write.

## Studio motion controls

Studio animates original geometric shapes through four poses. Use **Pause**, **Resume**, and **Next pose** to control the sequence. Reduced-motion settings prevent autoplay, and switching to a hidden tab pauses it.

## Signal Trail in the Arcade

Select the highlighted numbered tile by touch, click, or keys **1–4**. Use Escape or **Back to Focus** to leave the game. The browser saves the numeric seed, turn, and score so you can resume. Signal Trail is original MIT-licensed code; its [rights record](../examples/companion_home/arcade-rights.json) is included with the project.

## Stop, restart, and keep your notes

Press Ctrl+C in the terminal that started Companion Home. Restart with the same database path to reopen your notes, and use the new session token. **Lock Notebook** clears the current page while leaving the saved database intact.

Keep the database when updating or removing the application. SQLite stores readable local data, so protect its directory and backups. Deleting a note removes it from the current notebook view; use appropriate storage practices if you need physical data erasure.

## Developer reference

Companion Home uses the existing `space_server.make_server` and the `RoomNotebook` adapter over `PersonalCompanion` storage. The notebook mode exposes list, put, and forget operations with session, room, scope, and revision checks. The launcher enables it explicitly with `--companion-home`.

The example below checks notebook updates, restart, and restoration into a new empty store:

```sh
PYTHONPATH=src python3 -B examples/companion_home_notebook_demo.py
python -B scripts/run_source_test.py test_companion_home_h14_h17.py
```

On PowerShell, set `$env:PYTHONPATH = "src"` for the example. HTTP, launcher, and browser-client regressions are in `tests/test_companion_room_http.py`, `tests/test_companion_room_launcher.py`, and `tests/test_companion_room_client.py`. The client tests require Node.js.

[Get started](GETTING_STARTED.md) · [Daily Desk](spaces/DAILY_DESK.md) · [Personal Companion](../presets/personal-companion/INSTALL.md)
