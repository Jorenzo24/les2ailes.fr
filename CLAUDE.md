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
- **Ancien site** : `https://www.les2ailes.fr/` — WordPress + Elementor + OceanWP.
  **Toujours en ligne**, il reste la référence tant que la bascule n'est pas faite.
- **Compte GitHub** : `Jorenzo24` — repo : `github.com/Jorenzo24/les2ailes.fr` (public)
- **Aperçu en ligne** : `https://jorenzo24.github.io/les2ailes.fr/` (GitHub Pages, branche `main`, racine `/`)

---

## 2. Stack technique (décidée — ne pas remettre en cause sans accord explicite)

| Couche | Choix | Statut |
|---|---|---|
| Front | **HTML statique pur** — 1 fichier par page, aucun framework | ✅ |
| CSS | **1 seule feuille** : `assets/css/style.css`, variables CSS, aucun build | ✅ |
| JS | **1 seul fichier** : `assets/js/main.js`, vanilla ES5, aucune dépendance | ✅ |
| Polices | Google Fonts (EB Garamond + Dancing Script) | ✅ |
| Génération | Scripts **Python 3** dans `_build/` (stdlib uniquement) | ✅ |
| Hébergement | **GitHub Pages** (aperçu) — cible finale à décider avec la cliente | ✅ aperçu |

- **Pas de WordPress, pas de framework, pas de npm.** Le site doit rester
  ouvrable en double-cliquant sur `index.html`.
- **Aucune dépendance externe** hors Google Fonts et l'iframe Google Maps de la
  page contact.

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
3. **Les couleurs de la charte ne changent pas** : bleu marine `#062c5a`,
   prune `#864c80`, blanc. Reprises de l'ancien site.
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
4 ter. **Pas de marqueurs d'écriture IA.** Interdits dans les textes rédigés par
   Claude : cadratins `—`, points médians `·`, tirets décoratifs en guise de
   ponctuation. Utiliser virgules, deux-points ou `|` dans les balises title.
   Exception : les caractères présents dans les textes d'origine de la cliente
   (ex. le `–` de « LES2L Centre de Formation – est une nouvelle structure »).
5. **Tant que le site est en aperçu** : `<meta name="robots" content="noindex, nofollow">`
   sur toutes les pages + `robots.txt` en `Disallow: /`. Le site ne doit pas
   concurrencer `les2ailes.fr` dans Google.
