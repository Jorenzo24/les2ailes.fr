# les2ailes.fr — LES 2 L

Refonte du site du studio **Les2L** (Pilates · Yoga · Ballet), 228 Chemin de Pagadoy, 64990 Mouguerre.

Site statique : HTML + CSS + un fichier JavaScript, aucune dépendance à installer.
Hébergé pour l'instant sur GitHub Pages en aperçu.

## Contenu

| Fichier | Page |
|---|---|
| `index.html` | Accueil |
| `disciplines.html` | Les disciplines (12 fiches) |
| `equipe.html` | L'équipe |
| `planning.html` | Planning 2026-2027 |
| `tarifs.html` | Tarifs et abonnements |
| `event.html` | Event |
| `contact.html` | Contact |
| `centre-de-formation.html` | Centre de formation professionnelle |
| `404.html` | Page d'erreur |

## Organisation

```
assets/css/style.css     feuille de style unique
assets/js/main.js        menu mobile, galerie, apparitions au défilement
assets/img/              photos du site, portraits de l'équipe (N&B), planning
assets/docs/             tarifs.pdf, planning.pdf
_build/                  scripts Python qui génèrent les pages HTML
```

### Regénérer les pages

Les pages HTML sont générées depuis `_build/` pour garder en-tête, pied de page
et métadonnées identiques partout.

```bash
cd _build
for f in build_*.py; do python3 "$f"; done
```

Modifier un texte : éditer le script correspondant dans `_build/`, puis relancer la commande.
(Il est aussi possible d'éditer directement le HTML, mais la modification sera écrasée
à la prochaine génération.)

## Charte

| | |
|---|---|
| Bleu marine | `#062c5a` |
| Prune | `#864c80` |
| Titres et textes | EB Garamond |
| Accents manuscrits | Alex Brush |

## Avant la mise en ligne sur le domaine définitif

1. Retirer `<meta name="robots" content="noindex, nofollow">` dans `_build/common.py`, puis regénérer.
2. Remplacer le contenu de `robots.txt` (le modèle est en commentaire dans le fichier).
3. Vérifier les `<loc>` de `sitemap.xml`.
4. Brancher le formulaire de contact sur un service d'envoi (Formspree, Netlify Forms…) :
   renseigner l'attribut `action` du `<form id="contact-form">`. Sans `action`, le
   formulaire ouvre le client mail du visiteur.
