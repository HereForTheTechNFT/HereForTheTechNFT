# 07 — Compteur et unicité des défis

**Source :** `prototype/base_passkey_replay.py`.

Ce chapitre isole le compteur de défi. un compteur ou nonce monotone empêche qu’un même message soit accepté plusieurs fois. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Le stockage et la concurrence doivent conserver l’unicité même en cas d’échec partiel. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Garde anti-rejeu pour NFT](08-base-replay-guard.md)._
