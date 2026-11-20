---
name: capsule-crm-connector
description: "Capsule CRM: add note to entity, create contact, create project."
---

# Capsule CRM for Muse

Capsule CRM: add note to entity, create contact, create project.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Capsule CRM**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://api.capsulecrm.com/oauth/authorise>
- Token endpoint: <https://api.capsulecrm.com/oauth/token>

Provider scopes: `read`, `write`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/capsule-crm/src/index.ts).

## Actions

### Add Note to Entity

Add a comment/note to an entity (e.g., contact, opportunity, project).

| Input | What to provide | Required |
| --- | --- | --- |
| `content` | The body of the note. | Yes |
| `entityType` | The type of entity to add the note to. | Yes |
| `entityId` | Entity | Yes |
| `activityTypeId` | The activity type for this entry. Defaults to "Note". | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/capsule-crm/src/lib/actions/add-note-to-entity.ts).

### Create Contact

Create a new Person or Organisation in Capsule CRM.

| Input | What to provide | Required |
| --- | --- | --- |
| `type` | The type of contact to create. | Yes |
| `contactFields` | Details | Yes |
| `about` | About | Optional |
| `ownerId` | Owner | Optional |
| `teamId` | Team | Optional |
| `tags` | Tags | Optional |
| `customFields` | Custom Fields | Yes |
| `emailAddresses` | Email Addresses | Yes |
| `phoneNumbers` | Phone Numbers | Yes |
| `addresses` | Addresses | Optional |
| `websites` | Websites | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/capsule-crm/src/lib/actions/create-contact.ts).

### Create Project

Create a new Project in Capsule CRM.

| Input | What to provide | Required |
| --- | --- | --- |
| `partyId` | The main contact for this project. | Yes |
| `name` | The name of this project. | Yes |
| `description` | The description of this project. | Optional |
| `opportunityId` | An optional link to the opportunity that this project was created to support. | Optional |
| `stageId` | The stage that this project is on. | Optional |
| `status` | The status of the project. | Optional |
| `expectedCloseOn` | The expected close date of this project. | Optional |
| `ownerId` | The user this project is assigned to. | Optional |
| `teamId` | The team this project is assigned to. | Optional |
| `tags` | An array of tags that are added to this project. | Optional |
| `customFields` | An array of custom fields that are defined for this project. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/capsule-crm/src/lib/actions/create-project.ts).

### Create Task

Create a new Task in Capsule CRM.

| Input | What to provide | Required |
| --- | --- | --- |
| `description` | A short description of the task. | Yes |
| `dueOn` | The date when this task is due. | Yes |
| `detail` | More details about the task. | Optional |
| `dueTime` | The time when this task is due (e.g., 18:00:00). Note: The time is in the user's timezone. | Optional |
| `linkTo` | The entity this task is linked to. Only one can be selected. | Optional |
| `linkedEntityId` | Linked Entity | Yes |
| `categoryId` | The category of this task. | Optional |
| `ownerId` | The user this task is assigned to. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/capsule-crm/src/lib/actions/create-task.ts).

### Find Contact

Find a Person by search criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `term` | The value to search for (e.g., a name or email). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/capsule-crm/src/lib/actions/find-contact.ts).

### Find Opportunity

Find an Opportunity by search criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `filter` | The structured filter query. See the [documentation](https://capsulecrm.com/developer/api-v2/filters/) for examples. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/capsule-crm/src/lib/actions/find-opportunity.ts).

### Find Project

Find a Project by search criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `filter` | The structured filter query. See the [documentation](https://capsulecrm.com/developer/api-v2/filters/) for examples. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/capsule-crm/src/lib/actions/find-project.ts).

### Update Contact

Update fields on an existing Person or Organisation.

| Input | What to provide | Required |
| --- | --- | --- |
| `contact_id` | Contact_Id | See action definition |
| `contactFields` | Details | Yes |
| `ownerId` | Owner Id | See action definition |
| `teamId` | Team Id | See action definition |
| `about` | Update the biography or description for the contact. | Optional |
| `addresses` | Addresses | Optional |
| `websites` | Websites | Optional |
| `emailAddresses` | Email Addresses | Optional |
| `phoneNumbers` | Phone Numbers | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/capsule-crm/src/lib/actions/update-contact.ts).

## Try it

> Use Capsule CRM to find contact. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
