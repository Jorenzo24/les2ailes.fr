# -*- coding: utf-8 -*-
import common as c

# ---------------------------------------------------------------- EVENT ----
html = c.head(
    "Event — ateliers, masterclass et stages | LES 2 L Pays Basque",
    "Un dimanche par mois, Les2L propose des ateliers, masterclass, stages et cours exceptionnels "
    "pendant les vacances, ainsi que des groupes privés le week-end et les jours fériés.",
    "https://www.les2ailes.fr/event/",
)
html += c.header("event.html")
html += c.pagehead(
    "Un dimanche par mois",
    "Event",
    "Les2L c’est aussi un Event un dimanche par mois: Ateliers, Masterclass, stages, cours "
    "exceptionnels pendant les vacances.",
    "assets/img/gallery/g13.jpg",
)
html += f"""
<main id="main">
  <section class="section">
    <div class="container">
      <div class="split">
        <div class="split__media reveal">
          <img src="assets/img/gallery/g02.jpg" alt="Séance de yoga aérien au studio Les2L"
               width="1100" height="1375" loading="lazy" decoding="async">
        </div>
        <div class="split__body reveal" data-delay="1">
          <p class="eyebrow">Les rendez-vous</p>
          <h2 class="title">Ateliers, masterclass &amp; stages</h2>
          <div class="rule rule--left"><span></span></div>
          <p>Les2L c’est aussi un Event un dimanche par mois: Ateliers, Masterclass, stages, cours
          exceptionnels pendant les vacances.</p>
          <p><strong>Rejoignez-nous !</strong></p>
          <p><a class="btn" href="contact.html">Être informé des prochains events</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="container">
      <div class="split split--reverse">
        <div class="split__media reveal">
          <img src="assets/img/gallery/g12.jpg" alt="La piscine du studio Les2L au coucher du soleil"
               width="1100" height="825" loading="lazy" decoding="async">
        </div>
        <div class="split__body reveal" data-delay="1">
          <p class="eyebrow">Sur réservation</p>
          <h2 class="title">Groupes privés</h2>
          <div class="rule rule--left"><span></span></div>
          <p>Sur réservation, Les2L offre l’opportunité de pratiquer le week-end ou jour férié, en
          groupe privé, la discipline de votre choix avec le professeur de votre choix (EVJF,
          anniversaire, cadeau, etc…). Tous les prétextes sont propices pour partager un moment
          inoubliable !</p>
          <p><a class="btn btn--ghost" href="contact.html">Réserver un groupe privé</a></p>
        </div>
      </div>
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
html += c.footer()
open("../event.html", "w", encoding="utf-8").write(html)
print("event.html ok")

# -------------------------------------------------------------- CONTACT ----
MAP = ("https://www.google.com/maps?q=228+Chemin+de+Pagadoy,+64990+Mouguerre&output=embed")

html = c.head(
    "Contact — studio Les2L à Mouguerre | Pilates, Yoga, Ballet",
    "Contactez le studio Les2L, 228 Chemin de Pagadoy à Mouguerre (64990), à quelques minutes de "
    "Bayonne, Biarritz et Hossegor. Parking gratuit sur place.",
    "https://www.les2ailes.fr/contact/",
)
html += c.header("contact.html")
html += c.pagehead(
    "Écrivez-nous",
    "Contact",
    "Une question sur un cours, un niveau, une réservation ou un groupe privé&nbsp;? "
    "Nous vous répondons rapidement.",
    "assets/img/lieu-exterieur.jpg",
)
html += f"""
<main id="main">
  <section class="section">
    <div class="container">
      <div class="contact-grid">

        <div class="reveal">
          <h2 class="subtitle">Envoyer un message</h2>
          <div class="rule rule--left"><span></span></div>
          <form class="form" id="contact-form" data-mailto="{c.EMAIL}" novalidate>
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
            <div>
              <button class="btn" type="submit">Envoyer</button>
            </div>
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
            <li>{c.IC_MAIL}<div><b>E-mail</b><a href="mailto:{c.EMAIL}">{c.EMAIL}</a></div></li>
            <li>{c.IC_CAL}<div><b>Horaires</b>Voir <a href="planning.html">le planning des cours</a></div></li>
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
html += c.footer()
open("../contact.html", "w", encoding="utf-8").write(html)
print("contact.html ok")
