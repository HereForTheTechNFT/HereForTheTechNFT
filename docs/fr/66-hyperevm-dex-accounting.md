# 66 — Comptabilité d’un transfert DEX

**Source :** `prototype/hyperevm_dex_transfer.py`.

Ce chapitre isole le débit et le crédit d’un transfert. le flux conserve les montants avant et après chaque marché pour rendre le règlement rapprochable. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Les frais et arrondis doivent être comptés séparément du montant échangé. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Frontière KMS et données FHE](67-fhe-key-boundary.md)._
