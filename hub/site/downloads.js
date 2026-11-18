/* Progressive enhancement: every download remains an ordinary link. */
(() => {
  'use strict';
  const search = document.getElementById('download-search');
  const kind = document.getElementById('download-kind');
  const count = document.getElementById('download-count');
  const empty = document.getElementById('download-empty');
  const reset = document.getElementById('download-reset');
  const clearEmpty = document.getElementById('download-clear-empty');
  const cards = [...document.querySelectorAll('.download-card')];
  const sections = [...document.querySelectorAll('.download-section')];
  if (!search || !kind || !count || !empty || !reset || !clearEmpty || !cards.length) return;
  function update() {
    const term = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    for (const card of cards) {
      const match = (kind.value === 'all' || kind.value === card.dataset.kind) &&
        (!term || card.dataset.search.toLocaleLowerCase().includes(term));
      card.hidden = !match;
      if (match) visible += 1;
    }
    for (const section of sections) {
      section.hidden = ![...section.querySelectorAll('.download-card')].some(card => !card.hidden);
    }
    count.textContent = `Showing ${visible} of ${cards.length} downloads`;
    empty.hidden = visible !== 0;
  }
  function clear() {
    search.value = '';
    kind.value = 'all';
    update();
    search.focus();
  }
  search.addEventListener('input', update);
  kind.addEventListener('change', update);
  reset.addEventListener('click', clear);
  clearEmpty.addEventListener('click', clear);
  for (const link of document.querySelectorAll('.download-jumps a')) {
    link.addEventListener('click', () => {
      search.value = '';
      kind.value = 'all';
      update();
    });
  }
  update();
})();
