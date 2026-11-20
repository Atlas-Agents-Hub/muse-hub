import { Database } from "bun:sqlite";
import { readdirSync, readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

export const APP_ROOT = fileURLToPath(new URL("..", import.meta.url));
export function migrateDatabase(path: string) {
  const db = new Database(path);
  try {
    db.exec("PRAGMA foreign_keys = ON; PRAGMA busy_timeout = 5000; PRAGMA journal_mode = WAL;");
    db.exec("CREATE TABLE IF NOT EXISTS _standalone_migrations (name TEXT PRIMARY KEY, checksum TEXT NOT NULL, applied_at TEXT NOT NULL)");
    const applied = new Map((db.query("SELECT name, checksum FROM _standalone_migrations").all() as { name: string; checksum: string }[]).map(row => [row.name, row.checksum]));
    let ran = 0;
    for (const file of readdirSync(join(APP_ROOT, "drizzle")).filter(file => /^\d{4}_.+\.sql$/.test(file)).sort()) {
      const source = readFileSync(join(APP_ROOT, "drizzle", file), "utf8");
      const checksum = createHash("sha256").update(source).digest("hex");
      if (applied.has(file)) {
        if (applied.get(file) !== checksum) throw new Error(`Migration ${file} differs from the applied file.`);
        continue;
      }
      db.transaction(() => {
        db.exec(source);
        db.query("INSERT INTO _standalone_migrations (name, checksum, applied_at) VALUES (?, ?, ?)").run(file, checksum, new Date().toISOString());
      })();
      ran += 1;
    }
    return { applied: ran, path };
  } finally { db.close(); }
}
if (import.meta.main) console.log(JSON.stringify(migrateDatabase(process.env.GTD_DB ?? join(APP_ROOT, "app.db"))));
