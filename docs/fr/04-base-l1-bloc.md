# 04 — Lecture cohérente du bloc L1

**Source :** `prototype/base_l1_context.py`.

Ce chapitre isole la lecture du numéro de bloc. la lecture du bloc sert d’ancrage temporel pour comparer des états et produire un diagnostic reproductible. Le point important est de conserver la trace de la donnée observée, de son contexte et de la décision qui en découle.

**Point de vigilance.** Une lecture effectuée à des hauteurs différentes rend les comparaisons trompeuses. Cette note décrit le comportement lisible du prototype ; elle ne remplace ni un audit ni une exécution de tests.

_Suite : [Passkeys et anti-rejeu sur Base](05-base-passkey-replay.md)._
