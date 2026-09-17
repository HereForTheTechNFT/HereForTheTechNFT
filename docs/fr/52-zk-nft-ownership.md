# 52 — Preuve de propriété NFT

**Source :** `prototype/zk_nft_replay.py`.

Ce chapitre isole la propriété comme assertion. le prototype distingue la possession revendiquée de la preuve vérifiée par le contrat. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un cache d’ownership périmé ne doit pas être utilisé comme autorité. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Transfert et changement de contexte NFT](53-zk-nft-transfer.md)._
