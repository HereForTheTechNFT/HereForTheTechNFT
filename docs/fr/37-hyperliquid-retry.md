# 37 — Retry borné pour une requête

**Source :** `prototype/hyperliquid_retry_reconciliation.py`.

Ce chapitre isole la politique de retry. le retry est limité, temporisé et lié à une classe d’erreur plutôt qu’appliqué à toute panne. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Réessayer une erreur définitive peut dupliquer une action ou saturer le service. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Idempotence des retries Hyperliquid](38-hyperliquid-retry-idempotence.md)._
