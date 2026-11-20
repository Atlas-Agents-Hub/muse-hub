---
name: freshservice-connector
description: "IT service management software for ticketing, asset management, and IT operations."
---

# Freshservice for Muse

IT service management software for ticketing, asset management, and IT operations.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Freshservice**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Freshservice Domain** (`domain`): Your Freshservice subdomain (e.g., "mycompany" from mycompany.freshservice.com).
- **Api_Key** (`api_key`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/index.ts).

## Actions

### Add Note to Change

Adds a private or public note to an existing change request.

| Input | What to provide | Required |
| --- | --- | --- |
| `change_id` | Change_Id | See action definition |
| `body` | The content of the note. HTML is supported. | Yes |
| `private` | If checked, the note is only visible to agents. If unchecked, the requester can also see it. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/actions/add-note-to-change.ts).

### Add Note to Ticket

Adds a private or public note to an existing ticket.

| Input | What to provide | Required |
| --- | --- | --- |
| `ticket_id` | Ticket_Id | See action definition |
| `body` | The content of the note. HTML is supported. | Yes |
| `private` | If checked, the note is only visible to agents. If unchecked, the requester can also see it. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/actions/add-note-to-ticket.ts).

### Create Change

Creates a new change request in Freshservice.

| Input | What to provide | Required |
| --- | --- | --- |
| `subject` | The subject of the change. | Yes |
| `requester_id` | Requester_Id | See action definition |
| `description` | HTML content describing the change. | Optional |
| `agent_id` | Agent_Id | See action definition |
| `group_id` | Group_Id | See action definition |
| `department_id` | Department_Id | See action definition |
| `priority` | Priority | See action definition |
| `impact` | Impact | See action definition |
| `status` | Status | See action definition |
| `risk` | Risk | See action definition |
| `change_type` | Change_Type | See action definition |
| `planned_start_date` | Planned start date and time (ISO 8601, e.g. 2025-01-15T09:00:00Z). | Optional |
| `planned_end_date` | Planned end date and time (ISO 8601, e.g. 2025-01-15T17:00:00Z). | Optional |
| `category` | Category of the change. | Optional |
| `sub_category` | Sub-category of the change. | Optional |
| `item_category` | Item category of the change. | Optional |
| `custom_fields` | A JSON object of custom field names and values. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/actions/create-change.ts).

### Create Change Task

Creates a new task on a change request in Freshservice.

| Input | What to provide | Required |
| --- | --- | --- |
| `change_id` | Change_Id | See action definition |
| `title` | The title of the task. | Yes |
| `description` | Description of the task. | Optional |
| `agent_id` | Agent_Id | See action definition |
| `group_id` | Group_Id | See action definition |
| `status` | Status | See action definition |
| `due_date` | Task due date and time (ISO 8601, e.g. 2025-01-15T17:00:00Z). | Optional |
| `notify_before` | Time in seconds before the due date to send a reminder notification. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/actions/create-change-task.ts).

### Create Requester

Creates a new requester (end user) in Freshservice.

| Input | What to provide | Required |
| --- | --- | --- |
| `first_name` | The first name of the requester. | Yes |
| `primary_email` | The primary email address of the requester. | Yes |
| `last_name` | The last name of the requester. | Optional |
| `job_title` | The job title of the requester. | Optional |
| `phone` | The work phone number of the requester. | Optional |
| `mobile_phone_number` | The mobile phone number of the requester. | Optional |
| `department_id` | Department_Id | See action definition |
| `custom_fields` | A JSON object of custom field names and values. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/actions/create-requester.ts).

### Create Ticket

Creates a new ticket in Freshservice.

| Input | What to provide | Required |
| --- | --- | --- |
| `subject` | The subject of the ticket. | Yes |
| `description` | HTML content of the ticket. You can use basic HTML tags for formatting. | Yes |
| `requester_id` | Requester_Id | See action definition |
| `status` | Status | See action definition |
| `priority` | Priority | See action definition |
| `source` | Source | See action definition |
| `urgency` | Urgency | See action definition |
| `impact` | Impact | See action definition |
| `type` | The type of ticket (e.g., Incident, Service Request). | Optional |
| `responder_id` | Responder_Id | See action definition |
| `department_id` | Department_Id | See action definition |
| `group_id` | Group_Id | See action definition |
| `category` | The category of the ticket. | Optional |
| `sub_category` | The sub-category of the ticket. | Optional |
| `tags` | Tags to add to the ticket. | Optional |
| `custom_fields` | A JSON object of custom field names and values. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/actions/create-ticket.ts).

### Delete Change

Deletes a change request from Freshservice.

| Input | What to provide | Required |
| --- | --- | --- |
| `change_id` | Change_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/actions/delete-change.ts).

### Update Change

Updates an existing change request in Freshservice.

| Input | What to provide | Required |
| --- | --- | --- |
| `change_id` | Change_Id | See action definition |
| `subject` | New subject for the change. | Optional |
| `description` | HTML content describing the change. | Optional |
| `requester_id` | Requester_Id | See action definition |
| `agent_id` | Agent_Id | See action definition |
| `group_id` | Group_Id | See action definition |
| `department_id` | Department_Id | See action definition |
| `priority` | Priority | See action definition |
| `impact` | Impact | See action definition |
| `status` | Status | See action definition |
| `risk` | Risk | See action definition |
| `change_type` | Change_Type | See action definition |
| `planned_start_date` | Planned start date and time (ISO 8601, e.g. 2025-01-15T09:00:00Z). | Optional |
| `planned_end_date` | Planned end date and time (ISO 8601, e.g. 2025-01-15T17:00:00Z). | Optional |
| `category` | Category of the change. | Optional |
| `sub_category` | Sub-category of the change. | Optional |
| `item_category` | Item category of the change. | Optional |
| `custom_fields` | A JSON object of custom field names and values. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/actions/update-change.ts).

## Events and recurring work

- **[New Change](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/triggers/new-change.ts)** — Triggers when a new change request is created in Freshservice.
- **[New Change Task](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/triggers/new-change-task.ts)** — Triggers when a new task is created on a specific change request.
- **[New Requester](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshservice/src/lib/triggers/new-requester.ts)** — Triggers when a new requester (user) is created in Freshservice.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Freshservice to add note to change. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
