# 25 — Handle chiffré et référence FHE

**Source :** `prototype/fhe_handle_acl.py`.

Ce chapitre isole le handle comme référence opaque. le handle représente une valeur chiffrée sans exposer son contenu à la couche applicative. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un handle ne doit pas être traité comme une donnée publique décodable. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [ACL et droit de lecture FHE](26-fhe-acl.md)._
