/** Run SQLite tests in a child so native file handles close before cleanup on Windows. */
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
const targets = process.argv.slice(2);
if (targets.length !== 1 || !["server/tests", "tests/preview.test.ts"].includes(targets[0]!)) throw new Error("Choose the server or preview test target.");
const root = await mkdtemp(join(tmpdir(), "muse-planner-suite-"));
const child = Bun.spawn([process.execPath, "test", ...targets], {
  env: { ...process.env, PLANNER_TEST_ROOT: root }, stdin: "ignore", stdout: "inherit", stderr: "inherit",
});
const timer = setTimeout(() => child.kill("SIGKILL"), 90_000);
try { process.exitCode = await child.exited; }
finally {
  clearTimeout(timer);
  await rm(root, { recursive: true, force: true, maxRetries: 8, retryDelay: 100 });
}
