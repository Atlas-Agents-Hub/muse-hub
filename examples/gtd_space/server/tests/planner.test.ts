import { afterEach, expect, test } from "bun:test";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { openLocalRuntime } from "../../scripts/local-runtime";
import { migrateDatabase } from "../../scripts/migrate";
import { backupSchema } from "../src/backup";
import type { ActionResponse } from "@hatch/space-sdk";
import { Actions } from "../src/actions";

type Runtime = Awaited<ReturnType<typeof openLocalRuntime>>;
const paths: string[] = [];
const runtimes: Runtime[] = [];
afterEach(async () => { for (const runtime of runtimes.splice(0)) runtime.close(); for (const path of paths.splice(0)) { if (process.platform !== "win32" || !process.env.PLANNER_TEST_ROOT) await rm(path, { recursive: true, force: true, maxRetries: 8, retryDelay: 100 }); } });
async function fresh() {
  const path = await mkdtemp(join(process.env.PLANNER_TEST_ROOT ?? tmpdir(), "muse-planner-test-")); paths.push(path);
  const filename = join(path, "planner.db");
  const runtime = await openLocalRuntime(filename); runtimes.push(runtime);
  return { runtime, filename };
}
async function call<K extends keyof typeof Actions>(runtime: Runtime, name: K, args: unknown = {}) {
  return await runtime.dispatch(name, args) as ActionResponse<(typeof Actions)[K]>;
}

test("fresh workspace needs no calendar configuration and migrations reopen idempotently", async () => {
  const { runtime, filename } = await fresh();
  const workspace = await call(runtime, "listWorkspace");
  expect(workspace.row_count).toBe(0);
  expect(workspace.daily_items).toEqual([]);
  expect(workspace.weekly_items).toEqual([]);
  expect(workspace.calendar_settings.enabled).toEqual([]);
  expect(workspace.calendar_settings.labels.intent).toBe("Focus time");
  expect(migrateDatabase(filename).applied).toBe(0);
  await expect(runtime.dispatch("__proto__")).rejects.toThrow("Unknown Planner action");
});

test("projects, actions, notes, schedules and routine history survive close and reopen", async () => {
  const { runtime, filename } = await fresh();
  const client = await call(runtime, "saveClient", { name: "Design studio" });
  const project = await call(runtime, "saveProject", { title: "Launch café site", client_id: client.id, outcome: "Launch page and booking form" });
  const action = await call(runtime, "saveNextAction", { title: "Review → publish", project_id: project.id, context: "computer", priority: "A" });
  await call(runtime, "saveInbox", { title: "Capture λ idea" });
  await call(runtime, "saveReference", { title: "Brief", url: "https://example.com/brief", notes: "<script>render as text</script>" });
  await call(runtime, "saveSomeday", { title: "Build a newsletter" });
  await call(runtime, "saveTickler", { title: "Revisit designs", remind_on: "2026-11-20" });
  await call(runtime, "saveScheduledItem", { title: "Focus on layout", scheduled_date: "2026-11-19", start_time: "09:00", end_time: "10:00" });
  const daily = await call(runtime, "saveDailyItem", { name: "Review inbox" });
  const weekly = await call(runtime, "saveWeeklyItem", { name: "Weekly review" });
  await call(runtime, "recordDailyResult", { item_id: daily.item_id, date: "2026-11-19", passed: true });
  await call(runtime, "recordWeeklyResult", { item_id: weekly.item_id, week: "2026-11-16", passed: true });
  await call(runtime, "setItemStatus", { kind: "action", id: action.id, done: true });
  const before = await call(runtime, "exportWorkspace");
  runtime.close(); runtimes.splice(runtimes.indexOf(runtime), 1);
  const reopened = await openLocalRuntime(filename); runtimes.push(reopened);
  const workspace = await call(reopened, "listWorkspace", { daily_date: "2026-11-19" });
  expect(workspace.row_count).toBe(8);
  expect(workspace.projects[0]?.client_name).toBe("Design studio");
  expect(workspace.actions[0]?.project_title).toBe("Launch café site");
  expect(workspace.actions[0]?.status).toBe("completed");
  expect(workspace.daily_items[0]?.today_passed).toBe(true);
  expect(workspace.weekly_items[0]?.this_week_passed).toBe(true);
  expect((await call(reopened, "exportWorkspace")).backup.tables).toEqual(before.backup.tables);
  await call(reopened, "setItemStatus", { kind: "action", id: action.id, done: false });
  await call(reopened, "deleteItem", { kind: "project", id: project.id });
  expect((await call(reopened, "listWorkspace")).actions[0]?.project_id).toBeNull();
});

