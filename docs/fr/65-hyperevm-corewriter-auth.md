# 65 — Autorisation d’une action CoreWriter

**Source :** `prototype/hyperevm_corewriter.py`.

Ce chapitre isole la frontière d’autorité. l’émetteur, la précompile et l’action demandée sont vérifiés ensemble avant l’encodage. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** L’adresse de l’appelant ne doit pas être remplacée par une identité fournie dans les données. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Comptabilité d’un transfert DEX](66-hyperevm-dex-accounting.md)._
