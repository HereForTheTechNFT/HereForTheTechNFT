# 33 — Rejeu et fenêtre de validité

**Source :** `prototype/hyperliquid_nonce.py`.

Ce chapitre isole la fenêtre temporelle. une requête porte un contexte de validité qui limite son acceptation tardive. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une fenêtre trop large augmente le risque ; trop étroite, elle fragilise les relais lents. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Cycle de vie d’un ordre](34-hyperliquid-order.md)._
