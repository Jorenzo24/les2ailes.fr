# -*- coding: utf-8 -*-
import common as c


# Ateliers repris mot pour mot du PDF « ATELIERS 2026-2027 » de la cliente.
# (titre, intervenant, date, créneaux, durée en minutes)
# Les six dates ont été vérifiées : elles tombent toutes un dimanche.
ATELIERS = [
 ("Technique Martha Graham", "Laureen Elisabeth", "Dimanche 18 octobre 2026",
  ["10h à 11h30"], 90),
 ("Danse aérienne", "Melissa Delattre", "Dimanche 6 décembre 2026",
  ["10h à 12h"], 120),
 ("Yoga Inversions &amp; Wheel", "Sabine Sandri", "Dimanche 24 janvier 2027",
  ["Débutant 9h30 à 11h", "Avancé 11h30 à 13h"], 90),
 ("Bain sonore hypnotique", "Benjamin, « une voie pour soi »", "Dimanche 21 mars 2027",
  ["10h à 11h30"], 90),
 ("Yoga en famille", "Alexandra Strzempa", "Dimanche 23 mai 2027",
  ["10h à 11h30"], 90),
 ("Danses basques", "Itziar Mendivil", "Dimanche 27 juin 2027",
  ["Débutant 9h30 à 11h", "Inter. 11h30 à 13h"], 90),
]

# Un lien vide masque simplement le bouton : les deux liens Stripe sont en
# attente de la cliente (un pour 1 h 30, un pour 2 h).
LIENS = {90: c.STRIPE_ATELIER_1H30, 120: c.STRIPE_ATELIER_2H}
DUREES = {90: "1 h 30", 120: "2 h"}

ateliers_html = ""
for titre, qui, date, creneaux, duree in ATELIERS:
    horaires = "".join('<li>%s</li>' % h for h in creneaux)
    lien = LIENS.get(duree, "")
    bouton = ('<a class="btn btn--sm" href="%s" target="_blank" rel="noopener">Réserver</a>' % lien) if lien else ""
    ateliers_html += f"""        <article class="atelier reveal">
          <div class="atelier__tete">
            <h3 class="atelier__titre">{titre}</h3>
            <p class="atelier__qui">avec {qui}</p>
          </div>
          <div class="atelier__quand">
            <p class="atelier__date">{date}</p>
            <ul class="atelier__horaires">{horaires}</ul>
          </div>
          <div class="atelier__action">
            <span class="atelier__duree">{DUREES[duree]}</span>
            {bouton}
          </div>
        </article>
"""

# ---------------------------------------------------------------- EVENT ----
html = c.head(
    "Events, ateliers, masterclass et stages | LES 2 L Pays Basque",
    "Un dimanche par mois, Les2L propose des ateliers, masterclass, stages et cours exceptionnels "
    "pendant les vacances, ainsi que des groupes privés le week-end et les jours fériés.",
    "https://www.les2ailes.fr/event/",
    "../",
)
html += c.header("event/", "../")
html += c.pagehead(
    "Un dimanche par mois",
    "Events",
    "Les2L c’est aussi un Event un dimanche par mois: Ateliers, Masterclass, stages, cours "
    "exceptionnels pendant les vacances.",
    "../assets/img/gallery/g04.jpg",
)
html += f"""
<main id="main">
  <section class="section">
    <div class="container">
      <div class="split">
        <div class="split__media reveal">
          <!-- TODO cliente : photo dédiée aux ateliers à recevoir ; en attendant,
               on garde ce visuel de yoga aérien, choisi par la cliente -->
          <img src="../assets/img/gallery/g02.jpg" alt="Séance de yoga aérien au studio Les2L"
               width="1100" height="1375" loading="lazy" decoding="async">
        </div>
        <div class="split__body reveal" data-delay="1">
          <p class="eyebrow">Les rendez-vous</p>
          <h2 class="title">Ateliers, masterclass &amp; stages</h2>
          <div class="rule rule--left"><span></span></div>
          <p>Les2L c’est aussi un Event un dimanche par mois: Ateliers, Masterclass, stages, cours
          exceptionnels pendant les vacances.</p>
          <p><strong>Rejoignez-nous !</strong></p>
          <p><a class="btn" href="#ateliers">Voir les ateliers de la saison</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="container">
      <div class="split split--reverse">
        <div class="split__media reveal">
          <img src="../assets/img/cours-prive.jpg"
               alt="La salle du studio Les2L, prête pour un cours en groupe privé"
               width="1400" height="933" loading="lazy" decoding="async">
        </div>
        <div class="split__body reveal" data-delay="1">
          <p class="eyebrow">Sur réservation</p>
          <h2 class="title">Groupes privés</h2>
          <div class="rule rule--left"><span></span></div>
          <p>Sur réservation, Les2L offre l’opportunité de pratiquer le week-end ou jour férié, en
          groupe privé, la discipline de votre choix avec le professeur de votre choix (EVJF,
          anniversaire, cadeau, etc…). Tous les prétextes sont propices pour partager un moment
          inoubliable !</p>
          <p>Il y a la possibilité d’organiser un cours privé les week-end, en duo, trio ou
          groupe pour un EVJF, Baby Shower, Retrouvailles, anniversaire de mariage,
          anniversaire, célébration et réussite, etc.</p>
          <p>Prenez contact avec moi par le formulaire ou par téléphone.</p>
          <p style="display:flex;gap:12px;flex-wrap:wrap">
            <a class="btn btn--ghost" href="../contact/">Nous écrire</a>
            <a class="btn btn--ghost" href="tel:{c.PHONE_HREF}">{c.PHONE}</a>
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="ateliers">
    <div class="container container--wide">
      <div class="center" style="margin-bottom:clamp(30px,4vw,48px)">
        <p class="eyebrow">Un dimanche par mois</p>
        <h2 class="title">Les ateliers 2026-2027</h2>
        <div class="rule"><span></span></div>
      </div>
      <div class="ateliers">
{ateliers_html}      </div>
      <p class="center" style="margin-top:clamp(28px,3.4vw,42px)">
        <a class="btn btn--ghost" href="../{c.EVENT_PDF}" target="_blank" rel="noopener">
          {c.IC_PDF}Télécharger le programme (PDF)
        </a>
      </p>
    </div>
  </section>

  <section class="section section--navy section--tight center">
    <div class="container">
      <p class="eyebrow" style="color:var(--plum-light)">Restez informé</p>
      <h2 class="title">Le programme des prochains events</h2>
      <div class="rule rule--light"><span></span></div>
      <p class="lead" style="max-width:660px;margin-inline:auto">
        Les dates et thèmes des prochains ateliers sont annoncés sur nos réseaux sociaux
        et au studio.
      </p>
      <p style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:24px">
        <a class="btn btn--light" href="{c.INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
        <a class="btn btn--light" href="{c.FACEBOOK}" target="_blank" rel="noopener">Facebook</a>
      </p>
    </div>
  </section>
</main>
"""
html += c.footer("../")
open("../event/index.html", "w", encoding="utf-8").write(html)
print("event.html ok")

