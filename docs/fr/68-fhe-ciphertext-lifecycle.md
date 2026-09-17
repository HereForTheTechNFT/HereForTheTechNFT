# 68 — Cycle de vie d’un ciphertext

**Source :** `prototype/fhe_acl_lifecycle.py`.

Ce chapitre isole la durée de vie d’une valeur chiffrée. les transitions de création, dérivation, autorisation et révocation sont documentées séparément. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** La suppression d’une référence applicative ne constitue pas à elle seule une révocation cryptographique. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Classes d’erreurs d’un ordre](69-hyperliquid-errors.md)._
