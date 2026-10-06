# CLAUDE.md — Mémoire projet les2ailes.fr (LES 2 L)

> Fichier lu par Claude Code à chaque session. Contexte, décisions verrouillées
> et règles du projet. À respecter strictement. Mettre à jour quand une décision
> structurante change. En cas de doute, demander — ne pas inventer de contenu.

---

## 1. Le projet en une phrase

Refonte **à l'identique** du site du studio **Les2L** (Pilates · Yoga · Ballet),
228 Chemin de Pagadoy, 64990 Mouguerre (Pays Basque), en site **statique**,
avec seulement des améliorations visuelles et d'UX.

- **Cliente** : Laurence Lanté — `les2ailespy@gmail.com` — gérante, ancienne
  danseuse professionnelle, enseigne le Pilates depuis 12 ans.
- **En production** : `https://www.les2ailes.fr/` depuis le 28 septembre 2026,
  serveur cPanel `65.21.136.233`, derrière Cloudflare.
- **Ancien site** : WordPress + Elementor + OceanWP chez OVH mutualisé, remplacé.
  Son hébergement n'est pas résilié : le domaine porte des **MX OVH actifs**.
- **Compte GitHub** : `Jorenzo24` — repo : `github.com/Jorenzo24/les2ailes.fr` (public)
- **GitHub Pages** a servi d'aperçu pendant la refonte. À couper si ce n'est pas
  déjà fait : il ferait doublon avec la production.

---

## 2. Stack technique (décidée — ne pas remettre en cause sans accord explicite)

| Couche | Choix | Statut |
|---|---|---|
| Front | **HTML statique pur** — 1 fichier par page, aucun framework | ✅ |
| CSS | **1 seule feuille** : `assets/css/style.css`, variables CSS, aucun build | ✅ |
| JS | **1 seul fichier** : `assets/js/main.js`, vanilla ES5, aucune dépendance | ✅ |
| Polices | Google Fonts (EB Garamond + Dancing Script) | ✅ |
| Génération | Scripts **Python 3** dans `_build/` (stdlib uniquement) | ✅ |
| Hébergement | **cPanel** `65.21.136.233`, derrière **Cloudflare** | ✅ en prod |
| Back-end | **PHP** pour le seul formulaire de contact (`contact/envoi.php`) | ✅ en prod |

- **Pas de WordPress, pas de framework, pas de npm.** Le site doit rester
  ouvrable en double-cliquant sur `index.html`.
- **Aucune dépendance externe** hors Google Fonts, l'iframe Google Maps de la
  page contact, et PHPMailer, embarqué dans `lib/` pour éviter Composer.
- Un `cp -R` dans `.cpanel.yml` par dossier déployé : **penser à l'y ajouter**
  en créant un nouveau dossier, sinon il ne partira jamais en ligne.

---

## 3. Décisions verrouillées (NE PAS contredire)

1. **Les textes sont repris MOT POUR MOT.** Ne jamais réécrire, résumer,
   corriger l'orthographe ni « améliorer » un texte fourni par la cliente —
   y compris les fautes et coquilles présentes dans les sources
   (ex. « de ka méthode Pilates », « LES ÉVALUTATIONS », « et favoriser la
   relaxation »). Elles sont conservées volontairement.
2. **Toutes les photos des professeures sont en noir et blanc.** Consigne
   explicite de la cliente (mail « Précision site internet »). Les fichiers de
   `assets/img/equipe/` sont déjà convertis en niveaux de gris, ET un
   `filter:grayscale(100%)` est appliqué en CSS (double sécurité).
3. **Bleu marine `#062c5a` + blanc**, repris de l'ancien site. En revanche le
   violet a changé : le `#864c80` d'origine était jugé trop rose par la cliente,
   qui craignait de faire fuir la clientèle masculine. Remplacé le 7 septembre
   2026 par **`#6e4b87`** (violet-indigo), avec `--plum-light:#a08cc4` et
   `--plum-dark:#5a3d70`. Contraste de la teinte claire sur le bleu marine :
   4,65:1 contre 3,75:1 avant. Ne pas revenir vers le magenta.
