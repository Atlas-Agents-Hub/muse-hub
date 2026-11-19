# Muse Planner — tasks, projects, and routines in one Space

Capture an idea, turn it into a project, choose the next action, and keep the result. Muse Planner brings your inbox, projects, daily routines, weekly review, notes, and calendar into a full-stack Muse Space with persistent SQLite storage.

## What you can do

| View | Your result |
| --- | --- |
| Today | See the next actions, priorities, routines, and scheduled work that matter today. |
| Inbox | Capture ideas quickly, then clarify and move them into the right place. |
| Projects | Define a successful outcome and keep its next actions together. |
| Future | Maintain daily and weekly checklists, dated reminders, and scheduled work. |
| Week | View connected calendars and create focus blocks in your chosen calendar. |
| Someday | Keep ideas worth revisiting without filling today's list. |
| Reference | Save notes and useful links alongside your work. |
| Done | Review completed work by completion date and reopen an item when needed. |

Use client or workspace names to filter related work. Copy an item's reference into a Muse conversation so you and your specialist can discuss the same task. Export a portable JSON backup whenever you want to save or move the workspace.

## Create your Muse Space

1. Ask Muse to create a new **TypeScript Space** named **Muse Planner**. Give it the contents of this app folder, including `space.json`, `client/`, `server/`, `drizzle/`, `scripts/`, and the package files. Use a fresh Space workspace and choose a unique slug if you already have a planner.
2. In that Space workspace, prepare the SDK supplied by the Muse host, then install the locked dependencies:

   ```bash
   bun run sdk:prepare
   bun install --frozen-lockfile --ignore-scripts
   ```

   The SDK helper copies the host's `space-sdk.tgz` into the project's `.sdk` folder. A host with a different package location can provide it explicitly:

   ```bash
   bun run sdk:prepare /path/to/space-sdk.tgz
   ```

3. Have Muse apply the SQL migrations in `drizzle/` in journal order and build the Space through its normal Space builder. `space.json` opens `client/dist/index.html`; the action bundle is `server/dist/actions.js`. Keep the host-managed build entry in `client/build.mjs` intact.
4. Open the Space. Create an inbox item, a project, and a next action. Add one daily routine in **Future**, check it, reopen the Space, and confirm your work is there.
5. Use **Export** to download your first workspace backup.

A useful first request:

> Set up Muse Planner for my current projects. Help me capture the loose tasks in Inbox, define an outcome for each project, choose a small next action, and create a weekly review routine. Use my preferred client and workspace names.

The planner starts with an empty workspace. Calendar setup is optional; capture, projects, routines, notes, reminders, and backups are ready first.

## Run a local preview

Use **Bun 1.3.10** and the Muse host's SDK package. From this folder:

```bash
bun run sdk:prepare /path/to/space-sdk.tgz
bun install --frozen-lockfile --ignore-scripts
bun run verify
bun run serve:standalone
```

Open the loopback address printed in the terminal. The default address is `http://127.0.0.1:8479/`. Your data is stored in `app.db` beside this README; the preview applies pending migrations when it starts.

Choose a different database or port when you want another workspace:

```bash
GTD_DB=/path/to/personal-planner.db PORT=8480 bun run serve:standalone
```

In PowerShell:

```powershell
$env:GTD_DB = 'C:\Workspaces\personal-planner.db'
$env:PORT = '8480'
bun run serve:standalone
```

The local preview uses `build:standalone`. Muse's Space builder uses `build:client`. Both use the same client source and SDK; the host owns its native build entry.

## Connect calendars with your own labels

Connect Google Calendar through Muse, then set the server environment variable `GTD_CALENDARS_JSON` for this Space. Enable only the calendars you want:

```json
{
  "primary": { "id": "primary", "label": "My schedule" },
  "intent": { "id": "YOUR_FOCUS_CALENDAR_ID", "label": "Writing blocks" },
  "shared": { "id": "YOUR_SHARED_CALENDAR_ID", "label": "Family calendar" }
}
```

| Key | How Planner uses it |
| --- | --- |
| `primary` | Read your schedule and display busy periods. |
| `intent` | Create, edit, and delete focus blocks when you use the Week editor. |
| `shared` | Read another calendar, such as a family, team, or project schedule. |

Calendar account IDs stay on the server. The page receives your labels and event details. Times display in the browser's local time zone. The optional adapter invokes the Muse host's `hatch_gws_cli` through a fixed argument vector; each process has a six-second limit and bounded output. A refresh follows up to four pages per calendar and retains the last complete schedule if a pull fails.

To remove a calendar from this Space, remove its entry from the environment setting and restart its runtime. The **Calendars** control in Week lets you show or hide connected calendars without changing their configuration.

## Back up and restore your work

**Export** downloads `muse-planner-YYYY-MM-DD.json`, containing projects, linked tasks, clients, notes, reminders, scheduled items, daily and weekly routines, their recorded results, and visibility preferences. The backup supports up to **10,000 rows** and **4 MiB**. Calendar event caches and account configuration are refreshed from the connected service.

**Import** opens a backup file and asks you to confirm replacing the current workspace. Planner validates the file, restores all rows in one transaction, and rejects the restore if another change arrived while you were reviewing it. A failed restore keeps the current workspace intact. Export your current work first when you want to keep both versions.

## Work with a Muse Hub specialist

- **Coordinator:** turn an outcome into projects, next actions, review dates, and a realistic weekly plan.
- **Research Evaluator:** capture questions in Inbox, keep source links in Reference, and track the next investigation.
- **Data Engineering & Database Architect:** plan a data delivery, keep validation tasks with the project, and record handoff notes.
- **Creative Studio:** turn a brief into drafting and review tasks, then reserve focus blocks for the work.
- **Learning Coach:** organize a study project, capture open questions, and track daily practice and weekly review.
- **Personal Companion:** build routines and reminders around your priorities, then review what helped.

Start by giving your specialist the project outcome and the copied item reference. Ask for a small next action with a saved or checkable result.

## Package structure

| Path | Purpose |
| --- | --- |
| `client/src/` | Responsive workspace interface, typed RPC client, and styles. |
| `server/src/actions.ts` | Project, task, note, calendar, and routine actions. |
| `server/src/backup.ts` | Portable backups and transactional restore. |
| `server/src/privileged.ts` | Optional calendar integration and private configuration. |
| `server/src/schema.ts` | Drizzle storage model. |
| `drizzle/` | Ordered migrations for a new Space database. |
| `scripts/` | SDK preparation, migrations, and loopback preview. |
| `tests/` and `server/tests/` | Browser, HTTP, persistence, concurrency, and adapter checks. |
| `client/tests/` | Mounted interface regression checks. |

`bun run verify` runs TypeScript checks, server and mounted UI tests, both local bundles, and the preview HTTP checks. For a complete browser run with installed Chrome and Node 22+, use a new evidence directory:

```bash
node tests/browser-planner.cjs /path/to/bun /path/to/chrome /path/to/new-planner-evidence
```

The browser runner creates its own preview database and profile, exercises the user journeys, saves screenshots and a JSON report, and closes only the processes it started.
