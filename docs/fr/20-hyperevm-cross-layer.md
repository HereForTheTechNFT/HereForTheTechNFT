# 20 — État croisé HyperEVM

**Source :** `prototype/hyperevm_cross_layer_state.py`.

Ce chapitre isole la synchronisation d’un état croisé. le prototype compare les observations des deux couches à partir d’un instant de référence. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une synchronisation sans borne temporelle peut rapprocher des états incompatibles. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Divergence et rattrapage inter-couches](21-hyperevm-cross-layer-divergence.md)._