6. **`_mails/` et `mails.zip` ne sont jamais commités** (photos personnelles des
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
├── planning/index.html               /planning/
├── tarifs/index.html                 /tarifs/
├── event/index.html                  /event/
├── contact/index.html                /contact/
├── le-centre-de-formation/index.html /le-centre-de-formation/
├── 404.html
├── robots.txt / sitemap.xml / .nojekyll
├── assets/
│   ├── css/style.css           feuille unique (tokens en :root)
│   ├── js/main.js              menu mobile, lightbox, reveal, cookies, formulaire
│   ├── img/
│   │   ├── equipe/             7 portraits N&B, 900×1200
│   │   ├── gallery/            g01…g18.jpg (galerie accueil)
│   │   ├── formation/          visuels + icônes du centre de formation
│   │   ├── hero.jpg, logo.png, logo-blanc.png, planning-2026-2027.jpg…
│   └── docs/                   tarifs.pdf, planning.pdf
├── _build/                     ← GÉNÉRATEURS (voir §6)
│   ├── common.py               head / header / footer / pagehead partagés
│   └── build_*.py              un script par page
├── _mails/                     ← gitignored (données cliente)
└── mails.zip                   ← gitignored
```

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
6. **Ne rien inventer.** S'il manque un contenu (voir §8), le signaler à Joseph
   plutôt que de rédiger un texte de remplacement.

---

## 7. Git & déploiement

- Branche unique : `main`. Push direct, pas de PR sur ce projet.
- GitHub Pages est branché sur `main` / racine — **chaque push redéploie**
  automatiquement en ~1 min.
- `.nojekyll` est présent : les dossiers `_build/` et les fichiers commençant par
  `_` sont donc servis tels quels (sans lui, Jekyll les ignorerait).
- Vérifier après déploiement :
  ```bash
  curl -s -o /dev/null -w "%{http_code}\n" https://jorenzo24.github.io/les2ailes.fr/
  ```

---

## 7 bis. Typographie

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

## 8. État d'avancement (maj 2026-09-07)

**Fait :** les 8 pages + 404, URL identiques au site actuel, charte,
accessibilité (skip-link, `aria-current`, focus visibles,
`prefers-reduced-motion`), SEO (meta, canonical, Open Graph, JSON-LD
`SportsActivityLocation`), images optimisées, aperçu en ligne sur GitHub Pages.

**Responsive vérifié** : 0 débordement horizontal sur les 9 pages à 500, 768 et
1024 px (`scrollWidth == clientWidth`). Les grilles utilisent
`minmax(min(Xpx,100%),1fr)` pour tenir jusqu'à 320 px. Seul le tableau du
planning dépasse volontairement, dans un conteneur `.table-scroll`
(`overflow-x:auto`). ⚠️ Chrome headless refusant de descendre sous 500 px, les
largeurs 320-390 px n'ont pas pu être testées automatiquement.

**Documents PDF** : le lien « planning » de l'ancien site pointait sur le
**Planning 2025/2026** (`wp-content/uploads/2025/10/Planing.pdf`). Le PDF du
site refait est régénéré à partir du visuel **2026-2027** envoyé par la cliente :

```python
from PIL import Image
im = Image.open('_mails/extracted/Planning/PLANNING 2026-2027.png').convert('RGB')
# ... centrage sur une page A4 150 dpi (1240x1754) ...
page.save('assets/docs/planning.pdf', 'PDF', resolution=150.0)
```

Le `tarifs.pdf` provient toujours de l'ancien site
(`wp-content/uploads/2025/07/Tarifs.pdf`) : **millésime à faire confirmer**.

**Page planning** : le tableau HTML + le bouton de téléchargement suffisent.
La section « version imprimable » qui réaffichait le visuel a été retirée
(doublon), ainsi que `assets/img/planning-2026-2027.jpg`.

**Les 12 pièces jointes « disciplines »** du mail sont des **cartes de texte**
(75 à 90 % de blanc pur, saturation quasi nulle), pas des photos. Leur contenu
est intégralement retranscrit en HTML : les republier ferait doublon, et du
texte en image serait illisible pour Google et les lecteurs d'écran.

**En attente de la cliente :**

| # | Manque | Impact |
|---|---|---|
| 1 | Photo + bio de **Laurence Lanté** | Le site annonce « 8 Professeures », il n'y en a que 7 sur la page Équipe |
| 2 | Contenu réel de la page **Event** | Page construite avec les textes events de l'accueil, faute de mieux |
| 3 | **Numéro de téléphone** du studio | Introuvable sur l'ancien site et dans les mails ; seul l'e-mail est affiché |
| 4 | Fiches des disciplines manquantes | La cliente a fourni 12 fiches ; l'accueil en cite d'autres (Yoga Kundalini, Yoga Nidra, Bain Sonore, Pilates Reformer, coaching danseur préprofessionnel) |
| 5 | Confirmation de la **grille tarifaire** | Le PDF vient de l'ancien site (déposé en 07/2025), comme le planning périmé qui s'y trouvait |

**Décisions techniques en attente :**

- **Formulaire de contact** : GitHub Pages n'envoie pas de mail. Actuellement
  `main.js` ouvre le client mail du visiteur (`mailto:`). Pour un envoi direct,
  renseigner l'attribut `action` du `<form id="contact-form">` avec un service
  (Formspree, Netlify Forms…) — le JS se désactive tout seul dans ce cas.
- **Hébergement final** : GitHub Pages n'est qu'un aperçu. À la bascule sur
  `les2ailes.fr`, prévoir : retirer le `noindex` de `_build/common.py`, remplacer
  `robots.txt` (modèle en commentaire dans le fichier), vérifier `sitemap.xml`,
  et décider du plan de redirections depuis les anciennes URL WordPress
  (`/les-disciplines/`, `/les-professionnels/`, `/le-centre-de-formation/`…)
  vers les nouveaux fichiers `.html`.
