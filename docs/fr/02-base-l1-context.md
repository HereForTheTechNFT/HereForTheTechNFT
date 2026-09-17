# 02 — Contexte L1 de Base

**Source :** `prototype/base_l1_context.py`.

Ce chapitre isole le rattachement au contexte L1. le prototype sépare les informations de chaîne, de bloc et de séquence avant de les transmettre à une application. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Un mauvais contexte peut faire accepter une preuve ou une autorisation sur le mauvais réseau. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Identité de chaîne et séparation des réseaux](03-base-l1-identite.md)._
