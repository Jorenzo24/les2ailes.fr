# -*- coding: utf-8 -*-
import common as c

# Textes repris mot pour mot des visuels fournis par la cliente (mail « SITE INTERNET »).
D = [
 ("Le Pilates Mat", [
  "Le Pilates Mat, ou Pilates sur tapis, se concentre sur le contrôle du corps, le renforcement du centre, l'amélioration de la flexibilité, de l'équilibre et de la posture, tout en promouvant une respiration correcte.",
  "La pratique régulière du Pilates favorise également une meilleure conscience du corps et une meilleure coordination.",
  "Les exercices sont généralement effectués en séries avec un accent sur la précision , le contrôle et la respiration.",
  "Le Pilates Mat est adapté à tous les niveaux, que vous soyez un débutant complet ou un pratiquant avancé.",
 ], "Explorez le monde du Pilates Mat avec Les2L et ressentez la transformation de votre force, de votre équilibre et de votre flexibilité !"),

 ("Le Pilates Wall Unit", [
  "Le Pilates Wall Unit est une forme de Pilates qui utilise un cadre mural avec des ressorts pour résistance.",
  "Il offre une variété d'exercices de la méthode Pilates qui renforcent le corps, améliorent la posture, augmentent la flexibilité et développent une conscience corporelle accrue.",
  "Le Pilates Wall Unit convient à tous les niveaux, des débutants aux pratiquants avancés.",
  "Il est particulièrement bénéfique pour ceux qui cherchent à améliorer leur force, leur flexibilité et leur posture, ou à ajouter une dimension supplémentaire à leur routine d'entraînement.",
 ], "Rejoignez Les2L pour une séance de Pilates Wall Unit et ressentez l’efficacité d’un entraînement qui engage tout votre corps !"),

 ("Le Pilates en suspension", [
  "Le Pilates en suspension est une variante de la méthode Pilates qui reprend le répertoire des mouvements sur machines ( Cadillac et reformer).",
  "Cette variante est un entraînement fonctionnel afin d’améliorer le mouvement et le fonctionnement du corps en général.",
  "C’est une manière de rendre la pratique plus ludique avec ce challenge de la suspension et du travail de poids du corps.",
  "On va associer un travail d’équilibre, de renforcement des muscles stabilisateurs dû à l’instabilité constante apportée par les sangles mais également un challenge pour le centre du corps avec des positions de gainage dans différents plans de travail dû à la suspension.",
 ], None),

 ("Le Stott Pilates®", [
  "Le STOTT PILATES® est une méthode moderne du Pilates qui respecte les courbures naturelles de la colonne vertébrale et s’appuie sur les connaissances actuelles en biomécanique.",
  ("ul", ["Renforce les muscles profonds", "Améliore la posture", "Développe la mobilité et la souplesse",
          "Soulage les tensions et les douleurs du dos", "Favorise un corps fort, équilibré et fonctionnel"]),
  "Chaque mouvement est réalisé avec précision, contrôle et respiration pour des résultats durables.",
  "Bouger mieux pour se sentir mieux au quotidien.",
 ], None),

 ("Le Yin Yoga", [
  "Le Yin Yoga est une forme de yoga lente et méditative qui met l'accent sur le maintien de postures ou \"asanas\", généralement de 3 à 5 minutes.",
  "Il s'agit d'une pratique douce mais profonde qui cible les tissus conjonctifs du corps pour améliorer la flexibilité et libérer les tensions.",
  "Il permet d’équilibrer le système nerveux, de réduire le stress et l'anxiété, et permet ainsi une plus grande capacité à être présent et conscient. Le Yin Yoga offre de nombreux avantages, tant physiques que mentaux.",
  "Le Yin Yoga est adapté à tous les niveaux de pratique, que vous soyez un débutant absolu ou un yogi expérimenté. C'est une excellente forme de yoga pour ceux qui cherchent à ralentir, à se détendre et à se connecter à leur corps d'une manière douce et respectueuse.",
 ], "Vivez l’expérience du Yin Yoga avec Les2L ! Explorez la tranquillité, le bien-être et la connexion."),

 ("Le Yoga Aérien Restauratif", [
  "Le Yoga Aérien Restauratif est une forme douce de yoga aérien qui utilise un hamac suspendu pour soutenir le corps dans des postures de relaxation profonde.",
  "Il combine les éléments thérapeutiques du yoga traditionnel et du yoga aérien, favorisant un sentiment d’apesanteur qui permet de libérer les tensions de manière plus profonde.",
  "La pratique du Yoga Aérien Restauratif améliore la flexibilité, encourage la détente profonde, soulage le stress et l'anxiété, et favorise un sentiment de bien-être général.",
  "Le soutien du hamac permet également un étirement doux et sécurisé de la colonne vertébrale et des articulations.",
 ], "Rejoignez Les2L pour une expérience de détente et de renouveau avec le Yoga Aérien Restauratif !"),

 ("Le Vinyasa Yoga", [
  "Le Vinyasa Yoga est une forme dynamique et fluide de yoga qui met l'accent sur la coordination du mouvement et de la respiration.",
  "Le terme \"Vinyasa\" signifie \"placer de manière spéciale\" en sanskrit, selon un flux continu de mouvements pour atteindre la capacité à développer la force, la flexibilité, et la concentration.",
  "Chaque posture est liée à la suivante par la respiration, créant ainsi un lien harmonieux entre le corps, le souffle et l'esprit.",
  "Le Vinyasa Yoga convient aux personnes déjà expérimentés en yoga. Grâce à sa nature dynamique et adaptable, il est idéal pour ceux qui aiment la variété, le mouvement, et le défi dans leur pratique du yoga.",
 ], "Embarquez-vous dans une aventure dynamique de Vinyasa Yoga avec Les2L ! Explorez la fluidité, la force et la sérénité intérieure."),

 ("Le Yoga Aérien", [
  "Le Yoga Aérien est une forme innovante de yoga qui intègre un hamac suspendu pour soutenir et améliorer les postures traditionnelles du yoga.",
  "Il offre une combinaison unique de renforcement, d'étirement et de relaxation.",
  "Le Yoga Aérien développe la flexibilité, renforce les muscles, améliore l'équilibre et la coordination, et favoriser la relaxation.",
  "De plus, certaines postures peuvent aider à soulager la tension dans le dos et le cou.",
  "Le hamac permet également de réaliser des inversions sans mettre de pression sur la colonne vertébrale.",
  "Le Yoga Aérien est idéal pour ceux qui cherchent à ajouter un élément ludique et dynamique à leur pratique du yoga",
 ], "Découvrez le monde du Yoga Aérien avec Les2L et ressentez la liberté et le plaisir de bouger dans l’espace tridimensionnel !"),

 ("Le Munz Floor®", [
  "Le Munz Floor® est une méthode douce pratiquée au sol, guidée uniquement par la voix et basée sur des mouvements lents et spiralés.",
  "Elle aide à relâcher les tensions, décompresser la colonne vertébrale et favoriser la récupération du corps.",
  "Particulièrement adaptée :",
  ("ul", ["après une blessure ou une immobilisation,", "en complément d'un suivi thérapeutique,",
          "pour accompagner une pratique sportive ou de bien-être."]),
  "Ses bénéfices :",
  ("checks", ["système nerveux apaisé,", "meilleure mobilité,", "récupération optimisée,", "concentration renforcée."]),
  "Une pratique à la fois douce, profonde et régénérante.",
 ], None),

 ("Danse Classique Adultes", [
  "La Danse Classique pour Adultes est accessible à tous, peu importe l'âge ou le niveau de compétence. Il n’est jamais trop tard pour apprendre à danser !",
  "Cette pratique offre une introduction ou un retour à la beauté et à la discipline du ballet classique.",
  "La pratique de la Danse Classique pour Adultes améliore la posture, la coordination, la flexibilité et la force, développe la grâce et l’élégance.",
  "Elle stimule également l'expression artistique, réduit le stress, contribue à l'amélioration de la santé mentale et développe la confiance en soi.",
  "Une séance typique de Danse Classique pour Adultes comprend un échauffement, des exercices à la barre et au centre, et parfois des séquences de danse plus élaborées.",
  "La Danse Classique pour Adultes est idéale pour ceux qui ont toujours voulu apprendre le ballet ou qui souhaitent reprendre une passion de jeunesse, selon des cours de niveau différent.",
 ], "Venez rejoindre Les2L pour un voyage de beauté et d’expression à travers la Danse Classique pour Adultes !"),

 ("Le Total Barre®", [
  "Le TOTAL BARRE® est un entraînement dynamique inspiré de la danse, du Pilates et du fitness.",
  "Il utilise la barre comme support pour renforcer l’ensemble du corps tout en améliorant l’équilibre, la posture et l’endurance.",
  ("ul", ["Travail complet du corps", "Renforcement musculaire profond", "Élégance et fluidité des mouvements",
          "Cardio et dépense énergétique", "Posture, tonicité et mobilité"]),
  "Une méthode accessible à tous pour se sentir plus fort(e), plus tonique et plus énergique.",
 ], None),

 ("Ballet Sculpt®", [
  "La rencontre parfaite entre la grâce de la danse classique et l’énergie du fitness !",
  "Un cours complet qui fait travailler tout le corps : renforcement musculaire, cardio, posture, équilibre et coordination.",
  "Le tout dans une ambiance dynamique, bienveillante et fun, pour se tonifier tout en dansant et s’amusant .",
 ], None),
]


