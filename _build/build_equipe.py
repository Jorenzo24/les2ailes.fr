# -*- coding: utf-8 -*-
import common as c

# Textes repris mot pour mot du mail « Onglet EQUIPE ».
T = [
 ("HELEN WATKINS", "Yoga", "helen-watkins.jpg", "@lnwatkins", "https://www.instagram.com/lnwatkins/", [
  "HELEN WATKINS @lnwatkins est enseignante et formatrice de Yoga.",
  "Son approche tout en douceur saura séduire les élèves en quête de reconnection à eux-même.",
  "Ses cours sont une vraie expérience holistique, pensés en fonction des saisons, des méridiens de la médecine chinoise et parfois accompagnés de sono thérapie.",
  "Si vous aimez les voyages introspectifs, la voix douce d’Helen saura apaiser votre cœur, votre corps, et votre esprit.",
 ]),
 ("EMILIE LANGLET", "Pilates", "emilie-langlet.jpg", None, None, [
  "Diplômé d’État dans les métiers de la remise en forme et titulaire d’une licence Staps, Emilie a découvert le Pilates lors de son cursus universitaire.",
  "Après de graves blessures et de longs mois de rééducation, la méthode Pilates est devenue comme une évidence dans la prise de conscience de soi, de se réapproprier son corps et dans le développement personnel.",
  "Le mouvement c’est la vie. Le corps en mouvement la fascine et soucieuse de l’intégrité physique de la personne, son objectif dans son enseignement et sa pédagogie est que chaque pratiquant puisse se découvrir ou se redécouvrir.",
  "Formée à la méthode Pilates en Mat et sur Reformer /Cadillac depuis plus de 10 ans ainsi qu’à la méthode PSM ( Pilates en suspension), Emilie intervient depuis début septembre 2025 au sein du studio Les2L.",
 ]),
 ("CAROLINE ROBERT", "Danse classique", "caroline-robert.jpg", None, None, [
  "CAROLINE ROBERT débute sa formation à l’École de l’Opéra national de Paris en 1992 avant d’intégrer le Corps de Ballet en 1998. Nommée Coryphée en 2008 puis Sujet en 2012, elle construit un parcours riche et exigeant au sein de la compagnie.",
  "Artiste à la palette étendue, elle interprète aussi bien les grands ballets du répertoire classique que des œuvres contemporaines majeures signées par des chorégraphes de renom. Elle incarne des rôles variés et marquants, tout en participant à plusieurs créations à l’Opéra de Paris, affirmant ainsi sa polyvalence et sa sensibilité artistique.",
  "Elle participe également à plusieurs créations et se produit à l’international.",
  "Aujourd’hui, après une belle carrière sur scène, Caroline Robert souhaite transmettre ce que la danse lui a apporté : la rigueur, la joie, la confiance et le goût du partage. Avec bienveillance et sincérité, elle accompagne les jeunes danseurs dans leur propre chemin artistique",
 ]),
 ("ALEXANDRA STRZEMPA", "Yoga & FlyYoga", "alexandra-strzempa.jpg", "@uhainayoga", "https://www.instagram.com/uhainayoga/", [
  "ALEXANDRA STRZEMPA @uhainayoga est Professeure de Yoga depuis 10 ans sur la Côte Basque et formée à la méthode FlyYoga en 2016, sa pratique est dynamique et créative alliant engagement et lâcher prise.",
  "Son credo est un corps souple, fort et endurant pour maintenir une bonne santé physique et émotionnelle avec joie, légèreté et bonne humeur.",
  "Son mantra : prends soin de ton corps pour que ton âme ait envie d’y rester. Elle accompagne chacun à apprivoiser son corps pour trouver l’équilibre, l’harmonie et tenir la posture juste.",
 ]),
 ("LÉNIE CHERINO", "Munz Floor® & Yoga Vinyasa", "lenie-cherino.jpg", None, None, [
  "Lénie Cherino, coach certifiée en MUNZ FLOOR®, enseignante de Yoga Vinyasa et praticienne en massage traditionnel Thaïlandais et Amma assis.",
  "Du théâtre à la danse contemporaine et jazz, le long d'une carrière de vingt ans d'artiste interprète, du yoga au massage, en passant par diverses approches somatiques, Lenie est fascinée par l’alchimie subtile qui relie geste, voix, souffle, toucher et émotion. Depuis qu'elle est jeune adulte, le yoga est pour elle un allié précieux, un chemin d’introspection qui ne cesse de lui ouvrir de nouvelles perspectives.",
 ]),
 ("LAUREEN ELISABETH", "Stott Pilates® & Danse", "laureen-elisabeth.jpg", "@laureen_pilates_danse", "https://www.instagram.com/laureen_pilates_danse/", [
  "LAUREEN ELISABETH @laureen_pilates_danse est Chorégraphe, Professeure de danse technique Martha Graham et Professeure de Pilates certifiée STOTT Pilates.",
  "Elle se forme à la danse à Paris puis à New York à la Martha Graham School of Contemporary Dance. C’est là qu’elle découvre le Pilates.",
  "Pendant sa carrière de danseuse elle se forme au Pilates méthode STOTT et l’enseigne depuis.",
 ]),
 ("SARAH ACHTE", "Pilates & Bodyflow", "sarah-achte.jpg", "@sarohnoixdecoco", "https://www.instagram.com/sarohnoixdecoco/", [
  "SARAH ACHTE @sarohnoixdecoco est diplômée d'un BTS Diététique d'abord puis d'un BPJEPS AF. Elle a complété sa formation initiale avec plusieurs modules de ka méthode Pilates avec et sans matériel. Elle aime approfondir et décliner les mouvements fondamentaux de la méthode Pilates en les rendant accessibles à tous les niveaux de pratique. Sarah est aussi certifiée en Hypnose Ericksonienne et en massage Suédois/Deep Tissue.",
 ]),
]

