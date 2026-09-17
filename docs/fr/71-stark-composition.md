# 71 — Composition de contraintes STARK

**Source :** `prototype/stark_air.py`.

Ce chapitre isole la composition des contraintes. plusieurs contraintes sont réunies en une relation vérifiable en conservant leurs poids et leur domaine. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une composition mal bornée peut masquer une contrainte absente derrière un polynôme nul. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Transcript et défis FRI](72-fri-transcript.md)._
