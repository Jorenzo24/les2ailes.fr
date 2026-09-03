# -*- coding: utf-8 -*-
import common as c

DAYS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

# (heure de départ, {jour: (créneau, cours, professeure)})
ROWS = [
 ("8h30",  {"Mercredi": ("8H30/9H30", "YIN YOGA", "Laurence")}),
 ("9h30",  {"Lundi":     ("9H30/10H30", "PILATES Machines *", "Emilie"),
            "Mardi":     ("9H30/10H30", "PILATES Sol *", "Laurence"),
            "Jeudi":     ("9H30/10H30", "PILATES Machines *", "Laurence"),
            "Vendredi":  ("9H30/10H30", "MUNZ FLOOR", "Lenie"),
            "Samedi":    ("9H30/10H30", "BALLET SCULPT", "Caroline")}),
 ("10h45", {"Lundi":     ("10H45/11H45", "PILATES Suspension TRX *", "Emilie"),
            "Samedi":    ("10H45/11H45", "BALLET", "Caroline/Laurence")}),
 ("11h15", {"Vendredi":  ("11H15/12H15", "PILATES Sol &amp; Stretching", "Sarah")}),
 ("12h00", {"Samedi":    ("12h00/13h00", "PILATES Machines/Sol", "Caroline/Laurence")}),
 ("12h30", {"Mardi":     ("12H30/13H30", "PILATES Machines ***", "Laurence"),
            "Jeudi":     ("12H30/13H30", "PILATES Machines/Hamac **", "Laurence"),
            "Vendredi":  ("12H30/13H30", "BODYFLOW", "Sarah")}),
 ("13h15", {"Mercredi":  ("13H15/14H15", "PILATES Machines/Hamac **", "Laurence")}),
 ("14h30", {"Mercredi":  ("14H30/15H30", "STOTT PILATES", "Laureen")}),
 ("15h45", {"Mercredi":  ("15H45/16H45", "TOTAL BARRE", "Laureen")}),
 ("17h00", {"Mercredi":  ("17H00/18H00", "YOGA AERIEN KIDS 8/14", "Alexandra"),
            "Vendredi":  ("17H00/18H00", "YOGA Vinyasa &amp; Inversions ***", "Helen")}),
 ("17h30", {"Lundi":     ("17H30/18H30", "PILATES Machines/Hamac **", "Laurence")}),
 ("18h00", {"Mardi":     ("18H00/19H00", "PILATES Machines **", "Laurence")}),
 ("18h15", {"Vendredi":  ("18H15/19H15", "YIN YOGA Aérien &amp; Bain Sonore", "Helen")}),
 ("18h30", {"Mercredi":  ("18H30/19H30", "YOGA AERIEN ***", "Alexandra")}),
 ("18h45", {"Lundi":     ("18H45/19H45", "PILATES Sol **", "Laurence"),
            "Jeudi":     ("18H45/19H45", "PILATES Suspension TRX **", "Emilie")}),
 ("19h15", {"Mardi":     ("19H15/20H15", "YOGA AERIEN **", "Laurence")}),
 ("19h45", {"Mercredi":  ("19H45/20H45", "PILATES Sol **", "Laurence")}),
]

head_cells = "".join('<th scope="col">%s</th>' % d for d in DAYS)
body = ""
for hour, slots in ROWS:
    tds = ""
    for d in DAYS:
        if d in slots:
            time, name, teacher = slots[d]
            tds += (f'<td><span class="slot__time">{time}</span>'
                    f'<span class="slot__name">{name}</span>'
                    f'<span class="slot__teacher">{teacher}</span></td>')
        else:
            tds += "<td></td>"
    body += f'        <tr><th scope="row">{hour}</th>{tds}</tr>\n'

html = c.head(
    "Planning 2026-2027 — cours de Pilates, Yoga et Ballet | LES 2 L",
    "Le planning 2026-2027 du studio Les2L à Mouguerre : Pilates Mat et machines, Yoga Aérien, "
    "Yin Yoga, Munz Floor, Ballet Sculpt, Total Barre — du lundi au samedi.",
    "https://www.les2ailes.fr/planning/",
)
html += c.header("planning.html")
html += c.pagehead(
    "Saison 2026-2027",
    "Le planning",
    "Du lundi au samedi, matin, midi et soir. Remplacez librement vos cours selon votre planning "
    "et réservez facilement via l’application.",
    "assets/img/gallery/g04.jpg",
)
html += f"""
<main id="main">
  <section class="section">
    <div class="container container--wide">
      <div class="reveal">
        <div class="table-scroll">
          <table class="planning-table">
            <thead>
              <tr><th scope="col"><span class="sr-only">Horaire</span></th>{head_cells}</tr>
            </thead>
            <tbody>
{body}            </tbody>
          </table>
        </div>
        <ul class="legend">
          <li><b>*</b> Débutant</li>
          <li><b>**</b> Intermédiaire</li>
          <li><b>***</b> Avancé</li>
        </ul>
        <p style="margin-top:26px">
          <a class="btn" href="assets/docs/planning.pdf" target="_blank" rel="noopener">
            {c.IC_PDF}Télécharger le planning (PDF)
          </a>
        </p>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="container container--narrow">
      <div class="center" style="margin-bottom:clamp(26px,3vw,38px)">
        <p class="eyebrow">Version imprimable</p>
        <h2 class="title">Planning 2026-2027</h2>
        <div class="rule"><span></span></div>
      </div>
      <figure class="planning-figure reveal">
        <img src="assets/img/planning-2026-2027.jpg"
             alt="Planning des cours 2026-2027 du studio Les2L Mouguerre, du lundi au samedi"
             width="1600" height="2000" loading="lazy" decoding="async">
      </figure>
    </div>
  </section>

  <section class="section section--tight center">
    <div class="container">
      <p class="lead" style="max-width:640px;margin-inline:auto">
        Une question sur un créneau, un niveau ou une réservation&nbsp;? Écrivez-nous, nous vous répondons rapidement.
      </p>
      <p style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:22px">
        <a class="btn" href="contact.html">Nous contacter</a>
        <a class="btn btn--ghost" href="tarifs.html">Voir les tarifs</a>
      </p>
    </div>
  </section>
</main>
"""
html += c.footer()
open("../planning.html", "w", encoding="utf-8").write(html)
print("planning.html ok")
