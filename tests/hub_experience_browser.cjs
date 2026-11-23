/* Focused Muse Hub browser regression. Node 22+, built-ins only; no downloads.
 * node tests/hub_experience_browser.cjs <repo-or-site-root> <chrome-executable> <new-output-dir> [--require-journeys]
 * Serves only the supplied static site on an owned 127.0.0.1 ephemeral port.
 * A fresh Chrome profile, exact child/process-group cleanup and bounded waits
 * keep this runner independent of existing browsers and provider accounts.
 */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const { spawn, execFile } = require('node:child_process');

const [rootArg, chromeArg, outArg, ...flags] = process.argv.slice(2);
assert(rootArg && chromeArg && outArg, 'Usage: <repo-or-site-root> <chrome-executable> <new-output-dir> [--require-journeys]');
assert(flags.every(flag => ['--require-journeys','--visual-inventory'].includes(flag)), 'Unknown argument');
assert(Number(process.versions.node.split('.')[0]) >= 22 && typeof WebSocket === 'function', 'Node 22+ with built-in WebSocket required');
const suppliedRoot = fs.realpathSync(rootArg);
const site = fs.existsSync(path.join(suppliedRoot, 'hub/site/index.html')) ? path.join(suppliedRoot, 'hub/site') : suppliedRoot;
const repo = path.basename(site) === 'site' && path.basename(path.dirname(site)) === 'hub' ? path.resolve(site, '../..') : suppliedRoot;
const chromePath = fs.realpathSync(chromeArg);
const out = path.resolve(outArg);
const contained = (parent, child) => child === parent || child.startsWith(parent + path.sep);
assert(!fs.existsSync(out), 'Output already exists; use a new directory and preserve prior evidence');
fs.mkdirSync(path.dirname(out), { recursive: true });
assert(!contained(repo, path.join(fs.realpathSync(path.dirname(out)), path.basename(out))), 'Evidence must be outside the product repository');
for (const name of ['index.html', 'public/index.html', 'public/app.js', 'public/catalog.json']) assert(fs.statSync(path.join(site, name)).isFile(), 'Missing site file: ' + name);
fs.mkdirSync(out);
const profile = path.join(out, 'owned-chrome-profile');
fs.mkdirSync(profile);
fs.copyFileSync(__filename, path.join(out, 'EXECUTED_HARNESS.cjs'));
const sha256 = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const catalog = JSON.parse(fs.readFileSync(path.join(site, 'public/catalog.json'), 'utf8'));
const routes = new Map(catalog.routes.map(route => [route.id, route]));
assert.deepEqual([...routes.keys()].sort(), ['cli', 'companion', 'desktop', 'doors', 'family', 'watch']);
const report = { schema: 'muse-hub/experience-browser/v1', started_at: new Date().toISOString(), site, chrome: chromePath, node: process.version, require_journeys: flags.includes('--require-journeys'), harness_sha256: sha256(fs.readFileSync(__filename)), source_files: {}, checks: [], screenshots: [], errors: [], blocked_external_requests: [], requests: [] };
for (const name of ['index.html', 'site.js', 'site.css', 'experience.css', 'downloads.html', 'downloads.js', 'downloads.json', 'roles.json', 'sitemap.xml', 'public/index.html', 'public/app.js', 'public/styles.css', 'public/catalog.json', 'planner-desktop.png', 'planner-mobile.png']) {
  const bytes = fs.readFileSync(path.join(site, name));
  report.source_files[name] = { bytes: bytes.length, sha256: sha256(bytes) };
}
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
const q = JSON.stringify;
let chrome, socket, server, base, sequence = 0, loaded = 0, width = 1440;
let catalogFault = null;
const pending = new Map();
let chromeLog = '';
const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml', '.png': 'image/png' };

