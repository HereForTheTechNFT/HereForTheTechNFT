# 38 — Idempotence des retries Hyperliquid

**Source :** `prototype/hyperliquid_retry_reconciliation.py`.

Ce chapitre isole la clé de corrélation. la clé permet de rapprocher plusieurs tentatives d’une seule intention utilisateur. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Sans corrélation, le journal surestime les ordres effectivement exécutés. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Backoff et reprise progressive](39-hyperliquid-retry-backoff.md)._
