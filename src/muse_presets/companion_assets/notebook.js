/* Opt-in loopback Notebook. No provider calls, persistent browser notes or retries. */
(() => {
  'use strict';
  const el = id => document.getElementById(id);
  if (!el('room-note-form')) return;
  let token = '', room = 'notebook', notes = [], busy = false, blocked = false;
  let pending = null, current = null, sessionEpoch = 0;
  const status = text => { el('notebook-status').textContent = text; };
  const draft = () => el('room-note-text').value;
  const dirty = () => current && draft() !== current.text;
  const uid = () => 'n' + crypto.randomUUID().replaceAll('-', '');
  const knownRooms = new Set(['focus', 'notebook', 'garden', 'arcade', 'studio']);

  function controls() {
    el('notebook-workspace').setAttribute('aria-busy', String(busy));
    for (const id of ['notebook-refresh', 'notebook-lock', 'notebook-room', 'room-note-new']) el(id).disabled = busy;
    el('room-note-text').disabled = busy || Boolean(pending);
    el('room-note-save').disabled = busy || blocked || Boolean(pending);
    el('room-note-delete').disabled = busy || blocked || Boolean(pending);
    for (const button of el('room-note-list').querySelectorAll('button')) button.disabled = busy || Boolean(pending);
    el('notebook-session-form').querySelector('button').disabled = busy;
  }
  function resetEditor() {
    current = {note_id: uid(), revision: 0, text: ''};
    el('room-note-text').value = '';
    el('notebook-editor-title').textContent = 'A new note';
    el('notebook-revision').textContent = 'Not saved yet';
    el('room-note-delete').hidden = true;
    blocked = false;
  }
  function discardDraft() {
    return !dirty() || window.confirm('Discard the unsaved changes in this tab?');
  }
  function node(tag, text) {
    const item = document.createElement(tag); item.textContent = text; return item;
  }
  function renderNotes() {
    const list = el('room-note-list'); list.replaceChildren();
    el('notebook-count').textContent = String(notes.length);
    el('notebook-empty').hidden = notes.length !== 0;
    for (const note of notes) {
      const li = node('li', '');
      const button = node('button', ''); button.type = 'button';
      const heading = note.text.split('\n')[0].slice(0, 80);
      button.append(node('strong', heading), node('span', 'Revision ' + note.revision + ' · Open to edit'));
      button.addEventListener('click', () => {
        if (busy || pending || !discardDraft()) return;
        current = {...note}; blocked = false;
        el('room-note-text').value = note.text;
        el('notebook-editor-title').textContent = 'Edit your note';
        el('notebook-revision').textContent = 'Revision ' + note.revision;
        el('room-note-delete').hidden = false;
        controls(); el('room-note-text').focus();
        status('Saved version loaded. Changes need an explicit Save.');
      });
      li.append(button); list.append(li);
    }
  }
  async function api(path, data) {
    const requestEpoch = sessionEpoch;
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 8000);
    try {
      const response = await fetch(path, {method: 'POST', cache: 'no-store', credentials: 'omit', redirect: 'error',
        headers: {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'},
        body: JSON.stringify(data), signal: controller.signal});
      const body = await response.json();
      if (requestEpoch !== sessionEpoch) throw new Error('SESSION_CLEARED');
      if (!response.ok) {
        const error = new Error(typeof body.error === 'string' ? body.error : 'REQUEST_UNCONFIRMED');
        error.status = response.status; throw error;
      }
      return body;
    } finally { clearTimeout(timer); }
  }
  function validList(data) {
    return data && data.room_id === room && data.native_installed === false && data.provider_connected === false &&
      Array.isArray(data.notes) && data.notes.length <= 256 &&
      new Set(data.notes.map(n => n && n.note_id)).size === data.notes.length &&
      data.notes.every(n => n && n.room_id === room && /^[A-Za-z][A-Za-z0-9-]{0,39}$/.test(n.note_id) &&
        typeof n.text === 'string' && n.text.length <= 8000 && Number.isSafeInteger(n.revision) && n.revision > 0);
  }
  async function refresh() {
    const data = await api('/api/room/list', {room_id: room});
    if (!validList(data)) throw new Error('READBACK_UNCONFIRMED');
    notes = data.notes; renderNotes();
    if (pending) {
      const found = notes.find(note => note.note_id === pending.note_id);
      const observed = pending.operation === 'forget' ? !found :
        found && found.revision === pending.expected_revision + 1 && found.text === pending.text.trim();
      const operation = pending.operation;
      pending = null;
      if (observed) {
        resetEditor();
        status(operation === 'forget' ? 'The note is absent from saved notes. No write was retried.' : 'Note saved and read back from SQLite. No write was retried.');
      } else {
        blocked = true;
        status('Saved state differs from the attempted change. Your draft is preserved. Review a saved note or choose New note; nothing was retried.');
      }
    } else if (!blocked) status('Saved notes read back from this computer.');
  }
  async function perform(action) {
    if (busy) return;
    const actionEpoch = sessionEpoch;
    busy = true; controls();
    try { await action(); }
    catch (error) {
      if (actionEpoch !== sessionEpoch) return;
      if (pending && error.status >= 400 && error.status < 500) {
        pending = null;
        blocked = error.status === 409 || error.status === 401 || error.status === 403;
        status(error.status === 409 ? 'A newer saved revision exists. Your draft is preserved. Refresh saved notes, then review before editing again.' :
          'The change was refused (' + error.message + '). Your draft is preserved. Check the input or reopen the local session.');
      } else {
        blocked = true;
        status(pending ? 'Save or delete outcome is not confirmed. Your draft is preserved. Use Refresh saved notes before any new change; do not resend.' :
          'Could not read saved notes. Check the local session and server, then Refresh saved notes.');
      }
    } finally { if (actionEpoch === sessionEpoch) { busy = false; controls(); } }
  }
  async function mutate(operation) {
    if (pending || blocked || !current) return;
    pending = {operation, room_id: room, note_id: current.note_id, expected_revision: current.revision};
    if (operation === 'put') pending.text = draft();
    controls();
    const {operation: _, ...body} = pending;
    const result = await api('/api/room/' + operation, body);
    if (!result || result.note_id !== pending.note_id || result.room_id !== room ||
        result.revision !== pending.expected_revision + 1) throw new Error('MUTATION_READBACK_UNCONFIRMED');
    await refresh();
  }
  el('notebook-session-form').addEventListener('submit', event => {
    event.preventDefault();
    const openingEpoch = sessionEpoch;
    perform(async () => {
      token = el('notebook-token').value;
      el('notebook-token').value = '';
      pending = null; blocked = false; room = 'notebook';
      el('notebook-room').value = room; resetEditor();
      await refresh();
      el('notebook-unlock').hidden = true; el('notebook-workspace').hidden = false;
    }).then(() => {
      // Enabled controls in a just-revealed panel may not be focusable until paint.
      const openedToken = token, previousFocus = document.activeElement;
      const focusEditor = () => {
        if (openingEpoch === sessionEpoch && token && token === openedToken && !busy && !el('notebook-workspace').hidden &&
            (document.activeElement === previousFocus || document.activeElement === document.body)) {
          el('room-note-text').focus({preventScroll: true});
        }
      };
      requestAnimationFrame(focusEditor);
      setTimeout(focusEditor, 120);
    });
  });
  el('room-note-form').addEventListener('submit', event => {
    event.preventDefault(); perform(() => mutate('put'));
  });
  el('room-note-delete').addEventListener('click', () => {
    if (busy || blocked || pending || !current || !current.revision) return;
    if (window.confirm('Delete this saved note? This is not secure physical erasure.')) perform(() => mutate('forget'));
  });
  el('notebook-refresh').addEventListener('click', () => perform(async () => {
    // A read is allowed after an uncertain effect; a mutation is never retried.
    const hadPending = Boolean(pending);
    await refresh();
    if (!hadPending && blocked) status('Saved notes refreshed. Your draft is unchanged. Open a saved note or choose New note after reviewing.');
  }));
  el('room-note-new').addEventListener('click', () => {
    if (busy || pending || !discardDraft()) return;
    resetEditor(); controls(); el('room-note-text').focus(); status('New draft. Nothing saved yet.');
  });
  el('notebook-room').addEventListener('change', event => {
    const next = event.target.value;
    if (busy || pending || !knownRooms.has(next) || !discardDraft()) { event.target.value = room; return; }
    perform(async () => { room = next; notes = []; renderNotes(); resetEditor(); await refresh(); });
  });
  function clearSession() {
    sessionEpoch += 1; // A late fetch must not refill a locked or cached page.
    token = ''; notes = []; pending = null; current = null; blocked = false; busy = false;
    el('room-note-text').value = ''; el('notebook-token').value = ''; renderNotes();
    el('notebook-workspace').hidden = true; el('notebook-unlock').hidden = false;
    status('Locked. Page memory cleared; the saved database was not erased.'); controls();
  }
  el('notebook-lock').addEventListener('click', () => {
    if (busy || (dirty() && !window.confirm('Lock and clear the unsaved draft from this page?'))) return;
    clearSession(); el('notebook-token').focus();
  });
  window.addEventListener('beforeunload', event => {
    if (dirty() || pending) { event.preventDefault(); event.returnValue = ''; }
  });
  window.addEventListener('pagehide', clearSession);
  controls();
})();
