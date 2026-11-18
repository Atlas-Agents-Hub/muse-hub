/* Explicit browser acceptance against an already owned synthetic loopback fixture.
 * Usage: node tests/browser_companion_notebook.mjs connection.json output-prefix
 * Requires an owned Chromium CDP port. Does not start a provider or public host.
 */
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
const connection = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const prefix = path.resolve(process.argv[3]);
assert.equal(connection.synthetic_scope_only, true);
const base = new URL(connection.base_url);
assert.equal(base.hostname, '127.0.0.1');
assert.equal(base.protocol, 'http:');
assert(Number.isInteger(connection.debug_port));
const token = 'synthetic-notebook-browser-fixture-' + 'x'.repeat(32);
const tabs = await fetch('http://127.0.0.1:' + connection.debug_port + '/json/list').then(r => r.json());
const tab = tabs.find(p => p.type === 'page' && p.url.startsWith(base.href));
assert(tab, 'OWNED_LOCAL_TAB_REQUIRED');
const socket = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise((resolve, reject) => {socket.addEventListener('open', resolve, {once: true}); socket.addEventListener('error', reject, {once: true});});
let sequence = 0, dropNextSave = false, droppedSave = false, loaded = 0, holdNextRead = false, heldRead = null;
const pending = new Map(), exceptions = [], external = [], writes = [], passed = [];
const report = {scope: 'synthetic-loopback-Chromium-not-native-iPhone', source_base: connection.source_base,
  started_at: new Date().toISOString(), passed, viewports: [], screenshots: [], expected_network_faults: 0};
