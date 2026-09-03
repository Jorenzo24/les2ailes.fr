# -*- coding: utf-8 -*-
"""Fragments partagés par toutes les pages (en-tête, pied de page, etc.)."""

SITE = "LES 2 L"
BASELINE = "Pilates · Yoga · Ballet — Pays Basque"
ADDRESS = "228 Chemin de Pagadoy, 64990 Mouguerre"
FACEBOOK = "https://www.facebook.com/profile.php?id=100070696928721"
INSTAGRAM = "https://www.instagram.com/_les2l_/"
EMAIL = "les2ailespy@gmail.com"

NAV = [
    ("disciplines.html", "Disciplines"),
    ("equipe.html", "L’équipe"),
    ("planning.html", "Planning"),
    ("tarifs.html", "Tarifs"),
    ("event.html", "Event"),
    ("contact.html", "Contact"),
    ("centre-de-formation.html", "Centre de formation professionnelle"),
]

IC_FB = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 13.5h2.5l1-4H14v-2c0-1.03 0-2 2-2h1.5V2.14c-.33-.04-1.55-.14-2.84-.14C12 2 10.5 3.66 10.5 6.7v2.8H8v4h2.5V22H14v-8.5Z"/></svg>')
IC_IG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 3.25.15 4.77 1.69 4.92 4.92.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.15 3.23-1.66 4.77-4.92 4.92-1.27.06-1.64.07-4.85.07s-3.58-.01-4.85-.07c-3.26-.15-4.77-1.7-4.92-4.92-.06-1.27-.07-1.64-.07-4.85s.01-3.58.07-4.85C2.38 3.92 3.89 2.38 7.15 2.23 8.42 2.18 8.8 2.16 12 2.16Zm0 5.5a4.34 4.34 0 1 0 0 8.68 4.34 4.34 0 0 0 0-8.68Zm0 7.16a2.82 2.82 0 1 1 0-5.64 2.82 2.82 0 0 1 0 5.64Zm4.5-8.4a1.01 1.01 0 1 0 0 2.03 1.01 1.01 0 0 0 0-2.03Z"/></svg>')
IC_PIN = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/></svg>')
IC_MAIL = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm0 4.24-8 4.76-8-4.76V6l8 4.76L20 6v2.24Z"/></svg>')
IC_CAL = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-2V2h-2v2H9V2H7Zm12 8v10H5V10h14Z"/></svg>')
IC_PDF = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 16 7 11h3V4h4v7h3l-5 5Zm-7 2h14v2H5v-2Z"/></svg>')
IC_UP = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 6 8 8-1.4 1.4L12 8.8l-6.6 6.6L4 14l8-8Z"/></svg>')


def head(title, description, current, extra=""):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#062c5a">
<!-- APERÇU GitHub Pages : retirer cette ligne + ajuster robots.txt lors de la mise en ligne sur le domaine définitif -->
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{current}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="assets/img/hero.jpg">
<meta property="og:locale" content="fr_FR">
<link rel="icon" href="assets/img/favicon-32.jpg" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/favicon-192.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap">
<link rel="stylesheet" href="assets/css/style.css">
{extra}</head>
<body>
<a class="skip-link" href="#main">Aller au contenu</a>
"""


def header(active):
    CUR = ' aria-current="page"'
    links = "".join(
        '<li><a class="nav__link" href="%s"%s>%s</a></li>' % (h, CUR if h == active else "", t)
        for h, t in NAV
    )
    dlinks = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (h, CUR if h == active else "", t)
        for h, t in NAV
    )
    home_cur = CUR if active == "index.html" else ""
    return f"""<header class="header">
  <div class="header__inner">
    <a class="header__logo" href="index.html"{home_cur} aria-label="LES 2 L — accueil">
      <img src="assets/img/logo.png" alt="LES 2 L" width="516" height="580">
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
  <img class="drawer__logo" src="assets/img/logo-blanc.png" alt="" width="516" height="580">
  <nav aria-label="Navigation mobile">
    <ul class="drawer__list">
      <li><a href="index.html"{home_cur}>Accueil</a></li>
      {dlinks}
    </ul>
  </nav>
</div>
"""


def footer(scripts=""):
    nav_items = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <img class="footer__logo" src="assets/img/logo-blanc.png" alt="LES 2 L" width="516" height="580">
        <p><strong>Les2L</strong> — Pilates, Yoga et Ballet au cœur du Pays Basque,
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
        <p><a class="btn btn--light btn--sm" href="contact.html">Nous écrire</a></p>
      </div>
    </div>
    <div class="footer__bottom">
      <p style="margin:0">&copy; Les2ailes.fr</p>
      <p style="margin:0">Pilates &middot; Yoga &middot; Ballet &mdash; Mouguerre, Pays Basque</p>
    </div>
  </div>
</footer>

<button class="to-top" type="button" aria-label="Revenir en haut de la page">{IC_UP}</button>

<div class="cookie" id="cookie" hidden>
  <p>Nous utilisons des cookies pour vous garantir la meilleure expérience sur notre site web.
  Si vous continuez à utiliser ce site, nous supposerons que vous en êtes satisfait.</p>
  <button class="btn btn--sm" type="button">OK</button>
</div>

<script src="assets/js/main.js" defer></script>
{scripts}</body>
</html>
"""


def pagehead(eyebrow, title, intro, bg="assets/img/hero.jpg"):
    intro_html = f"<p>{intro}</p>" if intro else ""
    return f"""<section class="pagehead">
  <div class="pagehead__bg" style="background-image:url('{bg}')"></div>
  <p class="eyebrow">{eyebrow}</p>
  <h1>{title}</h1>
  {intro_html}
</section>
"""
