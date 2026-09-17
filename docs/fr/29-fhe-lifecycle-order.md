# 29 — Ordre des transitions ACL

**Source :** `prototype/fhe_acl_lifecycle.py`.

Ce chapitre isole la monotonie des versions. chaque changement de permission est rattaché à une version ou un événement ordonné. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Les messages arrivant dans le désordre ne doivent pas réactiver une permission ancienne. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Échec du coprocessseur et ACL](30-fhe-lifecycle-failure.md)._
