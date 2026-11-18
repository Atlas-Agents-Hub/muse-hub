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
assert(flags.every(flag => flag === '--require-journeys'), 'Unknown argument');
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
for (const name of ['index.html', 'site.js', 'site.css', 'downloads.html', 'downloads.js', 'downloads.json', 'roles.json', 'sitemap.xml', 'public/index.html', 'public/app.js', 'public/styles.css', 'public/catalog.json']) {
  const bytes = fs.readFileSync(path.join(site, name));
  report.source_files[name] = { bytes: bytes.length, sha256: sha256(bytes) };
}
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
const q = JSON.stringify;
let chrome, socket, server, base, sequence = 0, loaded = 0, width = 1440;
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
}
async function click(selector) {
  const element = 'document.querySelector(' + q(selector) + ')';
  await evaluate(element + '.scrollIntoView({block:"center",inline:"center",behavior:"instant"})');
  const box = await evaluate('(()=>{const e=' + element + ',r=e.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2,visible:!!e.getClientRects().length};})()');
  assert(box.visible, 'Click target is hidden: ' + selector);
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
      const bytes = fs.readFileSync(file);
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
  const targets = await fetch(endpoint + '/json/list', { signal: AbortSignal.timeout(5000) }).then(response => response.json());
  const target = targets.find(item => item.type === 'page' && item.url === 'about:blank');
  assert(target, 'Fresh profile has no blank page');
  socket = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => { const timer = setTimeout(() => reject(Error('CDP connection timeout')), 5000); socket.addEventListener('open', () => { clearTimeout(timer); resolve(); }, { once: true }); socket.addEventListener('error', error => { clearTimeout(timer); reject(error); }, { once: true }); });
  socket.addEventListener('message', event => {
    const message = JSON.parse(event.data);
    if (message.id) {
      const entry = pending.get(message.id);
      if (entry) { clearTimeout(entry.timer); pending.delete(message.id); message.error ? entry.reject(Error(JSON.stringify(message.error))) : entry.resolve(message.result); }
    } else if (message.method === 'Page.loadEventFired') loaded++;
    else if (message.method === 'Runtime.exceptionThrown') report.errors.push({ kind: 'page', details: message.params.exceptionDetails });
    else if (message.method === 'Runtime.consoleAPICalled' && message.params.type === 'error') report.errors.push({ kind: 'console', details: message.params.args });
    else if (message.method === 'Fetch.requestPaused') {
      const { requestId, request } = message.params;
      const allowed = request.url.startsWith(base);
      if (!allowed) report.blocked_external_requests.push(request.url);
      call(allowed ? 'Fetch.continueRequest' : 'Fetch.failRequest', allowed ? { requestId } : { requestId, errorReason: 'BlockedByClient' }).catch(error => report.errors.push({ kind: 'request', message: error.message }));
    }
  });
  await call('Page.enable'); await call('Runtime.enable');
  await call('Fetch.enable', { patterns: [{ urlPattern: '*' }] });
  await call('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
  await resize(1440);
}

