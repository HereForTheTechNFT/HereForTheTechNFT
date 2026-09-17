# 63 — Anti-rejeu des messages de bridge

**Source :** `prototype/base_bridge_reconciliation.py`.

Ce chapitre isole la consommation d’un message de bridge. le rapprochement doit empêcher qu’un même message source soit traité deux fois lors d’une reprise. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** La clé de déduplication doit couvrir le domaine, le message et la destination. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Récupération contrôlée d’une passkey](64-base-passkey-recovery.md)._
