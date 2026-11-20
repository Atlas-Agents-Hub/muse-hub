---
name: copper-connector
description: "Copper: create lead, create task, search for a company."
---

# Copper for Muse

Copper: create lead, create task, search for a company.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Copper**.
2. Configure **Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Email Address** (`email`): Email Address of the Token Owner
- **API Key** (`apiKey`): Your API Key in settings > integrations

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/index.ts).

## Actions

### Create Lead

Adds a new lead.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Full Name | Yes |
| `email` | Email | Yes |
| `category` | Category of the email address (e.g., work, personal) | Yes |
| `phone_numbers` | Phone Numbers | Yes |
| `address_street` | Street | Optional |
| `address_city` | City | Optional |
| `address_state` | State/Region | Optional |
| `address_postal_code` | Postal Code | Optional |
| `address_country` | Country | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/actions/create-lead.ts).

### Create Task

Adds a new task under a person, lead, or opportunity.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Task Name | Yes |
| `details` | Details fo this task | Optional |
| `custom_activity_type_id` | Custom_Activity_Type_Id | See action definition |
| `assigneeId` | Assignee Id | See action definition |
| `entity` | Choose the type of Copper record this task should be linked to (e.g. Person, Company, Lead, Opportunity, or Project). | Optional |
| `entityItemId` | Select the specific record (from the chosen type above) that this task should be attached to. For example, pick the Person or Opportunity the task relates to. | Optional |
| `due_date` | Enter date and time in 24-hour format, e.g. `2025-09-09 11:40` (11:40 AM) or `2025-09-09 13:00` (1:00 PM). | Optional |
| `reminder_date` | Enter date and time in 24-hour format, e.g. `2025-09-09 11:40` (11:40 AM) or `2025-09-09 13:00` (1:00 PM) | Optional |
| `priority` | Priority | Optional |
| `tags` | Tags | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/actions/create-task.ts).

### Search for a Company

Lookup a company.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Full name of the Company to search for. | Optional |
| `phone_number` | Phone Number of the Company to search for. | Optional |
| `email_domains` | Email Domain of the Company to search for. | Optional |
| `contact_type_ids` | Contact_Type_Ids | See action definition |
| `assignee_ids` | Assignee_Ids | See action definition |
| `city` | The city in which Company must be located. | Optional |
| `state` | The state or province in which Company must be located. | Optional |
| `postal_code` | The postal code in which Company must be located. | Optional |
| `country` | The two character country code where Company must be located. | Optional |
| `tags` | Filter Company to those that match at least one of the tags specified. | Optional |
| `socials` | Filter Company to those that match at least one of the social accounts specified. | Optional |
| `followed` | Filter by followed state | Optional |
| `age` | The maximum age in seconds that Company must be. | Optional |
| `page_size` | Default 50. Max 200. | Optional |
| `page_number` | Page Number | Optional |
| `sort_by` | The field on which to sort the results | Optional |
| `sort_direction` | The direction in which to sort the result | Optional |
| `minimum_interaction_count` | The minimum number of interactions Company must have had. | Optional |
| `maximum_interaction_count` | The maximum number of interactions Company must have had. | Optional |
| `minimum_interaction_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date of the last interaction. | Optional |
| `maximum_interaction_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date of the last interaction. | Optional |
| `minimum_created_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date Company are created. | Optional |
| `maximum_created_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date Company are Created. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/actions/search-for-a-company.ts).

### Search for a Lead

Lookup a lead using match criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Full name of the Lead to search for. | Optional |
| `phone_number` | Phone Number of the Lead to search for. | Optional |
| `emails` | Emails of the Lead to search for. | Optional |
| `assignee_ids` | Assignee_Ids | See action definition |
| `status_ids` | Status_Ids | See action definition |
| `customer_source_ids` | Customer_Source_Ids | See action definition |
| `city` | The city in which Lead must be located. | Optional |
| `state` | The state or province in which Lead must be located. | Optional |
| `postal_code` | The postal code in which Lead must be located. | Optional |
| `country` | The two character country code where Lead must be located. | Optional |
| `tags` | Filter Lead to those that match at least one of the tags specified. | Optional |
| `socials` | Filter Lead to those that match at least one of the social accounts specified. | Optional |
| `followed` | Filter by followed state | Optional |
| `age` | The maximum age in seconds that Lead must be. | Optional |
| `page_size` | Default 50. Max 200. | Optional |
| `page_number` | Page Number | Optional |
| `sort_by` | The field on which to sort the results | Optional |
| `sort_direction` | The direction in which to sort the result | Optional |
| `include_converted_leads` | Specify if response should contain converted leads. | Optional |
| `minimum_monetary_value` | The minimum monetary value Leads must have. | Optional |
| `maximum_monetary_value` | The maximum monetary value Leads must have. | Optional |
| `minimum_interaction_count` | The minimum number of interactions Lead must have had. | Optional |
| `maximum_interaction_count` | The maximum number of interactions Lead must have had. | Optional |
| `minimum_interaction_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date of the last interaction. | Optional |
| `maximum_interaction_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date of the last interaction. | Optional |
| `minimum_created_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date Lead are created. | Optional |
| `maximum_created_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date Lead are Created. | Optional |
| `minimum_modified_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date Lead are Modified. | Optional |
| `maximum_modified_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date Lead are Modified. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/actions/search-for-a-lead.ts).

### Search for a Person