function call(method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = ++sequence;
    const timeout = setTimeout(() => {pending.delete(id); reject(Error('CDP_TIMEOUT_' + method));}, 10000);
    pending.set(id, {resolve, reject, timeout}); socket.send(JSON.stringify({id, method, params}));
  });
}
socket.addEventListener('message', event => {
  const message = JSON.parse(event.data);
  if (message.id) {
    const job = pending.get(message.id); if (!job) return;
    pending.delete(message.id); clearTimeout(job.timeout);
    if (message.error) job.reject(Error('CDP_' + JSON.stringify(message.error))); else job.resolve(message.result || {});
  } else if (message.method === 'Page.loadEventFired') loaded += 1;
  else if (message.method === 'Runtime.exceptionThrown') exceptions.push(message.params.exceptionDetails.text);
  else if (message.method === 'Page.javascriptDialogOpening') call('Page.handleJavaScriptDialog', {accept: true}).catch(() => {});
  else if (message.method === 'Network.requestWillBeSent') {
    const request = message.params.request;
    if (/^https?:/.test(request.url) && !request.url.startsWith(base.href)) external.push(request.url);
    if (request.method === 'POST' && /\/api\/room\/(put|forget)$/.test(request.url)) writes.push(request.url);
  } else if (message.method === 'Fetch.requestPaused') {
    if (holdNextRead && message.params.request.url.endsWith('/api/room/list') && message.params.responseStatusCode === 200) {
      holdNextRead = false; heldRead = message.params.requestId;
    } else if (dropNextSave && message.params.request.url.endsWith('/api/room/put') && message.params.responseStatusCode === 200) {
      dropNextSave = false; droppedSave = true;
      call('Fetch.failRequest', {requestId: message.params.requestId, errorReason: 'ConnectionReset'}).catch(() => {});
    } else call('Fetch.continueRequest', {requestId: message.params.requestId}).catch(() => {});
  }
});
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
async function evaluate(expression) {
  const result = await call('Runtime.evaluate', {expression, returnByValue: true, awaitPromise: true});
  if (result.exceptionDetails) throw Error('BROWSER_EVALUATION_' + result.exceptionDetails.text);
  return result.result?.value;
}
async function wait(expression) {
  const until = Date.now() + 8000;
  while (Date.now() < until) {if (await evaluate(expression)) return; await pause(50);}
  throw Error('BROWSER_STATE_TIMEOUT_' + expression);
}
const click = id => evaluate('document.getElementById(' + JSON.stringify(id) + ').click()');
const fill = (id, value) => evaluate('document.getElementById(' + JSON.stringify(id) + ').value=' + JSON.stringify(value));
async function ready() {await wait("document.getElementById('notebook-workspace').getAttribute('aria-busy') === 'false'");}
async function unlock() {
  await wait("Boolean(document.getElementById('notebook-session-form'))");
  await click('tab-notebook');
  await fill('notebook-token', token);
  await evaluate("document.getElementById('notebook-token').focus(); document.getElementById('notebook-session-form').requestSubmit()");
  await wait("!document.getElementById('notebook-workspace').hidden"); await ready();
  await pause(250);
  assert.equal(await evaluate('document.activeElement.id'), 'room-note-text', 'UNLOCK_MUST_FOCUS_ENABLED_EDITOR');
}
async function save(text) {
  await fill('room-note-text', text);
  await evaluate("document.getElementById('room-note-form').requestSubmit()");
  await ready();
}
async function api(route, data) {
  return evaluate('(async()=>{const r=await fetch(' + JSON.stringify(route) + ',{method:"POST",headers:{"Authorization":' +
    JSON.stringify('Bearer ' + token) + ',"Content-Type":"application/json"},body:JSON.stringify(' + JSON.stringify(data) + ')});return {status:r.status,body:await r.json()}})()');
}
try {
  await call('Runtime.enable'); await call('Page.enable'); await call('Network.enable');
  const initialLoad = loaded;
  await call('Page.reload', {ignoreCache: true});
  for (let n=0; n<100 && loaded===initialLoad; n++) await pause(50);
  assert(loaded>initialLoad, 'PAGE_LOAD_UNCONFIRMED');
  await unlock(); passed.push('unlock-focus-token-cleared');
  assert.equal(await evaluate("document.getElementById('notebook-token').value"), '');
  const unique = 'Browser note ' + Date.now();
  await save(unique + '\n<script>literal text, never executed</script>');
  assert.match(await evaluate("document.getElementById('notebook-status').textContent"), /saved and read back/);
  let state = await api('/api/room/list', {room_id: 'notebook'});
  const created = state.body.notes.find(n => n.text.startsWith(unique));
  assert(created && created.revision === 1); passed.push('browser-to-http-to-sqlite-create');
  assert.equal(await evaluate("document.getElementById('room-note-list').querySelectorAll('script').length"), 0);
  const previousLoad = loaded;
  await call('Page.reload', {ignoreCache: true});
  for (let n=0; n<100 && loaded===previousLoad; n++) await pause(50);
  assert(loaded>previousLoad, 'RELOAD_UNCONFIRMED'); await unlock();
  assert((await evaluate("document.getElementById('room-note-list').textContent")).includes(unique));
  passed.push('reload-persistence-and-literal-markup');
  await evaluate('Array.from(document.querySelectorAll("#room-note-list button")).find(b=>b.textContent.includes(' + JSON.stringify(unique) + ')).click()');
  await save(unique + ' edited');
  state = await api('/api/room/list', {room_id: 'notebook'});
  assert.equal(state.body.notes.find(n => n.note_id === created.note_id).revision, 2); passed.push('revision-edit');
  // A different authorized request wins while this page is editing an old revision.
  await evaluate('Array.from(document.querySelectorAll("#room-note-list button")).find(b=>b.textContent.includes(' + JSON.stringify(unique) + ')).click()');
  const other = await api('/api/room/put', {room_id: 'notebook', note_id: created.note_id, text: unique + ' other editor', expected_revision: 2});
  assert.equal(other.status, 200);
  await save(unique + ' unsaved stale draft');
  assert.match(await evaluate("document.getElementById('notebook-status').textContent"), /newer saved revision/);
  assert.equal(await evaluate("document.getElementById('room-note-text').value"), unique + ' unsaved stale draft');
  assert.equal(await evaluate("document.getElementById('room-note-save').disabled"), true);
  await click('notebook-refresh'); await ready();
  assert.equal(await evaluate("document.getElementById('room-note-text').value"), unique + ' unsaved stale draft');
  passed.push('stale-update-draft-preserved-no-overwrite');
  await click('room-note-new');
  await call('Fetch.enable', {patterns: [{urlPattern: base.href + 'api/room/put', requestStage: 'Response'}]});
  dropNextSave = true;
  const writesBefore = writes.length;
  await save(unique + ' lost acknowledgement');
  assert(droppedSave, 'RESPONSE_FAULT_NOT_INJECTED');
  assert.match(await evaluate("document.getElementById('notebook-status').textContent"), /not confirmed/);
  assert.equal(await evaluate("document.getElementById('room-note-save').disabled"), true);
  await pause(250); assert.equal(writes.length, writesBefore + 1, 'AUTOMATIC_WRITE_RETRY');
  await click('notebook-refresh'); await ready();
  assert.match(await evaluate("document.getElementById('notebook-status').textContent"), /saved and read back/);
  assert.equal(writes.length, writesBefore + 1);
  await call('Fetch.disable'); report.expected_network_faults += 1;
  passed.push('lost-response-after-commit-reconciled-without-retry');
  await evaluate("document.getElementById('notebook-room').value='garden';document.getElementById('notebook-room').dispatchEvent(new Event('change',{bubbles:true}))"); await ready();
  assert.equal(await evaluate("document.querySelectorAll('#room-note-list li').length"), 0);
  await save(unique + ' garden');
  assert.equal(await evaluate("document.querySelectorAll('#room-note-list li').length"), 1);
  await evaluate("document.querySelector('#room-note-list button').click()");
  await click('room-note-delete'); await ready();
  assert.equal(await evaluate("document.querySelectorAll('#room-note-list li').length"), 0);
  passed.push('room-isolation-and-explicit-delete');
  // Original non-notebook interactions remain intact.
  await click('tab-arcade');
  const score = await evaluate("Number(document.getElementById('arcade-score').textContent)");
  await evaluate("document.querySelector('[data-pad][data-active=true]').click()");
  assert.equal(await evaluate("Number(document.getElementById('arcade-score').textContent)"), score + 1);
  await click('arcade-back'); assert.equal(await evaluate('document.activeElement.id'), 'tab-focus');
  await click('tab-studio'); await call('Emulation.setEmulatedMedia', {features: [{name: 'prefers-reduced-motion', value: 'reduce'}]});
  await evaluate("document.querySelector('[data-action=motion]').click()");
  assert.equal(await evaluate('document.body.dataset.motion'), 'paused');
  passed.push('arcade-back-motion-regressions'); await click('tab-notebook');
  await evaluate("document.getElementById('notebook-room').value='notebook';document.getElementById('notebook-room').dispatchEvent(new Event('change',{bubbles:true}))"); await ready();
  for (const width of [320,390,768,1440]) {
    await call('Emulation.setDeviceMetricsOverride', {width, height: 1000, deviceScaleFactor: 1, mobile: width < 768});
    await evaluate("document.getElementById('notebook').scrollIntoView({block:'start',behavior:'instant'})");
    await pause(100);
    const layout = await evaluate('({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,buttons:Array.from(document.querySelectorAll("#notebook button")).filter(b=>b.getClientRects().length).map(b=>({height:b.getBoundingClientRect().height,text:b.textContent}))})');
    assert(layout.scrollWidth <= layout.width + 1, 'DOCUMENT_OVERFLOW_' + width);
    assert(layout.buttons.every(b => b.height >= 44), 'SMALL_TOUCH_TARGET_' + width);
    const shot = await call('Page.captureScreenshot', {format: 'png', captureBeyondViewport: false});
    const file = prefix + '-' + width + '.png'; fs.writeFileSync(file, Buffer.from(shot.data, 'base64'), {flag:'wx'});
    report.screenshots.push(file); report.viewports.push(layout);
  }
  await evaluate("window.__textSizes=Array.from(document.querySelectorAll('#notebook h4,#notebook h5,#notebook p,#notebook label,#notebook button,#notebook textarea,#notebook select')).map(n=>[n,getComputedStyle(n).fontSize]);window.__textSizes.forEach(([n,size])=>n.style.fontSize=(parseFloat(size)*2)+'px')");
  assert(await evaluate('document.documentElement.scrollWidth<=innerWidth+1'), 'LARGE_TEXT_OVERFLOW');
  await evaluate("window.__textSizes.forEach(([n])=>n.style.fontSize='');delete window.__textSizes");
  report.large_text_method='Double computed font sizes on Notebook headings, labels, paragraphs and form controls; not native browser zoom';
  passed.push('responsive-four-widths-and-200-percent-text-stress');
  await click('notebook-lock');
  assert.equal(await evaluate("document.getElementById('room-note-list').children.length"), 0);
  assert.equal(await evaluate("document.getElementById('room-note-text').value"), '');
  assert.equal(await evaluate('document.activeElement.id'), 'notebook-token');
  const stored = await evaluate('({local:Object.keys(localStorage),session:Object.keys(sessionStorage)})');
  assert(stored.local.every(key => key === 'muse-hub/signal-trail/v1')); assert.equal(stored.session.length, 0);
  passed.push('lock-scrubs-notes-no-token-or-notes-in-browser-storage');
  await unlock();
  await call('Input.dispatchKeyEvent', {type:'keyDown',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});
  await call('Input.dispatchKeyEvent', {type:'keyUp',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});
  assert.equal(await evaluate('document.activeElement.id'), 'room-note-save', 'KEYBOARD_EDITOR_TO_SAVE');
  await call('Fetch.enable', {patterns: [{urlPattern: base.href + 'api/room/list', requestStage: 'Response'}]});
  holdNextRead = true; await click('notebook-refresh');
  for (let n=0; n<100 && !heldRead; n++) await pause(30);
  assert(heldRead, 'READ_RESPONSE_NOT_INTERCEPTED');
  await evaluate("document.getElementById('room-note-text').value='Unsaved synthetic thought';window.dispatchEvent(new PageTransitionEvent('pagehide',{persisted:true}))");
  await call('Fetch.continueRequest', {requestId: heldRead}); await call('Fetch.disable'); await pause(150);
  assert.equal(await evaluate("document.getElementById('room-note-list').children.length"), 0, 'PAGEHIDE_PRIVATE_NOTES_RETAINED');
  assert.equal(await evaluate("document.getElementById('room-note-text').value"), '', 'PAGEHIDE_DRAFT_RETAINED');
  assert.equal(await evaluate("document.getElementById('notebook-workspace').hidden"), true);
  passed.push('keyboard-tab-pagehide-clearing-and-late-response-refusal');
  assert.equal(external.length, 0, 'UNEXPECTED_EXTERNAL_REQUEST'); assert.equal(exceptions.length, 0, 'UNHANDLED_JAVASCRIPT');
  report.status = 'PASS';
} catch (error) {
  report.status = 'FAIL'; report.error = error.message; process.exitCode = 1;
} finally {
  report.finished_at = new Date().toISOString(); report.exceptions = exceptions; report.external = external; report.write_requests = writes.length;
  fs.writeFileSync(prefix + '.json', JSON.stringify(report, null, 2) + '\n', {flag:'wx'});
  console.log(JSON.stringify(report)); socket.close();
}
