---
name: mongodb-connector
description: "MongoDB: aggregate documents, delete documents, find and replace documents."
---

# MongoDB for Muse

MongoDB: aggregate documents, delete documents, find and replace documents.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **MongoDB**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Host** (`host`): The hostname or address of the MongoDB server (e.g., localhost:27017 or cluster.example.mongodb.net)
- **Use MongoDB Atlas URL Format** (`useAtlasUrl`): Enable this if connecting to MongoDB Atlas (uses mongodb+srv:// protocol)
- **Database** (`database`): The MongoDB database to connect to (can be specified per action if left empty)
- **Username** (`username`): The username to use for connecting to the MongoDB server
- **Password** (`password`): ProviderField
- **Auth Source** (`authSource`): The database to authenticate against (default: admin)

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mongodb/src/index.ts).

## Actions

### Aggregate Documents

Perform aggregation operations on documents in a collection

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `collection` | Collection | See action definition |
| `pipeline` | Array of aggregation stages (e.g., [{"$match": {"status": "active"}}, {"$group": {"_id": "$category", "count": {"$sum": 1}}}]) | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mongodb/src/lib/actions/aggregate-documents.ts).

### Delete Documents

Delete documents from a collection

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `collection` | Collection | See action definition |
| `filter` | MongoDB query to select documents to delete (e.g., {"status": "archived"}) | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mongodb/src/lib/actions/delete-documents.ts).

### Find and Replace Documents

Replace documents that match a filter with a new document

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `collection` | Collection | See action definition |
| `filter` | MongoDB query to select documents to replace (e.g., {"_id": "123"}) | Yes |
| `replacement` | New document that will replace the matched documents | Yes |
| `upsert` | Insert the document if no documents match the filter | Optional |
| `returnDocument` | Which version of the document to return | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mongodb/src/lib/actions/find-and-replace-documents.ts).

### Find and Update Documents

Find documents and update them, returning the updated documents

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `collection` | Collection | See action definition |
| `filter` | MongoDB query to select documents to update (e.g., {"status": "pending"}) | Yes |
| `update` | MongoDB update operations (e.g., {"$set": {"status": "completed"}}) | Yes |
| `upsert` | Insert a document if no documents match the filter | Optional |
| `returnUpdated` | Return the documents after updates are applied | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mongodb/src/lib/actions/find-and-update-documents.ts).

### Find Documents

Find documents in a collection

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `collection` | Collection | See action definition |
| `query` | MongoDB query to filter documents (e.g., {"status": "active"}) | Optional |
| `projection` | Fields to include or exclude (e.g., {"name": 1, "_id": 0}) | Optional |
| `sort` | Sort criteria (e.g., {"createdAt": -1}) | Optional |
| `limit` | Maximum number of documents to return | Optional |
| `skip` | Number of documents to skip | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mongodb/src/lib/actions/find-documents.ts).

### Insert Documents

Insert one or more documents into a collection

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `collection` | Collection | See action definition |
| `documents` | Document(s) to insert. Can be a single document object or an array of documents. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mongodb/src/lib/actions/insert-documents.ts).

### Update Documents

Update multiple documents in a collection

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `collection` | Collection | See action definition |
| `filter` | MongoDB query to select documents to update (e.g., {"status": "pending"}) | Yes |
| `update` | MongoDB update operations (e.g., {"$set": {"status": "completed"}}) | Yes |
| `upsert` | Insert a document if no documents match the filter | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mongodb/src/lib/actions/update-documents.ts).

## Try it

> Use MongoDB to find and replace documents. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
