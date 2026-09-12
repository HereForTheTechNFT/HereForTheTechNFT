# Parcours STARK : de la trace à FRI

Un STARK commence par une trace d'exécution : chaque ligne représente un état et chaque colonne une valeur du calcul. L'AIR exprime ensuite les contraintes de transition et les contraintes de frontière.

La composition transforme ces contraintes en un polynôme dont les évaluations doivent respecter le domaine choisi. Un engagement authentifie les valeurs avant les ouvertures demandées par le vérificateur.

FRI ne prouve pas directement le calcul : il vérifie de manière probabiliste qu'un polynôme est proche d'un degré admissible. Les paramètres doivent donc être liés au niveau de sécurité visé.

Ce parcours ne remplace pas l'étude du code du prover et du verifier : il fournit une grille de lecture pour vérifier que trace, contraintes, engagement et requêtes décrivent bien le même calcul.
