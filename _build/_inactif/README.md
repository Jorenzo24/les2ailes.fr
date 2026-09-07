# Générateurs mis de côté

Décision cliente du 7 septembre 2026 : les onglets **Planning** et **Tarifs**
du menu pointent directement sur leurs PDF (`assets/docs/planning.pdf` et
`assets/docs/tarifs.pdf`), comme sur le site WordPress d'origine. Les deux
pages HTML `/planning/` et `/tarifs/` ont donc été supprimées.

Les générateurs sont conservés ici : le tableau de planning responsive et les
cartes de tarifs sont prêts à revenir en une commande si la cliente change
d'avis.

```bash
cd _build && python3 _inactif/build_planning.py   # attention : chemins relatifs à _build/
```

Ils recréeraient `planning/index.html` et `tarifs/index.html`. Il faudrait
alors remettre les deux entrées dans `NAV` (`common.py`) en `False` pour
l'ouverture dans un nouvel onglet.
