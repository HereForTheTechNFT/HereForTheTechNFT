# 69 — Classes d’erreurs d’un ordre

**Source :** `prototype/hyperliquid_order_lifecycle.py`.

Ce chapitre isole la distinction erreur définitive et transitoire. le cycle d’ordre doit classer les erreurs avant de décider entre abandon, retry ou réconciliation. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un retry automatique sur une erreur métier peut produire une action non désirée. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Curseur de réconciliation Hyperliquid](70-hyperliquid-cursor.md)._
