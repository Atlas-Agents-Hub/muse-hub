# Build a local Space workspace

Build a local browser workspace with request tracking and saved SQLite state. This example combines a browser UI, loopback HTTP service, and the `space-starter/1` request state machine. Follow the launch steps below, then inspect the integration contract when extending it.

## Try the worked example

From a source checkout with Python 3.12+:

```sh
python -B examples/space_starter.py
```

The example uses a temporary database to save and reopen a note, record a request, and process a sample callback. It checks duplicate requests, cancellation, and recovery of an interrupted operation after restart.

## Open the workspace

Create an owner-protected directory first, then pass a new absolute database path in it:

```sh
python -B examples/space_starter.py --serve --database /absolute/owner-directory/space.db
```

On Windows use an absolute path in an owner-protected directory, for example `C:\example-owner\space.db`. The directory must already exist. Reopen an existing database by using its path. SQLite stores readable data, so protect the directory and its backups with your operating system's access controls.

The launcher prints a loopback URL and a new random local-session token. Open the URL on **that same computer** and paste the token into the page. The page keeps the token in memory for the current session. Reloading requires the token again. A new launcher session creates a new token. Close the foreground launcher with Ctrl+C. Keep this local listener on the same computer; use an appropriately authenticated host when building a shared deployment.

The browser can read local records, create/edit notes, explicitly enable/disable local requests, queue intentions, cancel requests and refresh receipts. Enable request handling when you want to queue work. A host adapter processes queued requests through the tools you configure. The layout supports narrow browser windows. Open the local URL on the computer running the server.

## Connect a host adapter

The host authenticates the user and supplies a fresh `CompanionScope` through the `authority` callback for each operation. Keep this callback separate from request JSON, URL parameters, and browser input.

`SpaceCompanion` exposes:

| Operation | Local behavior |
|---|---|
| `configure` | Owner-present policy change with expected revision; default OFF |
| `request` | Stores a bounded prompt and stable request ID; conflicting reuse is refused |
| `claim` | Reserves one operation ID and expiry for the host to execute |
| `callback` | Requires a separately injected verifier, exact request hash/operation binding and unique event ID |
| `cancel` | Marks the request cancelled; check the connected service to reconcile work already sent |
| `expire` | Marks an expired operation UNKNOWN for reconciliation |
| `snapshot` | Returns the current records within the user's scope |

The host authenticates the user, enables the selected requests, reserves an operation with `claim`, and performs it through the connected service. Verify the service callback and its operation ID, save the receipt with `callback`, and check the result in the original service.

After an interrupted operation, call `expire` and reconcile the UNKNOWN record against the original service before retrying. Check the service when cancelling work that has already been sent. Repeating an acknowledged callback returns its saved result; changed event content, late callbacks, and mismatched request IDs are refused.

The trusted host owns `claim` and `callback`; the browser API handles workspace operations. Supply a verifier for the real service when adding an integration. The worked example uses a test verifier for its sample callback.

## Requirements and deployment

Use Python 3.12+ and a browser on the same computer. The example uses Python's standard library and plain HTML, CSS, and JavaScript. `space-starter/1` defines the request operations above, and PersonalCompanion provides scoped local storage.

For a shared application, connect the current host's documented account, authorization, and callback interfaces. Match the installed SDK version and test the complete request and recovery path before using real task data.

Use the standard-library HTTP server for development on your computer. It checks the bind address, request origin, session token, content type, JSON fields, and size. For a shared deployment, use a production server with TLS, account authentication, rate limits, and user isolation, then test the complete request and recovery flow.

## Verification

```sh
PYTHONPATH=src python -B -m unittest discover -s tests -p 'test_space_*.py' -v
python -B examples/space_starter.py
```

For PowerShell, set `$env:PYTHONPATH = "src"` before invoking unittest. These checks use disposable data and cover HTTP requests, saved SQLite state, account and token checks, restart, concurrent requests, duplicate callbacks, cancellation, and timeout. Open the workspace to check the browser interactions as well.

Implementation references: [Python HTTP server limitations](https://docs.python.org/3.12/library/http.server.html) and [SQLite transactions and parameter binding](https://docs.python.org/3.12/library/sqlite3.html).
