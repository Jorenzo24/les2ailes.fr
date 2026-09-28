# -*- coding: utf-8 -*-
"""Fragments partagés par toutes les pages (en-tête, pied de page, etc.).

`base` = chemin relatif vers la racine du site depuis la page générée.
   ""    pour index.html et 404.html (racine)
   "../" pour les pages en sous-dossier (/planning/, /tarifs/, ...)
"""

# ---------------------------------------------------------------------------
# PROD = False : aperçu GitHub Pages, les pages portent un noindex et
#                robots.txt interdit tout.
# PROD = True  : mise en ligne sur www.les2ailes.fr, indexation autorisée.
# Après changement : cd _build && python3 build_all.py
# ---------------------------------------------------------------------------
PROD = False

BASE_URL = "https://www.les2ailes.fr"

SITE = "LES 2 L"
ADDRESS = "228 Chemin de Pagadoy, 64990 Mouguerre"
FACEBOOK = "https://www.facebook.com/profile.php?id=100070696928721"
INSTAGRAM = "https://www.instagram.com/_les2l_/"
EMAIL = "les2ailespy@gmail.com"
PHONE = "+33 6 09 14 84 56"
PHONE_HREF = "+33609148456"

# Réseaux propres au centre de formation, distincts de ceux du studio.
# Transmis par la cliente le 28/09/2026.
FACEBOOK_FORMATION = "https://www.facebook.com/profile.php?id=61572158867367"
INSTAGRAM_FORMATION = "https://www.instagram.com/les2l.centre.de.formation/"

# TODO cliente : PDF « évènements » à recevoir, puis remplacer par
#   EVENT_PDF = "assets/docs/events.pdf"
EVENT_PDF = "event/"

# TODO cliente : nouveaux PDF planning et tarifs à recevoir ; il suffira de
# remplacer les fichiers dans assets/docs/, les liens ne bougent pas.
PLANNING_PDF = "assets/docs/planning.pdf"
TARIFS_PDF = "assets/docs/tarifs.pdf"

# (cible, libelle, ouverture dans un nouvel onglet)
# Les pages conservent exactement les URL du site actuel ; Planning et Tarifs
# pointent directement sur leur PDF, comme sur le site d'origine.
NAV = [
    ("les-disciplines/", "Disciplines", False),
    ("les-professionnels/", "L’équipe", False),
    (PLANNING_PDF, "Planning", True),
    (TARIFS_PDF, "Tarifs", True),
    ("event/", "Events", False),
    ("contact/", "Contact", False),
    ("le-centre-de-formation/", "Centre de formation professionnelle", False),
]

IC_FB = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 13.5h2.5l1-4H14v-2c0-1.03 0-2 2-2h1.5V2.14c-.33-.04-1.55-.14-2.84-.14C12 2 10.5 3.66 10.5 6.7v2.8H8v4h2.5V22H14v-8.5Z"/></svg>')
IC_IG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 3.25.15 4.77 1.69 4.92 4.92.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.15 3.23-1.66 4.77-4.92 4.92-1.27.06-1.64.07-4.85.07s-3.58-.01-4.85-.07c-3.26-.15-4.77-1.7-4.92-4.92-.06-1.27-.07-1.64-.07-4.85s.01-3.58.07-4.85C2.38 3.92 3.89 2.38 7.15 2.23 8.42 2.18 8.8 2.16 12 2.16Zm0 5.5a4.34 4.34 0 1 0 0 8.68 4.34 4.34 0 0 0 0-8.68Zm0 7.16a2.82 2.82 0 1 1 0-5.64 2.82 2.82 0 0 1 0 5.64Zm4.5-8.4a1.01 1.01 0 1 0 0 2.03 1.01 1.01 0 0 0 0-2.03Z"/></svg>')
IC_PIN = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/></svg>')
IC_MAIL = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm0 4.24-8 4.76-8-4.76V6l8 4.76L20 6v2.24Z"/></svg>')
IC_CAL = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-2V2h-2v2H9V2H7Zm12 8v10H5V10h14Z"/></svg>')
IC_GOOGLE_G = ('<svg viewBox="0 0 24 24" aria-hidden="true">'
 '<path fill="#4285F4" d="M23.5 12.27c0-.79-.07-1.54-.2-2.27H12v4.51h6.47a5.53 5.53 0 0 1-2.4 3.63v3h3.87c2.27-2.09 3.56-5.17 3.56-8.87Z"/>'
 '<path fill="#34A853" d="M12 24c3.24 0 5.96-1.08 7.94-2.91l-3.87-3c-1.08.72-2.45 1.16-4.07 1.16-3.13 0-5.78-2.11-6.73-4.96H1.29v3.09A12 12 0 0 0 12 24Z"/>'
 '<path fill="#FBBC05" d="M5.27 14.29a7.2 7.2 0 0 1 0-4.58V6.62H1.29a12 12 0 0 0 0 10.76l3.98-3.09Z"/>'
 '<path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.43-3.43C17.95 1.18 15.24 0 12 0A12 12 0 0 0 1.29 6.62l3.98 3.09C6.22 6.86 8.87 4.75 12 4.75Z"/></svg>')
