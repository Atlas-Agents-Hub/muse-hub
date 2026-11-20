import { createClient } from "@libsql/client";
import { drizzle } from "drizzle-orm/libsql";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";
import { createPrivilegedExecutor, type Ctx, type PrivilegedHandlers } from "@hatch/space-sdk";
import { Actions } from "../server/src/actions";
import { privilegedHandlers } from "../server/src/privileged";
import * as schema from "../server/src/schema";
import { APP_ROOT, migrateDatabase } from "./migrate";

export async function openLocalRuntime(path: string, handlers: PrivilegedHandlers = privilegedHandlers) {
  const absolutePath = resolve(path);
  migrateDatabase(absolutePath);
  const client = createClient({ url: pathToFileURL(absolutePath).href });
  await client.executeMultiple("PRAGMA foreign_keys = ON; PRAGMA busy_timeout = 5000;");
  const db = drizzle(client, { schema });
  async function dispatch(name: string, input: unknown = {}): Promise<unknown> {
    if (!Object.hasOwn(Actions, name)) throw new Error("Unknown Planner action.");
    const action = Actions[name as keyof typeof Actions];
    const args = action.request.parse(input);
    const executor = createPrivilegedExecutor("privileged" in action ? action.privileged : undefined, async (contract, payload) => {
      // Native and preview bundles create separate descriptor objects; names
      // are the SDK's documented contract identity across bundle boundaries.
      const entry = handlers.entries.find(entry => entry.contract.name === contract.name);
      if (!entry) throw new Error("No handler for this declared privileged action.");
      return entry.handler(payload);
    });
    const ctx = { slug: "muse-planner", invocationId: crypto.randomUUID(), spaceDir: APP_ROOT,
      db: () => db, ...executor, blobs: {}, emit: () => {}, invalidateQueries: () => {} } as unknown as Ctx;
    // Each action validates its own request/response. The generic dispatch
    // boundary intentionally erases only the union of individual handler types.
    const handler = action.handler as (context: Ctx, payload: unknown) => Promise<unknown>;
    return action.response.parse(await handler(ctx, args));
  }
  return { client, db, dispatch, close: () => client.close() };
}
