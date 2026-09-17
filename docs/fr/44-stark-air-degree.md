# 44 — Degré des contraintes AIR

**Source :** `prototype/stark_air.py`.

Ce chapitre isole le degré algébrique. le degré borne la complexité de l’interpolation et influence les paramètres du protocole. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Modifier une expression sans revoir cette borne peut invalider le paramétrage annoncé. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [FRI et réduction de degré](45-stark-fri.md)._
