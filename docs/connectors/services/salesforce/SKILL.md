---
name: salesforce-connector
description: "CRM software solutions and enterprise cloud computing"
---

# Salesforce for Muse

CRM software solutions and enterprise cloud computing

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Salesforce**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://{environment}/services/oauth2/authorize>
- Token endpoint: <https://{environment}/services/oauth2/token>
- **Salesforce Domain** (`environment`): login.salesforce.com for production, test.salesforce.com for a sandbox, or your My Domain.

Provider scopes: `api`, `full`, `refresh_token`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/index.ts).

## Actions

### Add Contact to Campaign

Adds a contact to a campaign with a member status.

| Input | What to provide | Required |
| --- | --- | --- |
| `campaign_id` | Campaign_Id | See action definition |
| `contact_id` | Contact_Id | See action definition |
| `status` | Status | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/add-contact-to-campaign.ts).

### Add File to Record

Uploads a file and attaches it to an existing record.

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `record_id` | Record_Id | See action definition |
| `file` | File | Yes |
| `file_name` | Include the extension. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/add-file-to-record.ts).

### Add Lead to Campaign

Adds a lead to a campaign with a member status.

| Input | What to provide | Required |
| --- | --- | --- |
| `campaign_id` | Campaign_Id | See action definition |
| `lead_id` | Lead_Id | See action definition |
| `status` | Status | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/add-lead-to-campaign.ts).

### Batch Upsert

Creates or updates up to 200 records, matched on an external ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `external_field` | API name of the external ID field to match records on. | Yes |
| `records` | JSON with a records array. Each record needs attributes with its type. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/upsert-by-external-id.ts).

### Bulk Upsert

Creates or updates records from a CSV with a Bulk API job.

| Input | What to provide | Required |
| --- | --- | --- |
| `job_info` | Job_Info | Optional |
| `object` | Object | See action definition |
| `external_field` | API name of the external ID field to match records on. | Yes |
| `records` | CSV with a header row of field API names. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/upsert-by-external-id-bulk.ts).

### Create Case

Creates a case for a customer issue.

| Input | What to provide | Required |
| --- | --- | --- |
| `Subject` | Subject | Yes |
| `Description` | Description | Optional |
| `Status` | Status | See action definition |
| `Priority` | Priority | See action definition |
| `Origin` | Origin | See action definition |
| `AccountId` | Account Id | See action definition |
| `ContactId` | Contact Id | See action definition |
| `other_fields` | More fields as JSON, with Salesforce field API names as keys. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/create-case.ts).

### Create Contact

Creates a contact.

| Input | What to provide | Required |
| --- | --- | --- |
| `LastName` | Last Name | Yes |
| `FirstName` | First Name | Optional |
| `AccountId` | Account Id | See action definition |
| `Email` | Email | Optional |
| `Phone` | Phone | Optional |
| `Title` | Title | Optional |
| `other_fields` | More fields as JSON, with Salesforce field API names as keys. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/create-contact.ts).

### Create Lead

Creates a lead.

| Input | What to provide | Required |
| --- | --- | --- |
| `LastName` | Last Name | Yes |
| `Company` | Company | Yes |
| `FirstName` | First Name | Optional |
| `Email` | Email | Optional |
| `Phone` | Phone | Optional |
| `LeadSource` | Lead Source | See action definition |
| `other_fields` | More fields as JSON, with Salesforce field API names as keys. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/create-lead.ts).

### Create Legacy Attachment

Creates a classic attachment. For new work, use Add File to Record.

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `parent_id` | Parent_Id | See action definition |
| `file` | File | Yes |
| `file_name` | Include the extension. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/create-attachment.ts).

### Create Note

Creates a note on a record.

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `parent_id` | Parent_Id | See action definition |
| `Title` | Title | Yes |
| `Body` | Body | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/create-note.ts).

### Create Object (Advanced)

Create new object

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `data` | Select mapped object | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/create-new-object.ts).

### Create Opportunity

Creates an opportunity.

| Input | What to provide | Required |
| --- | --- | --- |
| `Name` | Name | Yes |
| `CloseDate` | The date the deal should close, as YYYY-MM-DD. | Yes |
| `StageName` | Stage Name | See action definition |
| `AccountId` | Account Id | See action definition |
| `Amount` | In your org's currency. | Optional |
| `other_fields` | More fields as JSON, with Salesforce field API names as keys. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/create-opportunity.ts).

### Create Record

Creates a record of any object.

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `data` | Field API names as keys, with the values to set. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/create-record.ts).

### Create Task

Creates a task.

| Input | What to provide | Required |
| --- | --- | --- |
| `Subject` | Subject | Yes |
| `OwnerId` | Owner Id | See action definition |
| `Status` | Status | See action definition |
| `Priority` | Priority | See action definition |
| `Description` | Description | Optional |
| `WhoId` | ID of the contact or lead, from its record URL or an earlier step. | Optional |
| `WhatId` | Account, case or other record ID, from its URL or an earlier step. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/create-task.ts).

