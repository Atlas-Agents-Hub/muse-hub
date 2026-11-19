import { expect, test } from "bun:test";
import { mkdtemp, rm, symlink, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { servePlanner } from "../scripts/serve-standalone";
import { APP_ROOT } from "../scripts/migrate";

test("loopback preview serves its bundle and persists API edits while rejecting cross-origin and malformed writes", async () => {
  const root = await mkdtemp(join(process.env.PLANNER_TEST_ROOT ?? tmpdir(), "planner-http-test-"));
  const app = await servePlanner({ port: 0, dbPath: join(root, "planner.db") });
  const send = (action: string, args: unknown = {}, headers = {}) => fetch(new URL("actions", app.url), { method: "POST", headers: { "content-type": "application/json", ...headers }, body: JSON.stringify({ action, args }) });
  try {
    const index = await fetch(app.url); expect(index.status).toBe(200);
    const html = await index.text(); expect(html).toContain("Muse Planner");
    for (const src of [...html.matchAll(/(?:src|href)="([^"#]+\.(?:js|css))"/g)].map(match => match[1]!)) expect((await fetch(new URL(src, app.url))).status).toBe(200);
    const saved = await (await send("saveInbox", { title: "Saved from HTTP → café" })).json() as any;
    expect(saved.data.ok).toBe(true);
    const workspace = await (await send("listWorkspace")).json() as any;
    expect(workspace.data.inbox[0].title).toBe("Saved from HTTP → café");
    expect(workspace.data.calendar_settings.enabled).toEqual([]);
    expect((await send("saveInbox", { title: "Blocked" }, { origin: "https://unrelated.example" })).status).toBe(403);
    expect((await send("saveInbox", { title: "Blocked" }, { host: "rebind.example" })).status).toBe(403);
    expect((await send("saveInbox", { title: "" })).status).toBe(400);
    expect((await fetch(new URL("actions", app.url))).status).toBe(405);
    expect((await fetch(new URL("actions", app.url), { method: "POST", body: "{}" })).status).toBe(415);
    const prototype = await send("__proto__"); expect(prototype.status).toBe(500);
    expect(await prototype.text()).not.toContain("handler");
    try {
      const oversized = await fetch(new URL("actions", app.url), { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ action: "saveInbox", args: { title: "x".repeat(5 * 1024 * 1024) } }) });
      expect(oversized.status).toBe(413);
    } catch (error) {
      // Bun on Windows closes the upload socket at its body limit. The final
      // workspace read below also checks that rejection caused no write.
      if (process.platform !== "win32") throw error;
      expect((error as { code?: string }).code).toBe("ECONNRESET");
    }
    const secret = join(root, "outside.txt"), link = join(APP_ROOT, "client", "dist", "planner-http-test-link.txt");
    await writeFile(secret, "must remain outside served files");
    try {
      if (process.platform !== "win32") {
      await symlink(secret, link);
      expect((await fetch(new URL("planner-http-test-link.txt", app.url))).status).toBe(404);
      }
    } finally { await rm(link, { force: true }); }
    expect((await fetch(new URL("%2e%2e/server/src/actions.ts", app.url))).status).toBe(404);
    const final = await (await send("listWorkspace")).json() as any;
    expect(final.data.inbox).toHaveLength(1);
  } finally { app.stop(); if (process.platform !== "win32" || !process.env.PLANNER_TEST_ROOT) await rm(root, { recursive: true, force: true, maxRetries: 8, retryDelay: 100 }); }
});
