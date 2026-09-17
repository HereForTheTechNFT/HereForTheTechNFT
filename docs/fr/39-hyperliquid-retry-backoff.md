# 39 — Backoff et reprise progressive

**Source :** `prototype/hyperliquid_retry_reconciliation.py`.

Ce chapitre isole le délai progressif. les tentatives s’espacent pour laisser le temps au système distant de converger. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un backoff déterministe doit rester compatible avec la fenêtre de validité de la signature. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Réconciliation de l’état Hyperliquid](40-hyperliquid-state.md)._
