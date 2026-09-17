# 17 — CoreWriter et intention de transfert

**Source :** `prototype/hyperevm_corewriter.py`.

Ce chapitre isole la construction d’une intention CoreWriter. le prototype prépare explicitement l’action demandée avant son envoi vers HyperCore. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une intention mal formée peut être valide au niveau transactionnel mais fausse au niveau métier. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Paramètres et encodage CoreWriter](18-hyperevm-corewriter-parametres.md)._
