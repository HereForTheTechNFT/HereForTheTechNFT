# 40 — Réconciliation de l’état Hyperliquid

**Source :** `prototype/hyperliquid_state_reconciliation.py`.

Ce chapitre isole le rapprochement local-distant. le modèle compare l’intention locale, l’accusé distant et l’état finalement observé. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un accusé de réception ne doit pas être assimilé à un état de compte final. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Écart d’état et diagnostic](41-hyperliquid-state-gap.md)._
