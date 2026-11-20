---
name: mailchimp-connector
description: "All-in-One integrated marketing platform for managing audiences, sending campaigns, tracking engagement, and automating lifecycle communications."
---

# Mailchimp for Muse

All-in-One integrated marketing platform for managing audiences, sending campaigns, tracking engagement, and automating lifecycle communications.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Mailchimp**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://login.mailchimp.com/oauth2/authorize>
- Token endpoint: <https://login.mailchimp.com/oauth2/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/index.ts).

## Actions

### Create Audience

Create a new audience (list) in your Mailchimp account

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | The name of the list | Yes |
| `company` | Company name for list contact information | Yes |
| `address1` | Street address for list contact information | Yes |
| `address2` | Additional address information (optional) | Optional |
| `city` | City for list contact information | Yes |
| `state` | State or province for list contact information | Optional |
| `zip` | ZIP or postal code for list contact information | Optional |
| `country` | Country for list contact information | Yes |
| `phone` | Phone number for list contact information (optional) | Optional |
| `permission_reminder` | The permission reminder for the list | Yes |
| `from_name` | Default from name for campaigns | Yes |
| `from_email` | Default from email address for campaigns | Yes |
| `subject` | Default subject line for campaigns | Yes |
| `language` | Default language for campaigns (e.g., "en", "es", "fr") | Yes |
| `email_type_option` | Whether the list supports multiple email formats (HTML/plain text) | Optional |
| `use_archive_bar` | Whether campaigns use the Archive Bar in archives by default | Optional |
| `notify_on_subscribe` | Email address to send subscribe notifications to (optional) | Optional |
| `notify_on_unsubscribe` | Email address to send unsubscribe notifications to (optional) | Optional |
| `double_optin` | Whether to require subscriber confirmation via email | Optional |
| `marketing_permissions` | Whether the list has marketing permissions (GDPR) enabled | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/actions/create-audience.ts).

### Create Tag

Create a new tag in a Mailchimp audience

| Input | What to provide | Required |
| --- | --- | --- |
| `list_id` | List_Id | See action definition |
| `name` | The name of the tag to create | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/actions/create-tag.ts).

### Find Campaign

Search all campaigns for the specified query terms

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Search terms to find campaigns | Yes |
| `fields` | Comma-separated list of fields to return | Optional |
| `exclude_fields` | Comma-separated list of fields to exclude | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/actions/find-campaign.ts).

### Find Customer

Find a customer by email address in a store

| Input | What to provide | Required |
| --- | --- | --- |
| `store_id` | Store_Id | See action definition |
| `email_address` | Email address to search for | Yes |
| `fields` | Comma-separated list of fields to return | Optional |
| `exclude_fields` | Comma-separated list of fields to exclude | Optional |
| `count` | Number of records to return (max 1000) | Optional |
| `offset` | Number of records to skip for pagination | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/actions/find-customer.ts).

### Find Subscriber

Search for subscribers across all lists or within a specific list. This action provides comprehensive subscriber information including merge fields, interests, and activity data.

| Input | What to provide | Required |
| --- | --- | --- |
| `list_id` | List_Id | See action definition |
| `email` | Email address of the subscriber to search for | Yes |
| `include_fields` | Fields to include in the response (leave empty for all fields). Use dot notation for nested fields (e.g., "merge_fields.FNAME") | Optional |
| `exclude_fields` | Fields to exclude from the response. Use dot notation for nested fields | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/actions/find-subscriber.ts).

### Find Tag

Search for tags on a list by name

| Input | What to provide | Required |
| --- | --- | --- |
| `list_id` | List_Id | See action definition |
| `name` | Search query to filter tags (optional - if empty, returns all tags) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/actions/find-tag.ts).

### Get Campaign Report

Get comprehensive report details for a specific sent campaign including opens, clicks, bounces, and performance metrics

| Input | What to provide | Required |
| --- | --- | --- |
| `campaign_id` | Campaign_Id | See action definition |
| `fields` | Comma-separated list of fields to return (e.g., "opens.unique_opens,clicks.click_rate") | Optional |
| `exclude_fields` | Comma-separated list of fields to exclude (e.g., "timeseries,_links") | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/actions/get-campaign-report.ts).

### Send Campaign

Send a draft campaign to the subscribers in its audience, segment, or tag

| Input | What to provide | Required |
| --- | --- | --- |
| `campaign_id` | Campaign_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/actions/send-campaign.ts).

## Events and recurring work

- **[Email Opened](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/triggers/email-opened-trigger.ts)** — Fires when a recipient opens a an email in a specific campaign
- **[Link Clicked](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/triggers/link-clicked-trigger.ts)** — Fires when a recipient clicks a specified link in a campaign
- **[New Campaign](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailchimp/src/lib/triggers/new-campaign-trigger.ts)** — Fires when a new campaign is created or sent

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Mailchimp to find campaign. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

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
python connector.py inspect mailchimp
```

Available HTTP reads: `read-oauth2-metadata`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
