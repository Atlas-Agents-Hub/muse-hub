---
name: folk-connector
description: "Folk is a CRM for building relationships at scale. Manage your contacts, companies, and relationships in one place."
---

# Folk for Muse

Folk is a CRM for building relationships at scale. Manage your contacts, companies, and relationships in one place.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Folk**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/index.ts).

## Actions

### Create Company

Create a new company in your Folk workspace. You can add emails, links, phone numbers, and assign it to a group.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | The name of the company | Yes |
| `description` | A short description of the company | Optional |
| `industry` | The industry the company operates in | Optional |
| `addresses` | Physical addresses for the company. The first address is primary. | Yes |
| `emails` | Email addresses for the company. The first email is primary. | Yes |
| `phones` | Phone numbers for the company. The first phone is primary. | Yes |
| `urls` | Website URLs for the company. The first URL is primary. | Yes |
| `groupId` | Group Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/actions/create-company.ts).

### Create Person

Create a new person in your Folk workspace. You can link them to a company, add contact details, and assign to a group.

| Input | What to provide | Required |
| --- | --- | --- |
| `firstName` | The first name of the person | Optional |
| `lastName` | The last name of the person | Optional |
| `fullName` | The full name of the person (alternative to first/last) | Optional |
| `description` | A short description of the person | Optional |
| `birthday` | The birthday in YYYY-MM-DD format | Optional |
| `jobTitle` | The job title of the person | Optional |
| `companyNames` | The names of companies to associate with the person. The first company will be primary. | Yes |
| `companyIds` | Company Ids | See action definition |
| `addresses` | Physical addresses for the person. The first address is primary. | Yes |
| `emails` | Email addresses for the person. The first email is primary. | Yes |
| `phones` | Phone numbers for the person. The first phone is primary. | Yes |
| `urls` | Website URLs for the person. The first URL is primary. | Yes |
| `groupId` | Group Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/actions/create-person.ts).

### Find Company

Search for companies in your Folk workspace whose name contains the search text.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Text the company name contains. | Yes |
| `cursor` | Next Cursor from the previous result. Empty for the first page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/actions/find-company.ts).

### Get Company

Retrieve detailed information about a company from your Folk workspace.

| Input | What to provide | Required |
| --- | --- | --- |
| `companyId` | Company Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/actions/get-company.ts).

### Get Person

Retrieve detailed information about a person from your Folk workspace.

| Input | What to provide | Required |
| --- | --- | --- |
| `personId` | Person Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/actions/get-person.ts).

### List People

Retrieve a page of people in your Folk workspace, optionally filtered by name or email.

| Input | What to provide | Required |
| --- | --- | --- |
| `limit` | The number of people to return (1-100). | Optional |
| `cursor` | Next Cursor from the previous result. Empty for the first page. | Optional |
| `combinator` | How to combine the name and email filters when both are set. | Optional |
| `nameFilter` | Filter by person name (contains) | Optional |
| `emailFilter` | Filter by email address (contains) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/actions/find-person.ts).

### Update Company

Update an existing company in your Folk workspace. Select the company from the dropdown to update its details.

| Input | What to provide | Required |
| --- | --- | --- |
| `companyId` | Company Id | See action definition |
| `name` | The name of the company | Optional |
| `description` | A short description of the company | Optional |
| `industry` | The industry the company operates in | Optional |
| `addresses` | Physical addresses for the company. The first address is primary. | Yes |
| `emails` | Email addresses for the company. The first email is primary. | Yes |
| `phones` | Phone numbers for the company. The first phone is primary. | Yes |
| `urls` | Website URLs for the company. The first URL is primary. | Yes |
| `groupId` | Group Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/actions/update-company.ts).

### Update Person

Update an existing person in your Folk workspace with new information.

| Input | What to provide | Required |
| --- | --- | --- |
| `personId` | Person Id | See action definition |
| `firstName` | The first name of the person | Optional |
| `lastName` | The last name of the person | Optional |
| `fullName` | The full name of the person (alternative to first/last) | Optional |
| `description` | A short description of the person | Optional |
| `birthday` | The birthday in YYYY-MM-DD format | Optional |
| `jobTitle` | The job title of the person | Optional |
| `companyIds` | Company Ids | See action definition |
| `companyNames` | Company names to create or associate with. Companies will be created if they don't exist. | Yes |
| `addresses` | Physical addresses for the person. The first address is primary. | Yes |
| `emails` | Email addresses for the person. The first email is primary. | Yes |
| `phones` | Phone numbers for the person. The first phone is primary. | Yes |
| `urls` | Website URLs for the person. The first URL is primary. | Yes |
| `groupId` | Group Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/actions/update-person.ts).

## Events and recurring work

- **[Company Added](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/triggers/company-added.ts)** — Fires when a new company is added to your Folk workspace.
- **[Company Groups Updated](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/triggers/company-custom-field-updated.ts)** — Fires when a company's group assignments are updated in your Folk workspace.
- **[Company Removed](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/folk/src/lib/triggers/company-removed.ts)** — Fires when a company is removed from your Folk workspace.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Folk to find company. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
