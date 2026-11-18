---
name: pinterest-connector
description: "Pinterest: find pin by keyword, get board, get pin."
---

# Pinterest for Muse

Pinterest: find pin by keyword, get board, get pin.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Pinterest**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://www.pinterest.com/oauth/>
- Token endpoint: <https://api.pinterest.com/v5/oauth/token>

Provider scopes: `ads:read`, `boards:read`, `boards:read_secret`, `boards:write`, `pins:read`, `pins:read_secret`, `pins:write`, `user_accounts:read`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/index.ts).

## Actions

### Find Pin by Keyword

Search for Pins using title, description, or keywords.

| Input | What to provide | Required |
| --- | --- | --- |
| `ad_account_id` | Ad_Account_Id | See action definition |
| `query` | Words in the title, description or tags, or comma-separated Pin IDs. | Yes |
| `bookmark` | Bookmark from a previous run to continue where it stopped. | Optional |
| `max_results` | Never returns more than this many Pins. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/actions/find-pin.ts).

### Get Board

Read a single board by its id.

| Input | What to provide | Required |
| --- | --- | --- |
| `board_id` | Numeric board id, as returned by List Boards. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/actions/get-board.ts).

### Get Pin

Read a single Pin by its id.

| Input | What to provide | Required |
| --- | --- | --- |
| `pin_id` | Numeric pin id, as returned by List Pins or Search Pins. | Yes |
| `pin_metrics` | Return 90-day and lifetime metrics alongside the Pin. Total comments and reactions are lifetime-only. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/actions/get-pin.ts).

### List Boards

List the boards owned by the connected Pinterest account.

| Input | What to provide | Required |
| --- | --- | --- |
| `privacy` | Return only boards with this privacy setting. Omit to return all of them. | Optional |
| `page_size` | Boards per page (1-250, Pinterest defaults to 25). | Optional |
| `bookmark` | Opaque cursor returned by a previous call; omit to read the first page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/actions/list-boards.ts).

### List Followers

List the accounts following the connected account.

| Input | What to provide | Required |
| --- | --- | --- |
| `page_size` | Followers per page (1-250, Pinterest defaults to 25). | Optional |
| `bookmark` | Opaque cursor returned by a previous call; omit to read the first page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/actions/list-followers.ts).

### List Pins

List the Pins owned by the connected Pinterest account.

| Input | What to provide | Required |
| --- | --- | --- |
| `pin_filter` | Restrict the results to a subset of the account Pins. | Optional |
| `page_size` | Pins per page (1-250, Pinterest defaults to 25). | Optional |
| `bookmark` | Opaque cursor returned by a previous call; omit to read the first page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/actions/list-pins.ts).

### Search Boards

Search the account's boards by text.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Text to match against board names and descriptions. | Yes |
| `bookmark` | Opaque cursor returned by a previous call; omit to read the first page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/actions/search-boards.ts).

### Search Pins

Search the account's Pins by text.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Text to match against Pin titles, descriptions and tags. Comma-separated pin ids also work. | Yes |
| `bookmark` | Opaque cursor returned by a previous call; omit to read the first page. | Optional |
| `max_results` | Return at most this many Pins, 1 to 250. Pinterest has no page-size parameter for Pin search, so further pages are followed until the count is reached. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/actions/search-pins.ts).

## Events and recurring work

- **[New Board](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/triggers/new-board.ts)** — Fires when a new board is created in the account.
- **[New Follower](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/triggers/new-follower.ts)** — Triggers when a user gains a new follower.
- **[New Pin on Board](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinterest/src/lib/triggers/new-pin-on-board.ts)** — Fires when a new Pin is added to a specific board.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Pinterest to find pin by keyword. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)

## Run a direct request

From the connector directory, inspect available requests with:

```console
python connector.py inspect pinterest
```

Available HTTP reads: `read-v5-user-account`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
