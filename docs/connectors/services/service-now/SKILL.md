---
name: service-now-connector
description: "Enterprise IT service management platform for incident, change, and service request management"
---

# ServiceNow for Muse

Enterprise IT service management platform for incident, change, and service request management

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **ServiceNow**.
2. Configure **Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Instance URL** (`instanceUrl`): Your ServiceNow instance URL without trailing slash (e.g., https://dev12345.service-now.com)
- **Username** (`username`): Your ServiceNow username (not email)
- **Password** (`password`): Your ServiceNow password (not API token)

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/index.ts).

## Actions

### Add Comment or Work Note

Append a customer-visible comment or an internal work note to a record (incident, request, problem, change, etc.)

| Input | What to provide | Required |
| --- | --- | --- |
| `table` | Table | See action definition |
| `record` | Record | See action definition |
| `manual_sys_id` | Enter the sys_id directly if not found in dropdown | Optional |
| `comment_type` | Customer-visible comment or internal work note | Yes |
| `comment` | The text to append to the record | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/actions/add-comment.ts).

### Find File

List or download file attachments from a record

| Input | What to provide | Required |
| --- | --- | --- |
| `action_type` | List attachments or download a file | Yes |
| `table` | Table | See action definition |
| `record` | Record | See action definition |
| `manual_sys_id` | Record sys_id (for listing attachments) | Optional |
| `filename` | Filter attachments by filename (optional) | Optional |
| `attachment_sys_id` | Attachment sys_id to download | Optional |
| `accept_type` | File type to accept when downloading | Optional |
| `return_format` | Format for returned file data | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/actions/find-file.ts).

### Find Records

Search for records in a table using a query

| Input | What to provide | Required |
| --- | --- | --- |
| `table` | Table | See action definition |
| `query` | Encoded query string (e.g., state=1^priority=1) | Yes |
| `limit` | Maximum records to return | Optional |
| `fields` | Specific fields to include in response (optional) | Optional |
| `sysparm_display_value` | How to format the response data | Optional |
| `sysparm_exclude_reference_link` | Exclude API links for reference fields | Optional |
| `sysparm_query_no_domain` | Include records from all domains | Optional |
| `sysparm_view` | View context for returned fields | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/actions/find-record.ts).

### Get Catalog Item

Retrieve full details of a catalog item including its variable definitions. Use this before "Submit Catalog Request" to discover the variables expected by the item.

| Input | What to provide | Required |
| --- | --- | --- |
| `item_sys_id` | Item_Sys_Id | See action definition |
| `manual_item_sys_id` | Provide the catalog item sys_id directly if it is not in the dropdown | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/actions/get-catalog-item.ts).

### Get Knowledge Article

Retrieve the full content of a knowledge article by sys_id

| Input | What to provide | Required |
| --- | --- | --- |
| `article_sys_id` | sys_id of the article. Use "Search Knowledge Articles" first if you only have a KB number. | Yes |
| `update_view` | Whether to increment the article view counter when fetching | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/actions/get-knowledge-article.ts).

### Get Record

Retrieve a specific record by its ID

| Input | What to provide | Required |
| --- | --- | --- |
| `table` | Table | See action definition |
| `record` | Record | See action definition |
| `manual_sys_id` | Enter the sys_id directly if not found in dropdown | Optional |
| `sysparm_display_value` | How to format the response data | Optional |
| `sysparm_exclude_reference_link` | Exclude API links for reference fields | Optional |
| `sysparm_fields` | Specific fields to include in response (optional) | Optional |
| `sysparm_query_no_domain` | Include records from all domains | Optional |
| `sysparm_view` | View context for returned fields | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/actions/get-record.ts).

### Search Knowledge Articles

Search published knowledge base articles using free text. Requires the Knowledge API plugin to be active.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Free-text search query | Optional |
| `kb` | Optional. Limit search to a specific knowledge base. | Optional |
| `language` | Optional ISO language code (e.g., en, de, fr) | Optional |
| `limit` | Maximum number of articles to return (1-100) | Optional |
| `offset` | Number of articles to skip for pagination | Optional |
| `fields` | Optional list of article field names to include in the response | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/actions/search-knowledge-articles.ts).

### Send Email

Send an email through your ServiceNow instance using the Email API. Requires the email outbound capability to be configured.

| Input | What to provide | Required |
| --- | --- | --- |
| `to` | One or more recipient email addresses | Yes |
| `subject` | Email subject line | Yes |
| `body` | Email body. HTML is supported by ServiceNow. | Yes |
| `from` | Optional sender address. Defaults to the instance email-from setting. | Optional |
| `cc` | Optional CC recipients | Optional |
| `bcc` | Optional BCC recipients | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/actions/send-email.ts).

## Events and recurring work

- **[New Comment or Work Note](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/triggers/new-comment.ts)** — Triggers when a new comment or work note is added to a record in the selected table
- **[New Record](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/triggers/new-record.ts)** — Triggers when a new record is created in a table
- **[Updated Record](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/service-now/src/lib/triggers/updated-record.ts)** — Triggers when a record is updated in a table

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use ServiceNow to find file. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
