# 26 — ACL et droit de lecture FHE

**Source :** `prototype/fhe_handle_acl.py`.

Ce chapitre isole la liste de contrôle d’accès. le droit est accordé à une identité précise et séparé de la simple possession du handle. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** L’accès doit être vérifié pour chaque opération sensible, y compris les dérivées. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Dérivation de handles FHE](27-fhe-handle-derive.md)._