4. **Les sections et l'ordre du menu sont conservés** tels que sur l'ancien site :
   Disciplines, L'équipe, Planning, Tarifs, Event, Contact,
   Centre de formation professionnelle.
4 bis. **Les URL doivent rester identiques à celles du site actuel.** Chaque page
   est un `index.html` dans un dossier portant le slug WordPress d'origine
   (`/les-disciplines/`, `/les-professionnels/`, `/le-centre-de-formation/`...).
   Ne jamais renommer un dossier : aucune redirection ne doit être nécessaire.
   Conséquence : dans les scripts de `_build/`, les pages en sous-dossier passent
   `base="../"` à `c.head()`, `c.header()` et `c.footer()`, et tous leurs chemins
   d'assets sont préfixés `../`.
   **Exception (7 septembre 2026)** : les pages `/planning/` et `/tarifs/` ont été
   supprimées à la demande de la cliente. Les onglets du menu ouvrent directement
   les PDF, comme sur le site d'origine. Générateurs conservés dans
   `_build/_inactif/` si elle change d'avis.
4 ter. **Pas de marqueurs d'écriture IA.** Interdits dans les textes rédigés par
   Claude : cadratins `—`, points médians `·`, tirets décoratifs en guise de
   ponctuation. Utiliser virgules, deux-points ou `|` dans les balises title.
   Exception : les caractères présents dans les textes d'origine de la cliente
   (ex. le `–` de « LES2L Centre de Formation – est une nouvelle structure »).
5. **`PROD` dans `_build/common.py` pilote l'indexation.** À `False`, toutes les
   pages portent `noindex, nofollow` et `robots.txt` interdit tout ; à `True`,
   l'indexation est ouverte et le sitemap pointe sur le domaine. **Il est à
   `True` depuis la mise en production.** Ne le repasser à `False` que pour
   remonter un aperçu, et ne jamais oublier de le remettre.
6. **Les intitulés de la page Équipe ne se déduisent pas des disciplines.**
   La cliente les a corrigés un par un le 30 septembre 2026 : Lénie n'enseigne
   que le Munz Floor®, Alexandra que le Yoga Aérien pour Enfants, etc. Ne jamais
   les « compléter » d'après les bios ou le planning, ils viennent d'elle.
7. **`_mails/` et `mails.zip` ne sont jamais commités** (photos personnelles des
   professeures + adresses e-mail). Ils sont dans `.gitignore`.

---

## 4. Origine des contenus (important)

