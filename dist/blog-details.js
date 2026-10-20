const articles = {
  'first-visit': {
    title: 'Wat gebeurt er tijdens een eerste tandartsbezoek?',
    category: 'Eerste afspraak',
    date: 'Praktische informatie',
    image: 'assets/article-child-figma.webp',
    alt: 'Kind tijdens een tandartsbezoek',
    lead: 'Tijdens uw eerste bezoek bespreekt de tandarts uw vraag en bekijkt uw tanden en tandvlees.',
    content: `<h2>Uw eerste afspraak</h2><p>Vertel de tandarts waar u last van heeft en welke vragen u heeft. Zo kunnen we de controle afstemmen op uw situatie.</p><h2>De controle</h2><p>De tandarts bekijkt uw tanden en tandvlees op gaatjes, aften of tandvleesproblemen en bespreekt de bevindingen met u.</p><h2>Wat gebeurt er daarna?</h2><p>We leggen uit welke zorg eventueel nodig is en bespreken samen de volgende stap. Als een gaatje kan worden gevuld, doen we dat wanneer dit mogelijk is.</p>`
  },
  'tooth-pain': {
    title: 'Wanneer gaat u met tandpijn naar de tandarts?',
    category: 'Mondgezondheid',
    date: 'Praktische informatie',
    image: 'assets/article-toothache-figma.webp',
    alt: 'Man met tandpijn',
    lead: 'Blijft tandpijn aanhouden of keert die terug? Neem contact op met een tandarts voor advies.',
    content: `<h2>Let op aanhoudende klachten</h2><p>Tandpijn kan verschillende oorzaken hebben. Neem contact op met een tandarts wanneer de pijn aanhoudt, terugkomt of eten en slapen moeilijk maakt.</p><h2>Wanneer is snelle hulp belangrijk?</h2><p>Bij hevige pijn, zwelling, koorts of tandletsel is snelle beoordeling belangrijk. Neem bij ademhalings- of slikproblemen onmiddellijk contact op met de spoeddiensten.</p><h2>Bespreek uw klachten</h2><p>De tandarts kan uw tanden en tandvlees onderzoeken en uitleggen welke vervolgstappen passend zijn.</p>`
  },
  'braces-care': {
    title: 'Wat u kunt doen bij tandvleesproblemen',
    category: 'Mondgezondheid',
    date: 'Praktische informatie',
    image: 'assets/article-braces-figma.webp',
    alt: 'Illustratie over tandheelkundige zorg',
    lead: 'Bloedend of terugtrekkend tandvlees komt vaak voor. De tandarts kan de oorzaak onderzoeken en advies geven.',
    content: `<h2>Bespreek tandvleesklachten</h2><p>De tandarts bekijkt uw tandvlees en bespreekt mogelijke oorzaken en passende verzorging.</p><h2>Verzorg uw mond dagelijks</h2><p>Poets uw tanden zorgvuldig en volg het advies van uw tandarts over dagelijkse mondverzorging.</p><h2>Maak een afspraak</h2><p>Blijven uw klachten aanhouden? Neem contact op met de praktijk om uw klachten te bespreken.</p>`
  }
};

const params = new URLSearchParams(window.location.search);
const article = articles[params.get('article')] || articles['first-visit'];
document.title = `${article.title} — Global Smile Care`;
document.querySelector('#article-title').textContent = article.title;
document.querySelector('#article-breadcrumb-title').textContent = article.title;
document.querySelector('#article-category').textContent = article.category;
document.querySelector('#article-lead').textContent = article.lead;
const image = document.querySelector('#article-image');
image.src = article.image;
image.alt = article.alt;
document.querySelector('#article-content').innerHTML = article.content;
