# 27 — Dérivation de handles FHE

**Source :** `prototype/fhe_handle_acl.py`.

Ce chapitre isole la filiation entre handles. la dérivation conserve la relation entre une opération chiffrée et ses entrées. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Perdre cette filiation empêche de vérifier la provenance et complique la révocation. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Cycle de vie d’une ACL FHE](28-fhe-lifecycle.md)._
