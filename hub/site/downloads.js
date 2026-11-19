/* Progressive enhancement: every download remains an ordinary link. */
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
  const pager = document.getElementById('download-pages');
  const previous = document.getElementById('download-previous');
  const next = document.getElementById('download-next');
  const pageLabel = document.getElementById('download-page-label');
  const cards = [...document.querySelectorAll('.download-card')];
  const sections = [...document.querySelectorAll('.download-section')];
  if (!search || !kind || !role || !category || !count || !empty || !reset || !clearEmpty || !cards.length) return;
  const filters = { type: kind, role, subject: category };
  const allowed = Object.fromEntries(Object.entries(filters).map(([name, control]) =>
    [name, new Set([...control.options].map(option => option.value))]));
  const pageSize = 60;
  let page = 1;
  const indexed = cards.map(card => ({ card, text: card.dataset.search.toLocaleLowerCase(),
    roles: card.dataset.roles.split(' ') }));
  function readUrl() {
    const params = new URLSearchParams(location.search.length <= 2048 ? location.search : '');
    for (const [name, control] of Object.entries(filters)) {
      const values = params.getAll(name);
      control.value = values.length === 1 && allowed[name].has(values[0]) ? values[0] : 'all';
    }
    if (!params.has('type')) {
      kind.value = ({specialists:'specialist',skills:'skill',workflows:'workflow','tool-guides':'tool-guide'})[location.hash.slice(1)] || 'all';
    }
    const terms = params.getAll('q');
    search.value = terms.length === 1 && terms[0].length <= 200 ? terms[0] : '';
    const pages = params.getAll('page');
    page = pages.length === 1 && /^[1-9][0-9]{0,3}$/.test(pages[0]) ? Number(pages[0]) : 1;
  }
  function update(writeUrl = false) {
    const terms = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    const matches = indexed.filter(item =>
      (kind.value === 'all' || kind.value === item.card.dataset.kind) &&
      (role.value === 'all' || item.roles.includes(role.value)) &&
      (category.value === 'all' || category.value === item.card.dataset.category) &&
      terms.every(term => item.text.includes(term)));
    const pageCount = Math.max(1, Math.ceil(matches.length / pageSize));
    page = Math.min(page, pageCount);
    const shown = new Set(matches.slice((page - 1) * pageSize, page * pageSize).map(item => item.card));
    for (const card of cards) card.hidden = !shown.has(card);
    for (const section of sections) {
      section.hidden = ![...section.querySelectorAll('.download-card')].some(card => !card.hidden);
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
  window.addEventListener('popstate', () => { readUrl(); update(); });
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
    link.addEventListener('click', () => {
      search.value = '';
      kind.value = ({specialists:'specialist',skills:'skill',workflows:'workflow','tool-guides':'tool-guide'})[link.hash.slice(1)] || 'all';
      role.value = 'all';
      category.value = 'all';
      page = 1;
      update(true);
    });
  }
  readUrl();
  update();
})();
