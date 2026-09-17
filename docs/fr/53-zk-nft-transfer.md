# 53 — Transfert et changement de contexte NFT

**Source :** `prototype/zk_nft_replay.py`.

Ce chapitre isole la liaison du transfert. le message de transfert porte le contrat, le token et le destinataire attendus. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Oublier l’adresse du contrat permet des substitutions entre collections. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Entrées d’une expérience reproductible](54-reproducible-inputs.md)._
