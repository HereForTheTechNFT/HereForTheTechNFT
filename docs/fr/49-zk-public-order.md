# 49 — Ordre canonique des entrées publiques

**Source :** `prototype/zk_public_input_binding.py`.

Ce chapitre isole l’ordre des champs. la représentation canonique évite que deux encodages décrivent des messages différents. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Les conversions implicites de tableaux ou d’entiers sont une source classique de désaccord. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Domaine de vérification ZK](50-zk-public-domain.md)._
