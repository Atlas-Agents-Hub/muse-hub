import { realpath } from "node:fs/promises";
import { extname, resolve, sep } from "node:path";
import { openLocalRuntime } from "./local-runtime";
import { APP_ROOT } from "./migrate";

const MAX_REQUEST = 4 * 1024 * 1024 + 16 * 1024;
export async function servePlanner(options: { dbPath?: string; port?: number } = {}) {
  const port = options.port ?? Number(process.env.PORT ?? 8479);
  if (!Number.isInteger(port) || port < 0 || port > 65535) throw new Error("PORT must be an integer from 0 to 65535.");
  const runtime = await openLocalRuntime(options.dbPath ?? process.env.GTD_DB ?? resolve(APP_ROOT, "app.db"));
  const dist = await realpath(resolve(APP_ROOT, "client", "dist"));
  const server = Bun.serve({
    port, hostname: "127.0.0.1", maxRequestBodySize: MAX_REQUEST,
    async fetch(req, server) {
      const expectedHost = `127.0.0.1:${server.port}`;
      if (req.headers.get("host") !== expectedHost) return new Response("Use the local Planner URL.", { status: 403 });
      const origin = req.headers.get("origin");
      if (origin && origin !== `http://${expectedHost}`) return new Response("Cross-origin requests are not accepted.", { status: 403 });
      const url = new URL(req.url);
      if (url.pathname === "/actions") {
        if (req.method !== "POST") return new Response("Use POST.", { status: 405, headers: { Allow: "POST" } });
        if (!req.headers.get("content-type")?.startsWith("application/json")) return new Response("Use JSON.", { status: 415 });
        if (Number(req.headers.get("content-length") ?? 0) > MAX_REQUEST) return new Response("Request too large.", { status: 413 });
        try {
          const bytes = await req.arrayBuffer();
          if (bytes.byteLength > MAX_REQUEST) return new Response("Request too large.", { status: 413 });
          const body: unknown = JSON.parse(new TextDecoder().decode(bytes));
          if (!body || typeof body !== "object" || Array.isArray(body) || !("action" in body) || typeof body.action !== "string") return Response.json({ error: "Choose a Planner action." }, { status: 400 });
          const data = await runtime.dispatch(body.action, "args" in body ? body.args : {});
          return Response.json({ data }, { headers: { "cache-control": "no-store" } });
        } catch (error) {
          const issues = error && typeof error === "object" && "issues" in error ? error.issues : null;
          return Response.json({ error: issues ? "Check the submitted fields and try again." : "Planner could not complete this request." }, { status: issues ? 400 : 500 });
        }
      }
      if (!["GET", "HEAD"].includes(req.method)) return new Response("Use GET.", { status: 405 });
      let pathname: string;
      try { pathname = decodeURIComponent(url.pathname); } catch { return new Response("Not found.", { status: 404 }); }
      if (pathname.includes("\0") || pathname.includes("\\")) return new Response("Not found.", { status: 404 });
      const candidate = resolve(dist, pathname === "/" ? "index.html" : `.${pathname}`);
      let path: string;
      try { path = await realpath(candidate); } catch { return new Response("Not found.", { status: 404 }); }
      if (!path.startsWith(dist + sep)) return new Response("Not found.", { status: 404 });
      const file = Bun.file(path);
      const contentType = ({ ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8", ".svg": "image/svg+xml", ".png": "image/png", ".ico": "image/x-icon", ".woff2": "font/woff2" } as Record<string, string>)[extname(path)] ?? "application/octet-stream";
      return new Response(req.method === "HEAD" ? null : file, { headers: { "content-type": contentType, "x-content-type-options": "nosniff", "cache-control": extname(path) === ".html" ? "no-store" : "public, max-age=3600" } });
    },
  });
  return { url: `http://127.0.0.1:${server.port}/`, stop: () => { server.stop(true); runtime.close(); } };
}
if (import.meta.main) {
  const app = await servePlanner();
  console.log(`Muse Planner is ready at ${app.url}`);
  process.on("SIGINT", () => { app.stop(); process.exit(0); });
  process.on("SIGTERM", () => { app.stop(); process.exit(0); });
}
