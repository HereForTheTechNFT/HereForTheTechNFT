# 30 — Échec du coprocessseur et ACL

**Source :** `prototype/fhe_acl_lifecycle.py`.

Ce chapitre isole la conservation de l’autorité après erreur. le flux sépare l’échec de calcul de l’état d’autorisation lui-même. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une erreur de calcul ne doit ni accorder un accès ni effacer une révocation. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Nonce et domaine Hyperliquid](31-hyperliquid-nonce.md)._
