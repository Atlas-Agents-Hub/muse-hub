---
name: qdrant-connector
description: "Make any action on your qdrant vector database"
---

# Qdrant for Muse

Make any action on your qdrant vector database

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Qdrant**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Server Address** (`serverAddress`): The url of the Qdrant instance.
- **Key** (`key`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/qdrant/src/index.ts).

## Actions

### Add points to collection

Insert a point (= embedding or vector + other infos) to a specific collection, if the collection does not exist it will be created

| Input | What to provide | Required |
| --- | --- | --- |
| `collectionName` | Collection Name | See action definition |
| `embeddings` | Embeddings (= vectors) for the points | Yes |
| `embeddingsIds` | The ids of the embeddings for the points. If not provided, the ids will be generated automatically | Optional |
| `distance` | Distance | See action definition |
| `payload` | Please follow [payload documentation](https://qdrant.tech/documentation/concepts/payload/) to add additional information to the points. | Optional |
| `storage` | Define where points will be stored | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/qdrant/src/lib/actions/add-points.ts).

### Delete Collection

Delete a collection of your database

| Input | What to provide | Required |
| --- | --- | --- |
| `collectionName` | Collection Name | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/qdrant/src/lib/actions/delete-collection.ts).

### Delete Points

Delete points of a specific collection

| Input | What to provide | Required |
| --- | --- | --- |
| `collectionName` | Collection Name | See action definition |
| `getPointsBy` | Get Points By | See action definition |
| `infosToGetPoint` | Infos To Get Point | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/qdrant/src/lib/actions/delete-points.ts).

### Get Collection Infos

Get the all the infos of a specific collection

| Input | What to provide | Required |
| --- | --- | --- |
| `collectionName` | Collection Name | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/qdrant/src/lib/actions/get-collection-infos.ts).

### Get Collection List

Get the list of all the collections of your database

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/qdrant/src/lib/actions/get-collection-list.ts).

### Get Points

Get the points of a specific collection

| Input | What to provide | Required |
| --- | --- | --- |
| `collectionName` | Collection Name | See action definition |
| `getPointsBy` | Get Points By | See action definition |
| `infosToGetPoint` | Infos To Get Point | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/qdrant/src/lib/actions/get-points.ts).

### Search Points

Search for points closest to your given vector (= embedding)

| Input | What to provide | Required |
| --- | --- | --- |
| `collectionName` | Collection Name | See action definition |
| `vector` | The vector (= embedding) you want to search for. | Yes |
| `must` | Must | See action definition |
| `must_not` | Must_Not | See action definition |
| `negativeVector` | The vector (= embedding) you want to be the farthest. | Optional |
| `limitResult` | The max number of results you want to get. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/qdrant/src/lib/actions/search-points.ts).

## Try it

> Use Qdrant to get collection infos. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