Lookup a person using match criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Full name of the People to search for. | Optional |
| `phone_number` | Phone Number of the People to search for. | Optional |
| `emails` | Emails of the People to search for. | Optional |
| `contact_type_ids` | Contact_Type_Ids | See action definition |
| `assignee_ids` | Assignee_Ids | See action definition |
| `company_ids` | Company_Ids | See action definition |
| `opportunity_ids` | Opportunity_Ids | See action definition |
| `city` | The city in which People must be located. | Optional |
| `state` | The state or province in which People must be located. | Optional |
| `postal_code` | The postal code in which People must be located. | Optional |
| `country` | The two character country code where People must be located. | Optional |
| `tags` | Filter People to those that match at least one of the tags specified. | Optional |
| `socials` | Filter People to those that match at least one of the social accounts specified. | Optional |
| `followed` | Filter by followed state | Optional |
| `age` | The maximum age in seconds that People must be. | Optional |
| `page_size` | Default 50. Max 200. | Optional |
| `page_number` | Page Number | Optional |
| `sort_by` | The field on which to sort the results | Optional |
| `sort_direction` | The direction in which to sort the result | Optional |
| `minimum_interaction_count` | The minimum number of interactions People must have had. | Optional |
| `maximum_interaction_count` | The maximum number of interactions People must have had. | Optional |
| `minimum_interaction_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date of the last interaction. | Optional |
| `maximum_interaction_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date of the last interaction. | Optional |
| `minimum_created_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date People are created. | Optional |
| `maximum_created_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date People are Created. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/actions/search-for-a-person.ts).

### Search for a Project

Lookup a project.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Full name of the Opportunity to search for. | Optional |
| `assignee_ids` | Assignee_Ids | See action definition |
| `statuses` | Filter by Opportunity status | Optional |
| `tags` | Filter People to those that match at least one of the tags specified. | Optional |
| `followed` | Filter by followed state | Optional |
| `page_size` | Default 50. Max 200. | Optional |
| `page_number` | Page Number | Optional |
| `sort_by` | The field on which to sort the results | Optional |
| `sort_direction` | The direction in which to sort the result | Optional |
| `minimum_created_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date Opportunity are created. | Optional |
| `maximum_created_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date Opportunity are Created. | Optional |
| `minimum_modified_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date Opportunity are Modified. | Optional |
| `maximum_modified_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date Opportunity are Modified. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/actions/search-for-a-project.ts).

### Search for an Activity

Find an existing activity by type/criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `entity` | Select parent entity | Optional |
| `entityItemId` | Select Resource | Optional |
| `activity_types` | Activity_Types | See action definition |
| `page_size` | Default 50. Max 200. | Optional |
| `page_number` | Page Number | Optional |
| `minimum_activity_date` | 24-hour format, e.g. 2025-09-10 11:40. The timestamp of the earliest activity date. | Optional |
| `maximum_activity_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest activity date. | Optional |
| `full_result` | (Optional) If set, search performance improves but duplicate activity logs may be returned | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/actions/search-for-an-activity.ts).

### Search for an Opportunity

Lookup an opportunity.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Full name of the Opportunity to search for. | Optional |
| `assignee_ids` | Assignee_Ids | See action definition |
| `company_ids` | Company_Ids | See action definition |
| `status_ids` | Filter by Opportunity status | Optional |
| `priorities` | Priority | Optional |
| `pipeline_ids` | Pipeline_Ids | See action definition |
| `pipeline_stage_ids` | Select a stage | Optional |
| `primary_contact_ids` | Primary_Contact_Ids | See action definition |
| `customer_source_ids` | Customer_Source_Ids | See action definition |
| `loss_reason_ids` | Loss_Reason_Ids | See action definition |
| `tags` | Filter People to those that match at least one of the tags specified. | Optional |
| `followed` | Filter by followed state | Optional |
| `page_size` | Default 50. Max 200. | Optional |
| `page_number` | Page Number | Optional |
| `sort_by` | The field on which to sort the results | Optional |
| `sort_direction` | The direction in which to sort the result | Optional |
| `minimum_monetary_value` | The minimum monetary value Opportunities must have. | Optional |
| `maximum_monetary_value` | The maximum monetary value Opportunities must have. | Optional |
| `minimum_interaction_count` | The minimum number of interactions Opportunity must have had. | Optional |
| `maximum_interaction_count` | The maximum number of interactions Opportunity must have had. | Optional |
| `minimum_close_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date close date. | Optional |
| `maximum_close_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date close date. | Optional |
| `minimum_interaction_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date of the last interaction. | Optional |
| `maximum_interaction_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date of the last interaction. | Optional |
| `minimum_stage_change_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date of a stage change. | Optional |
| `maximum_stage_change_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date of a stage change. | Optional |
| `minimum_created_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date Opportunity are created. | Optional |
| `maximum_created_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date Opportunity are Created. | Optional |
| `minimum_modified_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the earliest date Opportunity are Modified. | Optional |
| `maximum_modified_date` | 24-hour format, e.g. 2025-09-10 13:00. The timestamp of the latest date Opportunity are Modified. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/actions/search-for-an-opportunity.ts).

## Events and recurring work

- **[New Activity](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/triggers/new-activity.ts)** — Triggers when a new activity is logged
- **[New Lead](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/triggers/new-lead.ts)** — Triggers when a new lead is created.
- **[New Person](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/copper/src/lib/triggers/new-person.ts)** — Triggers when a new person/contact is created.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Copper to search for a company. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
