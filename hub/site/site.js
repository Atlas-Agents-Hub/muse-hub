/* Muse Hub specialist discovery and setup. */
(() => {
  'use strict';
  const directory = document.querySelector('.specialist-directory');
  const directoryLabel = document.getElementById('role-directory-label');
  const searchPanel = document.querySelector('.specialist-search-panel');
  const setupDisclosure = document.querySelector('.setup-disclosure');
  const search = document.getElementById('role-search');
  const category = document.getElementById('role-category');
  const count = document.getElementById('role-count');
  const reset = document.getElementById('role-reset');
  const empty = document.getElementById('role-empty');
  const emptyClear = document.getElementById('role-empty-clear');
  const cards = [...document.querySelectorAll('.role-card[data-role]')];
  const quickPicks = [...document.querySelectorAll('[data-suggest-role]')];
  if (!search || !category || !count || !reset || !empty || !emptyClear || cards.length !== 15) return;
  let suggestedRole = '';

  function update() {
    const needle = search.value.trim().toLocaleLowerCase();
    const group = category.value;
    let visible = 0;
    for (const card of cards) {
      const hasTerm = suggestedRole
        ? card.dataset.role === suggestedRole
        : !needle || card.dataset.search.toLocaleLowerCase().includes(needle);
      const hasGroup = group === 'all' || card.dataset.category === group;
      const show = hasTerm && hasGroup;
      card.hidden = !show;
      if (show) visible += 1;
    }
    count.textContent = `Showing ${visible} of ${cards.length} specialists`;
    if (directoryLabel) {
      const filtered = !!needle || group !== 'all';
      directoryLabel.textContent = filtered
        ? 'View ' + visible + ' matching specialist' + (visible === 1 ? '' : 's')
        : 'Browse all ' + cards.length + ' specialists';
    }
    empty.hidden = visible !== 0;
    for (const button of quickPicks) {
      button.setAttribute('aria-pressed', String(suggestedRole === button.dataset.suggestRole));
    }
  }
  function clear() {
    suggestedRole = '';
    search.value = '';
    category.value = 'all';
    update();
    search.focus();
  }
  // Outcome shortcuts resolve only the 15 reviewed role cards. No arbitrary path input.
  for (const button of quickPicks) {
    button.addEventListener('click', () => {
      const target = cards.find(card => card.dataset.role === button.dataset.suggestRole);
      const heading = target?.querySelector('h3');
      if (!target || !heading) return;
      if (suggestedRole === target.dataset.role) {
        clear();
        return;
      }
      suggestedRole = target.dataset.role;
      search.value = heading.textContent.trim();
      category.value = 'all';
      if (directory) directory.open = true;
      update();
      target.tabIndex = -1;
      target.focus({ preventScroll: true });
      target.scrollIntoView({ block: 'center', behavior: 'auto' });
    });
  }
  search.addEventListener('focus', () => { if (directory) directory.open = true; });
  function applyManualFilters() {
    suggestedRole = '';
    if (directory) directory.open = true;
    update();
  }
  search.addEventListener('input', applyManualFilters);
  category.addEventListener('change', applyManualFilters);
  reset.addEventListener('click', clear);
  emptyClear.addEventListener('click', clear);
  if (window.location.hash === '#specialists' && directory) directory.open = true;
  for (const link of document.querySelectorAll('a[href="#specialists"], a[href="index.html#specialists"]')) {
    link.addEventListener('click', () => { if (directory) directory.open = true; });
  }
  document.addEventListener('keydown', event => {
    if (event.key === '/' && !event.metaKey && !event.ctrlKey && !event.altKey) {
      const active = document.activeElement;
      const typing = active && (active.tagName === 'INPUT' || active.tagName === 'TEXTAREA' || active.tagName === 'SELECT' || active.isContentEditable);
      if (!typing) { event.preventDefault(); if (directory) directory.open = true; search.focus(); }
    }
    if (event.key === 'Escape' && document.activeElement === search) {
      search.value = '';
      applyManualFilters();
    }
  });
  // Use only the role and asset identifiers present in the reviewed cards.
  const setupSelect = document.getElementById('setup-role-select');
  const setupResult = document.getElementById('setup-role-result');
  const setupEmpty = document.getElementById('setup-role-empty');
  const setupTitle = document.getElementById('setup-role-title');
  const setupDescription = document.getElementById('setup-role-description');
  const setupInstall = document.getElementById('setup-role-install');
  const setupProfile = document.getElementById('setup-role-profile');
  const setupDownload = document.getElementById('setup-role-download');
  const roleAssets = new Map(cards.map(card => [card.dataset.role, card.dataset.asset]));
  const roleDownloads = new Map(cards.map(card => [card.dataset.role, card.querySelector('.role-card-download')?.href]));
  const knownRoles = new Set(cards.map(card => card.dataset.role));
  const sourceBase = 'https://github.com/Atlas-Agents-Hub/muse-hub/blob/main/presets/';
  const setupReady = setupSelect && setupResult && setupEmpty && setupTitle &&
    setupDescription && setupInstall && setupProfile && setupDownload && knownRoles.size === 15;

  function selectSetupRole() {
    if (!setupReady) return;
    const slug = setupSelect.value;
    if (!knownRoles.has(slug) || !/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/.test(slug)) {
      setupResult.hidden = true;
      setupEmpty.hidden = false;
      return;
    }
    const asset = roleAssets.get(slug);
    if (!asset || !/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/.test(asset)) return;
    const option = setupSelect.selectedOptions[0];
    setupTitle.textContent = option.textContent;
    setupDescription.textContent = option.dataset.description || '';
    setupInstall.href = `${sourceBase}${slug}/INSTALL.md#set-up-or-update-in-muse`;
    setupProfile.href = `${sourceBase}${slug}/README.md`;
    const download = roleDownloads.get(slug);
    if (!download || !download.startsWith('https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/')) return;
    setupDownload.href = download;
    setupEmpty.hidden = true;
    setupResult.hidden = false;
  }
  if (setupReady) {
    // Only reviewed role identifiers may affect onboarding state.
    const incomingRole = new URL(window.location.href).searchParams.get('role');
    if (incomingRole && knownRoles.has(incomingRole)) {
      setupSelect.value = incomingRole;
      if (setupDisclosure) setupDisclosure.open = true;
    }
    if (window.location.hash === '#setup' && setupDisclosure) setupDisclosure.open = true;
    function syncRoleURL(slug) {
      const url = new URL(window.location.href);
      if (slug && knownRoles.has(slug)) {
        url.searchParams.set('role', slug);
        url.hash = '#setup';
      } else {
        url.searchParams.delete('role');
      }
      try {
        // file:// previews can disallow history updates.
        history.replaceState(null, '', url);
      } catch (_) {
        // Local selection still works when history is unavailable.
      }
    }
    setupSelect.addEventListener('change', () => {
      selectSetupRole();
      syncRoleURL(setupSelect.value);
    });
    for (const link of document.querySelectorAll('[data-select-role]')) {
      link.addEventListener('click', event => {
        const slug = link.dataset.selectRole;
        if (!knownRoles.has(slug)) return;
        event.preventDefault();
        setupSelect.value = slug;
        if (setupDisclosure) setupDisclosure.open = true;
        selectSetupRole();
        syncRoleURL(slug);
        const reduceMotion = window.matchMedia &&
          window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        // Keyboard and reduced-motion navigation should not animate across
        // the long specialist catalog. The document's CSS otherwise uses
        // smooth scrolling for ordinary anchor navigation.
        const immediate = reduceMotion || event.detail === 0;
        const rootStyle = document.documentElement.style;
        const originalBehavior = rootStyle.scrollBehavior;
        if (immediate) rootStyle.scrollBehavior = 'auto';
        try {
          setupTitle.scrollIntoView({behavior: immediate ? 'auto' : 'smooth', block: 'center'});
        } finally {
          if (immediate) rootStyle.scrollBehavior = originalBehavior;
        }
        setupTitle.focus({ preventScroll: true });
      });
    }
    selectSetupRole();
    // A specialist setup link should reveal its selected actions, not stop at
    // the general three-step introduction above them.
    if (incomingRole && knownRoles.has(incomingRole) && window.location.hash === '#setup') {
      const revealDeepLinkedRole = () => {
        if (setupSelect.value !== incomingRole || setupResult.hidden || window.location.hash !== '#setup') return;
        const selectorPanel = setupSelect.closest('.setup-selector');
        if (!selectorPanel) return;
        const rootStyle = document.documentElement.style;
        const previousScrollBehavior = rootStyle.scrollBehavior;
        rootStyle.scrollBehavior = 'auto';
        try {
          selectorPanel.scrollIntoView({ block: 'start', behavior: 'instant' });
        } finally {
          rootStyle.scrollBehavior = previousScrollBehavior;
        }
        setupTitle.focus({ preventScroll: true });
      };
      const onReady = () => requestAnimationFrame(revealDeepLinkedRole);
      if (document.readyState === 'complete') onReady();
      else window.addEventListener('load', onReady, { once: true });
    }
  }
  update();
  if (searchPanel) searchPanel.hidden = false;
})();
