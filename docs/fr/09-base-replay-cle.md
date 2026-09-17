# 09 — Clé de replay et séparation des actions

**Source :** `prototype/base_replay_guard.py`.

Ce chapitre isole la construction de la clé. la clé combine le type d’action et son identifiant pour éviter qu’un nonce d’un flux ne valide un autre flux. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une clé trop courte crée des collisions entre mint, transfert ou retrait. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Échec et conservation de l’état anti-rejeu](10-base-replay-echec.md)._
