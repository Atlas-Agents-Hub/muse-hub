---
name: lemlist-connector
description: "Lemlist: add custom variables on lead, add lead to a campaign, mark lead from all campaign as interested."
---

# Lemlist for Muse

Lemlist: add custom variables on lead, add lead to a campaign, mark lead from all campaign as interested.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Lemlist**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/index.ts).

## Actions

### Add Custom Variables on Lead

Add new custom variables to a lead.

| Input | What to provide | Required |
| --- | --- | --- |
| `leadId` | The unique identifier of the lead (e.g. lea_8xJSc7sV7ggpiVnXe). Available as the _id field returned by the Add Lead To A Campaign and Search Lead actions. | Yes |
| `customVariables` | New custom variables to create on the lead. Each key is the variable name and each value is its content. Names must not match an existing default or custom variable. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/lib/actions/add-custom-variables-on-lead.ts).

### Add Lead To A Campaign

Adds a lead to a specific campaign with optional enrichment and lead details. Enrichment options use lemlist credits.

| Input | What to provide | Required |
| --- | --- | --- |
| `campaignId` | Campaign Id | See action definition |
| `email` | The email of the lead to add | Yes |
| `firstName` | First Name | Optional |
| `lastName` | Last Name | Optional |
| `picture` | Picture URL | Optional |
| `phone` | Phone | Optional |
| `linkedinUrl` | LinkedIn URL | Optional |
| `companyName` | Company Name | Optional |
| `companyDomain` | Company Domain | Optional |
| `icebreaker` | Icebreaker | Optional |
| `jobTitle` | Job Title | Optional |
| `deduplicate` | Refuse the lead if the contact is already in another campaign. | Optional |
| `linkedinEnrichment` | Run LinkedIn enrichment for this lead. Uses lemlist credits. | Optional |
| `findEmail` | Try to find a verified email for this lead. Uses lemlist credits. | Optional |
| `verifyEmail` | Verify the lead’s email. Uses lemlist credits. | Optional |
| `findPhone` | Try to find a phone number for this lead. Uses lemlist credits. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/lib/actions/add-lead-to-a-campaign.ts).

### Mark Lead From All Campaign as Interested

Mark a lead as “interested” across all campaigns.

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | The email of the lead to mark as interested. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/lib/actions/mark-lead-from-all-campaign-as-interested.ts).

### Remove Lead from A Campaign

Removes a lead from a specific campaign.

| Input | What to provide | Required |
| --- | --- | --- |
| `campaignId` | Campaign Id | See action definition |
| `email` | The email of the lead to remove. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/lib/actions/remove-lead-from-a-campaign.ts).

### Remove Lead From Unsubscribe List

Remove a lead from the “unsubscribe” list so lemlist can contact them again. Only do this when the person opted back in.

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | The email of the lead to remove from the unsubscribe list. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/lib/actions/remove-lead-from-unsubscribe-list.ts).

### Search Lead

Look up a lead by email and campaign.

| Input | What to provide | Required |
| --- | --- | --- |
| `campaignId` | Campaign Id | See action definition |
| `email` | The email of the lead to look up | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/lib/actions/search-lead.ts).

### Unsubscribe a Lead

Unsubscribe a lead from a campaign.

| Input | What to provide | Required |
| --- | --- | --- |
| `campaignId` | Campaign Id | See action definition |
| `email` | The email of the lead to unsubscribe. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/lib/actions/unsubscribe-a-lead.ts).

### Update Lead From Campaign

Updates a lead in a specific campaign. Empty fields are left unchanged.

| Input | What to provide | Required |
| --- | --- | --- |
| `campaignId` | Campaign Id | See action definition |
| `email` | The email of the lead to update. | Yes |
| `firstName` | First Name | Optional |
| `lastName` | Last Name | Optional |
| `picture` | Picture URL | Optional |
| `phone` | Phone | Optional |
| `linkedinUrl` | LinkedIn URL | Optional |
| `companyName` | Company Name | Optional |
| `companyDomain` | Company Domain | Optional |
| `icebreaker` | Icebreaker | Optional |
| `jobTitle` | Job Title | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/lib/actions/update-lead-from-campaign.ts).

## Events and recurring work

- **[New Activity](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/lib/triggers/new-activity.ts)** — Triggers for each new activity, optionally only some event types or one campaign.
- **[Unsubscribed Recipient](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lemlist/src/lib/triggers/unsubscribed-recipient.ts)** — Triggers when a recipient unsubscribes.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Lemlist to remove lead from unsubscribe list. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
