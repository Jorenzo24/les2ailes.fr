# -*- coding: utf-8 -*-
import common as c

MODULES = [
 ("MATWORK 1", "[pour public niveau débutant]", "26 &amp; 27 Septembre + 3 &amp; 4 octobre 2026",
  [("financement personnel", "890€"), ("avec prise en charge", "1090€")]),
 ("MATWORK 2", "[pour public niveau intermédiaire]", "28 &amp; 29 novembre 2026 + 5 &amp; 6 décembre",
  [("financement personnel", "890€"), ("avec prise en charge", "1090€")]),
 ("MATWORK 3", "[pour public niveau avancé]", "30 &amp; 31 janvier 2027 + 6 &amp; 7 février 2027",
  [("financement personnel", "890€"), ("avec prise en charge", "1090€")]),
 ("Petit matériel (magic circle, foam roller, élastique, balles, ballon paille.)", "[pour tous niveaux]",
  "6 &amp; 7 mars 2027",
  [("financement personnel", "490€"), ("avec prise en charge", "590€")]),
 ("SWISS BALL", "[pour tous niveaux]", "3 &amp; 4 avril 2027",
  [("financement personnel", "490€"), ("avec prise en charge", "590€")]),
 ("WALL UNIT [Machine]", "[pour public niveau débutant, intermédiaire et avancé]",
  "29 &amp; 30 mai 2027 + 5 &amp; 6 juin 2027",
  [("financement personnel", "1090€"), ("avec prise en charge", "1290€")]),
]

CURSUS = [
 ("ico-cursus-complet.png", "CURSUS COMPLET", "Matwork 1 2,3, Petit Matériel, Swiss Ball, Machines Wall Unit",
  [("financement personnel", "4029€"), ("avec prise en charge", "4429€")]),
 ("ico-cursus-matwork.png", "CURSUS MATWORK 1,2,3", "",
  [("financement personnel", "2470€"), ("avec prise en charge", "2770€")]),
 ("ico-package.png", "PACKAGE PETIT MATÉRIEL &amp; SWISSBALL", "",
  [("financement personnel", "880€"), ("avec prise en charge", "1080€")]),
]


def prices(items):
    return "".join('<li><span>%s</span><b>%s</b></li>' % (lbl, p) for lbl, p in items)


modules = ""
for i, (title, level, dates, pr) in enumerate(MODULES, 1):
    lignes = "".join('<li><span>%s</span><b>%s</b></li>' % (lbl, p) for lbl, p in pr)
    modules += f"""      <article class="step reveal">
        <p class="step__num">{i:02d}</p>
        <div>
          <h3 class="step__title">{title}</h3>
          <p class="step__level">{level}</p>
          <p class="step__dates">{c.IC_CAL}<span>{dates}</span></p>
        </div>
        <ul class="step__prices">{lignes}</ul>
      </article>
"""

cursus = ""
for i, (icon, title, sub, pr) in enumerate(CURSUS):
    cls = " pack--highlight" if i == 0 else ""
    detail = sub if sub else "&nbsp;"
    lignes = "".join('<li><b>%s</b><span>%s</span></li>' % (p, lbl) for lbl, p in pr)
    cursus += f"""      <article class="pack{cls} reveal" data-delay="{i % 3}">
        <img class="pack__icon" src="../assets/img/formation/{icon}" alt="" width="600" height="600" loading="lazy">
        <h3 class="pack__title">{title}</h3>
        <p class="pack__detail">{detail}</p>
        <ul class="pack__prices">{lignes}</ul>
      </article>
"""

