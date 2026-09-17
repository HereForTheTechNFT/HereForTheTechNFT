# 06 — Domaine d’une passkey

**Source :** `prototype/base_passkey_replay.py`.

Ce chapitre isole la vérification du domaine. le domaine fait partie du contexte vérifié afin de distinguer une application de confiance d’une autre. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une signature correcte cryptographiquement peut rester dangereuse si son domaine est mal interprété. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Compteur et unicité des défis](07-base-passkey-compteur.md)._
