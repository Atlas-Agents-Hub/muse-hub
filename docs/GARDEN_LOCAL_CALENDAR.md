# Garden observations and planning

Keep observations, planting dates, and seasonal plans together. Start with the [Garden Companion](../presets/garden-companion/INSTALL.md), give it your garden notes, and ask for a plan you can review. The toolkit also includes a Python calendar library for applications that need saved events and reviewed date changes.

## Try the calendar example

From the toolkit root with Python 3.12+:

```sh
PYTHONPATH=src python3 -B examples/garden_calendar_demo.py
```

In Windows PowerShell, set `$env:PYTHONPATH = "src"` and run `python -B examples/garden_calendar_demo.py`.

The example uses a temporary SQLite database and a fictional garden. It creates an event, proposes a two-day shift, reviews the exact change, applies the owner's decision, and reopens the saved result. Read its printed report to follow the sequence. The example removes its sample database when finished.

To run the same example from a separate folder, use the [portable Garden kit](kits/GARDEN_SOURCEKIT.md). Keep your real notes in your chosen workspace; the example is a demonstration, not the place to enter personal records.

## Review a calendar change

1. Read the current event and revision.
2. Prepare a proposal with the original date and requested shift.
3. Show the owner the before/after dates and any stale or expired records.
4. Apply the owner's decision to the complete batch.
5. Read the saved operation receipt before continuing.

The library updates a batch in one SQLite transaction. A stale event, cancelled event, or storage error rolls back the complete change. A proposal can cover 1–21 events and shift them by up to 30 days. Its default expiry is one hour.

## Save your own records in an application

Use `GardenCalendar(database, authority=host_resolver)` from [`garden_calendar.py`](../src/muse_presets/garden_calendar.py) with an absolute database path in an existing private directory. Store that database outside the application package and keep the same path when reopening it. SQLite stores readable local data, so protect the directory and back it up before moving or updating the application.

The host resolver must supply the current verified user, Space, garden, and actor scope on every operation. Keep it inside the trusted application; never construct account authority from browser JSON, a chat message, or a client-supplied ID. The example uses fictional scopes to exercise the API.

Owner sessions can create and cancel events and decide proposals. A scoped specialist can read events and propose changes. The application must preserve this separation when exposing the API. Event lists include an explicit `truncated` flag after the 100-record limit; show that flag when displaying a partial list.

Use a new database for a new integration. Review schema and storage compatibility before moving existing records. To connect a calendar or weather service, follow its [connector guide](connectors/README.md) and choose the required account and permissions.

## Recover after an interruption

Keep the original operation ID. Read `receipt()` and the current event revisions before retrying. Repeating the identical operation returns its saved receipt; changing the decision or request under the same ID produces `OPERATION_CONFLICT`. An `OUTCOME_UNKNOWN_RECONCILE_BY_OPERATION_ID` result requires checking the original outcome before another write.

Keep stale and expired findings visible for review. Do not silently replace an event with a newer timestamp or create a new operation ID to bypass an uncertain result.

## Developer checks

```sh
PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_garden_calendar.py -v
```

The library validates scope, revisions, paths, batch sizes, and operation IDs. It rejects user-controlled symlink and junction paths while recognizing the operating system's standard macOS directory aliases.

[Garden Companion](../presets/garden-companion/INSTALL.md) · [Portable kit](kits/GARDEN_SOURCEKIT.md) · [Setup and saved data](INSTALL_AND_PERSISTENCE.md)
