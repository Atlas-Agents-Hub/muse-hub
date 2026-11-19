import { expect, test } from "bun:test";
import { createHash } from "node:crypto";
import { createCalendarHandlers } from "../src/privileged";
import { CalendarAdapterError, runBounded, type CalendarRunner } from "../src/calendar-runner";
import { readCalendarSettings, publicCalendarSettings } from "../src/calendar-settings";
import { privileged } from "../src/calendar-contracts";

const windowArgs = { time_min: "2026-11-18T00:00:00Z", time_max: "2026-11-27T00:00:00Z" };
async function invoke(name: keyof typeof privileged, args: unknown, runner: CalendarRunner, config = {}) {
  const handlers = createCalendarHandlers(runner, () => config);
  const entry = handlers.entries.find(entry => entry.contract.name === name)!;
  return entry.contract.response.parse(await entry.handler(entry.contract.request.parse(args))) as Record<string, any>;
}
const event = { id: "event42", summary: "Focus → finish", start: { dateTime: "2026-11-19T10:00:00+02:00" }, end: { dateTime: "2026-11-19T11:00:00+02:00" } };

test("calendar is optional, validates configuration, and exposes labels without IDs", () => {
  expect(readCalendarSettings("")).toEqual({});
  const config = readCalendarSettings(JSON.stringify({ intent: { id: "private-calendar-id", label: "Writing blocks" } }));
  const visible = publicCalendarSettings(config);
  expect(visible.enabled).toEqual(["intent"]); expect(visible.labels.intent).toBe("Writing blocks");
  expect(JSON.stringify(visible)).not.toContain("private-calendar-id");
  for (const value of ["[]", "{", '{"unknown":{"id":"x"}}', '{"primary":{"id":""}}', '{"primary":{"id":"x","label":""}}']) expect(() => readCalendarSettings(value)).toThrow();
});

test("disconnected calendars never start a command and malformed config cannot block the workspace", async () => {
  let calls = 0;
  const runner: CalendarRunner = async () => { calls += 1; return {}; };
  expect((await invoke("readCalendarWindow", windowArgs, runner)).ok).toBe(false);
  expect((await invoke("writeIntentCalendarEvent", { operation: "delete", event_id: "abc" }, runner)).ok).toBe(false);
  expect(calls).toBe(0);
  const handlers = createCalendarHandlers(runner, () => { throw new Error("bad setting"); });
  const entry = handlers.entries.find(entry => entry.contract.name === "getCalendarSettings")!;
  expect(await entry.handler({})).toEqual(publicCalendarSettings({}));
});

test("read follows bounded pagination for configured calendars and rejects truncation", async () => {
  const calls: Record<string, unknown>[] = [];
  const runner: CalendarRunner = async (_method, args) => { calls.push(args); return args.pageToken ? { items: [{ ...event, id: "event43" }] } : { items: [event], nextPageToken: "page2" }; };
  const result = await invoke("readCalendarWindow", windowArgs, runner, { shared: { id: "only-this", label: "Team" } });
  expect(result.ok).toBe(true); expect(result.events).toHaveLength(2); expect(calls).toHaveLength(2);
  expect(calls.every(call => call.calendarId === "only-this")).toBe(true);
  expect(result.events[0].calendar_name).toBe("shared");
  const oversized = await invoke("readCalendarWindow", windowArgs, async () => ({ items: [event], nextPageToken: "more" }), { primary: { id: "x", label: "Main" } });
  expect(oversized.ok).toBe(false); expect(oversized.events).toEqual([]);
  const invalidRange = await invoke("readCalendarWindow", { ...windowArgs, time_max: "2027-11-19T00:00:00Z" }, runner, { primary: { id: "x", label: "Main" } });
  expect(invalidRange.ok).toBe(false);
});

test("create uses a stable provider ID and reconciles a confirmed duplicate", async () => {
  const operationKey = "9f1b12f1-cb6f-41fa-9383-66547f07a0d2";
  const id = createHash("sha256").update(operationKey).digest("hex");
  const calls: { method: string; params: Record<string, unknown>; body?: Record<string, unknown> }[] = [];
  const runner: CalendarRunner = async (method, params, body) => {
    calls.push({ method, params, body });
    if (method === "insert") throw new CalendarAdapterError("provider", 409);
    return { ...event, id };
  };
  const result = await invoke("writeIntentCalendarEvent", { operation: "create", operation_key: operationKey, title: "Focus", start_time: event.start.dateTime, end_time: event.end.dateTime }, runner, { intent: { id: "focus-id", label: "Focus" } });
  expect(result.ok).toBe(true); expect(calls.map(call => call.method)).toEqual(["insert", "get"]);
  expect(calls[0]?.body?.id).toBe(id); expect(calls[1]?.params.eventId).toBe(id);
});

test("delete accepts an empty successful response and write errors report uncertain outcomes without secrets", async () => {
  const config = { intent: { id: "focus-id", label: "Focus" } };
  const success = await invoke("writeIntentCalendarEvent", { operation: "delete", event_id: "event42" }, async () => ({}), config);
  expect(success.ok).toBe(true);
  const alreadyGone = await invoke("writeIntentCalendarEvent", { operation: "delete", event_id: "event42" }, async () => { throw new CalendarAdapterError("provider", 404); }, config);
  expect(alreadyGone.ok).toBe(true);
  const failure = await invoke("writeIntentCalendarEvent", { operation: "delete", event_id: "event42" }, async () => { throw new Error("account private@example.com secret_token"); }, config);
  expect(failure.ok).toBe(false); expect(failure.outcome_unknown).toBe(true);
  expect(JSON.stringify(failure)).not.toContain("secret_token"); expect(JSON.stringify(failure)).not.toContain("private@example.com");
});

test("actual subprocess boundary caps output, terminates timeout, and never interprets shell arguments", async () => {
  const literal = "$(not-a-command); 'quoted' → value";
  const output = await runBounded(process.execPath, ["-e", "process.stdout.write(process.argv[1])", literal]);
  expect(output).toBe(literal);
  const start = Date.now();
  await expect(runBounded(process.execPath, ["-e", "setInterval(() => {}, 1000)"], 150)).rejects.toThrow("timeout");
  expect(Date.now() - start).toBeLessThan(3000);
  await expect(runBounded(process.execPath, ["-e", "process.stdout.write('x'.repeat(100000))"], 1000, 1024)).rejects.toThrow("output");
  await expect(runBounded("muse-planner-command-that-does-not-exist", [])).rejects.toThrow("unavailable");
});
