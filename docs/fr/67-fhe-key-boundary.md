# 67 — Frontière KMS et données FHE

**Source :** `prototype/fhe_handle_acl.py`.

Ce chapitre isole la séparation entre handle et clé. le handle circule dans l’application tandis que la capacité de déchiffrement reste dans une frontière dédiée. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un service qui reçoit la clé complète élargit inutilement le périmètre de confiance. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Cycle de vie d’un ciphertext](68-fhe-ciphertext-lifecycle.md)._
