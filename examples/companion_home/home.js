/* Muse Hub Companion Home — neutral rooms, deterministic motion, original game.
 * All source-only. No Muse API, room chat, network, task scheduler or permissions.
 * Only the original game's non-personal score/turn/seed may use localStorage.
 */
(() => {
  'use strict';
  const config = window.MUSE_HOME_CONFIG;
  const roomNav = document.getElementById('room-nav');
  const panel = document.getElementById('room-panel');
  if (!config || config.schema !== 'muse-hub/neutral-companion-home/v1' ||
      config.native_muse_installed !== false || config.room_local_chat !== false ||
      config.global_assistant_external !== true || !Array.isArray(config.rooms) ||
      config.rooms.length !== 5) {
    document.body.dataset.configError = 'true';
    return;
  }
  const rooms = config.rooms;
  const ids = ['focus', 'notebook', 'garden', 'arcade', 'studio'];
  if (rooms.some((room, i) => room.id !== ids[i])) {
    document.body.dataset.configError = 'true';
    return;
  }
  const map = new Map(rooms.map(room => [room.id, room]));
  const count = document.getElementById('room-number');
  const kicker = document.getElementById('room-kicker');
  const title = document.getElementById('room-heading');
  const desc = document.getElementById('room-description');
  const feature = document.getElementById('room-feature');
  const controls = [];
  let selectedRoom = 'focus';

  function setRoom(id, options = {}) {
    if (!map.has(id)) return false;
    if (selectedRoom === 'studio' && id !== 'studio') pauseMotion('Left Studio');
    selectedRoom = id;
    const room = map.get(id);
    document.body.dataset.theme = room.theme;
    title.textContent = room.label;
    desc.textContent = room.description;
    kicker.textContent = room.kicker;
    feature.textContent = room.feature_ids.join(' / ').toUpperCase();
    count.textContent = String(ids.indexOf(id) + 1).padStart(2, '0') + ' / 05';
    for (const [index, button] of controls.entries()) {
      const current = rooms[index].id === id;
      button.setAttribute('aria-selected', String(current));
      button.tabIndex = current ? 0 : -1;
    }
    for (const content of document.querySelectorAll('[data-room-panel]')) {
      content.hidden = content.getAttribute('data-room-panel') !== id;
    }
    panel.setAttribute('aria-labelledby', 'tab-' + id);
    // Keep the selected tab inside the horizontal room strip without
    // moving the entire page or stealing keyboard focus.
    const activeTab = controls[ids.indexOf(id)];
    if (activeTab) {
      const tabRect = activeTab.getBoundingClientRect();
      const stripRect = roomNav.getBoundingClientRect();
      if (tabRect.left < stripRect.left) {
        roomNav.scrollLeft -= stripRect.left - tabRect.left + 6;
      } else if (tabRect.right > stripRect.right) {
        roomNav.scrollLeft += tabRect.right - stripRect.right + 6;
      }
    }
    if (!options.fromHash) {
      const url = new URL(window.location.href);
      url.hash = 'room=' + id;
      try {
        history.replaceState(null, '', url);
      } catch (_) {
        // Offline file previews may not allow rewriting browser history.
      }
    }
    return true;
  }

  rooms.forEach((room, index) => {
    const button = document.createElement('button');
    const number = document.createElement('span');
    const label = document.createElement('span');
    number.className = 'nav-number';
    number.textContent = String(index + 1).padStart(2, '0') + ' / 05';
    label.textContent = room.label;
    button.append(number, label);
    button.type = 'button';
    button.id = 'tab-' + room.id;
    button.setAttribute('role', 'tab');
    button.setAttribute('aria-controls', 'room-panel');
    button.addEventListener('click', () => setRoom(room.id));
    button.addEventListener('keydown', event => {
      const which = event.key;
      if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(which)) return;
      event.preventDefault();
      const next = which === 'Home' ? 0 : which === 'End' ? controls.length - 1 :
        (index + (which === 'ArrowRight' ? 1 : -1) + controls.length) % controls.length;
      controls[next].focus();
      setRoom(rooms[next].id);
    });
    roomNav.appendChild(button);
    controls.push(button);
  });

  function roomFromHash() {
    const fragment = window.location.hash.replace(/^#/, '');
    if (!fragment.startsWith('room=')) return 'focus';
    let value = '';
    try { value = decodeURIComponent(fragment.slice(5)); } catch (_) { return 'focus'; }
    return map.has(value) ? value : 'focus';
  }
  setRoom(roomFromHash(), {fromHash: true});
  window.addEventListener('hashchange', () => {
    setRoom(roomFromHash(), {fromHash: true});
  });
  for (const link of document.querySelectorAll('[data-room-target]')) {
    link.addEventListener('click', event => {
      const dest = link.getAttribute('data-room-target');
      if (!map.has(dest)) return;
      event.preventDefault();
      setRoom(dest);
      roomNav.querySelector('#tab-' + dest).focus();
      document.getElementById('rooms').scrollIntoView({
        behavior: (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) ? 'auto' : 'smooth',
      });
    });
  }

  // A local visual checklist: no provider task or reminder is created.
  const focus = document.getElementById('focus-check');
  const focusStatus = document.getElementById('focus-status');
  focus.addEventListener('click', () => {
    const active = focus.getAttribute('aria-pressed') !== 'true';
    focus.setAttribute('aria-pressed', String(active));
    focusStatus.textContent = active ?
      'One focus marked in this browser view; nothing was scheduled.' :
      'Focus cleared. No task or notification was sent.';
  });

  // H15: deterministic neutral poses, reduced-motion support, no media assets.
  const shape = document.getElementById('pose-shape');
  const motionButton = document.querySelector('[data-action="motion"]');
  const frameButton = document.querySelector('[data-action="next-pose"]');
  const motionStatus = document.getElementById('motion-status');
  const reduced = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : null;
  const poses = [
    {x: 0, y: 0, rot: 0, scale: 1},
    {x: 30, y: -12, rot: 9, scale: 1.03},
    {x: -24, y: 5, rot: -11, scale: .97},
    {x: 10, y: -19, rot: 5, scale: 1.02},
  ];
  let poseIndex = 0;
  let playing = false;
  let animationFrame = 0;
  let lastMotion = 0;
  function renderPose() {
    const pose = poses[poseIndex];
    shape.style.setProperty('--pose-x', pose.x + 'px');
    shape.style.setProperty('--pose-y', pose.y + 'px');
    shape.style.setProperty('--pose-rot', pose.rot + 'deg');
    shape.style.setProperty('--pose-scale', String(pose.scale));
    motionStatus.textContent = (playing ? 'Motion active' : 'Motion paused') +
      ' · Pose ' + (poseIndex + 1) + ' / ' + poses.length;
  }
  function nextPose() {
    poseIndex = (poseIndex + 1) % poses.length;
    renderPose();
  }
  function frame(timestamp) {
    if (!playing) return;
    if (lastMotion === 0 || timestamp - lastMotion >= 1200) {
      if (lastMotion !== 0) nextPose();
      lastMotion = timestamp;
    }
    animationFrame = requestAnimationFrame(frame);
  }
  function pauseMotion(reason) {
    playing = false;
    document.body.dataset.motion = 'paused';
    cancelAnimationFrame(animationFrame);
    animationFrame = 0;
    lastMotion = 0;
    motionButton.setAttribute('aria-pressed', 'false');
    motionButton.textContent = 'Resume motion ↗';
    renderPose();
    if (reason) motionStatus.textContent += ' · ' + reason;
  }
  function playMotion() {
    if ((reduced && reduced.matches) || document.hidden) {
      pauseMotion('Reduced motion or hidden tab');
      return;
    }
    playing = true;
    document.body.dataset.motion = 'playing';
    motionButton.setAttribute('aria-pressed', 'true');
    motionButton.textContent = 'Pause motion ↗';
    renderPose();
    animationFrame = requestAnimationFrame(frame);
  }
  motionButton.setAttribute('aria-pressed', 'false');
  motionButton.addEventListener('click', () => {
    if (playing) pauseMotion();
    else playMotion();
  });
  frameButton.addEventListener('click', () => nextPose());
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) pauseMotion('Hidden tab');
  });
  if (reduced) {
    const onReduced = () => { if (reduced.matches) pauseMotion('Reduced motion preference'); };
    if (typeof reduced.addEventListener === 'function') reduced.addEventListener('change', onReduced);
    else if (typeof reduced.addListener === 'function') reduced.addListener(onReduced);
  }
  renderPose();

  // H16: an original small browser game. localStorage keeps only numeric
  // progress for this game, never notes, identities, credentials or chat.
  const GAME_KEY = 'muse-hub/signal-trail/v1';
  const PADS = Array.from(document.querySelectorAll('[data-pad]'));
  const scoreLabel = document.getElementById('arcade-score');
  const turnLabel = document.getElementById('arcade-turn');
  const message = document.getElementById('arcade-message');
  message.setAttribute('aria-live', 'polite');
  let game = {seed: 1137, turn: 1, score: 0};
  function validGame(value) {
    return value && typeof value === 'object' &&
      Object.keys(value).sort().join(',') === 'score,seed,turn' &&
      Number.isSafeInteger(value.seed) && value.seed >= 0 && value.seed <= 0xffffffff &&
      Number.isSafeInteger(value.turn) && value.turn >= 1 && value.turn <= 1_000_000 &&
      Number.isSafeInteger(value.score) && value.score >= 0 && value.score < value.turn;
  }
  function readSaved() {
    try {
      const raw = localStorage.getItem(GAME_KEY);
      if (raw && raw.length <= 160) {
        const saved = JSON.parse(raw);
        if (validGame(saved)) game = saved;
      }
    } catch (_) {
      message.textContent = 'Local game save unavailable in this browser.';
    }
  }
  function save() {
    try { localStorage.setItem(GAME_KEY, JSON.stringify(game)); }
    catch (_) { message.textContent = 'Game score stays in this view only.'; }
  }
  function target() {
    // Pure deterministic function of saved seed; no external RNG/asset.
    const next = (Math.imul(game.seed, 1664525) + 1013904223) >>> 0;
    return next % 4;
  }
  function renderGame() {
    const wanted = target();
    for (const pad of PADS) {
      const active = Number(pad.dataset.pad) === wanted;
      pad.dataset.active = String(active);
      pad.setAttribute('aria-description', active ? 'Highlighted signal' : 'Unlit tile');
    }
    scoreLabel.textContent = String(game.score);
    turnLabel.textContent = String(game.turn);
  }
  function choosePad(index) {
    if (selectedRoom !== 'arcade' || !Number.isInteger(index) || index < 0 || index > 3) return;
    if (index !== target()) {
      message.textContent = 'Not this one. Try the highlighted tile.';
      return;
    }
    if (game.turn >= 1_000_000) {
      message.textContent = 'Session limit reached. Start a new game.';
      return;
    }
    game.seed = (Math.imul(game.seed, 1664525) + 1013904223) >>> 0;
    game.turn += 1;
    game.score += 1;
    message.textContent = 'Correct. Find the next signal.';
    save();
    renderGame();
  }
  for (const pad of PADS) {
    pad.addEventListener('click', () => choosePad(Number(pad.dataset.pad)));
  }
  document.getElementById('arcade-new').addEventListener('click', () => {
    game = {seed: 1137, turn: 1, score: 0};
    message.textContent = 'A new trail is ready.';
    save();
    renderGame();
  });
  document.getElementById('arcade-back').addEventListener('click', () => {
    setRoom('focus');
    roomNav.querySelector('#tab-focus').focus();
  });
  window.addEventListener('keydown', event => {
    if (selectedRoom !== 'arcade' || event.ctrlKey || event.metaKey || event.altKey) return;
    if (['1','2','3','4'].includes(event.key)) {
      event.preventDefault();
      choosePad(Number(event.key) - 1);
    } else if (event.key === 'Escape') {
      event.preventDefault();
      setRoom('focus');
      roomNav.querySelector('#tab-focus').focus();
    }
  });
  readSaved();
  renderGame();
})();
