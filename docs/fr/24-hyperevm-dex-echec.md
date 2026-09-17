# 24 — Reprise après échec d’un transfert DEX

**Source :** `prototype/hyperevm_dex_transfer.py`.

Ce chapitre isole la reprise idempotente. les étapes déjà confirmées sont distinguées de celles qui peuvent être relancées. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une reprise aveugle peut effectuer un second swap ou perdre la traçabilité du premier. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Handle chiffré et référence FHE](25-fhe-handles.md)._
