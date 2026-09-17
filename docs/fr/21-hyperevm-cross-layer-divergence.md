# 21 — Divergence et rattrapage inter-couches

**Source :** `prototype/hyperevm_cross_layer_state.py`.

Ce chapitre isole la détection de divergence. une divergence est conservée comme signal explicite et non masquée par une valeur par défaut. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Le rattrapage doit être traçable pour distinguer retard temporaire et incohérence durable. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Suite](22-suite.md)._