# -------------------------------------------------------------- CONTACT ----
MAP = ("https://www.google.com/maps?q=228+Chemin+de+Pagadoy,+64990+Mouguerre&output=embed")

html = c.head(
    "Contact | Studio Les2L à Mouguerre, Pilates, Yoga, Ballet",
    "Contactez le studio Les2L au +33 6 09 14 84 56, 228 Chemin de Pagadoy à Mouguerre (64990), "
    "à quelques minutes de Bayonne, Biarritz et Hossegor. Parking gratuit sur place.",
    "https://www.les2ailes.fr/contact/",
    "../",
)
html += c.header("contact/", "../")
html += c.pagehead(
    "Écrivez-nous",
    "Contact",
    "Une question sur un cours, un niveau, une réservation ou un groupe privé&nbsp;? "
    "Nous vous répondons rapidement.",
    "../assets/img/lieu-exterieur.jpg",
)
html += f"""
<main id="main">
  <section class="section">
    <div class="container">
      <div class="contact-grid">

        <div class="reveal">
          <h2 class="subtitle">Envoyer un message</h2>
          <div class="rule rule--left"><span></span></div>
          <form class="form" id="contact-form" action="envoi.php" method="post" novalidate>
            <div class="field">
              <label for="nom">Nom</label>
              <input type="text" id="nom" name="nom" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="email">E-mail</label>
              <input type="email" id="email" name="email" autocomplete="email" required>
            </div>
            <div class="field">
              <label for="message">Message</label>
              <textarea id="message" name="message" required></textarea>
            </div>
            <div class="field field--pot" aria-hidden="true">
              <label for="website">Ne pas remplir ce champ</label>
              <input type="text" id="website" name="website" tabindex="-1" autocomplete="off">
            </div>
            <div>
              <button class="btn" type="submit">Envoyer</button>
            </div>
            <p class="form__status" id="form-status" role="status" hidden></p>
            <p class="form__note">
              Vos informations ne servent qu’à répondre à votre demande.
            </p>
          </form>
        </div>

        <div class="reveal" data-delay="1">
          <h2 class="subtitle">Le studio</h2>
          <div class="rule rule--left"><span></span></div>
          <ul class="contact-list">
            <li>{c.IC_PIN}<div><b>Adresse</b>228 Chemin de Pagadoy<br>Mouguerre 64990</div></li>
            <li>{c.IC_TEL}<div><b>Téléphone</b><a href="tel:{c.PHONE_HREF}">{c.PHONE}</a></div></li>
            <li>{c.IC_MAIL}<div><b>E-mail</b><a href="mailto:{c.EMAIL}">{c.EMAIL}</a></div></li>
            <li>{c.IC_CAL}<div><b>Horaires</b>Voir <a href="../{c.PLANNING_PDF}" target="_blank" rel="noopener">le planning des cours</a></div></li>
          </ul>
          <p>Un établissement élégant et confortable, avec parking gratuit sur place et accès direct
          à l’autoroute, à quelques minutes de Bayonne, Biarritz et Hossegor.</p>
          <div class="footer__socials" style="margin-bottom:22px">
            <a href="{c.FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook"
               style="border-color:var(--line);color:var(--navy)">{c.IC_FB}</a>
            <a href="{c.INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram"
               style="border-color:var(--line);color:var(--navy)">{c.IC_IG}</a>
          </div>
          <iframe class="map" src="{MAP}" title="Carte : 228 Chemin de Pagadoy, Mouguerre"
                  loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        </div>

      </div>
    </div>
  </section>
</main>
"""
html += c.footer("../")
open("../contact/index.html", "w", encoding="utf-8").write(html)
print("contact.html ok")
