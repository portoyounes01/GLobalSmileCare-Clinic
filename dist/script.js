const BOOKING_URL = 'https://agenda.clickdocdentist.be/short/2B4OaRgY5BLx6ZVG';

// Keep motion progressive: content remains visible if the script or observer is unavailable.
const motionTargetSelector = [
    '.section-heading', '.faq-grid > div', '.faq-list details',
    '.services > .eyebrow', '.services > h2', '.services > .section-lead', '.value-card', '.service-feature', '.doctor-card',
    '.doctor-feature', '.clinic-about-card', '.clinic-value-card', '.clinic-service-card',
    '.review-grid article', '.appointment-card', '.question-box',
    '.contact-item', '.modern-card', '.about-value', '.blog-card', '.blog-card-feature',
    '.article-list article', '.article-detail', '.related-articles', '.service-detail-intro',
    '.visit-steps article', '.detail-overview-image', '.detail-final-cta', '.cta', '.about-cta',
    '.blogs-cta', '.services-promo', '.service-detail-card', '.newsletter',
    '.about-story', '.story-copy', '.result-card', '.about-team', '.team-heading',
    '.doctor-profile', '.doctor-directory-grid', '.doctors-intro-copy', '.contact-copy',
    '.blog-grid', '.article-hero-image', '.article-sidebar', '.article-help',
    '.article-content p', '.article-content h2', '.article-content h3', '.article-content ul',
    '.article-content blockquote', '.detail-benefit-grid .value-card'
].join(',');

let scrollMotionEnabled = false;
let scrollMotionUpdate = null;
function enableScrollMotion() {
  if (scrollMotionEnabled) {
    scrollMotionUpdate?.();
    return;
  }
  const motionTargets = document.querySelectorAll(motionTargetSelector);
  if (!motionTargets.length) return;

  document.documentElement.classList.add('motion-ready');
  const revealOrderByGroup = new Map();
  motionTargets.forEach(element => {
    element.classList.add('reveal-item');
    const group = element.closest('section, article') || element.parentElement;
    const groupOrder = revealOrderByGroup.get(group) || 0;
    element.dataset.revealOrder = String(Math.min(groupOrder, 3));
    revealOrderByGroup.set(group, groupOrder + 1);
    if (element.matches('.value-card, .doctor-card, .clinic-about-card, .clinic-value-card, .clinic-service-card, .review-grid article, .contact-item, .blog-card, .article-list article, .service-feature, .appointment-card')) {
      element.classList.add('motion-card');
    }
  });

  let animationFrame = 0;
  const updateScrollReveals = () => {
    animationFrame = 0;
    const startLine = window.innerHeight * 0.92;
    const centerLine = window.innerHeight * 0.48;
    const revealDistance = startLine - centerLine;
    motionTargets.forEach(element => {
      const rect = element.getBoundingClientRect();
      const staggerPixels = Number(element.dataset.revealOrder || 0) * 48;
      const progress = Math.max(0, Math.min(1, (startLine - rect.top - staggerPixels) / revealDistance));
      element.style.opacity = String(progress);
      element.style.transform = `translateY(${(1 - progress) * 22}px)`;
    });
  };
  const schedule = () => {
    if (!animationFrame) animationFrame = requestAnimationFrame(updateScrollReveals);
  };
  scrollMotionEnabled = true;
  scrollMotionUpdate = schedule;
  window.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', schedule, { passive: true });
  updateScrollReveals();
}
enableScrollMotion();
const menuButton = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');
menuButton?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Menu sluiten' : 'Menu openen');
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('open');
  menuButton?.setAttribute('aria-expanded', 'false');
  menuButton?.setAttribute('aria-label', 'Menu openen');
}));

const services = {
  checkups: ['Controles en advies', 'Tijdens een controle bekijken we uw tanden en tandvlees en bespreken we wat nodig is.', 'service-details.html', 'Meer informatie'],
  whitening: ['Tanden bleken', 'Een pijnloze bleekbehandeling voor een zichtbaar wittere glimlach.', BOOKING_URL, 'Afspraak maken'],
  dentures: ['Tandprotheses', 'U kunt bij ons terecht voor een tandprothese of volledig kunstgebit.', BOOKING_URL, 'Afspraak maken'],
  fillings: ['Gaatjes vullen', 'Als we een gaatje vinden, vullen we dit wanneer dat mogelijk is.', BOOKING_URL, 'Afspraak maken']
};
const serviceIcons = {
  checkups: 'checkup',
  whitening: 'whitening',
  dentures: 'denture',
  fillings: 'filling'
};
document.querySelectorAll('[data-service]').forEach(tab => tab.addEventListener('click', () => {
  document.querySelectorAll('[data-service]').forEach(item => item.setAttribute('aria-selected', String(item === tab)));
  const service = services[tab.dataset.service];
  if (!service) return;
  const [title, description, destination, actionLabel] = service;
  const serviceTitle = document.querySelector('#service-title');
  const serviceDescription = document.querySelector('#service-description');
  if (serviceTitle) serviceTitle.textContent = title;
  if (serviceDescription) serviceDescription.textContent = description;
  const serviceIcon = document.querySelector('#service-icon');
  const iconName = serviceIcons[tab.dataset.service];
  if (serviceIcon && iconName) {
    serviceIcon.className = `icon blue icon-${iconName}`;
    serviceIcon.querySelector('use')?.setAttribute('href', `assets/icons.svg#icon-${iconName}`);
  }
  const serviceAction = document.querySelector('.service-card-actions .button');
  if (serviceAction) {
    serviceAction.href = destination;
    serviceAction.firstChild.textContent = actionLabel + ' ';
  }
}));

document.querySelectorAll('[data-slide]').forEach(button => button.addEventListener('click', () => {
  const grid = document.querySelector('#about-doctor-grid') || document.querySelector('#doctor-grid');
  if (!grid) return;
  grid.scrollBy({ left: Number(button.dataset.slide) * (grid.clientWidth * .55), behavior: 'smooth' });
}));
