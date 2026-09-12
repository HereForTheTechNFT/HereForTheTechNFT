# FHE : handles chiffrés et frontières de confiance

Dans une application FHE, un handle chiffré représente une valeur dont le calcul peut rester confidentiel. Le handle n'est pas automatiquement une preuve de validité : son origine, son type et son état doivent être contrôlés.

Les opérations homomorphes préservent la confidentialité sous les hypothèses du schéma, mais le système complet ajoute des dépendances : gestion des clés, autorisation d'accès, coprocessor, gateway et déchiffrement final.

Une analyse sérieuse distingue le contrat, le service de calcul et le KMS. Elle documente les erreurs, la révocation, les limites de bruit et les conditions dans lesquelles une sortie peut être révélée.

La confidentialité cryptographique ne supprime donc pas les choix de gouvernance : elle déplace la frontière de confiance vers les clés, les ACL et les composants d'exécution.