test("backup restores all records atomically and rejects stale or invalid imports", async () => {
  const { runtime } = await fresh();
  const project = await call(runtime, "saveProject", { title: "Keep project" });
  await call(runtime, "saveNextAction", { title: "Linked action", project_id: project.id });
  const saved = await call(runtime, "exportWorkspace");
  await call(runtime, "saveInbox", { title: "New work" });
  const changed = await call(runtime, "exportWorkspace");
  const stale = await call(runtime, "restoreWorkspace", { expected_revision: saved.revision, backup: saved.backup });
  expect(stale.ok).toBe(false); expect(stale.error).toContain("changed");
  expect((await call(runtime, "listWorkspace")).inbox[0]?.title).toBe("New work");
  const invalid = structuredClone(saved.backup);
  invalid.tables.next_actions![0]!.project_id = 99999;
  const rejected = await call(runtime, "restoreWorkspace", { expected_revision: changed.revision, backup: invalid });
  expect(rejected.ok).toBe(false);
  expect((await call(runtime, "exportWorkspace")).backup.tables).toEqual(changed.backup.tables);
  expect((await call(runtime, "restoreWorkspace", { expected_revision: changed.revision, backup: saved.backup })).ok).toBe(true);
  expect((await call(runtime, "exportWorkspace")).backup.tables).toEqual(saved.backup.tables);
  const duplicate = structuredClone(saved.backup); duplicate.tables.projects!.push(duplicate.tables.projects![0]!);
  expect(backupSchema.safeParse(duplicate).success).toBe(false);
  const unsafeUrl = structuredClone(saved.backup); unsafeUrl.tables.projects![0]!.url = "javascript:alert(1)";
  expect(backupSchema.safeParse(unsafeUrl).success).toBe(false);
});

test("concurrent captures and repeated routine results preserve every row and preference", async () => {
  const { runtime, filename } = await fresh();
  const other = await openLocalRuntime(filename); runtimes.push(other);
  await Promise.all(Array.from({ length: 24 }, (_, index) => call(index % 2 ? other : runtime, "saveInbox", { title: `Capture ${index}` })));
  expect((await call(runtime, "listWorkspace")).inbox).toHaveLength(24);
  const daily = await call(runtime, "saveDailyItem", { name: "Check inbox" });
  const weekly = await call(runtime, "saveWeeklyItem", { name: "Review week" });
  await Promise.all(Array.from({ length: 12 }, (_, index) => call(index % 2 ? other : runtime, "recordDailyResult", { item_id: daily.item_id, date: "2026-11-19", passed: true })));
  await Promise.all(Array.from({ length: 12 }, (_, index) => call(index % 2 ? other : runtime, "recordWeeklyResult", { item_id: weekly.item_id, week: "2026-11-16", passed: true })));
  await Promise.all([call(runtime, "setCalendarVisibility", { calendar: "primary", visible: false }), call(other, "setCalendarVisibility", { calendar: "shared", visible: false })]);
  const backup = await call(runtime, "exportWorkspace");
  expect(backup.backup.tables.daily_results).toHaveLength(1);
  expect(backup.backup.tables.weekly_results).toHaveLength(1);
  expect((await call(runtime, "listWorkspace")).calendar_visibility).toEqual({ primary: false, intent: true, shared: false });
  const attempts = await Promise.all([call(runtime, "restoreWorkspace", { expected_revision: backup.revision, backup: backup.backup }), call(other, "restoreWorkspace", { expected_revision: backup.revision, backup: backup.backup })]);
  expect(attempts.filter(result => result.ok)).toHaveLength(1);
  expect((await call(runtime, "listWorkspace")).inbox).toHaveLength(24);
});

test("calendar cache keeps identical IDs from separate calendars and preserves the last complete pull on failure", async () => {
  const { runtime, filename } = await fresh();
  runtime.close(); runtimes.splice(runtimes.indexOf(runtime), 1);
  const { createCalendarHandlers } = await import("../src/privileged");
  let broken = false;
  const handlers = createCalendarHandlers(async (_method, params) => {
    if (broken) throw new Error("provider connection unavailable");
    return { items: [{ id: "same-provider-id", summary: String(params.calendarId), start: { dateTime: "2026-11-19T09:00:00Z" }, end: { dateTime: "2026-11-19T10:00:00Z" } }] };
  }, () => ({ primary: { id: "My calendar", label: "Personal" }, shared: { id: "Team calendar", label: "Team" } }));
  const app = await openLocalRuntime(filename, handlers); runtimes.push(app);
  expect((await call(app, "syncCalendarWeek", { week_start: "2026-11-16" })).ok).toBe(true);
  let workspace = await call(app, "listWorkspace", { daily_date: "2026-11-19" });
  expect(workspace.calendar_events).toHaveLength(2);
  expect(new Set(workspace.calendar_events.map(event => event.calendar_name)).size).toBe(2);
  broken = true;
  expect((await call(app, "syncCalendarWeek", { week_start: "2026-11-16" })).ok).toBe(false);
  workspace = await call(app, "listWorkspace", { daily_date: "2026-11-19" });
  expect(workspace.calendar_events).toHaveLength(2);
  expect(workspace.calendar_sync.status).toBe("error");
});
