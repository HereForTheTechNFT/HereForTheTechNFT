# 08 — Garde anti-rejeu pour NFT

**Source :** `prototype/base_replay_guard.py`.

Ce chapitre isole la consommation d’un identifiant. le garde mémorise les identifiants déjà consommés avant d’autoriser l’action protégée. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** La vérification seule ne suffit pas si la consommation n’est pas atomique. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Clé de replay et séparation des actions](09-base-replay-cle.md)._
