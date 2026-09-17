# 10 — Échec et conservation de l’état anti-rejeu

**Source :** `prototype/base_replay_guard.py`.

Ce chapitre isole le comportement après erreur. le prototype documente le point où l’état doit rester inchangé lorsqu’une validation échoue. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Marquer trop tôt un identifiant peut provoquer un déni de service ; trop tard, un double traitement. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Réconciliation d’un bridge Base](11-base-bridge-reconciliation.md)._