def block(item):
    if isinstance(item, tuple):
        kind, items = item
        cls = ' class="checks"' if kind == "checks" else ""
        lis = "".join("<li>%s</li>" % x for x in items)
        return "<ul%s>%s</ul>" % (cls, lis)
    return "<p>%s</p>" % item


cards = ""
for i, (name, body, cta) in enumerate(D):
    inner = "\n          ".join(block(b) for b in body)
    cta_html = '\n          <p class="discipline__cta">%s</p>' % cta if cta else ""
    cards += f"""      <article class="discipline reveal" data-delay="{i % 3}">
        <h2 class="discipline__name">{name}</h2>
        <div class="discipline__body">
          {inner}{cta_html}
        </div>
      </article>
"""

html = c.head(
    "Les disciplines de Pilates, Yoga et Ballet | LES 2 L Pays Basque",
    "Découvrez les disciplines enseignées au studio Les2L : Pilates Mat, Wall Unit, en suspension, "
    "Stott Pilates, Yin Yoga, Vinyasa, Yoga Aérien, Munz Floor, Danse Classique, Total Barre et Ballet Sculpt.",
    "https://www.les2ailes.fr/les-disciplines/",
    "../",
)
html += c.header("les-disciplines/", "../")
html += c.pagehead(
    "Prendre soin de soi",
    "Les disciplines",
    "17 disciplines pour prendre soin de votre corps, de votre santé et de votre vie, "
    "pour les sportifs ou sédentaires, débutants ou confirmés, mixte et de tout âge.",
    "../assets/img/gallery/g05.jpg",
)
html += f"""
<main id="main">
  <section class="section">
    <div class="container container--wide">
      <div class="disciplines">
{cards}      </div>
    </div>
  </section>

  <section class="section section--paper section--tight">
    <div class="container center">
      <p class="eyebrow">Passez à la pratique</p>
      <h2 class="title">Trouvez votre cours</h2>
      <div class="rule"><span></span></div>
      <p class="lead" style="max-width:620px;margin-inline:auto">
        Consultez le planning de la saison, découvrez les tarifs ou venez rencontrer l’équipe.
      </p>
      <p style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:26px">
        <a class="btn" href="../planning/">Le planning</a>
        <a class="btn btn--ghost" href="../tarifs/">Les tarifs</a>
      </p>
    </div>
  </section>
</main>
"""
html += c.footer("../")
open("../les-disciplines/index.html", "w", encoding="utf-8").write(html)
print("disciplines.html ok")
