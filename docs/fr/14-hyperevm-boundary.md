# 14 — Frontière HyperEVM et HyperCore

**Source :** `prototype/hyperevm_core_boundary.py`.

Ce chapitre isole la séparation des états. les données EVM et Core sont modélisées comme deux espaces qui nécessitent un pont explicite. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une lecture implicite de l’autre couche rend les invariants difficiles à défendre. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Lecture contextualisée d’un état HyperCore](15-hyperevm-boundary-lecture.md)._
