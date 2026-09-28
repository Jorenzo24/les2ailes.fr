# Mise en ligne sur le serveur cPanel

Mode opératoire pour remplacer le WordPress de `www.les2ailes.fr` par ce site
statique. À suivre dans l'ordre.

---

## Ce qui a été constaté (28 septembre 2026)

| | |
|---|---|
| Hébergement actuel | OVH mutualisé, `cluster130.hosting.ovh.net`, IP `145.239.37.162`, Apache + PHP 7.4 |
| Zone DNS | Gérée par OVH (`dns111.ovh.net`, `ns111.ovh.net`) |
| TTL des enregistrements A | 3600 s (1 heure) |
| Canonique | `les2ailes.fr` redirige en 301 vers `www.les2ailes.fr` |
| **Mails** | **MX OVH actifs** (`mx1/mx2/mx3.mail.ovh.net`) + SPF `include:mx.ovh.com` |
| Sitemap WordPress | 8 pages seulement, plus une page auteur |

### ⚠️ Les deux pièges de cette migration

1. **Il y a des mails sur le domaine.** On migre le web, pas la messagerie.
   Ne toucher qu'aux enregistrements **A** de `les2ailes.fr` et `www`.
   Ne **jamais** changer les serveurs de noms, ni les MX, ni le SPF.
2. **Chez OVH, la messagerie est souvent liée au pack d'hébergement web.**
   Avant de résilier quoi que ce soit chez OVH, vérifier dans le manager si
   les adresses @les2ailes.fr dépendent de l'hébergement ou d'un MX Plan
   séparé. En cas de doute, **garder l'hébergement OVH** : il ne servira plus
   à rien pour le web mais gardera les mails en vie.

---

## Phase 0 — Avant de toucher à quoi que ce soit

- [ ] **Sauvegarder le WordPress** : fichiers + base, depuis le manager OVH.
      Même si on ne le garde pas, c'est le seul retour arrière possible.
- [ ] Récupérer les accès : manager OVH, Search Console, fiche Google Business.
- [ ] Lister les adresses mail @les2ailes.fr existantes (manager OVH → Emails).
- [ ] Vérifier qui est titulaire du domaine et qu'on peut modifier la zone DNS.

---

## Phase 1 — Préparer le serveur cPanel

- [ ] Créer le compte cPanel pour `les2ailes.fr`.
- [ ] Noter l'utilisateur cPanel, puis **remplacer `<UTILISATEUR_CPANEL>`**
      dans `.cpanel.yml` (ligne `DEPLOYPATH`), committer et pousser.
- [ ] cPanel → **Git Version Control** → Create :
      - Clone URL : `https://github.com/Jorenzo24/les2ailes.fr.git`
      - Repository Path : `/home/<UTILISATEUR_CPANEL>/repositories/les2ailes.fr`
      - Branche : `main`
- [ ] Cliquer **Update from Remote** puis **Deploy HEAD Commit**.
- [ ] Vérifier que `public_html/` contient bien `index.html`, `assets/`,
      les 5 dossiers de pages, `.htaccess`, `robots.txt`, `sitemap.xml`.

> Le dépôt contient `_build/` et `_mails/` : ils ne sont pas copiés par
> `.cpanel.yml`, et le `.htaccess` les bloque de toute façon.

---

## Phase 2 — Tout tester avant de toucher au DNS

C'est l'intérêt de faire la bascule dans ce sens : on valide le site sur le
nouveau serveur pendant que l'ancien tourne encore.

Sur le Mac, ajouter temporairement dans `/etc/hosts` :

```
sudo nano /etc/hosts
# ajouter, avec l'IP du serveur cPanel :
<IP_SERVEUR_CPANEL>   les2ailes.fr www.les2ailes.fr
sudo dscacheutil -flushcache
```

- [ ] Parcourir les 6 pages, tester le menu, le carrousel d'avis, la galerie,
      le formulaire, les deux PDF.
- [ ] Vérifier les redirections (voir le tableau plus bas).
- [ ] **Retirer la ligne de `/etc/hosts`** une fois terminé.

---

## Phase 3 — Bascule

- [ ] **La veille** : dans la zone DNS OVH, passer le TTL des enregistrements
      `A` de `les2ailes.fr` et `www` à **300 s**. La bascule du lendemain sera
      quasi instantanée au lieu d'une heure.
- [ ] Passer le site en production :
      ```bash
      # dans _build/common.py : PROD = False  ->  PROD = True
      cd _build && python3 build_all.py
      cd .. && git add -A && git commit -m "Mise en production" && git push
      ```
      Cela retire le `noindex` de toutes les pages, ouvre `robots.txt` et
      génère le sitemap sur `https://www.les2ailes.fr`.
