# 16 — Invariant de frontière inter-couches

**Source :** `prototype/hyperevm_core_boundary.py`.

Ce chapitre isole la conservation de l’invariant. l’invariant relie le fait observé sur une couche à la représentation attendue sur l’autre. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Toute conversion doit être documentée avec ses unités, arrondis et conditions d’échec. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [CoreWriter et intention de transfert](17-hyperevm-corewriter.md)._
