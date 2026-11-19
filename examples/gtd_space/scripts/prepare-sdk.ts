import { copyFile, mkdir, realpath } from "node:fs/promises";
import { resolve } from "node:path";
import { createHash } from "node:crypto";
import { APP_ROOT } from "./migrate";

const source = await realpath(process.argv[2] ?? process.env.MUSE_SPACE_SDK_PATH ?? "/opt/hatch/skills/spaces/ts-runtime/dist/space-sdk.tgz");
const destination = resolve(APP_ROOT, ".sdk", "space-sdk.tgz");
const file = Bun.file(source);
if (file.size < 1000 || file.size > 32 * 1024 * 1024) throw new Error("Choose the Muse host's space-sdk.tgz package.");
const bytes = new Uint8Array(await file.arrayBuffer());
await mkdir(resolve(APP_ROOT, ".sdk"), { recursive: true });
if (source !== destination) await copyFile(source, destination);
console.log(JSON.stringify({ sdk: destination, bytes: bytes.byteLength, sha256: createHash("sha256").update(bytes).digest("hex") }));
