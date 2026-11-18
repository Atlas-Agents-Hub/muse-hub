# Build a local Space workspace

Build a local browser workspace with request tracking and saved SQLite state. This example combines a browser UI, loopback HTTP service, and the `space-starter/1` request state machine. Follow the launch steps below, then inspect the integration contract when extending it.

## Run the disposable offline example

From a source checkout with Python 3.12+:

```sh
python -B examples/space_starter.py
```

This creates an isolated temporary database, writes and reopens a notebook item, records a request, reserves a host operation, supplies a clearly synthetic callback, confirms duplicate suppression, refuses a late callback after cancellation, and preserves UNKNOWN on restart. It starts no listener, cron, model, provider job or notification.

## Open the local fullstack example

Create an owner-protected directory first, then pass a new absolute database path in it:

```sh
python -B examples/space_starter.py --serve --database /absolute/owner-directory/space.db
```

On Windows use an absolute path in an owner-protected directory, for example `C:\example-owner\space.db`. The directory must already exist. Existing regular database files may be reopened; SQLite is unencrypted and this is not secure erasure or an OS sandbox.

The launcher prints a loopback URL and a new random local-session token. Open the URL on **that same computer** and paste the token into the page. The token is not put in a URL, cookie or browser persistent storage. Reloading the page requires the token again. A new launcher session creates a new token. Close the foreground launcher with Ctrl+C. Keep this local listener on the same computer; use an appropriately authenticated host when building a shared deployment.

The browser can read local records, create/edit notes, explicitly enable/disable local requests, queue intentions, cancel requests and refresh receipts. Request handling is OFF by default. Enabling it does not connect a model or execute queued prompts. The layout supports narrow browser windows. Open the local URL on the computer running the server.

## Host adapter boundary

The host supplies a fresh `CompanionScope` through the `authority` callable on each operation. Constructing a scope is not authentication. Never derive owner authority from request JSON, URL parameters or a browser claim.

`SpaceCompanion` exposes:

| Operation | Local behavior |
|---|---|
| `configure` | Owner-present policy change with expected revision; default OFF |
| `request` | Stores a bounded prompt and stable request ID; conflicting reuse is refused |
| `claim` | Atomically records one operation ID and expiry before returning an intent; does not dispatch |
| `callback` | Requires a separately injected verifier, exact request hash/operation binding and unique event ID |
| `cancel` | Keeps terminal cancellation; does not prove a remote provider stopped |
| `expire` | Explicit foreground transition of expired claims to UNKNOWN; never reissues |
| `snapshot` | Read-only scoped state, without taking or dispatching work |

Host sequence: authenticate owner and authorization; configure explicit opt-in; reserve with `claim`; perform the permitted operation through the original provider; authenticate the provider's callback and binding; commit its receipt with `callback`; read original recipient/provider state separately. A claimed row does not prove a provider call happened. The returned `provider_dispatched` and `native_installed` fields remain false because this adapter does not attest those claims.

Interrupted claims stay dispatching until the foreground host calls `expire`. UNKNOWN records cannot be reclaimed automatically. Resolve actual remote outcomes at their original provider; this example deliberately does not provide a generic retry or force-success button. A cancellation is local intent, not proof that external work was cancelled. Acknowledged callbacks replay idempotently; changed event content, late callbacks and mismatched request bindings are refused.

**Neither claim nor callback is exposed to the browser HTTP API.** A production integration must inject an actual verifier; the sample's always-true verifier exists only inside its disposable synthetic demonstration. Browser messages and model text cannot act as callback authority.

## Requirements and deployment

Use Python 3.12+ and a browser on the same computer. The example uses Python's standard library and plain HTML, CSS, and JavaScript. `space-starter/1` defines the request operations above, and PersonalCompanion provides scoped local storage.

For a shared application, connect the current host's documented account, authorization, and callback interfaces. Match the installed SDK version and test the complete request and recovery path before using real task data.

The standard-library HTTP server is for local development, not production. The example restricts its bind address, host/origin, authorization token, content type, JSON keys and request size; denies CORS; sets a restrictive content security policy; avoids HTML injection and logs no session token. These checks are not a replacement for a production framework, TLS, operating-system access controls, provider authentication, rate limits or multi-user isolation.

## Verification

```sh
PYTHONPATH=src python -B -m unittest discover -s tests -p 'test_space_*.py' -v
python -B examples/space_starter.py
```

For PowerShell set `$env:PYTHONPATH='src'` before invoking unittest. Tests include actual disposable loopback HTTP requests, persistent SQLite state, wrong-owner/origin/token refusal, restart, concurrent claims, duplicates, invalid callbacks, cancellation, timeout and source-bound limitations. Browser evidence must be captured from actual rendered UI, not inferred from these assertions. Only run disposable test data.

Authoritative implementation references: [Python HTTP server limitations](https://docs.python.org/3.12/library/http.server.html) and [SQLite transactions and parameter binding](https://docs.python.org/3.12/library/sqlite3.html). All included code and UI are first-party source.
