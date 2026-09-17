# 31 — Nonce et domaine Hyperliquid

**Source :** `prototype/hyperliquid_nonce.py`.

Ce chapitre isole le nonce signé. le nonce relie une demande à son émetteur et à son domaine d’exécution. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Partager un nonce entre comptes ou marchés facilite les collisions et les rejouements. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Ordonnancement des demandes Hyperliquid](32-hyperliquid-nonce-order.md)._
