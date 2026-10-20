const cards = [...document.querySelectorAll('.blog-card')];
const filterButtons = [...document.querySelectorAll('[data-category]')];
const searchInput = document.querySelector('#blog-search');
const emptyMessage = document.querySelector('#blog-empty');
let activeCategory = 'all';

function filterArticles() {
  const query = searchInput.value.trim().toLowerCase();
  let visibleCount = 0;
  cards.forEach(card => {
    const categoryMatches = activeCategory === 'all' || card.dataset.category === activeCategory;
    const searchMatches = !query || card.dataset.search.includes(query) || card.textContent.toLowerCase().includes(query);
    const visible = categoryMatches && searchMatches;
    card.hidden = !visible;
    visibleCount += Number(visible);
  });
  emptyMessage.hidden = visibleCount > 0;
}

filterButtons.forEach(button => button.addEventListener('click', () => {
  activeCategory = button.dataset.category;
  filterButtons.forEach(item => {
    const selected = item === button;
    item.classList.toggle('selected', selected);
    item.setAttribute('aria-pressed', String(selected));
  });
  filterArticles();
}));
searchInput?.addEventListener('input', filterArticles);
