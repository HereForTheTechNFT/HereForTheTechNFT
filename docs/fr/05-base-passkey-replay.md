# 05 — Passkeys et anti-rejeu sur Base

**Source :** `prototype/base_passkey_replay.py`.

Ce chapitre isole la liaison d’une autorisation à un défi. le prototype associe l’intention signée à un défi et à un domaine précis avant validation. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Réutiliser un défi ou ignorer le domaine permettrait de rejouer une autorisation ailleurs. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Domaine d’une passkey](06-base-passkey-domaine.md)._
