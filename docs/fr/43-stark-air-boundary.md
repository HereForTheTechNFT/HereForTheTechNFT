# 43 — Bords de trace et états initiaux

**Source :** `prototype/stark_air.py`.

Ce chapitre isole les contraintes de bord. les valeurs initiales et finales complètent les contraintes de transition. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une trace localement cohérente peut rester fausse si ses ancrages ne sont pas liés au calcul attendu. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Degré des contraintes AIR](44-stark-air-degree.md)._
