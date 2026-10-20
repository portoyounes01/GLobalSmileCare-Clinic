const articles = {
  'first-visit': {
    title: 'What to Expect During Your First Dental Visit',
    category: 'Children’s Dentistry',
    date: '18 Jul, 2023',
    image: 'assets/article-child-figma.png',
    alt: 'A child smiling during a comfortable dental visit',
    lead: 'A first dental visit gives your child a chance to meet the team, explore the room, and get comfortable at their own pace.',
    content: `<h2>Make the first visit feel familiar</h2><p>Before the appointment, talk about the visit in a calm, positive way. Let the clinic know about any worries or sensory needs so the team can help your child feel at ease.</p><h2>What happens at the appointment?</h2><p>The dentist will usually ask about your child’s health, check their teeth and gums, and explain what they see. The visit can be adapted to your child’s age and comfort.</p><p>Questions are welcome. Your dental team can suggest simple ways to make brushing and future visits easier at home.</p><h2>After the visit</h2><p>Keep brushing twice a day with an age-appropriate amount of fluoride toothpaste, and follow the schedule your dental team recommends for checkups.</p>`
  },
  'tooth-pain': {
    title: 'When to See a Dentist About Tooth Pain',
    category: 'Oral Health',
    date: '18 Jul, 2023',
    image: 'assets/article-toothache-figma.png',
    alt: 'Man holding his cheek with tooth pain',
    lead: 'Tooth discomfort can have different causes. Knowing when to contact a dentist can help you get the right advice.',
    content: `<h2>Notice how the pain changes</h2><p>Contact a dentist if pain persists, returns, or affects eating or sleeping. A prompt assessment can help identify what is causing it.</p><h2>When to seek urgent care</h2><p>Seek urgent dental advice for severe pain, facial swelling, fever, or an injury to a tooth. If you have difficulty breathing or swallowing, seek emergency medical care.</p><h2>What you can do while you wait</h2><p>Keep the area clean and follow advice from a dental professional. Avoid placing aspirin or other medication directly on the tooth or gums.</p>`
  },
  'braces-care': {
    title: 'What to Know Before Getting Braces',
    category: 'Treatments',
    date: '18 Jul, 2023',
    image: 'assets/article-braces-figma.png',
    alt: 'Dental model showing braces and orthodontic wires',
    lead: 'Braces can help align your smile. Learn what to expect and how to care for your teeth throughout treatment.',
    content: `<h2>Understand your treatment plan</h2><p>Your orthodontist will explain your treatment plan, how to care for your braces, and what to expect at adjustment visits.</p><h2>Care for your teeth and braces</h2><p>Brush carefully around brackets and wires, and use the cleaning tools recommended by your dental team to reach between them.</p><h2>Keep up daily care at home</h2><p>Brush twice a day with fluoride toothpaste, clean between your teeth, and ask your dental team if you need advice choosing products or improving your routine.</p>`
  }
};

const params = new URLSearchParams(window.location.search);
const article = articles[params.get('article')] || articles['first-visit'];
document.title = `${article.title} — Smile Dental Care`;
document.querySelector('#article-title').textContent = article.title;
document.querySelector('#article-breadcrumb-title').textContent = article.title;
document.querySelector('#article-category').textContent = article.category;
document.querySelector('#article-date').textContent = article.date;
document.querySelector('#article-lead').textContent = article.lead;
const image = document.querySelector('#article-image');
image.src = article.image;
image.alt = article.alt;
document.querySelector('#article-content').innerHTML = article.content;