html = c.head(
    "Centre de formation professionnelle Pilates | LES 2 L Pays Basque",
    "LES2L Centre de Formation : formation professionnelle qualifiante d’Instructeur Pilates au Pays "
    "Basque. Modules Matwork, Petit matériel, Swiss Ball et Wall Unit, finançables par l’État.",
    "https://www.les2ailes.fr/le-centre-de-formation/",
    "../",
)
html += c.header("le-centre-de-formation/", "../")
html += c.pagehead(
    "Devenir instructeur Pilates",
    "Le Centre de Formation",
    "Une structure unique dans le Pays Basque, les Landes et le Béarn.",
    "../assets/img/formation/salle.jpg",
)
html += f"""
<main id="main">

  <section class="section">
    <div class="container">
      <div class="split">
        <div class="split__media reveal">
          <img src="../assets/img/formation/batiment.jpg" alt="Le bâtiment du centre de formation Les2L à Mouguerre"
               width="1400" height="1050" loading="lazy" decoding="async">
        </div>
        <div class="split__body reveal" data-delay="1">
          <p>LES2L Centre de Formation –  est une nouvelle structure, unique dans le Pays Basque, les
          Landes et le Béarn, qui propose une <strong>Formation Professionnelle qualifiante
          d’Instructeur PILATES</strong>.</p>
          <p>Entourée d’une équipe riche en expérience et en compétences diversifiées, Laurence Lanté,
          ancienne danseuse professionnelle, enseignant le Pilates depuis 12ans, professeure de Yoga
          et ayant formé plusieurs élèves préprofessionnels en danse classique, vous guidera avec
          sérieux et pédagogie vers la maitrise de la méthode du Pilates authentique.</p>
          <p>L’établissement LES2L est une salle magique avec une vue sur la nature, un véritable bain
          de forêt, à quelques minutes de Bayonne, Biarritz et Hossegor. Tout le matériel se trouve
          disponible sur place. Pendant les pauses, les stagiaires ont accès au sauna, hammam et à la
          piscine.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="container">
      <div class="split split--reverse">
        <div class="split__media reveal">
          <img src="../assets/img/formation/salle.jpg" alt="La salle du centre de formation, vue sur la nature"
               width="1400" height="1012" loading="lazy" decoding="async">
        </div>
        <div class="split__body reveal" data-delay="1">
          <p class="eyebrow">Le cursus</p>
          <h2 class="title">Les modules de formation sont évolutifs&nbsp;:</h2>
          <div class="rule rule--left"><span></span></div>
          <ul>
            <li>MATWORK 1 (50 heures dont 30 en présentiel)</li>
            <li>MATWORK 2 (50 heures dont 30 en présentiel)</li>
            <li>MATWORK 3 (50 heures dont 30 en présentiel)</li>
            <li>PETIT MATERIEL (35 heures dont 15 en présentiel)</li>
            <li>BALLON SWISSBALL (35 heures dont 15 en présentiel)</li>
            <li>WALLUNIT MACHINE (50 heures dont 30 en présentiel)</li>
          </ul>
          <p>Chaque module est composé d’un ou deux week-ends de 15 heures chacun.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="split">
        <div class="split__media reveal">
          <img src="../assets/img/formation/swissball.jpg" alt="Travail sur Swiss Ball pendant la formation"
               width="1400" height="704" loading="lazy" decoding="async">
        </div>
        <div class="split__body reveal" data-delay="1">
          <h2 class="title">Pourquoi se former chez Les2L?</h2>
          <div class="rule rule--left"><span></span></div>
          <p>Parce que la véritable et authentique méthode PILATES, riche et exigeante, nécessite un
          niveau de pédagogie à la hauteur afin de devenir un excellent Instructeur Pilates</p>
          <p>Les stagiaires auront abouti leur formation  complète avec des notions acquises:</p>
          <ul>
            <li>de l’histoire et des fondamentaux de la méthode Joseph Pilates</li>
            <li>des exercices, des variantes et des enchaînements respectueux de son fondateur</li>
            <li>d’anatomie et de prévention des blessures avec un médecin du sport et une kinesthésique</li>
            <li>de pédagogie avec une Professeure en titre</li>
            <li>de business avec un expert comptable</li>
            <li>de l’ouverture possible en Stott Pilates, TRX, Gyrohinesis avec des intervenants
            expérimentés en leur spécificités</li>
          </ul>
          <p>Chaque stagiaire aura en sa possession en fin de formation les outils et les connaissances
          pour enseigner le PILATES, et aura pour base un manuel complet, ainsi que l’accès aux cours
          en visio pendant 3 mois après la formation.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="container">
      <div class="cta-band reveal">
        <img src="../assets/img/formation/logo-formation-blanc.png" alt="LES2L Centre de formation"
             width="500" height="500" loading="lazy">
        <p>Pour faciliter l’accès à ces formations, en cursus complet ou partiel, LES2L centre de
        formation est habilité au financement et à la prise en charge par l’État.</p>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="container container--wide">
      <div class="info-cards">
        <article class="info-card reveal">
          <img src="../assets/img/formation/ico-lieu.png" alt="" width="112" height="112" loading="lazy">
          <h3>Le lieu</h3>
          <p class="subtitle" style="font-size:1.15rem">228 Chemin de Pagadoy<br>Mouguerre 64990</p>
          <p>Un établissement élégant et confortable, avec parking gratuit sur place et accès direct à
          l’autoroute. Vous avez également la possibilité de déjeuner sur place et de profiter
          d’espaces bien-être incluant sauna, hammam, jacuzzi et piscine. Des solutions d’hébergement
          sont disponibles à proximité, ainsi que de nombreux autres avantages.</p>
          <p>Tous les modules sont finançables par l’état (FIFPL, AFDAS, France travail, Conseil
          régional).<br>Possibilité de paiement en 3 ou 4 fois sans frais pour un financement personnel</p>
        </article>

        <article class="info-card reveal" data-delay="1">
          <img src="../assets/img/formation/ico-enseignement.png" alt="" width="112" height="112" loading="lazy">
          <h3>Les pré-requis</h3>
          <ul>
            <li>Être âgé de 18 ans minimum</li>
            <li>Être titulaire de l’un des diplômes suivants : CQP, CQP ALS AGEE, BP JEPS, APT, licence
            STAPS, kinésithérapeute, ostéopathe, de danse (classique, contemporain ou jazz), professeur
            de danse ou professeur de yoga</li>
            <li>Justifier d’une pratique préalable de 20 heures minimum de cours de Pilates Mat au
            moment de l’entrée en formation → Ces heures peuvent être réalisées en présentiel ou en
            visio au sein de la structure LES2L, en amont de la formation choisie</li>
          </ul>
          <p style="text-align:left"><strong>Prérequis spécifiques selon les modules :</strong></p>
          <ul>
            <li>Matwork 2 : être titulaire de la certification niveau 1</li>
            <li>Matwork 3 : être titulaire des certifications niveaux 1 et 2</li>
            <li>Formations Petit matériel, Swissball, Wall Unit : être titulaire des certifications
            Matwork 1, 2 et 3</li>
          </ul>
        </article>

        <article class="info-card reveal" data-delay="2">
          <img src="../assets/img/formation/ico-evaluation.png" alt="" width="112" height="112" loading="lazy">
          <h3>Les évalutations</h3>
          <p>Un contrôle continu est mis en place pendant toute la formation.</p>
          <p>A la fin de chaque module, les stagiaires donneront une séance de 30mn de cours afin
          d’être évalués dans les meilleures conditions.</p>
          <p>Une évaluation écrite précède cette mise en situation.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="container">
      <div class="center" style="margin-bottom:clamp(28px,4vw,44px)">
        <p class="eyebrow">Dates et tarifs</p>
        <h2 class="title">Les modules</h2>
        <div class="rule"><span></span></div>
      </div>
      <div class="track">
{modules}      </div>

      <div class="center" style="margin:clamp(52px,7vw,88px) 0 clamp(28px,4vw,44px)">
        <h2 class="title">Les formations complètes</h2>
        <div class="rule"><span></span></div>
      </div>
      <div class="packs">
{cursus}      </div>
    </div>
  </section>

  <section class="section section--tight center">
    <div class="container">
      <img src="../assets/img/formation/qualiopi.jpg"
           alt="Qualiopi, processus certifié, République Française"
           width="900" height="480" loading="lazy" style="width:min(320px,80%);margin-inline:auto">
      <p style="margin-top:28px">
        <a class="btn" href="../contact/">Demander des informations</a>
      </p>
    </div>
  </section>

</main>
"""
html += c.footer("../")
open("../le-centre-de-formation/index.html", "w", encoding="utf-8").write(html)
print("centre-de-formation.html ok")
