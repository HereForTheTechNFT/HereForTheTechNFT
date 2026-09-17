# 70 — Curseur de réconciliation Hyperliquid

**Source :** `prototype/hyperliquid_state_reconciliation.py`.

Ce chapitre isole le curseur d’événements. le rapprochement mémorise le dernier événement traité et peut reprendre sans relire aveuglément tout l’historique. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Le curseur doit être lié au compte et au flux, jamais global à tous les marchés. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Composition de contraintes STARK](71-stark-composition.md)._