Sur l'ancien WordPress, **seules 2 pages avaient du contenu** : l'accueil et
« le centre de formation ». Les pages Disciplines, L'équipe, Planning, Tarifs et
Event étaient **totalement vides** (uniquement le widget d'avis Google du footer).
Tout le reste vient donc des documents de la cliente.

| Page | Source du contenu |
|---|---|
| Accueil | Textes de `les2ailes.fr/` (scrapés) |
| Centre de formation | Textes de `les2ailes.fr/le-centre-de-formation/` (scrapés) |
| Disciplines | **12 visuels** du mail « SITE INTERNET » (`mails.zip`), transcrits en texte réel |
| L'équipe | Mail « Onglet EQUIPE » (7 bios) + mails « Photo N&B … » (7 portraits) |
| Planning | `PLANNING 2026-2027.png` du mail « Planning », retranscrit en tableau HTML, et converti en PDF pour le téléchargement |
| Tarifs | `Tarifs.pdf` du site officiel, retranscrit en cartes HTML |
| Avis | Widget Trustindex/Google de l'ancien site, figés en HTML statique |

`mails.zip` est décompressé dans `_mails/` (non versionné). Les pièces jointes
sont extraites dans `_mails/extracted/<sujet du mail>/`.

---

## 5. Structure du projet

```
les2ailes.fr/
├── index.html                        /
├── les-disciplines/index.html        /les-disciplines/
├── les-professionnels/index.html     /les-professionnels/   (L'équipe)
├── event/index.html                  /event/
├── contact/
│   ├── index.html                    /contact/
│   └── envoi.php                     traitement du formulaire
├── le-centre-de-formation/index.html /le-centre-de-formation/
├── 404.html
├── .htaccess                   redirections, cache, sécurité
├── .cpanel.yml                 tâches de déploiement
├── robots.txt / sitemap.xml
├── assets/
│   ├── css/style.css           feuille unique (tokens en :root)
│   ├── js/main.js              menu, lightbox, reveal, avis, cookies, formulaire
│   ├── img/
│   │   ├── equipe/             8 portraits N&B, 900×1200
│   │   ├── gallery/            15 photos de l'accueil
│   │   ├── formation/          visuels + pictogrammes du centre de formation
│   │   └── hero.jpg, logo.png, logo-blanc.png, ornement.png, cours-prive.jpg…
│   └── docs/                   planning.pdf, tarifs.pdf, events.pdf
├── lib/PHPMailer/              3 fichiers, envoi SMTP du formulaire
├── _build/                     ← GÉNÉRATEURS (voir §6)
│   ├── common.py               données partagées + head / header / footer
│   ├── build_all.py            ← LA commande à lancer
│   ├── build_*.py              un script par page
│   └── _inactif/               générateurs des pages planning et tarifs supprimées
├── _mails/                     ← gitignored (données cliente)
├── mails.zip                   ← gitignored
└── .env                        ← gitignored (identifiants SMTP)
```

**Pas de pages `/planning/` ni `/tarifs/`** : les onglets ouvrent directement
les PDF. Leurs générateurs dorment dans `_build/_inactif/`.

---

## 6. Règles strictes pour Claude Code

1. **Ne jamais éditer les `.html` à la racine directement.** Ils sont générés.
   Toute modification passe par `_build/`, puis :
   ```bash
   cd _build && for f in build_*.py; do python3 "$f"; done
   ```
   Un texte modifié dans le HTML est perdu à la génération suivante.
2. **En-tête, pied de page, menu, `<head>`** : uniquement dans `_build/common.py`.
   Ne jamais dupliquer ces blocs dans un `build_*.py`.
3. **Python 3.9** sur cette machine : pas de backslash dans une expression
   f-string, pas de `match`, pas de syntaxe 3.10+.
4. **Vérifier visuellement** après chaque changement notable, via Chrome headless :
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
     --disable-gpu --hide-scrollbars --window-size=1440,7000 \
     --screenshot=/tmp/p.png --virtual-time-budget=7000 "file://$PWD/index.html"
   ```
   ⚠️ Chrome headless impose une **largeur minimale de 500 px** : impossible de
   tester en 390 px, les captures « mobile » se font à 500.
5. **Optimiser toute nouvelle image** avant commit (Pillow est dispo) :
   galerie ≤ 1100 px de large, photos pleine largeur ≤ 1400, hero ≤ 1920,
   portraits 900×1200 en niveaux de gris, JPEG qualité 84-86 progressif.
6. **Ne rien inventer.** S'il manque un contenu (voir §13), le signaler à Joseph
   plutôt que de rédiger un texte de remplacement.

---

## 7. Git & déploiement

**Mise en ligne** : la procédure complète est dans [MIGRATION.md](MIGRATION.md).
Points à retenir :

- `PROD` dans `_build/common.py` pilote le `noindex`, `robots.txt` et le
  sitemap. `False` = aperçu, `True` = production. Après changement :
  `cd _build && python3 build_all.py`.
- `build_all.py` régénère **tout** (pages + robots + sitemap). C'est la
  commande à utiliser, pas les `build_*.py` un par un.
- Le domaine reste canonique sur **www**, contrairement aux autres projets :
  c'est ce que Google a indexé.
- ⚠️ Le domaine porte des **MX OVH actifs**. On ne modifie que les
  enregistrements A. Ne jamais toucher aux NS, MX ou SPF.
- Branche unique : `main`. Push direct, pas de PR sur ce projet.

### Le déploiement n'est pas automatique

Pousser sur GitHub **ne met rien en ligne**. Il faut, dans cPanel →
Git™ Version Control → onglet Pull or Deploy :

1. **Update from Remote** (récupère le dernier commit)
2. **Deploy HEAD Commit** (exécute `.cpanel.yml`)

Le dépôt est cloné dans `/home/les2ailes/repositories/les2ailes.fr`, **pas dans
`public_html`** : `.cpanel.yml` y copie les fichiers, ce qui garde `.git/`,
`_build/` et `CLAUDE.md` hors du web.

### Vérifier après déploiement

```bash
# la page sert bien la dernière version
diff <(curl -s https://www.les2ailes.fr/) index.html >/dev/null && echo "à jour"

# les redirections depuis l'ancien WordPress
for u in "" les-disciplines/ planning/ tarifs/ wp-login.php nawak/; do
  printf "%-22s %s\n" "/$u" "$(curl -s -o /dev/null -w '%{http_code}' "https://www.les2ailes.fr/$u")"
done
```

Attendu : `200` sur les pages, `301` sur planning et tarifs, `410` sur
`wp-login.php`, `404` sur une URL bidon.

### Si une modification n'apparaît pas en ligne

C'est **presque toujours le cache Cloudflare**, pas le déploiement. Vérifier
l'en-tête `cf-cache-status`. Tout ce qui est servi porte une empreinte de
version (voir plus bas) : si un fichier modifié garde la même URL, c'est que
`build_all.py` n'a pas été relancé.

---

## 8. Typographie

| Usage | Police |
|---|---|
| Titres et textes courants | **EB Garamond** |
| Accents manuscrits (`.eyebrow`, `.hero__place`, `.discipline__name`, `.discipline__cta`, `.member__role`) | **Dancing Script** |

Décision du 7 septembre 2026 : **Alex Brush est abandonnée** (police de l'ancien
site, jugée illisible par Joseph) et remplacée partout par Dancing Script, plus
lisible. Elle n'est plus chargée depuis Google Fonts.

Dancing Script ayant une hauteur d'x plus grande, les tailles des éléments
manuscrits ont été réduites et passées en graisse 600. Ne pas les remonter aux
valeurs d'origine sans revoir l'ensemble.

---

## 9. Le centre de formation est en couleurs inversées

À la demande de la cliente, `/le-centre-de-formation/` est **entièrement sur
fond bleu marine** pour le distinguer du reste du site. C'est le rôle de
`<body class="theme-navy">` : toutes les surcharges sont regroupées dans
`style.css` sous « Page inversée (centre de formation) ».

Son bandeau de page est un cas particulier : `c.pagehead(..., h1="eyebrow")`.
Le `<h1>` est le **petit sur-titre violet** « Formation Instructeur Pilates »,
pour le mot-clé, et le gros titre « Le Centre de Formation » n'est plus qu'un
`<p class="pagehead__display">`. Une seule balise h1 sur la page, et le visuel
reste celui d'origine.

Points d'attention si on ajoute un bloc à cette page :
- les cartes deviennent `rgba(255,255,255,.055)` avec bordure translucide ;
- la carte mise en avant (`.pack--highlight`) s'inverse à son tour, en blanc ;
- les pictogrammes noirs passent en `filter:brightness(0) invert(1)` ;
- un logo sur fond blanc opaque (Qualiopi) doit être posé dans `.logo-card`,
  sinon il forme un bloc blanc disgracieux ;
- les boutons pleins passent en `--plum-light` sur texte bleu marine, sinon ils
  ne ressortent pas.

---

## 10. Partis pris, page par page

### Les ateliers de la page Events

`ATELIERS` dans `_build/build_event_contact.py` reprend mot pour mot le PDF
« ATELIERS 2026-2027 ». Les six dates ont été vérifiées : elles tombent toutes
un dimanche.

Chaque atelier dure 1 h 30, sauf la Danse aérienne qui dure 2 h. Le dictionnaire
`LIENS` associe une durée à un lien de paiement Stripe. **Tant qu'un lien est
vide, le bouton « Réserver » ne s'affiche pas** : il suffit de renseigner
`STRIPE_ATELIER_1H30` et `STRIPE_ATELIER_2H` dans `common.py` pour que les six
boutons apparaissent.

La cliente voulait mettre les liens de paiement dans le PDF. On a fait
l'inverse : le PDF reste un document d'affichage, et la page porte les boutons.
Un lien dans un PDF ne se met pas à jour et se clique mal sur mobile.

---

### Sessions de formation : la source de vérité

`MODULES` dans `_build/build_formation.py` liste **les sessions**, pas les
modules : plusieurs sessions peuvent porter le même intitulé (une session
classique et une session intensive de MATWORK 3, par exemple). Elles sont
rangées dans **l'ordre chronologique du tout**, comme la cliente l'a demandé
le 28/09/2026.

Chaque entrée est `(intitulé, public, dates, tarifs, mention)`. Un `tarifs`
vide affiche « Nous consulter » : c'est le cas des 5 sessions intensives, dont
**les prix n'ont pas été communiqués**. La `mention` sert au badge
« Possibilité d'hébergement ».

---

### Tout ce qui est servi porte une empreinte de version

CSS, JS, PDF **et images**. Sans ça, remplacer un fichier sans changer son nom
ne change pas son URL, et Cloudflare continue de servir l'ancien jusqu'à un an.
C'est arrivé trois fois : le CSS du pot de miel, le planning corrigé, puis
l'icône des évaluations restée blanche alors qu'elle était détourée.

- CSS et JS : `V_CSS` / `V_JS` dans `common.py`
- PDF : l'empreinte est intégrée à `PLANNING_PDF`, `TARIFS_PDF`, `EVENT_PDF`
- **images** : ajoutées automatiquement par `build_all.py`, en post-traitement
  du HTML généré. Rien à faire dans les gabarits.

Conséquence : **toujours passer par `build_all.py`**, jamais par les
`build_*.py` un par un, sinon les images perdent leur empreinte.

---

### Le module d'avis est dans le pied de page

Depuis le 28 septembre 2026, le carrousel d'avis Google est produit par
`c.reviews_band()` dans `common.py` et injecté **en tête du pied de page**,
donc sur **toutes les pages**. Il n'y a plus de section d'avis sur l'accueil.

Il reproduit le widget Trustindex de l'ancien site : cartes blanches
arrondies, avatar rond qui déborde en haut avec la pastille Google, nom, date
relative, étoiles dorées et badge vérifié bleu, texte centré, « Lire la suite »,
flèches sur les côtés et pastilles.

Deux partis pris :

- **Pas de photos de profil.** Le widget d'origine affichait les photos Google
  des auteurs, hébergées sur `lh3.googleusercontent.com`. Les réhéberger poserait
  un problème de données personnelles et les URL expirent. Les avatars sont donc
  des initiales sur un rond de la charte (5 teintes en rotation via `data-i`).
- **Les dates sont calculées en JS** à partir de l'horodatage Unix de chaque
  avis (`data-ts`), relevé dans le widget de l'ancien site. « il y a 9 mois »
  reste donc juste avec le temps, sans rien à maintenir.

Les 9 avis sont figés dans `REVIEWS` (`common.py`). Il n'y a **aucun appel à
l'API Google** : si la cliente en obtient de nouveaux, il faut les ajouter à la
main dans cette liste.

---

### « Le lieu » : pas de calque sur la photo

Décision de la cliente le 29 septembre 2026, après essai dans les deux sens.
Elle a d'abord demandé le texte **sur** la photo, comme sur l'ancien site, puis
a tranché l'inverse : « c'est beaucoup trop sombre, il ne faut pas de calque sur
la photo », et « autant mieux remettre le texte à part car c'est la plus belle
photo ».

Le bloc est donc un `.photoband` pleine largeur, **sans aucun voile**, suivi du
titre et du texte en dessous. Ne pas y remettre de calque : c'est un arbitrage
tranché, pas un oubli.

---

### L'ornement vient de ses PDF

`assets/img/ornement.png` est l'arabesque de ses documents, extraite du PDF de
planning puis détourée :

```bash
sips -s format png --resampleHeightWidthMax 3000 assets/docs/planning.pdf --out /tmp/plan.png
# puis crop + blanc rendu transparent avec Pillow
```

Elle coiffe chaque encadré de `/les-disciplines/`, refaits le 26 septembre 2026
d'après le feed Instagram de la cliente : double filet (bordure extérieure plus
`::before` en retrait de 8px), angles droits, pas d'ombre, ornement centré,
titre manuscrit et filet de séparation. Le corps du texte reste aligné à gauche,
ses visuels ne portent que deux lignes quand nos fiches en portent quinze.

---

### Le bloc « fondatrice » de la page équipe

La bio de Laurence Lanté, reçue le 24 septembre 2026, vient de sa publication
Instagram. Elle pose deux problèmes que la mise en page résout :

- elle est **à la première personne** (« Après une carrière de ballerine… je me
  consacre… »), alors que les 7 fiches du mail « Onglet EQUIPE » sont à la
  troisième (« HELEN WATKINS est enseignante… ») ;
- elle fait **7 paragraphes** contre 3 ou 4 pour les autres.

Plutôt que de la réécrire (règle du mot pour mot) ou de la comprimer dans une
carte, elle a son propre bloc `.founder` en tête de `/les-professionnels/` :
grille asymétrique photo / texte, label « Fondatrice », filet 1px, cadre décalé
sur la photo. La première personne y devient cohérente, on lit une parole de
fondatrice. Les 7 professeures suivent dans la grille `.team`, sous un intitulé
`.section-label`, sur fond `--paper-warm`.

Les deux colonnes du bloc fondatrice font **exactement la même hauteur** :
`align-items:stretch` sur la grille, puis `height:100%` + `object-fit:cover`
sur la photo, qui se recadre donc à la volée sur la hauteur du texte. Le ratio
de colonnes `.88fr / 1.12fr` est calé pour qu'à largeur confortable le
recadrage soit quasi nul. En dessous de **1000 px** on empile et la photo
retrouve son ratio naturel : plus bas, l'étirement la réduirait à une bande.

Deux structures différentes qui se suivent, c'est voulu : le bloc fondatrice
est horizontal et pleine largeur, les fiches sont des cartes verticales en
3 colonnes (`max-width:1180px`). Ne pas passer la grille en 4 colonnes, les
fiches deviennent des colonnes de texte trop étroites.

---

### Les couleurs viennent des PDF de la cliente

Le 14 septembre 2026, la cliente a autorisé à piocher dans les couleurs de ses
PDF. Palette relevée automatiquement sur `assets/docs/tarifs.pdf` et
`assets/docs/planning.pdf`, avec le contraste sur le bleu marine `#062c5a` :

| Hex | Où, dans ses documents | Contraste |
|---|---|---|
| `#e5dae3` | lilas pâle du planning | 10,21:1 |
| `#ddd7d0` | blocs Zoom / Carte / Modalités du PDF tarifs | 9,70:1 |
| `#acb7d8` | lavande du planning | 6,94:1 |
| `#bea4bb` | mauve clair du planning | 6,08:1 |
| `#7f8ec0` | bloc Solaire du PDF tarifs | 4,31:1 |
| `#967297` | bloc Galaxie du PDF tarifs | 3,40:1 |
| `#54305a`, `#361d3b`, `#293c77`, `#03053b` | teintes foncées | < 1,5:1, **inutilisables sur le bleu marine** |

Trois teintes sont désormais en service sur `/le-centre-de-formation/` :
`--sand:#ddd7d0` pour les formations complètes et les cartes Le lieu /
Pré-requis / Évaluations, `--prune:#54305a` pour les modules, `--aubergine:#361d3b`
pour le filet du cursus complet. Le prune a un contraste faible sur le bleu
marine (1,28:1) mais s'en détache par la teinte, comme les blocs de ses PDF.

« Les formations complètes » utilise le **beige `#ddd7d0`** : le meilleur
contraste de la palette avec le blanc exclu, chaud face au bleu froid, et la
seule teinte claire qui ne tire pas vers le rose (la cliente y est attentive).
Le cursus complet se distingue par un filet supérieur et un titre en aubergine
`#361d3b`.

**Deux taupes, deux usages.** `--sand` (`#ddd7d0`) sert de **fond de carte** :
sur le bleu marine il ressort à 9,7:1. Mais en **texte** il ne fait que 1,4:1
face au blanc, donc on le prend pour du blanc sali. D'où `--taupe` (`#9c9893`),
celui des blocs Munz Floor et Bodyflow du planning : 4,83:1 sur le marine et
2,87:1 face au blanc, il se lit comme une vraie couleur. Ne pas intervertir.

Pour refaire l'extraction après une mise à jour des PDF :
`sips -s format png assets/docs/tarifs.pdf --out /tmp/t.png`, puis un comptage
de couleurs avec Pillow en écartant le blanc.


---

## 11. Le formulaire de contact

Envoi par **SMTP authentifié**, via PHPMailer embarqué dans `lib/PHPMailer/`
(3 fichiers, pas de Composer). Le traitement est dans `contact/envoi.php`.

**Les identifiants ne sont jamais dans le dépôt : il est public.** Ils vivent
dans un `.env` que `envoi.php` cherche dans cet ordre :

1. `/home/les2ailes/.env` — **hors de `public_html`**, c'est l'emplacement voulu
2. la racine du site, en secours

`.env` est dans `.gitignore`, `.env.example` sert de modèle, et le `.htaccess`
le bloque en plus (ceinture et bretelles).

Le formulaire marche **avec et sans JavaScript** : `main.js` intercepte l'envoi
et fait un `fetch`, mais l'attribut `action` du formulaire suffit à lui seul,
`envoi.php` renvoyant alors sur `/contact/?envoi=ok` ou `?envoi=erreur`.

Protections : pot de miel (`name="website"`, masqué en CSS), validation
serveur, refus des retours à la ligne dans les en-têtes, et une limite d'un
envoi toutes les 30 secondes par IP.

Le destinataire est `les2ailespy@gmail.com`, l'expéditeur technique
`noreply@startmailapp.com`, et le `Reply-To` est l'adresse du visiteur : la
cliente répond directement depuis Gmail.

---

## 12. État d'avancement (maj 2026-10-06)

### Le site est **en production** depuis le 28 septembre 2026

`https://www.les2ailes.fr` sert le site statique, sur le serveur cPanel
`65.21.136.233`, derrière Cloudflare. Le WordPress OVH a été remplacé.
Détail de la bascule dans [MIGRATION.md](MIGRATION.md).

Vérifié au moment de la bascule : les 6 pages en 200, `/planning/` et `/tarifs/`
en 301 vers leur PDF, les reliquats WordPress en 410, `les2ailes.fr` → `www`,
`http` → `https`, aucun `noindex`, et `/CLAUDE.md`, `/.git/config`, `/_build/`
en 403. **Zéro 404 entre l'ancien et le nouveau site.**

**Responsive** : 0 débordement horizontal sur toutes les pages à 500, 768, 1024
et 1440 px (`scrollWidth == clientWidth`). Les grilles utilisent
`minmax(min(Xpx,100%),1fr)` pour tenir jusqu'à 320 px.
⚠️ Chrome headless refusant de descendre sous 500 px, les largeurs 320-390 px
n'ont jamais pu être testées automatiquement.

### Les documents sont des PDF fournis par la cliente

`assets/docs/planning.pdf`, `tarifs.pdf` et `events.pdf` viennent directement
d'elle. Pour les mettre à jour : **remplacer le fichier, relancer `build_all.py`,
committer**. L'empreinte de version change toute seule, donc pas de purge de
cache à faire.

⚠️ La **grille tarifaire a entièrement changé** pour 2026-2027. L'ancienne
(Liberté / Challenge / Zoom, cours à l'unité 25 €, inscription 50 €) est
caduque. La nouvelle est en formules **Solaire, Lunaire, Étoile, Galaxie**, plus
des **Constellations**, Zoom, Kids Yoga Aérien, Cours Privés, Carte et Modalités.
L'onglet Tarifs ouvrant le PDF, aucune page n'a eu à être retouchée — mais **si
une page de tarifs HTML est un jour réactivée depuis `_build/_inactif/`, tout son
contenu est à refaire**.

**Page planning** : supprimée le 7 septembre 2026, l'onglet ouvre le PDF.
Le tableau HTML responsive reste disponible dans `_build/_inactif/`.

**Les 12 pièces jointes « disciplines »** du mail sont des **cartes de texte**
(75 à 90 % de blanc pur, saturation quasi nulle), pas des photos. Leur contenu
est intégralement retranscrit en HTML : les republier ferait doublon, et du
texte en image serait illisible pour Google et les lecteurs d'écran.

### Les trois liens de paiement Stripe

Dans `common.py`. Ce sont **trois produits distincts**, ne pas les confondre :

| Constante | Usage | Où |
|---|---|---|
| `STRIPE_COURS_1H` | cours à l'unité, « ceux qui viennent en touriste » | bande de l'accueil |
| `STRIPE_ATELIER_1H30` | 5 ateliers du dimanche | `/event/` |
| `STRIPE_ATELIER_2H` | la danse aérienne, seule à durer 2 h | `/event/` |

Sur `/event/`, c'est la **durée de l'atelier** qui choisit le lien
(dictionnaire `LIENS`). Un nouvel atelier prendra donc le bon tout seul.

⚠️ La bande « De passage au Pays Basque ? » de l'accueil est **mon initiative**,
pas une demande de la cliente, et son texte n'est pas d'elle. Elle a relu le
site sans la relever. À reposer si l'occasion se présente.

### Ajouter des avis Google

`REVIEWS` dans `common.py` : `(nom, horodatage unix, note, texte)`. La liste
est **triée automatiquement du plus récent au plus ancien**, donc l'ordre de
saisie n'a pas d'importance.

- **Vérifier les doublons avant d'ajouter.** Sur un lot de 5 reçus le
  30/09/2026, 3 étaient déjà en ligne.
- **Google ne se laisse pas lire automatiquement** : page entièrement en
  JavaScript et mur de consentement européen. Testé, y compris en pilotant un
  vrai navigateur. Il faut des captures d'écran, ou brancher l'API Google
  Places (clé Google Cloud, gratuit sous 5 000 requêtes/mois).
- L'horodatage se déduit du « il y a N jours / mois » affiché par Google.
  19 avis au 30 septembre 2026.

---

## 13. En attente de la cliente

| # | Manque | Détail |
|---|---|---|
| 1 | **3 avis Google** | Sur les 11 noms de son mail, Sabrina, Marilyn et LTN manquent encore |
| 2 | **1 photo pour la page Events** | Celle des « Ateliers, masterclass & stages ». En attendant elle a choisi de garder `g02.jpg`, la femme à l'envers. Repéré par un `TODO cliente` dans `build_event_contact.py` |
| 3 | **Fiches de disciplines manquantes** | Elle a fourni 12 fiches ; l'accueil en cite d'autres : Yoga Kundalini, Yoga Nidra, Bain Sonore, Pilates Reformer, coaching du danseur préprofessionnel |
| 4 | **Cohérence du bain sonore** | Il est dans les 17 disciplines de l'accueil et existe comme atelier du 21 mars, mais il a disparu du planning hebdomadaire |
| 5 | **« finançables par l'état »** | Elle a demandé « l'État » → « les OPCO » pour le bandeau de financement. La carte « Le lieu » garde « finançables par l'état (FIFPL, AFDAS, France travail, Conseil régional) », qui liste des financeurs précis. À trancher |
| 6 | **Pré-requis, formulation** | Sa correction « il manque professeur avant de danse » créait un doublon avec le « professeur de danse » qui suivait. Le second a été retiré. À faire valider |
| 7 | **Nouveaux intervenants** | Melissa Delattre, Sabine Sandri, Benjamin et Itziar Mendivil animent des ateliers mais ne sont pas sur la page Équipe. Volontaire ? |

## 14. Chantiers reportés

- **La refonte en deux onglets.** Elle veut séparer « Les cours » et « Le centre
  de formation », qui va prendre de l'ampleur. Reporté d'un commun accord à
  **fin octobre 2026**, pour laisser Google digérer la migration. En attendant,
  les deux boutons du hero donnent déjà l'accès direct qu'elle demandait.
  Ce ne sera pas qu'un changement de menu : il faudra une vraie page d'accueil
  pour la formation, avec ses sous-pages.
- **AutoSSL et `Full (strict)`.** Cloudflare est en `Full`, ce qui fonctionne.
  Passer en `Full (strict)` une fois le certificat d'origine émis.
- **Search Console.** Soumettre `sitemap.xml`, supprimer l'ancien
  `wp-sitemap.xml`, surveiller la couverture.
- **Ne rien résilier chez OVH** tant que la question des mails n'est pas
  tranchée : le domaine porte des **MX OVH actifs**, et chez OVH la messagerie
  est souvent adossée au pack d'hébergement web.
