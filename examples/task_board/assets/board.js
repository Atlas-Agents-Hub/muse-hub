'use strict';
const byId = id => document.getElementById(id);
const states = ['todo', 'doing', 'done'];
const stateNames = {todo: 'To do', doing: 'In progress', done: 'Done'};
let token = '', state = null, revision = 0, adapter = null, busy = false, pendingPlan = null;
let editingId = null, editingRevision = null, undoRemoval = null, writeBlocked = false;
const sorters = [];
const message = text => { byId('status').textContent = text; };
const freshId = prefix => prefix + crypto.randomUUID().replaceAll('-', '');
const make = (tag, text, className = '') => {
  const node = document.createElement(tag);
  node.textContent = text;
  if (className) node.className = className;
  return node;
};
function validateBoard(value) {
  if (!value || typeof value !== 'object' || Array.isArray(value) ||
      Object.keys(value).sort().join(',') !== 'cards,schema' || value.schema !== 'muse-task-board/v1' ||
      !Array.isArray(value.cards) || value.cards.length > 24) throw new Error('Choose a Muse board with up to 24 cards.');
  const ids = new Set();
  for (const card of value.cards) {
    if (!card || Object.keys(card).sort().join(',') !== 'details,id,priority,status,title' ||
        typeof card.id !== 'string' || !/^[a-zA-Z0-9_-]{1,60}$/.test(card.id) || ids.has(card.id) ||
        typeof card.title !== 'string' || !card.title.trim() || card.title.length > 120 ||
        typeof card.details !== 'string' || card.details.length > 240 ||
        !states.includes(card.status) || !['high', 'normal', 'low'].includes(card.priority) ||
        (card.title + card.details).includes('\u0000')) throw new Error('A card has an invalid or duplicate field.');
    ids.add(card.id);
  }
  if (JSON.stringify(value).length > 7500) throw new Error('This board is full. Export it before starting another.');
  return value;
}
async function api(path, data) {
  const options = {method: data === undefined ? 'GET' : 'POST',
    headers: {Authorization: 'Bearer ' + token}, credentials: 'omit', redirect: 'error', cache: 'no-store'};
  if (data !== undefined) {
    options.headers['Content-Type'] = 'application/json';
    options.body = JSON.stringify(data);
  }
  const response = await fetch(path, options);
  const result = await response.json();
  if (!response.ok) throw new Error(result.error || 'The request did not finish.');
  return result;
}
async function refresh() {
  const result = await api('/api/state');
  const saved = result.notes.find(note => note.note_id === 'muse-task-board');
  state = validateBoard(saved ? JSON.parse(saved.text) : {schema: 'muse-task-board/v1', cards: []});
  revision = saved ? saved.revision : 0;
  adapter = result.adapter;
  writeBlocked = false;
  undoRemoval = null;
  render();
}
async function perform(action) {
  if (busy) return false;
  busy = true;
  document.body.classList.add('busy');
  document.body.setAttribute('aria-busy', 'true');
  try { await action(); return true; }
  catch (error) {
    message(error.message === 'STALE_REVISION'
      ? 'The board changed in another window. Refresh to pick up those changes.'
      : error.message + ' Refresh before repeating a save.');
    if (state) render();
    return false;
  } finally {
    busy = false;
    document.body.classList.remove('busy');
    document.body.removeAttribute('aria-busy');
  }
}
async function save(next, focusId) {
  if (writeBlocked) throw new Error('Refresh the board before saving another change.');
  validateBoard(next);
  const text = JSON.stringify(next);
  let result;
  try {
    result = await api('/api/note', {note_id: 'muse-task-board', text, expected_revision: revision});
    if (result.note_id !== 'muse-task-board' || result.text !== text || result.revision !== revision + 1)
      throw new Error('The save response could not be confirmed.');
  } catch (error) {
    writeBlocked = true;
    throw error;
  }
  state = next; revision = result.revision;
  undoRemoval = null;
  render();
  message('Board saved.');
  if (focusId) byId(focusId)?.focus();
  return revision;
}
function mutate(change, focusId) {
  return perform(async () => {
    if (!state) return;
    const next = structuredClone(state);
    change(next);
    await save(next, focusId);
  });
}
function resetComposer(focusId) {
  editingId = null; editingRevision = null;
  byId('card-title').value = ''; byId('card-details').value = ''; byId('card-priority').value = 'normal';
  updateComposer();
  if (focusId) byId(focusId)?.focus();
}
function updateComposer() {
  byId('composer-mode').textContent = editingId ? 'Edit your card' : 'Add a next action';
  byId('card-submit').textContent = editingId ? 'Save card' : 'Add card';
  byId('card-submit').disabled = writeBlocked || Boolean(editingId && editingRevision !== revision);
  byId('cancel-edit').hidden = !editingId;
}
function editCard(id) {
  if (busy || writeBlocked || !state) return;
  const card = state.cards.find(item => item.id === id);
  if (!card) return;
  editingId = id; editingRevision = revision;
  byId('card-title').value = card.title; byId('card-details').value = card.details;
  byId('card-priority').value = card.priority;
  updateComposer(); byId('card-title').focus();
  message('Edit the title, context or priority, then save your card.');
}
function renderUndo() {
  byId('undo-removal').hidden = !undoRemoval;
  byId('undo-removal-message').textContent = undoRemoval ? 'Removed “' + undoRemoval.title + '”.' : '';
  byId('undo-remove').disabled = writeBlocked;
}
function removeCard(id) {
  if (busy || writeBlocked || !state) return;
  return perform(async () => {
    const removed = state.cards.find(card => card.id === id);
    if (!removed) return;
    const previous = structuredClone(state);
    const next = structuredClone(state); next.cards = next.cards.filter(card => card.id !== id);
    const savedRevision = await save(next);
    if (editingId === id) resetComposer();
    undoRemoval = {board: previous, revision: savedRevision, cardId: id, title: removed.title};
    renderUndo(); byId('undo-remove').focus();
    message('Card removed. Undo is available until your next saved board change or refresh.');
  });
}
function render() {
  for (const sorter of sorters) sorter.destroy();
  sorters.length = 0;
  for (const status of states) {
    const list = byId(status); list.replaceChildren();
    const cards = state.cards.filter(card => card.status === status);
    byId('count-' + status).textContent = String(cards.length);
    if (!cards.length) list.append(make('p', status === 'todo' ? 'Add your first next action above.' : 'Move a card here when it is ready.', 'empty'));
    for (const card of cards) {
      const article = make('article', '', 'card'); article.dataset.id = card.id;
      const top = make('div', '', 'card-top');
      top.append(make('h4', card.title));
      const handle = make('span', '⠿', 'handle'); handle.setAttribute('aria-hidden', 'true');
      top.append(handle); article.append(top);
      if (card.details) article.append(make('p', card.details));
      article.append(make('span', card.priority + ' priority', 'priority ' + card.priority));
      const controls = make('div', '', 'card-controls');
      const select = make('select', ''); select.id = 'move-' + card.id;
      select.disabled = writeBlocked;
      select.setAttribute('aria-label', 'Move ' + card.title);
      for (const nextState of states) {
        const option = make('option', stateNames[nextState]); option.value = nextState;
        option.selected = nextState === card.status; select.append(option);
      }
      select.addEventListener('change', () => {
        const target = select.value;
        mutate(next => { next.cards.find(item => item.id === card.id).status = target; }, select.id);
      });
      const up = make('button', '↑', 'quiet'); up.type = 'button';
      up.disabled = writeBlocked;
      up.setAttribute('aria-label', 'Move ' + card.title + ' earlier');
      up.addEventListener('click', () => mutate(next => {
        const at = next.cards.findIndex(item => item.id === card.id);
        let before = at - 1;
        while (before >= 0 && next.cards[before].status !== card.status) before--;
        if (before >= 0) [next.cards[before], next.cards[at]] = [next.cards[at], next.cards[before]];
      }, select.id));
      controls.append(select, up); article.append(controls);
      const actions = make('div', '', 'card-actions');
      const edit = make('button', 'Edit', 'quiet'); edit.type = 'button'; edit.id = 'edit-' + card.id;
      edit.setAttribute('aria-label', 'Edit ' + card.title); edit.disabled = writeBlocked;
      edit.addEventListener('click', () => editCard(card.id));
      const remove = make('button', 'Remove', 'quiet'); remove.type = 'button'; remove.id = 'remove-' + card.id;
      remove.setAttribute('aria-label', 'Remove ' + card.title); remove.disabled = writeBlocked;
      remove.addEventListener('click', () => removeCard(card.id));
      actions.append(edit, remove); article.append(actions); list.append(article);
    }
    sorters.push(new Sortable(list, {group: 'muse-board', animation: 160, handle: '.handle', draggable: '.card',
      ghostClass: 'sortable-ghost', onMove: () => !busy && !writeBlocked, onEnd: () => {
        if (busy || writeBlocked) { render(); return; }
        const order = states.flatMap(status => [...byId(status).querySelectorAll('.card')].map(card => ({id: card.dataset.id, status})));
        mutate(next => {
          const map = new Map(next.cards.map(card => [card.id, card]));
          next.cards = order.map(item => ({...map.get(item.id), status: item.status}));
        });
      }}));
  }
  const complete = state.cards.filter(card => card.status === 'done').length;
  byId('summary').textContent = state.cards.length ? `${state.cards.length} cards · ${complete} finished · a little progress at a time.` : 'A clear start for your next project.';
  updateComposer(); renderUndo();
  byId('requests').replaceChildren();
  const requests = adapter.requests.filter(request => {
    try { return JSON.parse(request.prompt).schema === 'muse-board-plan/v1'; }
    catch { return false; }
  });
  if (!requests.length) byId('requests').append(make('p', 'Your requests and saved results will appear here.'));
  for (const request of requests.slice(-5).reverse()) {
    const row = make('article', '', 'request'); row.append(make('strong', 'Board plan · ' + request.state));
    if (request.result) row.append(make('pre', request.result));
    else row.append(make('p', 'Three next actions from your selected cards.'));
    byId('requests').append(row);
  }
}
byId('session-form').addEventListener('submit', event => {
  event.preventDefault(); perform(async () => {
    token = byId('session-key').value; await refresh();
    byId('session-key').value = ''; byId('unlock').hidden = true; byId('workspace').hidden = false;
    message('Your saved board is open.'); byId('card-title').focus();
  });
});
byId('card-form').addEventListener('submit', async event => {
  event.preventDefault();
  if (!state || busy) return;
  if (editingId) {
    const id = editingId;
    const saved = await mutate(next => {
      if (editingRevision !== revision) throw new Error('The board changed while you were editing. Cancel this edit and open the current card.');
      const current = next.cards.find(card => card.id === id);
      if (!current) throw new Error('This card is no longer on the board. Cancel this edit to continue.');
      current.title = byId('card-title').value.trim(); current.details = byId('card-details').value;
      current.priority = byId('card-priority').value;
    });
    if (saved) resetComposer('edit-' + id);
    return;
  }
  const card = {id: freshId('card'), title: byId('card-title').value.trim(), details: byId('card-details').value,
    status: 'todo', priority: byId('card-priority').value};
  const saved = await mutate(next => next.cards.push(card), 'card-title');
  if (saved) resetComposer('card-title');
});
byId('cancel-edit').addEventListener('click', () => {
  if (busy) return;
  const id = editingId;
  resetComposer(state?.cards.some(card => card.id === id) ? 'edit-' + id : 'card-title');
  message('Edit cancelled. Your saved card is unchanged.');
});
byId('undo-remove').addEventListener('click', () => {
  if (busy || writeBlocked || !state || !undoRemoval) return;
  perform(async () => {
    const undo = undoRemoval;
    if (revision !== undo.revision) throw new Error('The board changed. Refresh to load the latest cards.');
    await save(structuredClone(undo.board), 'edit-' + undo.cardId);
    message('Card restored to its original position.');
  });
});
byId('refresh').addEventListener('click', () => perform(async () => {
  await refresh();
  message(editingId && editingRevision !== revision
    ? 'Latest board loaded. Your draft is kept; cancel the edit and open the current card before saving.'
    : 'Latest board loaded.');
}));
byId('export').addEventListener('click', () => {
  if (busy || !state) return;
  const blob = new Blob([JSON.stringify(state, null, 2) + '\n'], {type: 'application/json'});
  const url = URL.createObjectURL(blob); const link = make('a', '');
  link.href = url; link.download = 'muse-task-board.json'; document.body.append(link); link.click(); link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000); message('Board exported as JSON.');
});
byId('import').addEventListener('change', async event => {
  const file = event.target.files[0]; if (!file) return;
  await perform(async () => {
    if (file.size > 65536) throw new Error('Choose a board JSON file smaller than 64 KB.');
    const incoming = validateBoard(JSON.parse(await file.text()));
    const next = structuredClone(state); const existing = new Map(next.cards.map(card => [card.id, card]));
    for (const card of incoming.cards) {
      const previous = existing.get(card.id);
      if (previous && ['title', 'details', 'status', 'priority'].some(key => previous[key] !== card[key])) throw new Error('A card ID has different content. Export your board and give the imported card a new ID.');
      if (!previous) { next.cards.push(card); existing.set(card.id, card); }
    }
    await save(next); message('Imported cards saved. Existing cards kept.');
  });
  event.target.value = '';
});
byId('queue').addEventListener('click', () => perform(async () => {
  if (!state.cards.length) throw new Error('Add a card to plan first.');
  if (!adapter.enabled) await api('/api/config', {enabled: true, expected_revision: adapter.revision});
  if (!pendingPlan) pendingPlan = {request_id: freshId('plan'), prompt: JSON.stringify({schema: 'muse-board-plan/v1',
    task: 'Choose the next three concrete actions from this board.',
    cards: state.cards.map(({id, title, status, priority}) => ({id, title, status, priority}))})};
  await api('/api/request', pendingPlan); pendingPlan = null;
  await refresh(); message('Board plan queued. Its saved result will appear here.');
}));
byId('lock').addEventListener('click', () => {
  if (busy) return;
  for (const sorter of sorters) sorter.destroy(); sorters.length = 0;
  token = ''; state = null; revision = 0; adapter = null; pendingPlan = null;
  undoRemoval = null; writeBlocked = false; resetComposer(); renderUndo();
  for (const status of states) byId(status).replaceChildren();
  byId('requests').replaceChildren(); byId('card-title').value = ''; byId('card-details').value = '';
  byId('workspace').hidden = true; byId('unlock').hidden = false; byId('session-key').focus();
  message('Board closed. Your saved cards are ready for next time.');
});
