# 12 — Idempotence d’un message de bridge

**Source :** `prototype/base_bridge_reconciliation.py`.

Ce chapitre isole la déduplication d’un message. un identifiant stable permet de rejouer l’observation sans créer deux crédits applicatifs. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** L’idempotence doit couvrir les retries du relayer et les reprises après interruption. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Finalité et fenêtre de réconciliation](13-base-bridge-finalite.md)._
