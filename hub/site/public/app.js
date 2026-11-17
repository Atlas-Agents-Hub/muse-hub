/* Muse Hub directory. Local catalog only; no network, analytics, storage or account access. */
(() => {
  'use strict';
  const byId = id => document.getElementById(id);
  const raw = byId('catalog-data');
  const status = byId('count');
  if (!raw || !status) return;
  let data;
  try { data = JSON.parse(raw.textContent); }
  catch { status.textContent = 'This directory could not load. Try opening a fresh copy.'; return; }
  if (data.schema !== 'muse-hub-h02/public-discovery/v1' || data.count !== 63 ||
      data.native_muse_connected !== false || data.publication !== 'OFFLINE_PREVIEW_NOT_PUBLISHED' ||
      !Array.isArray(data.items) || data.items.length !== 63 || !Array.isArray(data.routes)) {
    status.textContent = 'Catalog verification failed. No sources are shown.';
    return;
  }
  // Validate every field used by rendering before constructing any UI.
  // A malformed offline copy must explain the failure, not throw on a null row.
  const isText = value => typeof value === 'string' && value.trim().length > 0;
  const itemFields = ['id', 'name', 'summary', 'category', 'platform',
                      'install_method', 'evidence', 'license_class', 'url'];
  const malformedItem = item => !item || typeof item !== 'object' ||
    Array.isArray(item) || itemFields.some(key => !isText(item[key]));
  const malformedRoute = route => !route || typeof route !== 'object' ||
    Array.isArray(route) || !isText(route.id) || !isText(route.title) ||
    !isText(route.notice) || !Array.isArray(route.source_ids) ||
    route.source_ids.some(id => !isText(id));
  if (data.items.some(malformedItem) || data.routes.some(malformedRoute)) {
    status.textContent = 'Catalog source restriction failed. No sources are shown.';
    return;
  }
  const allowed = new Set(data.items.map(item => item.id));
  const routeIds = new Set(data.routes.map(route => route.id));
  if (allowed.size !== 63 || routeIds.size !== data.routes.length ||
      data.routes.some(route => route.source_ids.some(id => !allowed.has(id)))) {
    status.textContent = 'Catalog source restriction failed. No sources are shown.';
    return;
  }

  const input = byId('search'), select = byId('category'), form = byId('filters');
  const results = byId('results'), empty = byId('empty'), chip = byId('active-chip');
  const notice = byId('route-notice'), buttons = Array.from(document.querySelectorAll('[data-route]'));
  const detail = byId('detail-panel'), detailBody = byId('detail-content');
  const detailClose = byId('detail-close'), backdrop = byId('detail-backdrop');
  const routes = new Map(data.routes.map(route => [route.id, route]));
  const queryState = { search: '', category: '', route: null };
  let selectedId = data.items[0].id;
  let returnFocus = null;

  const categories = [...new Set(data.items.map(x => x.category))].sort((a,b) => a.localeCompare(b));
  categories.forEach(name => {
    const option = document.createElement('option'); option.value = name; option.textContent = name;
    select.append(option);
  });
  const elt = (tag, klass, value) => {
    const node = document.createElement(tag);
    if (klass) node.className = klass;
    if (value !== undefined) node.textContent = value;
    return node;
  };
  const safeUrl = value => {
    try {
      const url = new URL(value);
      return url.protocol === 'https:' && Boolean(url.hostname) &&
        !url.username && !url.password && !url.port;
    } catch { return false; }
  };
  const sourceLink = (item, classname, label) => {
    if (!safeUrl(item.url)) return null;
    const link = elt('a', classname);
    link.href = item.url;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    link.append(elt('span', '', label), elt('span', '', '↗'));
    return link;
  };
  const makeMeta = (key, value, container) => {
    const row = elt('div');
    row.append(elt('dt', '', key), elt('dd', '', value));
    container.append(row);
  };
  const isMobileSheet = () => window.matchMedia('(max-width: 960px)').matches;
  const closeDetail = (restoreFocus = true) => {
    detail.classList.remove('is-open');
    detail.removeAttribute('role');
    detail.removeAttribute('aria-modal');
    backdrop.hidden = true;
    document.body.classList.remove('detail-visible');
    if (restoreFocus && returnFocus && returnFocus.isConnected) returnFocus.focus();
    returnFocus = null;
  };
  const markSelection = () => {
    results.querySelectorAll('.resource-card').forEach(card => {
      const active = card.dataset.id === selectedId;
      card.classList.toggle('is-selected', active);
      const trigger = card.querySelector('[data-details]');
      if (trigger) trigger.setAttribute('aria-pressed', String(active));
    });
  };
  const showDetails = (item, trigger = null) => {
    selectedId = item.id;
    detailBody.replaceChildren();
    const category = elt('div', 'detail-category', item.category + ' / ' + item.id);
    const heading = elt('h3', '', item.name);
    heading.id = 'detail-heading';
    const summary = elt('p', 'detail-summary', item.summary);
    const metadata = elt('dl', 'detail-metadata');
    makeMeta('Platform', item.platform, metadata);
    makeMeta('Getting started', item.install_method, metadata);
    makeMeta('Checked', item.evidence, metadata);
    makeMeta('Rights', item.license_class.replaceAll('_', ' ').toLowerCase() + ' — confirm with publisher', metadata);
    const note = elt('p', 'detail-note', 'This link has not been tested as a Muse Hub integration. Check the original project’s setup and license before using it.');
    detailBody.append(category, heading, summary, metadata, note);
    const link = sourceLink(item, 'detail-source', 'Open original source');
    if (link) detailBody.append(link);
    detailBody.append(elt('small', 'detail-disclaimer', 'The original publisher owns its source and instructions.'));
    markSelection();
    if (trigger && isMobileSheet()) {
      returnFocus = trigger;
      detail.classList.add('is-open');
      detail.setAttribute('role', 'dialog');
      detail.setAttribute('aria-modal', 'true');
      backdrop.hidden = false;
      document.body.classList.add('detail-visible');
      detail.focus();
    }
  };
  const card = item => {
    const article = elt('article', 'resource-card');
    article.dataset.id = item.id;
    const top = elt('div', 'resource-card-top');
    top.append(elt('span', 'category-badge', item.category), elt('span', 'record-id', item.id));
    article.append(top, elt('h3', '', item.name), elt('p', 'resource-summary', item.summary));
    const actions = elt('div', 'card-actions');
    const detailsButton = elt('button', 'details-button', 'Details');
    detailsButton.type = 'button'; detailsButton.dataset.details = item.id;
    detailsButton.setAttribute('aria-label', 'Show details for ' + item.name);
    detailsButton.setAttribute('aria-pressed', String(item.id === selectedId));
    detailsButton.addEventListener('click', () => showDetails(item, detailsButton));
    actions.append(detailsButton);
    const link = sourceLink(item, 'record-link', 'View source');
    if (link) actions.append(link);
    article.append(actions);
    return article;
  };
  const matches = item => {
    const q = queryState.search.toLocaleLowerCase().trim();
    const haystack = [item.name, item.summary, item.category, item.platform, item.install_method,
      item.evidence, item.id].join(' ').toLocaleLowerCase();
    const route = queryState.route ? routes.get(queryState.route) : null;
    return (!q || haystack.includes(q)) && (!queryState.category || queryState.category === item.category) &&
      (!route || route.source_ids.includes(item.id));
  };
  const render = () => {
    closeDetail(false);
    const items = data.items.filter(matches);
    if (items.length && !items.some(item => item.id === selectedId)) selectedId = items[0].id;
    results.replaceChildren(...items.map(card));
    status.textContent = `Showing ${items.length} of ${data.count} sources`;
    empty.hidden = items.length !== 0;
    const route = queryState.route ? routes.get(queryState.route) : null;
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.route === queryState.route)));
    chip.hidden = !route;
    chip.textContent = route ? route.title : '';
    notice.hidden = !route;
    if (route) notice.replaceChildren(elt('strong', '', 'About this route'), elt('span', '', route.notice));
    else notice.replaceChildren();
    if (items.length) showDetails(items.find(item => item.id === selectedId) || items[0]);
    else detailBody.replaceChildren(elt('h3', '', 'No resource selected'), elt('p', '', 'Try another search to see tools and guides.'));
  };
  const clear = () => {
    queryState.search = ''; queryState.category = ''; queryState.route = null;
    input.value = ''; select.value = '';
    selectedId = data.items[0].id;
    render();
  };
  buttons.forEach(button => button.addEventListener('click', () => {
    const id = button.dataset.route;
    if (!routes.has(id)) return;
    queryState.route = queryState.route === id ? null : id;
    render();
    byId('browse-results').scrollIntoView({block: 'start', behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
  }));
  input.addEventListener('input', () => { queryState.search = input.value; render(); });
  select.addEventListener('change', () => { queryState.category = select.value; render(); });
  form.addEventListener('reset', event => { event.preventDefault(); clear(); });
  byId('clear-empty').addEventListener('click', () => { clear(); input.focus(); });
  detailClose.addEventListener('click', () => closeDetail());
  backdrop.addEventListener('click', () => closeDetail());
  document.addEventListener('keydown', event => {
    if (event.key === 'Tab' && detail.classList.contains('is-open') && isMobileSheet()) {
      const focusable = Array.from(detail.querySelectorAll('button:not([disabled]), a[href]'));
      const first = focusable[0], last = focusable[focusable.length - 1];
      if (first && last) {
        if (event.shiftKey && (document.activeElement === first || document.activeElement === detail)) {
          event.preventDefault(); last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault(); first.focus();
        } else if (!event.shiftKey && document.activeElement === detail) {
          event.preventDefault(); first.focus();
        }
      }
      return;
    }
    if (event.key === 'Escape' && detail.classList.contains('is-open')) {
      event.preventDefault(); closeDetail(); return;
    }
    if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey &&
        !['INPUT','TEXTAREA','SELECT'].includes(document.activeElement?.tagName)) {
      event.preventDefault(); input.focus();
    }
  });
  window.addEventListener('resize', () => { if (!isMobileSheet()) closeDetail(false); });
  render();
})();
