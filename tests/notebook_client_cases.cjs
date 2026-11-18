/* Execute the shipped Notebook client against deterministic DOM/HTTP boundaries.
 * This is a client state regression, not a replacement for real-browser checks.
 */
'use strict';
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync(process.argv[3], 'utf8');

class Element {
  constructor(id = '', tag = 'div') {
    this.id = id; this.tagName = tag; this.children = []; this.events = {};
    this.value = ''; this.hidden = false; this.disabled = false; this.attributes = {}; this.text = '';
  }
  set textContent(value) { this.text = String(value); this.children = []; }
  get textContent() { return this.text + this.children.map(child => child.textContent).join(''); }
  append(...children) { this.children.push(...children); }
  replaceChildren(...children) { this.children = children; this.text = ''; }
  setAttribute(name, value) { this.attributes[name] = String(value); }
  getAttribute(name) { return this.attributes[name]; }
  addEventListener(name, callback) { this.events[name] = callback; }
  querySelectorAll(tag) {
    return this.children.flatMap(child => (child.tagName === tag ? [child] : []).concat(child.querySelectorAll(tag)));
  }
  querySelector(tag) { return this.querySelectorAll(tag)[0]; }
  focus() { this.document.activeElement = this; }
  fire(name) { this.events[name]?.({preventDefault() {}, target: this}); }
}
function fixture(initial = []) {
  const nodes = new Map();
  const get = id => {
    if (!nodes.has(id)) { const element = new Element(id); element.document = document; nodes.set(id, element); }
    return nodes.get(id);
  };
  const document = {
    getElementById: get,
    createElement(tag) { const element = new Element('', tag); element.document = document; return element; },
    body: new Element('body'), activeElement: null
  };
  document.activeElement = document.body;
  get('notebook-workspace').hidden = true;
  get('notebook-session-form').append(document.createElement('button'));
  let rows = initial.map(note => ({...note})), listFailure = null, afterWrite = null, writeFailure = null, writes = 0;
  const response = (status, body, malformed = false) => ({
    status, ok: status >= 200 && status < 300,
    json: async () => { if (malformed) throw Error('INVALID_JSON'); return body; }
  });
  const fetch = async (route, options) => {
    assert.equal(options.method, 'POST');
    assert.match(options.headers.Authorization, /^Bearer .{32,}$/);
    const data = JSON.parse(options.body);
    if (route === '/api/room/list') {
      assert.deepEqual(Object.keys(data), ['room_id']);
      if (listFailure) return response(listFailure.status, {error: listFailure.error}, listFailure.malformed);
      return response(200, {room_id: data.room_id, notes: rows.map(note => ({...note})),
        native_installed: false, provider_connected: false});
    }
    if (route === '/api/room/put') {
      writes++;
      if (writeFailure) return response(writeFailure, {error: 'STALE_REVISION'});
      assert.deepEqual(Object.keys(data).sort(), ['expected_revision', 'note_id', 'room_id', 'text']);
      const row = {room_id: data.room_id, note_id: data.note_id, text: data.text.trim(), revision: data.expected_revision + 1};
      rows = rows.filter(note => note.note_id !== row.note_id).concat(row);
      listFailure = afterWrite;
      return response(200, row);
    }
    throw Error('UNEXPECTED_ROUTE_' + route);
  };
  let uuid = 0;
  vm.runInNewContext(source, {
    document, window: {confirm: () => true, addEventListener() {}}, fetch,
    crypto: {randomUUID: () => String(++uuid).padStart(32, '0')},
    AbortController, setTimeout, clearTimeout, requestAnimationFrame: callback => setTimeout(callback, 0)
  });
  async function settle() {
    for (let i = 0; i < 100; i++) {
      await new Promise(resolve => setImmediate(resolve));
      if (get('notebook-workspace').getAttribute('aria-busy') === 'false') return;
    }
    throw Error('CLIENT_DID_NOT_SETTLE');
  }
  return {get, settle, state: () => ({writes, rows}),
    failList: value => { listFailure = value; },
    failAfterWrite: value => { afterWrite = value; },
    failWrite: value => { writeFailure = value; },
    async unlock() { get('notebook-token').value = 'synthetic-client-session-' + 'x'.repeat(32); get('notebook-session-form').fire('submit'); await settle(); },
    async save(text) { get('room-note-text').value = text; get('room-note-form').fire('submit'); await settle(); }
  };
}
const note = {room_id: 'notebook', note_id: 'note1', text: 'Private owner note', revision: 1};
const cases = {
  async revoked_read_403() {
    const f = fixture([note]); await f.unlock();
    const oldButton = f.get('room-note-list').querySelector('button');
    oldButton.fire('click');
    f.failList({status: 403, error: 'SESSION_SCOPE_CHANGED'});
    f.get('notebook-refresh').fire('click'); await f.settle();
    assert.equal(f.get('notebook-workspace').hidden, true, 'Revoked scope must hide the workspace');
    assert.equal(f.get('room-note-list').children.length, 0, 'Revoked scope must clear saved notes');
    assert.equal(f.get('room-note-text').value, '', 'Revoked scope must clear the draft');
    oldButton.fire('click'); // A retained event closure must not restore cleared private text.
    assert.equal(f.get('room-note-text').value, '');
    assert.equal(f.get('room-note-save').disabled, true);
    f.get('room-note-new').fire('click');
    assert.equal(f.get('room-note-save').disabled, true);
    assert.equal(f.state().writes, 0);
  },
  async revoked_read_401_malformed() {
    const f = fixture([note]); await f.unlock();
    f.failList({status: 401, error: 'SESSION_INVALID', malformed: true});
    f.get('notebook-refresh').fire('click'); await f.settle();
    assert.equal(f.get('notebook-workspace').hidden, true, 'HTTP authority refusal must clear even an invalid response body');
    assert.equal(f.get('room-note-list').children.length, 0);
    assert.equal(f.get('room-note-save').disabled, true);
  },
  async committed_write_read_403() {
    const f = fixture(); await f.unlock();
    f.failAfterWrite({status: 403, error: 'SESSION_SCOPE_CHANGED'});
    await f.save('Acknowledged once');
    assert.equal(f.state().writes, 1);
    assert.equal(f.state().rows[0].text, 'Acknowledged once');
    assert.match(f.get('notebook-status').textContent, /acknowledged/i);
    assert.doesNotMatch(f.get('notebook-status').textContent, /change was refused/i);
    assert.equal(f.get('notebook-workspace').hidden, true);
    assert.equal(f.get('room-note-text').value, '');
    assert.equal(f.get('room-note-save').disabled, true);
  },
  async committed_write_read_400() {
    const f = fixture(); await f.unlock();
    f.failAfterWrite({status: 400, error: 'READ_REFUSED'});
    await f.save('Readback still pending');
    assert.equal(f.state().writes, 1);
    assert.doesNotMatch(f.get('notebook-status').textContent, /change was refused/i);
    assert.equal(f.get('room-note-save').disabled, true);
    await f.save('Do not retry');
    assert.equal(f.state().writes, 1, 'A failed follow-up read must not release the write fence');
    f.failList(null); f.get('notebook-refresh').fire('click'); await f.settle();
    assert.match(f.get('notebook-status').textContent, /saved and read back/i);
    assert.equal(f.state().writes, 1);
  },
  async mutation_conflict_preserves_draft() {
    const f = fixture([note]); await f.unlock();
    f.get('room-note-list').querySelector('button').fire('click');
    f.failWrite(409); await f.save('Uncommitted draft');
    assert.equal(f.get('room-note-text').value, 'Uncommitted draft');
    assert.equal(f.get('notebook-workspace').hidden, false);
    assert.equal(f.get('room-note-save').disabled, true);
    assert.equal(f.state().rows[0].text, 'Private owner note');
  },
  async unicode_saved_note_is_readable() {
    const text = '😀'.repeat(4001);
    const f = fixture([{...note, text}]); await f.unlock();
    assert.equal(f.get('notebook-workspace').hidden, false, '4001 Unicode code points are within the server limit');
    f.get('room-note-list').querySelector('button').fire('click');
    assert.equal(f.get('room-note-text').value, text);
  },
  async unicode_limit_save() {
    const f = fixture(); await f.unlock(); await f.save('😀'.repeat(8000));
    assert.equal(f.state().writes, 1);
    assert.equal(Array.from(f.state().rows[0].text).length, 8000);
    assert.match(f.get('notebook-status').textContent, /saved and read back/i);
  },
  async unicode_over_limit_refused_locally() {
    const f = fixture(); await f.unlock(); await f.save('😀'.repeat(8001));
    assert.equal(f.state().writes, 0, 'Over-limit Unicode input must not send a mutation');
    assert.equal(Array.from(f.get('room-note-text').value).length, 8001);
    assert.match(f.get('notebook-status').textContent, /8,000/);
  }
};
(async () => {
  const name = process.argv[2]; assert(cases[name], 'UNKNOWN_CASE'); await cases[name]();
  console.log(JSON.stringify({case: name, status: 'PASS'}));
})().catch(error => { console.error(error); process.exitCode = 1; });
