# 32 — Ordonnancement des demandes Hyperliquid

**Source :** `prototype/hyperliquid_nonce.py`.

Ce chapitre isole la relation entre ordre et nonce. le prototype distingue l’ordre logique des demandes de la date de réception. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un client doit savoir si un nonce est consommé, rejeté ou encore réessayable. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Rejeu et fenêtre de validité](33-hyperliquid-nonce-replay.md)._
