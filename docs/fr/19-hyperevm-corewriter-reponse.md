# 19 — Réponse et échec de CoreWriter

**Source :** `prototype/hyperevm_corewriter.py`.

Ce chapitre isole la lecture de la réponse. le flux conserve la distinction entre appel accepté, exécution effective et erreur retournée. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Ne pas vérifier la réponse crée une illusion de règlement. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [État croisé HyperEVM](20-hyperevm-cross-layer.md)._
