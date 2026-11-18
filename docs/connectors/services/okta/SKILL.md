---
name: okta-connector
description: "Okta: activate user, add user to group, create user."
---

# Okta for Muse

Okta: activate user, add user to group, create user.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Okta**.
2. Configure **Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Okta Domain** (`domain`): Your Okta organization domain (e.g., https://dev-12345.okta.com or dev-12345.okta.com)
- **API Token** (`apiToken`): Your Okta API token (from Admin → Security → API → Tokens)

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/okta/src/index.ts).

## Actions

### Activate User

Activate a previously deactivated or pending user

| Input | What to provide | Required |
| --- | --- | --- |
| `userId` | User Id | See action definition |
| `sendEmail` | Send activation email to user | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/okta/src/lib/actions/activate-user.ts).

### Add User to Group

Add a user to a specific Okta group

| Input | What to provide | Required |
| --- | --- | --- |
| `userId` | User Id | See action definition |
| `groupId` | Group Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/okta/src/lib/actions/add-user-to-group.ts).

### Create User

Creates a user without credentials and sends account creation prompt via email

| Input | What to provide | Required |
| --- | --- | --- |
| `firstName` | User first name | Yes |
| `lastName` | User last name | Yes |
| `email` | User email address | Yes |
| `login` | User login (typically same as email) | Optional |
| `mobilePhone` | User mobile phone number | Optional |
| `sendEmail` | Send account creation email to user | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/okta/src/lib/actions/create-user.ts).

### Deactivate User

Deactivate (disable) a user in Okta

| Input | What to provide | Required |
| --- | --- | --- |
| `userId` | User Id | See action definition |
| `sendEmail` | Send deactivation email to user | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/okta/src/lib/actions/deactivate-user.ts).

### Find Group by Name

Search for an Okta group by name

| Input | What to provide | Required |
| --- | --- | --- |
| `groupName` | The group name to search for | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/okta/src/lib/actions/find-group-by-name.ts).

### Find User by Email

Look up an Okta user by their email address

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | The user email address | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/okta/src/lib/actions/find-user-by-email.ts).

### Suspend User

Temporarily suspend a user in Okta

| Input | What to provide | Required |
| --- | --- | --- |
| `userId` | User Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/okta/src/lib/actions/suspend-user.ts).

### Update User

Update user profile information

| Input | What to provide | Required |
| --- | --- | --- |
| `userId` | User Id | See action definition |
| `firstName` | Updated first name | Optional |
| `lastName` | Updated last name | Optional |
| `email` | Updated email address | Optional |
| `mobilePhone` | Updated mobile phone number | Optional |
| `customAttributes` | JSON object with custom profile attributes | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/okta/src/lib/actions/update-user.ts).

## Events and recurring work

- **[New Event](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/okta/src/lib/triggers/new-event.ts)** — Fires when a new Okta event is generated

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Okta to find group by name. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
