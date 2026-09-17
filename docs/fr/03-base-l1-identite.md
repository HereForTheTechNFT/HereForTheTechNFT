# 03 — Identité de chaîne et séparation des réseaux

**Source :** `prototype/base_l1_context.py`.

Ce chapitre isole l’identifiant de chaîne. l’identifiant est traité comme une donnée de sécurité et non comme un simple paramètre d’affichage. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Les configurations partagées doivent refuser toute ambiguïté entre environnements. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Lecture cohérente du bloc L1](04-base-l1-bloc.md)._
