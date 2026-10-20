const BOOKING_URL = 'https://agenda.clickdocdentist.be/short/2B4OaRgY5BLx6ZVG';
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