async function runChecks() {
  const downloads = JSON.parse(fs.readFileSync(path.join(site, 'downloads.json'), 'utf8'));
  await check('download inventory, specialist filters and shareable search', async () => {
    await navigate('downloads.html');
    const links = await evaluate('[...document.querySelectorAll(".download-card a[aria-label]")].map(a=>a.href)');
    assert.equal(links.length, downloads.items.length);
    assert.deepEqual(new Set(links), new Set(downloads.items.map(item => item.url)));
    const sample = downloads.items.find(row => row.kind === 'skill' && row.roles.includes('software-engineer'));
    assert(sample, 'Software engineering skill must be discoverable');
    await navigate('downloads.html?type=skill&role=software-engineer&q=' + encodeURIComponent(sample.id));
    const visible = await evaluate('[...document.querySelectorAll(".download-card:not([hidden]) a[aria-label]")].map(a=>a.href)');
    assert(visible.includes(sample.url));
    assert(visible.every(url => downloads.items.find(row => row.url === url).roles.includes('software-engineer')));
    await type('#download-search', 'no-matching-download-39715');
    assert.equal(await evaluate('document.querySelector("#download-empty").hidden'), false);
    await click('#download-clear-empty');
    assert.equal(await evaluate('document.querySelectorAll(".download-card:not([hidden])").length'), downloads.items.length);
    assert.equal(new URL(await evaluate('location.href')).searchParams.has('role'), false);
    return {individual_downloads:links.length, specialist_search:true, empty_state_reset:true};
  });
  await check('invalid download filters recover without reflected markup', async () => {
    for (const query of ['type=bad&role=bad', 'type=skill&type=workflow', 'role=%3Cimg%20src=x%3E', 'q='+'x'.repeat(3000)]) {
      await navigate('downloads.html?' + query);
      assert.equal(await evaluate('document.querySelectorAll(".download-card:not([hidden])").length'), downloads.items.length);
      assert.equal(await evaluate('document.querySelectorAll("#download-role img").length'), 0);
    }
    return {invalid_queries:4};
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
  await check('homepage journey links resolve to real routes', async () => {
    await navigate('');
    let journeys = null;
    if (report.require_journeys) {
      journeys = await evaluate('({paths:[...document.querySelectorAll("nav[aria-label=\\"Explore Muse Hub\\"] a[href]")].map(a=>({hash:new URL(a.href).hash,exists:!!document.getElementById(new URL(a.href).hash.slice(1)),visible:!!a.getClientRects().length})),guides:[...document.querySelectorAll("#roadmap a[href]")].map(a=>new URL(a.href).pathname.split("/").pop())})');
      assert.deepEqual(journeys.paths.map(item => item.hash), ['#explore-muse', '#specialists', '#connect-automate', '#companion-spaces', '#computer-devices', '#explore']);
      assert(journeys.paths.every(item => item.exists && item.visible), 'All six discovery paths must have visible links and real sections');
      for (const guide of ['ORGANIZE_YOUR_DAY.md', 'BUILD_AND_AUTOMATE.md', 'CREATE_SOMETHING.md']) assert(journeys.guides.includes(guide), 'Missing user journey guide: ' + guide);
    }
    const links = await evaluate('[...document.querySelectorAll("a[href]")].map(a=>({href:a.href,text:a.textContent.trim()})).filter(a=>{const u=new URL(a.href);return u.origin===location.origin && u.pathname.includes("/public/") && u.searchParams.has("route")})');
    if (report.require_journeys) assert.deepEqual([...new Set(links.map(link => new URL(link.href).searchParams.get('route')))].sort(), [...routes.keys()].sort(), 'Homepage must expose all six resource routes');
    for (const href of [...new Set(links.map(link => link.href))]) {
      const url = new URL(href); const ids = url.searchParams.getAll('route');
      assert(ids.length === 1 && routes.has(ids[0]), 'Homepage has an invalid route link');
      await navigate(url.href); await assertRoute(ids[0]);
    }
    return { route_links: links, journeys };
  });
  for (const viewport of [320, 375, 1440]) await check('homepage and directory layout at ' + viewport, async () => {
    await resize(viewport); const rows = [];
    for (const [name, relative] of [['home', ''], ['resources', 'public/index.html?route=companion'], ['downloads','downloads.html?role=product-interface-designer']]) {
      await navigate(relative); rows.push({ page: name, ...await layout() });
      await screenshot(name + '-' + viewport + '.png');
      if (name === 'downloads') {
        await click('a[href="#download-search"]');
        await wait('document.activeElement.id === "download-search"');
        rows.push({page:'download filters',...await layout()});
        await screenshot('download-filters-' + viewport + '.png');
      }
    }
    return rows;
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
  await check('no JavaScript keeps all project links usable', async () => {
    await call('Emulation.setScriptExecutionDisabled', { value: true });
    try {
      await navigate('public/index.html?route=cli', false);
      const links = await evaluate('[...document.querySelectorAll("#results .record-link")].map(a=>({href:a.href,visible:!!a.getClientRects().length}))');
      assert.equal(links.length, catalog.items.length); assert(links.every(link => link.visible));
      assert.deepEqual(new Set(links.map(link => link.href)), new Set(catalog.items.map(item => item.url)));
      assert.equal(await evaluate('getComputedStyle(document.querySelector("#filters")).display'), 'none');
      await layout(); await screenshot('resources-no-javascript-375.png');
      return { visible_project_links: links.length };
    } finally { await call('Emulation.setScriptExecutionDisabled', { value: false }); }
  });
  await check('downloads remain usable without JavaScript', async () => {
    await call('Emulation.setScriptExecutionDisabled', { value: true });
    try {
      await navigate('downloads.html?role=software-engineer', false);
      assert.equal(await evaluate('document.querySelectorAll(".download-card:not([hidden]) a[aria-label]").length'), downloads.items.length);
      await layout();
      return {visible_downloads:downloads.items.length};
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
    console.log(JSON.stringify({ status: report.status, passed: report.passed, failed: report.failed, errors: report.errors.length, blocked_external: report.blocked_external_requests.length, evidence: out }));
    if (report.status !== 'PASS') process.exitCode = 1;
  })();
const watchdog = setTimeout(() => { report.errors.push({ kind: 'timeout', message: 'Overall 120 second budget exceeded' }); finish().finally(() => process.exit(1)); }, 120000);
(async () => { await start(); await runChecks(); })()
  .catch(error => { report.errors.push({ kind: 'harness', message: error.stack || String(error) }); console.error(error.stack || error); })
  .finally(finish);