IC_VERIFIED = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#1a73e8" '
 'd="M12 1 9.6 3.4 6.3 3l-.6 3.3L2.6 7.9 4.2 11l-1.6 3.1 3.1 1.6.6 3.3 3.3-.4L12 21l2.4-2.4 3.3.4.6-3.3 3.1-1.6-1.6-3.1 1.6-3.1-3.1-1.6-.6-3.3-3.3.4Z"/>'
 '<path fill="#fff" d="m10.8 14.6-2.5-2.5 1.1-1.1 1.4 1.4 3.8-3.8 1.1 1.1Z"/></svg>')
IC_TEL = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1l-2.3 2.2Z"/></svg>')
IC_PDF = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 16 7 11h3V4h4v7h3l-5 5Zm-7 2h14v2H5v-2Z"/></svg>')
IC_ARROW = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 4 8 8-8 8-1.4-1.4 6.6-6.6-6.6-6.6z"/></svg>')
IC_UP = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 6 8 8-1.4 1.4L12 8.8l-6.6 6.6L4 14l8-8Z"/></svg>')

# Avis Google, repris de la fiche MyBusiness via le widget de l'ancien site.
# (nom, horodatage unix, note, texte) : la date affichée est calculée en JS,
# elle reste donc juste avec le temps.
REVIEWS = [
    ("nathalie craspail", 1764720000, 5, "Laurence est une professionnelle hors pair, alliant bienveillance, rigueur et humour. Le tout dans un lieu magique et une très chaleureuse ambiance."),
    ("Nath Ledev", 1764720000, 5, "Un lieu magique, des cours exceptionnels où Laurence, par ses qualités professionnelles, sa créativité et sa grande bienveillance, permet à chacun de découvrir et d'entretenir son corps. Un moment d'apaisement précieux."),
    ("Gerard Zenoni", 1761609600, 5, "Incroyable d’avoir ce niveau de professionnalisme et d'équipements, à  Mouguerre, France ! En deux ans, je suis progressivement passé d'un cours par semaine... à deux... puis trois... et je sens que le quatre n'est pas loin ! Et plus de maux de dos 👍"),
    ("Valérie Hellin", 1761004800, 5, "Un studio exceptionnel avec une propriétaire ex danseuse professionnelle accompagnée de différents intervenants qui vous font travailler tt en longueur et en douceur dans un cadre idyllique"),
    ("Gaelle Llanos Vieillard", 1761004800, 5, "Des cours exceptionnels avec une prof exceptionnelle (Laurence).Je recommande fortement aux adeptes de yoga et pilâtes."),
    ("Sandrine AGUERRE", 1755475200, 5, "Un lieu magique où on prend soin de soi grâce à Laurence, une professeure à l'écoute de ses élèves, très bienveillante et qui nous permet de progresser, d'apprendre à mieux se connaitre grâce à ses cours très complets !! Une très belle découverte à tous points de vue me concernant !!"),
    ("Elise CUISSET", 1679961600, 5, "Lieu magique, au cœur de la nature. Laurence est très professionnelle et bienveillante. Les cours sont variés et efficaces."),
    ("Karine Locatelli", 1679875200, 5, "Les cours de yoga et de pilates de Laurence sont tout simplement magiques. Une professeure de qualité qui œuvre pour le bien être de ses élèves. Résultats assurés !!!"),
    ("Mathias rosandic", 1679011200, 5, "Un lieu exceptionnel avec des cours géniaux. Bon pour le corps mais aussi avec de l'humour. La maîtresse des lieux donne envie que l'on revienne. Merci à Laurence pour ce qu'elle nous partage et enseigne."),
]

