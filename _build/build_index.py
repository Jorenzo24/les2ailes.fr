# -*- coding: utf-8 -*-
import common as c

REVIEWS = [
    ("nathalie craspail", "Laurence est une professionnelle hors pair, alliant bienveillance, rigueur et humour. Le tout dans un lieu magique et une très chaleureuse ambiance."),
    ("Nath Ledev", "Un lieu magique, des cours exceptionnels où Laurence, par ses qualités professionnelles, sa créativité et sa grande bienveillance, permet à chacun de découvrir et d'entretenir son corps. Un moment d'apaisement précieux."),
    ("Gerard Zenoni", "Incroyable d’avoir ce niveau de professionnalisme et d'équipements, à Mouguerre, France ! En deux ans, je suis progressivement passé d'un cours par semaine… à deux… puis trois… et je sens que le quatre n'est pas loin ! Et plus de maux de dos 👍"),
    ("Valérie Hellin", "Un studio exceptionnel avec une propriétaire ex danseuse professionnelle accompagnée de différents intervenants qui vous font travailler tt en longueur et en douceur dans un cadre idyllique"),
    ("Sandrine AGUERRE", "Un lieu magique où on prend soin de soi grâce à Laurence, une professeure à l'écoute de ses élèves, très bienveillante et qui nous permet de progresser, d'apprendre à mieux se connaitre grâce à ses cours très complets !! Une très belle découverte à tous points de vue me concernant !!"),
    ("Mathias rosandic", "Un lieu exceptionnel avec des cours géniaux. Bon pour le corps mais aussi avec de l'humour. La maîtresse des lieux donne envie que l'on revienne. Merci à Laurence pour ce qu'elle nous partage et enseigne."),
    ("Gaelle Llanos Vieillard", "Des cours exceptionnels avec une prof exceptionnelle (Laurence).Je recommande fortement aux adeptes de yoga et pilâtes."),
    ("Elise CUISSET", "Lieu magique, au cœur de la nature. Laurence est très professionnelle et bienveillante. Les cours sont variés et efficaces."),
    ("Karine Locatelli", "Les cours de yoga et de pilates de Laurence sont tout simplement magiques. Une professeure de qualité qui œuvre pour le bien être de ses élèves. Résultats assurés !!!"),
]

IC_GOOGLE = ('<svg viewBox="0 0 24 24" aria-hidden="true">'
 '<path fill="#4285F4" d="M23.5 12.27c0-.79-.07-1.54-.2-2.27H12v4.51h6.47a5.53 5.53 0 0 1-2.4 3.63v3h3.87c2.27-2.09 3.56-5.17 3.56-8.87Z"/>'
 '<path fill="#34A853" d="M12 24c3.24 0 5.96-1.08 7.94-2.91l-3.87-3c-1.08.72-2.45 1.16-4.07 1.16-3.13 0-5.78-2.11-6.73-4.96H1.29v3.09A12 12 0 0 0 12 24Z"/>'
 '<path fill="#FBBC05" d="M5.27 14.29a7.2 7.2 0 0 1 0-4.58V6.62H1.29a12 12 0 0 0 0 10.76l3.98-3.09Z"/>'
 '<path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.43-3.43C17.95 1.18 15.24 0 12 0A12 12 0 0 0 1.29 6.62l3.98 3.09C6.22 6.86 8.87 4.75 12 4.75Z"/></svg>')

# Retirées le 26/09/2026 à la demande de la cliente : le doublon de piscine,
# le poêle à granules et le sauna au panneau « l'endroit idéal ».
GALLERY = [
    ("g01.jpg", "Cours de Pilates au studio Les2L"),
    ("g02.jpg", "Yoga aérien en hamac"),
    ("g03.jpg", "Le studio Les2L à Mouguerre"),
    ("g04.jpg", "La salle et ses barres de danse"),
    ("g05.jpg", "La salle ouverte sur la forêt"),
    ("g06.jpg", "L'espace d'accueil du studio"),
    ("g08.jpg", "La carte cadeau Les2L"),
    ("g09.jpg", "Les agrès de yoga aérien"),
    ("g11.jpg", "Le sauna du studio"),
    ("g12.jpg", "La piscine au coucher du soleil"),
    ("g13.jpg", "Yoga aérien au studio Les2L"),
    ("g14.jpg", "La piscine et la terrasse"),
    ("g16.jpg", "Vue sur la nature depuis la salle"),
    ("g17.jpg", "Le jacuzzi face à la vallée"),
    ("g18.jpg", "Cours à la barre au studio Les2L"),
]

