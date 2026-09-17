# 48 — Liaison des entrées publiques ZK

**Source :** `prototype/zk_public_input_binding.py`.

Ce chapitre isole la liaison entrée-preuve. le prototype encode les entrées publiques dans le contexte vérifié de la preuve. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une preuve valide avec des entrées différentes ne doit jamais être acceptée. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Ordre canonique des entrées publiques](49-zk-public-order.md)._
