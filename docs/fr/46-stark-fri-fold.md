# 46 — Folding FRI

**Source :** `prototype/stark_fri.py`.

Ce chapitre isole le pliage des évaluations. le pliage combine des points selon un défi afin de réduire progressivement le domaine. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Le défi doit être imprévisible et lié au transcript pour empêcher une réponse préparée. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Requêtes FRI et chemins Merkle](47-stark-fri-query.md)._
