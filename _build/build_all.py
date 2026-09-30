# -*- coding: utf-8 -*-
"""Régénère tout le site, plus robots.txt et sitemap.xml.

    cd _build && python3 build_all.py

Le contenu de robots.txt et du sitemap dépend de common.PROD.
"""
import glob
import os
import runpy

import common as c

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)

# --- Pages -----------------------------------------------------------------
os.chdir(ICI)
for f in sorted(glob.glob("build_*.py")):
    if f == "build_all.py":
        continue
    runpy.run_path(f, run_name="__main__")


# --- Empreinte de version sur les images ------------------------------------
# Sans ça, remplacer une photo ou une icône ne change pas son URL : Cloudflare
# continue de servir l'ancienne pendant un an. C'est ce qui est arrivé à
# l'icône des évaluations, corrigée mais toujours blanche en ligne.
import hashlib
import re

_EMPREINTES = {}


def _empreinte(chemin_disque):
    if chemin_disque not in _EMPREINTES:
        try:
            with open(chemin_disque, "rb") as f:
                _EMPREINTES[chemin_disque] = hashlib.md5(f.read()).hexdigest()[:8]
        except OSError:
            _EMPREINTES[chemin_disque] = None
    return _EMPREINTES[chemin_disque]


MOTIF = re.compile(r'((?:\.\./)*assets/img/[-\w./]+\.(?:jpg|jpeg|png|webp|svg))')
pages = glob.glob(os.path.join(RACINE, "*.html")) + glob.glob(os.path.join(RACINE, "*", "index.html"))
total = 0
for page in pages:
    dossier = os.path.dirname(page)
    html = open(page, encoding="utf-8").read()

    def remplacer(m):
        global total
        url = m.group(1)
        v = _empreinte(os.path.normpath(os.path.join(dossier, url)))
        if not v:
            return url
        total += 1
        return url + "?v=" + v

    nouveau = MOTIF.sub(remplacer, html)
    if nouveau != html:
        open(page, "w", encoding="utf-8").write(nouveau)
print("images versionnées : %d" % total)

# --- robots.txt ------------------------------------------------------------
if c.PROD:
    robots = (
        "User-agent: *\n"
        "Allow: /\n\n"
        "Disallow: /_build/\n\n"
        "Sitemap: %s/sitemap.xml\n" % c.BASE_URL
    )
else:
    robots = (
        "# Aperçu : indexation désactivée (PROD=False dans _build/common.py).\n"
        "User-agent: *\n"
        "Disallow: /\n"
    )
open(os.path.join(RACINE, "robots.txt"), "w", encoding="utf-8").write(robots)

# --- sitemap.xml -----------------------------------------------------------
PAGES = [
    ("/", "1.0"),
    ("/les-disciplines/", "0.9"),
    ("/les-professionnels/", "0.9"),
    ("/le-centre-de-formation/", "0.9"),
    ("/event/", "0.7"),
    ("/contact/", "0.8"),
]
urls = "".join(
    '  <url><loc>%s%s</loc><priority>%s</priority></url>\n' % (c.BASE_URL, p, prio)
    for p, prio in PAGES
)
sitemap = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + urls +
    "</urlset>\n"
)
open(os.path.join(RACINE, "sitemap.xml"), "w", encoding="utf-8").write(sitemap)

print("\nPROD = %s" % c.PROD)
print("robots.txt et sitemap.xml régénérés.")
