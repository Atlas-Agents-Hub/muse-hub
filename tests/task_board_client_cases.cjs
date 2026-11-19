'use strict';
// Run the shipped board client against deterministic DOM and HTTP boundaries.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(process.argv[3], 'utf8');

class Element {
  constructor(tag = 'div') {
    this.tagName = tag; this.id = ''; this.children = []; this.events = {};
    this.value = ''; this.hidden = false; this.disabled = false; this.attributes = {};
    this.dataset = {}; this.text = ''; this.className = ''; this.files = [];
    this.classList = {add() {}, remove() {}};
  }
  set textContent(value) { this.text = String(value); this.children = []; }
  get textContent() { return this.text + this.children.map(child => child.textContent).join(''); }
  set innerHTML(_) { throw Error('UNSAFE_HTML_RENDER'); }
  append(...children) { this.children.push(...children); }
  replaceChildren(...children) { this.children = children; this.text = ''; }
  setAttribute(name, value) { this.attributes[name] = String(value); }
  removeAttribute(name) { delete this.attributes[name]; }
  addEventListener(name, callback) { this.events[name] = callback; }
  querySelectorAll(selector) {
    return this.children.flatMap(child => {
      const matches = selector.startsWith('.') ? child.className.split(' ').includes(selector.slice(1)) : child.tagName === selector;
      return (matches ? [child] : []).concat(child.querySelectorAll(selector));
    });
  }
  focus() { this.document.activeElement = this; }
  fire(name) { this.events[name]?.({preventDefault() {}, target: this}); }
  click() { this.fire('click'); }
  remove() {}
}
const card = (id = 'first', title = 'Read the brief', status = 'doing') => ({
  id, title, details: 'Preserve this context', status, priority: 'normal'
});
const clone = value => JSON.parse(JSON.stringify(value));
function fixture(initial = [card()]) {
  const fixed = new Map();
  function find(root, id) {
    if (root.id === id) return root;
    for (const child of root.children) { const result = find(child, id); if (result) return result; }
    return null;
  }
  const document = {
    getElementById(id) { return fixed.get(id) || [...fixed.values()].map(root => find(root, id)).find(Boolean) || null; },
    createElement(tag) { const element = new Element(tag); element.document = document; return element; },
    activeElement: null
  };
  document.body = document.createElement('body');
  for (const id of ['status', 'todo', 'doing', 'done', 'count-todo', 'count-doing', 'count-done',
    'summary', 'requests', 'session-form', 'session-key', 'unlock', 'workspace', 'card-form',
    'card-title', 'card-details', 'card-priority', 'card-submit', 'cancel-edit', 'composer-mode',
    'refresh', 'export', 'import', 'queue', 'lock', 'undo-removal', 'undo-removal-message', 'undo-remove']) {
    const element = document.createElement('div'); element.id = id; fixed.set(id, element);
  }
  fixed.get('card-priority').value = 'normal';
  fixed.get('workspace').hidden = true;
  fixed.get('undo-removal').hidden = true;
  fixed.get('cancel-edit').hidden = true;
  let board = {schema: 'muse-task-board/v1', cards: clone(initial)}, revision = initial.length ? 1 : 0;
  let writes = [], uuid = 0, writeFailure = null, loseAfterCommit = false;
  const response = (status, value) => ({status, ok: status >= 200 && status < 300, json: async () => clone(value)});
  const context = {
    document, structuredClone: clone, console, Blob, URL, setTimeout,
    crypto: {randomUUID: () => String(++uuid).padStart(32, '0')},
    Sortable: class { destroy() {} },
    fetch: async (url, options) => {
      if (url === '/api/state') return response(200, {
        notes: revision ? [{note_id: 'muse-task-board', text: JSON.stringify(board), revision}] : [],
        adapter: {enabled: true, revision: 1, requests: []}
      });
      assert.equal(url, '/api/note');
      const data = JSON.parse(options.body); writes.push(data);
      if (writeFailure) return response(writeFailure, {error: 'STALE_REVISION'});
      if (data.expected_revision !== revision) return response(409, {error: 'STALE_REVISION'});
      board = JSON.parse(data.text); revision++;
      if (loseAfterCommit) { loseAfterCommit = false; throw Error('LOST_REPLY_AFTER_COMMIT'); }
      return response(200, {note_id: 'muse-task-board', text: JSON.stringify(board), revision});
    }
  };
  vm.runInNewContext(source, context);
  async function settle() {
    for (let attempt = 0; attempt < 40; attempt++) {
      await new Promise(resolve => setImmediate(resolve));
      if (!document.body.attributes['aria-busy']) return;
    }
    throw Error('BOARD_DID_NOT_SETTLE');
  }
  const get = id => { const node = document.getElementById(id); assert(node, 'Missing control: ' + id); return node; };
  return {
    get, document, settle, state: () => ({board: clone(board), revision, writes: clone(writes)}),
    failWrites: value => { writeFailure = value; }, loseNextReply: () => { loseAfterCommit = true; },
    remoteChange: cards => { board = {schema: 'muse-task-board/v1', cards: clone(cards)}; revision++; },
    async unlock() { get('session-key').value = 'test-session-key'; get('session-form').fire('submit'); await settle(); },
    async click(id) { get(id).fire('click'); await settle(); },
    async submit(title, details = 'Updated context', priority = 'high') {
      get('card-title').value = title; get('card-details').value = details; get('card-priority').value = priority;
      get('card-form').fire('submit'); await settle();
    }
  };
}

