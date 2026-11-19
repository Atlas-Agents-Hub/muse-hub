import { execFile } from "node:child_process";

export class CalendarAdapterError extends Error {
  constructor(readonly reason: "unavailable" | "timeout" | "output" | "provider" | "invalid", readonly providerStatus?: number) {
    super(`Calendar adapter ${reason}`);
  }
}

export type CalendarRunner = (method: "list" | "insert" | "patch" | "delete" | "get", params: Record<string, unknown>, body?: Record<string, unknown>) => Promise<Record<string, unknown>>;

/** Fixed executable and argument vector: no shell interpolation or unlimited output. */
export function runBounded(command: string, args: string[], timeoutMs = 6_000, maxBuffer = 1_048_576): Promise<string> {
  return new Promise((resolve, reject) => {
    execFile(command, args, { timeout: timeoutMs, maxBuffer, encoding: "utf8", killSignal: "SIGKILL", windowsHide: true }, (error, stdout, stderr) => {
      if (error) {
        const detail = error as NodeJS.ErrnoException & { killed?: boolean };
        let status: number | undefined;
        try {
          const response = JSON.parse(stderr.slice(0, 8192)) as { error?: { code?: number }; code?: number };
          status = response.error?.code ?? response.code;
        } catch { /* Never return raw command errors, which may contain account data. */ }
        reject(new CalendarAdapterError(detail.code === "ENOENT" ? "unavailable" : detail.code === "ERR_CHILD_PROCESS_STDIO_MAXBUFFER" ? "output" : detail.killed ? "timeout" : "provider", status));
        return;
      }
      resolve(stdout);
    });
  });
}

export const runCalendar: CalendarRunner = async (method, params, body) => {
  const args = ["calendar", "events", method, "--params", JSON.stringify(params)];
  if (body) args.push("--json", JSON.stringify(body));
  const stdout = await runBounded("hatch_gws_cli", args);
  if (method === "delete" && !stdout.trim()) return {};
  let parsed: unknown;
  try { parsed = JSON.parse(stdout); } catch { throw new CalendarAdapterError("invalid"); }
  if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) throw new CalendarAdapterError("invalid");
  return parsed as Record<string, unknown>;
};
