/* Keep the first page useful while loading the complete searchable catalog. */
(() => {
  'use strict';
  const search = document.getElementById('download-search');
  const kind = document.getElementById('download-kind');
  const role = document.getElementById('download-role');
  const category = document.getElementById('download-category');
  const count = document.getElementById('download-count');
  const empty = document.getElementById('download-empty');
  const reset = document.getElementById('download-reset');
  const clearEmpty = document.getElementById('download-clear-empty');
  const results = document.getElementById('download-results');
  const pager = document.getElementById('download-pages');
  const previous = document.getElementById('download-previous');
  const next = document.getElementById('download-next');
  const pageLabel = document.getElementById('download-page-label');
  const sections = [...document.querySelectorAll('.download-section')];
  if (!search || !kind || !role || !category || !count || !empty || !reset || !clearEmpty || !results || !sections.length) return;
  const filters = { type: kind, role, subject: category };
  const allowed = Object.fromEntries(Object.entries(filters).map(([name, control]) =>
    [name, new Set([...control.options].map(option => option.value))]));
  const controls = [search, kind, role, category, reset, clearEmpty];
  const pageSize = 60;
  const repository = 'https://github.com/Atlas-Agents-Hub/muse-ai-agent-presets';
  const expectedTotal = Number(results.dataset.total);
  const initialCount = document.querySelectorAll('.download-card').length;
  const groupKinds = {specialists:'specialist',skills:'skill',workflows:'workflow','tool-guides':'tool-guide'};
  let page = 1;
  let indexed = [];

  function verifyCatalog(data) {
    if (data?.schema !== 'muse-hub/downloads/v1' || data.version !== results.dataset.version ||
        !Array.isArray(data.items) || data.items.length !== expectedTotal ||
        !Number.isInteger(expectedTotal) || expectedTotal < 1 || expectedTotal > 60000) throw Error('Invalid download catalog');
    const releaseBase = repository + '/releases/download/' + data.version + '/';
    const identities = new Set();
    for (const row of data.items) {
      if (!row || !['id','title','description','category','asset','url'].every(key => typeof row[key] === 'string') ||
          !allowed.type.has(row.kind) || row.kind === 'all' || !allowed.subject.has(row.category) || row.category === 'all' ||
          !Array.isArray(row.roles) || !row.roles.every(value => value !== 'all' && allowed.role.has(value)) ||
          !/^[a-z0-9][a-z0-9._-]*\.zip$/.test(row.asset) || row.url !== releaseBase + row.asset ||
          (row.guide_url !== undefined && (typeof row.guide_url !== 'string' || !row.guide_url.startsWith(repository + '/blob/main/'))) ||
          (row.pack_kind === 'skill-pack' && (typeof row.entry !== 'string' || !Number.isInteger(row.pack_size) || row.pack_size < 1))) throw Error('Invalid download entry');
      const identity = row.kind + ':' + row.id;
      if (identities.has(identity)) throw Error('Duplicate download entry');
      identities.add(identity);
    }
    return data.items;
  }

  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function cardFor(row) {
    const card = element('article', 'download-card');
    card.dataset.id = row.id;
    card.dataset.kind = row.kind;
    card.dataset.category = row.category;
    card.dataset.roles = row.roles.join(' ');
    card.dataset.search = [row.title, row.description, row.id, row.category, row.keywords || ''].join(' ');
    const description = row.description.length > 320 ? row.description.slice(0, 317).replace(/ [^ ]*$/, '') + '…' : row.description;
    card.append(element('span', 'download-kind', row.category), element('h3', '', row.title), element('p', '', description));
    if (row.guide_url) {
      const guide = element('a', 'guide-link', 'Read guide →');
      guide.href = row.guide_url;
      card.append(guide);
    }
    const packed = row.pack_kind === 'skill-pack';
    if (packed) {
      const hint = element('p', 'download-entry');
      hint.append('Open ', element('code', '', row.entry), ' in this pack.');
      card.append(hint);
    }
    const download = element('a', '', packed ? `Download skill pack · ${row.pack_size} skills ` : 'Download ZIP ');
    download.href = row.url;
    download.setAttribute('aria-label', 'Download ' + row.title + (packed ? ' skill pack' : ' ZIP'));
    const arrow = element('span', '', '↓');
    arrow.setAttribute('aria-hidden', 'true');
    download.append(arrow);
    card.append(download);
    return card;
  }
  function readUrl() {
    const params = new URLSearchParams(location.search.length <= 2048 ? location.search : '');
    for (const [name, control] of Object.entries(filters)) {
      const values = params.getAll(name);
      control.value = values.length === 1 && allowed[name].has(values[0]) ? values[0] : 'all';
    }
    if (!params.has('type')) kind.value = groupKinds[location.hash.slice(1)] || 'all';
    const terms = params.getAll('q');
    search.value = terms.length === 1 && terms[0].length <= 200 ? terms[0] : '';
    const pages = params.getAll('page');
    page = pages.length === 1 && /^[1-9][0-9]{0,3}$/.test(pages[0]) ? Number(pages[0]) : 1;
  }
  function update(writeUrl = false) {
    if (!indexed.length) return;
    const terms = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    const matches = indexed.filter(item =>
      (kind.value === 'all' || kind.value === item.row.kind) &&
      (role.value === 'all' || item.row.roles.includes(role.value)) &&
      (category.value === 'all' || category.value === item.row.category) &&
      terms.every(term => item.text.includes(term)));
    const pageCount = Math.max(1, Math.ceil(matches.length / pageSize));
    page = Math.max(1, Math.min(page, pageCount));
    const shown = matches.slice((page - 1) * pageSize, page * pageSize);
    for (const section of sections) {
      const group = shown.filter(item => item.row.kind === section.dataset.kind);
      section.querySelector('.download-grid').replaceChildren(...group.map(item => cardFor(item.row)));
      section.hidden = group.length === 0;
    }
    const first = matches.length ? (page - 1) * pageSize + 1 : 0;
    count.textContent = `Showing ${first}–${Math.min(page * pageSize, matches.length)} of ${matches.length} matching downloads`;
    empty.hidden = matches.length !== 0;
    if (pager && previous && next && pageLabel) {
      pager.hidden = pageCount <= 1;
      previous.disabled = page <= 1;
      next.disabled = page >= pageCount;
      pageLabel.textContent = `Page ${page} of ${pageCount}`;
    }
    if (writeUrl) {
      const url = new URL(location.href);
      if (url.search.length > 2048) url.search = '';
      for (const [name, control] of Object.entries(filters)) {
        url.searchParams.delete(name);
        if (control.value !== 'all') url.searchParams.set(name, control.value);
      }
      url.searchParams.delete('q');
      if (search.value.trim()) url.searchParams.set('q', search.value.trim().slice(0, 200));
      url.searchParams.delete('page');
      if (page > 1) url.searchParams.set('page', String(page));
      if (groupKinds[url.hash.slice(1)] && groupKinds[url.hash.slice(1)] !== kind.value) url.hash = '';
      if (url.href !== location.href) history.replaceState(null, '', url.href);
    }
  }
  function clear() {
    search.value = '';
    kind.value = 'all';
    role.value = 'all';
    category.value = 'all';
    page = 1;
    update(true);
    search.focus();
  }
  search.maxLength = 200;
  search.addEventListener('input', () => { page = 1; update(true); });
  for (const control of Object.values(filters)) control.addEventListener('change', () => { page = 1; update(true); });
  window.addEventListener('popstate', () => { if (indexed.length) { readUrl(); update(); } });
  reset.addEventListener('click', clear);
  clearEmpty.addEventListener('click', clear);
  if (previous && next) {
    function turn(delta) {
      page += delta;
      update(true);
      count.scrollIntoView({ block: 'center', behavior: 'auto' });
    }
    previous.addEventListener('click', () => turn(-1));
    next.addEventListener('click', () => turn(1));
  }
  for (const link of document.querySelectorAll('.download-jumps a')) {
    if (!groupKinds[link.hash.slice(1)]) continue;
    link.addEventListener('click', () => {
      if (!indexed.length) return;
      search.value = '';
      kind.value = groupKinds[link.hash.slice(1)];
      role.value = 'all';
      category.value = 'all';
      page = 1;
      update(true);
    });
  }

  controls.forEach(control => { control.disabled = true; });
  results.setAttribute('aria-busy', 'true');
  count.textContent = 'Loading the full download library…';
  fetch('downloads.json', { credentials: 'omit', redirect: 'error' })
    .then(response => { if (!response.ok) throw Error('Download catalog unavailable'); return response.json(); })
    .then(verifyCatalog)
    .then(items => {
      indexed = items.map(row => ({row, text: [row.title, row.description, row.id, row.category, row.keywords || ''].join(' ').toLocaleLowerCase()}));
      readUrl();
      update();
      controls.forEach(control => { control.disabled = false; });
      results.removeAttribute('aria-busy');
      results.dataset.catalogSize = String(indexed.length);
      document.body.classList.add('downloads-ready');
      if (groupKinds[location.hash.slice(1)]) document.getElementById(location.hash.slice(1)).scrollIntoView({ block: 'start', behavior: 'auto' });
    })
    .catch(() => {
      results.removeAttribute('aria-busy');
      count.textContent = `Showing 1–${initialCount} of ${expectedTotal} downloads. Browse every download by subject.`;
      const subjects = document.querySelector('.catalog-subjects');
      if (subjects) subjects.open = true;
      document.body.classList.add('downloads-fallback');
    });
})();
