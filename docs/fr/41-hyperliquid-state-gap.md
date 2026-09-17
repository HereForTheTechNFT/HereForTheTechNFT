# 41 — Écart d’état et diagnostic

**Source :** `prototype/hyperliquid_state_reconciliation.py`.

Ce chapitre isole la classification d’un écart. les divergences sont classées en retard, événement manquant ou contradiction. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un fallback silencieux transforme un problème de données en solde apparemment valide. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Suite](42-suite.md)._
