# 64 — Récupération contrôlée d’une passkey

**Source :** `prototype/base_passkey_replay.py`.

Ce chapitre isole le changement de credential. une rotation de credential doit préserver le domaine et invalider les défis associés à l’ancien contexte. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une récupération trop permissive transforme la procédure de secours en contournement. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Autorisation d’une action CoreWriter](65-hyperevm-corewriter-auth.md)._
