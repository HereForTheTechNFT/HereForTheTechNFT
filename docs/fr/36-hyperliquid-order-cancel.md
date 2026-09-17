# 36 — Annulation et course avec l’exécution

**Source :** `prototype/hyperliquid_order_lifecycle.py`.

Ce chapitre isole la course entre cancel et fill. l’état final dépend de l’ordre observé des événements et doit être expliqué. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une interface ne doit pas annoncer une annulation certaine avant le règlement du dernier événement. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Retry borné pour une requête](37-hyperliquid-retry.md)._
