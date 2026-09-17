# 23 — Devis et slippage d’un transfert DEX

**Source :** `prototype/hyperevm_dex_transfer.py`.

Ce chapitre isole la validation du devis. le devis fixe les attentes de montant, de direction et de tolérance avant l’exécution. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un devis périmé doit être refusé plutôt que remplacé silencieusement. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Reprise après échec d’un transfert DEX](24-hyperevm-dex-echec.md)._