cards = ""
for i, (name, role, photo, handle, handle_url, bio) in enumerate(T):
    paras = "\n            ".join("<p>%s</p>" % p for p in bio)
    if handle:
        link = f"""
          <a class="member__handle" href="{handle_url}" target="_blank" rel="noopener">{c.IC_IG}{handle}</a>"""
    else:
        link = ""
    cards += f"""      <article class="member reveal" data-delay="{i % 3}">
        <div class="member__photo">
          <img src="assets/img/equipe/{photo}" alt="{name.title()}, professeure au studio Les2L"
               width="900" height="1200" loading="lazy" decoding="async">
        </div>
        <div class="member__body">
          <h2 class="member__name">{name}</h2>
          <p class="member__role">{role}</p>
          <div class="member__bio">
            {paras}
          </div>{link}
        </div>
      </article>
"""

html = c.head(
    "L’équipe — 8 professeures qualifiées | LES 2 L Pays Basque",
    "Rencontrez l’équipe du studio Les2L : des professeures qualifiées, certifiées, diplômées et "
    "expérimentées en Pilates, Yoga, Munz Floor et Danse Classique.",
    "https://www.les2ailes.fr/les-professionnels/",
)
html += c.header("equipe.html")
html += c.pagehead(
    "Faites connaissance",
    "L’équipe",
    "Une équipe de 8 Professeures qualifiées, certifiées, diplômées, expérimentées vous accueille "
    "tout au long de l’année.",
    "assets/img/barre-ballet.jpg",
)
html += f"""
<main id="main">
  <section class="section">
    <div class="container container--wide">
      <div class="team">
{cards}      </div>
    </div>
  </section>

  <section class="section section--paper section--tight">
    <div class="container center">
      <p class="eyebrow">Envie d’essayer&nbsp;?</p>
      <h2 class="title">Venez seul ou accompagné&nbsp;!</h2>
      <div class="rule"><span></span></div>
      <p style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:6px">
        <a class="btn" href="planning.html">Voir le planning</a>
        <a class="btn btn--ghost" href="contact.html">Nous contacter</a>
      </p>
    </div>
  </section>
</main>
"""
html += c.footer()
open("../equipe.html", "w", encoding="utf-8").write(html)
print("equipe.html ok")