CUR = ' aria-current="page"'


def head(title, description, canonical, base="", body_class="", extra=""):
    cls = ' class="%s"' % body_class if body_class else ""
    canon = '<link rel="canonical" href="%s">' % canonical if canonical else ""
    robots = "" if PROD else (
        "<!-- APERÇU : PROD=False dans _build/common.py. "
        "Passer à True puis relancer build_all.py pour la mise en ligne. -->\n"
        '<meta name="robots" content="noindex, nofollow">\n')
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#062c5a">
{robots}{canon}
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{base}assets/img/hero.jpg">
<meta property="og:locale" content="fr_FR">
<link rel="icon" href="{base}assets/img/favicon-32.jpg" sizes="32x32">
<link rel="apple-touch-icon" href="{base}assets/img/favicon-192.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap">
<link rel="stylesheet" href="{base}assets/css/style.css">
{extra}</head>
<body{cls}>
<a class="skip-link" href="#main">Aller au contenu</a>
"""


def header(active, base=""):
    blank = ' target="_blank" rel="noopener"'
    links = "".join(
        '<li><a class="nav__link" href="%s%s"%s%s>%s</a></li>'
        % (base, h, blank if b else "", CUR if h == active else "", t)
        for h, t, b in NAV
    )
    dlinks = "".join(
        '<li><a href="%s%s"%s%s>%s</a></li>'
        % (base, h, blank if b else "", CUR if h == active else "", t)
        for h, t, b in NAV
    )
    home_cur = CUR if active == "index" else ""
    home = base if base else "index.html"
    return f"""<header class="header">
  <div class="header__inner">
    <a class="header__logo" href="{home}"{home_cur} aria-label="LES 2 L, retour à l’accueil">
      <img src="{base}assets/img/logo.png" alt="LES 2 L" width="516" height="580">
    </a>
    <nav class="nav" aria-label="Navigation principale">
      <ul class="nav__list">{links}</ul>
    </nav>
    <button class="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="drawer">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="Menu">
  <button class="drawer__close" type="button" aria-label="Fermer le menu">&times;</button>
  <img class="drawer__logo" src="{base}assets/img/logo-blanc.png" alt="" width="516" height="580">
  <nav aria-label="Navigation mobile">
    <ul class="drawer__list">
      <li><a href="{home}"{home_cur}>Accueil</a></li>
      {dlinks}
    </ul>
  </nav>