function call(method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = ++sequence;
    const timer = setTimeout(() => { pending.delete(id); reject(Error('CDP timeout: ' + method)); }, 8000);
    pending.set(id, { resolve, reject, timer });
    try { socket.send(JSON.stringify({ id, method, params })); }
    catch (error) { clearTimeout(timer); pending.delete(id); reject(error); }
  });
}
async function evaluate(expression) {
  const result = await call('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
  if (result.exceptionDetails) throw Error('Browser evaluation: ' + JSON.stringify(result.exceptionDetails));
  return result.result?.value;
}
async function wait(expression, label = expression) {
  const until = Date.now() + 6000;
  while (Date.now() < until) { if (await evaluate(expression)) return; await pause(30); }
  throw Error('Browser state timeout: ' + label);
}
async function navigate(relative, enhanced = true) {
  const target = new URL(relative, base).href;
  assert(target.startsWith(base), 'Navigation must remain on the owned local site');
  const previous = loaded;
  const result = await call('Page.navigate', { url: target });
  assert(!result.errorText, result.errorText);
  const until = Date.now() + 8000;
  while (loaded === previous && Date.now() < until) await pause(30);
  assert(loaded > previous, 'Page load was not observed');
  await wait('document.readyState === "complete"');
  if (enhanced && new URL(target).pathname.includes('/public/')) await wait('document.body.classList.contains("directory-ready")');
  if (enhanced && new URL(target).pathname.endsWith('/downloads.html')) await wait('document.body.classList.contains("downloads-ready")');
}
async function click(selector) {
  const element = 'document.querySelector(' + q(selector) + ')';
  let box;
  for (let attempt = 0; attempt < 12; attempt++) {
    await evaluate(element + '.scrollIntoView({block:"center",inline:"center",behavior:"instant"})');
    await pause(45);
    box = await evaluate('(()=>{const e=' + element + ',r=e.getBoundingClientRect(),x=r.x+r.width/2,y=r.y+r.height/2,top=document.elementFromPoint(x,y);return {x,y,width:r.width,height:r.height,viewportWidth:innerWidth,viewportHeight:innerHeight,visible:!!e.getClientRects().length,hit:!!top && (top===e || e.contains(top)),obscurer:top?.outerHTML?.slice(0,160) || null};})()');
    assert(box.visible, 'Click target is hidden: ' + selector);
    if (box.hit) break;
  }
  assert(box.hit, 'Click target did not become pointer-reachable: '+selector+' '+JSON.stringify(box));
  for (const type of ['mousePressed', 'mouseReleased']) await call('Input.dispatchMouseEvent', { type, x: box.x, y: box.y, button: 'left', clickCount: 1 });
}
async function key(name, modifiers = 0) {
  const code = { Enter: 13, Escape: 27, Tab: 9, a: 65 }[name];
  for (const type of ['keyDown', 'keyUp']) await call('Input.dispatchKeyEvent', { type, key: name, code: name === 'a' ? 'KeyA' : name, windowsVirtualKeyCode: code, modifiers, ...(name === 'Enter' ? { text: '\r' } : {}) });
}
async function type(selector, text) {
  await click(selector); await key('a', 2); await call('Input.insertText', { text });
}
async function resize(nextWidth) {
  width = nextWidth;
  await call('Emulation.setDeviceMetricsOverride', { width, height: width >= 1000 ? 900 : 844, deviceScaleFactor: 1, mobile: false });
}
async function screenshot(name) {
  const result = await call('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  const bytes = Buffer.from(result.data, 'base64');
  fs.writeFileSync(path.join(out, name), bytes, { flag: 'wx' });
  report.screenshots.push({ name, bytes: bytes.length, sha256: sha256(bytes) });
}
async function state() {
  return evaluate('({ids:[...document.querySelectorAll("#results .resource-card")].map(e=>e.dataset.id),pressed:[...document.querySelectorAll("[data-route][aria-pressed=true]")].map(e=>e.dataset.route),chip:document.querySelector("#active-chip").textContent,chipHidden:document.querySelector("#active-chip").hidden,noticeHidden:document.querySelector("#route-notice").hidden,count:document.querySelector("#count").textContent,url:location.href,search:document.querySelector("#search").value,category:document.querySelector("#category").value})');
}
async function assertRoute(id, expectedItems = null) {
  const actual = await state();
  const route = routes.get(id);
  const expected = expectedItems || catalog.items.filter(item => !route || route.source_ids.includes(item.id));
  assert.deepEqual(actual.ids, expected.map(item => item.id), 'Visible resources must match the catalog route and local filters');
  assert.deepEqual(actual.pressed, id ? [id] : [], 'Selected route must match the URL');
  assert.equal(actual.chip, route?.title || '');
  assert.equal(actual.chipHidden, !route);
  assert.equal(actual.noticeHidden, !route);
  assert.equal(actual.count, `Showing ${expected.length} of ${catalog.count} sources`);
  return { route: id, ids: actual.ids, count: expected.length, url: actual.url };
}
async function check(name, run) {
  const row = { name };
  try { row.observed = await run(); row.status = 'PASS'; }
  catch (error) { row.status = 'FAIL'; row.error = error.stack || String(error); await screenshot('failure-' + report.checks.length + '.png').catch(() => {}); }
  report.checks.push(row);
  console.log(row.status + ' ' + name);
  if (row.error) console.error(row.error);
}
async function layout() {
  const result = await evaluate('({width:innerWidth,documentWidth:document.documentElement.scrollWidth,bodyWidth:document.body.scrollWidth,brokenAria:[...document.querySelectorAll("[aria-labelledby],[aria-describedby],[aria-controls]")].flatMap(e=>["aria-labelledby","aria-describedby","aria-controls"].flatMap(a=>(e.getAttribute(a)||"").split(/\\s+/).filter(Boolean).filter(id=>!document.getElementById(id)).map(id=>({element:e.id||e.tagName,attribute:a,id}))))})');
  assert(result.documentWidth <= result.width + 1 && result.bodyWidth <= result.width + 1, 'Horizontal overflow: ' + JSON.stringify(result));
  assert.deepEqual(result.brokenAria, []);
  return result;
}

async function start() {
  server = http.createServer((request, response) => {
    try {
      assert(request.method === 'GET' || request.method === 'HEAD');
      const pathname = decodeURIComponent(new URL(request.url, 'http://127.0.0.1').pathname);
      if (pathname === '/favicon.ico') { response.writeHead(204); response.end(); return; }
      let file = path.resolve(site, '.' + pathname);
      assert(contained(site, file));
      if (fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
      file = fs.realpathSync(file);
      assert(contained(site, file) && fs.statSync(file).isFile());
      let bytes = fs.readFileSync(file);
      if (pathname === '/downloads.json' && catalogFault) {
        if (catalogFault === 'unavailable') { response.writeHead(503); response.end('Temporarily unavailable'); return; }
        const changed = JSON.parse(bytes);
        changed.items[0].url = 'https://example.invalid/redirected.zip';
        bytes = Buffer.from(JSON.stringify(changed));
      }
      report.requests.push({ path: path.relative(site, file).replaceAll(path.sep, '/'), sha256: sha256(bytes) });
      response.writeHead(200, { 'Content-Type': MIME[path.extname(file)] || 'application/octet-stream', 'Content-Length': bytes.length, 'Cache-Control': 'no-store' });
      response.end(request.method === 'HEAD' ? undefined : bytes);
    } catch { response.writeHead(404); response.end('Not found'); }
  });
  await new Promise((resolve, reject) => { server.once('error', reject); server.listen(0, '127.0.0.1', resolve); });
  base = 'http://127.0.0.1:' + server.address().port + '/';
  report.base = base;
  const args = ['--headless=new', '--disable-gpu', '--remote-debugging-address=127.0.0.1', '--remote-debugging-port=0', '--user-data-dir=' + profile, '--no-first-run', '--no-default-browser-check', '--disable-background-networking', '--disable-component-update', '--disable-default-apps', '--disable-sync', '--metrics-recording-only', '--disable-features=MediaRouter', '--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE localhost, EXCLUDE 127.0.0.1'];
  if (process.platform === 'linux' && process.getuid?.() === 0) args.push('--no-sandbox');
  args.push('about:blank');
  chrome = spawn(chromePath, args, { stdio: ['ignore', 'pipe', 'pipe'], detached: process.platform !== 'win32' });
  chrome.on('error', error => { report.errors.push({ kind: 'chrome', message: error.message }); });
  for (const stream of [chrome.stdout, chrome.stderr]) stream.on('data', chunk => { chromeLog = (chromeLog + chunk).slice(-16000); });
  const activePort = path.join(profile, 'DevToolsActivePort');
  const until = Date.now() + 30000;
  let port;
  while (Date.now() < until && chrome.exitCode === null) {
    try {
      // Chrome can briefly lock this file on Windows or expose it mid-write.
      // A newline confirms the port field is complete before we trust it.
      const contents = fs.readFileSync(activePort, 'utf8');
      const candidate = contents.split(/\r?\n/)[0];
      if (contents.includes('\n') && /^\d+$/.test(candidate) && Number(candidate) > 0 && Number(candidate) <= 65535) { port = candidate; break; }
    } catch (error) {
      if (!['ENOENT', 'EBUSY', 'EACCES'].includes(error.code)) throw error;
    }
    await pause(50);
  }
  assert(port, 'Chrome did not expose a complete valid CDP port: ' + chromeLog);
  const endpoint = 'http://127.0.0.1:' + port;
  // A complete DevToolsActivePort file only proves the socket was announced,
  // not that a cold hosted-runner Chrome is already serving HTTP. Retry ONLY
  // this bounded startup handshake; never retry/ignore page or product failures.
  const discoveryUntil = Date.now() + 20000;
  let targets, lastDiscoveryError, discoveryAttempts = 0;
  while (Date.now() < discoveryUntil && chrome.exitCode === null) {
    discoveryAttempts++;
    try {
      const response = await fetch(endpoint + '/json/list', { signal: AbortSignal.timeout(2500) });
      assert(response.ok, 'DevTools HTTP ' + response.status);
      const candidate = await response.json();
      assert(Array.isArray(candidate), 'DevTools target list is not an array');
      targets = candidate;
      break;
    } catch (error) {
      lastDiscoveryError = String(error);
      if (Date.now() < discoveryUntil) await pause(150);
    }
  }
  assert(Array.isArray(targets),
    'CDP endpoint did not become ready after ' + discoveryAttempts +
    ' bounded attempts: ' + lastDiscoveryError + '; Chrome=' + chromeLog.slice(-1200));
  const target = targets.find(item => item.type === 'page' && item.url === 'about:blank');
  assert(target, 'Fresh profile has no blank page');
  socket = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => { const timer = setTimeout(() => reject(Error('CDP connection timeout')), 5000); socket.addEventListener('open', () => { clearTimeout(timer); resolve(); }, { once: true }); socket.addEventListener('error', error => { clearTimeout(timer); reject(error); }, { once: true }); });
  const isolationProbe = new URL('favicon.ico?isolation-probe', base);
  isolationProbe.hostname = 'localhost';
  let probeRequest, probeBlockReason;
  let probing = true;
  socket.addEventListener('message', event => {
    const message = JSON.parse(event.data);
    if (message.id) {
      const entry = pending.get(message.id);
      if (entry) { clearTimeout(entry.timer); pending.delete(message.id); message.error ? entry.reject(Error(JSON.stringify(message.error))) : entry.resolve(message.result); }
    } else if (message.method === 'Page.loadEventFired') loaded++;
    else if (message.method === 'Runtime.exceptionThrown') report.errors.push({ kind: 'page', details: message.params.exceptionDetails });
    else if (message.method === 'Runtime.consoleAPICalled' && message.params.type === 'error') report.errors.push({ kind: 'console', details: message.params.args });
    else if (message.method === 'Network.requestWillBeSent') {
      const { requestId, request } = message.params;
      if (probing && request.url === isolationProbe.href) probeRequest = requestId;
      else if (!request.url.startsWith(base)) report.blocked_external_requests.push(request.url);
    } else if (message.method === 'Network.loadingFailed' && message.params.requestId === probeRequest) {
      probeBlockReason = message.params.blockedReason;
    }
  });
  await call('Page.enable'); await call('Runtime.enable');
  // A headless window otherwise lacks OS focus even when its input is active.
  await call('Emulation.setFocusEmulationEnabled', { enabled: true });
  // Leave local requests in Chrome's network stack so a viewport change can
  // cancel an image without racing a CDP request interception.
  await call('Network.enable');
  await call('Network.setBlockedURLs', { urlPatterns: [
    { urlPattern: base + '*', block: false },
    { urlPattern: '*://*:*/*', block: true }
  ] });
  await evaluate('fetch(' + q(isolationProbe.href) + ').catch(() => {})');
  for (let attempt = 0; !probeBlockReason && attempt < 40; attempt++) await pause(25);
  assert.equal(probeBlockReason, 'inspector', 'Chrome must block requests to other origins');
  probing = false;
  report.network_isolation = { blocked_reason: probeBlockReason };
  await call('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
  await resize(1440);
}

async function runChecks() {
  const pageSize = 18;
  const downloads = JSON.parse(fs.readFileSync(path.join(site, 'downloads.json'), 'utf8'));
  await check('download inventory, specialist filters and shareable search', async () => {
    await navigate('downloads.html');
    const links = await evaluate('[...document.querySelectorAll(".download-card a[aria-label]")].map(a=>a.href)');
    assert.equal(links.length, Math.min(pageSize, downloads.items.length));
    assert.deepEqual(links, downloads.items.slice(0,pageSize).map(item => item.url));
    assert.equal(await evaluate('Number(document.querySelector("#download-results").dataset.catalogSize)'), downloads.items.length);
    const sample = downloads.items.slice(pageSize).findLast(row => row.kind === 'skill' && row.roles.includes('software-engineer'));
    assert(sample, 'Software engineering skill must be discoverable');
    await navigate('downloads.html?type=skill&role=software-engineer&q=' + encodeURIComponent(sample.id));
    const visible = await evaluate('[...document.querySelectorAll(".download-card:not([hidden])")].map(card=>({id:card.dataset.id,kind:card.dataset.kind,url:card.querySelector("a[aria-label]").href}))');
    assert(visible.some(item => item.id === sample.id && item.url === sample.url));
    assert(visible.every(item => downloads.items.find(row => row.id === item.id && row.kind === item.kind).roles.includes('software-engineer')));
    await type('#download-search', 'no-matching-download-39715');
    assert.equal(await evaluate('document.querySelector("#download-empty").hidden'), false);
    await click('#download-clear-empty');
    assert.equal(await evaluate('document.querySelectorAll(".download-card:not([hidden])").length'), Math.min(pageSize, downloads.items.length));
    assert.equal(new URL(await evaluate('location.href')).searchParams.has('role'), false);
    return {searchable_resources:downloads.items.length, rendered_cards:links.length, specialist_search:true, empty_state_reset:true};
  });
  await check('invalid download filters recover without reflected markup', async () => {
    for (const query of ['type=bad&role=bad', 'type=skill&type=workflow', 'role=%3Cimg%20src=x%3E', 'q='+'x'.repeat(3000)]) {
      await navigate('downloads.html?' + query);
      assert.equal(await evaluate('document.querySelectorAll(".download-card:not([hidden])").length'), Math.min(pageSize, downloads.items.length));
      assert.equal(await evaluate('document.querySelectorAll("#download-role img").length'), 0);
    }
    return {invalid_queries:4};
  });
  await check('download pagination has distinct results and shareable history', async () => {
    await navigate('downloads.html?type=skill');
    const visibleIds=() => evaluate('[...document.querySelectorAll(".download-card:not([hidden])")].map(card=>card.dataset.id)');
    const first=await visibleIds();
    assert.equal(first.length,pageSize);
    await click('#download-next');
    await wait('new URL(location.href).searchParams.get("page") === "2" && document.querySelector("#download-page-label").textContent.startsWith("Page 2")', 'second page URL and rendered state settled');
    const second=await visibleIds();
    assert.equal(second.length,pageSize);
    assert(second.every(id=>!first.includes(id)));
    assert.equal(new URL(await evaluate('location.href')).searchParams.get('page'),'2');
    await navigate(await evaluate('location.href'));
    assert.deepEqual(await visibleIds(),second);
    await click('#download-previous');
    await wait('new URL(location.href).searchParams.has("page") === false && document.querySelector("#download-previous").disabled', 'previous-page URL and controls settled');
    assert.deepEqual(await visibleIds(),first);
    await type('#download-search','no-matching-page-92574');
    assert.equal(await evaluate('document.querySelector("#download-pages").hidden'),true);
    await click('#download-clear-empty');
    assert.equal(await evaluate('document.querySelector("#download-previous").disabled'),true);
    await navigate('downloads.html?entry=skills#skills');
    assert.equal(await evaluate('document.querySelector("#download-kind").value'),'skill');
    const visibleSearch = () => evaluate('document.querySelector("#download-search").getBoundingClientRect().top < innerHeight && document.querySelector("#download-search").getBoundingClientRect().bottom > document.querySelector(".site-header").getBoundingClientRect().bottom');
    await wait('document.querySelector("#download-search").getBoundingClientRect().top < innerHeight', 'legacy Skills link keeps catalog controls in view');
    assert.equal(await visibleSearch(), true);
    await evaluate('(() => { const sort = document.querySelector("#download-sort"); sort.value="az"; sort.dispatchEvent(new Event("change")); })()');
    const alphabeticalStart = await visibleIds();
    await evaluate('(() => { const sort = document.querySelector("#download-sort"); sort.value="za"; sort.dispatchEvent(new Event("change")); })()');
    const descending = await visibleIds();
    assert(descending.every(id => !alphabeticalStart.includes(id)));
    assert.equal(new URL(await evaluate('location.href')).searchParams.get('sort'), 'za');
    const sortedUrl = await evaluate('location.href');
    await navigate('downloads.html');
    await navigate(sortedUrl);
    assert.deepEqual(await visibleIds(), descending);
    await click('#download-reset');
    const cleared = await evaluate('location.href');
    assert.equal(new URL(cleared).hash,'');
    await navigate(cleared);
    assert.equal(await evaluate('document.querySelector("#download-kind").value'),'all');
    return {page_size:pageSize, distinct_pages:true, shareable_page:true, filter_resets_page:true};
  });
  await check('unavailable or invalid catalog retains safe downloads and subject navigation', async () => {
    try {
      for (const fault of ['unavailable','redirected-entry']) {
        catalogFault = fault;
        await navigate('downloads.html',false);
        await wait('document.body.classList.contains("downloads-fallback")');
        assert.equal(await evaluate('document.querySelector("#download-results").hasAttribute("aria-busy")'),false);
        assert.equal(await evaluate('document.querySelector("#download-search").disabled'),true);
        assert.equal(await evaluate('document.querySelector(".catalog-subjects").open'),true);
        const links=await evaluate('[...document.querySelectorAll(".download-card a[aria-label]")].map(a=>a.href)');
        assert.deepEqual(links,downloads.items.slice(0,pageSize).map(row=>row.url));
        await layout();
      }
    } finally { catalogFault = null; }
    return {unavailable_fallback:true, redirected_entry_refused:true, initial_downloads_preserved:true};
  });
  await check('all resources without a route', async () => { await navigate('public/index.html'); return assertRoute(null); });
  for (const id of routes.keys()) await check('shareable route: ' + id, async () => {
    await navigate('public/index.html?route=' + id + '#browse-results');
    return assertRoute(id);
  });
  await check('invalid, duplicate, oversized and injected route values fall back safely', async () => {
    const queries = ['route=unknown', 'route=', 'route=CLI', 'route=cli&route=desktop', 'route=cli&route=cli', 'route=' + 'x'.repeat(3000), 'route=cli&extra=' + 'x'.repeat(3000), 'route=' + encodeURIComponent('<img data-route-injection src=x onerror="window.routeInjection=true">'), 'route=cli%26route%3Ddesktop', 'route%5B%5D=cli'];
    for (const query of queries) {
      await navigate('public/index.html?' + query);
      await assertRoute(null);
      assert.equal(await evaluate('Boolean(window.routeInjection || document.querySelector("[data-route-injection]"))'), false);
    }
    return { cases: queries.length, reflected_markup: false };
  });
  await check('route toggle, keyboard activation and reset update shareable URL', async () => {
    await navigate('public/index.html?from=home#browse-results');
    await click('[data-route="cli"]'); await assertRoute('cli');
    let url = new URL((await state()).url); assert.equal(url.searchParams.get('route'), 'cli'); assert.equal(url.searchParams.get('from'), 'home'); assert.equal(url.hash, '#browse-results');
    await key('Enter'); await assertRoute(null); assert.equal(new URL((await state()).url).searchParams.has('route'), false);
    await click('[data-route="watch"]'); await assertRoute('watch');
    await click('#reset'); await assertRoute(null); url = new URL((await state()).url); assert.equal(url.searchParams.has('route'), false); assert.equal(url.searchParams.get('from'), 'home');
    return { preserved_other_query_and_fragment: true, keyboard_toggle: true, reset: true };
  });
  await check('back and forward restore route controls and results', async () => {
    await navigate('public/index.html?route=cli');
    await click('[data-route="desktop"]'); await click('[data-route="watch"]');
    for (const [direction, id] of [['back', 'desktop'], ['back', 'cli'], ['forward', 'desktop']]) {
      await evaluate('history.' + direction + '()');
      await wait('new URL(location.href).searchParams.get("route") === ' + q(id));
      await assertRoute(id);
    }
    await click('#reset'); await assertRoute(null); await evaluate('history.back()');
    await wait('new URL(location.href).searchParams.get("route") === "desktop"');
    return assertRoute('desktop');
  });
  await check('invalid history clears stale route controls and a new selection reloads safely', async () => {
    const queries = ['route=unknown', 'route=cli&route=desktop', 'route=cli&extra=' + 'x'.repeat(3000)];
    for (const query of queries) {
      await navigate('public/index.html?' + query); await assertRoute(null);
      await click('[data-route="companion"]'); await assertRoute('companion');
      const selected = new URL((await state()).url);
      assert.deepEqual(selected.searchParams.getAll('route'), ['companion']);
      assert(selected.search.length <= 2048, 'New route link must recover from oversized query input');
      await evaluate('history.back()'); await wait('location.search === ' + q('?' + query)); await assertRoute(null);
      await evaluate('history.forward()'); await wait('location.search === ' + q(selected.search)); await assertRoute('companion');
      await navigate(selected.href); await assertRoute('companion');
    }
    return { histories: queries.length, stale_chip: false, new_links_reload: true };
  });
  await check('ordinary search and category stay local and combine with route', async () => {
    await navigate('public/index.html?route=cli');
    const item = catalog.items.find(item => routes.get('cli').source_ids.includes(item.id));
    const originalUrl = (await state()).url;
    await type('#search', item.id); await assertRoute('cli', [item]);
    const previous = loaded; await key('Enter'); assert.equal(loaded, previous);
    await evaluate('(()=>{const e=document.querySelector("#category");e.value=' + q(item.category) + ';e.dispatchEvent(new Event("change",{bubbles:true}));})()');
    await assertRoute('cli', [item]); assert.equal((await state()).url, originalUrl);
    await click('[data-route="desktop"]');
    const filtered = catalog.items.filter(candidate => candidate.id === item.id && candidate.category === item.category && routes.get('desktop').source_ids.includes(candidate.id));
    await assertRoute('desktop', filtered);
    await evaluate('history.back()'); await wait('new URL(location.href).searchParams.get("route") === "cli"'); await assertRoute('cli', [item]);
    assert.equal((await state()).search, item.id);
    await type('#search', 'nothing-matches-293751'); await assertRoute('cli', []);
    await click('#clear-empty'); await assertRoute(null); assert.equal((await state()).search, ''); assert.equal((await state()).category, '');
    return { local_filters_survive_route_history: true, enter_did_not_navigate: true, empty_state_reset: true };
  });
  await check('homepage task journeys reach real Spaces, downloads and all resource routes', async () => {
    await navigate('');
    const journeys = await evaluate('({paths:[...document.querySelectorAll(".premium-path-grid > a.premium-path-card")].map(a=>({href:a.getAttribute("href"),visible:!!a.getClientRects().length})),spaces:[...document.querySelectorAll(".premium-space-card a[href]")].map(a=>a.href),directory:[...document.querySelectorAll("a[href]")].some(a=>a.getAttribute("href")==="public/index.html")})');
    if (report.require_journeys) {
      assert.deepEqual(journeys.paths.map(link => link.href), ['?role=software-engineer#setup', '?role=research-evaluator#setup', '?role=product-interface-designer#setup', '?role=coordinator#setup']);
      assert(await evaluate('document.querySelector("#hero-heading")?.textContent?.replace(/\\s+/g," ").trim()==="Make Muse your own."'), 'R7 home heading must be present');
      assert(await evaluate('Boolean(document.querySelector(".r7-pyramid svg") && document.querySelector(".r7-metrics"))'), 'R7 must preserve pyramid artwork and resource inventory');
      const inventory = await evaluate('[...document.querySelectorAll(".r7-metrics dd")].map(x=>x.textContent.trim())');
      assert.deepEqual(inventory, ['5,200+', '375+', '15', '50+'], 'Resource counts must remain visible');
      assert(journeys.paths.every(link => link.visible), 'All four task paths must be visible');
      for (const role of ['software-engineer', 'research-evaluator', 'product-interface-designer', 'coordinator']) {
        await navigate('index.html?role=' + role + '#setup');
        const selection = await evaluate('({selected:document.getElementById("setup-role-select").value,expanded:document.querySelector(".setup-disclosure").open})');
        assert(selection.selected === role && selection.expanded, 'Task choice must open its named specialist: ' + role);
      }
      await navigate('index.html');
      for (const href of journeys.paths.map(link => link.href).filter(href => href.startsWith('#'))) {
        assert(await evaluate('Boolean(document.getElementById(' + q(href.slice(1)) + '))'), 'Task path anchor is missing: ' + href);
      }
      for (const guide of ['MUSE_PLANNER.md', 'TASK_BOARD.md', 'DAILY_DESK.md']) {
        assert(journeys.spaces.some(href => href.endsWith('/docs/spaces/' + guide)), 'Featured Space guide link missing: ' + guide);
        assert(fs.statSync(path.join(repo, 'docs/spaces', guide)).isFile(), 'Featured Space guide source missing: ' + guide);
      }
      assert(journeys.directory, 'Homepage must provide a direct link to the searchable resource directory');
    }
    await navigate('downloads.html');
    assert(await evaluate('Boolean(document.getElementById("download-search"))'), 'Downloads page must provide search');
    await navigate('public/index.html');
    await assertRoute(null);
    for (const id of routes.keys()) {
      await navigate('public/index.html?route=' + id + '#browse-results');
      await assertRoute(id);
    }
    return { paths: journeys.paths, featured_space_guides: journeys.spaces.length, directory_link: journeys.directory, resource_routes: [...routes.keys()] };
  });
  await check('authentic Planner capture and direct specialist search on mobile', async () => {
    await resize(375);
    await navigate('index.html#specialists');
    await evaluate('document.querySelector(".r7-app-preview").scrollIntoView({block:"start",behavior:"instant"})');
    await wait('(()=>{const img=document.querySelector(".premium-capture-picture img");return !!img&&img.complete&&img.naturalWidth>0&&!!img.currentSrc})()');
    const proof = await evaluate('(()=>{const img=document.querySelector(".premium-capture-picture img");const field=document.getElementById("role-search");return {loaded:!!img&&img.complete&&img.naturalWidth>0,mobile:!!img&&new URL(img.currentSrc).pathname.endsWith("/planner-mobile.png"),searchVisible:!!field&&!!field.getClientRects().length,searchOutside:!!field&&!field.closest("details"),directory:document.querySelector(".specialist-directory").open}})()');
    assert(proof.loaded && proof.mobile && proof.searchVisible && proof.searchOutside && proof.directory, JSON.stringify(proof));
    const ring = await evaluate('(()=>{const field=document.getElementById("role-search");field.focus();const css=getComputedStyle(field);return {focused:document.activeElement === field,color:css.borderTopColor,style:css.borderTopStyle,width:parseFloat(css.borderTopWidth)}})()');
    assert.equal(ring.color, 'rgb(244, 255, 82)', 'Search focus indicator must contrast against the dark panel');
    assert(ring.focused && ring.style === 'solid' && ring.width >= 2, JSON.stringify(ring));
    await type('#role-search', 'software engineer');
    const narrowed = await evaluate('document.querySelectorAll(".role-card:not([hidden])").length');
    assert(narrowed>=1 && narrowed<15,narrowed);
    await type('#role-search', 'no-such-specialist-123456');
    assert(await evaluate('!document.getElementById("role-empty").hidden && document.querySelectorAll(".role-card:not([hidden])").length===0'));
    await click('#role-empty-clear');
    assert(await evaluate('document.getElementById("role-search").value==="" && document.querySelectorAll(".role-card:not([hidden])").length===15'));
    await navigate('index.html?role=software-engineer#setup');
    assert(await evaluate('document.querySelector(".setup-disclosure").open && document.getElementById("setup-role-select").value==="software-engineer"'));
    return {real_capture:true,mobile_preview:true,search_direct:true,filters:true,clear_empty:true,deep_link:true};
  });
  await check('authentic Planner captures remain inspectable on phone and desktop', async () => {
    const observations = [];
    for (const viewport of [320, 360, 375, 390, 393, 768, 1024, 1440]) {
      // Set the size away from the showcase before a fresh load so resizing
      // the old page cannot cancel a pending responsive image request.
      await navigate('public/index.html');
      await resize(viewport); await navigate('index.html');
      // The authentic capture is intentionally lazy-loaded. Reveal it before checking load state.
      await evaluate('document.querySelector(".r7-app-preview").scrollIntoView({block:"start",behavior:"instant"})');
      await wait('(()=>{const i=document.querySelector(".premium-capture-picture img");return !!i&&i.complete&&i.naturalWidth>0&&!!i.currentSrc})()');
      const proof = await evaluate('(()=>{const img=document.querySelector(".premium-capture-picture img"),peek=document.querySelector(".premium-mobile-peek"),links=[...document.querySelectorAll(".premium-capture-inspect a")];return {loaded:img.complete&&img.naturalWidth>0,source:new URL(img.currentSrc).pathname,rect:{width:img.getBoundingClientRect().width,height:img.getBoundingClientRect().height,top:img.getBoundingClientRect().top},height:innerHeight,peekVisible:getComputedStyle(peek).display!=="none",links:links.map(a=>a.getAttribute("href")),scrollWidth:document.documentElement.scrollWidth}})()');
      assert(proof.loaded, 'Planner capture failed to load: ' + viewport);
      assert(proof.source.endsWith(viewport <= 690 ? '/planner-mobile.png' : '/planner-desktop.png'), JSON.stringify(proof));
      assert(proof.rect.width >= (viewport <= 690 ? viewport * .70 : Math.min(500,viewport * .50)) && proof.rect.height >= (viewport <= 690 ? 280 : 330), JSON.stringify(proof));
      assert(proof.rect.top >= 0, 'Planner demonstration should remain in page flow: ' + viewport);
      await evaluate('document.querySelector(".r7-app-preview").scrollIntoView({block:"start"})');
      const visible = await evaluate('(()=>{const r=document.querySelector(".premium-capture-picture img").getBoundingClientRect();return r.top<innerHeight && r.bottom>0})()');
      assert(visible, 'Planner capture must become visible when scrolled to: ' + viewport);
      assert(Math.abs(proof.rect.width / proof.rect.height - (viewport <= 690 ? 390 / 490 : 980 / 745)) < .015,
        'Planner capture must keep its original aspect ratio');
      assert.equal(proof.peekVisible, viewport > 690, 'Dual-device evidence mode differs from viewport');
      assert.deepEqual(proof.links, ['planner-desktop.png', 'planner-mobile.png']);
      for (const name of proof.links) assert(fs.statSync(path.join(site, name)).isFile(), name);
      assert(proof.scrollWidth <= viewport + 1, 'Showcase caused horizontal overflow');
      observations.push({viewport, ...proof});
    }
    return observations;
  });
  await check('outcome shortcuts expose real specialist cards with keyboard focus', async () => {
    await resize(390); await navigate('index.html');
    await call('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
    assert(await evaluate('getComputedStyle(document.querySelector(".role-quickpick-button")).transitionDuration === "0s"'));
    await evaluate('document.querySelector("[data-suggest-role=claims-adjudicator]").focus()');
    await key('Enter');
    const first = await evaluate('({open:document.querySelector(".specialist-directory").open,visible:[...document.querySelectorAll(".role-card:not([hidden])")].map(c=>c.dataset.role),search:document.getElementById("role-search").value,count:document.getElementById("role-count").textContent,pressed:document.querySelector("[data-suggest-role=claims-adjudicator]").getAttribute("aria-pressed"),label:document.getElementById("role-directory-label").textContent,focus:document.activeElement?.dataset?.role})');
    assert(first.open && first.search === 'Claims Adjudicator' && first.count === 'Showing 1 of 15 specialists' && first.label === 'View 1 matching specialist' && first.pressed === 'true',JSON.stringify(first));
    assert.deepEqual(first.visible,['claims-adjudicator']);
    assert.equal(first.focus,'claims-adjudicator');
    await screenshot('specialist-quickpick-390.png');
    await click('[data-suggest-role="product-interface-designer"]');
    const second = await evaluate('({visible:[...document.querySelectorAll(".role-card:not([hidden])")].map(c=>c.dataset.role),pressed:[...document.querySelectorAll("[data-suggest-role][aria-pressed=true]")].map(b=>b.dataset.suggestRole),focused:document.activeElement?.dataset?.role})');
    assert.deepEqual(second.visible,['product-interface-designer']);
    assert.deepEqual(second.pressed,['product-interface-designer']);
    assert.equal(second.focused,'product-interface-designer');
    await click('[data-suggest-role="product-interface-designer"]');
    assert(await evaluate('document.querySelectorAll(".role-card:not([hidden])").length === 15'));
    for (const id of ['software-engineer', 'coordinator']) {
      await click('[data-suggest-role="' + id + '"]');
      assert.deepEqual(await evaluate('[...document.querySelectorAll(".role-card:not([hidden])")].map(card => card.dataset.role)'), [id]);
    }
    await evaluate('document.getElementById("role-search").focus()');
    await key('Escape');
    assert(await evaluate('document.getElementById("role-search").value === "" && document.querySelectorAll(".role-card:not([hidden])").length === 15 && !document.querySelector("[data-suggest-role][aria-pressed=true]")'));
    await click('[data-suggest-role="coordinator"]');
    await click('#role-reset');
    await call('Emulation.setEmulatedMedia', { features: [] });
    assert(await evaluate('document.getElementById("role-search").value==="" && [...document.querySelectorAll(".role-card:not([hidden])")].length===15 && !document.querySelector("[data-suggest-role][aria-pressed=true]")'));
    return {first,second,reset:true};
  });
  for (const viewport of [320, 360, 375, 390, 393, 768, 1024, 1440]) await check('homepage and directory layout at ' + viewport, async () => {
    await resize(viewport); const rows = [];
    for (const [name, relative] of [['home', ''], ['resources', 'public/index.html?route=companion'], ['downloads','downloads.html']]) {
      await navigate(relative); rows.push({ page: name, ...await layout() });
      if (name === 'home') {
        const mark = await evaluate('(()=>{const i=document.querySelector(".r7-header img.brand-symbol");return {loaded:!!i&&i.complete&&i.naturalWidth>=64&&i.getAttribute("src")==="muse-mark.png",width:i?.getBoundingClientRect().width}})()');
        assert(mark.loaded && mark.width >= (viewport <= 850 ? 52 : 56), 'Brand mark must load at a legible size: ' + viewport);
        if (viewport <= 850) {
          const labels = await evaluate('(()=>[...document.querySelectorAll(".r7-metrics dt")].map(x=>{const t=x.getBoundingClientRect(),cell=x.parentElement.getBoundingClientRect();return {size:parseFloat(getComputedStyle(x).fontSize),left:t.left,right:t.right,valueRight:x.parentElement.querySelector("dd").getBoundingClientRect().right,cellLeft:cell.left,cellRight:cell.right,text:x.textContent.trim()}}))()');
          assert(labels.length === 4 && labels.every(x=>x.size>=13&&x.left>=x.cellLeft-1&&x.right<=x.cellRight+1&&x.valueRight<=x.cellRight+1), 'Resource labels must fit their own column without clipping: ' + viewport + ' ' + JSON.stringify(labels));
          const tasks = await evaluate('[...document.querySelectorAll(".r7-task-card")].map(x=>({width:x.getBoundingClientRect().width,height:x.getBoundingClientRect().height,title:parseFloat(getComputedStyle(x.querySelector("strong")).fontSize),body:parseFloat(getComputedStyle(x.querySelector("small")).fontSize)}))');
          assert(tasks.length === 4 && tasks.every(x=>x.width >= viewport*.80 && x.height>=85 && x.title>=17 && x.body>=14), 'Four readable touch targets required: ' + JSON.stringify(tasks));
        }
        const header = await evaluate('getComputedStyle(document.querySelector(".r7-header")).backgroundColor');
        assert.equal(header, 'rgb(21, 21, 21)', 'Sticky header must be fully opaque while scrolling');
      }
      if (name === 'resources') {
        const palette = await evaluate('({text:getComputedStyle(document.querySelector(".intro-description")).color,background:getComputedStyle(document.body).backgroundColor})');
        assert.deepEqual(palette, {text:'rgb(201, 203, 189)',background:'rgb(21, 21, 21)'});
      }
      await screenshot(name + '-' + viewport + '.png');
      if (name === 'home' && (viewport === 390 || viewport === 1440)) {
        await evaluate('document.querySelector("#roadmap").scrollIntoView({block:"start",behavior:"instant"})');
        await screenshot('home-tasks-' + viewport + '.png');
        await evaluate('document.querySelector("#specialists").scrollIntoView({block:"start",behavior:"instant"})');
        await screenshot('home-specialists-' + viewport + '.png');
      }
      if (name === 'downloads') {
        const controls = await evaluate('({top:document.querySelector("#download-search").getBoundingClientRect().top,height:innerHeight,background:getComputedStyle(document.body).backgroundColor})');
        assert(controls.top > 0 && controls.top < controls.height, JSON.stringify(controls));
        assert.equal(controls.background, 'rgb(21, 21, 21)');
        await evaluate('document.querySelector("#download-search").focus({preventScroll:true})');
        await wait('document.activeElement.id === "download-search"');
        rows.push({page:'download filters',...await layout()});
        await screenshot('download-filters-' + viewport + '.png');
      }
    }
    return rows;
  });
  await check('all generated subject pages share navigation, legibility and overflow safety', async () => {
    const names = fs.readdirSync(path.join(site, 'library')).filter(name=>name.endsWith('.html')).sort();
    assert(names.length >= 35, 'Full public subject catalogue must be present');
    const visited = [];
    for (const viewport of [320, 360, 375, 390, 393, 768, 1024, 1440]) {
      await resize(viewport);
      for (const name of names) {
        await navigate('library/' + name);
        const proof = await evaluate('(()=>{const header=document.querySelector(".r7-header"),main=document.querySelector(".subject-main"),footer=document.querySelector(".premium-footer"),cards=document.querySelectorAll(".subject-card"),h=document.querySelector(".subject-heading h1"),first=cards[0];return {header:!!header&&header.getBoundingClientRect().height>=70,footer:!!footer,main:!!main,cards:cards.length,heading:h?.textContent.trim(),crumb:document.querySelector(".subject-breadcrumb span:last-child")?.textContent.trim(),brand:document.querySelector(".r7-header img.brand-symbol")?.complete,font:parseFloat(getComputedStyle(first.querySelector("h2")).fontSize),overflow:document.documentElement.scrollWidth-innerWidth,styles:[...document.styleSheets].some(s=>s.href?.endsWith("/experience.css"))}})()');
        assert(proof.header && proof.footer && proof.main && proof.cards>0 && proof.cards<=200 && proof.heading && proof.heading===proof.crumb && proof.brand && proof.styles,
          'Missing shared subject experience '+name+' '+viewport+' '+JSON.stringify(proof));
        assert(proof.overflow<=1, 'Subject horizontal overflow: '+name+' '+viewport+' '+JSON.stringify(proof));
        assert(proof.font>=20, 'Subject card titles too small: '+name+' '+viewport+' '+proof.font);
        if (viewport<=690) {
          const pager=await evaluate('(()=>{const nav=document.querySelector(".subject-pagination");if(!nav)return null;const visible=[...nav.querySelectorAll("a")].filter(a=>a.getClientRects().length);return {count:visible.length,topRows:[...new Set(visible.map(a=>Math.round(a.getBoundingClientRect().top)))],types:visible.map(a=>a.getAttribute("rel")||a.getAttribute("aria-current")||"unexpected")}})()');
          assert(!pager || (pager.count<=3 && pager.topRows.length===1 && pager.types.every(t=>['prev','next','page'].includes(t))),
            'Mobile pagination must have one row with accessible Prev/current/Next: '+name+' '+viewport+' '+JSON.stringify(pager));
        }
        if ((name==='software-automation-001.html' && viewport===390) ||
            (name==='design-visualization-001.html' && viewport===1440))
          await screenshot('subject-' + viewport + '.png');
        if (flags.includes('--visual-inventory') && (viewport===390 || viewport===1440))
          await screenshot('visual-subject-'+name.replace('.html','')+'-'+viewport+'.png');
        visited.push(name+':'+viewport);
      }
    }
    return {subject_pages:names.length,verified_viewports:[320,360,375,390,393,768,1024,1440],checked:visited.length};
  });
  await check('library advanced filters disclose without losing search and reset', async () => {
    for (const viewport of [390,1440]) {
      await resize(viewport);
      await navigate('downloads.html');
      assert.equal(await evaluate('document.querySelector(".download-advanced").open'),false);
      await click('.download-advanced summary');
      assert.equal(await evaluate('document.querySelector(".download-advanced").open'),true);
      const proof = await evaluate('(()=>({controls:["download-kind","download-role","download-category","download-sort"].every(id=>{const e=document.getElementById(id);return !!e.getClientRects().length}),overflow:document.documentElement.scrollWidth-innerWidth}))()');
      assert(proof.controls && proof.overflow<=1,'Expanded filters must be fully accessible: '+JSON.stringify(proof));
      await click('.download-advanced summary');
      assert.equal(await evaluate('document.querySelector(".download-advanced").open'),false);
      const search = await evaluate('document.querySelector("#download-search").getBoundingClientRect().height');
      assert(search>=50,'Search remains primary on '+viewport);
    }
    return {viewport:[390,1440],disclosure:true,search_first:true};
  });
  await check('shared R10 header, typography and card tokens across all page families', async () => {
    const screens = [];
    const families = [
      ['index.html','.r7-task-card'],
      ['downloads.html','.download-card'],
      ['library/design-visualization-001.html','.subject-card'],
      ['public/index.html','.route-card']
    ];
    for (const viewport of [390, 1440]) {
      await resize(viewport);
      const measurements = [];
      for (const [page,card] of families) {
        await navigate(page);
        const state = await evaluate('(()=>{const h=document.querySelector(".muse-header"),logo=h.querySelector(".brand-symbol"),title=document.querySelector("h1"),card=document.querySelector(' + q(card) + '),shell=document.querySelector("main .shell")||document.querySelector("main.shell")||document.querySelector("main .directory-section");const cs=getComputedStyle(card),hs=getComputedStyle(h),ts=getComputedStyle(title),s= shell?.getBoundingClientRect();return {headerHeight:Math.round(h.getBoundingClientRect().height),logoSize:Math.round(logo.getBoundingClientRect().width),headerBackground:hs.backgroundColor,titleFamily:ts.fontFamily,cardBackground:cs.backgroundColor,cardBorder:cs.borderTopColor,cardRadius:cs.borderTopLeftRadius,gutter:s?Math.round(s.left+(parseFloat(getComputedStyle(shell).paddingLeft)||0)):null,overflow:document.documentElement.scrollWidth-innerWidth}})()');
        assert(state.overflow<=1,'Unexpected horizontal overflow '+page+' '+viewport);
        assert(state.headerHeight>=68&&state.headerHeight<=85,'Inconsistent header height '+page+' '+viewport+' '+JSON.stringify(state));
        assert(state.logoSize>=(viewport<=370?54:56)&&state.logoSize<=60,'Inconsistent logo size '+page+' '+viewport);
        assert.equal(state.cardRadius,'5px','Cards must share visible corners: '+page);
        measurements.push({page,...state});
      }
      const a=measurements[0];
      for(const m of measurements.slice(1)){
        assert.equal(m.headerHeight,a.headerHeight,'Header height differs from Home: '+m.page);
        assert.equal(m.logoSize,a.logoSize,'Logo size differs from Home: '+m.page);
        assert.equal(m.headerBackground,a.headerBackground,'Header surface differs: '+m.page);
        assert.equal(m.titleFamily,a.titleFamily,'Primary heading font family differs: '+m.page);
        assert.equal(m.cardBackground,a.cardBackground,'Primary card surfaces differ: '+m.page);
        assert.equal(m.cardBorder,a.cardBorder,'Primary card borders differ: '+m.page);
        assert(Math.abs(m.gutter-a.gutter)<=2,'Content gutters drift across families: '+m.page+' '+JSON.stringify(measurements));
      }
      screens.push({viewport,measurements});
    }
    return {screens};
  });
  await check('reference phone hierarchy and complete laptop hero', async () => {
    const proofs=[];
    for (const viewport of [320,390,1440]) {
      await resize(viewport);
      await navigate('index.html');
      const state=await evaluate('(()=>{const a=[...document.querySelectorAll(".r7-actions .r7-button")].map(x=>x.getBoundingClientRect()),m=[...document.querySelectorAll(".r7-metrics>div")].map(x=>x.getBoundingClientRect()),art=document.querySelector(".r7-pyramid"),featured=document.querySelector(".r7-feature-card").getBoundingClientRect();return {actions:a.map(x=>({left:x.left,right:x.right,top:x.top,bottom:x.bottom})),metrics:m.map(x=>({left:x.left,top:x.top})),art:getComputedStyle(art).display,featuredBottom:featured.bottom,viewportHeight:innerHeight}})()');
      if(viewport<=390){
        assert(state.art==='none','Phone reference must not insert decorative artwork between tasks and controls: '+viewport);
        assert(state.actions[1].top>=state.actions[0].bottom+6,'Phone CTAs must be stacked with consistent spacing: '+JSON.stringify(state));
        assert(state.actions.every(x=>x.right-x.left>=viewport*.75),'Phone CTAs must span the content rail: '+JSON.stringify(state));
        assert(state.metrics.every(x=>Math.abs(x.top-state.metrics[0].top)<=1),'Four phone resource totals must share one baseline: '+JSON.stringify(state));
      }else{
        assert(state.art!=='none' && state.actions[1].left>state.actions[0].left,'Desktop must retain pyramid art and inline actions');
        assert(state.featuredBottom<state.viewportHeight-20,'Featured specialist should remain in the initial desktop screen: '+JSON.stringify(state));
      }
      proofs.push({viewport,...state});
    }
    return proofs;
  });
  await check('all mobile Spaces and all five library types stay fully visible without sideways scrolling', async () => {
    const observations=[];
    for (const viewport of [320,360,375,390,393]) {
      await resize(viewport);
      await navigate('index.html');
      const spaces=await evaluate('(()=>{const grid=document.querySelector(".premium-space-grid"),cards=[...grid.querySelectorAll(".premium-space-card")],rects=cards.map(c=>c.getBoundingClientRect()),r=grid.getBoundingClientRect();return {display:getComputedStyle(grid).display,count:cards.length,gridWidth:r.width,overflow:grid.scrollWidth-grid.clientWidth,cardWidth:Math.max(...rects.map(a=>a.width)),rows:[...new Set(rects.map(a=>Math.round(a.top)))]}})()');
      assert(spaces.display==='grid' && spaces.count>=3 && spaces.overflow<=1 && spaces.cardWidth<=spaces.gridWidth+1 && spaces.rows.length===spaces.count,
        'All phone Spaces must appear as full-width readable vertical cards: '+viewport+' '+JSON.stringify(spaces));
      await navigate('downloads.html');
      const filters=await evaluate('(()=>{const nav=document.querySelector(".downloads-catalog .download-jumps"),links=[...nav.querySelectorAll("a[data-download-type]")],r=nav.getBoundingClientRect(),bounds=links.map(a=>a.getBoundingClientRect());return {count:links.length,overflow:nav.scrollWidth-nav.clientWidth,rows:[...new Set(bounds.map(a=>Math.round(a.top)))],links:links.map((a,i)=>({type:a.dataset.downloadType,visible:!!a.getClientRects().length,left:bounds[i].left,right:bounds[i].right,height:bounds[i].height})),left:r.left,right:r.right}})()');
      assert(filters.count===5 && filters.overflow<=1 && filters.rows.length===2 && filters.links.every(x=>x.visible&&x.height>=44&&x.left>=filters.left-1&&x.right<=filters.right+1),
        'All five phone library filters must be visible within the container on two orderly rows: '+viewport+' '+JSON.stringify(filters));
      observations.push({viewport,spaces,filters});
    }
    return observations;
  });
  await check('subject pack paths are accessible disclosures with working method links', async () => {
    await resize(390);
    await navigate('library/design-visualization-001.html');
    const details = await evaluate('document.querySelectorAll(".subject-source").length');
    assert(details>1,'Expected multiple skill-pack disclosures');
    const first = await evaluate('(()=>{const e=document.querySelector(".subject-source");return {closed:!e.open,link:!!e.closest(".subject-card").querySelector(".subject-guide-link"),path:e.querySelector("code")?.textContent}})()');
    assert(first.closed&&first.link&&first.path.includes('/SKILL.md'),'Pack path and read guide must be preserved');
    await click('.subject-source summary');
    assert(await evaluate('document.querySelector(".subject-source").open'),'Pack path must disclose on click');
    return {details,first};
  });
  await check('mobile-first page rhythm and guide navigation are measurable', async () => {
    const observations = [];
    for (const viewport of [320, 360, 375, 390, 393]) {
      await resize(viewport);
      await navigate('index.html');
      const home = await evaluate('(()=>{const h=document.querySelector(".r7-header").getBoundingClientRect(),hero=document.querySelector(".r7-hero").getBoundingClientRect(),task=document.querySelector(".r7-task-card").getBoundingClientRect(),label=document.querySelector(".r7-task-paths h2").getBoundingClientRect();return {header:h.height,heroBottom:hero.bottom,taskTop:task.top,taskHeight:task.height,labelTop:label.top,viewport:innerHeight,overflow:document.documentElement.scrollWidth-innerWidth}})()');
      assert(home.header<=79 && home.heroBottom < home.viewport-85,
        'Mobile hero pushes tasks out of reach: '+viewport+' '+JSON.stringify(home));
      assert(home.taskTop < home.viewport-40 && home.taskHeight>=85 && home.overflow<=1,
        'First task must be visible without a scroll: '+viewport+' '+JSON.stringify(home));
      await navigate('downloads.html');
      const library = await evaluate('(()=>{const heading=document.querySelector(".download-section h2").getBoundingClientRect(),card=document.querySelector(".download-card").getBoundingClientRect(),search=document.getElementById("download-search").getBoundingClientRect();return {searchTop:search.top,headingTop:heading.top,firstCardTop:card.top,viewport:innerHeight,overflow:document.documentElement.scrollWidth-innerWidth}})()');
      assert(library.searchTop < 360 && library.firstCardTop < library.viewport-80 && library.overflow<=1,
        'Library must reach first result within initial phone view: '+viewport+' '+JSON.stringify(library));
      await navigate('public/index.html');
      const guide = await evaluate('(()=>{const h=document.querySelector(".site-header").getBoundingClientRect(),nav=document.querySelector(".header-nav"),menu=document.querySelector(".mobile-navigation"),title=document.querySelector("h1").getBoundingClientRect();return {header:h.height,menu:!!menu&&!!menu.getClientRects().length,oldNav:!!nav.getClientRects().length,titleTop:title.top,overflow:document.documentElement.scrollWidth-innerWidth}})()');
      assert(guide.header<=80 && guide.menu && !guide.oldNav && guide.titleTop>=guide.header && guide.overflow<=1,
        'Guide directory needs one-row mobile header: '+viewport+' '+JSON.stringify(guide));
      await click('.mobile-navigation summary');
      assert(await evaluate('document.querySelector(".mobile-navigation").open'), 'Menu must actually open on mobile');
      const links = await evaluate('[...document.querySelectorAll(".mobile-navigation nav a")].map(a=>({href:a.getAttribute("href"),height:a.getBoundingClientRect().height,visible:!!a.getClientRects().length}))');
      assert(links.length===6 && links.every(a=>a.visible&&a.height>=44),
        'Menu links must have accessible touch targets: '+JSON.stringify(links));
      if(viewport===390) await screenshot('resources-mobile-menu-390.png');
      await click('.mobile-navigation summary');
      assert.equal(await evaluate('document.querySelector(".mobile-navigation").open'),false);
      observations.push({viewport,home,library,guide});
    }
    await resize(1440); await navigate('public/index.html');
    const desktop = await evaluate('({nav:!!document.querySelector(".header-nav").getClientRects().length,mobile:!!document.querySelector(".mobile-navigation").getClientRects().length})');
    assert(desktop.nav&&!desktop.mobile, 'Desktop must preserve full guide navigation');
    return {phones:observations,desktop};
  });
  await check('mobile detail dialog keeps and restores keyboard focus', async () => {
    await resize(375); await navigate('public/index.html?route=cli'); await click('.details-button');
    await wait('document.querySelector("#detail-panel").contains(document.activeElement)');
    assert(await evaluate('Boolean(document.querySelector("#search").closest("[inert]"))'));
    for (let index = 0; index < 5; index++) { await key('Tab', index > 2 ? 8 : 0); assert(await evaluate('document.querySelector("#detail-panel").contains(document.activeElement)')); }
    await key('Escape'); assert.equal(await evaluate('document.querySelectorAll("[inert]").length'), 0);
    assert.equal(await evaluate('document.activeElement.className'), 'details-button');
    return { tab_contained: true, escape_restored: true };
  });
  await check('no JavaScript keeps all selected guide links usable', async () => {
    await call('Emulation.setScriptExecutionDisabled', { value: true });
    try {
      await navigate('public/index.html?route=cli', false);
      const links = await evaluate('[...document.querySelectorAll("#results .record-link")].map(a=>({href:a.href,visible:!!a.getClientRects().length}))');
      assert.equal(links.length, catalog.items.length); assert(links.every(link => link.visible));
      assert.deepEqual(new Set(links.map(link => link.href)), new Set(catalog.items.map(item => item.url)));
      assert.equal(await evaluate('getComputedStyle(document.querySelector("#filters")).display'), 'none');
      await layout(); await screenshot('resources-no-javascript-375.png');
      return { visible_guide_links: links.length };
    } finally { await call('Emulation.setScriptExecutionDisabled', { value: false }); }
  });
  await check('specialist kits remain reachable without JavaScript', async () => {
    await resize(390);
    await call('Emulation.setScriptExecutionDisabled', { value: true });
    try {
      await navigate('index.html#specialists', false);
      assert(await evaluate('document.querySelector(".specialist-search-panel").hidden'));
      await click('.specialist-directory summary');
      const kits = await evaluate('[...document.querySelectorAll(".role-card-download")].filter(a => a.getClientRects().length).length');
      assert.equal(kits, 15);
      return { accessible_downloads: kits };
    } finally { await call('Emulation.setScriptExecutionDisabled', { value: false }); }
  });
  await check('downloads remain usable without JavaScript', async () => {
    await call('Emulation.setScriptExecutionDisabled', { value: true });
    try {
      await navigate('downloads.html?role=software-engineer', false);
      const initial=await evaluate('document.querySelectorAll(".download-card:not([hidden]) a[aria-label]").length');
      assert.equal(initial,Math.min(pageSize,downloads.items.length));
      await click('.catalog-subjects summary');
      const subjects=await evaluate('[...document.querySelectorAll("nav[aria-label=\\"Subject library\\"] a")].map(a=>({href:a.href,visible:!!a.getClientRects().length}))');
      const expectedSubjects=fs.readdirSync(path.join(site,'library')).filter(name=>name.endsWith('-001.html')).map(name=>new URL('library/'+name,base).href);
      assert.deepEqual(new Set(subjects.map(row=>row.href)),new Set(expectedSubjects));
      assert(subjects.every(row=>row.visible));
      await layout();
      await navigate(subjects[0].href,false);
      const subjectDownloads=await evaluate('[...document.querySelectorAll(".download-card a")].map(a=>a.href).filter(href=>href.includes("/releases/download/"))');
      assert(subjectDownloads.length>0 && subjectDownloads.length<=200);
      assert(subjectDownloads.every(href=>downloads.items.some(row=>row.url===href)));
      await layout();
      return {initial_downloads:initial, linked_subject_pages:subjects.length, subject_downloads:subjectDownloads.length};
    } finally { await call('Emulation.setScriptExecutionDisabled', { value:false }); }
  });
}

async function cleanup() {
  if (socket?.readyState === WebSocket.OPEN) { await call('Browser.close').catch(() => {}); socket.close(); }
  if (chrome?.pid) {
    const until = Date.now() + 3000;
    while (chrome.exitCode === null && chrome.signalCode === null && Date.now() < until) await pause(50);
    if (process.platform !== 'win32') {
      for (const signal of ['SIGTERM', 'SIGKILL']) {
        try { process.kill(-chrome.pid, 0); process.kill(-chrome.pid, signal); } catch (error) { if (error.code !== 'ESRCH') report.errors.push({ kind: 'cleanup', message: error.message }); }
        await pause(100);
      }
    } else if (chrome.exitCode === null && chrome.signalCode === null) {
      await new Promise(resolve => execFile('taskkill.exe', ['/PID', String(chrome.pid), '/T', '/F'], { timeout: 5000 }, error => { if (error) report.errors.push({ kind: 'cleanup', message: error.message }); resolve(); }));
    }
  }
  for (const entry of pending.values()) { clearTimeout(entry.timer); entry.reject(Error('Runner closed')); }
  pending.clear();
  if (server) { server.closeAllConnections(); await new Promise(resolve => server.close(resolve)); }
  report.cleanup = { server_closed: !server?.listening, chrome_pid: chrome?.pid, chrome_exit: chrome?.exitCode, chrome_signal: chrome?.signalCode, profile_removed: false };
  if (chrome?.pid && chrome.exitCode === null && chrome.signalCode === null) report.errors.push({ kind: 'cleanup', message: 'Owned Chrome has not exited' });
  else { fs.rmSync(profile, { recursive: true, force: true, maxRetries: 4, retryDelay: 100 }); report.cleanup.profile_removed = !fs.existsSync(profile); }
}

let finalization;
const finish = () => finalization ||= (async () => {
    clearTimeout(watchdog);
    await cleanup().catch(error => report.errors.push({ kind: 'cleanup', message: error.message })); clearTimeout(watchdog);
    report.changed_source_files = Object.entries(report.source_files).filter(([name, before]) => {
      try { return sha256(fs.readFileSync(path.join(site, name))) !== before.sha256; } catch { return true; }
    }).map(([name]) => name);
    report.finished_at = new Date().toISOString(); report.passed = report.checks.filter(row => row.status === 'PASS').length; report.failed = report.checks.filter(row => row.status === 'FAIL').length;
    report.status = report.failed || report.errors.length || report.blocked_external_requests.length || report.changed_source_files.length ? 'FAIL' : 'PASS';
    fs.writeFileSync(path.join(out, 'CHROME.log'), chromeLog);
    fs.writeFileSync(path.join(out, 'BROWSER_REPORT.json'), JSON.stringify(report, null, 2) + '\n');
    for (const error of report.errors) console.error(JSON.stringify(error));
    console.log(JSON.stringify({ status: report.status, passed: report.passed, failed: report.failed, errors: report.errors.length, blocked_external: report.blocked_external_requests.length, evidence: out }));
    if (report.status !== 'PASS') process.exitCode = 1;
  })();
const watchdog = setTimeout(() => { report.errors.push({ kind: 'timeout', message: 'Overall 120 second budget exceeded' }); finish().finally(() => process.exit(1)); }, 120000);
(async () => { await start(); await runChecks(); })()
  .catch(error => { report.errors.push({ kind: 'harness', message: error.stack || String(error) }); console.error(error.stack || error); })
  .finally(finish);
