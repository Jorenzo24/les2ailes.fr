# -*- coding: utf-8 -*-
import common as c

html = c.head("Page introuvable — LES 2 L", "Cette page n’existe pas ou a été déplacée.", "")
html += c.header("")
html += """
<main id="main">
  <section class="section center">
    <div class="container container--narrow">
      <p class="eyebrow">Erreur 404</p>
      <h1 class="title">Cette page n’existe pas</h1>
      <div class="rule"><span></span></div>
      <p class="lead">Le lien est peut-être erroné ou la page a été déplacée.</p>
      <p style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:26px">
        <a class="btn" href="index.html">Retour à l’accueil</a>
        <a class="btn btn--ghost" href="planning.html">Voir le planning</a>
      </p>
    </div>
  </section>
</main>
"""
html += c.footer()
open("../404.html", "w", encoding="utf-8").write(html)
print("404.html ok")