</div>
"""


def reviews_band():
    """Carrousel d'avis Google, affiché en pied de page sur toutes les pages."""
    cards = ""
    for i, (nom, ts, note, texte) in enumerate(REVIEWS):
        initiale = nom.strip()[0].upper()
        etoiles = "".join('<span class="rv__star">&#9733;</span>' for _ in range(note))
        cards += f"""          <figure class="rv" role="group" aria-label="Avis de {nom}">
            <span class="rv__avatar" data-i="{i % 5}" aria-hidden="true">{initiale}
              <span class="rv__badge">{IC_GOOGLE_G}</span>
            </span>
            <figcaption class="rv__name">{nom}</figcaption>
            <p class="rv__date" data-ts="{ts}"></p>
            <p class="rv__stars" aria-label="{note} étoiles sur 5">{etoiles}{IC_VERIFIED}</p>
            <blockquote class="rv__text">{texte}</blockquote>
          </figure>
"""
    return f"""<section class="reviews-band" aria-labelledby="reviews-title">
  <div class="container container--wide">
    <h2 class="reviews-band__title" id="reviews-title">Les avis de nos élèves</h2>
    <div class="reviews">
      <button class="reviews__btn reviews__btn--prev" type="button" data-rev="prev" aria-label="Avis précédents">{IC_ARROW}</button>
      <div class="reviews__track" id="reviews-track" tabindex="0"
           role="group" aria-label="Avis Google, faites défiler pour en voir plus">
{cards}      </div>
      <button class="reviews__btn reviews__btn--next" type="button" data-rev="next" aria-label="Avis suivants">{IC_ARROW}</button>
    </div>
    <div class="reviews__dots" id="reviews-dots"></div>
  </div>
</section>

"""


def footer(base="", scripts=""):
    nav_items = "".join(
        '<li><a href="%s%s"%s>%s</a></li>'
        % (base, h, ' target="_blank" rel="noopener"' if b else "", t)
        for h, t, b in NAV
    )
    return reviews_band() + f"""<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <img class="footer__logo" src="{base}assets/img/logo-blanc.png" alt="LES 2 L" width="516" height="580">
        <p><strong>Les2L</strong>, Pilates, Yoga et Ballet au cœur du Pays Basque,
        à quelques minutes de Bayonne, Biarritz et Hossegor.</p>
        <div class="footer__socials">
          <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{IC_FB}</a>
          <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{IC_IG}</a>
        </div>
      </div>
      <div>
        <h4>Le studio</h4>
        <ul>{nav_items}</ul>
      </div>
      <div>
        <h4>Nous trouver</h4>
        <p>{ADDRESS}</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p><a class="btn btn--light btn--sm" href="{base}contact/">Nous écrire</a></p>
      </div>
    </div>
    <div class="footer__bottom">
      <p style="margin:0">&copy; Les2ailes.fr</p>
      <p style="margin:0">Pilates - Yoga - Ballet, Mouguerre, Pays Basque</p>
    </div>
  </div>
</footer>

<button class="to-top" type="button" aria-label="Revenir en haut de la page">{IC_UP}</button>

<div class="cookie" id="cookie" hidden>
  <p>Nous utilisons des cookies pour vous garantir la meilleure expérience sur notre site web.
  Si vous continuez à utiliser ce site, nous supposerons que vous en êtes satisfait.</p>
  <button class="btn btn--sm" type="button">OK</button>
</div>

<script src="{base}assets/js/main.js" defer></script>
{scripts}</body>
</html>
"""


def pagehead(eyebrow, title, intro, bg=None, h1="title"):
    """h1="title"   : le gros titre porte le <h1> (cas général).
       h1="eyebrow" : le <h1> est le petit sur-titre violet, le gros titre
                      n'est plus qu'un élément d'affichage. Utilisé sur le
                      centre de formation, pour que « Formation Instructeur
                      Pilates » soit le h1 sans occuper la place du titre."""
    intro_html = "<p>%s</p>" % intro if intro else ""
    bg_html = ("""<div class="pagehead__bg" style="background-image:url('%s')"></div>""" % bg) if bg else ""
    if h1 == "eyebrow":
        eyebrow_html = '<h1 class="eyebrow">%s</h1>' % eyebrow
        title_html = '<p class="pagehead__display">%s</p>' % title
    else:
        eyebrow_html = '<p class="eyebrow">%s</p>' % eyebrow
        title_html = "<h1>%s</h1>" % title
    return f"""<section class="pagehead">
  {bg_html}
  {eyebrow_html}
  {title_html}
  {intro_html}
</section>
"""