const cases = {
  async full_board_can_make_room_for_new_work() {
    const initial = Array.from({length: 24}, (_, index) => card('item' + index, 'Task ' + index, 'todo'));
    const f = fixture(initial); await f.unlock(); await f.click('remove-item0');
    await f.submit('The next project action');
    assert.equal(f.state().board.cards.length, 24);
    assert.equal(f.state().board.cards.at(-1).title, 'The next project action');
    assert(!f.state().board.cards.some(item => item.id === 'item0'));
  },
  async edit_preserves_identity_and_status() {
    const f = fixture(); await f.unlock(); await f.click('edit-first');
    assert.equal(f.get('card-title').value, 'Read the brief');
    assert.equal(f.get('card-submit').textContent, 'Save card');
    assert.equal(f.document.activeElement.id, 'card-title');
    await f.submit('Read the revised brief', 'New context', 'high');
    assert.deepEqual(f.state().board.cards, [{id: 'first', title: 'Read the revised brief', details: 'New context', status: 'doing', priority: 'high'}]);
    assert.equal(f.state().writes[0].expected_revision, 1);
    assert.equal(f.get('card-title').value, '');
    assert.equal(f.get('card-submit').textContent, 'Add card');
    assert.equal(f.document.activeElement.id, 'edit-first');
  },
  async removal_undo_restores_order_and_focus() {
    const original = [card('first'), card('second', 'Check the diagram', 'todo')];
    const f = fixture(original); await f.unlock(); await f.click('remove-first');
    assert.deepEqual(f.state().board.cards.map(item => item.id), ['second']);
    assert.equal(f.get('undo-removal').hidden, false);
    assert.equal(f.document.activeElement.id, 'undo-remove');
    await f.click('undo-remove');
    assert.deepEqual(f.state().board.cards, original);
    assert.deepEqual(f.state().writes.map(write => write.expected_revision), [1, 2]);
    assert.equal(f.get('undo-removal').hidden, true);
    assert.equal(f.document.activeElement.id, 'edit-first');
  },
  async next_mutation_expires_undo() {
    const f = fixture(); await f.unlock(); await f.click('remove-first');
    await f.submit('A new task');
    assert.equal(f.get('undo-removal').hidden, true);
    const writes = f.state().writes.length;
    await f.click('undo-remove');
    assert.equal(f.state().writes.length, writes);
    assert.equal(f.state().board.cards[0].title, 'A new task');
  },
  async conflict_preserves_draft_and_fences_writes() {
    const f = fixture(); await f.unlock(); await f.click('edit-first');
    f.remoteChange([card('first', 'Other window changed this')]);
    await f.submit('My unsaved edit');
    assert.equal(f.get('card-title').value, 'My unsaved edit');
    assert.match(f.get('status').textContent, /another window/i);
    const writes = f.state().writes.length;
    await f.submit('Do not overwrite');
    assert.equal(f.state().writes.length, writes);
    await f.click('refresh');
    assert.equal(f.get('card-title').value, 'Do not overwrite');
    assert.equal(f.get('card-submit').disabled, true, 'Refreshing must not apply a stale draft to a newer card');
    await f.click('cancel-edit'); await f.click('edit-first');
    assert.equal(f.get('card-title').value, 'Other window changed this');
    await f.submit('Merged edit');
    assert.equal(f.state().board.cards[0].title, 'Merged edit');
  },
  async stale_undo_never_overwrites_new_cards() {
    const f = fixture(); await f.unlock(); await f.click('remove-first');
    f.remoteChange([card('remote', 'New task in another window', 'todo')]);
    await f.click('undo-remove');
    assert.deepEqual(f.state().board.cards.map(item => item.id), ['remote']);
    assert.equal(f.state().writes.at(-1).expected_revision, 2);
    assert.match(f.get('status').textContent, /another window/i);
    await f.click('refresh');
    assert.equal(f.get('undo-removal').hidden, true);
  },
  async lost_remove_reply_is_reconciled_before_another_write() {
    const f = fixture(); await f.unlock(); f.loseNextReply(); await f.click('remove-first');
    assert.equal(f.state().board.cards.length, 0, 'Server committed the removal');
    assert.equal(f.get('undo-removal').hidden, true, 'Do not promise undo for an unacknowledged operation');
    await f.submit('Wait for refresh');
    assert.equal(f.state().writes.length, 1);
    await f.click('refresh'); await f.submit('A new action');
    assert.equal(f.state().writes.length, 2);
    assert.equal(f.state().writes[1].expected_revision, 2);
    assert.equal(f.state().board.cards[0].title, 'A new action');
  },
  async text_is_literal_and_cancel_keeps_saved_card() {
    const title = '<img src=x onerror=alert(1)>';
    const f = fixture([card('first', title)]); await f.unlock();
    assert.match(f.get('doing').textContent, /<img src=x/);
    await f.click('edit-first');
    f.get('card-title').value = 'Unsaved draft'; await f.click('cancel-edit');
    assert.equal(f.state().writes.length, 0);
    assert.equal(f.state().board.cards[0].title, title);
    assert.equal(f.document.activeElement.id, 'edit-first');
    await f.click('remove-first');
    assert.match(f.get('undo-removal-message').textContent, /<img src=x/);
    await f.click('lock');
    assert.equal(f.get('undo-removal').hidden, true);
    assert.equal(f.get('card-title').value, '');
  }
};
(async () => {
  const name = process.argv[2]; assert(cases[name], 'UNKNOWN_CASE'); await cases[name]();
  console.log(JSON.stringify({case: name, status: 'PASS'}));
})().catch(error => { console.error(error); process.exitCode = 1; });
