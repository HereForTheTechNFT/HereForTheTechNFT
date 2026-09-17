# 13 — Finalité et fenêtre de réconciliation

**Source :** `prototype/base_bridge_reconciliation.py`.

Ce chapitre isole la distinction entre en attente et finalisé. le prototype sépare l’observation provisoire de l’état final avant de conclure. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Confondre inclusion et finalité peut exposer des soldes prématurément. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Frontière HyperEVM et HyperCore](14-hyperevm-boundary.md)._
