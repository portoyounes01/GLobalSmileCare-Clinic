const BOOKING_URL = 'https://agenda.clickdocdentist.be/short/2B4OaRgY5BLx6ZVG';

// Keep motion progressive: content remains visible if the script or observer is unavailable.
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReducedMotion && 'IntersectionObserver' in window) {
  const motionTargets = document.querySelectorAll([
    '.hero-copy', '.hero-visual', '.value-card', '.service-feature', '.doctor-card',
    '.doctor-feature', '.clinic-about-card', '.clinic-value-card', '.clinic-service-card',
    '.review-grid article', '.appointment-card', '.question-box',
    '.contact-item', '.modern-card', '.about-value', '.blog-card', '.blog-card-feature',
    '.article-list article', '.article-detail', '.related-articles', '.service-detail-intro',
    '.visit-steps article', '.detail-overview-image', '.detail-final-cta'
  ].join(','));

  if (motionTargets.length) {
    document.documentElement.classList.add('motion-ready');
    const revealObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -36px 0px' });

    motionTargets.forEach((element, index) => {
      element.classList.add('reveal-item');
      if (element.matches('.value-card, .doctor-card, .clinic-about-card, .clinic-value-card, .clinic-service-card, .review-grid article, .contact-item, .blog-card, .article-list article, .service-feature, .appointment-card')) {
        element.classList.add('motion-card');
      }
      element.style.setProperty('--reveal-delay', `${Math.min(index % 4, 3) * 65}ms`);
      revealObserver.observe(element);
    });
  }
}

// Users can explicitly preview the hero animation, including when system motion is reduced.
const replayMotion = document.createElement('button');
replayMotion.type = 'button';
replayMotion.className = 'motion-replay';
replayMotion.textContent = 'Animatie afspelen ↻';
replayMotion.setAttribute('aria-label', 'Animatie afspelen');
replayMotion.addEventListener('click', () => {
  document.documentElement.classList.remove('motion-preview');
  void document.documentElement.offsetWidth;
  document.documentElement.classList.add('motion-preview');
  document.querySelectorAll('.reveal-item').forEach(element => element.classList.remove('is-visible'));
  requestAnimationFrame(() => {
    document.querySelectorAll('.reveal-item').forEach(element => {
      if (element.getBoundingClientRect().top < window.innerHeight) element.classList.add('is-visible');
    });
  });
});
document.body.append(replayMotion);
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
