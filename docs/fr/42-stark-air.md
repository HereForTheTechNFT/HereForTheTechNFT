# 42 — AIR : contraintes sur une trace STARK

**Source :** `prototype/stark_air.py`.

Ce chapitre isole les contraintes AIR. la trace est décrite comme une suite d’états soumis à des relations locales vérifiables. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une contrainte oubliée laisse une transition invalide hors du contrôle du vérificateur. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Bords de trace et états initiaux](43-stark-air-boundary.md)._
