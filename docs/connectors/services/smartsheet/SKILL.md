---
name: smartsheet-connector
description: "Dynamic work execution platform for teams to plan, capture, manage, automate, and report on work at scale."
---

# Smartsheet for Muse

Dynamic work execution platform for teams to plan, capture, manage, automate, and report on work at scale.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Smartsheet**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/smartsheet/src/index.ts).

## Actions

### Add Row to Sheet

Adds new row to a sheet.

| Input | What to provide | Required |
| --- | --- | --- |
| `sheet_id` | Sheet_Id | See action definition |
| `cells` | Cells | See action definition |
| `location_type` | Add Row to Top or Bottom | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/smartsheet/src/lib/actions/add-row-to-sheet.ts).

### Attach File to Row

Adds a file attachment to a row.

| Input | What to provide | Required |
| --- | --- | --- |
| `sheet_id` | Sheet_Id | See action definition |
| `row_id` | Row_Id | See action definition |
| `attachment_type` | Type of attachment to add | Yes |
| `file` | The file to attach (required for FILE type) | Optional |
| `url` | The URL to attach (required for URL-based attachment types) | Optional |
| `attachment_name` | Name for the attachment (optional, will use file name or URL if not provided) | Optional |
| `attachment_sub_type` | Sub type for Google Drive and Egnyte attachments | Optional |
| `mime_type` | MIME type of the attachment (optional, auto-detected for files) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/smartsheet/src/lib/actions/attach-file-to-row.ts).

### Find Row

Finds rows in a specific sheet or across all accessible sheets using text queries with advanced filtering options.

| Input | What to provide | Required |
| --- | --- | --- |
| `search_scope` | Choose whether to search within a specific sheet or across all accessible sheets. | Yes |
| `sheet_id` | Sheet_Id | See action definition |
| `query` | Text to search for. Use double quotes for exact phrase matching (e.g., "project status") | Yes |
| `search_scopes` | Specify what types of content to search in (leave empty to search all) | Optional |
| `include_favorites` | Include information about which items are marked as favorites | Optional |
| `modified_since` | Only return results modified on or after this date/time | Optional |
| `max_results` | Maximum number of results to return (default: 50, max: 100) | Optional |
| `object_types_filter` | Only return results of specific object types (leave empty for all types) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/smartsheet/src/lib/actions/find-rows-by-query.ts).

### Find Sheet(s)

Fetches existings sheets matching provided filter criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `sheet_name` | Filter sheets by name (partial or exact match). Leave empty to list all sheets. | Optional |
| `exact_match` | When filtering by name, require exact match instead of partial match | Optional |
| `include_all` | If true, include all results without pagination (overrides page and page size) | Optional |
| `page` | Which page to return (defaults to 1, ignored if "Include All Results" is true) | Optional |
| `page_size` | Maximum number of items to return per page (defaults to 100, max 10000, ignored if "Include All Results" is true) | Optional |
| `access_api_level` | API access level for viewing and filtering permissions | Optional |
| `access_level_filter` | Only return sheets where you have specific access levels (leave empty for all) | Optional |
| `modified_since` | Only return sheets modified on or after this date/time | Optional |
| `include_sheet_version` | Include current version number of each sheet | Optional |
| `include_source_info` | Include information about the source (template/sheet) each sheet was created from | Optional |
| `numeric_dates` | Return dates as milliseconds since UNIX epoch instead of ISO strings | Optional |
| `created_date_range` | Filter sheets by creation date range | Optional |
| `sort_by` | How to sort the returned sheets | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/smartsheet/src/lib/actions/find-sheet-by-name.ts).

### List Row Attachments

Get all attachments for a specific row in a Smartsheet, including row and discussion-level attachments with comprehensive pagination and filtering options

| Input | What to provide | Required |
| --- | --- | --- |
| `sheet_id` | Sheet_Id | See action definition |
| `row_id` | Row_Id | See action definition |
| `include_all` | If true, include all results without pagination (overrides page and page size) | Optional |
| `page` | Which page to return (defaults to 1, ignored if "Include All Results" is true) | Optional |
| `page_size` | Maximum number of items to return per page (defaults to 100, max 10000, ignored if "Include All Results" is true) | Optional |
| `attachment_type_filter` | Only return attachments of specific types (leave empty for all types) | Optional |
| `parent_type_filter` | Only return attachments from specific parent types (leave empty for all) | Optional |
| `min_file_size_kb` | Only return files with size greater than or equal to this value (applies to FILE type only) | Optional |
| `max_file_size_kb` | Only return files with size less than or equal to this value (applies to FILE type only) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/smartsheet/src/lib/actions/find-attachment-by-row-id.ts).

### Update Row

Updates an existing row.

| Input | What to provide | Required |
| --- | --- | --- |
| `sheet_id` | Sheet_Id | See action definition |
| `row_id` | Row_Id | See action definition |
| `cells` | Cells | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/smartsheet/src/lib/actions/update-row.ts).

## Events and recurring work

- **[New Attachment Added](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/smartsheet/src/lib/triggers/new-attachment-trigger.ts)** — Triggers when a new attachment is added to a row or sheet.
- **[New Comment Added](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/smartsheet/src/lib/triggers/new-comment-trigger.ts)** — Triggers when a new comment is added to a discussion on a sheet.
- **[New Row Added](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/smartsheet/src/lib/triggers/new-row-trigger.ts)** — Triggers when a new row is added.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Smartsheet to find row. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

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
python connector.py inspect smartsheet
```

Available HTTP reads: `read-2-0-sheets`, `read-2-0-sheets-sheetid`, `read-2-0-sheets-sheetid-columns`, `read-2-0-sheets-sheetid-rows-rowid-attachments`, `read-2-0-webhooks`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
