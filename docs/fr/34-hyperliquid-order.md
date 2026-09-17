# 34 — Cycle de vie d’un ordre

**Source :** `prototype/hyperliquid_order_lifecycle.py`.

Ce chapitre isole les états d’un ordre. le modèle passe de la création à l’acceptation, au remplissage partiel, puis à la clôture ou l’annulation. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Les états doivent être exclusifs et leurs transitions auditables. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Remplissage partiel et quantité restante](35-hyperliquid-order-partial.md)._
