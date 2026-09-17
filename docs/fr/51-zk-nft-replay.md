# 51 — Preuve ZK et rejeu NFT

**Source :** `prototype/zk_nft_replay.py`.

Ce chapitre isole l’unicité d’une action NFT. l’action protégée combine identité, token, intention et identifiant consommable. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** La connaissance d’un secret ne suffit pas à rendre l’action unique. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Preuve de propriété NFT](52-zk-nft-ownership.md)._
