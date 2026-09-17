# 35 — Remplissage partiel et quantité restante

**Source :** `prototype/hyperliquid_order_lifecycle.py`.

Ce chapitre isole la quantité ouverte. le prototype conserve la quantité exécutée et le reliquat comme deux valeurs distinctes. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Confondre reliquat et volume total produit des réconciliations fausses. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Annulation et course avec l’exécution](36-hyperliquid-order-cancel.md)._
