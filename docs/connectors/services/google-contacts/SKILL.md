---
name: google-contacts-connector
description: "Stay connected and organized"
---

# Google Contacts for Muse

Stay connected and organized

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Google Contacts**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.google.com/o/oauth2/auth>
- Token endpoint: <https://oauth2.googleapis.com/token>

Provider scopes: `email`, `https://www.googleapis.com/auth/contacts`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/index.ts).

## Actions

### Add Contact

Add a new contact to your Google Contacts.

| Input | What to provide | Required |
| --- | --- | --- |
| `firstName` | First Name | Yes |
| `lastName` | Last Name | Yes |
| `middleName` | Middle Name | Optional |
| `company` | Company | Optional |
| `jobTitle` | Job Title | Optional |
| `email` | Email | Optional |
| `phoneNumber` | Phone Number | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/create-contact.ts).

### Add Or Remove Contact Group Members

Add contacts to a contact group or remove them from it.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceName` | Opaque contact group resource name such as contactGroups/abc123, contactGroups/myContacts or contactGroups/starred. Resolve it with List Contact Groups. | Yes |
| `resourceNamesToAdd` | Opaque contact resource names such as people/c12345 to add to the group. | Optional |
| `resourceNamesToRemove` | Opaque contact resource names such as people/c12345 to remove from the group. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/modify-contact-group-members.ts).

### Batch Create Contacts

Create up to 200 contacts in a single call.

| Input | What to provide | Required |
| --- | --- | --- |
| `contacts` | Up to 200 contacts to create. Each needs at least a name, an email or a phone number. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/batch-create-contacts.ts).

### Batch Delete Contacts

Permanently delete up to 500 contacts in a single call.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceNames` | Up to 500 opaque contact resource names such as people/c12345. Every listed contact is deleted permanently and cannot be restored. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/batch-delete-contacts.ts).

### Batch Get Contact Groups

Read up to 200 contact groups in one call by their resource names.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceNames` | Up to 200 opaque contact group resource names such as contactGroups/abc123, resolved with List Contact Groups. | Yes |
| `maxMembers` | How many member resource names to return per group. Defaults to 0, which returns none. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/batch-get-contact-groups.ts).

### Batch Get Contacts

Read up to 200 contacts in one call by their resource names.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceNames` | Up to 200 opaque contact resource names such as people/c12345, resolved with List Contacts or Search Contacts. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/batch-get-contacts.ts).

### Batch Update Contacts

Update up to 200 contacts in a single call from full Person objects.

| Input | What to provide | Required |
| --- | --- | --- |
| `contacts` | JSON array of up to 200 full Person objects taken from Batch Get Contacts, each keeping its resourceName and etag, with the fields to change edited in place. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/batch-update-contacts.ts).

### Create Contact

Create a new contact in the connected Google account.

| Input | What to provide | Required |
| --- | --- | --- |
| `firstName` | First Name | Optional |
| `middleName` | Middle Name | Optional |
| `lastName` | Last Name | Optional |
| `nickname` | Nickname | Optional |
| `emails` | Array of email address strings, for example ["ada@example.com"]. A single address still has to be wrapped in an array. | Optional |
| `phoneNumbers` | Array of phone number strings, for example ["+1 555 0100"]. A single number still has to be wrapped in an array. | Optional |
| `company` | Company | Optional |
| `jobTitle` | Job Title | Optional |
| `biography` | Free-text notes stored on the contact biography. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/create-contact-agent.ts).

### Create Contact Group

Create a contact group, or return the existing one with that name.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Name of the contact group to find or create. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/create-contact-group.ts).

### Delete Contact

Permanently delete a contact by its resource name.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceName` | Opaque contact resource name such as people/c12345. Resolve it with List Contacts or Search Contacts. Deletion cannot be undone. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/delete-contact.ts).

### Delete Contact Group

Delete a user-created contact group.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceName` | Opaque contact group resource name such as contactGroups/abc123. Resolve it with List Contact Groups. | Yes |
| `deleteContacts` | When enabled, every contact in the group is permanently deleted as well. Leave off to remove only the group. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/delete-contact-group.ts).

### Delete Contact Photo

