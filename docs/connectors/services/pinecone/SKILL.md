---
name: pinecone-connector
description: "Manage vector databases, store embeddings, and perform similarity searches"
---

# Pinecone for Muse

Manage vector databases, store embeddings, and perform similarity searches

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Pinecone**.
2. Configure **Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **API Key** (`apiKey`): Enter your Pinecone API key. You can create a new API key in the Pinecone console for your target project.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinecone/src/index.ts).

## Actions

### Create Index

Creates a new Pinecone index with custom settings.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | You must pass a non-empty string for name in order to create an index | Yes |
| `dimension` | You must pass a positive integer for dimension in order to create an index. For dense indexes, this is required. | Yes |
| `indexType` | Choose between serverless or pod-based index deployment | Yes |
| `cloud` | Cloud | See action definition |
| `region` | The region where you would like your index to be created (for serverless) | Optional |
| `environment` | The environment where the index is hosted (for pod-based indexes) | Optional |
| `podType` | The type of pod to use | Optional |
| `replicas` | The number of replicas. Replicas duplicate your index for higher availability and throughput. | Optional |
| `shards` | The number of shards. Shards split your data across multiple pods. | Optional |
| `pods` | The number of pods to be used in the index. This should be equal to shards x replicas. | Optional |
| `metric` | Metric | See action definition |
| `vectorType` | Vector Type | See action definition |
| `deletionProtection` | Enable deletion protection for the index | Optional |
| `waitUntilReady` | Wait until the index is ready to receive data before completing | Optional |
| `suppressConflicts` | Do not throw if you attempt to create an index that already exists | Optional |
| `tags` | Optional tags for the index (e.g., {"team": "data-science"}) | Optional |
| `sourceCollection` | The name of the collection to be used as the source for the index | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinecone/src/lib/actions/create-index.ts).

### Delete a Vector

Delete vectors by ID from a namespace.

| Input | What to provide | Required |
| --- | --- | --- |
| `indexName` | The name of the index to delete vectors from | Yes |
| `indexHost` | The unique host for the index (optional, see Pinecone docs for targeting an index) | Optional |
| `namespace` | The namespace to delete vectors from (e.g., "example-namespace") | Optional |
| `deleteMode` | Choose how to delete vectors | Yes |
| `id` | The ID of the vector to delete (for single vector deletion) | Optional |
| `ids` | Array of vector IDs to delete (e.g., ["id-2", "id-3"]) | Optional |
| `confirmDeleteAll` | Check this box to confirm you want to delete ALL vectors in the namespace | Optional |
| `filter` | Metadata filter expression to select vectors to delete. Examples: • {"genre": {"$eq": "documentary"}} • {"year": {"$gt": 2019}} • {"$and": [{"genre": "comedy"}, {"year": {"$gte": 2020}}]} | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinecone/src/lib/actions/delete-vector.ts).

### Get a Vector

Look up and return vectors by ID from a namespace.

| Input | What to provide | Required |
| --- | --- | --- |
| `indexName` | The name of the index to fetch vectors from | Yes |
| `indexHost` | The unique host for the index (optional, see Pinecone docs for targeting an index) | Optional |
| `ids` | The vector IDs to fetch. Does not accept values containing spaces (e.g., ["id-1", "id-2"]) | Yes |
| `namespace` | The namespace containing the vectors to fetch (e.g., "example-namespace") | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinecone/src/lib/actions/get-vector.ts).

### Search Index

Search indexes by name or list all indexes in your project.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchMode` | Choose how to search for indexes | Yes |
| `indexName` | The name of the specific index to search for (when using Find Specific Index mode) | Optional |
| `nameFilter` | Filter indexes by name (partial match, case-insensitive) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinecone/src/lib/actions/search-index.ts).

### Search Vectors

Search a namespace using a query vector to find similar records.

| Input | What to provide | Required |
| --- | --- | --- |
| `indexName` | The name of the index to search in | Yes |
| `indexHost` | The unique host for the index (optional, see Pinecone docs for targeting an index) | Optional |
| `topK` | The number of results to return for each query (range: 1-10000) | Yes |
| `namespace` | The namespace to query (e.g., "example-namespace") | Optional |
| `queryMethod` | Choose how to provide the query | Yes |
| `vector` | The query vector. This should be the same length as the dimension of the index (e.g., [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]) | Optional |
| `id` | The unique ID of the vector to be used as a query vector (max length: 512) | Optional |
| `sparseIndices` | Array of indices for sparse vector data (optional) | Optional |
| `sparseValues` | Array of sparse values corresponding to indices (must be same length as indices) | Optional |
| `filter` | Filter to apply using vector metadata. Examples: • {"genre": {"$eq": "documentary"}} • {"year": {"$gt": 2019}} • {"$and": [{"genre": {"$in": ["comedy", "drama"]}}, {"year": {"$gte": 2020}}]} | Optional |
| `includeValues` | Whether vector values are included in the response | Optional |
| `includeMetadata` | Whether metadata is included in the response | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinecone/src/lib/actions/search-vector.ts).

### Update a Vector

Updates a vector in a namespace. Overwrites existing values and metadata.

| Input | What to provide | Required |
| --- | --- | --- |
| `indexName` | The name of the index containing the vector to update | Yes |
| `indexHost` | The unique host for the index (optional, see Pinecone docs for targeting an index) | Optional |
| `id` | Vector's unique id (required, string length: 1 - 512) | Yes |
| `namespace` | The namespace containing the vector to update (e.g., "example-namespace") | Optional |
| `values` | Vector data to update (e.g., [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]) | Optional |
| `sparseIndices` | Array of indices for sparse values (optional) | Optional |
| `sparseValues` | Array of sparse values corresponding to indices (must be same length as indices) | Optional |
| `metadata` | Key-value pairs to set for the vector | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinecone/src/lib/actions/update-vector.ts).

### Upsert Vector

Upsert vectors into a namespace. Overwrites existing vectors with the same ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `indexName` | The name of the index to upsert vectors into | Yes |
| `indexHost` | The unique host for the index (optional, see Pinecone docs for targeting an index) | Optional |
| `namespace` | The namespace where you upsert vectors (e.g., "example-namespace") | Optional |
| `vectorsInput` | Choose how to provide vector data | Yes |
| `id` | The unique identifier for the vector (e.g., "vec1") | Optional |
| `values` | Array of numbers representing the vector (e.g., [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]) | Optional |
| `vectors` | Array of vectors to upsert (for multiple vectors input) | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pinecone/src/lib/actions/upsert-vector.ts).

## Try it

> Use Pinecone to get a vector. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
