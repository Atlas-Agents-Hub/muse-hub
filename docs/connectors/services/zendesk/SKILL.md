---
name: zendesk-connector
description: "Customer service software and support ticket system"
---

# Zendesk for Muse

Customer service software and support ticket system

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Zendesk**.
2. Configure **Provider connection fields; OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://{subdomain}.zendesk.com/oauth/authorizations/new>
- Token endpoint: <https://{subdomain}.zendesk.com/oauth/tokens>
- **Agent Email** (`email`): The email address you use to login to Zendesk
- **Token** (`token`): The API token you can generate in Zendesk
- **Organization (e.g activepieceshelp)** (`subdomain`): The subdomain of your Zendesk instance

Provider scopes: `read`, `write`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zendesk/src/index.ts).

## Actions

### Create User

Add a new user to the Zendesk instance.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | The name of the user | Yes |
| `email` | The primary email address of the user | Optional |
| `role` | The role of the user. Defaults to "end-user" if not specified. | Optional |
| `custom_role_id` | Custom_Role_Id | See action definition |
| `organization_id` | Organization_Id | See action definition |
| `organization_name` | Create and associate user with a new organization by name (alternative to Organization ID) | Optional |
| `phone` | The phone number of the user | Optional |
| `alias` | An alias displayed to end users | Optional |
| `details` | Additional details about the user | Optional |
| `notes` | Internal notes about the user | Optional |
| `external_id` | A unique external ID for the user (useful for integrations) | Optional |
| `time_zone` | The time zone of the user (e.g., "America/New_York") | Optional |
| `locale` | The locale of the user (e.g., "en-US") | Optional |
| `verified` | Whether the user is verified | Optional |
| `active` | Whether the user is active. Defaults to true. | Optional |
| `shared` | Whether the user is shared from a different Zendesk Support instance | Optional |
| `shared_agent` | Whether the user is a shared agent from a different Zendesk Support instance | Optional |
| `moderator` | Whether the user has forum moderation capabilities | Optional |
| `suspended` | Whether the user is suspended | Optional |
| `restricted_agent` | Whether the agent has restrictions on what tickets they can access | Optional |
| `only_private_comments` | Whether the user can only create private comments | Optional |
| `report_csv` | Whether the user can access CSV reports | Optional |
| `skip_verify_email` | Skip sending a verification email to the user | Optional |
| `ticket_restriction` | The ticket restriction for the user | Optional |
| `signature` | The user's signature for email responses | Optional |
| `default_group_id` | Default_Group_Id | See action definition |
| `agent_brand_ids` | Agent_Brand_Ids | See action definition |
| `tags` | Array of tags to apply to the user | Optional |
| `user_fields` | User_Fields | See action definition |
| `identities` | Array of identity objects with type and value. Example: [{"type": "email", "value": "test@example.com"}, {"type": "twitter", "value": "username"}] | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zendesk/src/lib/actions/create-user.ts).

### Delete User

Remove a user and associated records from the account.

| Input | What to provide | Required |
| --- | --- | --- |
| `user_id` | User_Id | See action definition |
| `confirmation` | I understand that deleted users are not recoverable and this action cannot be undone. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zendesk/src/lib/actions/delete-user.ts).

### Find a Group

Find a group by name.

| Input | What to provide | Required |
| --- | --- | --- |
| `group_name` | The name of the group to find | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zendesk/src/lib/actions/find-group.ts).

### Find an Agent

Find an agent by email or name.

| Input | What to provide | Required |
| --- | --- | --- |
| `search_type` | Choose how to search for the agent | Yes |
| `search_value` | The email or name to search for | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zendesk/src/lib/actions/find-agent.ts).

### Find Latest Comment

Find the latest comment on a ticket.

| Input | What to provide | Required |
| --- | --- | --- |
| `ticket_id` | Ticket_Id | See action definition |
| `include_private` | Include private internal comments in the search | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zendesk/src/lib/actions/find-latest-comment.ts).

### Find Organization(s)

Search organizations by name, domain, external ID, or other criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `search_type` | Choose how to search for organizations | Yes |
| `name` | The name of the organization to search for | Optional |
| `domain` | Search organizations by domain name | Optional |
| `external_id` | Search organizations by external ID | Optional |
| `tag` | Search organizations containing this tag | Optional |
| `details` | Search in organization details/notes | Optional |
| `custom_query` | Custom search query using Zendesk search syntax (e.g., "type:organization domain:example.com") | Optional |
| `sort_by` | How to sort the results | Optional |
| `sort_order` | Sort order for results | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zendesk/src/lib/actions/find-organization.ts).

### Find Ticket(s)

Search tickets by ID, field, or content.

| Input | What to provide | Required |
| --- | --- | --- |
| `search_type` | Choose how to search for tickets | Yes |
| `timeFilter` | Date Time Filter | Yes |
| `ticket_id` | The ID of the ticket to find | Optional |
| `status` | Search tickets by status | Optional |
| `priority` | Search tickets by priority | Optional |
| `ticket_type` | Search tickets by type | Optional |
| `tag` | Search tickets containing this tag | Optional |
| `requester_email` | Search tickets by requester email address | Optional |
| `assignee_email` | Search tickets by assignee email address | Optional |
| `content` | Search in ticket subject and content | Optional |
| `custom_query` | Custom search query using Zendesk search syntax (e.g., "type:ticket status:open priority:high") | Optional |
| `sort_by` | How to sort the results | Optional |
| `sort_order` | Sort order for results | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zendesk/src/lib/actions/find-tickets.ts).

### Find User(s)

Search users by email, name, role, or other criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `search_type` | Choose how to search for users | Yes |
| `email` | The email address of the user to search for | Optional |
| `name` | The name of the user to search for | Optional |
| `role` | Search users by role | Optional |
| `organization` | Search users by organization name | Optional |
| `tag` | Search users containing this tag | Optional |
| `external_id` | Search users by external ID | Optional |
| `custom_query` | Custom search query using Zendesk search syntax (e.g., "type:user role:agent") | Optional |
| `sort_by` | How to sort the results | Optional |
| `sort_order` | Sort order for results | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zendesk/src/lib/actions/find-user.ts).

## Try it

> Use Zendesk to find a group. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
