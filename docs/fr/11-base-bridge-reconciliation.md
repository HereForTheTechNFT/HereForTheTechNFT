# 11 — Réconciliation d’un bridge Base

**Source :** `prototype/base_bridge_reconciliation.py`.

Ce chapitre isole la comparaison des événements source et destination. le flux rapproche les messages émis, relayés et finalisés au lieu de faire confiance à un seul compteur. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Les événements manquants ou dupliqués doivent être signalés comme divergences. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Idempotence d’un message de bridge](12-base-bridge-idempotence.md)._
