# 47 — Requêtes FRI et chemins Merkle

**Source :** `prototype/stark_fri.py`.

Ce chapitre isole la vérification d’une requête. une requête emporte une évaluation et les preuves de chemin nécessaires à l’engagement. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un chemin mal indexé peut faire vérifier une valeur appartenant à une autre position. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Liaison des entrées publiques ZK](48-zk-public-input.md)._
