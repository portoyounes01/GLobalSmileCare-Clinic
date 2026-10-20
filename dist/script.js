const menuButton = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');
menuButton?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('open');
  menuButton?.setAttribute('aria-expanded', 'false');
  menuButton?.setAttribute('aria-label', 'Open menu');
}));

const services = {
  cleaning: ['Cleaning & Checkups', 'Preventive care that protects your oral health and keeps your smile feeling good.', 'service-details.html', 'Learn More'],
  whitening: ['Teeth Whitening', 'Gentle whitening options to help brighten your smile with care tailored to you.', 'index.html#appointment', 'Ask About Whitening'],
  implants: ['Dental Implants', 'Personalized implant care to restore comfort, function, and confidence.', 'index.html#appointment', 'Ask About Implants'],
  braces: ['Braces & Aligners', 'Straightening options designed around your smile and daily life.', 'index.html#appointment', 'Ask About Aligners']
};
document.querySelectorAll('[data-service]').forEach(tab => tab.addEventListener('click', () => {
  document.querySelectorAll('[data-service]').forEach(item => item.setAttribute('aria-selected', String(item === tab)));
  const [title, description, destination, actionLabel] = services[tab.dataset.service];
  const serviceTitle = document.querySelector('#service-title');
  const serviceDescription = document.querySelector('#service-description');
  if (serviceTitle) serviceTitle.textContent = title;
  if (serviceDescription) serviceDescription.textContent = description;
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

document.querySelector('#appointment')?.addEventListener('submit', event => {
  event.preventDefault();
  const form = event.currentTarget;
  if (!form.reportValidity()) return;
  form.querySelector('.form-message').textContent = 'Online booking is not connected yet. Please call +21 283 588982 to request an appointment.';
});
document.querySelector('#newsletter-form')?.addEventListener('submit', event => {
  event.preventDefault();
  const form = event.currentTarget;
  if (!form.reportValidity()) return;
  form.querySelector('.newsletter-message').textContent = 'Newsletter signup is not connected yet.';
});
