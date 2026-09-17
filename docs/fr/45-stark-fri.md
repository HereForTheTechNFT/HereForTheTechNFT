# 45 — FRI et réduction de degré

**Source :** `prototype/stark_fri.py`.

Ce chapitre isole la réduction de degré. FRI transforme un polynôme supposé bas degré en engagements successifs plus petits. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** La réduction ne prouve rien seule : elle dépend des ouvertures et des vérifications de cohérence. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Folding FRI](46-stark-fri-fold.md)._