Remove the photo of an existing contact.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceName` | Opaque contact resource name such as people/c12345. Resolve it with List Contacts or Search Contacts. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/delete-contact-photo.ts).

### Get Contact

Read a single contact by its resource name.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceName` | Opaque contact resource name such as people/c12345. Resolve it with List Contacts or Search Contacts. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/get-contact.ts).

### Get Contact Group

Read one contact group, optionally with its member resource names.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceName` | Opaque contact group resource name such as contactGroups/abc123, or a system group like contactGroups/myContacts. Resolve it with List Contact Groups. | Yes |
| `maxMembers` | How many member resource names to return. Defaults to 0, which returns none. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/get-contact-group.ts).

### List Contact Groups

List every contact group of the connected Google account.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/list-contact-groups.ts).

### List Contacts

List the contacts of the connected Google account.

| Input | What to provide | Required |
| --- | --- | --- |
| `maxResults` | Maximum number of contacts to return. Defaults to 200. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/list-contacts.ts).

### Search Contacts

Find contacts by name, email, phone number or company.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Matches the start of any word in a name, email, phone or company. | Yes |
| `readMask` | Contact details included in each result. | Yes |
| `pageSize` | How many contacts to return, up to 30. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/search-contact.ts).

### Search Contacts

Search the connected account contacts by a plain-text query.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Plain-text query prefix-matched against contact fields such as name, email and phone number. | Yes |
| `pageSize` | Number of results to return, maximum 30. Defaults to 30. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/search-contacts.ts).

### Update Contact

Change an existing contact's details in Google Contacts.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceName` | The resourceName (people/…) from Search Contacts or Add Contact. | Yes |
| `etag` | The etag returned with the Contact ID. Fails if the contact changed. | Yes |
| `updatePersonFields` | Only these fields change on the contact. | Yes |
| `updateNote` | Update Note | Optional |
| `firstName` | First Name | Optional |
| `lastName` | Last Name | Optional |
| `middleName` | Middle Name | Optional |
| `company` | Company | Optional |
| `jobTitle` | Job Title | Optional |
| `email` | Email | Optional |
| `phoneNumber` | Phone Number | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/update-contact.ts).

### Update Contact Fields

Update only the supplied fields on an existing contact.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceName` | Opaque contact resource name such as people/c12345. Resolve it with List Contacts or Search Contacts. | Yes |
| `firstName` | First Name | Optional |
| `middleName` | Middle Name | Optional |
| `lastName` | Last Name | Optional |
| `nickname` | Nickname | Optional |
| `emails` | Array of email address strings, for example ["ada@example.com"]. Replaces every email address stored on the contact. Leaving it empty keeps the stored addresses; it does not clear them, because an untouched list and an emptied one cannot be told apart. Use Clear Email Addresses to remove them. | Optional |
| `clearEmails` | Remove every email address from the contact, including the last one. This is the only way to clear them. Cannot be combined with a non-empty Email Addresses list. | Optional |
| `phoneNumbers` | Array of phone number strings, for example ["+1 555 0100"]. Replaces every phone number stored on the contact. Leaving it empty keeps the stored numbers; it does not clear them, because an untouched list and an emptied one cannot be told apart. Use Clear Phone Numbers to remove them. | Optional |
| `clearPhoneNumbers` | Remove every phone number from the contact, including the last one. This is the only way to clear them. Cannot be combined with a non-empty Phone Numbers list. | Optional |
| `company` | Company | Optional |
| `jobTitle` | Job Title | Optional |
| `biography` | Notes | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/update-contact-fields.ts).

### Update Contact Group

Rename an existing user-created contact group.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceName` | Opaque contact group resource name such as contactGroups/abc123. Resolve it with List Contact Groups. | Yes |
| `name` | New Group Name | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/update-contact-group.ts).

### Update Contact Photo

Set the photo of an existing contact from base64 image bytes.

| Input | What to provide | Required |
| --- | --- | --- |
| `resourceName` | Opaque contact resource name such as people/c12345. Resolve it with List Contacts or Search Contacts. | Yes |
| `photoBytes` | Base64-encoded JPEG, PNG or WebP image. A data URL prefix is accepted and stripped. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/action/update-contact-photo.ts).

## Events and recurring work

- **[New or Updated Contact](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-contacts/src/lib/trigger/new-contact.ts)** — Runs when a contact is added or edited in Google Contacts.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Google Contacts to batch get contact groups. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
