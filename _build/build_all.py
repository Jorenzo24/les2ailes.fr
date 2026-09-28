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