### Delete Opportunity

Deletes an opportunity. It goes to the Recycle Bin.

| Input | What to provide | Required |
| --- | --- | --- |
| `recycle_info` | Recycle_Info | Optional |
| `opportunity_id` | Opportunity_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/delete-opportunity.ts).

### Delete Record

Deletes a record. It goes to the Recycle Bin.

| Input | What to provide | Required |
| --- | --- | --- |
| `recycle_info` | Recycle_Info | Optional |
| `object` | Object | See action definition |
| `record_id` | Record_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/delete-record.ts).

### Export Report

Exports a report as an Excel file.

| Input | What to provide | Required |
| --- | --- | --- |
| `report_id` | Report_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/export-report.ts).

### Find Child Records

Finds child records related to a parent record.

| Input | What to provide | Required |
| --- | --- | --- |
| `parent_object` | Parent_Object | See action definition |
| `parent_id` | Parent_Id | See action definition |
| `child_relationship` | Child_Relationship | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/find-child-records.ts).

### Find Record

Finds records where a field equals a value, up to 200.

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `field` | Field | See action definition |
| `search_value` | Matched exactly against the field. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/find-record.ts).

### Find Records by Query

Finds up to 200 records of an object that match SOQL conditions.

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `where_clause` | SOQL conditions to filter by, without the WHERE keyword. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/find-records-by-query.ts).

### Get Record Attachments

Lists the files and classic attachments on a record.

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `record_id` | Record_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/get-record-attachments.ts).

### Log Email

Records an email on a contact or lead. Salesforce does not send it.

| Input | What to provide | Required |
| --- | --- | --- |
| `delivery_warning` | Delivery_Warning | Optional |
| `recipientId` | Recipient Id | See action definition |
| `subject` | Subject | Yes |
| `body` | Plain text or HTML. | Yes |
| `relatedToId` | Account, case or other record ID, from its URL or an earlier step. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/send-email.ts).

### Run Query

Runs a SOQL query in Salesforce.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | A SOQL query. Returns up to 2,000 records. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/run-sf-query.ts).

### Run Report

Runs a report and returns its rows.

| Input | What to provide | Required |
| --- | --- | --- |
| `report_id` | Report_Id | See action definition |
| `filters` | JSON list of column, operator and value. Empty: the saved filters. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/run-report.ts).

### Update Contact

Updates a contact.

| Input | What to provide | Required |
| --- | --- | --- |
| `contact_id` | Contact_Id | See action definition |
| `changes_info` | Changes_Info | Optional |
| `FirstName` | First Name | Optional |
| `LastName` | Last Name | Optional |
| `AccountId` | Account Id | See action definition |
| `Email` | Email | Optional |
| `Phone` | Phone | Optional |
| `Title` | Title | Optional |
| `other_fields` | More fields as JSON, with Salesforce field API names as keys. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/update-contact.ts).

### Update Lead

Updates a lead.

| Input | What to provide | Required |
| --- | --- | --- |
| `lead_id` | Lead_Id | See action definition |
| `changes_info` | Changes_Info | Optional |
| `FirstName` | First Name | Optional |
| `LastName` | Last Name | Optional |
| `Company` | Company | Optional |
| `Email` | Email | Optional |
| `Phone` | Phone | Optional |
| `LeadSource` | Lead Source | See action definition |
| `other_fields` | More fields as JSON, with Salesforce field API names as keys. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/update-lead.ts).

### Update Object (Advanced)

Update object by Id

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `id` | Select the Id | Yes |
| `data` | Select mapped object | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/update-object-by-id.ts).

### Update Record

Updates fields on a record of any object.

| Input | What to provide | Required |
| --- | --- | --- |
| `object` | Object | See action definition |
| `record_id` | Record_Id | See action definition |
| `changes_info` | Changes_Info | Optional |
| `data` | Field API names as keys, with the new values. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/action/update-record.ts).

## Events and recurring work

- **[New Case Attachment](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/trigger/new-case-attachment.ts)** — Fires when a new Attachment or File is added to any Case record.
- **[New Case in Queue](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/trigger/new-case-in-queue.ts)** — Fires when a case is assigned to the chosen queue.
- **[New Contact](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/trigger/new-contact.ts)** — Fires when a new Contact record is created in Salesforce.
- **[New Field History Event](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/trigger/new-field-history-event.ts)** — Fires when a tracked field is updated on a specified object.
- **[New Lead](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/trigger/new-lead.ts)** — Fires when a new Lead record is created in Salesforce.
- **[New or Updated File](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/trigger/new-updated-file.ts)** — Fires when a file is added or changed. Classic attachments are not included.
- **[New or Updated Record](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/trigger/new-updated-record.ts)** — Fires when a record of the chosen object is created or changed.
- **[New Outbound Message](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/trigger/new-outbound-message.ts)** — Fires when Salesforce sends an outbound message to this flow.
- **[New Record](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/salesforce/src/lib/trigger/new-record.ts)** — Fires when a record of the chosen object is created.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Salesforce to find child records. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