DISCOVER = [
    ("Le planning", c.PLANNING_PDF, True),
    ("Les disciplines", "les-disciplines/", False),
    ("L’équipe", "les-professionnels/", False),
    ("Les tarifs", c.TARIFS_PDF, True),
]

def review_card(name, text):
    initial = name.strip()[0].upper()
    return f"""        <figure class="review">
          <div class="review__head">
            <div class="review__avatar" aria-hidden="true">{initial}</div>
            <div>
              <div class="review__name">{name}</div>
              <div class="review__stars" aria-label="5 étoiles sur 5">★★★★★</div>
            </div>
          </div>
          <blockquote class="review__text">{text}</blockquote>
          <p class="review__source">{IC_GOOGLE}Avis publié sur Google</p>
        </figure>
"""

gallery = "".join(
    f'      <a class="gallery__item" href="assets/img/gallery/{f}" aria-label="Agrandir : {alt}">'
    f'<img src="assets/img/gallery/{f}" alt="{alt}" loading="lazy" decoding="async"></a>\n'
    for f, alt in GALLERY
)

discover = "".join(
    f"""      <article class="discover__card reveal" data-delay="{i % 4}">
        <p class="eyebrow">Découvrez</p>
        <h3>{title}</h3>
        <div class="rule"><span></span></div>
        <a class="btn btn--sm" href="{href}"{' target="_blank" rel="noopener"' if blank else ''}>Découvrir</a>
      </article>
"""
    for i, (title, href, blank) in enumerate(DISCOVER)
)

reviews = "".join(review_card(n, t) for n, t in REVIEWS)

SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SportsActivityLocation",
  "name": "LES 2 L, Pilates Yoga Ballet",
  "description": "Studio de Pilates, Yoga et Ballet au Pays Basque : 17 disciplines, 8 professeures qualifiées, à quelques minutes de Bayonne, Biarritz et Hossegor.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "228 Chemin de Pagadoy",
    "postalCode": "64990",
    "addressLocality": "Mouguerre",
    "addressCountry": "FR"
  },
  "telephone": "+33609148456",
  "email": "les2ailespy@gmail.com",
  "sameAs": [
    "https://www.facebook.com/profile.php?id=100070696928721",
    "https://www.instagram.com/_les2l_/"
  ]
}
</script>
"""

html = c.head(
    "LES 2 L | Pilates, Yoga et Ballet au Pays Basque",
    "Studio Les2L à Mouguerre, Pays Basque : 17 disciplines de Pilates, Yoga et Ballet, "
    "8 professeures qualifiées, à quelques minutes de Bayonne, Biarritz et Hossegor.",
    "https://www.les2ailes.fr/",
    "",
    "",
    SCHEMA,
)
html += c.header("index")
html += f"""
<main id="main">

  <!-- Bandeau d'ouverture -->
  <section class="hero">
    <div class="hero__inner">
      <img class="hero__logo" src="assets/img/logo-blanc.png" alt="" width="516" height="580">
      <p class="hero__brand">Les<em>2</em>L</p>
      <h1 class="hero__tagline">Pilates - Yoga - Ballet</h1>
      <h2 class="hero__place">Pays Basque</h2>
      <div class="hero__socials">
        <a href="{c.FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{c.IC_FB}</a>
        <a href="{c.INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{c.IC_IG}</a>
      </div>
    </div>
  </section>

  <!-- Le lieu -->
  <section class="feature">
    <figure class="feature__bg">
      <img src="assets/img/hero.jpg" alt="La salle du studio Les2L, ouverte sur la forêt"
           width="1920" height="1080" fetchpriority="high" decoding="async">
    </figure>
    <div class="container">
      <div class="feature__card reveal">
        <h2>Le lieu</h2>
        <div class="rule rule--left rule--light"><span></span></div>
        <p>Bienvenue dans Les2L où l'expérience et les qualités professionnelles vous feront découvrir
        17 disciplines pour prendre soin de votre corps, de votre santé et de votre vie.</p>
        <p>Les2L est un établissement convivial avec une superbe salle élégante et confortable au cœur
        d'un bain de forêt. Venez vivre une expérience intense dans une ambiance détendue et très
        sympathique! Les progrès sont ressentis et visibles rapidement. Pour y parvenir, la route est
        fluide, il est facile de se garer, tout est pensé pour faire perdurer les bienfaits de chaque séance.</p>
        <p>Les2L, c'est un lieu unique dans le Pays Basque pour les sportifs ou sédentaires, débutants
        ou confirmés, mixte et de tout âge.</p>
      </div>
    </div>
  </section>

  <!-- Une équipe, des disciplines -->
  <section class="section">
    <div class="container">
      <div class="split">
        <div class="split__media reveal">
          <img src="assets/img/lieu-exterieur.jpg" alt="Le studio Les2L à Mouguerre, au coucher du soleil"
               width="1400" height="1050" loading="lazy" decoding="async">
        </div>
        <div class="split__body reveal" data-delay="1">
          <p>Une équipe de 8 Professeures qualifiées, certifiées, diplômées, expérimentées vous accueille
          tout au long de l’année.</p>
          <p>Sont proposés des cours de Pilates Mat, Pilates sur machines Wall Unit, Pilates sur Reformer,
          Pilates en Suspension(sangles TRX), Stott Pilates, Yin Yoga, Yoga Kundalini, Yoga Hatha Vinyasa,
          Yoga Aérien, Yoga aérien restauratif, Yoga Nidra, Bain Sonore, Munz Floor, Danse Classique pour
          adultes, Total Barre (en salle ou piscine selon météo), Ballet Sculpt et coaching du danseur
          préprofessionnel.</p>
          <p>Remplacez librement vos cours selon votre planning et réservez facilement via l’application.</p>
          <p>Tarifs modulables pour tous les budgets, paiement possible en 10 fois et réductions pour
          étudiants, demandeurs d’emploi et familles.<br>Venez seul ou accompagné !</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Groupes privés & events -->
  <section class="section section--paper">
    <div class="container">
      <div class="split split--reverse">
        <div class="split__media reveal">
          <img src="assets/img/barre-ballet.jpg" alt="Cours à la barre dans la salle Les2L"
               width="1400" height="933" loading="lazy" decoding="async">
        </div>
        <div class="split__body reveal" data-delay="1">
          <p>Sur réservation, Les2L offre l’opportunité de pratiquer le week-end ou jour férié, en groupe
          privé, la discipline de votre choix avec le professeur de votre choix (EVJF, anniversaire,
          cadeau, etc…). Tous les prétextes sont propices pour partager un moment inoubliable !</p>
          <p>Les2L c’est aussi un Event un dimanche par mois: Ateliers, Masterclass, stages, cours
          exceptionnels pendant les vacances.</p>
          <p><strong>Rejoignez-nous !</strong></p>
          <p><a class="btn" href="{c.EVENT_PDF}">Les prochains évènements</a></p>
        </div>
      </div>
    </div>
  </section>

  <!-- Découvrez -->
  <section class="section">
    <div class="container">
      <img src="assets/img/logo.png" alt="" width="516" height="580"
           style="width:88px;margin:0 auto clamp(30px,4vw,48px)" loading="lazy">
      <div class="discover">
{discover}      </div>
    </div>
  </section>

  <!-- Galerie -->
  <section class="section section--tight">
    <div class="container container--wide">
      <div class="gallery">
{gallery}      </div>
    </div>
  </section>

  <!-- Avis -->
  <section class="section section--navy">
    <div class="container">
      <div class="center" style="margin-bottom:clamp(30px,4vw,48px)">
        <p class="eyebrow" style="color:var(--plum-light)">Ils en parlent</p>
        <h2 class="title">Les avis de nos élèves</h2>
        <div class="rule rule--light"><span></span></div>
      </div>
      <div class="reviews">
        <div class="reviews__track" id="reviews-track" tabindex="0"
             role="group" aria-label="Avis de nos élèves, faites défiler pour en voir plus">
{reviews}        </div>
        <div class="reviews__nav">
          <button class="reviews__btn" type="button" data-rev="prev" aria-label="Avis précédents">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 4 7 12l8 8 1.4-1.4L9.8 12l6.6-6.6z"/></svg>
          </button>
          <div class="reviews__dots" id="reviews-dots"></div>
          <button class="reviews__btn" type="button" data-rev="next" aria-label="Avis suivants">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 4 8 8-8 8-1.4-1.4 6.6-6.6-6.6-6.6z"/></svg>
          </button>
        </div>
      </div>
    </div>
  </section>

</main>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Visionneuse d'images">
  <button class="lightbox__btn lightbox__close" type="button" aria-label="Fermer">&times;</button>
  <button class="lightbox__btn lightbox__prev" type="button" aria-label="Image précédente">&#8249;</button>
  <img src="" alt="">
  <button class="lightbox__btn lightbox__next" type="button" aria-label="Image suivante">&#8250;</button>
  <span class="lightbox__count"></span>
</div>
"""
html += c.footer()

open("../index.html", "w", encoding="utf-8").write(html)
print("index.html", len(html), "octets")
