---
name: zoho-crm-connector
description: "Customer relationship management software"
---

# Zoho CRM for Muse

Customer relationship management software

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Zoho CRM**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.{location}/oauth/v2/auth>
- Token endpoint: <https://accounts.{location}/oauth/v2/token>
- **Location** (`location`): The location of your Zoho CRM account

Provider scopes: `ZohoCRM.bulk.ALL`, `ZohoCRM.bulk.backup.ALL`, `ZohoCRM.modules.ALL`, `ZohoCRM.org.ALL`, `ZohoCRM.settings.ALL`, `ZohoCRM.users.ALL`, `ZohoFiles.files.ALL`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/index.ts).

## Actions

### Add Note

Adds a note to a record.

| Input | What to provide | Required |
| --- | --- | --- |
| `module` | Module | See action definition |
| `record_id` | Record_Id | See action definition |
| `title` | Title | Optional |
| `content` | Content | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/actions/add-note.ts).

### Convert Lead

Converts a lead into a contact and account, and optionally a deal.

| Input | What to provide | Required |
| --- | --- | --- |
| `lead_id` | Lead_Id | See action definition |
| `account_id` | Account_Id | See action definition |
| `contact_id` | Contact_Id | See action definition |
| `overwrite` | Move the existing contact to the given account. | Optional |
| `assign_to` | Assign_To | See action definition |
| `notify_lead_owner` | Notify Lead Owner | Optional |
| `notify_new_entity_owner` | Notify New Owner | Optional |
| `create_deal` | Create a Deal | Optional |
| `deal_name` | Deal Name | Optional |
| `deal_stage` | A Stage picklist value of your org, e.g. "Qualification". | Optional |
| `deal_closing_date` | Date as yyyy-MM-dd, e.g. 2026-12-31. | Optional |
| `deal_amount` | Deal Amount | Optional |
| `deal_pipeline` | Required when your org uses pipelines, e.g. "Standard (Standard)". | Optional |
| `deal_extra` | Other Deal Fields (JSON) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/actions/convert-lead.ts).

### Create or Update Record

Updates the record that matches on the duplicate-check fields, or creates it if none matches.

| Input | What to provide | Required |
| --- | --- | --- |
| `module` | Module | See action definition |
| `duplicate_check_fields` | Duplicate_Check_Fields | See action definition |
| `fields` | Fields | See action definition |
| `additional_fields` | Additional_Fields | See action definition |
| `skip_automation` | Skip All Automation | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/actions/upsert-record.ts).

### Create Record

Creates a record in any module, including custom fields.

| Input | What to provide | Required |
| --- | --- | --- |
| `module` | Module | See action definition |
| `fields` | Fields | See action definition |
| `additional_fields` | Additional_Fields | See action definition |
| `triggers` | Empty runs Zoho's default workflows; pick some to run only those. | Optional |
| `skip_automation` | Run no workflow, approval or blueprint for this record. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/actions/create-record.ts).

### Delete Record

Deletes a record (it moves to the Zoho CRM Recycle Bin).

| Input | What to provide | Required |
| --- | --- | --- |
| `module` | Module | See action definition |
| `record_id` | Record_Id | See action definition |
| `run_workflows` | Run delete workflows configured in Zoho (Zoho default: on). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/actions/delete-record.ts).

### Get Record

Gets a record by id from any module, with all its fields.

| Input | What to provide | Required |
| --- | --- | --- |
| `module` | Module | See action definition |
| `record_id` | Record_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/actions/get-record.ts).

### Read file

Download a file content from Zoho CRM. e.g.: a Backup File

| Input | What to provide | Required |
| --- | --- | --- |
| `url` | Full https URL on your Zoho API host (/crm/...) or download host. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/actions/read-file.ts).

### Update Record

Updates fields of a record in any module. Fields left empty are not changed.

| Input | What to provide | Required |
| --- | --- | --- |
| `module` | Module | See action definition |
| `record_id` | Record_Id | See action definition |
| `fields` | Fields | See action definition |
| `clear_fields` | Field API names to set to empty (e.g. "Phone", "Custom_Field__c"). | Optional |
| `additional_fields` | Additional_Fields | See action definition |
| `skip_automation` | Run no workflow, approval or blueprint for this update. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/actions/update-record.ts).

## Events and recurring work

- **[New Contact](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/triggers/new-contact.ts)** — Triggers when a new contact is created
- **[New Record](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/triggers/new-record.ts)** — Triggers when a record is created in any module (custom fields included).
- **[Updated Record](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoho-crm/src/lib/triggers/updated-record.ts)** — Triggers when a record is modified in any module.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Zoho CRM to get record. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
