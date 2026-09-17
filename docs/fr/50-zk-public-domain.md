# 50 — Domaine de vérification ZK

**Source :** `prototype/zk_public_input_binding.py`.

Ce chapitre isole le domaine applicatif. le transcript et le vérificateur identifient l’application ou le circuit concerné. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une preuve transportée entre domaines doit être rejetée si son contexte change. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Preuve ZK et rejeu NFT](51-zk-nft-replay.md)._
