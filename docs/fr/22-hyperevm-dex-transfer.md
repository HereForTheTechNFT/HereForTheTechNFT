# 22 — Transfert entre DEX sur HyperEVM

**Source :** `prototype/hyperevm_dex_transfer.py`.

Ce chapitre isole le transfert inter-DEX. le prototype ordonne la sortie d’un marché, le déplacement de l’actif et son entrée dans le marché suivant. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Chaque étape doit être associée à un état observable pour éviter de compter deux fois le même actif. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Devis et slippage d’un transfert DEX](23-hyperevm-dex-quote.md)._
