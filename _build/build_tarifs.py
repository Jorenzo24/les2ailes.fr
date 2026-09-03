# -*- coding: utf-8 -*-
import common as c

# Tarifs repris du document officiel Tarifs.pdf
PLANS = [
 ("ABONNEMENT LIBERTÉ", "Toutes les disciplines<br>Je viens quand je veux*", False,
  [("1 cours par semaine", "55€", "mois x10 mois"),
   ("2 cours par semaine", "85€", "mois x10 mois"),
   ("Cours illimités", "105€", "mois x10 mois")]),
 ("ABONNEMENT CHALLENGE", "Toutes les disciplines<br>(sauf Yoga Aérien / Pilates Machines)", True,
  [("1 cours par semaine", "45€", "mois x10 mois"),
   ("2 cours par semaine", "70€", "mois x10 mois"),
   ("Cours illimités", "90€", "mois x10 mois")]),
 ("ABONNEMENT ZOOM", "Toutes les disciplines<br>(sauf Yoga Aérien / Pilates Machines)", False,
  [("1 cours par semaine", "40€", "mois x10 mois"),
   ("2 cours par semaine", "65€", "mois x10 mois")]),
 ("YOGA AÉRIEN KIDS", "Terrien et aérien", False,
  [("1 cours par semaine", "40€", "mois x10 mois")]),
]

UNITS = [
 ("COURS À L’UNITÉ", "", "25€", ""),
 ("COURS INDIVIDUEL", "Sur Reformer (60 min)", "55€", ""),
 ("CARTE 10 COURS", "Valable 6 mois", "180€", ""),
]


def rates(items):
    out = ""
    for label, price, unit in items:
        small = ' <small>%s</small>' % unit if unit else ""
        out += (f'          <div class="rate"><span class="rate__label">{label}</span>'
                f'<span class="rate__price">{price}{small}</span></div>\n')
    return out


cards = ""
for i, (title, sub, feature, items) in enumerate(PLANS):
    cls = " plan--feature" if feature else ""
    cards += f"""      <article class="plan{cls} reveal" data-delay="{i % 3}">
        <div class="plan__head">
          <h2>{title}</h2>
          <p>{sub}</p>
        </div>
        <div class="plan__body">
{rates(items)}        </div>
      </article>
"""

units = ""
for i, (title, sub, price, unit) in enumerate(UNITS):
    subhtml = "<p>%s</p>" % sub if sub else ""
    units += f"""      <article class="plan reveal" data-delay="{i % 3}">
        <div class="plan__head">
          <h2>{title}</h2>
          {subhtml}
        </div>
        <div class="plan__body">
          <div class="rate"><span class="rate__price">{price}</span></div>
        </div>
      </article>
"""

html = c.head(
    "Tarifs et abonnements | LES 2 L — Pilates, Yoga, Ballet Pays Basque",
    "Abonnements Liberté, Challenge et Zoom, cours à l’unité, cours individuel et carte 10 cours. "
    "Tarifs modulables, paiement en 10 fois et réductions étudiants, demandeurs d’emploi et familles.",
    "https://www.les2ailes.fr/tarifs/",
)
html += c.header("tarifs.html")
html += c.pagehead(
    "Pour tous les budgets",
    "Les tarifs",
    "Tarifs modulables pour tous les budgets, paiement possible en 10 fois et réductions pour "
    "étudiants, demandeurs d’emploi et familles.",
    "assets/img/gallery/g18.jpg",
)
html += f"""
<main id="main">
  <section class="section">
    <div class="container container--wide">
      <div class="pricing">
{cards}      </div>

      <h2 class="title center" style="margin-top:clamp(48px,6vw,80px)">À l’unité</h2>
      <div class="rule"><span></span></div>
      <div class="pricing">
{units}      </div>

      <div class="pricing-note reveal">
        <p><strong>50€ de frais d’inscription</strong></p>
        <p>10% de réduction pour la 2ème personne du foyer, 10% de réduction pour les demandeurs
        d'emploi, 25% de réduction pour les étudiants</p>
        <p>Cours sur 35 semaines dans l’année (sauf pendant vacances scolaires)</p>
        <p style="margin-top:1.4em">
          <a class="btn" href="assets/docs/tarifs.pdf" target="_blank" rel="noopener">
            {c.IC_PDF}Télécharger les tarifs (PDF)
          </a>
        </p>
      </div>
    </div>
  </section>

  <section class="section section--navy section--tight center">
    <div class="container">
      <p class="eyebrow" style="color:var(--plum-light)">Une envie&nbsp;?</p>
      <h2 class="title">Venez seul ou accompagné&nbsp;!</h2>
      <div class="rule rule--light"><span></span></div>
      <p class="lead" style="max-width:660px;margin-inline:auto">
        Sur réservation, Les2L offre l’opportunité de pratiquer le week-end ou jour férié, en groupe
        privé, la discipline de votre choix avec le professeur de votre choix (EVJF, anniversaire,
        cadeau, etc…).
      </p>
      <p style="margin-top:24px"><a class="btn btn--light" href="contact.html">Nous contacter</a></p>
    </div>
  </section>
</main>
"""
html += c.footer()
open("../tarifs.html", "w", encoding="utf-8").write(html)
print("tarifs.html ok")
