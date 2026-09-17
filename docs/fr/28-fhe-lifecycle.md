# 28 — Cycle de vie d’une ACL FHE

**Source :** `prototype/fhe_acl_lifecycle.py`.

Ce chapitre isole l’octroi, la révocation et l’expiration. le prototype décrit les transitions de permission comme un cycle explicite. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une révocation qui ne couvre qu’un alias laisse une ancienne capacité active. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Ordre des transitions ACL](29-fhe-lifecycle-order.md)._