- [ ] Déployer dans cPanel (Update from Remote + Deploy HEAD Commit).
- [ ] Dans la zone DNS OVH, **modifier uniquement** :
      - `les2ailes.fr.  A  <IP_SERVEUR_CPANEL>`
      - `www.           A  <IP_SERVEUR_CPANEL>`
      Ne pas toucher aux MX, au SPF, ni aux serveurs de noms.
- [ ] Attendre la propagation (`dig +short www.les2ailes.fr` doit renvoyer la
      nouvelle IP), puis lancer **AutoSSL** dans cPanel pour le certificat.
      Tant que le certificat n'est pas émis, le site sera en erreur HTTPS :
      c'est normal, c'est une question de minutes.
- [ ] Remettre le TTL à 3600 une fois que tout est stable.

---

## Phase 4 — Après la bascule

- [ ] Vérifier toutes les redirections (tableau ci-dessous).
- [ ] Search Console : soumettre `https://www.les2ailes.fr/sitemap.xml`,
      supprimer l'ancien `wp-sitemap.xml`, demander l'indexation des 6 pages.
- [ ] Surveiller le rapport de couverture pendant 2 à 3 semaines.
- [ ] **Ne rien résilier chez OVH avant un mois**, et surtout pas avant
      d'avoir tranché la question des mails (voir les pièges plus haut).

---

## Les redirections

L'essentiel du travail a été fait en amont : **les URL du nouveau site sont
identiques à celles du WordPress**. Sur les 8 pages du sitemap, 6 ne bougent
pas du tout.

| Ancienne URL | Devient | Règle |
|---|---|---|
| `/` | `/` | aucune |
| `/les-disciplines/` | identique | aucune |
| `/les-professionnels/` | identique | aucune |
| `/le-centre-de-formation/` | identique | aucune |
| `/event/` | identique | aucune |
| `/contact/` | identique | aucune |
| `/planning/` | `/assets/docs/planning.pdf` | 301 |
| `/tarifs/` | `/assets/docs/tarifs.pdf` | 301 |
| `/author/admin3742/` | `/` | 301 |
| `/wp-content/uploads/2025/10/Planing.pdf` | `/assets/docs/planning.pdf` | 301 |
| `/wp-content/uploads/2025/07/Tarifs.pdf` | `/assets/docs/tarifs.pdf` | 301 |
| `/wp-content/uploads/**/<image>.jpg` | `/assets/img/…` | 301, 21 motifs |
| `/wp-admin/`, `/wp-login.php`, `/feed/`, `/category/`… | — | **410 Gone** |

Le 410 sur les reliquats WordPress est volontaire : Google désindexe plus vite
qu'avec un 404 et arrête de repasser dessus.

### Vérifier après la bascule

```bash
for u in "" les-disciplines/ les-professionnels/ le-centre-de-formation/ \
         event/ contact/ planning/ tarifs/ author/admin3742/ \
         wp-content/uploads/2025/07/Tarifs.pdf wp-login.php feed/ \
         assets/docs/planning.pdf assets/docs/tarifs.pdf page-qui-nexiste-pas/; do
  printf "%-45s %s  %s\n" "/$u" \
    "$(curl -s -o /dev/null -w '%{http_code}' "https://www.les2ailes.fr/$u")" \
    "$(curl -s -o /dev/null -w '%{redirect_url}' "https://www.les2ailes.fr/$u")"
done
```

Résultats attendus : `200` sur les 6 pages et les 2 PDF, `301` vers le bon PDF
pour `/planning/` et `/tarifs/`, `410` sur les URL WordPress, `404` sur
l'URL bidon.

```bash
# Le domaine nu doit rediriger vers www, et non l'inverse
curl -sI https://les2ailes.fr/ | head -3
# Plus aucun noindex en production
curl -s https://www.les2ailes.fr/ | grep -c noindex   # doit renvoyer 0
```

---

## Reste à régler avant ou juste après la mise en ligne

1. **Le formulaire de contact n'envoie pas de mail.** Il ouvre le logiciel de
   messagerie du visiteur. Sur un hébergement cPanel, deux options : brancher
   un service (Formspree) en renseignant l'attribut `action` du
   `<form id="contact-form">`, ou écrire un petit `contact.php`. Le JavaScript
   se désactive tout seul dès qu'un `action` est présent.
2. **Contenus encore en attente de la cliente** : nouvelles dates des modules
   de formation, photo des ateliers, PDF et liste des évènements.
3. **Google Business Profile** : vérifier que le lien du site pointe bien sur
   `https://www.les2ailes.fr/` et pas sur une ancienne URL.
