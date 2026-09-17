# 18 — Paramètres et encodage CoreWriter

**Source :** `prototype/hyperevm_corewriter.py`.

Ce chapitre isole l’encodage des paramètres. les paramètres sont traités comme un contrat d’interface, avec ordre et représentation déterministes. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une différence d’encodage entre client et précompile produit des erreurs difficiles à diagnostiquer. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Réponse et échec de CoreWriter](19-hyperevm-corewriter-reponse.md)._
